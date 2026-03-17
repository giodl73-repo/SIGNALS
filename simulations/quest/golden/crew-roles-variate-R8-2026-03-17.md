---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 8
rubric: crew-roles-rubric-v6-2026-03-17.md
---

# crew-roles — Variate R8

5 complete prompt body variations for the `crew-roles` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

**Baseline**: R7 V-01 scored 100/100 against rubric v6 (all 25 criteria). Only V-01 was scored
in R7 — no competing alternatives exist at this rubric level.

**R7 excellence signals driving R8 axes**:

- **ES-1 — Verify-question source binding is soft**: Phase 3 Frame Fill applies citation
  discipline (`Q1 slot ← Phase 2 Q1: [verbatim]`) to the frame string but not to the inertia-
  advocate `orientation.verify` fields. A verify question satisfies C-12/C-22 by naming the
  Q-dimension semantically without a traceable binding to a specific Phase 2 answer. The same
  implicit-population error C-25 closes for the frame string remains open for verify questions.

- **ES-2 — Discarded audit iterations are not preserved**: Phase 2 requires restarting from Q1
  on any NO row, but the instruction to "repeat until all three rows show YES" overwrites each
  failed attempt. The final all-YES table is structurally complete, but the replacement term's
  bucket origin is unverifiable — a term drawn from outside the correct bucket can pass its row
  in re-evaluation without leaving any record of the prior attempt.

**Variation axes**:
- V-01 (single): Verify-question source citation — extends Phase 3 citation discipline to verify fields
- V-02 (single): Audit iteration log — numbers and preserves all Phase 2 restart attempts in output
- V-03 (single): Inertia-first sequence — Q1 anchor answered before bucketed vocabulary extraction
- V-04 (combined): ES-1 + ES-2 — uniform Phase 2 citation discipline across frame and verify
- V-05 (combined): ES-1 + ES-2 + Inertia-first — full synthesis with all three axes

---

## V-01

**Axis**: Verify-question source citation (ES-1 — single axis)
**Hypothesis**: Extending the slot-citation discipline from Phase 3 (frame string slots) to the
inertia-advocate `orientation.verify` fields — requiring each question to carry a `[Q: Q1|Q2|Q3]`
annotation — closes the implicit-dimension gap ES-1 identifies. A verify question that names a
dimension semantically without binding to a Phase 2 answer cannot satisfy a structural citation
requirement. Applying the same discipline across all Phase 2-derived output (frame + verify)
makes the binding machine-checkable at the verification gate, not dependent on a semantic audit.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.craft/roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**6 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets written; each bucket non-empty; minimum 3 terms total

Read the input. Extract domain terms and assign each to exactly one of three named buckets:

```
## Domain Vocabulary

Current-System Terms: [terms naming the existing system, tool, API, or component being displaced]
Migration-Cost Terms: [terms naming effort, friction, risk, or transition investment]
User-Habit Terms: [terms naming workflows, mental models, or behaviors tied to the current system]
```

Assignment rules:
- Each term belongs to exactly one bucket; a term may not appear in two buckets
- If the input yields fewer than one term per bucket, extend by inference; label inferred terms
  `[inferred]` and state the basis: "inferred from [X] because [reason]"
- Proper nouns and named systems → Current-System Terms; cost and effort vocabulary →
  Migration-Cost Terms; workflow and behavioral vocabulary → User-Habit Terms

**Exit condition met**: three non-empty buckets, minimum 3 terms total.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION + AUDIT

**Entry**: Phase 1 complete
**Exit**: audit table shows all three rows YES after a full-pass re-evaluation from row 1;
         exit condition evaluated as a unit — per-row convergence does not satisfy this gate

Answer three questions. Each answer draws from its designated bucket:

**Q1** (draw from Current-System Terms): What existing system, tool, or approach does the domain
currently rely on?
Required format: `Q1: [answer] [vocab: {term-from-Current-System-bucket}]`

**Q2** (draw from Migration-Cost Terms): What concrete cost or friction does moving away from Q1
create?
Required format: `Q2: [answer] [vocab: {term-from-Migration-Cost-bucket}]`

**Q3** (draw from User-Habit Terms): What observable user workflow or daily behavior depends on Q1?
Required format: `Q3: [answer] [vocab: {term-from-User-Habit-bucket}]`

After writing all three answers, produce the domain-alignment audit table:

| Q  | Term Used | Expected Bucket  | Match YES/NO |
|----|-----------|------------------|--------------|
| Q1 | {term}    | Current-System   | YES/NO       |
| Q2 | {term}    | Migration-Cost   | YES/NO       |
| Q3 | {term}    | User-Habit       | YES/NO       |

**Restart protocol**: If any row shows NO, identify the failing answer and replace its term with a
term from the correct bucket. Then restart the audit table from Q1 — do not re-score only the
replaced row. Evaluate all three rows simultaneously as a unit. Repeat until all three show YES
in a single full-pass evaluation.

**Exit condition met**: audit table with all three rows YES, produced by a full-pass evaluation.

---

### Phase 3 — FRAME FILL

**Entry**: Phase 2 complete (all-YES audit table)
**Exit**: completed frame string written with source citations; slot-binding verified; no mismatch

The inertia-advocate `orientation.frame` uses this template:

```
Teams using [Q1 current system] have [Q2 migration cost] invested. Ask whether this change
is worth [Q3 user habit] disruption before committing.
```

