---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 12
rubric: crew-roles-rubric-v6-2026-03-17.md
---

# crew-roles — Variate R12

5 complete prompt body variations for the `crew-roles` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

**Baseline**: R11 V-05 (ES-1 + ES-2 combined, 100/100 against rubric v6). All 5 R11 variations
scored 100/100. The highest-integration baseline entering R12 is R11 V-05: verify questions carry
`[Q: Q1|Q2|Q3]` annotations validated by CHECK 5; Phase 2 restart attempts are numbered and
preserved with replacement provenance records.

**R11 excellence signals driving R12 axes**:

- **ES-1 — Vocabulary-grounded verify annotation is unverified**: R11 V-02 and V-05 require each
  inertia-advocate verify question to carry `[Q: Q1|Q2|Q3]`, and CHECK 5 validates that the
  annotation Q-number matches the question's dimension. But the annotation only names the
  Q-number — it does not require the Phase 2 vocabulary term to appear in the question text.
  A question can carry `[Q: Q1]` while being semantically correct about the Q1 dimension
  without invoking the specific vocabulary term drawn from Phase 2 Q1. The same traceability gap
  C-25 closes for frame slots (slot must cite verbatim Phase 2 answer) remains open for verify
  questions at the vocabulary-term level: `[Q: Q1]` confirms the dimension but not the term.

- **ES-2 — Replacement provenance is a re-inference, not a citation**: R11 V-03 and V-05 record
  each Phase 2 replacement as `"{old-term}" → "{new-term}" from [bucket name]. Basis: [one-line
  confirmation]`. The one-line basis is a re-assessment of whether the new term belongs to the
  expected bucket — it does not cite back to the specific Phase 1 row where the term was
  extracted. A term surfaced from memory or context can receive a bucket-confirmation statement
  that is indistinguishable from a term actually extracted in Phase 1. Tracing replacement terms
  back to Phase 1 output (by row identifier or position) closes this gap structurally.

**Variation axes**:
- V-01 (single): Vocab-term citation in verify annotation — extends `[Q: Q1]` to `[Q: Q1 — {vocab-term}]`; CHECK 5 validates term-level binding, not just Q-number binding
- V-02 (single): Phase-1 provenance citation in iteration log — replacement terms cite their Phase 1 row, not just their bucket name
- V-03 (single): Frame confirm re-paste — dedicated FRAME CONFIRM step before inertia-advocate role writing; frame string must be pasted verbatim from Phase 3 output, not recalled from memory
- V-04 (combined): ES-1 + ES-2 — vocab-term annotation + Phase-1 provenance citation
- V-05 (combined): ES-1 + ES-2 + Frame confirm — full three-axis synthesis

---

## V-01

**Axis**: Vocab-term citation in verify annotation (ES-1 — single axis)
**Hypothesis**: The `[Q: Q1|Q2|Q3]` annotation introduced in R11 V-02 establishes which Phase 2
dimension a verify question draws from, and CHECK 5 validates dimension-level binding. But a
question can satisfy `[Q: Q1]` while never invoking the specific vocabulary term used in Phase 2's
Q1 answer — it needs only to "reference" the Q1 dimension semantically. The same verbatim
discipline Phase 3 applies to frame-slot citations (Q1 slot ← Phase 2 Q1: [verbatim answer]) can
be applied to verify-question annotations: requiring `[Q: Q1 — vocab: {term}]` where `{term}` is
the exact vocabulary term used in Phase 2's Q1 answer forces the question to be grounded in the
specific Phase 2 output, not in a paraphrase of the Q1 domain. CHECK 5 can then validate both the
Q-number and the term — a question with `[Q: Q1 — vocab: {term}]` where the term does not match
Phase 2 Q1's recorded term is a binding error, not a semantic judgment call.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**6 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets written; each bucket non-empty; minimum 3 terms total;
         each term has a row identifier

Read the input. Extract domain terms and assign each to exactly one of three named buckets.
Output each term with a row identifier (`CS-N`, `MC-N`, `UH-N`) and source phrase:

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
- If any bucket is empty, extend by inference; label inferred terms `[inferred]` with basis:
  "inferred from {X} because {reason}"
