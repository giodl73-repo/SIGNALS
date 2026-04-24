---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 4
rubric: crew-roles-rubric-v4-2026-03-17.md
---

# crew-roles — Variate R4

5 complete prompt body variations for the `crew-roles` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

Round 4 targets four new aspirational criteria introduced in rubric v4:
- **C-17** Pre-Write-Scope-Audit: pre-write SCOPE AUDIT gates writing until plan shows ≥ 2 distinct scope values
- **C-18** Vocabulary-Check-In-Gate: verification gate must include explicit vocabulary coverage CHECK; gate cannot PASS without it
- **C-19** Inertia-Frame-Q-Slot-Template: `orientation.frame` is a fill-in template with named `[Q1]`/`[Q2]` slots — not a soft instruction to reference
- **C-20** Q-Domain-Aligned-Vocabulary-Distribution: Q1 answer references a current-system vocab term, Q2 a migration-cost term, Q3 a user-habit term; same-term reuse across all three fails

R3 V-05 baseline against v4:
- C-17: PASS (Phase 3 SCOPE AUDIT exit-gated before any file is written)
- C-18: PASS (Phase 5 CHECK 4 vocabulary coverage in gate)
- C-19: PASS (Phase 4 inertia-advocate frame is a fill-in template with Q1/Q2 placeholders)
- C-20: PARTIAL — Phase 2 exit condition requires `[vocab: {term}]` per answer but does not enforce Q-domain alignment; same-term reuse allowed; no bucket structure prevents cross-domain selection

The single gap entering R4 is **C-20**: Q-domain alignment in the Phase 2 answers.

---

## V-01

**Axis**: Q-domain-aligned vocabulary distribution via three-bucket Phase 1 (C-20 — single axis)
**Hypothesis**: Splitting Phase 1 vocabulary into three named domain buckets —
`Current-System Terms`, `Migration-Cost Terms`, `User-Habit Terms` — and requiring
each Q1/Q2/Q3 answer to draw from the matching bucket enforces Q-domain alignment at
term selection time. When the model must pick from a labeled bucket for each Q, it
cannot satisfy all three answers with the same term (a term can only occupy one bucket)
and cannot make a cross-domain selection without explicitly violating the bucket constraint.
Prevention at Phase 1 extraction is stronger than post-write audit at Phase 2 completion.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**5 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: vocabulary list written with at least 3 terms distributed across 3 named buckets; at least 1 term per bucket

Read the input. Assign each extracted term to exactly one bucket:

```
## Domain Vocabulary

Current-System Terms: [named tools, products, services, or approaches currently in use in this domain]
Migration-Cost Terms: [named costs, integration burdens, retraining categories, or disruption types replacing this system would create]
User-Habit Terms: [named workflows, behaviors, routines, or daily-use patterns that depend on the current system]
```

Minimum 1 term per bucket; minimum 3 terms total. Extend by inference if input yields fewer — label
inferred terms `[inferred]` and state basis. A term belongs to exactly one bucket; assign it to the
bucket representing its primary dimension.

**Exit condition met**: vocabulary list written; at least 1 term per bucket; at least 3 terms total.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION

**Entry**: Phase 1 complete
**Exit**: all 3 answers written; Q1 vocab term drawn from Current-System Terms; Q2 drawn from
         Migration-Cost Terms; Q3 drawn from User-Habit Terms; no cross-bucket term reuse

Answer these three questions. **Each answer must reference a vocabulary term from the matching bucket.
Wrong-bucket selection fails this phase — rewrite the answer with a correct-bucket term before proceeding.**

**Q1 — Current system**
What is the named current system or approach from `Current-System Terms`?
Required format: `Current system: [answer] [vocab: {term-from-Current-System-Terms}]`

**Q2 — Migration cost**
What concrete cost or risk does replacing the current system create? Use a term from `Migration-Cost Terms`.
Required format: `Migration cost: [answer] [vocab: {term-from-Migration-Cost-Terms}]`

**Q3 — User habit**
What observable workflow or daily behavior depends on the current system? Use a term from `User-Habit Terms`.
Required format: `User habit: [answer] [vocab: {term-from-User-Habit-Terms}]`

```
## Inertia Pre-Characterization

Current system: [answer] [vocab: {term-from-Current-System-Terms}]
Migration cost: [answer] [vocab: {term-from-Migration-Cost-Terms}]
User habit: [answer] [vocab: {term-from-User-Habit-Terms}]
```

**Exit condition met**: 3 answers written; each `[vocab]` term comes from the specified bucket; no term
appears in more than one answer; no cross-bucket reuse.

---

### Phase 3 — SCOPE PLANNING GATE

**Entry**: Phase 2 complete
**Exit**: scope planning table written with at least 2 distinct scope values confirmed before any file is written

Assign scope to each planned role. Scope values:
- `team` — decisions and risks contained within one team
- `cross-team` — requires coordination across 2+ teams
- `org` — requires org-level alignment or executive visibility

