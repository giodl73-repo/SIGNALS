---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 13
rubric: crew-roles-rubric-v7-2026-03-17.md
---

# crew-roles — Variate R13

5 complete prompt body variations for the `crew-roles` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

**Baseline**: R12 V-05 (ES-1 + ES-2 + Frame confirm combined, 100/100 against rubric v6). R12 V-05
implements C-26 (ROW-ID MISMATCH as fourth independent failure mode in CHECK 6) and C-27
(forensic source-phrase citation in replacement records, CHECK 7) — both now formalized in v7.
All five R12 variations scored 100/100 on v6. The highest-integration baseline entering R13 is
R12 V-05: seven phases; Phase 4 FRAME CONFIRM re-declares Phase 3 verbatim; Phase 6 verify
questions carry `[Q: QN — vocab: {row-id} — {term}]` validated by CHECK 6 with four failure
modes; Phase 2 replacements carry forensic `Phase 1 citation: {row-id} = "{term}" in Phase 1
{bucket}: "{source phrase}"` citations validated by CHECK 7.

**R12 excellence signals driving R13 axes**:

- **ES-1 — Verify annotation validates term metadata but not term presence in question body**:
  R12 V-01 and V-05 require each inertia-advocate verify question to carry
  `[Q: QN — vocab: {row-id} — {term}]`. CHECK 6 validates four failure modes: MISSING
  ANNOTATION, Q-NUMBER MISMATCH, TERM MISMATCH, and ROW-ID MISMATCH. All four operate on the
  annotation tag — they confirm the annotation correctly names the Phase 2 vocabulary term and
  row. But CHECK 6 does not require the question text body to contain the vocabulary term as a
  substring. A question `"Is the current routing infrastructure resilient to the proposed
  migration?" [Q: Q2 — vocab: MC-1 — re-routing-cost]` passes all four checks: the annotation
  is present, Q-number is Q2, term matches Phase 2 Q2's recorded term, row-id matches. Yet
  "re-routing-cost" appears nowhere in the question body — the annotation tags a grounding the
  question does not demonstrate. The annotation is a metadata assertion; the question body is
  an independent surface. A fifth failure mode `[TERM NOT IN QUESTION TEXT]` closes this:
  the annotation's `{term}` must appear verbatim as a substring of the question text itself.

