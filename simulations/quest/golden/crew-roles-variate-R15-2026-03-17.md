---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 15
rubric: crew-roles-rubric-v9-2026-03-17.md
---

# crew-roles -- Variate R15

5 complete prompt body variations for the `crew-roles` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

**Baseline**: R14 all-three-combined. No single R14 variation contained all three v9 mechanisms:
R14 V-04 = C-30 + C-31 (inertia-first + vocab binding, no inline LENS AUDIT). R14 V-05 = C-31 +
C-32 (vocab binding + inline LENS AUDIT, no inertia-first gate). R15 baseline synthesizes all three
before varying: Phase 5 planning table has Planned-Vocab-Term column; Phase 6 writes
inertia-advocate first with INERTIA-ADVOCATE WRITTEN gate, then writes other roles each with inline
LENS AUDIT; Phase 7 CHECK 4 splits into 4A (set coverage) + 4B (plan-to-write binding).

**Gaps identified in R14 all-combined against v9 criteria**:

- **Gap-A -- No perspective diversity gate (C-08)**: Phase 5 planning table has a Perspective
  column (product / technical / inertia / domain). Phase 6 instructs "minimum 3 roles; at least 3
  distinct perspective categories." But Phase 7 has no named CHECK auditing the Perspective column
  for >= 3 distinct values. CHECK 3A (scope gradient, >= 2 distinct scope values) has an explicit
  structural gate and emits `SCOPE AUDIT PASS`; perspective diversity has no equivalent gate. A
  registry with two `product` roles, one `inertia` role, and no `technical` or `domain` role passes
  all Phase 7 checks unchallenged. The sufficient fix is a PERSPECTIVE AUDIT in Phase 5 and CHECK 8
  in Phase 7, structurally analogous to SCOPE AUDIT + CHECK 3A.

- **Gap-B -- Source phrase provenance not traced to Phase 1 in FRAME FILL (C-25 / C-27)**:
  Phase 3 FRAME FILL traces from CONVERGENCE SUMMARY Q-FINAL answers to the frame template slots.
  The format is `Q{N} slot <- Q{N}-FINAL: [verbatim answer]`. C-25 requires "frame-slot source
  citation"; C-27 requires "source-phrase forensic citation." Both criteria demand that the citation
  reach back to the Phase 1 source phrase that grounded each Q-FINAL term -- not just to the
  CONVERGENCE SUMMARY answer. The Phase 1 vocabulary table carries a source phrase per row
  (`[CS-1] {term}: "{source phrase from input}"`). FRAME FILL never cites these. The provenance
  chain breaks one step before the input text. A `Phase 1 source:` citation line per slot in
  FRAME FILL closes the gap; a CHECK 5B gate in Phase 7 confirms each slot's Phase 1 row is
  present and verifiable.

- **Gap-C -- Role replacement re-audit is ad hoc (C-24)**: When CHECK 3B (scope binding) or CHECK
  4B (vocab binding) flags a mismatch, the current instruction is "rewrite file to match plan, or
  return to Phase 5 with justification." C-24 requires "audit-table full re-evaluation after
  replacement" -- meaning each flagged role produces a documented replacement event, a re-evaluation
  of its audit-table row, and a ROLE-REPLACE CONFIRMED signal before the CHECK closes. The current
  instruction allows silent rewriting with no confirmation artifact. A formalized ROLE-REPLACE
  sub-procedure triggered at every CHECK 3B / 4B mismatch closes C-24 without disrupting the
  happy-path flow.

**R15 variation axes**:
- V-01 (single): Perspective diversity gate -- Phase 5 PERSPECTIVE AUDIT + Phase 7 CHECK 8
- V-02 (single): Source phrase forensic citation -- Phase 3 FRAME FILL traces to Phase 1 rows;
  Phase 7 CHECK 5 splits into 5A (frame match) + 5B (source citations)
- V-03 (single): Role replacement re-audit -- formalized ROLE-REPLACE sub-procedure triggered by
  every CHECK 3B / CHECK 4B mismatch, producing a confirmed replacement artifact
- V-04 (combined): V-01 + V-02 (perspective gate + source phrase citation)
- V-05 (combined): V-01 + V-02 + V-03 (all three R15 axes)

---

## V-01

**Axis**: Perspective diversity gate (single axis)
**Hypothesis**: R14 all-combined (C-30 + C-31 + C-32 present) has no structural gate for
perspective diversity (C-08). CHECK 3A gates scope gradient at >= 2 distinct values and emits a
named pass signal; no equivalent gate exists for perspective categories. Phase 6 text says "at least
3 distinct perspective categories" but this is a narrative instruction -- if a model assigns two
roles to `product` without noticing, no Phase 7 check fires. Adding a PERSPECTIVE AUDIT immediately
after the SCOPE AUDIT in Phase 5, and CHECK 8 in Phase 7, creates the equivalent structural gate:
distinct perspective values listed, gate at >= 3, `PERSPECTIVE AUDIT PASS` required before Phase 6
opens. CHECK 8 re-verifies from written files. Single-axis: all other mechanisms unchanged.

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

Read the input. Extract domain terms and assign each to exactly one of three named buckets:

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

**Exit condition met**: three non-empty buckets; each term has row identifier; minimum 3 terms.

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

Phase 3 and Phase 6 consume from CONVERGENCE SUMMARY only.

**Exit condition met**: convergence declared; CONVERGENCE SUMMARY present.

---

### Phase 3 -- FRAME FILL

**Entry**: Phase 2 complete (CONVERGENCE SUMMARY present)
**Exit**: completed frame string written; all slot-binding checks YES

```
## Frame Fill

Q1 slot <- Q1-FINAL: [verbatim Q1-FINAL answer]
Q2 slot <- Q2-FINAL: [verbatim Q2-FINAL answer]
Q3 slot <- Q3-FINAL: [verbatim Q3-FINAL answer]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

Slot-binding: Q1<-Q1-FINAL, Q2<-Q2-FINAL, Q3<-Q3-FINAL -- all YES. Cross-slot binding is a
blocking error.

**Exit condition met**: completed frame written; all slot-binding checks YES.

---

### Phase 4 -- FRAME CONFIRM

**Entry**: Phase 3 complete
**Exit**: FRAME CONFIRM present with verbatim Phase 3 paste

```
## Frame Confirm