| Role | Perspective | Scope | Justification |
|------|-------------|-------|---------------|
| pm | product | {scope} | {one reason based on input context} |
| architect | technical | {scope} | {one reason based on input context} |
| inertia-advocate | inertia | cross-team | status quo spans the full domain |
| {domain-specialist} | domain | {scope} | derived from Phase 1 vocabulary |

Add domain specialist rows for each major system or pattern from Phase 1 that PM and Architect cannot adequately represent.

**SCOPE AUDIT**:
1. List all distinct scope values from the Scope column.
2. Gate condition: at least 2 distinct values.
3. If only 1 value: identify 1–2 roles where actual organizational reach differs. Revise table. State: "Revised {role} scope {old} → {new}: {reason}."
4. Confirm distinct count ≥ 2.

**Exit condition met**: `SCOPE AUDIT PASS — scope values: [list]`
Do not write any role file until scope audit passes.

---

### Phase 4 — WRITE ROLE FILES

**Entry**: Phase 3 complete (scope audit passed)
**Exit**: all role files written; inertia-advocate frame names Q1 current system and Q2 migration cost;
         every `expertise.relevance` references a Phase 1 vocabulary term from any bucket

List selected roles and one-line rationale before writing.

**For each non-inertia role**, write `.roles/{area}/{role-name}.md`:

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
serves: {who benefits from this perspective}

## lens
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative: Remove / Defer / Collapse / Merge / Move}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence containing at least one Phase 1 vocabulary term from any bucket}

## scope
{value from Phase 3 table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate**, write `.roles/{area}/inertia-advocate.md`:

- `orientation.frame`: "Challenge every proposal with evidence that [Q1 current system] remains sufficient
  given [Q2 migration cost]." Insert Phase 2 Q1 and Q2 answers verbatim into the brackets.
- `lens.verify`: 3 questions with Q-domain vocabulary distribution:
  - Question 1: names Q1 current system; references Q1's vocab term (Current-System Terms)
  - Question 2: references Q2 migration cost; references Q2's vocab term (Migration-Cost Terms)
  - Question 3: references Q3 user habit; references Q3's vocab term (User-Habit Terms)
- `lens.simplify`: at least 2 imperatives
- `expertise.relevance`: reference Q1 vocab term + at least one term from a different bucket
- `scope`: cross-team (from Phase 3 table)
- `collaborates_with`: pm

**Exit condition met**: all files written; inertia-advocate frame contains Q1 and Q2 verbatim;
every `expertise.relevance` references a Phase 1 term.

---

### Phase 5 — VERIFICATION GATE

**Entry**: Phase 4 complete
**Exit**: all 4 checks declare PASS; gate confirmed before delivery

**DELIVERY IS BLOCKED. Complete all 4 checks in order. Each must declare PASS before the next
opens. Fix defects found in earlier checks before proceeding to later ones.**

---

**CHECK 1 — Registry Summary Table**

Write from the role files produced:

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role file. Every cell filled. Role column matches file stems exactly.
Declare: `CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

For every name in Collaborates With: does it appear in the Role column?
Flag: `{name} [UNRESOLVED]`.
For each: add the missing role OR remove the reference. State action taken.
Gate condition: zero `[UNRESOLVED]` entries.
Declare: `CHECK 2: PASS` or `CHECK 2: FAIL — [actions taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values from the Scope column.
Gate condition: at least 2 distinct values (Phase 3 scope audit should have ensured this).
If Phase 3 was bypassed and all scopes are identical: revise 1–2 roles now. State changes.
Declare: `CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each role's `expertise.relevance`: does it reference a Phase 1 vocabulary term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise. State which term was added and from which bucket.
Gate condition: zero `[NO VOCAB TERM]` entries.
Declare: `CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

All 4 checks declared PASS → **VERIFICATION GATE CLEAR. Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Refresh vocabulary buckets: `/crew-roles {domain} --amend vocab` *(re-runs Phase 1; Phase 2 and Phase 4 update)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phase 2; inertia-advocate rewrites)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 3)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 5)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-02

**Axis**: Post-answer domain-alignment audit table (C-20 — single axis, different enforcement angle)
**Hypothesis**: An explicit domain-alignment audit table at the END of Phase 2 — that lists
Q1/Q2/Q3 vocab terms alongside their required domain and yields a Match? per row — creates a
structural audit point that catches cross-domain reuse even after terms are selected. The bucket
approach (V-01) prevents wrong selection by constraining the menu at Phase 1; this approach allows
any selection format but audits alignment after answers are written. The audit table makes
Q-domain mismatch visible as a detectable FAIL condition with a named correction path, rather than
a subtle omission that passes inspection. Complementary to V-01: V-01 prevents; V-02 catches.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**5 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: vocabulary list written with at least 3 terms

Read the input. Extract and label:

```
## Domain Vocabulary

Systems: [named products, services, modules, APIs — proper nouns from the input]
Patterns: [named workflows, protocols, architectural decisions from the input]
Key terms: [domain-specific nouns not present in generic engineering documentation]
```

Minimum 3 terms. Extend by inference if needed; label inferred terms `[inferred]` and state basis.

**Exit condition met**: vocabulary list written with 3+ terms.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION

**Entry**: Phase 1 complete
**Exit**: all 3 answers written with `[vocab: {term}]` annotations; domain-alignment table
         shows YES for all 3 rows; no cross-domain reuse

Answer these three questions. Each answer must reference at least one Phase 1 vocabulary term.
Use the required format below.

**Q1 — Current system**
What existing system, tool, or approach does the domain currently rely on?
The vocab term must be a current-system entity (a named tool, product, or approach —
not a cost category or behavior name).
Required format: `Current system: [answer] [vocab: {term}]`

**Q2 — Migration cost**
What concrete cost or risk does replacing the current system create?
The vocab term must name a cost category, risk type, or integration burden —
not the current system itself or a user behavior.
Required format: `Migration cost: [answer] [vocab: {term}]`

**Q3 — User habit**
What observable workflow or daily behavior depends on the current system?
The vocab term must name a workflow, behavior, routine, or usage pattern —
not the current system itself or a cost.
Required format: `User habit: [answer] [vocab: {term}]`

```
## Inertia Pre-Characterization

Current system: [answer] [vocab: {term}]
Migration cost: [answer] [vocab: {term}]
User habit: [answer] [vocab: {term}]
```

**Domain-alignment check** — run immediately after writing the 3 answers:

| Answer | Vocab Term | Required Domain | Match? |
|--------|------------|-----------------|--------|
| Q1 Current system | {term} | current-system entity (tool/product/approach) | {YES/NO} |
| Q2 Migration cost | {term} | cost or risk category | {YES/NO} |
| Q3 User habit | {term} | workflow or behavior | {YES/NO} |

Gate condition: all three Match? cells are YES.
If any Match? is NO: rewrite that answer with a term from the correct domain. Update the table. Re-confirm.

**Exit condition met**: domain-alignment table shows YES for all three; no term reused across answers.

---

### Phase 3 — SCOPE PLANNING GATE

**Entry**: Phase 2 complete
**Exit**: scope planning table written with at least 2 distinct scope values confirmed

Scope values: `team` | `cross-team` | `org`

| Role | Perspective | Scope | Justification |
|------|-------------|-------|---------------|
| pm | product | {scope} | {one reason} |
| architect | technical | {scope} | {one reason} |
| inertia-advocate | inertia | cross-team | status quo spans the full domain |
| {domain-specialist} | domain | {scope} | derived from Phase 1 vocabulary |

**SCOPE AUDIT**:
1. List all distinct scope values.
2. Gate: ≥ 2 distinct values.
3. If only 1: revise 1–2 roles. State: "Revised {role} scope {old} → {new}: {reason}." Confirm count.

**Exit condition met**: `SCOPE AUDIT PASS — scope values: [list]`
Do not write any role file until scope audit passes.

---

### Phase 4 — WRITE ROLE FILES

**Entry**: Phase 3 complete
**Exit**: all role files written; inertia-advocate frame names Q1 current system and Q2 migration cost
         verbatim; every `expertise.relevance` references a Phase 1 vocabulary term

List selected roles and one-line rationale before writing.

**For each non-inertia role**, write `.roles/{area}/{role-name}.md`:

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
serves: {who benefits from this perspective}

## lens
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative: Remove / Defer / Collapse / Merge / Move}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence containing at least one Phase 1 vocabulary term}

## scope
{value from Phase 3 table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate**, write `.roles/{area}/inertia-advocate.md`:

- `orientation.frame`: "Challenge every proposal with evidence that [Q1 current system] remains sufficient
  given [Q2 migration cost]." Insert Q1 and Q2 answers from Phase 2 verbatim into the brackets.
  The Q1 vocab term from the domain-alignment table must appear in the frame text.
- `lens.verify`: 3 questions mapped to Phase 2 dimensions using Q-matching terms from the domain-alignment table:
  - Question 1: names Q1 current system; uses Q1's domain-alignment vocab term
  - Question 2: references Q2 migration cost/risk; uses Q2's domain-alignment vocab term
  - Question 3: references Q3 user habit; uses Q3's domain-alignment vocab term
- `lens.simplify`: at least 2 imperatives
- `expertise.relevance`: reference Q1 vocab term + at least one other Phase 1 term
- `scope`: cross-team
- `collaborates_with`: pm

**Exit condition met**: all files written; inertia-advocate frame contains Q1/Q2 verbatim;
every `expertise.relevance` references a Phase 1 term.

---

### Phase 5 — VERIFICATION GATE

**Entry**: Phase 4 complete
**Exit**: all 4 checks declare PASS

**DELIVERY IS BLOCKED. Complete all 4 checks in order. Each must declare PASS before the next opens.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. Every cell filled. Role column matches file stems exactly.
Declare: `CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

Flag `{name} [UNRESOLVED]` for any Collaborates With name not in Role column. Fix each. State action.
Gate: zero `[UNRESOLVED]` entries.
Declare: `CHECK 2: PASS` or `CHECK 2: FAIL — [actions taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values. Gate: ≥ 2. If Phase 3 bypassed and all same: revise 1–2 roles. State changes.
Declare: `CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each `expertise.relevance`: flag `{role-name} [NO VOCAB TERM]` if no Phase 1 term present. Fix. State term added.
Gate: zero `[NO VOCAB TERM]` entries.
Declare: `CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

All 4 checks declared PASS → **VERIFICATION GATE CLEAR. Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Re-run domain alignment: `/crew-roles {domain} --amend vocab` *(re-runs Phase 1 + Phase 2 alignment check)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phase 2)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 3)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 5)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-03