- **ES-2 — Scope planning table and written scope are independently authored, never compared**:
  R12 V-05 Phase 5 builds a planning table assigning scope values to each planned role before
  writing begins. Phase 7 CHECK 3 confirms scope gradient exists (at least 2 distinct scope
  values) after writing. But CHECK 3 performs an aggregate check — it lists distinct values
  in the registry as-written, not a row-by-row comparison of Phase 5 planned scope to Phase 6
  written scope. A role planned as `team` in Phase 5 could be written as `cross-team` in Phase 6
  (perhaps because an adjacent role's scope was changed to avoid homogeneity), and CHECK 3 would
  pass — the gradient exists, but the planning-execution fidelity gap is undetected. The fix:
  after CHECK 3 confirms gradient, a SCOPE BINDING sub-check compares each role's Phase 5
  planning-table scope to its Phase 6 written scope; a mismatch is flagged
  `[{role}: planned {A}, written {B} — SCOPE BINDING MISMATCH]` and must be either corrected
  (rewrite file to match plan) or documented (update plan to reflect the intentional change,
  re-run scope audit). Scope decisions made during writing cannot silently overwrite planning
  decisions.

**Variation axes**:
- V-01 (single): Term-in-question-body enforcement — adds fifth CHECK 6 failure mode
  `[TERM NOT IN QUESTION TEXT]`; question text must contain annotation `{term}` as substring
- V-02 (single): Scope binding check — CHECK 3 extended with row-by-row Phase 5 plan vs Phase 6
  written scope comparison; SCOPE BINDING MISMATCH is a blocking error
- V-03 (single): Convergence summary — Phase 2 closes with a CONVERGENCE SUMMARY block
  declaring final row-ids and terms independent of iteration history; Phase 3 consumes from
  the summary, not from "most recent attempt"
- V-04 (combined): ES-1 + ES-2 — term-in-body + scope binding
- V-05 (combined): ES-1 + ES-2 + convergence summary — full three-axis synthesis

---

## V-01

**Axis**: Term-in-question-body enforcement (ES-1 — single axis)
**Hypothesis**: R12 V-05 establishes a four-failure-mode annotation gate in CHECK 6. All four
modes validate the annotation tag: MISSING ANNOTATION catches absent tags; Q-NUMBER MISMATCH
catches wrong dimension labels; TERM MISMATCH catches annotation terms that differ from Phase 2
recorded terms; ROW-ID MISMATCH catches correct terms cited at incorrect row positions. The gate
is exhaustive for annotation correctness. But annotation correctness is not question-body
grounding: a question whose text never invokes the vocabulary term can still carry a correct
annotation. The annotation asserts a grounding the question body does not demonstrate. Requiring
the annotation's `{term}` to appear verbatim in the question text converts the annotation from a
metadata tag into a structural constraint on question content — a question that cannot contain
its own annotation term is structurally mismatched and should be rewritten. The fifth failure
mode `[TERM NOT IN QUESTION TEXT]` makes this violation independently detectable and flaggable,
separate from the four existing annotation-level modes.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

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
  Phase 1 row — if a term has no row, add it to Phase 1 before using it as a replacement

**Exit condition met**: three non-empty buckets; each term has a row identifier; minimum 3 terms.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG WITH PROVENANCE

**Entry**: Phase 1 complete
**Exit**: convergence declared; all ATTEMPT blocks preserved; each replacement cites Phase 1 row

Answer three questions, citing Phase 1 row identifiers in each answer:

**Q1** (draw from Current-System Terms): What existing system, tool, or approach does the domain
currently rely on?
Required format: `Q1: [answer] [vocab: {CS-N} — {term}]`

**Q2** (draw from Migration-Cost Terms): What concrete cost or friction does moving away from Q1
create?
Required format: `Q2: [answer] [vocab: {MC-N} — {term}]`

**Q3** (draw from User-Habit Terms): What observable user workflow or daily behavior depends on Q1?
Required format: `Q3: [answer] [vocab: {UH-N} — {term}]`

After writing all three answers, open the iteration log:

---

**AUDIT ATTEMPT 1:**

| Q  | Row ID | Term Used | Expected Bucket | Match YES/NO |
|----|--------|-----------|-----------------|--------------|
| Q1 | {CS-N} | {term}    | Current-System  | YES/NO       |
| Q2 | {MC-N} | {term}    | Migration-Cost  | YES/NO       |
| Q3 | {UH-N} | {term}    | User-Habit      | YES/NO       |

If all rows YES:
`ATTEMPT 1 RESULT: ALL YES — Phase 2 convergence achieved.`

If any row NO:
`ATTEMPT 1 RESULT: BLOCKED — Q{N} row shows NO.`

Record replacement with Phase 1 provenance:
```
Replacement:
  Q{N} term "{old-term}" [{old-row-id}]
  -> "{new-term}" [{new-row-id}]
  Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"
```

If the new term has no Phase 1 row identifier, add it to Phase 1 under the correct bucket first,
then cite the newly-assigned row identifier.

Restart the audit table from Q1. **Prior ATTEMPT blocks are not deleted.**

---

**AUDIT ATTEMPT 2:** (if ATTEMPT 1 BLOCKED)

Re-evaluate all three rows from Q1. Write a new table. Continue until convergence.

`AUDIT CONVERGENCE: ATTEMPT {N} ALL YES. {N} attempt(s) required.`
`Replacement provenance: [all replacements cite Phase 1 rows]` or `[no replacements made]`

**Exit condition met**: convergence declared; all ATTEMPT blocks preserved; each replacement carries
a Phase 1 row citation with source phrase; no replacement term is undocumented.

---

### Phase 3 — FRAME FILL

**Entry**: Phase 2 complete (audit convergence declared)
**Exit**: completed frame string written with source citations; slot-binding verified; no mismatch

The inertia-advocate `orientation.frame` uses this template:

```
Teams using [Q1 current system] have [Q2 migration cost] invested. Ask whether this change
is worth [Q3 user habit] disruption before committing.
```

Fill each slot from its designated Phase 2 convergence answer:

```
## Frame Fill

Q1 slot <- Phase 2 Q1: [verbatim Phase 2 Q1 answer — from convergence Q1]
Q2 slot <- Phase 2 Q2: [verbatim Phase 2 Q2 answer — from convergence Q2]
Q3 slot <- Phase 2 Q3: [verbatim Phase 2 Q3 answer — from convergence Q3]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

**Slot-binding verification**:
- Q1 slot <- Q1 answer (not Q2, not Q3): YES/NO
- Q2 slot <- Q2 answer (not Q1, not Q3): YES/NO
- Q3 slot <- Q3 answer (not Q1, not Q2): YES/NO

All three must be YES. A cross-slot binding is a blocking error.

**Exit condition met**: frame string complete; source citations present; all three slot-binding
checks YES.

---

### Phase 4 — FRAME CONFIRM

**Entry**: Phase 3 complete (all slot-binding checks YES)
**Exit**: FRAME CONFIRM statement present; pasted string matches Phase 3 output character-for-
         character

Before scope audit or role writing, re-declare the Phase 3 frame string:

```
## Frame Confirm

FRAME CONFIRM: The inertia-advocate orientation.frame I will write in Phase 6 is:
"{paste Phase 3 completed frame string — character-for-character, including all punctuation}"
```

Rules:
- Paste verbatim — do not paraphrase, rephrase, or summarize
- If you cannot reproduce the Phase 3 output exactly, return to Phase 3 and regenerate the frame
  string, then re-attempt Phase 4
- This string is binding: Phase 6 inertia-advocate `orientation.frame` must match it exactly;
  Phase 7 CHECK 5 validates the match

**Exit condition met**: FRAME CONFIRM statement present with verbatim paste of Phase 3 output.

---

### Phase 5 — PRE-WRITE SCOPE AUDIT

**Entry**: Phase 4 complete
**Exit**: scope planning table shows at least 2 distinct scope values; writing blocked until pass

Before writing any role file, build the role plan:

| Planned Role       | Perspective | Scope      | Justification           |
|--------------------|-------------|------------|-------------------------|
| pm                 | product     | {scope}    | {one reason from input} |
| architect          | technical   | {scope}    | {one reason from input} |
| inertia-advocate   | inertia     | cross-team | status quo spans domain |
| {domain-specialist}| domain      | {scope}    | from Phase 1 vocabulary |

Add domain-specialist rows as needed. Scope definitions: `team`, `cross-team`, `org`.

**SCOPE AUDIT**: List distinct scope values. Gate: at least 2 distinct values.
If only 1: revise 1-2 roles. State changes. Confirm count >= 2.
`SCOPE AUDIT PASS — scope values: [list]`

Writing blocked until scope audit passes.

---

### Phase 6 — WRITE ROLE FILES

**Entry**: Phase 5 complete (scope audit passed)
**Exit**: all role files written; inertia-advocate frame matches Phase 4 FRAME CONFIRM string;
         inertia-advocate verify questions carry vocab-term annotations with terms present in
         question body; every `expertise.relevance` references a Phase 1 row-identified term

Write each role to `.roles/{area}/{role-slug}.md`. All 5 fields required.

**For non-inertia roles:**

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative: Remove / Defer / Collapse / Merge}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence referencing at least one Phase 1 row-identified term}

## scope
{value from Phase 5 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use the FRAME CONFIRM string from Phase 4 verbatim
- `orientation.verify`: exactly 3 questions; each must satisfy both conditions:
  1. Carries a vocab-term annotation:
     - Format: `{question ending in ?} [Q: Q1 — vocab: {CS-N} — {term-from-Phase-2-Q1}]`
     - Format: `{question ending in ?} [Q: Q2 — vocab: {MC-N} — {term-from-Phase-2-Q2}]`
     - Format: `{question ending in ?} [Q: Q3 — vocab: {UH-N} — {term-from-Phase-2-Q3}]`
     - The `{term}` in each annotation must match the vocabulary term recorded in Phase 2's
       convergence Q-answer for that Q-number
  2. The question text body contains the annotation `{term}` verbatim as a substring
     (e.g., if annotation says `[Q: Q2 — vocab: MC-1 — re-routing-cost]`, the phrase
     "re-routing-cost" must appear somewhere in the question text before the annotation tag;
     a question whose text never contains its annotation term fails this condition)
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: reference Phase 2 Q1 row identifier + at least one other Phase 1 term
- `scope`: cross-team
- `collaborates_with`: pm

Minimum 3 roles total; at least 3 distinct perspective categories.

**Exit condition met**: all files written; inertia-advocate frame matches Phase 4 FRAME CONFIRM;
each verify question has a valid annotation AND contains the annotation term in question body;
every `expertise.relevance` contains a Phase 1 row-identified term.

---

### Phase 7 — VERIFICATION GATE

**Entry**: Phase 6 complete
**Exit**: all 7 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. Complete all 7 checks in order. Each must declare PASS before the next
opens. Fix defects before proceeding.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. All cells filled. Role names match file stems exactly.
`CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

For every `collaborates_with` value: does a file with that name exist in this registry?
Flag: `{name} [UNRESOLVED]`. Add missing role or remove reference. State action.
Gate: zero unresolved references.
`CHECK 2: PASS` or `CHECK 2: FAIL — [action taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values from the written role files.
Gate: at least 2 distinct values.
If all identical: enforce now. State changes.
`CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each role's `expertise.relevance`: references a Phase 1 term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise; state term added.
Gate: all roles pass.
`CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

**CHECK 5 — Frame Confirm Match**

Compare the inertia-advocate `orientation.frame` against the Phase 4 FRAME CONFIRM string:

`Phase 4 FRAME CONFIRM: "{paste Phase 4 string}"`
`Inertia-advocate frame: "{paste Phase 6 frame value}"`

Gate: strings are identical, character-for-character.
If different: flag `[FRAME MISMATCH]`. Rewrite to match Phase 4 FRAME CONFIRM exactly.
`CHECK 5: PASS — strings match` or `CHECK 5: FAIL — [FRAME MISMATCH; rewritten]`

---

**CHECK 6 — Verify-Question Vocab-Term Citation Coverage**

For each of the inertia-advocate's 3 verify questions, check five failure modes in order:

1. `{question text} [MISSING ANNOTATION]` — no `[Q: QN — vocab: ...]` tag present
2. `{question text} [Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M} dimension]`
3. `{question text} [TERM MISMATCH: annotation says "{term-A}", Phase 2 Q{N} recorded "{term-B}"]`
4. `{question text} [ROW-ID MISMATCH: annotation says {row-A}, Phase 2 Q{N} used {row-B}]`
5. `{question text} [TERM NOT IN QUESTION TEXT: annotation term "{term}" not found in question body]`

Each failure mode is independently emitted before the next is checked. A question may produce
multiple flags. Revise; confirm all 5 checks clear for all 3 questions.

Gate: all 3 verify questions pass all 5 checks.
`CHECK 6: PASS` or `CHECK 6: FAIL — [revisions made]`

---

**CHECK 7 — Replacement Provenance Audit**

For each replacement recorded in Phase 2's iteration log: does the record contain a Phase 1 row
citation (`{new-row-id} = "{term}" in Phase 1 {bucket}: "{source phrase}"`)? Can that row
identifier be found in Phase 1 output?

Flag: `Q{N} replacement "{old-term}" -> "{new-term}" [MISSING PHASE-1 CITATION]`
For each flagged: locate in Phase 1 or re-run Phase 2 with a term that exists in Phase 1.

Gate: every replacement cites a verifiable Phase 1 row, or no replacements were made.
`CHECK 7: PASS` or `CHECK 7: FAIL — [revisions made]`

---

All 7 checks declared PASS -> `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2-4; new FRAME CONFIRM and verify annotations with term-in-body required before Phase 7)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-02