- Row identifiers are permanent: do not renumber after extraction

**Exit condition met**: three non-empty buckets; each term has a row identifier; minimum 3 terms
total.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG

**Entry**: Phase 1 complete
**Exit**: convergence declared; most-recent ATTEMPT shows all YES; all prior ATTEMPT blocks
         preserved in output

Answer three questions. Each answer draws from its designated bucket. Use a Phase 1 row identifier
to mark the vocabulary term:

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
Record replacement:
`Replacement: Q{N} term "{old-term}" [{old-row-id}] → "{new-term}" [{new-row-id}] from Phase 1
{bucket-name}. Basis: {new-row-id} confirmed in Phase 1 {bucket-name} bucket.`
Rewrite the affected Q-answer with the replacement term and its row identifier.

---

**AUDIT ATTEMPT 2:** (if ATTEMPT 1 BLOCKED)

Re-evaluate all three Q-answers starting from Q1. Write a new table — same format as ATTEMPT 1.
**ATTEMPT 1 block is not deleted.** Both blocks appear in output. Continue until convergence.

`AUDIT CONVERGENCE: ATTEMPT {N} ALL YES. {N} attempt(s) required.`

**Exit condition met**: convergence declared; all prior ATTEMPT blocks preserved; each replacement
cites Phase 1 row identifier for the new term.

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

Q1 slot ← Phase 2 Q1: [verbatim Phase 2 Q1 answer — from convergence Q1]
Q2 slot ← Phase 2 Q2: [verbatim Phase 2 Q2 answer — from convergence Q2]
Q3 slot ← Phase 2 Q3: [verbatim Phase 2 Q3 answer — from convergence Q3]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