FRAME CONFIRM: The inertia-advocate orientation.frame I will write first in Phase 6 is:
"{paste Phase 3 completed frame string -- character-for-character, including all punctuation}"
```

If you cannot reproduce the Phase 3 output exactly, return to Phase 3 and regenerate.

**Exit condition met**: FRAME CONFIRM present with verbatim Phase 3 paste.

---

### Phase 5 -- PRE-WRITE SCOPE + PERSPECTIVE + VOCAB AUDIT

**Entry**: Phase 4 complete
**Exit**: planning table shows >= 2 distinct scope values AND >= 3 distinct perspective categories;
         each role has Planned-Vocab-Term assigned; SCOPE AUDIT PASS, PERSPECTIVE AUDIT PASS, and
         VOCAB PLAN COMPLETE all declared

| Planned Role        | Perspective | Scope      | Planned-Vocab-Term | Justification           |
|---------------------|-------------|------------|--------------------|-------------------------|
| inertia-advocate    | inertia     | cross-team | {CS-N}: {term}     | Q1-FINAL anchor         |
| pm                  | product     | {scope}    | {X-N}: {term}      | {one reason from input} |
| architect           | technical   | {scope}    | {X-N}: {term}      | {one reason from input} |
| {domain-specialist} | domain      | {scope}    | {X-N}: {term}      | from Phase 1 vocabulary |

Add domain-specialist rows as needed. Scope values: `team`, `cross-team`, `org`.
Planned-Vocab-Term must be a Phase 1 row identifier + term. Each role selects a distinct term
where possible; if two roles share a term, note the overlap in Justification.

**SCOPE AUDIT**: List distinct scope values from table. Gate: >= 2 distinct values.
If only 1: revise 1-2 roles. State changes. Confirm count >= 2.
`SCOPE AUDIT PASS -- scope values: [list]`

**PERSPECTIVE AUDIT**: List distinct perspective values from table. Gate: >= 3 distinct values.
If < 3: add a role or re-assign an existing role's perspective to reach >= 3. State changes.
`PERSPECTIVE AUDIT PASS -- perspectives: [list]`

Scope and Planned-Vocab-Term values in this table are binding for Phase 6. Writing blocked until
both SCOPE AUDIT PASS and PERSPECTIVE AUDIT PASS are declared.

**Exit condition met**: >= 2 distinct scope values; >= 3 distinct perspective categories;
each role has Planned-Vocab-Term; both audits declared PASS.

---

### Phase 6 -- WRITE ROLE FILES (INERTIA-ADVOCATE FIRST, INLINE LENS AUDIT)

**Entry**: Phase 5 complete (both audits passed)
**Exit**: all role files written; inertia-advocate written first and gate passed; every role has
         LENS AUDIT PASS declared; frame matches Phase 4; annotations 5-mode-valid with terms in
         question bodies; every expertise.relevance references a Phase 1 term; scope matches Phase 5

Write each role to `.roles/{area}/{role-slug}.md`. **Write the inertia-advocate first.**
After writing each role's orientation fields, immediately run LENS AUDIT before proceeding.

**Step 1 -- Write inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use the FRAME CONFIRM string from Phase 4 verbatim
- `orientation.verify`: exactly 3 questions; BOTH conditions required per question:
  1. Carries annotation: `{question?} [Q: QN -- vocab: {row-id} -- {term-from-QN-FINAL}]`
  2. Question text body contains annotation `{term}` verbatim as substring
- `orientation.simplify`: 2+ imperatives
- `expertise.relevance`: Q1-FINAL row identifier + at least one other Phase 1 term
- `scope`: cross-team; `collaborates_with`: pm

**LENS AUDIT -- inertia-advocate** (run after writing orientation fields):

```
LENS AUDIT -- inertia-advocate:

verify items:
  [1] "{item}" -- ends in ? YES/NO
  [2] "{item}" -- ends in ? YES/NO
  [3] "{item}" -- ends in ? YES/NO

simplify items:
  [1] "{item}" -- begins with imperative verb? YES/NO
  [2] "{item}" -- begins with imperative verb? YES/NO
```

For each NO: emit `[inertia-advocate verify item {N}: "{item}" -- MISSING ? TERMINATOR]` or
`[inertia-advocate simplify item {N}: "{item}" -- NOT AN IMPERATIVE]`. Rewrite before proceeding.
`LENS AUDIT inertia-advocate: PASS` or `LENS AUDIT inertia-advocate: FAIL -- [rewrites made]`

**Step 2 -- Confirm inertia-advocate written**:
```
INERTIA-ADVOCATE WRITTEN:
  (1) File written: YES/NO
  (2) Frame matches Phase 4 FRAME CONFIRM: YES/NO
  (3) Domain grounding present (named system, cost, or habit from Phase 2 in verify questions): YES/NO
```
All three YES required. Any NO: rewrite before proceeding to Step 3.
`INERTIA-ADVOCATE WRITTEN GATE: PASS` or `INERTIA-ADVOCATE WRITTEN GATE: FAIL -- [action taken]`

**Step 3 -- Write remaining roles** (pm, architect, domain-specialist(s)):

Role template:
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
relevance: {sentence referencing the Planned-Vocab-Term from Phase 5 for this role}

## scope
{value from Phase 5 planning table -- do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**LENS AUDIT** (run after writing each role's orientation fields, before writing next role):

```
LENS AUDIT -- {role-name}:

verify items:
  [{N}] "{item}" -- ends in ? YES/NO
  ...

simplify items:
  [{N}] "{item}" -- begins with imperative verb? YES/NO
  ...
```

For each NO: emit flag and rewrite before proceeding.
`LENS AUDIT {role-name}: PASS` or `LENS AUDIT {role-name}: FAIL -- [rewrites made]`

Do not write the next role until LENS AUDIT PASS is declared for the current role.

**Exit condition met**: inertia-advocate written first; INERTIA-ADVOCATE WRITTEN GATE PASS;
every role has LENS AUDIT PASS; frame matches Phase 4; annotations valid with terms in bodies;
expertise.relevance references Planned-Vocab-Term for each role; scope matches Phase 5 table.

---

### Phase 7 -- VERIFICATION GATE

**Entry**: Phase 6 complete (all LENS AUDIT PASS declared)
**Exit**: all 8 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. Complete all 8 checks in order. Each must declare PASS before the next
opens. Fix defects before proceeding.**

---

**CHECK 1 -- Registry Summary Table**

| Role | Perspective | Frame (first 8 words) | Scope | Collaborates With |
|------|-------------|----------------------|-------|-------------------|

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
For each mismatch: rewrite file to match plan, or return to Phase 5 and amend.
Gate: zero mismatches.
`CHECK 3: PASS` or `CHECK 3: FAIL -- [action taken]`

---

**CHECK 4 -- Vocabulary Coverage + Binding**

Part A -- Coverage: for each role's `expertise.relevance`, does it reference a Phase 1 term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise. Gate: all pass.
`CHECK 4A: PASS` or `CHECK 4A: FAIL -- [revisions made]`

Part B -- Binding (after 4A PASS): compare Phase 5 Planned-Vocab-Term to Phase 6 written
expertise.relevance per role:

| Role | Phase 5 Planned Vocab | Phase 6 Written Vocab | Match? |
|------|-----------------------|-----------------------|--------|

Flag: `[{role}: planned vocab "{planned-term}", written vocab "{written-term}" -- VOCAB BINDING MISMATCH]`
For each mismatch: rewrite expertise.relevance to use planned term, or return to Phase 5 and amend.
Gate: zero mismatches.
`CHECK 4: PASS` or `CHECK 4: FAIL -- [action taken]`

---

**CHECK 5 -- Frame Confirm Match**

Compare the inertia-advocate `orientation.frame` against the Phase 4 FRAME CONFIRM string
character-for-character. Flag `[FRAME MISMATCH]`. Rewrite to match Phase 4 exactly.
`CHECK 5: PASS -- strings match` or `CHECK 5: FAIL -- [FRAME MISMATCH; rewritten]`

---

**CHECK 6 -- Verify-Question Vocab-Term Citation Coverage**

For each of the inertia-advocate's 3 verify questions, emit all applicable flags in order:

1. `[MISSING ANNOTATION]` -- no `[Q: QN -- vocab: ...]` tag present
2. `[Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M} dimension]`
3. `[TERM MISMATCH: annotation says "{term-A}", CONVERGENCE SUMMARY Q{N}-FINAL recorded "{term-B}"]`
4. `[ROW-ID MISMATCH: annotation says {row-A}, CONVERGENCE SUMMARY Q{N}-FINAL used {row-B}]`
5. `[TERM NOT IN QUESTION TEXT: annotation term "{term}" not found in question body]`

Each failure mode independently emitted. Gate: all 3 questions pass all 5 checks.
`CHECK 6: PASS` or `CHECK 6: FAIL -- [revisions made]`

---

**CHECK 7 -- Replacement Provenance Audit**

For each replacement recorded in Phase 2: does the record contain a Phase 1 row citation?
Flag: `Q{N} replacement "{old}" -> "{new}" [MISSING PHASE-1 CITATION]`
Gate: every replacement cites a verifiable Phase 1 row, or no replacements made.
`CHECK 7: PASS` or `CHECK 7: FAIL -- [revisions made]`

---

**CHECK 8 -- Perspective Diversity Gate** *(new in V-01)*

From the CHECK 1 registry summary table, list all distinct perspective values:

| Role | Perspective |
|------|-------------|

Distinct perspective values: [list]

Gate: >= 3 distinct perspective categories.
If < 3: add or reassign roles to reach >= 3. State action taken.
`CHECK 8: PASS -- distinct perspectives: [list]` or `CHECK 8: FAIL -- [action taken]`

---

All 8 checks declared PASS -> `GATE RESULT: PASS` -- **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(Phase 5 table updated including
>   Planned-Vocab-Term; SCOPE AUDIT + PERSPECTIVE AUDIT re-run; LENS AUDIT required; CHECK 3B +
>   CHECK 4B + CHECK 8 re-run)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2-4;
>   inertia re-written first with LENS AUDIT; term-in-body condition applies)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-02

**Axis**: Source phrase forensic citation in FRAME FILL (single axis)
**Hypothesis**: R14 all-combined Phase 3 FRAME FILL traces CONVERGENCE SUMMARY Q-FINAL answers
to frame template slots (`Q1 slot <- Q1-FINAL: [verbatim]`). This satisfies C-23 (Frame Fill as
phase-boundary artifact) but not C-25 (frame-slot source citation) or C-27 (source-phrase forensic
citation). Both criteria require the citation to reach back to the Phase 1 source phrase that
grounded the Q-FINAL term -- the verbatim string from the input that justified the term's placement
in its bucket. The Phase 1 vocabulary table already carries this string per row (`[CS-1] {term}:
"{source phrase}"`). Adding a `Phase 1 source:` line per slot in FRAME FILL extends the provenance
chain from input text through term assignment through Q-FINAL through frame fill. CHECK 5 splits
into 5A (existing frame-match check) + 5B (source citation verification). Single-axis: all other
mechanisms unchanged.

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
**Exit**: convergence declared; CONVERGENCE SUMMARY present; all blocks preserved

`Q1: [answer] [vocab: {CS-N} -- {term}]` (Current-System Terms)
`Q2: [answer] [vocab: {MC-N} -- {term}]` (Migration-Cost Terms)
`Q3: [answer] [vocab: {UH-N} -- {term}]` (User-Habit Terms)

**AUDIT ATTEMPT 1:**

| Q  | Row ID | Term Used | Expected Bucket | Match YES/NO |
|----|--------|-----------|-----------------|--------------|
| Q1 | {CS-N} | {term}    | Current-System  | YES/NO       |
| Q2 | {MC-N} | {term}    | Migration-Cost  | YES/NO       |
| Q3 | {UH-N} | {term}    | User-Habit      | YES/NO       |

ALL YES -> convergence. Any NO -> record replacement with Phase 1 citation; retry.

`AUDIT CONVERGENCE: ATTEMPT {N} ALL YES.`

```
## Convergence Summary