**Axis**: Scope binding check (ES-2 — single axis)
**Hypothesis**: R12 V-05 Phase 5 builds a planning table that assigns each role a scope value
before writing begins. Phase 7 CHECK 3 confirms scope gradient exists in the written registry.
But CHECK 3 is a post-hoc aggregate check — it asks "do at least 2 distinct scope values appear
in what was written?" without asking "does each written scope value match what was planned?" A
role planned as `team` can be written as `cross-team` during Phase 6 without triggering CHECK 3
(the gradient still exists). The planning table's authority over scope decisions is unenforceable
under CHECK 3 alone because Phase 5 and Phase 6 are separately authored surfaces with no binding
mechanism between them. A SCOPE BINDING sub-check compares each role in the Phase 5 planning
table to its Phase 6 written scope, row by row. Any deviation is flagged
`[{role}: planned {A}, written {B} — SCOPE BINDING MISMATCH]`. The response to a mismatch is
explicit: either rewrite the role file to match the plan, or return to Phase 5 and amend the
plan with justification, then re-run the scope audit before proceeding. Silent scope substitution
during writing is a structural error, not a stylistic choice.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

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
  Phase 1 row — if a term has no row, add it to Phase 1 before using it as a replacement

**Exit condition met**: three non-empty buckets; each term has a row identifier; minimum 3 terms.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG WITH PROVENANCE

**Entry**: Phase 1 complete
**Exit**: convergence declared; all ATTEMPT blocks preserved; each replacement cites Phase 1 row

Answer three questions, citing Phase 1 row identifiers in each answer:

**Q1** (draw from Current-System Terms): What existing system, tool, or approach does the domain
currently rely on?
Required format: `Q1: [answer] [vocab: {CS-N} — {term}]`

**Q2** (draw from Migration-Cost Terms): What concrete cost or friction does moving away from Q1
create?
Required format: `Q2: [answer] [vocab: {MC-N} — {term}]`

**Q3** (draw from User-Habit Terms): What observable user workflow or daily behavior depends on Q1?
Required format: `Q3: [answer] [vocab: {UH-N} — {term}]`

After writing all three answers, open the iteration log:

---

**AUDIT ATTEMPT 1:**

| Q  | Row ID | Term Used | Expected Bucket | Match YES/NO |
|----|--------|-----------|-----------------|--------------|
| Q1 | {CS-N} | {term}    | Current-System  | YES/NO       |
| Q2 | {MC-N} | {term}    | Migration-Cost  | YES/NO       |
| Q3 | {UH-N} | {term}    | User-Habit      | YES/NO       |

If all rows YES:
`ATTEMPT 1 RESULT: ALL YES — Phase 2 convergence achieved.`

If any row NO:
`ATTEMPT 1 RESULT: BLOCKED — Q{N} row shows NO.`

Record replacement with Phase 1 provenance:
```
Replacement:
  Q{N} term "{old-term}" [{old-row-id}]
  -> "{new-term}" [{new-row-id}]
  Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"
```

If the new term has no Phase 1 row identifier, add it to Phase 1 first, then cite the row.

Restart the audit table from Q1. **Prior ATTEMPT blocks are not deleted.**

---

**AUDIT ATTEMPT 2:** (if ATTEMPT 1 BLOCKED)

Re-evaluate all three rows from Q1. Write a new table. Continue until convergence.

`AUDIT CONVERGENCE: ATTEMPT {N} ALL YES. {N} attempt(s) required.`
`Replacement provenance: [all replacements cite Phase 1 rows]` or `[no replacements made]`

**Exit condition met**: convergence declared; all ATTEMPT blocks preserved; each replacement carries
a Phase 1 row citation with source phrase.

---

### Phase 3 — FRAME FILL

**Entry**: Phase 2 complete (audit convergence declared)
**Exit**: completed frame string written with source citations; slot-binding verified; no mismatch

The inertia-advocate `orientation.frame` uses this template:

```
Teams using [Q1 current system] have [Q2 migration cost] invested. Ask whether this change
is worth [Q3 user habit] disruption before committing.
```

Fill each slot from its designated Phase 2 convergence answer:

```
## Frame Fill

Q1 slot <- Phase 2 Q1: [verbatim Phase 2 Q1 answer — from convergence Q1]
Q2 slot <- Phase 2 Q2: [verbatim Phase 2 Q2 answer — from convergence Q2]
Q3 slot <- Phase 2 Q3: [verbatim Phase 2 Q3 answer — from convergence Q3]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

**Slot-binding verification**:
- Q1 slot <- Q1 answer (not Q2, not Q3): YES/NO
- Q2 slot <- Q2 answer (not Q1, not Q3): YES/NO
- Q3 slot <- Q3 answer (not Q1, not Q2): YES/NO

All three must be YES. A cross-slot binding is a blocking error.

**Exit condition met**: frame string complete; source citations present; all three slot-binding
checks YES.

---

### Phase 4 — FRAME CONFIRM

**Entry**: Phase 3 complete (all slot-binding checks YES)
**Exit**: FRAME CONFIRM statement present; pasted string matches Phase 3 output character-for-
         character

```
## Frame Confirm