**Axis**: Pre-write inertia frame fill as a dedicated phase (C-19 upgrade — single axis)
**Hypothesis**: Making the inertia-advocate frame fill-in an explicit standalone phase — which
produces a completed, filled sentence before any role file is written — is structurally stronger
than embedding Q-slot instructions inside the role-write phase. When the filled sentence is
produced as a named artifact in its own phase, it exists as a completed output that Phase 5 copies
verbatim. The constraint is not "follow the slot instruction when writing" (which can be bypassed
under model compression) but "this sentence is already resolved; copy it." Pre-resolution removes
the opportunity for slot omission at write time.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**6 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: vocabulary list written with at least 3 terms

Read the input. Extract and label:

```
## Domain Vocabulary

Systems: [named products, services, modules, APIs — proper nouns from the input]
Patterns: [named workflows, protocols, architectural decisions from the input]
Key terms: [domain-specific nouns not present in generic engineering documentation]
```

Minimum 3 terms. Extend by inference if needed; label inferred terms `[inferred]` and state basis.

**Exit condition met**: vocabulary list written with 3+ terms.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION

**Entry**: Phase 1 complete
**Exit**: all 3 answers written; each contains a `[vocab: {term}]` annotation referencing a Phase 1 term

**Q1 — Current system**
What existing system, tool, or approach from the Phase 1 vocabulary does the domain currently rely on?
Required format: `Current system: [answer] [vocab: {term-from-Phase-1}]`

**Q2 — Migration cost**
What concrete cost or risk does moving away from the current system create? Reference a vocabulary term.
Required format: `Migration cost: [answer] [vocab: {term-from-Phase-1}]`

**Q3 — User habit**
What observable workflow or daily behavior depends on the current system? Reference a vocabulary term.
Required format: `User habit: [answer] [vocab: {term-from-Phase-1}]`

```
## Inertia Pre-Characterization

Current system: [answer] [vocab: {term}]
Migration cost: [answer] [vocab: {term}]
User habit: [answer] [vocab: {term}]
```

**Exit condition met**: 3 answers written; each has a `[vocab: {term}]` annotation.
If any annotation is missing: rewrite that answer before proceeding.

---

### Phase 3 — INERTIA FRAME FILL

**Entry**: Phase 2 complete
**Exit**: completed inertia-advocate frame sentence produced; Q1 and Q2 answers appear verbatim;
         sentence matches the fill-in template structure

The inertia-advocate's `orientation.frame` is a fixed fill-in sentence. Fill it now —
before any role file is written — using Phase 2 answers.

Template:
```
Challenge every proposal with evidence that [Q1: current system name] remains sufficient given [Q2: migration cost description].
```

Procedure:
1. Take the Q1 answer (current system name) from Phase 2.
2. Take the Q2 answer (migration cost description) from Phase 2.
3. Replace `[Q1: current system name]` with the Q1 answer verbatim.
4. Replace `[Q2: migration cost description]` with the Q2 answer verbatim.
5. Record the completed sentence:

```
## Inertia Frame (filled)

orientation.frame: "Challenge every proposal with evidence that {Q1-answer} remains sufficient given {Q2-answer}."
```

This sentence is now fixed. In Phase 5, copy it verbatim into `inertia-advocate.md`'s
`orientation.frame` field. Do not rewrite it.

**Exit condition met**: frame sentence written; Q1 and Q2 answers from Phase 2 appear verbatim;
no generic placeholder text (`[Q1: ...]`, `[Q2: ...]`) remains.

---

### Phase 4 — SCOPE PLANNING GATE

**Entry**: Phase 3 complete
**Exit**: scope planning table written with at least 2 distinct scope values confirmed

Scope values: `team` | `cross-team` | `org`

| Role | Perspective | Scope | Justification |
|------|-------------|-------|---------------|
| pm | product | {scope} | {one reason} |
| architect | technical | {scope} | {one reason} |
| inertia-advocate | inertia | cross-team | status quo spans the full domain |
| {domain-specialist} | domain | {scope} | derived from Phase 1 vocabulary |

**SCOPE AUDIT**:
1. List all distinct scope values.
2. Gate: ≥ 2 distinct values.
3. If only 1: revise 1–2 roles. State: "Revised {role} scope {old} → {new}: {reason}." Confirm count.

**Exit condition met**: `SCOPE AUDIT PASS — scope values: [list]`
Do not write any role file until scope audit passes.

---

### Phase 5 — WRITE ROLE FILES

**Entry**: Phase 4 complete; Phase 3 frame sentence available
**Exit**: all role files written; inertia-advocate `orientation.frame` matches Phase 3 sentence verbatim;
         every `expertise.relevance` references a Phase 1 vocabulary term

List selected roles and one-line rationale before writing.

