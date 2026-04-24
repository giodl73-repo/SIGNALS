# crew-roles V-01 through V-05 — Rubric v6

---

## V-01
**Variation axis**: Lifecycle emphasis
**Hypothesis**: Naming every phase with explicit entry/exit conditions and blocking rules maximizes gate compliance (C-15, C-17, C-22, C-23, C-24, C-25) by making phases structurally unskippable.

---

You are generating a typed role registry for a domain. Analyze the provided input to determine what expert perspectives are needed. Each role file contains five required fields: `name`, `orientation`, `expertise`, `collaborates_with`, `scope`. Output directory: `.roles/{area}/`

---

### PHASE 1 — BUCKETED VOCABULARY EXTRACTION

**Entry condition**: Input has been read.
**Exit condition**: All three buckets populated with at least two terms each; every term assigned to exactly one bucket.

Extract domain-specific vocabulary and assign each term to one of three named buckets:

- **Bucket A — Current-System Terms**: Names of existing systems, components, patterns, or tools the domain currently uses.
- **Bucket B — Migration-Cost Terms**: Concepts relating to switching cost, deprecation, effort, risk, or disruption.
- **Bucket C — User-Habit Terms**: Patterns of how current users work — preferences, learned workflows, or habituated behaviors.

Produce Phase 1 output:

```
PHASE 1 VOCABULARY
Bucket A — Current-System Terms: [term1], [term2], ...
Bucket B — Migration-Cost Terms: [term1], [term2], ...
Bucket C — User-Habit Terms: [term1], [term2], ...
```

Do not proceed to Phase 2 until all three buckets are populated.

---

### PHASE 2 — INERTIA PRE-CHARACTERIZATION

**Entry condition**: Phase 1 vocabulary buckets are complete.
**Exit condition**: Domain-alignment audit table shows all three rows YES after a full re-evaluation pass. Phase 2 does not close until this condition is met as a unit.

Answer three characterization questions, drawing each answer from its designated bucket:

- **Q1 (current system)** — What is the specific current system, pattern, or tool being displaced? Draw from **Bucket A**.
- **Q2 (migration cost)** — What are the concrete migration costs or switching frictions? Draw from **Bucket B**.
- **Q3 (user habit)** — What established user habits or workflows create resistance? Draw from **Bucket C**.

After writing all three answers, produce the domain-alignment audit table:

```
| Q  | Term Used | Expected Bucket | Match |
|----|-----------|-----------------|-------|
| Q1 | [term]    | Bucket A        | YES/NO |
| Q2 | [term]    | Bucket B        | YES/NO |
| Q3 | [term]    | Bucket C        | YES/NO |
```

**Replacement rule**: If any row shows NO, replace the term with a correct-bucket term and restart the audit table evaluation from row Q1. Do not re-score only the replaced row. Re-evaluate all three rows simultaneously. The Phase 2 gate condition is: all three rows YES in the same evaluation pass. Phase 2 does not close on partial satisfaction.

---

### PHASE 3 — FRAME FILL

**Entry condition**: Phase 2 audit table is all-YES after a full pass.
**Exit condition**: Completed frame string produced with explicit slot-source citations; slot-binding verification passes on all three slots.

The inertia-advocate `orientation.frame` uses this fill-in template:

```
"[Q1 current system] is deeply embedded in this domain. Migration requires navigating [Q2 migration cost]. Teams have built workflows around [Q3 user habit]. The question is not whether change is possible but whether the cost is justified."
```

Populate each slot from the corresponding Phase 2 answer:

```
FRAME FILL
Q1 slot ← Phase 2 Q1: [verbatim Q1 answer]
Q2 slot ← Phase 2 Q2: [verbatim Q2 answer]
Q3 slot ← Phase 2 Q3: [verbatim Q3 answer]

Completed frame: "[frame text with all three slots filled]"
```

Slot-binding verification — run before proceeding:

```
Q1 slot drawn from Q1 answer: CHECK [PASS/FAIL]
Q2 slot drawn from Q2 answer: CHECK [PASS/FAIL]
Q3 slot drawn from Q3 answer: CHECK [PASS/FAIL]
```

Any FAIL is a blocking error. A slot populated from the wrong Phase 2 answer is not detected by inspecting the frame string alone; explicit citation makes mismatches visible. Do not proceed to Phase 4 until all three checks are PASS.

---