FRAME CONFIRM: The inertia-advocate orientation.frame I will write in Phase 6 is:
"{paste Phase 3 completed frame string — character-for-character, including all punctuation}"
```

Rules:
- Paste verbatim — do not paraphrase, rephrase, or summarize
- If you cannot reproduce the Phase 3 output exactly, return to Phase 3 and regenerate, then
  re-attempt Phase 4
- This string is binding: Phase 7 CHECK 5 validates the match

**Exit condition met**: FRAME CONFIRM statement present with verbatim paste of Phase 3 output.

---

### Phase 5 — PRE-WRITE SCOPE AUDIT

**Entry**: Phase 4 complete
**Exit**: scope planning table shows at least 2 distinct scope values; writing blocked until pass

Before writing any role file, build the role plan:

| Planned Role       | Perspective | Scope      | Justification           |
|--------------------|-------------|------------|-------------------------|
| pm                 | product     | {scope}    | {one reason from input} |
| architect          | technical   | {scope}    | {one reason from input} |
| inertia-advocate   | inertia     | cross-team | status quo spans domain |
| {domain-specialist}| domain      | {scope}    | from Phase 1 vocabulary |

Add domain-specialist rows as needed. Scope definitions: `team`, `cross-team`, `org`.

**SCOPE AUDIT**: List distinct scope values. Gate: at least 2 distinct values.
If only 1: revise 1-2 roles. State changes. Confirm count >= 2.
`SCOPE AUDIT PASS — scope values: [list]`

The scope values in this table are binding: Phase 6 role files must carry these exact scope
values. If you change a scope value while writing, you must return to Phase 5, update the table,
and confirm the scope audit still passes before proceeding.

Writing blocked until scope audit passes.

---

### Phase 6 — WRITE ROLE FILES

**Entry**: Phase 5 complete (scope audit passed)
**Exit**: all role files written; scope values match Phase 5 planning table exactly; inertia-
         advocate frame matches Phase 4 FRAME CONFIRM; verify questions carry vocab-term
         annotations; every `expertise.relevance` references a Phase 1 row-identified term

Write each role to `.roles/{area}/{role-slug}.md`. All 5 fields required.

**For non-inertia roles:**

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative: Remove / Defer / Collapse / Merge}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence referencing at least one Phase 1 row-identified term}

## scope
{value from Phase 5 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use the FRAME CONFIRM string from Phase 4 verbatim
- `orientation.verify`: exactly 3 questions; each carries a vocab-term annotation:
  - Format: `{question ending in ?} [Q: Q1 — vocab: {CS-N} — {term-from-Phase-2-Q1}]`
  - Format: `{question ending in ?} [Q: Q2 — vocab: {MC-N} — {term-from-Phase-2-Q2}]`
  - Format: `{question ending in ?} [Q: Q3 — vocab: {UH-N} — {term-from-Phase-2-Q3}]`
  - The `{term}` in each annotation must match Phase 2's convergence Q-answer term
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: reference Phase 2 Q1 row identifier + at least one other Phase 1 term
- `scope`: cross-team (from Phase 5 table — do not change)
- `collaborates_with`: pm

Minimum 3 roles total; at least 3 distinct perspective categories.

**Exit condition met**: all files written; scope values match Phase 5 table; inertia-advocate
frame matches Phase 4 FRAME CONFIRM; each verify question has a valid annotation; every
`expertise.relevance` contains a Phase 1 row-identified term.

---

### Phase 7 — VERIFICATION GATE

**Entry**: Phase 6 complete
**Exit**: all 7 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. Complete all 7 checks in order. Each must declare PASS before the next
opens. Fix defects before proceeding.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. All cells filled. Role names match file stems exactly.
`CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

For every `collaborates_with` value: does a file with that name exist in this registry?
Flag: `{name} [UNRESOLVED]`. Add missing role or remove reference. State action.
Gate: zero unresolved references.
`CHECK 2: PASS` or `CHECK 2: FAIL — [action taken]`

---

**CHECK 3 — Scope Gradient + Binding**

Part A — Gradient:
List distinct scope values from written role files. Gate: at least 2 distinct values.
If all identical: enforce now. State changes.
`CHECK 3A: PASS — scope values: [list]` or `CHECK 3A: FAIL — [action taken]`

Part B — Binding (runs only after CHECK 3A PASS):
Compare each role's Phase 5 planning-table scope to its Phase 6 written scope:

| Role | Phase 5 Planned Scope | Phase 6 Written Scope | Match? |
|------|-----------------------|-----------------------|--------|

Flag any mismatch: `[{role}: planned {A}, written {B} — SCOPE BINDING MISMATCH]`
For each flagged mismatch: choose one action —
  (a) Rewrite the role file to match the Phase 5 plan, or
  (b) Return to Phase 5, amend the plan with justification, re-run scope audit, then
      re-attempt Phase 6 writing for that role
State action taken. Confirm zero mismatches before PASS.

`CHECK 3: PASS` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each role's `expertise.relevance`: references a Phase 1 term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise; state term added.
Gate: all roles pass.
`CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

**CHECK 5 — Frame Confirm Match**

`Phase 4 FRAME CONFIRM: "{paste Phase 4 string}"`
`Inertia-advocate frame: "{paste Phase 6 frame value}"`

Gate: strings are identical, character-for-character.
If different: flag `[FRAME MISMATCH]`. Rewrite to match exactly.
`CHECK 5: PASS — strings match` or `CHECK 5: FAIL — [FRAME MISMATCH; rewritten]`

---

**CHECK 6 — Verify-Question Vocab-Term Citation Coverage**

For each of the inertia-advocate's 3 verify questions:

Flag each failure mode:
- `{question text} [MISSING ANNOTATION]`
- `{question text} [Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M} dimension]`
- `{question text} [TERM MISMATCH: annotation says "{term-A}", Phase 2 Q{N} recorded "{term-B}"]`
- `{question text} [ROW-ID MISMATCH: annotation says {row-A}, Phase 2 Q{N} used {row-B}]`

Revise; confirm annotation-dimension-term-row binding for all 3 questions.
Gate: all 3 verify questions have valid `[Q: QN — vocab: {row-id} — {term}]` annotations.
`CHECK 6: PASS` or `CHECK 6: FAIL — [revisions made]`

---

**CHECK 7 — Replacement Provenance Audit**

For each replacement in Phase 2's iteration log: contains a Phase 1 row citation
(`{new-row-id} = "{term}" in Phase 1 {bucket}: "{source phrase}"`) and row exists in Phase 1?

Flag: `Q{N} replacement "{old-term}" -> "{new-term}" [MISSING PHASE-1 CITATION]`
Gate: every replacement cites a verifiable Phase 1 row, or no replacements were made.
`CHECK 7: PASS` or `CHECK 7: FAIL — [revisions made]`

---

All 7 checks declared PASS -> `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(Phase 5 scope table updated; CHECK 3 binding re-run for new role)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2-4; new FRAME CONFIRM required)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5 and CHECK 3 binding)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-03

**Axis**: Convergence summary (single axis)
**Hypothesis**: R12 V-05 Phase 2 closes with `AUDIT CONVERGENCE: ATTEMPT {N} ALL YES.` The
convergence declaration confirms the iteration log reached all-YES but does not produce a
standalone output surface naming the final row-ids and terms for Q1/Q2/Q3. Phase 3 Frame Fill
consumes "Phase 2 convergence answers" by description — it draws from "the convergence Q1
answer," which requires tracing back through the iteration log to find the most recent all-YES
attempt. If the log has three attempts, the consumer must identify ATTEMPT 3's Q-answers as
authoritative. This is a trace burden, not a structural binding. A CONVERGENCE SUMMARY block
written immediately after convergence is declared collects the final row-ids and terms into a
single named surface. Phase 3 Frame Fill then consumes from CONVERGENCE SUMMARY Q1/Q2/Q3
entries, not from "convergence Q1 answer found in iteration log." Phase 5 verify-annotation
rules cite CONVERGENCE SUMMARY terms. The summary is not a new computation — it re-declares
what the iteration log already determined. Its structural value is that Phase 3 and Phase 6 have
an unambiguous single-point consumption target regardless of how many iteration attempts
occurred, and any discrepancy between the summary and the final ATTEMPT table is a flag rather
than an inference.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

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
  Phase 1 row — if a term has no row, add it to Phase 1 before using it as a replacement

**Exit condition met**: three non-empty buckets; each term has a row identifier; minimum 3 terms.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG + CONVERGENCE SUMMARY

**Entry**: Phase 1 complete
**Exit**: convergence declared; CONVERGENCE SUMMARY written; all ATTEMPT blocks preserved

Answer three questions, citing Phase 1 row identifiers in each answer:

**Q1** (draw from Current-System Terms): What existing system, tool, or approach does the domain
currently rely on?
Required format: `Q1: [answer] [vocab: {CS-N} — {term}]`

**Q2** (draw from Migration-Cost Terms): What concrete cost or friction does moving away from Q1
create?
Required format: `Q2: [answer] [vocab: {MC-N} — {term}]`

**Q3** (draw from User-Habit Terms): What observable user workflow or daily behavior depends on Q1?
Required format: `Q3: [answer] [vocab: {UH-N} — {term}]`