Q1-FINAL: [verbatim Q1 answer] [vocab: {CS-N} -- {term}]
Q2-FINAL: [verbatim Q2 answer] [vocab: {MC-N} -- {term}]
Q3-FINAL: [verbatim Q3 answer] [vocab: {UH-N} -- {term}]
```

**Exit condition met**: convergence declared; CONVERGENCE SUMMARY present.

---

### Phase 3 -- FRAME FILL WITH SOURCE PHRASE CITATIONS *(extended in V-02)*

**Entry**: Phase 2 complete
**Exit**: completed frame string written; all slot-binding checks YES; all source phrase citations
         present and traceable to Phase 1 rows

For each slot: state the Q-FINAL answer AND trace back to the Phase 1 source phrase that
grounded the term in that Q-FINAL answer.

```
## Frame Fill

Q1 slot <- Q1-FINAL: [verbatim Q1-FINAL answer]
  Phase 1 source: {CS-N} = "{source phrase from Phase 1 Current-System Terms row CS-N}"
Q2 slot <- Q2-FINAL: [verbatim Q2-FINAL answer]
  Phase 1 source: {MC-N} = "{source phrase from Phase 1 Migration-Cost Terms row MC-N}"
Q3 slot <- Q3-FINAL: [verbatim Q3-FINAL answer]
  Phase 1 source: {UH-N} = "{source phrase from Phase 1 User-Habit Terms row UH-N}"

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

If the Phase 1 source phrase for any slot cannot be located, emit:
`[SOURCE-PHRASE CITATION MISSING: slot Q{N} -- row {row-id} not found in Phase 1 vocabulary]`
Do not proceed until all three source citations are present and traceable.

Slot-binding: Q1<-Q1-FINAL, Q2<-Q2-FINAL, Q3<-Q3-FINAL -- all YES. Cross-slot blocking.

**Exit condition met**: completed frame written; slot-binding YES; all three `Phase 1 source:`
lines present with verbatim source phrases traceable to Phase 1 row identifiers.

---

### Phase 4 -- FRAME CONFIRM

**Entry**: Phase 3 complete
**Exit**: FRAME CONFIRM present with verbatim Phase 3 paste

```
## Frame Confirm

FRAME CONFIRM: The inertia-advocate orientation.frame I will write first in Phase 6 is:
"{paste Phase 3 completed frame string -- character-for-character}"
```

**Exit condition met**: FRAME CONFIRM present.

---

### Phase 5 -- PRE-WRITE SCOPE + VOCAB AUDIT

**Entry**: Phase 4 complete
**Exit**: planning table shows >= 2 distinct scope values; each role has Planned-Vocab-Term;
         SCOPE AUDIT PASS and VOCAB PLAN COMPLETE both declared

| Planned Role        | Perspective | Scope      | Planned-Vocab-Term | Justification           |
|---------------------|-------------|------------|--------------------|-------------------------|
| inertia-advocate    | inertia     | cross-team | {CS-N}: {term}     | Q1-FINAL anchor         |
| pm                  | product     | {scope}    | {X-N}: {term}      | {one reason from input} |
| architect           | technical   | {scope}    | {X-N}: {term}      | {one reason from input} |
| {domain-specialist} | domain      | {scope}    | {X-N}: {term}      | from Phase 1 vocabulary |

**SCOPE AUDIT**: Distinct scope values: [list]. Gate: >= 2. Revise if needed.
`SCOPE AUDIT PASS -- scope values: [list]`

Scope and Planned-Vocab-Term values binding for Phase 6. Writing blocked until scope audit passes.

**Exit condition met**: >= 2 distinct scope values; all roles have Planned-Vocab-Term; SCOPE AUDIT PASS.

---

### Phase 6 -- WRITE ROLE FILES (INERTIA-ADVOCATE FIRST, INLINE LENS AUDIT)

**Entry**: Phase 5 complete
**Exit**: all files written; inertia-advocate written first and gate passed; every role has
         LENS AUDIT PASS; frame matches Phase 4; annotations 5-mode-valid; expertise.relevance
         references Planned-Vocab-Term; scope matches Phase 5

Write to `.roles/{area}/{role-slug}.md`. Write inertia-advocate first.
Run LENS AUDIT after each role's orientation fields before writing the next role.

**Step 1 -- Write inertia-advocate**:
- `orientation.frame`: FRAME CONFIRM verbatim
- `orientation.verify`: 3 questions, each with annotation + term in question body
- `orientation.simplify`: 2+ imperatives
- `expertise.relevance`: Q1-FINAL row id + at least one other Phase 1 term
- `scope`: cross-team; `collaborates_with`: pm

**LENS AUDIT -- inertia-advocate**:
```
verify items: [{N}] "{item}" -- ends in ? YES/NO ...
simplify items: [{N}] "{item}" -- begins with imperative verb? YES/NO ...
```
Emit failure flags; rewrite violations before proceeding.
`LENS AUDIT inertia-advocate: PASS`

**Step 2 -- Confirm inertia-advocate written**:
```
INERTIA-ADVOCATE WRITTEN:
  (1) File written: YES/NO
  (2) Frame matches Phase 4 FRAME CONFIRM: YES/NO
  (3) Domain grounding (named system, cost, or habit from Phase 2) present: YES/NO
```
`INERTIA-ADVOCATE WRITTEN GATE: PASS` (all YES) or `FAIL -- [action taken]`

**Step 3 -- Write remaining roles**:
Template: orientation (frame, verify, simplify), expertise (depth, relevance with Planned-Vocab-Term
from Phase 5), scope (from Phase 5 -- do not change), collaborates_with.
After each role's orientation fields: run LENS AUDIT. Do not write next role until LENS AUDIT PASS.