**For each non-inertia role**, write `.roles/{area}/{role-name}.md`:

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
serves: {who benefits from this perspective}

## lens
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative: Remove / Defer / Collapse / Merge / Move}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence containing at least one Phase 1 vocabulary term}

## scope
{value from Phase 4 table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate**, write `.roles/{area}/inertia-advocate.md`:

- `orientation.frame`: **copy the Phase 3 filled sentence verbatim** — do not rewrite; do not paraphrase
- `lens.verify`: 3 questions; each references a Phase 2 Q1/Q2/Q3 vocab term respectively:
  - Question 1: references Q1 current system and its `[vocab]` term
  - Question 2: references Q2 migration cost and its `[vocab]` term
  - Question 3: references Q3 user habit and its `[vocab]` term
- `lens.simplify`: at least 2 imperatives
- `expertise.relevance`: reference Q1 vocab term + at least one other Phase 1 term
- `scope`: cross-team (from Phase 4 table)
- `collaborates_with`: pm

**Exit condition met**: all files written; inertia-advocate frame matches Phase 3 sentence;
every `expertise.relevance` references a Phase 1 term.

---

### Phase 6 — VERIFICATION GATE

**Entry**: Phase 5 complete
**Exit**: all 4 checks declare PASS

**DELIVERY IS BLOCKED. Complete all 4 checks in order. Each must declare PASS before the next opens.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. Every cell filled.
Declare: `CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

Flag `{name} [UNRESOLVED]` for any Collaborates With name not in Role column. Fix. State action.
Gate: zero `[UNRESOLVED]` entries.
Declare: `CHECK 2: PASS` or `CHECK 2: FAIL — [actions taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values. Gate: ≥ 2. If Phase 4 bypassed and all same: revise. State changes.
Declare: `CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each `expertise.relevance`: flag `{role-name} [NO VOCAB TERM]` if no Phase 1 term present. Fix. State term added.
Gate: zero `[NO VOCAB TERM]` entries.
Declare: `CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

All 4 checks declared PASS → **VERIFICATION GATE CLEAR. Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Refresh vocabulary: `/crew-roles {domain} --amend vocab` *(re-runs Phase 1; Phases 2–3 update)*
> - Re-fill frame: `/crew-roles {domain} --amend frame` *(re-runs Phase 3; inertia-advocate rewrites in Phase 5)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 4)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 6)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-04

**Axes**: C-20 three-bucket vocabulary (V-01) + C-19 pre-write frame fill (V-03)
**Hypothesis**: Combining Phase 1 three-bucket vocabulary extraction (which pre-sorts terms by
dimension so Phase 2 cannot reuse the same term across Q1/Q2/Q3) with a dedicated Phase 3
frame-fill step (which resolves the inertia-advocate frame before any file is written) addresses
the two remaining gaps simultaneously. Phase 1 makes Q-domain alignment structurally possible by
providing labeled buckets; Phase 3 makes Q-slot integration structurally necessary by producing
the filled sentence as a pre-write artifact. Together they close C-20 (cross-bucket reuse prevented
at Phase 1 extraction) and C-19 (slot omission prevented by pre-resolution before Phase 5).

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**6 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: vocabulary list written with at least 3 terms distributed across 3 domain buckets; at least 1 term per bucket

Read the input. Assign each extracted term to exactly one bucket:

```
## Domain Vocabulary

Current-System Terms: [named tools, products, services, or approaches currently in use]
Migration-Cost Terms: [named costs, integration burdens, retraining categories, or disruption types]
User-Habit Terms: [named workflows, behaviors, routines, or usage patterns]
```

Minimum 1 term per bucket; minimum 3 terms total. Extend by inference if needed; label inferred terms `[inferred]`.
A term belongs to exactly one bucket — assign it to the bucket representing its primary dimension.

**Exit condition met**: vocabulary list written; at least 1 term per bucket; at least 3 terms total.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION

**Entry**: Phase 1 complete
**Exit**: all 3 answers written; Q1 term from Current-System Terms; Q2 term from Migration-Cost Terms;
         Q3 term from User-Habit Terms; no cross-bucket reuse

**Q1 — Current system**
Draw a term from `Current-System Terms`.
Required format: `Current system: [answer] [vocab: {term-from-Current-System-Terms}]`

**Q2 — Migration cost**
Draw a term from `Migration-Cost Terms`.
Required format: `Migration cost: [answer] [vocab: {term-from-Migration-Cost-Terms}]`

**Q3 — User habit**
Draw a term from `User-Habit Terms`.
Required format: `User habit: [answer] [vocab: {term-from-User-Habit-Terms}]`

```
## Inertia Pre-Characterization

Current system: [answer] [vocab: {term-from-Current-System-Terms}]
Migration cost: [answer] [vocab: {term-from-Migration-Cost-Terms}]
User habit: [answer] [vocab: {term-from-User-Habit-Terms}]
```

**Exit condition met**: 3 answers written; each `[vocab]` term comes from the specified bucket;
no term appears in more than one answer.

---

### Phase 3 — INERTIA FRAME FILL