After writing all three answers, open the iteration log:

---

**AUDIT ATTEMPT 1:**

| Q  | Row ID | Term Used | Expected Bucket | Match YES/NO |
|----|--------|-----------|-----------------|--------------|
| Q1 | {CS-N} | {term}    | Current-System  | YES/NO       |
| Q2 | {MC-N} | {term}    | Migration-Cost  | YES/NO       |
| Q3 | {UH-N} | {term}    | User-Habit      | YES/NO       |

If all rows YES:
`ATTEMPT 1 RESULT: ALL YES — Phase 2 convergence achieved.`

If any row NO:
`ATTEMPT 1 RESULT: BLOCKED — Q{N} row shows NO.`

Record replacement with Phase 1 provenance:
```
Replacement:
  Q{N} term "{old-term}" [{old-row-id}]
  -> "{new-term}" [{new-row-id}]
  Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"
```

Restart from Q1. **Prior ATTEMPT blocks are not deleted.**

---

**AUDIT ATTEMPT 2:** (if ATTEMPT 1 BLOCKED)

Re-evaluate all three rows. Continue until convergence.

`AUDIT CONVERGENCE: ATTEMPT {N} ALL YES. {N} attempt(s) required.`

---

**CONVERGENCE SUMMARY** (written immediately after convergence is declared):

```
## Convergence Summary

Final Q-answers (canonical source for Phase 3 and Phase 6):

Q1-FINAL: [verbatim Q1 answer from convergence attempt] [vocab: {CS-N} — {term}]
Q2-FINAL: [verbatim Q2 answer from convergence attempt] [vocab: {MC-N} — {term}]
Q3-FINAL: [verbatim Q3 answer from convergence attempt] [vocab: {UH-N} — {term}]
```

Rules:
- Q1-FINAL through Q3-FINAL are copied verbatim from the all-YES ATTEMPT table, not rewritten
- If CONVERGENCE SUMMARY terms differ from the final ATTEMPT table, the summary is wrong;
  correct it before advancing to Phase 3
- Phase 3 Frame Fill consumes Q1-FINAL, Q2-FINAL, Q3-FINAL from this summary — not from the
  iteration log directly
- Phase 6 verify annotations cite the terms in this summary

**Exit condition met**: convergence declared; CONVERGENCE SUMMARY written; all ATTEMPT blocks
preserved; summary terms match final ATTEMPT table.

---

### Phase 3 — FRAME FILL

**Entry**: Phase 2 complete (convergence declared; CONVERGENCE SUMMARY written)
**Exit**: completed frame string written with source citations; slot-binding verified; no mismatch

The inertia-advocate `orientation.frame` uses this template:

```
Teams using [Q1 current system] have [Q2 migration cost] invested. Ask whether this change
is worth [Q3 user habit] disruption before committing.
```

Fill each slot from the Phase 2 CONVERGENCE SUMMARY (not from the iteration log directly):

```
## Frame Fill

Q1 slot <- CONVERGENCE SUMMARY Q1-FINAL: [verbatim Q1-FINAL answer]
Q2 slot <- CONVERGENCE SUMMARY Q2-FINAL: [verbatim Q2-FINAL answer]
Q3 slot <- CONVERGENCE SUMMARY Q3-FINAL: [verbatim Q3-FINAL answer]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

**Slot-binding verification**:
- Q1 slot <- Q1-FINAL (not Q2-FINAL, not Q3-FINAL): YES/NO
- Q2 slot <- Q2-FINAL (not Q1-FINAL, not Q3-FINAL): YES/NO
- Q3 slot <- Q3-FINAL (not Q1-FINAL, not Q2-FINAL): YES/NO

All three must be YES. A cross-slot binding is a blocking error.

**Exit condition met**: frame string complete; all three slot-binding checks YES.

---

### Phase 4 — FRAME CONFIRM

**Entry**: Phase 3 complete
**Exit**: FRAME CONFIRM statement present with verbatim Phase 3 paste

```
## Frame Confirm

FRAME CONFIRM: The inertia-advocate orientation.frame I will write in Phase 6 is:
"{paste Phase 3 completed frame string — character-for-character}"
```

Paste verbatim. If you cannot reproduce Phase 3 exactly, return to Phase 3 and regenerate.

**Exit condition met**: FRAME CONFIRM statement present with verbatim paste.

---

### Phase 5 — PRE-WRITE SCOPE AUDIT

**Entry**: Phase 4 complete
**Exit**: scope planning table shows at least 2 distinct scope values; writing blocked until pass

| Planned Role       | Perspective | Scope      | Justification           |
|--------------------|-------------|------------|-------------------------|
| pm                 | product     | {scope}    | {one reason from input} |
| architect          | technical   | {scope}    | {one reason from input} |
| inertia-advocate   | inertia     | cross-team | status quo spans domain |
| {domain-specialist}| domain      | {scope}    | from Phase 1 vocabulary |

**SCOPE AUDIT**: Gate: at least 2 distinct scope values.
If only 1: revise 1-2 roles. State changes.
`SCOPE AUDIT PASS — scope values: [list]`

Writing blocked until scope audit passes.

---

### Phase 6 — WRITE ROLE FILES

**Entry**: Phase 5 complete (scope audit passed)
**Exit**: all role files written; inertia-advocate frame matches Phase 4 FRAME CONFIRM; verify
         questions cite CONVERGENCE SUMMARY terms; every `expertise.relevance` references a
         Phase 1 row-identified term

Write each role to `.roles/{area}/{role-slug}.md`. All 5 fields required.

**For non-inertia roles:**

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative: Remove / Defer / Collapse / Merge}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence referencing at least one Phase 1 row-identified term}

## scope
{value from Phase 5 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use the FRAME CONFIRM string from Phase 4 verbatim
- `orientation.verify`: exactly 3 questions; each carries a vocab-term annotation citing
  the CONVERGENCE SUMMARY term for that Q:
  - Format: `{question ending in ?} [Q: Q1 — vocab: {CS-N} — {Q1-FINAL term}]`
  - Format: `{question ending in ?} [Q: Q2 — vocab: {MC-N} — {Q2-FINAL term}]`
  - Format: `{question ending in ?} [Q: Q3 — vocab: {UH-N} — {Q3-FINAL term}]`
  - Terms in annotations must match CONVERGENCE SUMMARY terms exactly; if annotation term
    differs from CONVERGENCE SUMMARY, it is a binding error — rewrite before proceeding
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: reference CONVERGENCE SUMMARY Q1-FINAL row identifier + at least one
  other Phase 1 term
- `scope`: cross-team
- `collaborates_with`: pm

Minimum 3 roles total; at least 3 distinct perspective categories.

**Exit condition met**: all files written; inertia-advocate frame matches Phase 4 FRAME CONFIRM;
verify annotations cite CONVERGENCE SUMMARY terms; every `expertise.relevance` contains a Phase 1
row-identified term.

---

### Phase 7 — VERIFICATION GATE

**Entry**: Phase 6 complete
**Exit**: all 7 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. Complete all 7 checks in order.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. All cells filled. Role names match file stems exactly.
`CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