Minimum 3 roles total; at least 3 distinct perspective categories.

---

### Phase 7 -- VERIFICATION GATE

**Entry**: Phase 6 complete
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

Part A: distinct scope values >= 2.
`CHECK 3A: PASS -- scope values: [list]`

Part B: Phase 5 planned vs Phase 6 written per role.
Flag: `[{role}: planned {A}, written {B} -- SCOPE BINDING MISMATCH]` Gate: zero mismatches.
`CHECK 3: PASS` or `CHECK 3: FAIL -- [action taken]`

---

**CHECK 4 -- Vocabulary Coverage + Binding**

Part A: all roles have vocab term in expertise.relevance. Flag `{role} [NO VOCAB TERM]`.
`CHECK 4A: PASS`

Part B: Phase 5 Planned-Vocab-Term vs Phase 6 written expertise.relevance per role.
Flag: `[{role}: planned vocab "{planned}", written vocab "{written}" -- VOCAB BINDING MISMATCH]`
Gate: zero mismatches.
`CHECK 4: PASS` or `CHECK 4: FAIL -- [action taken]`

---

**CHECK 5 -- Frame Confirm Match + Source Citation Verification** *(extended in V-02)*

Part A -- Frame match: Phase 4 FRAME CONFIRM vs Phase 6 inertia-advocate frame, char-for-char.
Flag `[FRAME MISMATCH]`. Rewrite to match Phase 4 exactly.
`CHECK 5A: PASS -- strings match` or `CHECK 5A: FAIL -- [FRAME MISMATCH; rewritten]`

Part B -- Source citation verification: For each slot in Phase 3 FRAME FILL:

| Slot | Row ID Cited | Source Phrase Present in FRAME FILL | Row ID Found in Phase 1 |
|------|--------------|-------------------------------------|------------------------|
| Q1   | {row-id}     | YES/NO                              | YES/NO                 |
| Q2   | {row-id}     | YES/NO                              | YES/NO                 |
| Q3   | {row-id}     | YES/NO                              | YES/NO                 |

Flag: `[SOURCE-PHRASE CITATION MISSING: slot Q{N}]` if Phase 1 source phrase absent.
Flag: `[PHASE-1 ROW NOT FOUND: slot Q{N} cites {row-id} which does not appear in Phase 1]`
Gate: all three slots have source phrases present and verifiable Phase 1 row IDs.
`CHECK 5B: PASS` or `CHECK 5B: FAIL -- [revisions made]`

`CHECK 5: PASS` (both 5A and 5B pass) or `CHECK 5: FAIL -- [details]`

---

**CHECK 6 -- Verify-Question Vocab-Term Citation Coverage**

For each of the inertia-advocate's 3 verify questions, emit all applicable flags:
1. `[MISSING ANNOTATION]`
2. `[Q-NUMBER MISMATCH]`
3. `[TERM MISMATCH]`
4. `[ROW-ID MISMATCH]`
5. `[TERM NOT IN QUESTION TEXT]`
Gate: all 3 questions pass all 5 checks.
`CHECK 6: PASS` or `CHECK 6: FAIL -- [revisions made]`

---

**CHECK 7 -- Replacement Provenance Audit**

Flag missing Phase 1 citations on Phase 2 replacements.
Gate: all replacements cited or none made.
`CHECK 7: PASS` or `CHECK 7: FAIL -- [revisions made]`

---

All 7 checks PASS -> `GATE RESULT: PASS` -- **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(Phase 5 table updated including
>   Planned-Vocab-Term; LENS AUDIT required; CHECK 3B + CHECK 4B re-run)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2-4 with
>   source phrase citations; inertia re-written first)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-03

**Axis**: Role replacement re-audit sub-procedure (single axis)
**Hypothesis**: R14 all-combined CHECK 3B and CHECK 4B instruct: "For each mismatch: rewrite file
to match plan, or return to Phase 5 with justification. Gate: zero mismatches." This permits silent
correction -- the model rewrites a file, re-runs the binding row, and marks CHECK 3B / 4B PASS
without any confirmation artifact. C-24 requires "audit-table full re-evaluation after replacement."
The sufficient condition is a named ROLE-REPLACE sub-procedure that fires for every mismatch: (1)
states the mismatch type and values, (2) states the resolution action, (3) re-evaluates the
affected row in the Phase 5 audit table and confirms the new value is still consistent with the
table, (4) emits `ROLE-REPLACE CONFIRMED: YES` before the CHECK closes. CHECK 3B / 4B may not
declare PASS until ROLE-REPLACE CONFIRMED appears for every flagged role. Single-axis: all other
mechanisms unchanged, CHECK 5 remains single-part, perspective diversity is a narrative requirement.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 -- DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets; each non-empty; each term has row identifier; minimum 3 terms

```
## Domain Vocabulary

Current-System Terms:
  [CS-1] {term}: "{source phrase from input}"

Migration-Cost Terms:
  [MC-1] {term}: "{source phrase from input}"

User-Habit Terms:
  [UH-1] {term}: "{source phrase from input}"
```

Row identifiers permanent. Empty buckets: extend by inference with `[inferred]` label.

**Exit condition met**: three non-empty buckets; each term has row identifier; minimum 3 terms.

---

### Phase 2 -- INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG + CONVERGENCE SUMMARY

**Entry**: Phase 1 complete
**Exit**: convergence declared; CONVERGENCE SUMMARY present; blocks preserved; replacements cited

`Q1/Q2/Q3` draw from Current-System / Migration-Cost / User-Habit Terms respectively.

**AUDIT ATTEMPT 1:**

| Q  | Row ID | Term Used | Expected Bucket | Match YES/NO |
|----|--------|-----------|-----------------|--------------|

ALL YES -> convergence. Any NO -> replacement with Phase 1 citation. Retry until convergence.
`AUDIT CONVERGENCE: ATTEMPT {N} ALL YES.`

```
## Convergence Summary
Q1-FINAL: [verbatim] [vocab: {CS-N} -- {term}]
Q2-FINAL: [verbatim] [vocab: {MC-N} -- {term}]
Q3-FINAL: [verbatim] [vocab: {UH-N} -- {term}]
```

**Exit condition met**: convergence declared; CONVERGENCE SUMMARY present.

---

### Phase 3 -- FRAME FILL

**Entry**: Phase 2 complete
**Exit**: completed frame; slot-binding YES