**Slot-binding verification**: Q1 slot drawn from Q1 answer; Q2 slot drawn from Q2 answer; Q3 slot
drawn from Q3 answer. A slot populated from the wrong Q answer is a blocking error. Verify before
declaring Phase 3 complete.

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
**Exit**: all role files written; inertia-advocate verify questions carry vocab-term annotations;
         every `expertise.relevance` references a Phase 1 term

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
{value from Phase 4 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use the Phase 3 completed frame string verbatim
- `orientation.verify`: exactly 3 questions; each carries a vocab-term annotation:
  - Format: `{question ending in ?} [Q: Q1 — vocab: {CS-N} — {term-from-Phase-2-Q1}]`
  - Format: `{question ending in ?} [Q: Q2 — vocab: {MC-N} — {term-from-Phase-2-Q2}]`
  - Format: `{question ending in ?} [Q: Q3 — vocab: {UH-N} — {term-from-Phase-2-Q3}]`
  - The `{term}` in each annotation must match the vocabulary term recorded in Phase 2's convergence
    Q-answer for that Q-number. A term that differs from Phase 2's recorded term is a binding error;
    rewrite before proceeding. A verify question without a vocab-term annotation fails Phase 5.
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: reference Phase 2 Q1 row identifier + at least one other Phase 1 term
- `scope`: cross-team (from Phase 4 table)
- `collaborates_with`: pm

Roles span at least 3 distinct perspective categories. Minimum 3 roles total including
inertia-advocate.

**Exit condition met**: all files written; each inertia-advocate verify question has a
`[Q: QN — vocab: {row-id} — {term}]` annotation matching its Phase 2 Q-answer term; every
`expertise.relevance` contains a Phase 1 term.

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

**CHECK 5 — Verify-Question Vocab-Term Citation Coverage**

For the inertia-advocate's `orientation.verify` fields: does each question carry a
`[Q: QN — vocab: {row-id} — {term}]` annotation? Does the row-id match Phase 2's convergence
Q-answer for that Q-number? Does the term match the vocabulary term recorded in that Phase 2
Q-answer?

Flag each failure mode:
- `{question text} [MISSING ANNOTATION]` — no annotation present
- `{question text} [Q-NUMBER MISMATCH: annotation says Q2, content references Q1 dimension]`
- `{question text} [TERM MISMATCH: annotation says {term-A}, Phase 2 Q{N} recorded {term-B}]`

Revise; confirm annotation-dimension-term binding for all 3 questions.
Gate condition: all 3 verify questions have valid `[Q: QN — vocab: {row-id} — {term}]` annotations
with term matching Phase 2 convergence record.
`CHECK 5: PASS` or `CHECK 5: FAIL — [revisions made]`

---

All 5 checks declared PASS → `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phase 2 with iteration log; verify annotations rebuilt from new convergence answers)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 4)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 6)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-02

**Axis**: Phase-1 provenance citation in iteration log (ES-2 — single axis)
**Hypothesis**: R11 V-03 and V-05 require each Phase 2 replacement to record `"{old-term}" →
"{new-term}" from [bucket name]. Basis: [one-line confirmation]`. The one-line confirmation
re-asserts that the new term belongs to the correct bucket but does not cite where in Phase 1 that
term was extracted. A term generated from context or inferred at replacement time can receive an
identical confirmation statement. The structural fix is to require Phase 1 to assign row identifiers
to each extracted term, and require replacement records to cite the new term's Phase 1 row. If the
replacement term does not appear in Phase 1, it cannot be cited — its absence from the citation
record is itself a structural signal. A Phase 2 replacement citing `[Phase 1 MC-2]` can be
cross-checked against Phase 1 output; a replacement with no Phase 1 citation cannot be verified
and must be re-examined before convergence is declared.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**6 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets written; each bucket non-empty; each term has a row identifier;
         minimum 3 terms total

Read the input. Extract domain terms and assign each to exactly one of three named buckets.
Output each term with a permanent row identifier (`CS-N`, `MC-N`, `UH-N`) and its source phrase:

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
- If any bucket is empty, extend by inference; label inferred terms `[inferred]` with basis
- Row identifiers are permanent: do not renumber after extraction; replacement terms in Phase 2
  must cite their Phase 1 row identifier — if a term has no Phase 1 row, it cannot be used as a
  replacement without being added to Phase 1 first

**Exit condition met**: three non-empty buckets; each term has a row identifier; minimum 3 terms
total.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG WITH PROVENANCE

**Entry**: Phase 1 complete
**Exit**: convergence declared; most-recent ATTEMPT shows all YES; all prior ATTEMPT blocks
         preserved; each replacement cites its Phase 1 row identifier

Answer three questions. Each answer draws from its designated bucket, citing the Phase 1 row:

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

Record the replacement decision with Phase 1 provenance:
```
Replacement:
  Q{N} term "{old-term}" [{old-row-id}]
  → "{new-term}" [{new-row-id}]
  Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"
```

If the new term has no Phase 1 row identifier — it was not extracted in Phase 1 — it cannot be
used as a replacement. Add it to Phase 1 under the correct bucket (with a new row identifier and
source phrase), then proceed with the replacement citation.

Rewrite the affected Q-answer using the replacement term and its row identifier.

---

**AUDIT ATTEMPT 2:** (if ATTEMPT 1 BLOCKED)

Re-evaluate all three Q-answers starting from Q1. Write a new table.
**ATTEMPT 1 block is not deleted.** Both blocks and all replacement records appear in output.

`AUDIT CONVERGENCE: ATTEMPT {N} ALL YES. {N} attempt(s) required.`
`Replacement provenance: all replacement terms cite Phase 1 rows.` (or "No replacements made.")

**Exit condition met**: convergence declared; all ATTEMPT blocks preserved; each replacement
carries a Phase 1 row citation for the new term; no replacement term is undocumented.

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

Q1 slot ← Phase 2 Q1: [verbatim Phase 2 Q1 answer — from convergence Q1]
Q2 slot ← Phase 2 Q2: [verbatim Phase 2 Q2 answer — from convergence Q2]
Q3 slot ← Phase 2 Q3: [verbatim Phase 2 Q3 answer — from convergence Q3]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

**Slot-binding verification**: each slot drawn from its matching Q answer. A slot populated from
the wrong Q answer is a blocking error. Verify before declaring Phase 3 complete.

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
**Exit**: all role files written; inertia-advocate frame uses Phase 3 verbatim;
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
{value from Phase 4 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use the Phase 3 completed frame string verbatim
- `orientation.verify`: 3 questions; each carries `[Q: Q1|Q2|Q3]` annotation referencing the
  Q-dimension it draws from; at least 2 questions must reference the Phase 2 convergence vocabulary
  terms by name
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: reference Phase 2 Q1 row identifier + at least one other Phase 1 term
- `scope`: cross-team (from Phase 4 table)
- `collaborates_with`: pm

Roles span at least 3 distinct perspective categories. Minimum 3 roles total.

**Exit condition met**: all files written; inertia-advocate frame matches Phase 3 output verbatim;
every `expertise.relevance` contains a Phase 1 row-identified term.

---

### Phase 6 — VERIFICATION GATE

**Entry**: Phase 5 complete
**Exit**: all 5 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. Complete all 5 checks in order.**

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

List distinct scope values. Gate condition: at least 2 distinct values.
If all identical: enforce now. State changes.
`CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each role's `expertise.relevance`: does it reference a Phase 1 term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise; state which term was added.
Gate condition: all roles pass.
`CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

**CHECK 5 — Replacement Provenance Audit**

For each replacement recorded in Phase 2's iteration log: does the replacement record contain a
Phase 1 row citation (`{new-row-id} = "{term}" in Phase 1 {bucket}: "{source phrase}"`)?

Flag: `Q{N} replacement "{old-term}" → "{new-term}" [MISSING PHASE-1 CITATION]`
For each flagged replacement: locate the term in Phase 1 output and add the citation, or re-run
Phase 2 with a term that exists in Phase 1.

Gate condition: every replacement cites a Phase 1 row, or no replacements were made.
`CHECK 5: PASS` or `CHECK 5: FAIL — [revisions made]`

---

All 5 checks declared PASS → `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phase 2; iteration log reset; new provenance citations required)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 4)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 6)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-03