Flag: `{name} [UNRESOLVED]`. Add missing role or remove reference.
Gate: zero unresolved references.
`CHECK 2: PASS` or `CHECK 2: FAIL — [action taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values. Gate: at least 2 distinct values.
If all identical: enforce now.
`CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each `expertise.relevance`: references a Phase 1 term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise; state term added.
`CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

**CHECK 5 — Frame Confirm Match**

`Phase 4 FRAME CONFIRM: "{paste Phase 4 string}"`
`Inertia-advocate frame: "{paste Phase 6 frame value}"`

Gate: identical, character-for-character.
`CHECK 5: PASS — strings match` or `CHECK 5: FAIL — [FRAME MISMATCH; rewritten]`

---

**CHECK 6 — Verify-Question Vocab-Term Citation Coverage**

For each verify question, flag:
- `[MISSING ANNOTATION]`
- `[Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M} dimension]`
- `[TERM MISMATCH: annotation says "{term-A}", CONVERGENCE SUMMARY Q{N}-FINAL recorded "{term-B}"]`
- `[ROW-ID MISMATCH: annotation says {row-A}, CONVERGENCE SUMMARY Q{N}-FINAL used {row-B}]`

Gate: all 3 verify questions pass all 4 checks.
`CHECK 6: PASS` or `CHECK 6: FAIL — [revisions made]`

---

**CHECK 7 — Replacement Provenance Audit**

For each replacement in Phase 2: contains forensic Phase 1 row citation? Row exists in Phase 1?
Flag: `Q{N} replacement "{old-term}" -> "{new-term}" [MISSING PHASE-1 CITATION]`
Gate: every replacement cites a verifiable Phase 1 row, or no replacements were made.
`CHECK 7: PASS` or `CHECK 7: FAIL — [revisions made]`

---

All 7 checks declared PASS -> `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2-4; new CONVERGENCE SUMMARY, FRAME CONFIRM, and verify annotations required)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-04

**Axis**: ES-1 + ES-2 combined — term-in-body enforcement + scope binding check
**Hypothesis**: V-01 closes the annotation-metadata vs question-body gap: CHECK 6 gains a fifth
failure mode requiring the annotation term to appear verbatim in the question text itself, not
just in the trailing tag. V-02 closes the scope planning-to-execution fidelity gap: CHECK 3
gains a Part B binding sub-check comparing Phase 5 planned scope to Phase 6 written scope
row-by-row. These two gaps are independent surfaces (question body vs tag; planning table vs
written file), so combining them does not create mutual dependencies — each axis adds a distinct
structural constraint to a different output artifact. V-04 tests whether both constraints can
coexist in a single skill without making Phase 6 or Phase 7 prohibitively complex. The expected
interaction: CHECK 3B raises the cost of silent scope drift during Phase 6 writing (which could
previously be corrected silently during CHECK 3); CHECK 6's fifth mode raises the cost of
annotation-only grounding for verify questions. Both raise the cost of undetectable deviation
without adding new phases.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

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

- Each term belongs to exactly one bucket; row identifiers are permanent; no renumbering
- Empty buckets: extend by inference; label `[inferred]` with basis
- Replacement terms in Phase 2 must have Phase 1 rows; add first if absent

**Exit condition met**: three non-empty buckets; each term has a row identifier; minimum 3 terms.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG WITH PROVENANCE

**Entry**: Phase 1 complete
**Exit**: convergence declared; all ATTEMPT blocks preserved; each replacement cites Phase 1 row

Answer three questions:

`Q1: [answer] [vocab: {CS-N} — {term}]` (draw from Current-System Terms)
`Q2: [answer] [vocab: {MC-N} — {term}]` (draw from Migration-Cost Terms)
`Q3: [answer] [vocab: {UH-N} — {term}]` (draw from User-Habit Terms)

Open iteration log:

**AUDIT ATTEMPT 1:**

| Q  | Row ID | Term Used | Expected Bucket | Match YES/NO |
|----|--------|-----------|-----------------|--------------|
| Q1 | {CS-N} | {term}    | Current-System  | YES/NO       |
| Q2 | {MC-N} | {term}    | Migration-Cost  | YES/NO       |
| Q3 | {UH-N} | {term}    | User-Habit      | YES/NO       |

ALL YES -> `ATTEMPT 1 RESULT: ALL YES — Phase 2 convergence achieved.`

Any NO -> `ATTEMPT 1 RESULT: BLOCKED — Q{N} row shows NO.`
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

**Exit condition met**: convergence declared; all blocks preserved; replacements carry Phase 1
citations.

---

### Phase 3 — FRAME FILL

**Entry**: Phase 2 complete
**Exit**: completed frame string written; all three slot-binding checks YES

```
## Frame Fill

Q1 slot <- Phase 2 Q1: [verbatim convergence Q1 answer]
Q2 slot <- Phase 2 Q2: [verbatim convergence Q2 answer]
Q3 slot <- Phase 2 Q3: [verbatim convergence Q3 answer]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

Slot-binding: Q1<-Q1, Q2<-Q2, Q3<-Q3 — all YES required. Cross-slot is blocking.

**Exit condition met**: frame complete; all slot-binding checks YES.

---

### Phase 4 — FRAME CONFIRM

**Entry**: Phase 3 complete
**Exit**: FRAME CONFIRM statement present with verbatim Phase 3 paste

```
## Frame Confirm

FRAME CONFIRM: "{paste Phase 3 completed frame string — character-for-character}"
```

Verbatim paste only. If unable, return to Phase 3 and regenerate.

**Exit condition met**: FRAME CONFIRM statement present.

---

### Phase 5 — PRE-WRITE SCOPE AUDIT

**Entry**: Phase 4 complete
**Exit**: planning table shows >= 2 distinct scope values; SCOPE AUDIT PASS declared

| Planned Role       | Perspective | Scope      | Justification           |
|--------------------|-------------|------------|-------------------------|
| pm                 | product     | {scope}    | {one reason from input} |
| architect          | technical   | {scope}    | {one reason from input} |
| inertia-advocate   | inertia     | cross-team | status quo spans domain |
| {domain-specialist}| domain      | {scope}    | from Phase 1 vocabulary |

Gate: >= 2 distinct scope values. If only 1: revise 1-2 roles.
`SCOPE AUDIT PASS — scope values: [list]`

Scope values in this table are binding for Phase 6. Any deviation during writing must be
corrected or returned to Phase 5 with justification before proceeding.

Writing blocked until scope audit passes.

---

### Phase 6 — WRITE ROLE FILES

**Entry**: Phase 5 complete
**Exit**: all role files written; scope values match Phase 5 table; inertia-advocate frame
         matches Phase 4; verify questions have annotations WITH terms in question body;
         every `expertise.relevance` references a Phase 1 term

Write each role to `.roles/{area}/{role-slug}.md`. All 5 fields required.

```markdown
# {Role Name}

## orientation
frame: {one sentence}
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence referencing at least one Phase 1 row-identified term}