```
## Frame Fill
Q1 slot <- Q1-FINAL: [verbatim]
Q2 slot <- Q2-FINAL: [verbatim]
Q3 slot <- Q3-FINAL: [verbatim]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

Slot-binding all YES. Cross-slot blocking.
**Exit condition met**: frame complete; binding YES.

---

### Phase 4 -- FRAME CONFIRM

**Entry**: Phase 3 complete
**Exit**: FRAME CONFIRM present

```
FRAME CONFIRM: "{paste Phase 3 completed frame -- character-for-character}"
```

---

### Phase 5 -- PRE-WRITE SCOPE + VOCAB AUDIT

**Entry**: Phase 4 complete
**Exit**: >= 2 distinct scope values; all roles have Planned-Vocab-Term; SCOPE AUDIT PASS

| Planned Role        | Perspective | Scope      | Planned-Vocab-Term | Justification           |
|---------------------|-------------|------------|--------------------|-------------------------|
| inertia-advocate    | inertia     | cross-team | {CS-N}: {term}     | Q1-FINAL anchor         |
| pm                  | product     | {scope}    | {X-N}: {term}      | {one reason from input} |
| architect           | technical   | {scope}    | {X-N}: {term}      | {one reason from input} |
| {domain-specialist} | domain      | {scope}    | {X-N}: {term}      | from Phase 1 vocabulary |

**SCOPE AUDIT**: distinct scope values [list]. Gate: >= 2.
`SCOPE AUDIT PASS -- scope values: [list]`

Scope and Planned-Vocab-Term binding for Phase 6. Writing blocked until scope audit passes.

---

### Phase 6 -- WRITE ROLE FILES (INERTIA-ADVOCATE FIRST, INLINE LENS AUDIT)

**Entry**: Phase 5 complete
**Exit**: all files written; inertia-advocate written first and gate passed; all LENS AUDIT PASS;
         frame matches Phase 4; annotations valid; expertise.relevance has Planned-Vocab-Term

Write inertia-advocate first. LENS AUDIT after each role's orientation fields.

**Step 1 -- Write inertia-advocate**: frame from Phase 4 verbatim; 3 annotated verify questions
(annotation + term in body); 2+ simplify imperatives; expertise.relevance with Q1-FINAL row id.
**LENS AUDIT -- inertia-advocate**: verify ? termination; simplify imperative start. Fix violations.
`LENS AUDIT inertia-advocate: PASS`

**Step 2 -- INERTIA-ADVOCATE WRITTEN GATE**:
```
(1) File written: YES/NO  (2) Frame matches FRAME CONFIRM: YES/NO
(3) Domain grounding present: YES/NO
```
`INERTIA-ADVOCATE WRITTEN GATE: PASS` (all YES) or `FAIL -- [action]`

**Step 3 -- Write remaining roles**: use Planned-Vocab-Term for expertise.relevance; scope from
Phase 5. LENS AUDIT after each role. `LENS AUDIT {role}: PASS` before writing next.

Minimum 3 roles; at least 3 distinct perspective categories.

---

### Phase 7 -- VERIFICATION GATE

**Entry**: Phase 6 complete
**Exit**: all 7 checks PASS; GATE RESULT declared

**DELIVERY IS BLOCKED. Complete all 7 checks in order.**

---

**CHECK 1 -- Registry Summary Table**
`CHECK 1: PASS` or `CHECK 1: FAIL -- [issue]`

---

**CHECK 2 -- Orphan Reference Resolution**
Zero unresolved `collaborates_with` references.
`CHECK 2: PASS` or `CHECK 2: FAIL -- [action taken]`

---

**CHECK 3 -- Scope Gradient + Binding**

Part A -- Gradient: distinct scope values >= 2.
`CHECK 3A: PASS -- scope values: [list]`

Part B -- Binding: Phase 5 planned vs Phase 6 written per role.

| Role | Phase 5 Planned | Phase 6 Written | Match? |
|------|-----------------|-----------------|--------|

For each mismatch, immediately trigger ROLE-REPLACE: *(new in V-03)*

```
ROLE-REPLACE -- {role} (SCOPE):
  Planned scope: {Phase 5 value}
  Written scope: {Phase 6 value}
  Resolution: [rewrite file to match Phase 5 | amend Phase 5 and re-run scope audit]
  Re-evaluation: [re-run Phase 5 Scope row for this role; confirm table still shows >= 2 distinct
                  scope values after any amendment]
  Updated Phase 5 row: | {role} | {perspective} | {scope-after} | {vocab-term} | {justification} |
  ROLE-REPLACE CONFIRMED ({role} SCOPE): YES/NO
```

CHECK 3B does not declare PASS until `ROLE-REPLACE CONFIRMED: YES` for every flagged role.
Gate: zero unresolved mismatches.
`CHECK 3: PASS` or `CHECK 3: FAIL -- [ROLE-REPLACE records above]`

---

**CHECK 4 -- Vocabulary Coverage + Binding**

Part A -- Coverage: all roles have vocab term in expertise.relevance.
`CHECK 4A: PASS`

Part B -- Binding: Phase 5 Planned-Vocab-Term vs Phase 6 written expertise.relevance per role.

| Role | Phase 5 Planned Vocab | Phase 6 Written Vocab | Match? |
|------|-----------------------|-----------------------|--------|

For each mismatch, immediately trigger ROLE-REPLACE: *(new in V-03)*

```
ROLE-REPLACE -- {role} (VOCAB):
  Planned vocab: {Phase 5 term}
  Written vocab: {Phase 6 term}
  Resolution: [rewrite expertise.relevance to use planned term | amend Phase 5 Planned-Vocab-Term]
  Re-evaluation: [re-run Phase 5 Planned-Vocab-Term row for this role; confirm term is in Phase 1]
  Updated Phase 5 row: | {role} | {perspective} | {scope} | {vocab-term-after} | {justification} |
  ROLE-REPLACE CONFIRMED ({role} VOCAB): YES/NO
```

CHECK 4B does not declare PASS until `ROLE-REPLACE CONFIRMED: YES` for every flagged role.
Gate: zero unresolved mismatches.
`CHECK 4: PASS` or `CHECK 4: FAIL -- [ROLE-REPLACE records above]`

---

**CHECK 5 -- Frame Confirm Match**
Phase 4 FRAME CONFIRM vs Phase 6 frame, char-for-char. Flag `[FRAME MISMATCH]`.
`CHECK 5: PASS` or `CHECK 5: FAIL -- [FRAME MISMATCH; rewritten]`

---

**CHECK 6 -- Verify-Question Vocab-Term Citation Coverage**
All 5 failure modes checked per verify question; independent emission.
Gate: all 3 questions pass all 5 checks.
`CHECK 6: PASS` or `CHECK 6: FAIL -- [revisions made]`

---

**CHECK 7 -- Replacement Provenance Audit**
All Phase 2 replacements cite Phase 1 rows.
`CHECK 7: PASS` or `CHECK 7: FAIL -- [revisions made]`

---

All 7 checks PASS -> `GATE RESULT: PASS` -- **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `--amend add:{role-name}` *(Phase 5 table updated; LENS AUDIT required; ROLE-REPLACE
>   sub-procedure available if CHECK 3B or CHECK 4B flags mismatch on new role)*
> - Re-characterize inertia: `--amend reinertia` *(re-runs Phases 2-4; inertia first)*
> - Re-run verification gate: `--amend verify` *(re-runs Phase 7 including ROLE-REPLACE if needed)*
> - Adjust levels: `--amend levels:{senior|staff|principal}`

---

---

## V-04

**Axis**: Perspective diversity gate + source phrase forensic citation (two-axis combination:
V-01 + V-02)
**Hypothesis**: V-01 adds the perspective diversity gate (PERSPECTIVE AUDIT in Phase 5, CHECK 8 in
Phase 7), closing Gap-A. V-02 adds source phrase citations to FRAME FILL and splits CHECK 5 into
5A + 5B, closing Gap-B. These two axes are independent: perspective tracking applies to role
planning and Phase 7 validation; source phrase citations apply to the inertia frame fill chain. No
shared mechanism -- V-01's PERSPECTIVE AUDIT reads the Perspective column; V-02's source citation
reads the Phase 1 vocabulary source phrases. Combining them closes both gap-A and gap-B while
avoiding the V-03 structural change (ROLE-REPLACE sub-procedure), keeping CHECK 3B and CHECK 4B
correction paths simple. V-04 is the expected strongest scoring variation: two gap closures, no
added Phase 7 CHECK complexity beyond what each axis independently introduces.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 -- DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets; each non-empty; each term has row identifier; minimum 3 terms

```
## Domain Vocabulary

Current-System Terms:
  [CS-1] {term}: "{source phrase from input}"

Migration-Cost Terms:
  [MC-1] {term}: "{source phrase from input}"

User-Habit Terms:
  [UH-1] {term}: "{source phrase from input}"
```

Row identifiers permanent. Empty buckets: extend by inference.

---

### Phase 2 -- INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG + CONVERGENCE SUMMARY

**Entry**: Phase 1 complete
**Exit**: convergence declared; CONVERGENCE SUMMARY present

Q1 (Current-System) / Q2 (Migration-Cost) / Q3 (User-Habit). AUDIT ATTEMPT loop until ALL YES.
Prior blocks preserved. Replacements cite Phase 1 rows.

```
## Convergence Summary
Q1-FINAL: [verbatim] [vocab: {CS-N} -- {term}]
Q2-FINAL: [verbatim] [vocab: {MC-N} -- {term}]
Q3-FINAL: [verbatim] [vocab: {UH-N} -- {term}]
```

---

### Phase 3 -- FRAME FILL WITH SOURCE PHRASE CITATIONS *(from V-02)*

**Entry**: Phase 2 complete
**Exit**: completed frame; slot-binding YES; all three source phrase citations present and
         traceable to Phase 1 row identifiers

```
## Frame Fill