### PHASE 4 — PRE-WRITE SCOPE AUDIT

**Entry condition**: Frame Fill phase is complete.
**Exit condition**: Planned role set contains at least 2 distinct scope values. Writing is blocked until this condition is met.

Plan the full role set — names and scope assignments only:

```
SCOPE AUDIT
| Role (planned)      | Scope (planned) |
|---------------------|-----------------|
| inertia-advocate    | ...             |
| ...                 | ...             |
```

Valid scope values: `team`, `cross-team`, `org`.

If all planned roles share a single scope value, revise 1–2 planned roles before proceeding. Do not begin writing role files until at least 2 distinct scope values appear in the plan.

---

### PHASE 5 — ROLE WRITING

**Entry condition**: Scope audit shows >= 2 distinct planned scope values.
**Exit condition**: All role files written; all 5 required fields present in every file.

Write each role file. Requirements:

- Every file contains: `name`, `orientation` (with `frame`, `verify`, `simplify`), `expertise` (with `relevance`, `skills`), `collaborates_with`, `scope`
- `orientation.verify` fields are questions ending in `?`
- `orientation.simplify` fields are imperatives
- `expertise.relevance` references at least one term from the Phase 1 vocabulary (any bucket)
- `collaborates_with` lists names of other roles in this registry (resolve after all roles are named)
- Minimum 3 roles spanning at least 3 distinct perspective categories (e.g., product, technical, inertia, domain-specialist)
- Scope values match the plan; overall set spans at least 2 distinct values

Write the inertia-advocate first, using the completed frame from Phase 3:

```yaml
name: inertia-advocate
orientation:
  frame: "[completed frame from Phase 3]"
  verify:
    - "What does [Q1 term] provide today that the proposed approach cannot match?"
    - "Who owns the migration effort for [Q2 term], and at what realistic cost?"
    - "What breaks for users who rely on [Q3 term] during transition?"
  simplify:
    - "Name the one concrete advantage of the current system that must not be lost."
    - "Reduce the migration plan to its single largest risk."
expertise:
  relevance: "[domain-specific statement anchored to a Phase 1 vocabulary term]"
  skills: [...]
collaborates_with: [...]
scope: [team|cross-team|org]
```

Write remaining roles. Each `expertise.relevance` must anchor to a Phase 1 vocabulary term by name.

---

### PHASE 6 — VERIFICATION GATE

**Entry condition**: All role files are written.
**Exit condition**: All four checks pass as a unit. Delivery is blocked until this phase emits PASS.

Run all checks before delivery:

**CHECK 1 — Registry Summary Table**

Produce:

```
| Role | Frame (one-line summary) | Scope | Collaborates With |
|------|--------------------------|-------|-------------------|
| ...  | ...                      | ...   | ...               |
```

**CHECK 2 — Orphan Reference Check**

Every name listed in any `collaborates_with` resolves to a role in the registry. List any unresolved references. If any exist, resolve before PASS.

**CHECK 3 — Scope Gradient Check**

Confirm at least 2 distinct scope values are present across all roles. If not, revise 1–2 roles and re-run CHECK 1.

**CHECK 4 — Vocabulary Coverage Check**

Confirm every `expertise.relevance` field references a term that appears in Phase 1 vocabulary. List any roles missing a vocabulary reference. If any exist, revise before PASS.

All four checks must pass simultaneously. Write:

```
VERIFICATION GATE: PASS
```

only when all four checks pass.

---

Write one file per role to `.roles/{area}/`.

---
---

## V-02
**Variation axis**: Phrasing register
**Hypothesis**: Conversational first-person imperative phrasing ("Do X, then do Y, confirm Z") reduces the cognitive overhead of parsing formal declarations and increases the likelihood that the model follows the sequential constraint correctly.

---

You're building a typed role registry for a domain. Read the input, then follow these steps exactly in order. Every step produces output you'll reference in a later step — don't skip ahead.

Output directory: `.roles/{area}/` — one file per role, each with five fields: `name`, `orientation`, `expertise`, `collaborates_with`, `scope`.

---

**Step 1 — Pull the vocabulary, sorted into three buckets.**

Read the input and extract the domain-specific terms you find. Sort every term into one of three buckets:

- **Bucket A — Current-System Terms** (existing systems, tools, components the domain uses right now)
- **Bucket B — Migration-Cost Terms** (anything about switching cost, effort, risk, disruption, deprecation)
- **Bucket C — User-Habit Terms** (how users currently work — their learned patterns, workflows, preferences)

Write out your buckets before you do anything else:

```
VOCABULARY BUCKETS
Bucket A — Current-System Terms: [list]
Bucket B — Migration-Cost Terms: [list]
Bucket C — User-Habit Terms: [list]
```

You need at least two terms per bucket. If a bucket is thin, look harder. Don't proceed until you have all three.

---

**Step 2 — Answer three questions about inertia, one bucket each.**

Pull answers to these three questions, drawing each from the bucket that matches:

- **Q1**: What's the specific current system or tool being replaced? Pull from Bucket A.
- **Q2**: What are the concrete switching costs or friction points? Pull from Bucket B.
- **Q3**: What user habits or workflows will resist the change? Pull from Bucket C.

Write your answers, then immediately run the audit table:

```
| Q  | Term You Used | Correct Bucket | Match? |
|----|---------------|----------------|--------|
| Q1 | [term]        | Bucket A       | YES/NO |
| Q2 | [term]        | Bucket B       | YES/NO |
| Q3 | [term]        | Bucket C       | YES/NO |
```

If any row says NO, swap in a term from the right bucket — then restart the table from Q1. Don't just fix the bad row; re-run all three rows from scratch. The table only closes when all three say YES in the same evaluation pass. That's the gate out of Step 2.

---

**Step 3 — Fill the inertia frame template.**

You're going to build the core framing sentence for the inertia-advocate role. Here's the template:

```
"[Q1 current system] is deeply embedded in this domain. Migration requires [Q2 migration cost]. Teams have built workflows around [Q3 user habit]. The question is not whether change is possible but whether the cost is justified."
```

Fill each slot from your Step 2 answers, then write out the citations explicitly:

```
FRAME FILL
Q1 slot ← Step 2 Q1 answer: [exact text]
Q2 slot ← Step 2 Q2 answer: [exact text]
Q3 slot ← Step 2 Q3 answer: [exact text]

Completed frame: "[your filled frame text]"
```

Before moving on, verify the slot bindings:

```
Q1 slot drawn from Q1 answer: PASS/FAIL
Q2 slot drawn from Q2 answer: PASS/FAIL
Q3 slot drawn from Q3 answer: PASS/FAIL
```

A wrong-slot binding — say, your Q2 answer slotted into the Q1 position — won't be obvious from reading the frame alone. That's why you're checking explicitly. Fix any FAIL before continuing.

---

**Step 4 — Plan the role set before writing anything.**

List every role you plan to write, with its scope, before you write a single file:

```
SCOPE PLAN
| Planned Role     | Planned Scope |
|------------------|---------------|
| inertia-advocate | ...           |
| ...              | ...           |
```

Valid scopes: `team`, `cross-team`, `org`.

If everything on your list has the same scope, change 1–2 of them. You need at least two distinct scope values in the plan. Don't start writing roles until the plan passes this check.

---

**Step 5 — Write the roles.**

Now write the role files. You need at least 3, covering at least 3 distinct perspective categories (for example: product, technical, inertia, domain-specialist — not all technical).

Rules for every role:

- All five fields required: `name`, `orientation` (with `frame`, `verify`, `simplify`), `expertise` (with `relevance`, `skills`), `collaborates_with`, `scope`
- `orientation.verify` items end in `?`
- `orientation.simplify` items are imperatives
- `expertise.relevance` names at least one term from your Step 1 vocabulary buckets
- `collaborates_with` lists other role names from this registry

Write the inertia-advocate first, using the completed frame from Step 3:

```yaml
name: inertia-advocate
orientation:
  frame: "[completed frame from Step 3]"
  verify:
    - "What concrete advantage does [Q1 term] provide that no replacement currently matches?"
    - "What is the realistic total cost of [Q2 term] — who absorbs it and when?"
    - "How do users who depend on [Q3 term] continue their work during transition?"
  simplify:
    - "State the single advantage the current system has that must survive the migration."
    - "Cut the migration plan to its one largest unresolved risk."
expertise:
  relevance: "[anchored to a Step 1 vocabulary term]"
  skills: [...]
collaborates_with: [...]
scope: [value from your scope plan]
```

Then write your remaining roles. Each `expertise.relevance` must reference a vocabulary term by name.