## scope
{value from Phase 5 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use Phase 4 FRAME CONFIRM string verbatim
- `orientation.verify`: exactly 3 questions; BOTH conditions required per question:
  1. Carries annotation: `{question?} [Q: QN — vocab: {row-id} — {term-from-Phase-2-QN}]`
  2. Question text contains the annotation `{term}` verbatim as a substring
     — the term must appear in the question body, not only in the annotation tag
     — e.g., `"Has the team accounted for {term} costs?" [Q: Q2 — vocab: MC-1 — {term}]`
       where `{term}` appears in both the question text and the annotation
- `orientation.simplify`: 2+ imperatives
- `expertise.relevance`: Phase 2 Q1 row identifier + at least one other Phase 1 term
- `scope`: cross-team (from Phase 5 table)
- `collaborates_with`: pm

Minimum 3 roles; at least 3 distinct perspective categories.

---

### Phase 7 — VERIFICATION GATE

**Entry**: Phase 6 complete
**Exit**: all 7 checks PASS; GATE RESULT declared

**DELIVERY IS BLOCKED. All 7 checks in order.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |

One row per role. Role names match file stems.
`CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

Flag unresolved `collaborates_with` values. Gate: zero unresolved.
`CHECK 2: PASS` or `CHECK 2: FAIL — [action taken]`

---

**CHECK 3 — Scope Gradient + Binding**

Part A — Gradient: list distinct values; gate >= 2.
`CHECK 3A: PASS — scope values: [list]` or `CHECK 3A: FAIL — [action taken]`

Part B — Binding (after 3A PASS): compare Phase 5 planned to Phase 6 written per role:

| Role | Phase 5 Planned | Phase 6 Written | Match? |

Flag: `[{role}: planned {A}, written {B} — SCOPE BINDING MISMATCH]`
For each mismatch: (a) rewrite file to match plan, or (b) return to Phase 5, amend plan,
re-run scope audit, then re-write. State action. Gate: zero mismatches.

`CHECK 3: PASS` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

Flag: `{role-name} [NO VOCAB TERM]`. Revise. Gate: all pass.
`CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

**CHECK 5 — Frame Confirm Match**

Compare Phase 4 FRAME CONFIRM to Phase 6 written frame. Character-for-character.
Flag: `[FRAME MISMATCH]`. Rewrite to match.
`CHECK 5: PASS — strings match` or `CHECK 5: FAIL — [FRAME MISMATCH; rewritten]`

---

**CHECK 6 — Verify-Question Vocab-Term Citation Coverage**

For each of the inertia-advocate's 3 verify questions, emit all applicable flags in order:

1. `[MISSING ANNOTATION]` — no `[Q: QN — vocab: ...]` tag
2. `[Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M} dimension]`
3. `[TERM MISMATCH: annotation says "{term-A}", Phase 2 Q{N} recorded "{term-B}"]`
4. `[ROW-ID MISMATCH: annotation says {row-A}, Phase 2 Q{N} used {row-B}]`
5. `[TERM NOT IN QUESTION TEXT: annotation term "{term}" not found in question body]`

Each failure mode is independently emitted before the next is checked. Revise until all 5
checks clear for all 3 questions.

Gate: all 3 questions pass all 5 checks.
`CHECK 6: PASS` or `CHECK 6: FAIL — [revisions made]`

---

**CHECK 7 — Replacement Provenance Audit**

Flag: `Q{N} replacement "{old}" -> "{new}" [MISSING PHASE-1 CITATION]`
Gate: every replacement cites verifiable Phase 1 row, or no replacements made.
`CHECK 7: PASS` or `CHECK 7: FAIL — [revisions made]`

---

All 7 checks PASS -> `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(Phase 5 scope table updated; CHECK 3 binding re-run; CHECK 6 term-in-body validated for new inertia verify if re-characterized)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2-4; new verify questions must satisfy term-in-body condition)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5 and CHECK 3B binding)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-05

**Axis**: ES-1 + ES-2 + convergence summary — all three axes combined
**Hypothesis**: V-04 combines term-in-body enforcement (CHECK 6 fifth failure mode) and scope
binding (CHECK 3B row-by-row comparison). V-03 introduces a CONVERGENCE SUMMARY block at the
close of Phase 2 that makes Q1-FINAL/Q2-FINAL/Q3-FINAL available as named consumption targets
for Phase 3 Frame Fill and Phase 6 verify annotations, eliminating the trace-through-iteration-
log burden. Combining all three creates a skill where: (1) every verify question's annotation
term is independently verifiable both as a metadata assertion (annotation matches Phase 2) and
as a content constraint (term appears in question body); (2) scope decisions made in planning
cannot silently diverge from scope values written into files; (3) Phase 3 and Phase 6 consume
convergence answers from a single explicitly-named summary surface rather than from scattered
iteration log entries. The three axes reinforce distinct structural principles: term-in-body
closes annotation-vs-content divergence; scope binding closes planning-vs-execution divergence;
convergence summary closes iteration-log ambiguity on multi-attempt convergence. Together they
enforce citation discipline at three independent output surfaces without redundancy.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

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
  Phase 1 row — if a term has no row, add it to Phase 1 before using it as a replacement

**Exit condition met**: three non-empty buckets; each term has a row identifier; minimum 3 terms.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG + CONVERGENCE SUMMARY

**Entry**: Phase 1 complete
**Exit**: convergence declared; CONVERGENCE SUMMARY written with Q1-FINAL/Q2-FINAL/Q3-FINAL;
         all ATTEMPT blocks preserved; each replacement cites Phase 1 row

Answer three questions, citing Phase 1 row identifiers:

`Q1: [answer] [vocab: {CS-N} — {term}]` (draw from Current-System Terms)
`Q2: [answer] [vocab: {MC-N} — {term}]` (draw from Migration-Cost Terms)
`Q3: [answer] [vocab: {UH-N} — {term}]` (draw from User-Habit Terms)

Open iteration log:

---

**AUDIT ATTEMPT 1:**

| Q  | Row ID | Term Used | Expected Bucket | Match YES/NO |
|----|--------|-----------|-----------------|--------------|
| Q1 | {CS-N} | {term}    | Current-System  | YES/NO       |
| Q2 | {MC-N} | {term}    | Migration-Cost  | YES/NO       |
| Q3 | {UH-N} | {term}    | User-Habit      | YES/NO       |

ALL YES -> `ATTEMPT 1 RESULT: ALL YES — Phase 2 convergence achieved.`

Any NO -> `ATTEMPT 1 RESULT: BLOCKED — Q{N} row shows NO.`
Record replacement with Phase 1 provenance:
```
Replacement:
  Q{N} term "{old-term}" [{old-row-id}]
  -> "{new-term}" [{new-row-id}]
  Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"
```
If new term has no Phase 1 row, add it to Phase 1 first.
Prior ATTEMPT blocks are not deleted. Continue until convergence.

`AUDIT CONVERGENCE: ATTEMPT {N} ALL YES. {N} attempt(s) required.`

---

**CONVERGENCE SUMMARY** (written immediately after convergence; copied verbatim from final ATTEMPT):

```
## Convergence Summary

Q1-FINAL: [verbatim Q1 answer from convergence] [vocab: {CS-N} — {term}]
Q2-FINAL: [verbatim Q2 answer from convergence] [vocab: {MC-N} — {term}]
Q3-FINAL: [verbatim Q3 answer from convergence] [vocab: {UH-N} — {term}]
```

Validation: CONVERGENCE SUMMARY terms must match the final ATTEMPT table row for row. Any
discrepancy is a blocking error — correct the summary before advancing to Phase 3.

Phase 3 and Phase 6 consume EXCLUSIVELY from CONVERGENCE SUMMARY, not from the iteration log
directly. If CONVERGENCE SUMMARY does not exist or contains errors, do not advance.

**Exit condition met**: convergence declared; CONVERGENCE SUMMARY written; terms match final
ATTEMPT table; all blocks preserved; replacements carry Phase 1 citations.

---

### Phase 3 — FRAME FILL

**Entry**: Phase 2 complete (CONVERGENCE SUMMARY present)
**Exit**: completed frame string written; slot-binding verified; no mismatch

```
## Frame Fill

Q1 slot <- CONVERGENCE SUMMARY Q1-FINAL: [verbatim Q1-FINAL answer]
Q2 slot <- CONVERGENCE SUMMARY Q2-FINAL: [verbatim Q2-FINAL answer]
Q3 slot <- CONVERGENCE SUMMARY Q3-FINAL: [verbatim Q3-FINAL answer]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

Slot-binding:
- Q1 slot <- Q1-FINAL only: YES/NO
- Q2 slot <- Q2-FINAL only: YES/NO
- Q3 slot <- Q3-FINAL only: YES/NO

All YES required. Cross-slot is a blocking error.

**Exit condition met**: frame complete; all slot-binding checks YES; sources are CONVERGENCE SUMMARY
entries, not iteration log entries.

---

### Phase 4 — FRAME CONFIRM

**Entry**: Phase 3 complete
**Exit**: FRAME CONFIRM statement present; pasted string matches Phase 3 character-for-character

```
## Frame Confirm

FRAME CONFIRM: The inertia-advocate orientation.frame I will write in Phase 6 is:
"{paste Phase 3 completed frame string — character-for-character, including all punctuation}"
```

Verbatim paste only. Cannot reproduce -> return to Phase 3, regenerate, re-attempt.

**Exit condition met**: FRAME CONFIRM statement present with verbatim Phase 3 paste.

---

### Phase 5 — PRE-WRITE SCOPE AUDIT

**Entry**: Phase 4 complete
**Exit**: planning table shows >= 2 distinct scope values; SCOPE AUDIT PASS declared; scope
         values binding for Phase 6

| Planned Role       | Perspective | Scope      | Justification           |
|--------------------|-------------|------------|-------------------------|
| pm                 | product     | {scope}    | {one reason from input} |
| architect          | technical   | {scope}    | {one reason from input} |
| inertia-advocate   | inertia     | cross-team | status quo spans domain |
| {domain-specialist}| domain      | {scope}    | from Phase 1 vocabulary |

Gate: >= 2 distinct scope values. If only 1: revise 1-2 roles. Confirm.
`SCOPE AUDIT PASS — scope values: [list]`

**Scope values in this table are binding.** If a scope value changes during Phase 6 writing,
stop: either rewrite to match the plan, or return to Phase 5, update the plan with justification,
re-run scope audit, then re-attempt the affected Phase 6 file.

Writing blocked until scope audit passes.

---

### Phase 6 — WRITE ROLE FILES

**Entry**: Phase 5 complete (scope audit passed)
**Exit**: all role files written; scope matches Phase 5 table; inertia-advocate frame matches
         Phase 4 FRAME CONFIRM; verify questions carry annotations with terms present in body;
         every `expertise.relevance` references a Phase 1 row-identified term

Write each role to `.roles/{area}/{role-slug}.md`. All 5 fields required.

**For non-inertia roles:**

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative: Remove / Defer / Collapse / Merge}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence referencing at least one Phase 1 row-identified term}