Q1 slot <- Q1-FINAL: [verbatim Q1-FINAL answer]
  Phase 1 source: {CS-N} = "{source phrase from Phase 1 Current-System Terms row CS-N}"
Q2 slot <- Q2-FINAL: [verbatim Q2-FINAL answer]
  Phase 1 source: {MC-N} = "{source phrase from Phase 1 Migration-Cost Terms row MC-N}"
Q3 slot <- Q3-FINAL: [verbatim Q3-FINAL answer]
  Phase 1 source: {UH-N} = "{source phrase from Phase 1 User-Habit Terms row UH-N}"

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

If any Phase 1 source phrase cannot be located:
`[SOURCE-PHRASE CITATION MISSING: slot Q{N} -- row {row-id} not found in Phase 1 vocabulary]`
Do not proceed until all three source citations are present and traceable.

Slot-binding Q1<-Q1-FINAL, Q2<-Q2-FINAL, Q3<-Q3-FINAL -- all YES. Cross-slot blocking.

---

### Phase 4 -- FRAME CONFIRM

**Entry**: Phase 3 complete (source citations present)
**Exit**: FRAME CONFIRM present

```
FRAME CONFIRM: "{paste Phase 3 completed frame -- character-for-character}"
```

---

### Phase 5 -- PRE-WRITE SCOPE + PERSPECTIVE + VOCAB AUDIT *(perspective gate from V-01)*

**Entry**: Phase 4 complete
**Exit**: >= 2 distinct scope values; >= 3 distinct perspective categories; all roles have
         Planned-Vocab-Term; SCOPE AUDIT PASS and PERSPECTIVE AUDIT PASS both declared

| Planned Role        | Perspective | Scope      | Planned-Vocab-Term | Justification           |
|---------------------|-------------|------------|--------------------|-------------------------|
| inertia-advocate    | inertia     | cross-team | {CS-N}: {term}     | Q1-FINAL anchor         |
| pm                  | product     | {scope}    | {X-N}: {term}      | {one reason from input} |
| architect           | technical   | {scope}    | {X-N}: {term}      | {one reason from input} |
| {domain-specialist} | domain      | {scope}    | {X-N}: {term}      | from Phase 1 vocabulary |

**SCOPE AUDIT**: distinct scope values [list]. Gate: >= 2. Revise if needed.
`SCOPE AUDIT PASS -- scope values: [list]`

**PERSPECTIVE AUDIT**: distinct perspective values [list]. Gate: >= 3. Add/reassign if needed.
`PERSPECTIVE AUDIT PASS -- perspectives: [list]`

Scope and Planned-Vocab-Term binding. Writing blocked until both audits pass.

---

### Phase 6 -- WRITE ROLE FILES (INERTIA-ADVOCATE FIRST, INLINE LENS AUDIT)

**Entry**: Phase 5 complete (both audits passed)
**Exit**: all files written; inertia-advocate first and gate passed; all LENS AUDIT PASS;
         frame matches Phase 4; annotations valid; expertise.relevance has Planned-Vocab-Term

Write inertia-advocate first. LENS AUDIT after each role's orientation fields.

**Step 1 -- Write inertia-advocate**: frame verbatim from FRAME CONFIRM; 3 annotated verify
questions (term in body); 2+ simplify imperatives; expertise.relevance with Q1-FINAL row id.
LENS AUDIT. `LENS AUDIT inertia-advocate: PASS`

**Step 2 -- INERTIA-ADVOCATE WRITTEN GATE**:
```
(1) File written: YES/NO  (2) Frame matches FRAME CONFIRM: YES/NO
(3) Domain grounding (system/cost/habit from Phase 2) present: YES/NO
```
`INERTIA-ADVOCATE WRITTEN GATE: PASS` or `FAIL -- [action]`

**Step 3 -- Write remaining roles**: expertise.relevance references Planned-Vocab-Term; scope from
Phase 5. LENS AUDIT after each. Do not write next role until LENS AUDIT PASS.

Minimum 3 roles; at least 3 distinct perspective categories (PERSPECTIVE AUDIT confirms this).

---

### Phase 7 -- VERIFICATION GATE

**Entry**: Phase 6 complete
**Exit**: all 8 checks declare PASS; GATE RESULT declared

**DELIVERY IS BLOCKED. Complete all 8 checks in order.**

---

**CHECK 1 -- Registry Summary Table**

| Role | Perspective | Frame (first 8 words) | Scope | Collaborates With |
|------|-------------|----------------------|-------|-------------------|
`CHECK 1: PASS` or `CHECK 1: FAIL -- [issue]`

---

**CHECK 2 -- Orphan Reference Resolution**
Zero unresolved `collaborates_with`.
`CHECK 2: PASS` or `CHECK 2: FAIL -- [action]`

---

**CHECK 3 -- Scope Gradient + Binding**

3A: distinct values >= 2. `CHECK 3A: PASS -- scope values: [list]`

3B: Phase 5 planned vs Phase 6 written per role.
Flag `[{role}: planned {A}, written {B} -- SCOPE BINDING MISMATCH]`. Rewrite or return to Phase 5.
Gate: zero mismatches. `CHECK 3: PASS` or `CHECK 3: FAIL -- [action]`

---

**CHECK 4 -- Vocabulary Coverage + Binding**

4A: all roles have vocab term. `CHECK 4A: PASS`

4B: Phase 5 Planned-Vocab-Term vs Phase 6 written expertise.relevance per role.
Flag `[{role}: planned vocab "{planned}", written vocab "{written}" -- VOCAB BINDING MISMATCH]`
Gate: zero mismatches. `CHECK 4: PASS` or `CHECK 4: FAIL -- [action]`

---

**CHECK 5 -- Frame Confirm Match + Source Citation Verification** *(from V-02)*

Part A -- Frame match: char-for-char. Flag `[FRAME MISMATCH]`.
`CHECK 5A: PASS` or `CHECK 5A: FAIL -- [FRAME MISMATCH; rewritten]`

Part B -- Source citations:

| Slot | Row ID Cited | Source Phrase in FRAME FILL | Row in Phase 1 |
|------|--------------|------------------------------|----------------|
| Q1   | {row-id}     | YES/NO                       | YES/NO         |
| Q2   | {row-id}     | YES/NO                       | YES/NO         |
| Q3   | {row-id}     | YES/NO                       | YES/NO         |

Flag `[SOURCE-PHRASE CITATION MISSING: slot Q{N}]` or `[PHASE-1 ROW NOT FOUND: slot Q{N}]`.
Gate: all citations present and verifiable.
`CHECK 5B: PASS` or `CHECK 5B: FAIL -- [revisions]`

`CHECK 5: PASS` (both) or `CHECK 5: FAIL -- [details]`

---

**CHECK 6 -- Verify-Question Vocab-Term Citation Coverage**
5 failure modes per question; independent emission; all 3 questions must pass all 5.
`CHECK 6: PASS` or `CHECK 6: FAIL -- [revisions]`

---

**CHECK 7 -- Replacement Provenance Audit**
Phase 2 replacements cite Phase 1 rows.
`CHECK 7: PASS` or `CHECK 7: FAIL -- [revisions]`

---

**CHECK 8 -- Perspective Diversity Gate** *(from V-01)*

From CHECK 1 registry table, list distinct perspective values:

| Role | Perspective |
|------|-------------|

Distinct values: [list]. Gate: >= 3 distinct perspective categories.
If < 3: add or reassign roles. State action.
`CHECK 8: PASS -- distinct perspectives: [list]` or `CHECK 8: FAIL -- [action]`

---

All 8 checks PASS -> `GATE RESULT: PASS` -- **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `--amend add:{role-name}` *(Phase 5 updated; SCOPE + PERSPECTIVE audits re-run;
>   LENS AUDIT required; CHECK 3B + CHECK 4B + CHECK 8 re-run)*
> - Re-characterize inertia: `--amend reinertia` *(re-runs Phases 2-4 including source citations)*
> - Re-run verification gate: `--amend verify` *(re-runs Phase 7)*
> - Adjust levels: `--amend levels:{senior|staff|principal}`