---

**Step 6 — Run the verification gate.**

Don't skip this. Run all four checks before you declare done.

**Check 1 — Summary table.** Write it out:

```
| Role | Frame (one-line summary) | Scope | Collaborates With |
|------|--------------------------|-------|-------------------|
```

**Check 2 — Orphan references.** Go through every `collaborates_with` list. Does each name exist in the registry? List any that don't. Fix them.

**Check 3 — Scope gradient.** Count distinct scope values. If there's only one, go back and revise 1–2 roles, then re-run Check 1.

**Check 4 — Vocabulary coverage.** Go through every `expertise.relevance`. Does each one reference a term that actually appeared in your Step 1 buckets? List any that don't. Fix them.

Once all four pass:

```
VERIFICATION GATE: PASS
```

Then write the files to `.roles/{area}/`.

---
---

## V-03
**Variation axis**: Output format (table-heavy)
**Hypothesis**: Representing every intermediate artifact as a structured table rather than prose minimizes ambiguity about what constitutes a complete phase output, making structural gaps in phase completion immediately visible.

---

Generate a typed role registry. Input: the provided product or codebase context. Output: `.roles/{area}/` — one markdown file per role.

Required fields per role file: `name` · `orientation` (frame, verify, simplify) · `expertise` (relevance, skills) · `collaborates_with` · `scope`

Execute the following phases in sequence. Each phase produces a structured table artifact. A phase is not complete until its table artifact is present and its exit condition is satisfied.

---

**PHASE 1 — VOCABULARY EXTRACTION**

Exit condition: table populated; all three buckets have ≥ 2 terms.

```
| Bucket                       | Terms Extracted         |
|------------------------------|-------------------------|
| A — Current-System Terms     | [term], [term], ...     |
| B — Migration-Cost Terms     | [term], [term], ...     |
| C — User-Habit Terms         | [term], [term], ...     |
```

---

**PHASE 2 — INERTIA PRE-CHARACTERIZATION**

Entry: Phase 1 table complete.
Exit: Audit table shows YES in all three rows after a full evaluation pass.

Answer table (draw each answer from the designated bucket):

```
| Q  | Question                                     | Answer (verbatim) | Source Bucket |
|----|----------------------------------------------|-------------------|---------------|
| Q1 | Name the specific current system/tool         | [answer]          | Bucket A      |
| Q2 | Name the concrete migration cost/friction      | [answer]          | Bucket B      |
| Q3 | Name the user habit creating resistance        | [answer]          | Bucket C      |
```

Domain-alignment audit table:

```
| Q  | Term Used | Expected Bucket | Match |
|----|-----------|-----------------|-------|
| Q1 | [term]    | Bucket A        | YES/NO|
| Q2 | [term]    | Bucket B        | YES/NO|
| Q3 | [term]    | Bucket C        | YES/NO|
```

Replacement protocol: Any NO row → replace term from correct bucket → restart audit from row Q1 → evaluate all three rows as a unit in the new pass. Re-scoring only the replaced row does not satisfy the exit condition. Phase 2 closes only when all three rows are YES in a single evaluation pass.

---

**PHASE 3 — FRAME FILL**

Entry: Phase 2 audit table all-YES.
Exit: Frame Fill table complete; slot-binding check all-PASS.

Template: `"[Q1 current system] is deeply embedded in this domain. Migration requires [Q2 migration cost]. Teams have built workflows around [Q3 user habit]. The question is not whether change is possible but whether the cost is justified."`

Frame Fill table:

```
| Slot | Source Question | Phase 2 Answer (verbatim)              | Filled Slot Value |
|------|-----------------|----------------------------------------|-------------------|
| Q1   | Phase 2 Q1      | [verbatim answer from Phase 2 Q1 row]  | [slot fill]       |
| Q2   | Phase 2 Q2      | [verbatim answer from Phase 2 Q2 row]  | [slot fill]       |
| Q3   | Phase 2 Q3      | [verbatim answer from Phase 2 Q3 row]  | [slot fill]       |
```

Completed frame string:

```
"[frame text with all three slots populated]"
```

Slot-binding check table:

```
| Slot | Drawn From Correct Source? | Status     |
|------|---------------------------|------------|
| Q1   | Phase 2 Q1 row            | PASS/FAIL  |
| Q2   | Phase 2 Q2 row            | PASS/FAIL  |
| Q3   | Phase 2 Q3 row            | PASS/FAIL  |
```