**Axis**: Frame confirm re-paste (single axis)
**Hypothesis**: Phase 3 produces the completed frame string with source citations and slot-binding
verification. Phase 5 instructs the inertia-advocate's `orientation.frame` to "use the Phase 3
completed frame string verbatim." The word "verbatim" is a soft instruction: it relies on the model
reproducing the Phase 3 output from memory when writing Phase 5. No structural step confirms that
the Phase 5 frame matches Phase 3 character-for-character before role writing begins. A paraphrase
— "Teams relying on [Q1] face [Q2] costs. Switching disrupts [Q3]." — could pass a semantic
verbatim check while being structurally distinct from the Phase 3 output. A dedicated FRAME
CONFIRM step, positioned between Phase 3 and Phase 5, requires the model to paste the Phase 3
completed frame string as an explicit re-statement before any role file is opened. The paste
creates a two-step chain — Phase 3 produces → FRAME CONFIRM re-declares → Phase 5 consumes —
that makes deviation from Phase 3 output structurally detectable rather than semantically inferred.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

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
- If any bucket is empty, extend by inference; label inferred terms `[inferred]` with basis:
  "inferred from {X} because {reason}"
- Proper nouns and named systems → Current-System; cost and effort vocabulary → Migration-Cost;
  workflow and behavioral vocabulary → User-Habit

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

**Restart protocol**: If any row shows NO, replace the failing term with a term from the correct
bucket. Restart the audit table from Q1 — do not re-score only the replaced row. Evaluate all
three rows simultaneously. Repeat until all three show YES in a single full-pass evaluation.

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

**Slot-binding verification**: Q1 slot drawn from Q1 answer; Q2 slot drawn from Q2 answer; Q3 slot
drawn from Q3 answer. A slot populated from the wrong Q answer is a blocking error. Verify before
declaring Phase 3 complete.

**Exit condition met**: completed frame string written; source citations present; no slot-binding
mismatch.

---

### Phase 4 — FRAME CONFIRM