---

---

## V-05

**Axis**: Perspective diversity gate + source phrase forensic citation + role replacement re-audit
(three-axis combination: V-01 + V-02 + V-03)
**Hypothesis**: V-04 closes Gap-A (perspective) and Gap-B (source citation). V-03 closes Gap-C
(replacement re-audit). All three gaps closed simultaneously. The three axes target separate
mechanisms: PERSPECTIVE AUDIT + CHECK 8 gate role population planning; source phrase citations gate
frame provenance; ROLE-REPLACE sub-procedure gates mismatch correction. No axis interferes with
another. Expected to score highest on all aspirational criteria including C-24 (replacement re-audit
via ROLE-REPLACE), C-25 / C-27 (source phrase forensic citation in FRAME FILL), C-08 (perspective
diversity via CHECK 8), while maintaining all baseline mechanisms from C-09 through C-32. V-05 is
the maximum-coverage variation -- trades prompt complexity for criterion completeness.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 -- DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets; each non-empty; each term has row identifier; minimum 3 terms

```
## Domain Vocabulary

Current-System Terms:
  [CS-1] {term}: "{source phrase from input}"

Migration-Cost Terms:
  [MC-1] {term}: "{source phrase from input}"

User-Habit Terms:
  [UH-1] {term}: "{source phrase from input}"
```

Row identifiers permanent. Empty buckets: extend by inference with `[inferred]` label.
Replacement terms in Phase 2 must have Phase 1 rows; add first if absent.

---

### Phase 2 -- INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG + CONVERGENCE SUMMARY

**Entry**: Phase 1 complete
**Exit**: convergence declared; CONVERGENCE SUMMARY present; all blocks preserved; replacements cited

Q1 (Current-System) / Q2 (Migration-Cost) / Q3 (User-Habit). AUDIT ATTEMPT loop until ALL YES.
Record each replacement with Phase 1 citation. Prior blocks not deleted.

```
## Convergence Summary
Q1-FINAL: [verbatim] [vocab: {CS-N} -- {term}]
Q2-FINAL: [verbatim] [vocab: {MC-N} -- {term}]
Q3-FINAL: [verbatim] [vocab: {UH-N} -- {term}]
```

Phase 3 and Phase 6 consume from CONVERGENCE SUMMARY only.

---

### Phase 3 -- FRAME FILL WITH SOURCE PHRASE CITATIONS *(V-02 axis)*

**Entry**: Phase 2 complete
**Exit**: completed frame; slot-binding YES; all three `Phase 1 source:` lines present and
         traceable to Phase 1 row identifiers

```
## Frame Fill

Q1 slot <- Q1-FINAL: [verbatim Q1-FINAL answer]
  Phase 1 source: {CS-N} = "{verbatim source phrase from Phase 1 Current-System Terms row CS-N}"
Q2 slot <- Q2-FINAL: [verbatim Q2-FINAL answer]
  Phase 1 source: {MC-N} = "{verbatim source phrase from Phase 1 Migration-Cost Terms row MC-N}"
Q3 slot <- Q3-FINAL: [verbatim Q3-FINAL answer]
  Phase 1 source: {UH-N} = "{verbatim source phrase from Phase 1 User-Habit Terms row UH-N}"

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

If Phase 1 source phrase for any slot not found:
`[SOURCE-PHRASE CITATION MISSING: slot Q{N} -- row {row-id} not in Phase 1 vocabulary]`
Do not proceed until all citations present and traceable.

Slot-binding: Q1<-Q1-FINAL, Q2<-Q2-FINAL, Q3<-Q3-FINAL -- all YES. Cross-slot blocking.

---

### Phase 4 -- FRAME CONFIRM

**Entry**: Phase 3 complete (frame string + source citations present)
**Exit**: FRAME CONFIRM present with verbatim Phase 3 paste

```
## Frame Confirm

FRAME CONFIRM: The inertia-advocate orientation.frame I will write first in Phase 6 is:
"{paste Phase 3 completed frame string -- character-for-character, including all punctuation}"
```

If you cannot reproduce Phase 3 output exactly, return to Phase 3 and regenerate.

---

### Phase 5 -- PRE-WRITE SCOPE + PERSPECTIVE + VOCAB AUDIT *(V-01 perspective gate axis)*

**Entry**: Phase 4 complete
**Exit**: >= 2 distinct scope values; >= 3 distinct perspective categories; all roles have
         Planned-Vocab-Term; SCOPE AUDIT PASS and PERSPECTIVE AUDIT PASS both declared

| Planned Role        | Perspective | Scope      | Planned-Vocab-Term | Justification           |
|---------------------|-------------|------------|--------------------|-------------------------|
| inertia-advocate    | inertia     | cross-team | {CS-N}: {term}     | Q1-FINAL anchor         |
| pm                  | product     | {scope}    | {X-N}: {term}      | {one reason from input} |
| architect           | technical   | {scope}    | {X-N}: {term}      | {one reason from input} |
| {domain-specialist} | domain      | {scope}    | {X-N}: {term}      | from Phase 1 vocabulary |

Add domain-specialist rows as needed. Scope values: `team`, `cross-team`, `org`.
Planned-Vocab-Term must be a Phase 1 row id + term. Each role selects a distinct term where
possible; shared terms noted in Justification.

**SCOPE AUDIT**: distinct scope values [list]. Gate: >= 2. Revise if needed.
`SCOPE AUDIT PASS -- scope values: [list]`

**PERSPECTIVE AUDIT**: distinct perspective values [list]. Gate: >= 3. Add/reassign if < 3.
`PERSPECTIVE AUDIT PASS -- perspectives: [list]`

Scope and Planned-Vocab-Term binding for Phase 6. Writing blocked until both audits pass.

---

### Phase 6 -- WRITE ROLE FILES (INERTIA-ADVOCATE FIRST, INLINE LENS AUDIT)

**Entry**: Phase 5 complete (both audits passed)
**Exit**: all files written; inertia-advocate written first and gate passed; all LENS AUDIT PASS;
         frame matches Phase 4; annotations 5-mode-valid with terms in bodies;
         expertise.relevance references Planned-Vocab-Term; scope matches Phase 5 table

Write each role to `.roles/{area}/{role-slug}.md`. **Write the inertia-advocate first.**
After each role's orientation fields: run LENS AUDIT before writing the next role.

**Step 1 -- Write inertia-advocate** (`.roles/{area}/inertia-advocate.md`):
- `orientation.frame`: FRAME CONFIRM verbatim
- `orientation.verify`: exactly 3 questions; BOTH conditions per question:
  1. Annotation: `{question?} [Q: QN -- vocab: {row-id} -- {term-from-QN-FINAL}]`
  2. Annotation `{term}` appears verbatim in question body
- `orientation.simplify`: 2+ items starting with imperative verb
- `expertise.relevance`: Q1-FINAL row id + at least one other Phase 1 term
- `scope`: cross-team; `collaborates_with`: pm

**LENS AUDIT -- inertia-advocate**:
```
verify items: [{N}] "{item}" -- ends in ? YES/NO ...
simplify items: [{N}] "{item}" -- begins with imperative verb? YES/NO ...
```
Flag violations; rewrite before proceeding.
`LENS AUDIT inertia-advocate: PASS`

**Step 2 -- INERTIA-ADVOCATE WRITTEN GATE**:
```
(1) File written: YES/NO
(2) Frame matches FRAME CONFIRM char-for-char: YES/NO
(3) Domain grounding (named system, cost, or habit from Phase 2 Q-FINAL answers) present: YES/NO
```
`INERTIA-ADVOCATE WRITTEN GATE: PASS` (all YES) or `FAIL -- [action taken before proceeding]`

**Step 3 -- Write remaining roles**:
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
relevance: {sentence referencing the Planned-Vocab-Term from Phase 5 table for this role}

## scope
{value from Phase 5 planning table -- do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**LENS AUDIT** (immediately after writing each role's orientation fields):
```
LENS AUDIT -- {role-name}:
verify items: [{N}] "{item}" -- ends in ? YES/NO ...
simplify items: [{N}] "{item}" -- begins with imperative verb? YES/NO ...
```
Flag `[{role} verify item {N}: "{item}" -- MISSING ? TERMINATOR]` or
`[{role} simplify item {N}: "{item}" -- NOT AN IMPERATIVE]`. Rewrite before proceeding.
`LENS AUDIT {role-name}: PASS` or `LENS AUDIT {role-name}: FAIL -- [rewrites made]`
Do not write the next role until LENS AUDIT PASS.

Minimum 3 roles total; at least 3 distinct perspective categories.

---

### Phase 7 -- VERIFICATION GATE

**Entry**: Phase 6 complete (all LENS AUDIT PASS; INERTIA-ADVOCATE WRITTEN GATE PASS)
**Exit**: all 8 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. Complete all 8 checks in order. Each must declare PASS before the
next opens. Fix defects before proceeding.**

---

**CHECK 1 -- Registry Summary Table**

| Role | Perspective | Frame (first 8 words) | Scope | Collaborates With |
|------|-------------|----------------------|-------|-------------------|

One row per role. Role names match file stems exactly.
`CHECK 1: PASS` or `CHECK 1: FAIL -- [issue]`

---

**CHECK 2 -- Orphan Reference Resolution**

Flag unresolved `collaborates_with`. Gate: zero unresolved.
`CHECK 2: PASS` or `CHECK 2: FAIL -- [action taken]`

---

**CHECK 3 -- Scope Gradient + Binding**

Part A: distinct scope values >= 2.
`CHECK 3A: PASS -- scope values: [list]`

Part B: Phase 5 planned vs Phase 6 written per role.

| Role | Phase 5 Planned | Phase 6 Written | Match? |
|------|-----------------|-----------------|--------|

For each mismatch, trigger ROLE-REPLACE: *(V-03 axis)*

```
ROLE-REPLACE -- {role} (SCOPE):
  Planned scope: {Phase 5 value}
  Written scope: {Phase 6 value}
  Resolution: [rewrite file to match plan | amend Phase 5 and re-run SCOPE AUDIT]
  Re-evaluation: updated Phase 5 row:
    | {role} | {perspective} | {scope-after} | {vocab-term} | {justification} |
    SCOPE AUDIT PASS still holds after amendment: YES/NO
  ROLE-REPLACE CONFIRMED ({role} SCOPE): YES/NO