Fill each slot from its designated Phase 2 answer:

```
## Frame Fill

Q1 slot ← Phase 2 Q1: [verbatim Phase 2 Q1 answer]
Q2 slot ← Phase 2 Q2: [verbatim Phase 2 Q2 answer]
Q3 slot ← Phase 2 Q3: [verbatim Phase 2 Q3 answer]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

**Slot-binding verification**: Q1 slot drawn from Q1 answer; Q2 slot drawn from Q2 answer; Q3
slot drawn from Q3 answer. A slot populated from the wrong answer is a blocking error. Verify
before declaring Phase 3 complete.

**Exit condition met**: completed frame string written; source citations present; no slot-binding
mismatch.

---

### Phase 4 — PRE-WRITE SCOPE AUDIT

**Entry**: Phase 3 complete
**Exit**: scope planning table shows at least 2 distinct scope values; writing blocked until pass

Before writing any role file, build the role plan:

| Planned Role       | Perspective | Scope      | Justification           |
|--------------------|-------------|------------|-------------------------|
| pm                 | product     | {scope}    | {one reason from input} |
| architect          | technical   | {scope}    | {one reason from input} |
| inertia-advocate   | inertia     | cross-team | status quo spans domain |
| {domain-specialist}| domain      | {scope}    | from Phase 1 vocabulary |

Scope definitions: `team` (one team), `cross-team` (2+ teams), `org` (org-wide alignment)

Add domain-specialist rows for Phase 1 vocabulary systems or patterns that PM and Architect
cannot represent. Minimum 4 rows including inertia-advocate.

**SCOPE AUDIT**:
1. List distinct scope values from the Scope column.
2. Gate condition: at least 2 distinct values.
3. If only 1 value: revise 1–2 roles. State "Revised {role} scope {old} → {new}: {reason}."
4. Confirm count ≥ 2.

`SCOPE AUDIT PASS — scope values: [list]`

Writing is blocked until scope audit passes.

---

### Phase 5 — WRITE ROLE FILES

**Entry**: Phase 4 complete (scope audit passed)
**Exit**: all role files written; inertia-advocate verify questions carry `[Q:]` citations;
         every `expertise.relevance` references a Phase 1 term

Write each role to `.craft/roles/{area}/{role-slug}.md`. All 5 fields required.

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
relevance: {sentence referencing at least one Phase 1 vocabulary term}

## scope
{value from Phase 4 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.craft/roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use the Phase 3 completed frame string verbatim
- `orientation.verify`: exactly 3 questions; each carries a Q-source citation in this format:
  - `{question referencing Q1 current system dimension, ending in ?} [Q: Q1]`
  - `{question referencing Q2 migration cost dimension, ending in ?} [Q: Q2]`
  - `{question referencing Q3 user habit dimension, ending in ?} [Q: Q3]`
  - A question whose `[Q:]` annotation does not match the dimension it draws from is a binding
    error; rewrite before proceeding. A verify question without a `[Q:]` annotation fails Phase 5.
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: reference Q1 vocab term + at least one other Phase 1 term
- `scope`: cross-team (from Phase 4 table)
- `collaborates_with`: pm

Roles span at least 3 distinct perspective categories (product, technical, inertia, domain-
specialist). Minimum 3 roles total including inertia-advocate.

**Exit condition met**: all files written; each inertia-advocate verify question has a `[Q:]`
annotation matching its Q-dimension; every `expertise.relevance` contains a Phase 1 term.

---

### Phase 6 — VERIFICATION GATE

**Entry**: Phase 5 complete
**Exit**: all 5 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. Complete all 5 checks in order. Each must declare PASS before the next
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
Flag: `{name} [UNRESOLVED]`. For each: add missing role OR remove reference. State action.
Gate condition: zero unresolved references.
`CHECK 2: PASS` or `CHECK 2: FAIL — [action taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values from Scope column.
Gate condition: at least 2 distinct values.
If all identical: enforce now — revise 1–2 roles. State changes.
`CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each role's `expertise.relevance`: does it reference a Phase 1 vocabulary term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise; state which term was added.
Gate condition: all roles pass.
`CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

**CHECK 5 — Verify-Question Citation Coverage**

For the inertia-advocate's `orientation.verify` fields: does each question carry a `[Q:]`
annotation? Does each annotation match the Q-dimension the question references?
Flag: `{question text} [MISSING CITATION]` or `{question text} [CITATION MISMATCH: expected Q2,
found Q1 content]`. Revise; confirm annotation-dimension binding.
Gate condition: all 3 verify questions have valid, matching `[Q:]` annotations.
`CHECK 5: PASS` or `CHECK 5: FAIL — [revisions made]`

---

All 5 checks declared PASS → `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phase 2; frame and inertia-advocate rewrite)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 4)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 6)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-02

**Axis**: Audit iteration log (ES-2 — single axis)
**Hypothesis**: The Phase 2 restart protocol's weakness is not that replacement is allowed but
that the replacement decision leaves no evidence in the output. When a failed attempt is
overwritten, the replacement term's bucket origin cannot be verified after convergence — a term
inferred from context rather than drawn from the correct bucket can produce an all-YES table
indistinguishable from a correctly-sourced one. Numbering each restart attempt and requiring all
prior blocks to remain in the output creates a permanent record of what was replaced, why, and
from which bucket the replacement came. The replacement term's provenance is visible alongside
the convergence result.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.craft/roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**6 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets written; each bucket non-empty; minimum 3 terms total

Read the input. Extract domain terms and assign each to exactly one of three named buckets:

```
## Domain Vocabulary

Current-System Terms: [terms naming the existing system, tool, API, or component being displaced]
Migration-Cost Terms: [terms naming effort, friction, risk, or transition investment]
User-Habit Terms: [terms naming workflows, mental models, or behaviors tied to the current system]
```

Each term belongs to exactly one bucket. If any bucket is empty, extend by inference; label
inferred terms `[inferred]` with basis.

**Exit condition met**: three non-empty buckets, minimum 3 terms total.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG

**Entry**: Phase 1 complete
**Exit**: the most recent AUDIT ATTEMPT block shows ALL YES; all prior ATTEMPT blocks are
         preserved in the output; convergence declared after the final all-YES attempt

Answer three questions. Each answer draws from its designated bucket:

**Q1** (draw from Current-System Terms): What existing system, tool, or approach does the domain
currently rely on?
Required format: `Q1: [answer] [vocab: {term-from-Current-System-bucket}]`

**Q2** (draw from Migration-Cost Terms): What concrete cost or friction does moving away from Q1
create?
Required format: `Q2: [answer] [vocab: {term-from-Migration-Cost-bucket}]`

**Q3** (draw from User-Habit Terms): What observable user workflow or daily behavior depends on Q1?
Required format: `Q3: [answer] [vocab: {term-from-User-Habit-bucket}]`

After writing all three answers, open the iteration log:

---

**AUDIT ATTEMPT 1:**

| Q  | Term Used | Expected Bucket  | Match YES/NO |
|----|-----------|------------------|--------------|
| Q1 | {term}    | Current-System   | YES/NO       |
| Q2 | {term}    | Migration-Cost   | YES/NO       |
| Q3 | {term}    | User-Habit       | YES/NO       |

If all rows YES:
`ATTEMPT 1 RESULT: ALL YES — Phase 2 convergence achieved.`

If any row NO:
`ATTEMPT 1 RESULT: BLOCKED — Q[N] row shows NO.`
Record the replacement decision:
`Replacement: Q[N] term "{old-term}" → "{new-term}" drawn from [bucket name]. Basis: [one-line
reasoning confirming new-term belongs to the expected bucket, not inferred from context].`
Rewrite the affected Q-answer using the replacement term.

---

**AUDIT ATTEMPT 2:** (if ATTEMPT 1 BLOCKED)

Re-evaluate all three Q-answers starting from Q1. Write a new table:

| Q  | Term Used | Expected Bucket  | Match YES/NO |
|----|-----------|------------------|--------------|
| Q1 | {term}    | Current-System   | YES/NO       |
| Q2 | {term}    | Migration-Cost   | YES/NO       |
| Q3 | {term}    | User-Habit       | YES/NO       |

**ATTEMPT 1 block is not deleted.** Both ATTEMPT 1 and ATTEMPT 2 appear in the output.
The output for Phase 2 is the complete iteration log, not only the convergence table.

If ATTEMPT 2 shows any NO: record replacement decision and open ATTEMPT 3. Continue.

---

`AUDIT CONVERGENCE: ATTEMPT [N] ALL YES. [N] attempt(s) required.`

If N = 1: no replacements were made.
If N > 1: replacements are recorded in the ATTEMPT blocks above with bucket source.

**Exit condition met**: convergence declared; all prior attempt blocks preserved in output.

---

### Phase 3 — FRAME FILL

**Entry**: Phase 2 complete (audit convergence declared)
**Exit**: completed frame string written with source citations; slot-binding verified

The inertia-advocate `orientation.frame` uses this template:

```
Teams using [Q1 current system] have [Q2 migration cost] invested. Ask whether this change
is worth [Q3 user habit] disruption before committing.
```

```
## Frame Fill

Q1 slot ← Phase 2 Q1: [verbatim Phase 2 Q1 answer — from convergence Q1]
Q2 slot ← Phase 2 Q2: [verbatim Phase 2 Q2 answer — from convergence Q2]
Q3 slot ← Phase 2 Q3: [verbatim Phase 2 Q3 answer — from convergence Q3]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

Slot-binding verification: each slot draws from its own Q answer. A slot populated from the
wrong Q answer is a blocking error.

**Exit condition met**: frame string complete; source citations present; no slot-binding mismatch.

---

### Phase 4 — PRE-WRITE SCOPE AUDIT

**Entry**: Phase 3 complete
**Exit**: scope planning table shows at least 2 distinct scope values; writing blocked until pass

Before writing any role file, build the role plan:

| Planned Role       | Perspective | Scope      | Justification           |
|--------------------|-------------|------------|-------------------------|
| pm                 | product     | {scope}    | {one reason from input} |
| architect          | technical   | {scope}    | {one reason from input} |
| inertia-advocate   | inertia     | cross-team | status quo spans domain |
| {domain-specialist}| domain      | {scope}    | from Phase 1 vocabulary |

Add domain-specialist rows as needed. Scope definitions: `team`, `cross-team`, `org`.

**SCOPE AUDIT**: List distinct scope values. Gate condition: at least 2 distinct values.
If only 1: revise 1–2 roles. State changes. Confirm count ≥ 2.
`SCOPE AUDIT PASS — scope values: [list]`

Writing blocked until scope audit passes.

---

### Phase 5 — WRITE ROLE FILES

**Entry**: Phase 4 complete (scope audit passed)
**Exit**: all role files written; inertia-advocate frame uses Phase 3 text verbatim;
         every `expertise.relevance` references a Phase 1 term

Write each role to `.craft/roles/{area}/{role-slug}.md`. All 5 fields required.

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
relevance: {sentence referencing at least one Phase 1 vocabulary term}

## scope
{value from Phase 4 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.craft/roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use the Phase 3 completed frame string verbatim
- `orientation.verify`: 3 questions; at least 2 reference the Q1/Q2/Q3 dimensions by name
  (using the vocabulary terms from Phase 2 convergence Q-answers)
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: reference Q1 vocab term + one other Phase 1 term
- `scope`: cross-team (from Phase 4 table)
- `collaborates_with`: pm

Roles span at least 3 distinct perspective categories. Minimum 3 roles total.

**Exit condition met**: all files written; every `expertise.relevance` contains a Phase 1 term.

---

### Phase 6 — VERIFICATION GATE

**Entry**: Phase 5 complete
**Exit**: all 4 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. All 4 checks must declare PASS before output is delivered.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. All cells filled. Role names match file stems.
`CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

For every `collaborates_with` value: does a matching file exist in this registry?
Flag: `{name} [UNRESOLVED]`. Add missing role or remove reference. State action.
Gate condition: zero unresolved references.
`CHECK 2: PASS` or `CHECK 2: FAIL — [action taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values from Scope column. Gate condition: at least 2 distinct values.
If all identical: enforce now. State changes.
`CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each role's `expertise.relevance`: does it reference a Phase 1 term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise; state which term was added.
Gate condition: all roles pass.
`CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

All 4 checks declared PASS → `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + gate re-run)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phase 2 with fresh iteration log)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 4)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 6)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-03

**Axis**: Inertia-first sequence (inertia framing — single axis)
**Hypothesis**: In the standard phase order (vocabulary → Q&A), the three buckets are constructed
abstractly before Q1 is answered, then Q1 draws from the resulting bucket. The inertia-first
approach inverts this: name the current system first (Q1 anchor), then extract vocabulary using
that anchor as the lens — each bucket is populated by asking "what terms describe this specific
system?", "what terms describe the cost of leaving it?", "what terms describe behaviors built
around it?" This produces tighter bucket assignment because the current system name constrains
what belongs in each bucket from the start, eliminating vocabulary that is abstractly domain-
relevant but not anchored to the actual status quo.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.craft/roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — CURRENT-SYSTEM IDENTIFICATION

**Entry**: domain input provided
**Exit**: current system named as a proper noun; inertia anchor established for Phase 2

Read the input. Identify the current system, tool, or approach this domain displaces or extends.
This is the Q1 answer and the inertia anchor for all subsequent phases.

```
## Inertia Anchor

Current system (Q1): [named entity — proper noun or named tool/approach from input]
Basis: [one sentence: where in the input this was identified or why this is the status quo]
```

If the input does not name a current system explicitly, identify the closest status-quo equivalent
and name it. Label it `[inferred]` and state the basis.

**Exit condition met**: current system named; `Q1 = [named entity]` established.

---

### Phase 2 — ANCHORED VOCABULARY EXTRACTION

**Entry**: Phase 1 complete (Q1 = [current system name])
**Exit**: three named buckets written; each bucket non-empty; minimum 3 terms total;
         every term is anchored to the Phase 1 current system

Extract vocabulary from the input using the Phase 1 current system as the lens. Populate three
buckets by asking:

- **Current-System Terms**: What terms name this specific system and its components?
  (Not generic domain vocabulary — terms that specifically describe what Q1 is)
- **Migration-Cost Terms**: What terms name the cost, effort, or risk of moving away from Q1?
  (Transition cost relative to Q1, not abstract effort language)
- **User-Habit Terms**: What terms name behaviors, workflows, or mental models built around Q1?
  (Habits that exist because Q1 exists, not general user patterns)

```
## Domain Vocabulary (anchored to: {Q1 current system})

Current-System Terms: [terms naming the Q1 system and its components]
Migration-Cost Terms: [terms naming the cost of leaving Q1]
User-Habit Terms: [terms naming behaviors built around Q1]
```

Each term belongs to exactly one bucket. If any bucket is empty after reading the input, extend
by inference; label inferred terms `[inferred]` and state the Q1-anchored basis.

**Exit condition met**: three non-empty buckets; every term traceable to the Q1 anchor.

---

### Phase 3 — Q2/Q3 COMPLETION + AUDIT

**Entry**: Phase 2 complete (bucketed vocabulary anchored to Q1)
**Exit**: Q2 and Q3 answered from their respective buckets; audit table shows all three rows YES;
         exit condition evaluated as a unit from row 1

Q1 is already answered (Phase 1). Complete Q2 and Q3:

**Q2** (draw from Migration-Cost Terms): What concrete cost or friction does moving away from Q1
create?
Required format: `Q2: [answer] [vocab: {term-from-Migration-Cost-bucket}]`

**Q3** (draw from User-Habit Terms): What observable user workflow or daily behavior depends on Q1?
Required format: `Q3: [answer] [vocab: {term-from-User-Habit-bucket}]`

The complete Q-answer set:
```
## Inertia Pre-Characterization

Q1: [Phase 1 current system answer] [vocab: {term-from-Current-System-bucket}]
Q2: [answer] [vocab: {term-from-Migration-Cost-bucket}]
Q3: [answer] [vocab: {term-from-User-Habit-bucket}]
```

For Q1, select a Current-System Term that best represents the named entity from Phase 1.

After writing all three answers, produce the audit table:

| Q  | Term Used | Expected Bucket  | Match YES/NO |
|----|-----------|------------------|--------------|
| Q1 | {term}    | Current-System   | YES/NO       |
| Q2 | {term}    | Migration-Cost   | YES/NO       |
| Q3 | {term}    | User-Habit       | YES/NO       |

**Restart protocol**: If any row shows NO, replace that term with one from the correct bucket,
then restart the audit table from Q1. Evaluate all three rows as a unit. Repeat until all YES.

**Exit condition met**: audit table all-YES after a full-pass evaluation from row 1.

---

### Phase 4 — FRAME FILL

**Entry**: Phase 3 complete (all-YES audit table)
**Exit**: completed frame string with source citations; slot-binding verified

```
## Frame Fill

Q1 slot ← Phase 1 / Phase 3 Q1: [verbatim Q1 answer]
Q2 slot ← Phase 3 Q2: [verbatim Q2 answer]
Q3 slot ← Phase 3 Q3: [verbatim Q3 answer]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

Slot-binding verification: each slot drawn from its own Q answer. Mismatch is a blocking error.

**Exit condition met**: frame complete; citations present; no mismatch.

---

### Phase 5 — PRE-WRITE SCOPE AUDIT

**Entry**: Phase 4 complete
**Exit**: scope planning table shows at least 2 distinct scope values; writing blocked until pass

| Planned Role       | Perspective | Scope      | Justification           |
|--------------------|-------------|------------|-------------------------|
| pm                 | product     | {scope}    | {one reason from input} |
| architect          | technical   | {scope}    | {one reason from input} |
| inertia-advocate   | inertia     | cross-team | Q1 system spans domain  |
| {domain-specialist}| domain      | {scope}    | from Phase 2 vocabulary |

Domain specialists are derived from Phase 2 Current-System and Migration-Cost terms. Add rows
for any major component or transition challenge the PM and Architect cannot represent.

**SCOPE AUDIT**: List distinct scope values. Gate condition: at least 2 distinct values.
If only 1: revise 1–2 roles. State changes. Confirm count ≥ 2.
`SCOPE AUDIT PASS — scope values: [list]`

Writing blocked until scope audit passes.

---

### Phase 6 — WRITE ROLE FILES

**Entry**: Phase 5 complete (scope audit passed)
**Exit**: all role files written; inertia-advocate uses Phase 4 frame verbatim;
         every `expertise.relevance` references a Phase 2 vocabulary term

Write each role to `.craft/roles/{area}/{role-slug}.md`. All 5 fields required.

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
relevance: {sentence referencing at least one Phase 2 vocabulary term — anchored to Q1 system}

## scope
{value from Phase 5 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.craft/roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use the Phase 4 completed frame verbatim — frame names Q1 current system
  by its Phase 1 proper noun; no paraphrase permitted
- `orientation.verify`: 3 questions; at least 2 reference Q1/Q2/Q3 dimensions using Phase 3 terms
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: reference Phase 2 Current-System Term (Q1 anchor) + one other Phase 2 term
- `scope`: cross-team (from Phase 5 table)
- `collaborates_with`: pm

Roles span at least 3 distinct perspective categories. Minimum 3 roles total.

**Exit condition met**: all files written; inertia-advocate frame is Phase 4 text verbatim;
every `expertise.relevance` contains a Phase 2 term.

---

### Phase 7 — VERIFICATION GATE

**Entry**: Phase 6 complete
**Exit**: all 4 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. All 4 checks must declare PASS before output is delivered.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. All cells filled. Role names match file stems.
`CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

For every `collaborates_with` value: does a matching file exist in this registry?
Flag: `{name} [UNRESOLVED]`. Add missing role or remove reference. State action.
`CHECK 2: PASS` or `CHECK 2: FAIL — [action taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values. Gate condition: at least 2 distinct values.
If all identical: enforce now. State changes.
`CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each role's `expertise.relevance`: does it reference a Phase 2 vocabulary term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise; state which term was added.
`CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

All 4 checks declared PASS → `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + gate re-run)*
> - Re-anchor vocabulary: `/crew-roles {domain} --amend anchor` *(re-runs Phase 1 + Phase 2; re-derives Q2/Q3)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-04

**Axes**: Verify-question source citation + Audit iteration log (ES-1 + ES-2 — two-axis combination)
**Hypothesis**: ES-1 and ES-2 are the same underlying gap on two different surfaces: Phase 2
answer traceability is applied rigorously to the frame string (C-25) but not to verify questions
or audit table history. Applying citation discipline uniformly closes both surfaces simultaneously.
V-01 closes ES-1 (verify citations). V-02 closes ES-2 (iteration log). Neither alone closes the
other. Combined: every Phase 2-derived content item in the output carries traceable provenance —
the frame string via slot citations, the verify questions via `[Q:]` annotations, and all
replacement decisions via the numbered attempt log.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.craft/roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**6 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets written; each bucket non-empty; minimum 3 terms total

Read the input. Extract domain terms and assign each to exactly one of three named buckets:

```
## Domain Vocabulary

Current-System Terms: [terms naming the existing system, tool, API, or component being displaced]
Migration-Cost Terms: [terms naming effort, friction, risk, or transition investment]
User-Habit Terms: [terms naming workflows, mental models, or behaviors tied to the current system]
```

Each term belongs to exactly one bucket. Extend by inference if needed; label inferred terms
`[inferred]` with basis.

**Exit condition met**: three non-empty buckets, minimum 3 terms total.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG

**Entry**: Phase 1 complete
**Exit**: convergence declared with all-YES audit table; all prior attempt blocks preserved

Answer three questions from their designated buckets:

**Q1** (Current-System Terms): What existing system, tool, or approach does the domain rely on?
Required format: `Q1: [answer] [vocab: {term-from-Current-System-bucket}]`

**Q2** (Migration-Cost Terms): What concrete cost or friction does moving away from Q1 create?
Required format: `Q2: [answer] [vocab: {term-from-Migration-Cost-bucket}]`

**Q3** (User-Habit Terms): What observable workflow or behavior depends on Q1?
Required format: `Q3: [answer] [vocab: {term-from-User-Habit-bucket}]`

Iteration log — open with AUDIT ATTEMPT 1:

---

**AUDIT ATTEMPT 1:**

| Q  | Term Used | Expected Bucket  | Match YES/NO |
|----|-----------|------------------|--------------|
| Q1 | {term}    | Current-System   | YES/NO       |
| Q2 | {term}    | Migration-Cost   | YES/NO       |
| Q3 | {term}    | User-Habit       | YES/NO       |

If all YES: `ATTEMPT 1 RESULT: ALL YES — Phase 2 convergence achieved.`

If any NO:
`ATTEMPT 1 RESULT: BLOCKED — Q[N] row shows NO.`
`Replacement: Q[N] "{old-term}" → "{new-term}" from [bucket name]. Basis: [one-line confirmation
that new-term belongs to the expected bucket, not inferred from context].`
Rewrite the affected Q-answer. Open ATTEMPT 2.

---

**AUDIT ATTEMPT N:** (repeat as needed — all prior blocks remain in output)

Re-evaluate all three Q-answers from Q1 as a unit. Each restart writes a new numbered block.
Prior blocks are not deleted.

`AUDIT CONVERGENCE: ATTEMPT [N] ALL YES. [N] attempt(s) required.`

**Exit condition met**: convergence declared; all prior attempt blocks preserved.

---

### Phase 3 — FRAME FILL

**Entry**: Phase 2 complete (convergence declared)
**Exit**: completed frame string with source citations; slot-binding verified

```
## Frame Fill

Q1 slot ← Phase 2 Q1: [verbatim Q1 answer from convergence]
Q2 slot ← Phase 2 Q2: [verbatim Q2 answer from convergence]
Q3 slot ← Phase 2 Q3: [verbatim Q3 answer from convergence]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

Slot-binding verification: each slot drawn from its own Q answer. Mismatch is a blocking error.

**Exit condition met**: frame complete; citations present; no mismatch.

---

### Phase 4 — PRE-WRITE SCOPE AUDIT

**Entry**: Phase 3 complete
**Exit**: scope planning table shows at least 2 distinct scope values; writing blocked until pass

| Planned Role       | Perspective | Scope      | Justification           |
|--------------------|-------------|------------|-------------------------|
| pm                 | product     | {scope}    | {one reason from input} |
| architect          | technical   | {scope}    | {one reason from input} |
| inertia-advocate   | inertia     | cross-team | status quo spans domain |
| {domain-specialist}| domain      | {scope}    | from Phase 1 vocabulary |

Add domain-specialist rows as needed. Scope: `team`, `cross-team`, `org`.

**SCOPE AUDIT**: List distinct values. Gate: at least 2 distinct values.
If only 1: revise 1–2 roles. State changes. Confirm count ≥ 2.
`SCOPE AUDIT PASS — scope values: [list]`

Writing blocked until scope audit passes.

---

### Phase 5 — WRITE ROLE FILES

**Entry**: Phase 4 complete (scope audit passed)
**Exit**: all role files written; inertia-advocate verify questions carry `[Q:]` citations;
         frame uses Phase 3 text verbatim; every `expertise.relevance` references a Phase 1 term

Write each role to `.craft/roles/{area}/{role-slug}.md`. All 5 fields required.

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
relevance: {sentence referencing at least one Phase 1 vocabulary term}

## scope
{value from Phase 4 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.craft/roles/{area}/inertia-advocate.md`):

- `orientation.frame`: Phase 3 completed frame verbatim
- `orientation.verify`: exactly 3 questions; each carries a `[Q:]` source citation:
  - `{question referencing Q1 current system, ending in ?} [Q: Q1]`
  - `{question referencing Q2 migration cost, ending in ?} [Q: Q2]`
  - `{question referencing Q3 user habit, ending in ?} [Q: Q3]`
  - Annotation must match the dimension the question draws from. Mismatch or missing annotation
    is a blocking error; rewrite before proceeding.
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: Q1 vocab term + one other Phase 1 term
- `scope`: cross-team (from Phase 4 table)
- `collaborates_with`: pm

Roles span at least 3 distinct perspective categories. Minimum 3 roles total.

**Exit condition met**: all files written; each verify question has valid `[Q:]` annotation;
every `expertise.relevance` contains a Phase 1 term.

---

### Phase 6 — VERIFICATION GATE

**Entry**: Phase 5 complete
**Exit**: all 5 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. All 5 checks must declare PASS.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. All cells filled. Role names match file stems.
`CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

For every `collaborates_with` value: does a matching file exist?
Flag: `{name} [UNRESOLVED]`. Add or remove. State action.
`CHECK 2: PASS` or `CHECK 2: FAIL — [action taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values. Gate: at least 2 distinct values.
If all identical: enforce. State changes.
`CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each role's `expertise.relevance`: does it reference a Phase 1 term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise; state which term was added.
`CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

**CHECK 5 — Verify-Question Citation Coverage**

For each inertia-advocate `orientation.verify` question: does it carry a `[Q:]` annotation?
Does the annotation match the Q-dimension the question draws from?
Flag: `{question} [MISSING CITATION]` or `{question} [CITATION MISMATCH: annotation says Q2,
content draws from Q1]`. Revise; confirm binding.
Gate: all 3 verify questions have valid, matching `[Q:]` annotations.
`CHECK 5: PASS` or `CHECK 5: FAIL — [revisions made]`

---

All 5 checks declared PASS → `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + gate re-run)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(fresh Phase 2 iteration log; frame and inertia-advocate rewrite)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 4)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 6)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-05

**Axes**: Verify-question source citation + Audit iteration log + Inertia-first sequence
         (ES-1 + ES-2 + inertia framing — three-axis combination)
**Hypothesis**: The highest-integrity variation anchors the phase order in the inertia analysis
(V-03), preserves all Phase 2 evidence (V-02), and cites all Phase 2 derivations including verify
questions (V-01). The three axes reinforce each other: inertia-first ensures the current-system
anchor is established before any vocabulary is extracted, so bucket assignments are anchored
rather than abstract; the iteration log makes each replacement decision traceable to a bucket-
confirmed term; and verify citations make the traceability uniform across all Phase 2-derived
output. Together they eliminate the implicit-dimension and unverifiable-replacement gaps while
grounding the entire vocabulary structure in the named status quo.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.craft/roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — CURRENT-SYSTEM IDENTIFICATION

**Entry**: domain input provided
**Exit**: current system named as a proper noun; Q1 established; inertia anchor set

Read the input. Identify the current system, tool, or approach this domain displaces or extends.

```
## Inertia Anchor

Current system (Q1): [named entity — proper noun from input]
Basis: [one sentence: where in the input this appears, or why this is the status quo]
Q1 answer: [same named entity, formatted for Phase 3 audit]
```

Label `[inferred]` if not explicit in input; state basis.

**Exit condition met**: current system named; Q1 = [named entity].

---

### Phase 2 — ANCHORED VOCABULARY EXTRACTION

**Entry**: Phase 1 complete (Q1 anchor established)
**Exit**: three named buckets written; each non-empty; minimum 3 terms total;
         all terms anchored to the Phase 1 current system

Extract vocabulary using the Phase 1 anchor as the lens:

- **Current-System Terms**: terms naming the Q1 system and its components specifically
  (not generic domain vocabulary)
- **Migration-Cost Terms**: terms naming the cost of leaving Q1 specifically
  (transition cost relative to this system, not abstract effort language)
- **User-Habit Terms**: terms naming behaviors and workflows built around Q1 specifically
  (habits that exist because Q1 exists, not general user patterns)

```
## Domain Vocabulary (anchored to: {Q1})

Current-System Terms: [terms]
Migration-Cost Terms: [terms]
User-Habit Terms: [terms]
```

Each term belongs to exactly one bucket. Extend by inference if needed; label `[inferred]` with
Q1-anchored basis.

**Exit condition met**: three non-empty buckets; all terms traceable to Q1 anchor.

---

### Phase 3 — Q2/Q3 COMPLETION + AUDIT ITERATION LOG

**Entry**: Phase 2 complete (anchored vocabulary)
**Exit**: convergence declared with all-YES audit table; all prior attempt blocks preserved

Q1 is established (Phase 1). Complete Q2 and Q3 from their buckets:

**Q2** (Migration-Cost Terms): What concrete cost or friction does moving away from Q1 create?
Required format: `Q2: [answer] [vocab: {term-from-Migration-Cost-bucket}]`

**Q3** (User-Habit Terms): What observable workflow or behavior depends on Q1?
Required format: `Q3: [answer] [vocab: {term-from-User-Habit-bucket}]`

Full Q-answer set for audit:
```
Q1: [Phase 1 current system] [vocab: {Current-System term}]
Q2: [answer] [vocab: {Migration-Cost term}]
Q3: [answer] [vocab: {User-Habit term}]
```

Iteration log — open with AUDIT ATTEMPT 1:

---

**AUDIT ATTEMPT 1:**

| Q  | Term Used | Expected Bucket  | Match YES/NO |
|----|-----------|------------------|--------------|
| Q1 | {term}    | Current-System   | YES/NO       |
| Q2 | {term}    | Migration-Cost   | YES/NO       |
| Q3 | {term}    | User-Habit       | YES/NO       |

If all YES: `ATTEMPT 1 RESULT: ALL YES — Phase 3 convergence achieved.`

If any NO:
`ATTEMPT 1 RESULT: BLOCKED — Q[N] row shows NO.`
`Replacement: Q[N] "{old-term}" → "{new-term}" from [bucket name]. Basis: [one-line confirmation
that new-term is anchored to Q1 and belongs to the expected bucket — not inferred from context].`
Rewrite the affected Q-answer. Open ATTEMPT 2.

---

**AUDIT ATTEMPT N:** (all prior blocks remain in output — do not overwrite)

Re-evaluate all three Q-answers starting from Q1. Write a new numbered block.
`AUDIT CONVERGENCE: ATTEMPT [N] ALL YES. [N] attempt(s) required.`

**Exit condition met**: convergence declared; all attempt blocks preserved.

---

### Phase 4 — FRAME FILL

**Entry**: Phase 3 complete (convergence declared)
**Exit**: completed frame string with source citations; slot-binding verified

```
## Frame Fill

Q1 slot ← Phase 1 / Phase 3 Q1: [verbatim Q1 answer — Phase 1 named entity]
Q2 slot ← Phase 3 Q2: [verbatim Q2 answer from convergence]
Q3 slot ← Phase 3 Q3: [verbatim Q3 answer from convergence]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

Slot-binding verification: Q1 slot from Q1 (Phase 1 anchor), Q2 slot from Q2 answer, Q3 slot
from Q3 answer. A slot drawn from the wrong Q answer is a blocking error.

**Exit condition met**: frame complete; citations present; no mismatch.

---

### Phase 5 — PRE-WRITE SCOPE AUDIT

**Entry**: Phase 4 complete
**Exit**: scope planning table shows at least 2 distinct scope values; writing blocked until pass

| Planned Role       | Perspective | Scope      | Justification                   |
|--------------------|-------------|------------|---------------------------------|
| pm                 | product     | {scope}    | {one reason from input}         |
| architect          | technical   | {scope}    | {one reason from input}         |
| inertia-advocate   | inertia     | cross-team | Q1 system spans the full domain |
| {domain-specialist}| domain      | {scope}    | from Phase 2 vocabulary         |

Domain specialists derived from Phase 2 Current-System and Migration-Cost terms.
Scope: `team`, `cross-team`, `org`.

**SCOPE AUDIT**: List distinct values. Gate: at least 2 distinct values.
If only 1: revise 1–2 roles. State changes. Confirm count ≥ 2.
`SCOPE AUDIT PASS — scope values: [list]`

Writing blocked until scope audit passes.

---

### Phase 6 — WRITE ROLE FILES

**Entry**: Phase 5 complete (scope audit passed)
**Exit**: all role files written; inertia-advocate frame is Phase 4 text verbatim;
         verify questions carry `[Q:]` citations; every `expertise.relevance` references Phase 2 term

Write each role to `.craft/roles/{area}/{role-slug}.md`. All 5 fields required.

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
relevance: {sentence referencing at least one Phase 2 vocabulary term — anchored to Q1 system}

## scope
{value from Phase 5 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.craft/roles/{area}/inertia-advocate.md`):

- `orientation.frame`: Phase 4 completed frame verbatim — names Q1 Phase 1 proper noun; no
  paraphrase
- `orientation.verify`: exactly 3 questions; each carries a `[Q:]` source citation:
  - `{question referencing Q1 current system — the Phase 1 named entity, ending in ?} [Q: Q1]`
  - `{question referencing Q2 migration cost — the Phase 3 Q2 dimension, ending in ?} [Q: Q2]`
  - `{question referencing Q3 user habit — the Phase 3 Q3 dimension, ending in ?} [Q: Q3]`
  - Annotation must match the Q-dimension the question draws from. Mismatch or absent annotation
    is a blocking error. The Q1 verify question must reference the Phase 1 proper noun specifically
    (not a generic current-system description).
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: Phase 2 Current-System Term (Q1-anchored) + one other Phase 2 term
- `scope`: cross-team (from Phase 5 table)
- `collaborates_with`: pm

Roles span at least 3 distinct perspective categories. Minimum 3 roles total.

**Exit condition met**: all files written; verify citations present and matching; every
`expertise.relevance` contains a Phase 2 term anchored to Q1.

---

### Phase 7 — VERIFICATION GATE

**Entry**: Phase 6 complete
**Exit**: all 5 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. All 5 checks must declare PASS before output is delivered.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. All cells filled. Role names match file stems exactly.
`CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

For every `collaborates_with` value: does a matching file exist in this registry?
Flag: `{name} [UNRESOLVED]`. Add missing role or remove reference. State action.
Gate: zero unresolved references.
`CHECK 2: PASS` or `CHECK 2: FAIL — [action taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values. Gate: at least 2 distinct values.
If all identical: enforce. State changes.
`CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each role's `expertise.relevance`: does it reference a Phase 2 vocabulary term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise; state which term was added.
`CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

**CHECK 5 — Verify-Question Citation Coverage**

For each inertia-advocate `orientation.verify` question: does it carry a valid `[Q:]` annotation?
Does the annotation match the Q-dimension the question draws from? Does the Q1 question reference
the Phase 1 proper noun specifically?
Flag: `{question} [MISSING CITATION]` or `{question} [CITATION MISMATCH]` or
      `{question} [Q1 MISSING PROPER NOUN — references dimension generically, not Phase 1 entity]`.
Revise; confirm binding.
Gate: all 3 verify questions have valid, matching `[Q:]` annotations; Q1 question names the
Phase 1 proper noun.
`CHECK 5: PASS` or `CHECK 5: FAIL — [revisions made]`

---

All 5 checks declared PASS → `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + gate re-run)*
> - Re-anchor inertia: `/crew-roles {domain} --amend anchor` *(re-runs Phase 1; fresh Q1 propagates through Phase 2, 3, 4, 6)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`