Any FAIL is a blocking error. Phase 3 does not close until all three rows are PASS.

---

**PHASE 4 — SCOPE AUDIT**

Entry: Phase 3 complete.
Exit: Planned role set shows ≥ 2 distinct scope values.

```
| Planned Role     | Perspective Category | Planned Scope |
|------------------|----------------------|---------------|
| inertia-advocate | inertia              | [value]       |
| [role 2]         | [category]           | [value]       |
| [role 3]         | [category]           | [value]       |
| ...              | ...                  | ...           |
```

Scope diversity check:

```
| Scope Value | Count | Meets ≥ 2 Distinct? |
|-------------|-------|---------------------|
| [value]     | [n]   | YES/NO              |
| [value]     | [n]   |                     |
```

If only one distinct scope value is present, revise 1–2 planned roles before proceeding. Role writing is blocked until this check passes.

---

**PHASE 5 — ROLE WRITING**

Entry: Phase 4 scope audit passes.

Write one file per role. Inertia-advocate uses the completed frame from Phase 3. Each `expertise.relevance` references at least one Phase 1 vocabulary term by name. `collaborates_with` values are resolved after all roles are named.

Minimum 3 roles. Perspective categories span ≥ 3 distinct types.

---

**PHASE 6 — VERIFICATION GATE**

Entry: All roles written.
Exit: All four check tables PASS as a unit. Delivery blocked until GATE: PASS is emitted.

**Check 1 — Registry Summary Table**

```
| Role | Frame (one-line) | Scope | Collaborates With |
|------|------------------|-------|-------------------|
| ...  | ...              | ...   | ...               |
```

**Check 2 — Orphan Reference Audit**

```
| Role | Collaborates_With Entry | Resolves? |
|------|-------------------------|-----------|
| ...  | [name]                  | YES/NO    |
```

Any NO → resolve before PASS.

**Check 3 — Scope Gradient Audit**

```
| Scope Value | Count |
|-------------|-------|
| [value]     | [n]   |
```

Distinct scope count: [n]. Passes if ≥ 2.

**Check 4 — Vocabulary Coverage Audit**

```
| Role | expertise.relevance excerpt | Phase 1 term cited | Present in buckets? |
|------|-----------------------------|--------------------|---------------------|
| ...  | [excerpt]                   | [term]             | YES/NO              |
```

Any NO → revise before PASS.

All four checks must pass simultaneously:

```
VERIFICATION GATE: PASS
```

---
---

## V-04
**Combined axes**: Role sequence (inertia-advocate authored first) + Inertia framing (status-quo competitor is the structural anchor; remaining roles are calibrated against it)
**Hypothesis**: Treating the inertia-advocate as the foundational role — the one all other roles are written in reaction to — produces stronger perspective diversity and more actionable verify questions across the registry, because each other role is explicitly positioned relative to a concrete status-quo challenge.

---

You are generating a typed role registry for a domain. The inertia-advocate is the anchor role — write it first. All other roles are written in relation to it: each role's verify questions should be answerable in the context of the inertia challenge the inertia-advocate raises.

Output: `.roles/{area}/` — one file per role.
Required fields: `name`, `orientation` (frame, verify, simplify), `expertise` (relevance, skills), `collaborates_with`, `scope`.

---

### STEP 1 — EXTRACT VOCABULARY BY BUCKET

Read the input and build three named vocabulary buckets before anything else:

```
VOCABULARY BUCKETS
Bucket A — Current-System Terms: [term1], [term2], ...
Bucket B — Migration-Cost Terms: [term1], [term2], ...
Bucket C — User-Habit Terms: [term1], [term2], ...
```

Assign every extracted term to exactly one bucket. Populate all three buckets (minimum 2 terms each) before proceeding.

---

### STEP 2 — CHARACTERIZE THE INERTIA CHALLENGE

Answer three questions. Each answer draws from the designated bucket:

- **Q1 (current system)**: The specific system, tool, or pattern being displaced. Draw from **Bucket A**.
- **Q2 (migration cost)**: The concrete switching cost or friction. Draw from **Bucket B**.
- **Q3 (user habit)**: The established user workflow or habit at risk. Draw from **Bucket C**.

After writing answers, verify bucket alignment:

```
| Q  | Term Used | Expected Bucket | Match |
|----|-----------|-----------------|-------|
| Q1 | [term]    | Bucket A        | YES/NO|
| Q2 | [term]    | Bucket B        | YES/NO|
| Q3 | [term]    | Bucket C        | YES/NO|
```

If any row is NO: replace the term with one from the correct bucket, then restart the audit table from row Q1. Evaluate all three rows simultaneously in the new pass. Step 2 does not close until all three rows show YES in the same pass.

---

### STEP 3 — FILL THE INERTIA FRAME

Populate the template using your Step 2 answers. Cite each slot's source explicitly:

```
FRAME FILL
Q1 slot ← Step 2 Q1: [verbatim answer]
Q2 slot ← Step 2 Q2: [verbatim answer]
Q3 slot ← Step 2 Q3: [verbatim answer]

Completed frame: "[Q1 term] is deeply embedded in this domain. Migration requires [Q2 term]. Teams have built workflows around [Q3 term]. The question is not whether change is possible but whether the cost is justified."
```

Verify slot bindings before proceeding:

```
Q1 slot filled from Q1 answer: PASS/FAIL
Q2 slot filled from Q2 answer: PASS/FAIL
Q3 slot filled from Q3 answer: PASS/FAIL
```

Any FAIL is a blocking error. Fix before Step 4.

---

### STEP 4 — WRITE THE INERTIA-ADVOCATE (anchor role)

Write this role first. It defines the status-quo challenge that structures the rest of the registry.

```yaml
name: inertia-advocate
orientation:
  frame: "[completed frame from Step 3]"
  verify:
    - "What does [Q1 term] guarantee today that no alternative currently provides?"
    - "Who absorbs [Q2 term] and over what timeline — is the estimate realistic?"
    - "What happens to users whose core workflow depends on [Q3 term]?"
  simplify:
    - "State the single capability the current system has that the replacement must match before adoption."
    - "Reduce the migration risk to one concrete scenario that could derail it."
expertise:
  relevance: "[domain-specific statement referencing a Bucket A vocabulary term]"
  skills: [domain-relevant skills]
collaborates_with: [to be resolved after all roles are named]
scope: [team|cross-team|org]
```

---

### STEP 5 — PLAN REMAINING ROLES RELATIVE TO THE INERTIA CHALLENGE

Before writing other roles, plan the registry with scope assignments. Frame each planned role in terms of how it engages with the inertia-advocate's challenge:

```
SCOPE + POSITIONING PLAN
| Planned Role | Perspective Category | Planned Scope | Position vs. Inertia Challenge |
|--------------|----------------------|---------------|-------------------------------|
| [role]       | [category]           | [scope]       | [e.g., "validates Q2 cost estimate", "owns Q1 migration"] |
```

Scope diversity gate: At least 2 distinct scope values must appear in the plan. If all roles share one scope, revise before proceeding.

Perspective diversity gate: At least 3 distinct perspective categories across the full registry (including inertia-advocate).

---

### STEP 6 — WRITE REMAINING ROLES

Write each planned role. Requirements:

- All 5 fields present in every file
- `orientation.verify` fields are questions ending in `?`; at least one verify question per role engages with Q1, Q2, or Q3 from the inertia characterization
- `orientation.simplify` fields are imperatives
- `expertise.relevance` references at least one term from the Step 1 vocabulary buckets by name
- `collaborates_with` resolves to role names in this registry

After writing all roles, resolve `collaborates_with` cross-references in the inertia-advocate and all other roles.

---

### STEP 7 — VERIFICATION GATE

Run all checks before delivery. All must pass as a unit.

**Check 1 — Registry Summary Table**

```
| Role | Frame / Position (one-line) | Scope | Collaborates With |
|------|-----------------------------|-------|-------------------|
| inertia-advocate | [summary] | [scope] | [names] |
| ...  | ...                         | ...   | ...               |
```

**Check 2 — Orphan Reference Check**

Every `collaborates_with` entry resolves to a role name in the registry. List any that do not. Fix before PASS.

**Check 3 — Scope Gradient Check**

Distinct scope values across all roles: [list]. Count ≥ 2: YES/NO. If NO, revise 1–2 roles and re-run Check 1.

**Check 4 — Vocabulary Coverage Check**

Every `expertise.relevance` references a Phase 1 vocabulary term by name. List any roles that do not. Fix before PASS.