**Entry**: Phase 3 complete
**Exit**: frame string re-declared verbatim; confirm statement present in output

Before proceeding to scope audit or role writing, re-declare the Phase 3 completed frame string:

```
## Frame Confirm

FRAME CONFIRM: The inertia-advocate orientation.frame I will write in Phase 6 is:
"{paste Phase 3 completed frame string exactly as written above}"
```

Rules:
- The pasted string must be character-for-character identical to the Phase 3 completed frame
  string, including punctuation and capitalization
- Do not paraphrase, summarize, or rephrase — paste verbatim
- If you cannot produce a character-identical paste, return to Phase 3, regenerate the frame
  string, and re-attempt Phase 4
- This statement is the binding contract for Phase 6: the inertia-advocate role file must contain
  this exact string in its `orientation.frame` field

**Exit condition met**: FRAME CONFIRM statement present; pasted string matches Phase 3 output.

---

### Phase 5 — PRE-WRITE SCOPE AUDIT

**Entry**: Phase 4 complete (frame confirm statement present)
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

### Phase 6 — WRITE ROLE FILES

**Entry**: Phase 5 complete (scope audit passed)
**Exit**: all role files written; inertia-advocate frame matches Phase 4 FRAME CONFIRM string;
         every `expertise.relevance` references a Phase 1 term

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
relevance: {sentence referencing at least one Phase 1 vocabulary term}

## scope
{value from Phase 5 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use the FRAME CONFIRM string from Phase 4 — the exact string declared in
  the Phase 4 FRAME CONFIRM statement. Do not recall from memory; use the Phase 4 output
- `orientation.verify`: 3 questions; each carries `[Q: Q1|Q2|Q3]` annotation; at least 2
  questions reference the Q1/Q2/Q3 vocabulary terms from Phase 2
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: reference Q1 vocab term + at least one other Phase 1 term
- `scope`: cross-team (from Phase 5 table)
- `collaborates_with`: pm

Roles span at least 3 distinct perspective categories. Minimum 3 roles total.

**Exit condition met**: all files written; inertia-advocate frame matches Phase 4 FRAME CONFIRM
string; every `expertise.relevance` contains a Phase 1 term.

---

### Phase 7 — VERIFICATION GATE

**Entry**: Phase 6 complete
**Exit**: all 5 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. Complete all 5 checks in order.**

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
Gate condition: zero unresolved references.
`CHECK 2: PASS` or `CHECK 2: FAIL — [action taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values. Gate condition: at least 2 distinct values.
If all identical: enforce now. State changes.
`CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each role's `expertise.relevance`: does it reference a Phase 1 term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise; state which term was added.
Gate condition: all roles pass.
`CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

**CHECK 5 — Frame Confirm Match**

Compare the inertia-advocate `orientation.frame` value against the Phase 4 FRAME CONFIRM string.

`Phase 4 FRAME CONFIRM: "{paste Phase 4 string}"`
`Inertia-advocate frame: "{paste Phase 6 frame value}"`

Gate condition: strings are identical.
If different: flag `[FRAME MISMATCH]`. Rewrite inertia-advocate frame to match Phase 4 FRAME
CONFIRM exactly. Confirm match before PASS.
`CHECK 5: PASS — strings match` or `CHECK 5: FAIL — [FRAME MISMATCH; rewritten]`

---

All 5 checks declared PASS → `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2–4; new FRAME CONFIRM required before Phase 6)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-04