**Entry**: Phase 2 complete
**Exit**: completed inertia-advocate frame sentence produced; Q1 and Q2 answers appear verbatim

Template:
```
Challenge every proposal with evidence that [Q1: current system name] remains sufficient given [Q2: migration cost description].
```

Procedure:
1. Take Q1 answer (current system name) from Phase 2.
2. Take Q2 answer (migration cost description) from Phase 2.
3. Fill the template:

```
## Inertia Frame (filled)

orientation.frame: "Challenge every proposal with evidence that {Q1-answer} remains sufficient given {Q2-answer}."
```

This sentence is now fixed. Copy it verbatim into `inertia-advocate.md` in Phase 5.

**Exit condition met**: frame sentence written; Q1 and Q2 answers from Phase 2 present verbatim; no unfilled placeholders remain.

---

### Phase 4 — SCOPE PLANNING GATE

**Entry**: Phase 3 complete
**Exit**: scope planning table with at least 2 distinct scope values; SCOPE AUDIT PASS declared

Scope values: `team` | `cross-team` | `org`

| Role | Perspective | Scope | Justification |
|------|-------------|-------|---------------|
| pm | product | {scope} | {one reason} |
| architect | technical | {scope} | {one reason} |
| inertia-advocate | inertia | cross-team | status quo spans the full domain |
| {domain-specialist} | domain | {scope} | derived from Phase 1 vocabulary |

**SCOPE AUDIT**:
1. List all distinct scope values.
2. Gate: ≥ 2 distinct values.
3. If only 1: revise 1–2 roles. State: "Revised {role} scope {old} → {new}: {reason}." Confirm count.

**Exit condition met**: `SCOPE AUDIT PASS — scope values: [list]`
Do not write any role file until scope audit passes.

---

### Phase 5 — WRITE ROLE FILES

**Entry**: Phase 4 complete; Phase 3 frame sentence available
**Exit**: all role files written; inertia-advocate `orientation.frame` matches Phase 3 sentence verbatim;
         every `expertise.relevance` references a Phase 1 vocabulary term from any bucket

List selected roles and one-line rationale before writing.

**For each non-inertia role**, write `.roles/{area}/{role-name}.md`:

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
serves: {who benefits from this perspective}

## lens
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative: Remove / Defer / Collapse / Merge / Move}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence containing at least one Phase 1 vocabulary term from any bucket}

## scope
{value from Phase 4 table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate**, write `.roles/{area}/inertia-advocate.md`:

- `orientation.frame`: **copy the Phase 3 filled sentence verbatim**
- `lens.verify`: 3 questions with Q-domain vocabulary distribution:
  - Question 1: names Q1 current system; references Q1's vocab term (Current-System Terms)
  - Question 2: references Q2 migration cost; references Q2's vocab term (Migration-Cost Terms)
  - Question 3: references Q3 user habit; references Q3's vocab term (User-Habit Terms)
- `lens.simplify`: at least 2 imperatives
- `expertise.relevance`: reference Q1 vocab term + at least one term from a different bucket
- `scope`: cross-team (from Phase 4 table)
- `collaborates_with`: pm

**Exit condition met**: all files written; inertia-advocate frame matches Phase 3; every `expertise.relevance` references a Phase 1 term.

---

### Phase 6 — VERIFICATION GATE

**Entry**: Phase 5 complete
**Exit**: all 4 checks declare PASS

**DELIVERY IS BLOCKED. Complete all 4 checks in order. Each must declare PASS before the next opens.
Fix defects found in earlier checks before proceeding to later ones.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. Every cell filled. Role column matches file stems exactly.
Declare: `CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

Flag `{name} [UNRESOLVED]` for any Collaborates With name not in Role column. Fix. State action.
Gate: zero `[UNRESOLVED]` entries.
Declare: `CHECK 2: PASS` or `CHECK 2: FAIL — [actions taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values. Gate: ≥ 2. If Phase 4 bypassed and all same: revise. State changes.
Declare: `CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each `expertise.relevance`: flag `{role-name} [NO VOCAB TERM]` if no Phase 1 term. Fix. State term added and bucket.
Gate: zero `[NO VOCAB TERM]` entries.
Declare: `CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

All 4 checks declared PASS → **VERIFICATION GATE CLEAR. Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Refresh vocabulary buckets: `/crew-roles {domain} --amend vocab` *(re-runs Phase 1; Phases 2–3 update)*
> - Re-fill frame: `/crew-roles {domain} --amend frame` *(re-runs Phase 3; inertia-advocate frame rewrites in Phase 5)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 4)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 6)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-05

**Axes**: Full synthesis — C-17/C-18/C-19/C-20 + V-05 R3 excellence patterns + R4 improvements
**Hypothesis**: All four new criteria and all R3 excellence patterns are wired into a single
non-redundant enforcement chain where each mechanism fires at the earliest possible execution
point and no mechanism depends on correction after writing:
- **C-20**: Phase 1 three-bucket extraction (term selection constrained by bucket) + Phase 2
  domain-alignment audit table (YES/NO per Q confirms correct-bucket selection)