All four checks pass:

```
VERIFICATION GATE: PASS
```

Write files to `.roles/{area}/`.

---
---

## V-05
**Combined axes**: Lifecycle emphasis (every gate is a structured checklist) + Output format (all intermediate artifacts are explicit tables or checklists, zero prose in phase bodies)
**Hypothesis**: Replacing all prose instructions with structured checklists eliminates the interpretation gap between "phase described" and "phase executed" — the model follows a checklist mechanically in ways it may not follow a paragraph, yielding the highest compliance on C-22, C-23, C-24, and C-25.

---

Generate a typed role registry. Input: product or codebase context provided below. Output: `.roles/{area}/` — one file per role.

Required fields per role: `name` · `orientation.frame` · `orientation.verify` · `orientation.simplify` · `expertise.relevance` · `expertise.skills` · `collaborates_with` · `scope`

Execute phases in order. Each phase has a checklist. Check off each item as you produce it. A phase does not close until every item is checked.

---

### PHASE 1 — VOCABULARY EXTRACTION

Checklist:

- [ ] Read input completely
- [ ] Extract Bucket A (Current-System Terms) — ≥ 2 terms
- [ ] Extract Bucket B (Migration-Cost Terms) — ≥ 2 terms
- [ ] Extract Bucket C (User-Habit Terms) — ≥ 2 terms
- [ ] Every extracted term assigned to exactly one bucket
- [ ] Produce Phase 1 output table:

```
| Bucket                       | Terms                   |
|------------------------------|-------------------------|
| A — Current-System Terms     |                         |
| B — Migration-Cost Terms     |                         |
| C — User-Habit Terms         |                         |
```

PHASE 1 STATUS: [ ] COMPLETE

---

### PHASE 2 — INERTIA PRE-CHARACTERIZATION

Entry gate: Phase 1 STATUS = COMPLETE

Checklist:

- [ ] Answer Q1 (current system) — draw term from **Bucket A**
- [ ] Answer Q2 (migration cost) — draw term from **Bucket B**
- [ ] Answer Q3 (user habit) — draw term from **Bucket C**
- [ ] Produce Q&A table:

```
| Q  | Answer (verbatim)                | Term Used | Source Bucket |
|----|----------------------------------|-----------|---------------|
| Q1 |                                  |           | Bucket A      |
| Q2 |                                  |           | Bucket B      |
| Q3 |                                  |           | Bucket C      |
```

- [ ] Produce domain-alignment audit table:

```
| Q  | Term Used | Expected Bucket | Match |
|----|-----------|-----------------|-------|
| Q1 |           | Bucket A        |       |
| Q2 |           | Bucket B        |       |
| Q3 |           | Bucket C        |       |
```

- [ ] Audit table evaluation — all rows YES in this pass?
  - If YES on all rows → proceed to exit check
  - If any row NO → replace term from correct bucket → **restart audit table from Q1** (not from the replaced row) → re-run all three rows as a unit → repeat until all-YES in one pass

- [ ] PHASE 2 EXIT CHECK: All three rows YES in same evaluation pass → [ ] PASS

PHASE 2 STATUS: [ ] COMPLETE

---

### PHASE 3 — FRAME FILL

Entry gate: Phase 2 STATUS = COMPLETE

Checklist:

- [ ] Identify Phase 2 Q1 verbatim answer
- [ ] Identify Phase 2 Q2 verbatim answer
- [ ] Identify Phase 2 Q3 verbatim answer
- [ ] Produce Frame Fill table:

```
| Slot | Source          | Phase 2 Verbatim Answer | Filled Value |
|------|-----------------|-------------------------|--------------|
| Q1   | Phase 2 Q1 row  |                         |              |
| Q2   | Phase 2 Q2 row  |                         |              |
| Q3   | Phase 2 Q3 row  |                         |              |
```

- [ ] Produce completed frame string:

```
Completed frame: "[Q1 filled value] is deeply embedded in this domain. Migration requires [Q2 filled value]. Teams have built workflows around [Q3 filled value]. The question is not whether change is possible but whether the cost is justified."
```

- [ ] Slot-binding verification:

```
| Slot | Drawn from correct Phase 2 row? | Status |
|------|----------------------------------|--------|
| Q1   | Phase 2 Q1                       | PASS/FAIL |
| Q2   | Phase 2 Q2                       | PASS/FAIL |
| Q3   | Phase 2 Q3                       | PASS/FAIL |
```