**Axis**: ES-1 + ES-2 — vocab-term annotation + Phase-1 provenance citation (two-axis)
**Hypothesis**: V-01 closes the annotation-granularity gap (verify questions cite vocabulary term,
not just Q-number) and V-02 closes the provenance gap (replacement terms cite Phase 1 rows, not
just bucket names). Both close traceability gaps at different points in the same citation chain:
Phase 2 Q-answers cite Phase 1 rows → Phase 3 frame slots cite Phase 2 answers → Phase 5 verify
questions cite Phase 2 answers AND vocabulary terms. V-04 applies both simultaneously, making the
complete citation chain — Phase 1 extraction → Phase 2 Q-answer → Phase 3 frame slot → Phase 5
verify question — structurally traceable at each link. Combining them surfaces any interaction: a
verify question with `[Q: Q1 — vocab: {CS-1} — {term}]` requires that {term} matches Phase 2 Q1's
recorded term, which itself must have been drawn from Phase 1 CS-1 (or a replacement that cites a
Phase 1 row). The citation chain from Phase 1 through to verify questions is closed end-to-end.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**6 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets written; each bucket non-empty; each term has a row identifier;
         minimum 3 terms total

Read the input. Extract domain terms and assign each to exactly one of three named buckets. Output
each term with a permanent row identifier (`CS-N`, `MC-N`, `UH-N`) and its source phrase:

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
- If any bucket is empty, extend by inference; label `[inferred]` with basis
- Row identifiers are permanent; replacement terms in Phase 2 must cite their Phase 1 row
  identifier or be added to Phase 1 first

**Exit condition met**: three non-empty buckets; each term has a row identifier; minimum 3 terms.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG WITH PROVENANCE

**Entry**: Phase 1 complete
**Exit**: convergence declared; all ATTEMPT blocks preserved; each replacement cites Phase 1 row

Answer three questions citing Phase 1 row identifiers:

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
  → "{new-term}" [{new-row-id}]
  Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"
```

If the new term has no Phase 1 row, add it to Phase 1 under the correct bucket before citing.

---

**AUDIT ATTEMPT 2:** (if ATTEMPT 1 BLOCKED)

Re-evaluate all three rows from Q1. **ATTEMPT 1 block not deleted.**
Continue until: `AUDIT CONVERGENCE: ATTEMPT {N} ALL YES.`

**Exit condition met**: convergence declared; all ATTEMPT blocks preserved; each replacement cites
Phase 1 row identifier with source phrase.

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

Slot-binding: each slot drawn from its matching Q answer. Cross-slot binding is a blocking error.

**Exit condition met**: frame string complete; source citations present; no slot-binding mismatch.

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

**SCOPE AUDIT**: List distinct scope values. Gate: at least 2 distinct values.
If only 1: revise 1–2 roles. State changes.
`SCOPE AUDIT PASS — scope values: [list]`

Writing blocked until scope audit passes.

---

### Phase 5 — WRITE ROLE FILES

**Entry**: Phase 4 complete (scope audit passed)
**Exit**: all role files written; inertia-advocate verify questions carry vocab-term annotations;
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
{value from Phase 4 planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use the Phase 3 completed frame string verbatim
- `orientation.verify`: exactly 3 questions; each carries a vocab-term annotation:
  - Format: `{question ending in ?} [Q: Q1 — vocab: {CS-N} — {term-from-Phase-2-Q1}]`
  - Format: `{question ending in ?} [Q: Q2 — vocab: {MC-N} — {term-from-Phase-2-Q2}]`
  - Format: `{question ending in ?} [Q: Q3 — vocab: {UH-N} — {term-from-Phase-2-Q3}]`
  - The `{term}` must match the vocabulary term in Phase 2's convergence Q-answer for that
    Q-number. A term that differs is a binding error. A question without a vocab-term annotation
    fails Phase 5.
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: reference Phase 2 Q1 row identifier + at least one other Phase 1 term
- `scope`: cross-team
- `collaborates_with`: pm

Minimum 3 roles total; at least 3 distinct perspective categories.

**Exit condition met**: all files written; each verify question has a valid vocab-term annotation;
every `expertise.relevance` contains a Phase 1 row-identified term.

---

### Phase 6 — VERIFICATION GATE

**Entry**: Phase 5 complete
**Exit**: all 6 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. Complete all 6 checks in order.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |

One row per role. All cells filled. Role names match file stems.
`CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

For every `collaborates_with`: matching file exists? Flag unresolved. Add or remove. State action.
Gate: zero unresolved references.
`CHECK 2: PASS` or `CHECK 2: FAIL — [action taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values. Gate: at least 2 distinct. If all identical: enforce; state changes.
`CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