- **C-19**: Phase 3 dedicated frame-fill (Q1+Q2 resolved into sentence before any file is written;
  Phase 5 copies verbatim — no slot instruction to drift under compression)
- **C-17**: Phase 4 SCOPE AUDIT exit-gated (scope diversity confirmed before any file is written)
- **C-18**: Phase 6 CHECK 4 (vocabulary coverage in the named blocking gate — cannot PASS without it)
- **R3 V-05 excellence**: phase-boundary Entry/Exit conditions prevent inter-phase leakage; layered
  vocab enforcement at Phase 1 (extraction), Phase 2 (annotation + alignment audit), Phase 5 exit
  condition (relevance constraint), and Phase 6 CHECK 4 (gate-level audit)
Each layer catches a distinct failure mode at the point where correction is cheapest.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**6 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: vocabulary list written with at least 3 terms; at least 1 term per domain bucket

Read the input. Assign each extracted term to exactly one domain bucket:

```
## Domain Vocabulary

Current-System Terms: [named tools, products, services, or approaches currently in use in this domain]
Migration-Cost Terms: [named costs, integration burdens, retraining requirements, or disruption categories
                       replacing this system would create]
User-Habit Terms: [named workflows, behaviors, routines, or daily-use patterns that depend on the current system]
```

Minimum 1 term per bucket; minimum 3 terms total. Extend by inference if input yields fewer —
label inferred terms `[inferred]` and state basis: "inferred from [X] because [reason]."

A term belongs to exactly one bucket. A term that spans multiple dimensions goes into the bucket
representing its primary dimension.

**Exit condition met**: vocabulary list written; at least 1 term per bucket; at least 3 terms total.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION

**Entry**: Phase 1 complete
**Exit**: all 3 answers written; Q1 term drawn from Current-System Terms; Q2 term drawn from
         Migration-Cost Terms; Q3 term drawn from User-Habit Terms; domain-alignment table
         shows YES for all 3 rows; no cross-bucket term reuse

Answer these three questions. **Each answer must reference a vocabulary term from the matching
bucket. Wrong-bucket selection fails this phase — rewrite with a correct-bucket term before proceeding.**

**Q1 — Current system**
Describe the primary current system this domain will displace or extend. Draw from `Current-System Terms`.
Required format: `Current system: [answer] [vocab: {term-from-Current-System-Terms}]`

**Q2 — Migration cost**
What concrete cost, risk, or burden does replacing the current system create? Draw from `Migration-Cost Terms`.
Required format: `Migration cost: [answer] [vocab: {term-from-Migration-Cost-Terms}]`

**Q3 — User habit**
What observable workflow, daily behavior, or usage pattern depends on the current system? Draw from `User-Habit Terms`.
Required format: `User habit: [answer] [vocab: {term-from-User-Habit-Terms}]`

```
## Inertia Pre-Characterization

Current system: [answer] [vocab: {term-from-Current-System-Terms}]
Migration cost: [answer] [vocab: {term-from-Migration-Cost-Terms}]
User habit: [answer] [vocab: {term-from-User-Habit-Terms}]
```

**Domain-alignment check** — run immediately after writing the 3 answers:

| Answer | Vocab Term Used | Required Bucket | Match? |
|--------|-----------------|-----------------|--------|
| Q1 Current system | {term} | Current-System Terms | {YES/NO} |
| Q2 Migration cost | {term} | Migration-Cost Terms | {YES/NO} |
| Q3 User habit | {term} | User-Habit Terms | {YES/NO} |

Gate condition: all three Match? cells are YES.
If any Match? is NO: identify the correct bucket, select a term from it, rewrite the answer,
update the table, re-confirm.

**Exit condition met**: domain-alignment table shows YES for all three; no term appears in more
than one answer.

---

### Phase 3 — INERTIA FRAME FILL

**Entry**: Phase 2 complete
**Exit**: completed inertia-advocate frame sentence produced; Q1 and Q2 answers appear verbatim;
         no unfilled placeholder syntax remains

Fill the inertia-advocate's `orientation.frame` now — before any role file is written.

Template:
```
Challenge every proposal with evidence that [Q1: current system name] remains sufficient given [Q2: migration cost description].
```

Procedure:
1. Take the Q1 answer (current system name) from Phase 2.
2. Take the Q2 answer (migration cost description) from Phase 2.
3. Replace `[Q1: current system name]` with the Q1 answer verbatim.
4. Replace `[Q2: migration cost description]` with the Q2 answer verbatim.
5. Record the completed sentence:

```
## Inertia Frame (filled)

orientation.frame: "Challenge every proposal with evidence that {Q1-answer} remains sufficient given {Q2-answer}."
```

This sentence is now fixed. In Phase 5, copy it verbatim into `inertia-advocate.md`'s
`orientation.frame`. Do not rewrite it. Do not paraphrase it.

**Exit condition met**: frame sentence written; Q1 and Q2 answers from Phase 2 appear verbatim;
no bracket placeholder text remains.

---

### Phase 4 — SCOPE PLANNING GATE

**Entry**: Phase 3 complete
**Exit**: scope planning table written with at least 2 distinct scope values confirmed;
         SCOPE AUDIT PASS declared; no role file written before this phase completes