- [ ] All three binding checks PASS → [ ] PASS
  - Any FAIL = blocking error — correct the mislabeled slot before proceeding

PHASE 3 STATUS: [ ] COMPLETE

---

### PHASE 4 — PRE-WRITE SCOPE AUDIT

Entry gate: Phase 3 STATUS = COMPLETE

Checklist:

- [ ] List every planned role with scope assignment:

```
| Planned Role     | Perspective Category | Planned Scope |
|------------------|----------------------|---------------|
| inertia-advocate | inertia              |               |
|                  |                      |               |
```

- [ ] Count distinct scope values in plan: ___
- [ ] Distinct scope count ≥ 2? [ ] YES / [ ] NO
  - If NO → revise 1–2 planned roles → re-run scope count → repeat until YES
- [ ] Count distinct perspective categories: ___
- [ ] Perspective category count ≥ 3? [ ] YES / [ ] NO
  - If NO → add or revise a planned role

PHASE 4 STATUS: [ ] COMPLETE

---

### PHASE 5 — ROLE WRITING

Entry gate: Phase 4 STATUS = COMPLETE

Checklist per role (repeat for each):

**inertia-advocate** (write first):

- [ ] `name`: inertia-advocate
- [ ] `orientation.frame`: completed frame from Phase 3 (verbatim)
- [ ] `orientation.verify`: ≥ 2 questions ending in `?`; at least one references Q1 term, one references Q2 or Q3 term
- [ ] `orientation.simplify`: ≥ 1 imperative
- [ ] `expertise.relevance`: references a Phase 1 vocabulary term by name
- [ ] `expertise.skills`: populated
- [ ] `collaborates_with`: placeholder (resolve after all roles named)
- [ ] `scope`: value from Phase 4 plan

**Each additional role**:

- [ ] `name`: defined
- [ ] `orientation.frame`: specific to this role's perspective
- [ ] `orientation.verify`: ≥ 2 questions ending in `?`
- [ ] `orientation.simplify`: ≥ 1 imperative
- [ ] `expertise.relevance`: references a Phase 1 vocabulary term by name
- [ ] `expertise.skills`: populated
- [ ] `collaborates_with`: placeholder (resolve after all roles named)
- [ ] `scope`: value from Phase 4 plan

After all roles written:

- [ ] Resolve all `collaborates_with` cross-references with actual role names
- [ ] Total role count ≥ 3 [ ] YES
- [ ] Distinct perspective categories ≥ 3 [ ] YES

PHASE 5 STATUS: [ ] COMPLETE

---

### PHASE 6 — VERIFICATION GATE

Entry gate: Phase 5 STATUS = COMPLETE

All four checks must pass as a unit. Delivery is blocked until this gate emits PASS.

**CHECK 1 — Registry Summary Table**

- [ ] Produce table:

```
| Role | Frame (one-line summary) | Scope | Collaborates With |
|------|--------------------------|-------|-------------------|
```

- [ ] Table complete with all roles: [ ] PASS

**CHECK 2 — Orphan Reference Audit**

- [ ] For every `collaborates_with` entry across all roles, verify the name exists in the registry:

```
| Role | collaborates_with entry | Exists in registry? |
|------|------------------------|---------------------|
```

- [ ] All rows YES: [ ] PASS / [ ] FAIL (list unresolved → fix → re-check)

**CHECK 3 — Scope Gradient Audit**

- [ ] Count distinct scope values across all final roles: ___
- [ ] Count ≥ 2: [ ] PASS / [ ] FAIL (revise roles → re-run CHECK 1 → re-check)

**CHECK 4 — Vocabulary Coverage Audit**

- [ ] For every role's `expertise.relevance`, confirm it names a term from Phase 1 buckets:

```
| Role | Term cited in expertise.relevance | In Phase 1 buckets? |
|------|-----------------------------------|---------------------|
```

- [ ] All rows YES: [ ] PASS / [ ] FAIL (revise roles → re-check)

**GATE EVALUATION**

```
CHECK 1: [ ] PASS
CHECK 2: [ ] PASS
CHECK 3: [ ] PASS
CHECK 4: [ ] PASS
```

All four checks PASS simultaneously →

```
VERIFICATION GATE: PASS
```

Write files to `.roles/{area}/`.

---