Each `expertise.relevance` references a Phase 1 term? Flag `[NO VOCAB TERM]`. Revise; state term.
Gate: all roles pass.
`CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

**CHECK 5 — Verify-Question Vocab-Term Citation Coverage**

For each inertia-advocate verify question: is a `[Q: QN — vocab: {row-id} — {term}]` annotation
present? Does the row-id match Phase 2's convergence Q-answer? Does the term match Phase 2's
recorded vocabulary term?

Flag:
- `[MISSING ANNOTATION]`
- `[Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M} dimension]`
- `[TERM MISMATCH: annotation says "{term-A}", Phase 2 Q{N} recorded "{term-B}"]`

Gate: all 3 verify questions have valid `[Q: QN — vocab: {row-id} — {term}]` annotations.
`CHECK 5: PASS` or `CHECK 5: FAIL — [revisions made]`

---

**CHECK 6 — Replacement Provenance Audit**

For each Phase 2 replacement record: does it contain a Phase 1 row citation (`{new-row-id} =
"{term}" in Phase 1 {bucket}: "{source phrase}"`)? Flag `[MISSING PHASE-1 CITATION]`. Locate in
Phase 1 or re-run Phase 2.

Gate: every replacement cites a Phase 1 row, or no replacements were made.
`CHECK 6: PASS` or `CHECK 6: FAIL — [revisions made]`

---

All 6 checks declared PASS → `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phase 2 with iteration log; verify annotations rebuilt from new convergence answers and their Phase 1 row citations)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 4)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 6)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-05

**Axis**: ES-1 + ES-2 + Frame confirm — all three axes combined
**Hypothesis**: V-04 closes both citation-chain gaps identified by R11: verify questions cite
Phase 2 vocabulary terms by row identifier (not just Q-number), and replacement terms cite Phase 1
rows (not just bucket names). V-03 closes the verbatim-frame gap: a dedicated FRAME CONFIRM step
forces the Phase 3 frame string to be re-declared before Phase 6 role writing, making deviation
structurally detectable. Combining all three creates a skill where every artifact that draws from
a prior phase must cite its source explicitly — Phase 2 Q-answers cite Phase 1 rows; Phase 3 frame
slots cite Phase 2 answers verbatim; Phase 4 FRAME CONFIRM re-declares Phase 3 output verbatim;
Phase 6 verify questions cite Phase 2 vocabulary terms by row; Phase 7 CHECK 5 validates the frame
match, CHECK 6 validates verify term bindings, CHECK 7 validates replacement provenance. The three
axes reinforce the same structural principle — citations, not re-inference — across three distinct
output surfaces.

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
  → "{new-term}" [{new-row-id}]
  Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"