Assign scope to each planned role. Scope values:
- `team` — decisions and risks contained within one team
- `cross-team` — requires coordination or sign-off across 2+ teams
- `org` — requires org-level alignment, policy, or executive visibility

| Role | Perspective | Scope | Justification |
|------|-------------|-------|---------------|
| pm | product | {scope} | {reason based on input context} |
| architect | technical | {scope} | {reason based on input context} |
| inertia-advocate | inertia | cross-team | status quo spans the full domain |
| {domain-specialist} | domain | {scope} | derived from Phase 1 vocabulary |

Add domain specialist rows for each major system or pattern from Phase 1 that PM and Architect
cannot adequately represent.

**SCOPE AUDIT**:
1. List all distinct scope values from the Scope column.
2. Gate condition: at least 2 distinct values.
3. If only 1 value: identify 1–2 roles where actual organizational reach differs. Revise table.
   State: "Revised {role} scope {old} → {new}: {reason}."
4. Re-confirm distinct count ≥ 2.

**Exit condition met**: `SCOPE AUDIT PASS — scope values: [list]`
Do not write any role file until scope audit passes.

---

### Phase 5 — WRITE ROLE FILES

**Entry**: Phase 4 complete; Phase 3 frame sentence available
**Exit**: all role files written; inertia-advocate `orientation.frame` matches Phase 3 sentence
         verbatim; every `expertise.relevance` references a Phase 1 vocabulary term from any bucket;
         inertia-advocate verify questions each reference the Q-domain-matching vocab term

List selected roles and one-line rationale before writing.

**For each non-inertia role**, write `.roles/{area}/{role-name}.md`:

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
serves: {who benefits from this perspective}

## lens
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative: Remove / Defer / Collapse / Merge / Move}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence containing at least one Phase 1 vocabulary term from any bucket}

## scope
{value from Phase 4 table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**Vocabulary constraint**: If a role's `expertise.relevance` cannot be written using a Phase 1 term,
the role is too generic for this domain — rename it to a more specific perspective before writing.

**For the inertia-advocate**, write `.roles/{area}/inertia-advocate.md`:

- `orientation.frame`: **copy the Phase 3 filled sentence verbatim** — no rewrites, no paraphrase
- `lens.verify`: 3 questions with Q-domain-aligned vocabulary distribution:
  - Question 1: names Q1 current system; uses Q1's vocab term (from Current-System Terms)
  - Question 2: references Q2 migration cost or risk category; uses Q2's vocab term (from Migration-Cost Terms)
  - Question 3: references Q3 user habit or dependent workflow; uses Q3's vocab term (from User-Habit Terms)
  A generic question ("Is the current approach sufficient?") fails even if 2 of 3 are specific.
- `lens.simplify`: at least 2 imperative rules for eliminating scope that fails inertia scrutiny
- `expertise.relevance`: reference Q1 vocab term (Current-System Terms) + at least one term from a different bucket
- `scope`: cross-team (from Phase 4 table)
- `collaborates_with`: pm

**Exit condition met**: all files written; inertia-advocate frame matches Phase 3 sentence; every
`expertise.relevance` references a Phase 1 term; inertia-advocate verify questions each reference
the Q-domain-matching vocab term.

---

### Phase 6 — VERIFICATION GATE

**Entry**: Phase 5 complete
**Exit**: all 4 checks declare PASS; gate explicitly confirmed before delivery

**DELIVERY IS BLOCKED. Complete all 4 checks in order. Each must declare PASS before the next
opens. Fix defects found in earlier checks before proceeding to later ones.**

---

**CHECK 1 — Registry Summary Table**

Write from the role files produced:

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role file. Every cell filled. Role column must match file stems exactly.
Declare: `CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

For every name in Collaborates With: does it appear in the Role column?
Flag: `{name} [UNRESOLVED]`.
For each: add the missing role to the registry OR remove the reference from the citing file.
State action taken for each.
Gate condition: zero `[UNRESOLVED]` entries.
Declare: `CHECK 2: PASS` or `CHECK 2: FAIL — [actions taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values from the Scope column.
Gate condition: at least 2 distinct values (Phase 4 scope audit should have ensured this).
If Phase 4 was bypassed and all scopes are identical: enforce now — revise 1–2 roles. State changes.
Declare: `CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each role's `expertise.relevance`: does it reference a Phase 1 vocabulary term from any bucket?
Flag: `{role-name} [NO VOCAB TERM]`. Revise the field. State which term was added and from which bucket.
Gate condition: zero `[NO VOCAB TERM]` entries.
Declare: `CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

All 4 checks declared PASS → **VERIFICATION GATE CLEAR. Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Refresh vocabulary buckets: `/crew-roles {domain} --amend vocab` *(re-runs Phase 1; Phases 2–3 update)*
> - Re-run domain alignment: `/crew-roles {domain} --amend align` *(re-runs Phase 2 alignment check only)*
> - Re-fill frame: `/crew-roles {domain} --amend frame` *(re-runs Phase 3; inertia-advocate frame updates in Phase 5)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 4)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 6)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`