## scope
{value from Phase 5 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use Phase 4 FRAME CONFIRM string verbatim — not from Phase 3, not
  from memory; consume the Phase 4 FRAME CONFIRM statement directly
- `orientation.verify`: exactly 3 questions; BOTH conditions required per question:
  1. Carries annotation citing CONVERGENCE SUMMARY term:
     - `{question?} [Q: Q1 — vocab: {CS-N} — {Q1-FINAL term from CONVERGENCE SUMMARY}]`
     - `{question?} [Q: Q2 — vocab: {MC-N} — {Q2-FINAL term from CONVERGENCE SUMMARY}]`
     - `{question?} [Q: Q3 — vocab: {UH-N} — {Q3-FINAL term from CONVERGENCE SUMMARY}]`
  2. The annotation `{term}` appears verbatim as a substring in the question text body
     (the term must appear before the annotation tag in the question text itself)
  — A question whose text does not contain the annotation term fails condition 2 and must be
    rewritten before Phase 7; do not proceed to Phase 7 with unannotated or term-absent questions
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: reference CONVERGENCE SUMMARY Q1-FINAL row identifier + at least one
  other Phase 1 term
- `scope`: cross-team (from Phase 5 table — do not change)
- `collaborates_with`: pm

Minimum 3 roles total; at least 3 distinct perspective categories.

**Exit condition met**: all files written; scope matches Phase 5 table; inertia-advocate frame
matches Phase 4 FRAME CONFIRM; each verify question has a valid annotation AND contains the
annotation term verbatim in the question body; every `expertise.relevance` contains a Phase 1
row-identified term.

---

### Phase 7 — VERIFICATION GATE

**Entry**: Phase 6 complete
**Exit**: all 7 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. Complete all 7 checks in order. Each must declare PASS before the next
opens. Fix defects before proceeding.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. All cells filled. Role names match file stems exactly.
`CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

For every `collaborates_with` value: file exists in registry?
Flag: `{name} [UNRESOLVED]`. Add missing role or remove reference.
Gate: zero unresolved references.
`CHECK 2: PASS` or `CHECK 2: FAIL — [action taken]`

---

**CHECK 3 — Scope Gradient + Binding**

Part A — Gradient:
List distinct scope values from written files. Gate: >= 2 distinct values.
If all identical: enforce now. State changes.
`CHECK 3A: PASS — scope values: [list]` or `CHECK 3A: FAIL — [action taken]`

Part B — Binding (runs only after CHECK 3A PASS):

| Role | Phase 5 Planned Scope | Phase 6 Written Scope | Match? |
|------|-----------------------|-----------------------|--------|

Flag: `[{role}: planned {A}, written {B} — SCOPE BINDING MISMATCH]`
For each mismatch: (a) rewrite file to match Phase 5, or (b) return to Phase 5, amend with
justification, re-run scope audit, re-write. State action. Gate: zero mismatches.

`CHECK 3: PASS` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each `expertise.relevance`: references a Phase 1 term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise; state term added. Gate: all pass.
`CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

**CHECK 5 — Frame Confirm Match**

`Phase 4 FRAME CONFIRM: "{paste Phase 4 string}"`
`Inertia-advocate frame: "{paste Phase 6 frame value}"`

Gate: identical, character-for-character. Flag: `[FRAME MISMATCH]`. Rewrite to match.
`CHECK 5: PASS — strings match` or `CHECK 5: FAIL — [FRAME MISMATCH; rewritten]`

---

**CHECK 6 — Verify-Question Vocab-Term Citation Coverage**

For each of the inertia-advocate's 3 verify questions, emit all applicable flags:

1. `{question} [MISSING ANNOTATION]`
2. `{question} [Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M}]`
3. `{question} [TERM MISMATCH: annotation says "{term-A}", CONVERGENCE SUMMARY Q{N}-FINAL
   recorded "{term-B}"]`
4. `{question} [ROW-ID MISMATCH: annotation says {row-A}, CONVERGENCE SUMMARY Q{N}-FINAL
   used {row-B}]`
5. `{question} [TERM NOT IN QUESTION TEXT: annotation term "{term}" not found in question body]`

Each failure mode is independently emitted before the next is checked; a question may receive
multiple flags. Revise; confirm all 5 checks clear for all 3 questions before PASS.

Gate: all 3 questions pass all 5 checks.
`CHECK 6: PASS` or `CHECK 6: FAIL — [revisions made]`

---

**CHECK 7 — Replacement Provenance Audit**

For each replacement in Phase 2's iteration log: contains forensic Phase 1 citation
(`{new-row-id} = "{term}" in Phase 1 {bucket}: "{source phrase}"`) and row verifiable in Phase 1?

Flag: `Q{N} replacement "{old-term}" -> "{new-term}" [MISSING PHASE-1 CITATION]`
Gate: every replacement cites verifiable Phase 1 row, or no replacements made.
`CHECK 7: PASS` or `CHECK 7: FAIL — [revisions made]`

---

All 7 checks declared PASS -> `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(Phase 5 scope table updated; CHECK 3B binding re-run for new role; CHECK 6 term-in-body validated if inertia re-characterized)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2-4; new CONVERGENCE SUMMARY, FRAME CONFIRM, verify annotations with term-in-body required before Phase 7)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5 and CHECK 3B binding)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`