```

If the new term has no Phase 1 row identifier, add it to Phase 1 under the correct bucket first,
then cite the newly-assigned row identifier.

Restart the audit table from Q1 — evaluate all three rows simultaneously. **Prior ATTEMPT blocks
are not deleted.**

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

Q1 slot ← Phase 2 Q1: [verbatim Phase 2 Q1 answer — from convergence Q1]
Q2 slot ← Phase 2 Q2: [verbatim Phase 2 Q2 answer — from convergence Q2]
Q3 slot ← Phase 2 Q3: [verbatim Phase 2 Q3 answer — from convergence Q3]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

**Slot-binding verification**:
- Q1 slot ← Q1 answer (not Q2, not Q3): YES/NO
- Q2 slot ← Q2 answer (not Q1, not Q3): YES/NO
- Q3 slot ← Q3 answer (not Q1, not Q2): YES/NO

All three must be YES. A cross-slot binding is a blocking error. Do not advance to Phase 4 until
all three bindings are verified.

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
- This string is binding: Phase 6 inertia-advocate `orientation.frame` must match it exactly; Phase
  7 CHECK 5 validates the match

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
If only 1: revise 1–2 roles. State changes. Confirm count ≥ 2.
`SCOPE AUDIT PASS — scope values: [list]`

Writing blocked until scope audit passes.

---

### Phase 6 — WRITE ROLE FILES

**Entry**: Phase 5 complete (scope audit passed)
**Exit**: all role files written; inertia-advocate frame matches Phase 4 FRAME CONFIRM string;
         verify questions carry vocab-term annotations; every `expertise.relevance` references a
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

- `orientation.frame`: use the FRAME CONFIRM string from Phase 4 — the exact string declared in
  the Phase 4 FRAME CONFIRM statement; do not recall from memory or from Phase 3; use Phase 4's
  re-declared string
- `orientation.verify`: exactly 3 questions; each carries a vocab-term annotation:
  - Format: `{question ending in ?} [Q: Q1 — vocab: {CS-N} — {term-from-Phase-2-Q1}]`
  - Format: `{question ending in ?} [Q: Q2 — vocab: {MC-N} — {term-from-Phase-2-Q2}]`
  - Format: `{question ending in ?} [Q: Q3 — vocab: {UH-N} — {term-from-Phase-2-Q3}]`
  - The `{term}` in each annotation must match the vocabulary term recorded in Phase 2's
    convergence Q-answer for that Q-number. A term that differs is a binding error. A question
    without a vocab-term annotation fails Phase 6.
- `orientation.simplify`: 2+ imperatives for scope that fails inertia scrutiny
- `expertise.relevance`: reference Phase 2 Q1 row identifier + at least one other Phase 1 term
- `scope`: cross-team
- `collaborates_with`: pm

Minimum 3 roles total; at least 3 distinct perspective categories.

**Exit condition met**: all files written; inertia-advocate frame matches Phase 4 FRAME CONFIRM
string; each verify question has a valid `[Q: QN — vocab: {row-id} — {term}]` annotation; every
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

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values. Gate: at least 2 distinct values.
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
If different: flag `[FRAME MISMATCH]`. Rewrite inertia-advocate frame to match Phase 4 FRAME
CONFIRM exactly. Confirm match before PASS.
`CHECK 5: PASS — strings match` or `CHECK 5: FAIL — [FRAME MISMATCH; rewritten]`

---

**CHECK 6 — Verify-Question Vocab-Term Citation Coverage**

For each of the inertia-advocate's 3 verify questions: is a `[Q: QN — vocab: {row-id} — {term}]`
annotation present? Does the row-id match Phase 2's convergence Q-answer for that Q-number? Does
the term match Phase 2's recorded vocabulary term for that Q-answer?

Flag each failure mode:
- `{question text} [MISSING ANNOTATION]`
- `{question text} [Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M} dimension]`
- `{question text} [TERM MISMATCH: annotation says "{term-A}", Phase 2 Q{N} recorded "{term-B}"]`
- `{question text} [ROW-ID MISMATCH: annotation says {row-A}, Phase 2 Q{N} used {row-B}]`

Revise; confirm annotation-dimension-term-row binding for all 3 questions.
Gate: all 3 verify questions have valid annotations with Q-number, row-id, and term matching Phase
2 convergence record.
`CHECK 6: PASS` or `CHECK 6: FAIL — [revisions made]`

---

**CHECK 7 — Replacement Provenance Audit**

For each replacement recorded in Phase 2's iteration log: does the record contain a Phase 1 row
citation (`{new-row-id} = "{term}" in Phase 1 {bucket}: "{source phrase}"`)? Can that row
identifier be found in Phase 1 output?

Flag: `Q{N} replacement "{old-term}" → "{new-term}" [MISSING PHASE-1 CITATION]`
For each flagged: locate in Phase 1 or re-run Phase 2 with a term that exists in Phase 1.

Gate: every replacement cites a verifiable Phase 1 row, or no replacements were made.
`CHECK 7: PASS` or `CHECK 7: FAIL — [revisions made]`

---

All 7 checks declared PASS → `GATE RESULT: PASS` — **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run; CHECK 6 re-validates new roles' vocab annotations if inertia role is unchanged)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2–4; full iteration log reset; new FRAME CONFIRM and verify annotations required before Phase 7)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`