```

CHECK 3B does not declare PASS until ROLE-REPLACE CONFIRMED: YES for all flagged roles.
Gate: zero unresolved mismatches.
`CHECK 3: PASS` or `CHECK 3: FAIL -- [ROLE-REPLACE records above]`

---

**CHECK 4 -- Vocabulary Coverage + Binding**

Part A: all roles have vocab term.
`CHECK 4A: PASS`

Part B: Phase 5 Planned-Vocab-Term vs Phase 6 written expertise.relevance per role.

| Role | Phase 5 Planned Vocab | Phase 6 Written Vocab | Match? |
|------|-----------------------|-----------------------|--------|

For each mismatch, trigger ROLE-REPLACE: *(V-03 axis)*

```
ROLE-REPLACE -- {role} (VOCAB):
  Planned vocab: {Phase 5 term}
  Written vocab: {Phase 6 term}
  Resolution: [rewrite expertise.relevance to use planned term | amend Phase 5 Planned-Vocab-Term]
  Re-evaluation: updated Phase 5 row:
    | {role} | {perspective} | {scope} | {vocab-term-after} | {justification} |
    Phase 1 row {vocab-term-after} found: YES/NO
  ROLE-REPLACE CONFIRMED ({role} VOCAB): YES/NO
```

CHECK 4B does not declare PASS until ROLE-REPLACE CONFIRMED: YES for all flagged roles.
Gate: zero unresolved mismatches.
`CHECK 4: PASS` or `CHECK 4: FAIL -- [ROLE-REPLACE records above]`

---

**CHECK 5 -- Frame Confirm Match + Source Citation Verification** *(V-02 axis)*

Part A -- Frame match: Phase 4 FRAME CONFIRM vs Phase 6 inertia-advocate frame, char-for-char.
Flag `[FRAME MISMATCH]`. Rewrite to match exactly.
`CHECK 5A: PASS -- strings match` or `CHECK 5A: FAIL -- [FRAME MISMATCH; rewritten]`

Part B -- Source citation verification:

| Slot | Row ID Cited | Source Phrase in FRAME FILL | Row Found in Phase 1 |
|------|--------------|-----------------------------|-----------------------|
| Q1   | {row-id}     | YES/NO                      | YES/NO                |
| Q2   | {row-id}     | YES/NO                      | YES/NO                |
| Q3   | {row-id}     | YES/NO                      | YES/NO                |

Flag `[SOURCE-PHRASE CITATION MISSING: slot Q{N}]` if source phrase absent from FRAME FILL.
Flag `[PHASE-1 ROW NOT FOUND: slot Q{N} cites {row-id}]` if row not in Phase 1.
Gate: all three slots present and verifiable.
`CHECK 5B: PASS` or `CHECK 5B: FAIL -- [revisions made]`

`CHECK 5: PASS` (5A and 5B) or `CHECK 5: FAIL -- [details]`

---

**CHECK 6 -- Verify-Question Vocab-Term Citation Coverage**

For each of the inertia-advocate's 3 verify questions, emit all applicable flags in order:

1. `[MISSING ANNOTATION]` -- no `[Q: QN -- vocab: ...]` tag present
2. `[Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M} dimension]`
3. `[TERM MISMATCH: annotation says "{term-A}", CONVERGENCE SUMMARY Q{N}-FINAL recorded "{term-B}"]`
4. `[ROW-ID MISMATCH: annotation says {row-A}, CONVERGENCE SUMMARY Q{N}-FINAL used {row-B}]`
5. `[TERM NOT IN QUESTION TEXT: annotation term "{term}" not found in question body]`

Each failure mode independently emitted before the next is checked.
Gate: all 3 questions pass all 5 checks.
`CHECK 6: PASS` or `CHECK 6: FAIL -- [revisions made]`

---

**CHECK 7 -- Replacement Provenance Audit**

For each replacement in Phase 2: Phase 1 row citation present and verifiable?
Flag `Q{N} replacement "{old}" -> "{new}" [MISSING PHASE-1 CITATION]`
Gate: all cited or none made.
`CHECK 7: PASS` or `CHECK 7: FAIL -- [revisions made]`

---

**CHECK 8 -- Perspective Diversity Gate** *(V-01 axis)*

From the CHECK 1 registry summary table, list all distinct perspective values:

| Role | Perspective |
|------|-------------|

Distinct perspective values: [list]

Gate: >= 3 distinct perspective categories.
If < 3: add or reassign roles. State action taken.
`CHECK 8: PASS -- distinct perspectives: [list]` or `CHECK 8: FAIL -- [action taken]`

---

All 8 checks declared PASS -> `GATE RESULT: PASS` -- **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `--amend add:{role-name}` *(Phase 5 table updated including Planned-Vocab-Term;
>   SCOPE AUDIT + PERSPECTIVE AUDIT re-run; LENS AUDIT required; CHECK 3B + CHECK 4B with
>   ROLE-REPLACE available; CHECK 8 re-run)*
> - Re-characterize inertia: `--amend reinertia` *(re-runs Phases 2-4 with source citations;
>   inertia re-written first with LENS AUDIT; term-in-body condition applies)*
> - Re-run scope gate: `--amend scope` *(re-runs Phase 5 SCOPE + PERSPECTIVE AUDIT and CHECK 3B)*
> - Re-run verification gate: `--amend verify` *(re-runs Phase 7 including ROLE-REPLACE if needed)*
> - Adjust levels: `--amend levels:{senior|staff|principal}`
