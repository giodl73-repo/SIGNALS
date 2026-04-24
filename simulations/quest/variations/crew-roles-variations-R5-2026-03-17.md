## crew-roles — Skill Body Variations V-01 through V-05

---

## V-01 — Single Axis: Bucketed Vocabulary Extraction

**Variation axis:** Phase 1 structure
**Hypothesis:** Assigning each extracted term to a named Q-domain bucket during extraction removes any semantic judgment at Q-answer time — cross-domain selection becomes a structural impossibility, not a soft alignment check.

---

```markdown
# crew-roles

Generate a typed role registry for a domain. Analyze the provided input (product
description, codebase context, or feature brief) to determine what expert perspectives
are needed. Produce one markdown role file per role in `.roles/{area}/`. The
inertia-advocate role is always included.

Each role file must contain all five fields:
- name
- orientation  (frame, verify, simplify)
- expertise    (relevance)
- collaborates_with
- scope

---

## PHASE 1 — BUCKETED VOCABULARY EXTRACTION

Read the input. Extract all domain-specific terms. Assign every extracted term to
exactly one of the three named Q-domain buckets below. Do not produce a flat list.
Bucket membership is permanent; a term cannot appear in more than one bucket.

Output the three buckets before proceeding:

**Current-System Terms**
`[list every term that describes what the system currently does, its existing state,
legacy behavior, or prior implementation — these are Q1 candidates]`

**Migration-Cost Terms**
`[list every term that describes effort, risk, disruption, or investment required to
change the current system — these are Q2 candidates]`

**User-Habit Terms**
`[list every term that describes how users currently behave, what they expect, or
patterns they have internalized — these are Q3 candidates]`

EXIT CONDITION: Every significant domain term is assigned to exactly one bucket.
No term appears in two buckets. No unassigned terms remain.

---

## PHASE 2 — INERTIA PRE-CHARACTERIZATION

Answer three questions about the inertia dimension of this domain. Each answer
must reference at least one term drawn from the corresponding Q-domain bucket
from Phase 1. Cross-bucket selection fails Phase 2 exit without re-examination.

**Q1 — Current system** (draw from Current-System Terms):
What is the specific current system, implementation, or state this domain builds on
or replaces?
→ Answer: ___

**Q2 — Migration cost** (draw from Migration-Cost Terms):
What is the concrete cost, risk, or effort of changing from Q1 to something new?
→ Answer: ___

**Q3 — User habit** (draw from User-Habit Terms):
What user expectation, behavior, or workflow pattern is at stake?
→ Answer: ___

EXIT CONDITION: Q1 answer contains at least one Current-System Term. Q2 answer
contains at least one Migration-Cost Term. Q3 answer contains at least one
User-Habit Term. No Q answer reuses all three terms from a single bucket.

---

## PHASE 3 — PRE-WRITE SCOPE AUDIT

Before writing any role file, plan the full role set. For each planned role,
assign a preliminary scope value.

Output as a table:

| Planned Role | Preliminary Scope |
|---|---|
| (role name) | team / cross-team / org |

EXIT CONDITION: At least two distinct scope values appear in the table.
If all rows share one scope value, revise the plan until the condition is met.
Writing is blocked until this gate passes.

---

## PHASE 4 — ROLE WRITING

Write one markdown file per role. File path: `.roles/{area}/{role-name}.md`

### Inertia-Advocate (write first)

Build the inertia-advocate using the Phase 2 answers. The orientation frame must
name Q1 and Q2 explicitly, not paraphrase them.

```
name: inertia-advocate
orientation:
  frame: >
    The current system is [Q1 answer]. Replacing it costs [Q2 answer]. Users
    have internalized [Q3 answer]. Every proposed change must justify this cost.
  verify:
    - Why is [Q1 current system] insufficient for this use case?
    - What evidence do we have that the migration cost ([Q2]) is acceptable?
    - How does this change account for the [Q3 user habit] that exists today?
  simplify: >
    Strip any change that cannot demonstrate value exceeding [Q2 migration cost].
expertise:
  relevance: >
    [domain-specific framing using at least one Phase 1 vocabulary term]
collaborates_with:
  - [role-name]
scope: [value from Phase 3 scope audit]
```

### Remaining Roles

For each remaining planned role:

```
name: [role-name]
orientation:
  frame: >
    [domain-grounded perspective — reference at least one Phase 1 vocabulary term]
  verify:
    - [question ending in ?]
    - [question ending in ?]
  simplify: >
    [imperative sentence]
expertise:
  relevance: >
    [specific to this domain; must include at least one Phase 1 vocabulary term]
collaborates_with:
  - [role-name that matches another file in this registry]
scope: [value from Phase 3 scope audit]
```

---

## PHASE 5 — VERIFICATION GATE

Perform all checks below. The gate does not pass until every check is YES.
Output the check results explicitly before delivering files.

| Check | Result |
|---|---|
| All 5 fields present in every role file | YES / NO |
| Every collaborates_with references a name that exists in this registry | YES / NO |
| At least 2 distinct scope values across all roles | YES / NO |
| Every expertise.relevance contains at least one Phase 1 vocabulary term | YES / NO |
| Inertia frame references Q1 and Q2 by name (not paraphrase) | YES / NO |
| At least 3 perspective categories represented | YES / NO |

Any NO blocks delivery. Fix the failing role(s) and re-evaluate the check before
proceeding.

---

## REGISTRY SUMMARY TABLE

After the gate passes, output:

| Role | Orientation Frame (first 8 words) | Scope | Collaborates With |
|---|---|---|---|
```

---

---

## V-02 — Single Axis: Domain-Alignment Audit Table

**Variation axis:** Phase 2 exit mechanism
**Hypothesis:** A visible Q × Domain audit table at Phase 2 exit surfaces mismatches as YES/NO rows rather than prose judgment calls. A NO row is an explicit blocking artifact; it cannot be missed or soft-passed.

---

```markdown
# crew-roles

Generate a typed role registry for a domain. Analyze the input and produce one
markdown role file per role in `.roles/{area}/`. The inertia-advocate is
always present. Each file must contain: name, orientation (frame, verify, simplify),
expertise (relevance), collaborates_with, scope.

---

## PHASE 1 — VOCABULARY EXTRACTION

Extract domain-specific terms from the input. Produce a named list:

**Phase 1 Vocabulary:** [term1, term2, ...]

Tag each term with its primary domain: [CS] = current-system, [MC] = migration-cost,
[UH] = user-habit. Use brackets inline.

Example: `legacy-auth-flow [CS]`, `re-onboarding effort [MC]`, `muscle-memory shortcuts [UH]`

---

## PHASE 2 — INERTIA PRE-CHARACTERIZATION + DOMAIN-ALIGNMENT AUDIT

Answer three questions. Each answer must reference a vocabulary term tagged with
the matching domain indicator.

**Q1 — Current system [CS]:**
What is the specific current system this domain builds on or replaces?
→ Answer: ___

**Q2 — Migration cost [MC]:**
What is the concrete cost or risk of replacing Q1?
→ Answer: ___

**Q3 — User habit [UH]:**
What behavior or workflow pattern do users currently rely on?
→ Answer: ___

### Domain-Alignment Audit Table

After writing the three answers, produce this table:

| Q | Term Used in Answer | Expected Tag | Tag Present | Match |
|---|---|---|---|---|
| Q1 | (term from answer) | [CS] | (tag on this term) | YES / NO |
| Q2 | (term from answer) | [MC] | (tag on this term) | YES / NO |
| Q3 | (term from answer) | [UH] | (tag on this term) | YES / NO |

EXIT CONDITION: All three rows show YES.

If any row shows NO: replace the mismatched term with one that carries the correct
tag, rewrite the affected answer, and re-render the table. Phase 2 is not complete
until the table shows YES / YES / YES.

---

## PHASE 3 — PRE-WRITE SCOPE AUDIT

Plan the role set. Assign a scope value to each planned role before writing begins.

| Planned Role | Scope |
|---|---|

EXIT CONDITION: At least 2 distinct scope values are present.
If all roles share one scope, revise the plan.

---

## PHASE 4 — ROLE WRITING

### Inertia-Advocate (first)

Build from Phase 2 Q1, Q2, Q3 answers.

```
name: inertia-advocate
orientation:
  frame: >
    [Q1 current system answer]. The cost of replacement: [Q2 migration cost answer].
    Users rely on [Q3 user habit answer]. Challenge every change to justify this
    displacement.
  verify:
    - Why is the [Q1 term] approach no longer sufficient?
    - Does evidence show the [Q2 term] cost is acceptable at the required scale?
    - What accommodates the [Q3 term] pattern for current users?
  simplify: >
    Remove any change that cannot quantify its value relative to [Q2 term].
expertise:
  relevance: >
    [domain-specific; must include at least one Phase 1 vocabulary term]
collaborates_with:
  - [name]
scope: [from scope audit]
```

### Remaining Roles

```
name: [role-name]
orientation:
  frame: >
    [perspective framing using at least one Phase 1 vocabulary term]
  verify:
    - [question?]
    - [question?]
  simplify: >
    [imperative]
expertise:
  relevance: >
    [specific to this domain; at least one Phase 1 vocabulary term]
collaborates_with:
  - [name matching another file in this registry]
scope: [from scope audit]
```

---

## PHASE 5 — VERIFICATION GATE

Output the full check table. Gate does not pass until all rows are YES.

| Check | Result |
|---|---|
| All 5 fields present in every role file | YES / NO |
| Every collaborates_with resolves to a name in this registry | YES / NO |
| At least 2 distinct scope values | YES / NO |
| Every expertise.relevance references at least one Phase 1 vocabulary term | YES / NO |
| Inertia frame references Q1 and Q2 answers | YES / NO |
| Domain-alignment audit table all YES | YES / NO |
| At least 3 perspective categories | YES / NO |

Fix any NO before proceeding.

---

## REGISTRY SUMMARY TABLE

| Role | Orientation Frame (first 8 words) | Scope | Collaborates With |
|---|---|---|---|
```

---

---

## V-03 — Single Axis: Frame-Fill as Dedicated Named Phase

**Variation axis:** Frame-slot population mechanism
**Hypothesis:** Making frame-slot population a named phase between Q&A and role writing creates a detectable phase boundary. An unfilled `[Q1]` or `[Q2]` placeholder at that boundary is a blocking error visible before any file is written, rather than an inline omission discovered during review.

---

```markdown
# crew-roles

Generate a typed role registry for a domain. Produce one markdown role file per
role in `.roles/{area}/`. Inertia-advocate always present. Each file:
name, orientation (frame, verify, simplify), expertise (relevance),
collaborates_with, scope.

---

## PHASE 1 — VOCABULARY EXTRACTION

Extract domain-specific terms from the input. Output as a named list:

**Phase 1 Vocabulary:** [term1, term2, term3, ...]

These terms are available for use in expertise.relevance fields and inertia answers.

---

## PHASE 2 — INERTIA PRE-CHARACTERIZATION

Answer Q1, Q2, Q3. Each answer must reference at least one Phase 1 vocabulary term.

**Q1 — Current system:**
What specific system, implementation, or state does this domain build on or replace?
→ Answer: ___

**Q2 — Migration cost:**
What is the concrete cost, risk, or effort of displacing Q1?
→ Answer: ___

**Q3 — User habit:**
What behavior, expectation, or workflow pattern do existing users rely on?
→ Answer: ___

EXIT CONDITION: Each answer is complete. Q1, Q2, Q3 reference distinct vocabulary
terms. Phase 2 answers are inputs to Phase 3.

---

## PHASE 3 — FRAME FILL  ← named phase

This phase has one job: produce the completed inertia frame string.

The frame template is:

```
The current system is [Q1: current system]. Replacing it costs [Q2: migration cost].
Users have internalized [Q3: user habit]. Every proposed change must justify this
displacement.
```

Fill all three slots using Phase 2 answers. Output the completed frame string as
the single deliverable of this phase:

**Completed Frame:**
```
The current system is [filled from Q1]. Replacing it costs [filled from Q2].
Users have internalized [filled from Q3]. Every proposed change must justify this
displacement.
```

EXIT CONDITION: The completed frame string contains no unfilled placeholders. No
`[Q1:...]`, `[Q2:...]`, or `[Q3:...]` bracket notation remains. If any placeholder
is unfilled, return to Phase 2 and complete the missing answer before re-filling.

Role writing does not begin until this exit condition is met.

---

## PHASE 4 — PRE-WRITE SCOPE AUDIT

Plan the role set. Assign scope before writing.

| Planned Role | Scope |
|---|---|

EXIT CONDITION: At least 2 distinct scope values appear. Writing is blocked until
this condition is met.

---

## PHASE 5 — ROLE WRITING

### Inertia-Advocate (first)

Use the completed frame string from Phase 3 directly.

```
name: inertia-advocate
orientation:
  frame: >
    [paste completed frame string from Phase 3 here — no further modification]
  verify:
    - Why is the current system (from Q1) no longer sufficient for this use case?
    - Is the migration cost (from Q2) justified by the proposed benefit?
    - How does this change account for the user habit (from Q3) that exists today?
  simplify: >
    Cut any change that cannot demonstrate value exceeding the Q2 migration cost.
expertise:
  relevance: >
    [domain-specific; at least one Phase 1 vocabulary term]
collaborates_with:
  - [role-name]
scope: [from Phase 4 scope audit]
```

### Remaining Roles

```
name: [role-name]
orientation:
  frame: >
    [perspective anchored to this domain; at least one Phase 1 vocabulary term]
  verify:
    - [question?]
    - [question?]
  simplify: >
    [imperative]
expertise:
  relevance: >
    [domain-specific; at least one Phase 1 vocabulary term]
collaborates_with:
  - [name matching another file in this registry]
scope: [from Phase 4 scope audit]
```

---

## PHASE 6 — VERIFICATION GATE

All checks must pass before delivery.

| Check | Result |
|---|---|
| Phase 3 completed frame string contains no unfilled placeholders | YES / NO |
| Inertia frame in role file matches Phase 3 output exactly | YES / NO |
| All 5 fields present in every role file | YES / NO |
| Every collaborates_with resolves to a name in this registry | YES / NO |
| At least 2 distinct scope values | YES / NO |
| Every expertise.relevance contains at least one Phase 1 term | YES / NO |
| At least 3 perspective categories represented | YES / NO |

Fix any NO. Re-evaluate.

---

## REGISTRY SUMMARY TABLE

| Role | Orientation Frame (first 8 words) | Scope | Collaborates With |
|---|---|---|---|
```

---

---

## V-04 — Combined: Lifecycle Emphasis × Formal Register

**Variation axes:** Lifecycle emphasis (explicit phase headers, explicit blockers, every gate labeled) + Phrasing register (formal/technical, imperative throughout, no conversational softeners)
**Hypothesis:** Combining unambiguous phase boundaries with a consistently imperative register removes the hedging language that allows an LLM to skip a gate by treating it as a suggestion rather than a hard precondition.

---

```markdown
# crew-roles

## PURPOSE

Produce a typed role registry for a domain. Input: product description, codebase
context, or feature brief. Output: one markdown file per role at
`.roles/{area}/{role-name}.md`. The inertia-advocate role is mandatory.

## REQUIRED FIELDS (all five must be present in every file)

| Field | Type |
|---|---|
| name | string |
| orientation.frame | string |
| orientation.verify | list of questions (each ending in ?) |
| orientation.simplify | imperative string |
| expertise.relevance | string (must reference at least one Phase 1 term) |
| collaborates_with | list of role names (must resolve within this registry) |
| scope | one of: team, cross-team, org |

---

## EXECUTION SEQUENCE

Phases execute in order. No phase may begin until the preceding phase has met its
stated EXIT CONDITION. An unmet EXIT CONDITION is a blocking error, not a warning.

---

### PHASE 1: BUCKETED VOCABULARY EXTRACTION

**Input:** All provided text.
**Task:** Extract domain-specific terms. Assign each term to exactly one of the
three named Q-domain buckets. Do not produce a flat list. Do not assign a term to
more than one bucket.

**Output** (required before Phase 2 may begin):

**Bucket A — Current-System Terms:**
`[terms describing existing system state, legacy implementations, prior behavior]`

**Bucket B — Migration-Cost Terms:**
`[terms describing effort, risk, disruption, investment, or friction of change]`

**Bucket C — User-Habit Terms:**
`[terms describing user expectations, learned behaviors, or workflow patterns]`

**EXIT CONDITION:** Every significant domain term is assigned to one bucket.
No term appears in two buckets. If any term is unassigned, assign it before exiting.

---

### PHASE 2: INERTIA PRE-CHARACTERIZATION

**Input:** Phase 1 bucket output.
**Task:** Answer Q1, Q2, Q3. Each answer must draw its primary term from the
corresponding bucket. Cross-bucket term selection is a Phase 2 EXIT FAILURE.

**Q1** — Draw from Bucket A (Current-System Terms):
State the specific current system, implementation, or state this domain operates on
or displaces.
→ **Q1 Answer:**

**Q2** — Draw from Bucket B (Migration-Cost Terms):
State the concrete cost, risk, or effort of replacing or changing Q1.
→ **Q2 Answer:**

**Q3** — Draw from Bucket C (User-Habit Terms):
State the specific behavior, expectation, or workflow pattern users currently
rely on.
→ **Q3 Answer:**

**DOMAIN-ALIGNMENT AUDIT TABLE** (required; produced after writing Q1/Q2/Q3):

| Q | Primary Term Used | Required Bucket | Term's Actual Bucket | Match |
|---|---|---|---|---|
| Q1 | | Bucket A | | YES / NO |
| Q2 | | Bucket B | | YES / NO |
| Q3 | | Bucket C | | YES / NO |

**EXIT CONDITION:** All three rows show YES. Any NO requires: (1) replace the
offending term with a term from the correct bucket, (2) rewrite the affected
answer, (3) re-render the audit table. Phase 2 is not complete until all rows
are YES.

---

### PHASE 3: FRAME FILL

**Input:** Phase 2 Q1, Q2, Q3 answers.
**Task:** Produce the completed inertia frame string. This phase has no other
deliverable.

**Frame template:**

```
The current system is [Q1]. Replacing it costs [Q2]. Users have internalized [Q3].
Challenge every proposed change to justify this displacement.
```

**Fill each slot with the corresponding Phase 2 answer.**

**Completed Frame** (output as a discrete labeled block):

```
[completed frame string — all three slots filled, no bracket notation remaining]
```

**EXIT CONDITION:** The completed frame string contains no unfilled bracket
placeholders. Any remaining `[Q1]`, `[Q2]`, or `[Q3]` is a Phase 3 blocking error.
Return to Phase 2 and complete the missing answer before re-executing Phase 3.
Phase 4 does not begin until this condition is met.

---

### PHASE 4: PRE-WRITE SCOPE AUDIT

**Input:** Intended role set (names + descriptions only).
**Task:** Assign a preliminary scope value to each planned role before writing begins.

| Planned Role Name | Preliminary Scope |
|---|---|
| | team / cross-team / org |

**EXIT CONDITION:** At least two distinct scope values appear in the table.
If all rows carry the same scope value, revise the role plan. Writing is blocked
until the condition is met. Do not proceed to Phase 5 until the audit table
satisfies the condition.

---

### PHASE 5: ROLE WRITING

**Order:** Write the inertia-advocate first. Write remaining roles in the order
established by the Phase 4 scope audit table.

#### Inertia-Advocate

```yaml
name: inertia-advocate
orientation:
  frame: >
    [insert completed frame string from Phase 3 verbatim]
  verify:
    - Why is [Q1 current system term] no longer sufficient for this use case?
    - What evidence shows that [Q2 migration cost term] is justified?
    - How does this change preserve or address the [Q3 user habit term]?
  simplify: >
    Eliminate any change that cannot demonstrate value exceeding [Q2 migration cost].
expertise:
  relevance: >
    [domain-grounded statement; must include at least one Phase 1 vocabulary term]
collaborates_with:
  - [role-name]
scope: [value from Phase 4 scope audit]
```

#### All Other Roles

```yaml
name: [role-name]
orientation:
  frame: >
    [perspective grounded in this domain; must include at least one Phase 1 term]
  verify:
    - [question ending in ?]
    - [question ending in ?]
  simplify: >
    [imperative sentence]
expertise:
  relevance: >
    [specific to this domain; must include at least one Phase 1 term]
collaborates_with:
  - [name that exists in this registry]
scope: [value from Phase 4 scope audit]
```

---

### PHASE 6: VERIFICATION GATE

**All checks must show YES. This gate does not pass until every row is YES.**
**Delivery is blocked until the gate passes.**

| Check | Result |
|---|---|
| All 5 required fields present in every role file | YES / NO |
| Every collaborates_with value resolves to a name in this registry | YES / NO |
| At least 2 distinct scope values across all roles | YES / NO |
| Every expertise.relevance references at least one Phase 1 vocabulary term | YES / NO |
| Inertia frame matches Phase 3 completed frame string | YES / NO |
| Domain-alignment audit table (Phase 2) all rows YES | YES / NO |
| Phase 3 completed frame contains no unfilled placeholders | YES / NO |
| At least 3 distinct perspective categories represented across roles | YES / NO |

For each NO: identify the failing role or artifact, correct it, re-evaluate that
row. Reissue the full table after corrections.

---

### PHASE 7: REGISTRY SUMMARY TABLE

Output after the gate passes:

| Role | Frame Summary (first 8 words) | Scope | Collaborates With |
|---|---|---|---|
```

---

---

## V-05 — Combined: Inertia Framing Prominence × Role Sequence (Inertia-First)

**Variation axes:** Inertia framing prominence (inertia pre-characterization precedes all other planning, vocabulary is extracted through the inertia lens) + Role sequence (inertia-advocate authored first, all other roles defined in relation to it)
**Hypothesis:** Running inertia characterization before scope audit or generic role planning forces domain anchoring before any role can be written. Generic roles cannot be planned until the inertia story constrains the space — reducing the chance that roles are defined in the abstract and then inertia is bolted on afterward.

---

```markdown
# crew-roles

Build a role registry that knows what it's fighting. The inertia-advocate is not
a boilerplate inclusion — it's the anchor that makes every other role's perspective
meaningful. We build the inertia story first, then define roles in relation to it.

Output: one markdown file per role at `.roles/{area}/{role-name}.md`.
Required fields in every file: name, orientation (frame, verify, simplify),
expertise (relevance), collaborates_with, scope.

---

## STEP 1 — READ THE INERTIA STORY

Before extracting vocabulary or planning roles, answer these three questions from
the input. These answers define what you're working against.

**What is the current system?**
Name the specific thing in place today — the implementation, the approach, the
workflow, the artifact. Use the domain's own vocabulary.
→ Current system:

**What does replacing it cost?**
Be concrete. Think effort, risk, re-training, migration, API breaks, data
transformation, user disruption — whatever the input implies.
→ Migration cost:

**What have users learned to live with?**
The shortcuts, workarounds, mental models, or muscle-memory habits that exist
because of Q1. Not aspirational behavior — current behavior.
→ User habit:

Do not proceed to Step 2 until all three answers are present.

---

## STEP 2 — VOCABULARY EXTRACTION (THROUGH THE INERTIA LENS)

Extract domain-specific terms from the full input. Organize them into three
labeled buckets. The labels match the Q-dimensions from Step 1.

**Current-System Terms** (Q1 domain):
`[terms that describe or elaborate the current system from Step 1]`

**Migration-Cost Terms** (Q2 domain):
`[terms that describe the cost, risk, or friction of change]`

**User-Habit Terms** (Q3 domain):
`[terms that describe user behaviors, expectations, or learned patterns]`

The bucket labels are not cosmetic. In Step 3, Q1 draws from Current-System Terms,
Q2 draws from Migration-Cost Terms, Q3 draws from User-Habit Terms. Terms are
pre-sorted; selection cannot go cross-bucket.

---

## STEP 3 — BUILD THE INERTIA FRAME

Construct the inertia-advocate's frame string. The frame uses the Step 1 answers
directly and incorporates at least one vocabulary term per bucket.

**Frame template:**

```
The current system is [Step 1 current system]. The cost of replacing it is
[Step 1 migration cost]. Users have built their workflow around
[Step 1 user habit]. Any change must justify displacement of all three.
```

**Verify term coverage before proceeding:**

| Slot | Step 1 Answer Used | Vocabulary Term Included | Term's Bucket |
|---|---|---|---|
| Current system | | | Current-System Terms |
| Migration cost | | | Migration-Cost Terms |
| User habit | | | User-Habit Terms |

All three rows must show a vocabulary term from the matching bucket. Fix any gap
before Step 4.

**Completed Frame:**

```
[completed frame — no unfilled slots, no bracket notation]
```

Step 4 does not begin until the completed frame is produced.

---

## STEP 4 — SCOPE AUDIT (PLAN ALL ROLES BEFORE WRITING ANY)

Name every role you intend to write, including the inertia-advocate. Assign a
scope. The inertia-advocate's scope is fixed from the input context — assign it
first, then balance the rest.

| Role | Scope |
|---|---|
| inertia-advocate | (assign based on what the domain warrants) |
| (other roles) | team / cross-team / org |

At least 2 distinct scope values must appear before writing begins.
If the set is homogeneous, revise it now.

---

## STEP 5 — WRITE INERTIA-ADVOCATE

The inertia-advocate is always written first. Other roles are written in relation
to it. Use the completed frame from Step 3 verbatim.

```yaml
name: inertia-advocate
orientation:
  frame: >
    [completed frame string from Step 3]
  verify:
    - Why is [current system term from Step 1] no longer adequate for this need?
    - Has the [migration cost term] been quantified and accepted by stakeholders?
    - What happens to users who depend on [user habit term] when this changes?
  simplify: >
    Remove every change that has not accounted for [migration cost term].
expertise:
  relevance: >
    [Grounds the advocate in this domain's specific context. Must reference at
    least one Current-System Term from Step 2.]
collaborates_with:
  - [role-name — will be filled once other roles are named in Step 6]
scope: [from Step 4 scope audit]
```

---

## STEP 6 — WRITE REMAINING ROLES

Write each remaining role from the Step 4 plan. Each role is defined in relation
to the inertia story: its verify questions may challenge or complement the
inertia-advocate's framing, but they must be aware of it.

```yaml
name: [role-name]
orientation:
  frame: >
    [perspective on this domain — must reference at least one Step 2 vocabulary
    term; may engage with or extend the inertia story directly]
  verify:
    - [question that tests this role's perspective — ends in ?]
    - [question — ends in ?]
  simplify: >
    [imperative]
expertise:
  relevance: >
    [anchored to this domain; must include at least one Step 2 vocabulary term]
collaborates_with:
  - [name matching another file in this registry]
scope: [from Step 4 scope audit]
```

Minimum 3 roles total (including inertia-advocate). At least 3 perspective
categories must be represented.

---

## STEP 7 — VERIFICATION GATE

Run all checks. Gate does not pass until every row is YES. Fix and re-check.

| Check | Result |
|---|---|
| All 5 required fields present in every role file | YES / NO |
| Inertia-advocate completed frame matches Step 3 output | YES / NO |
| Step 3 term-coverage table all rows have a matching-bucket term | YES / NO |
| Every collaborates_with resolves to a name in this registry | YES / NO |
| At least 2 distinct scope values | YES / NO |
| Every expertise.relevance includes at least one Step 2 vocabulary term | YES / NO |
| At least 3 perspective categories represented | YES / NO |
| Minimum 3 roles present | YES / NO |

---

## REGISTRY SUMMARY TABLE

| Role | Frame Summary (first 8 words) | Scope | Collaborates With |
|---|---|---|---|
```

---

## Summary

| Variation | Axis | Key Mechanism | Targets |
|---|---|---|---|
| V-01 | Bucketed vocabulary extraction | Phase 1 splits terms into 3 Q-domain buckets; cross-bucket Q-answers fail at exit | C-21 |
| V-02 | Domain-alignment audit table | Explicit YES/NO table gates Phase 2 exit; NO triggers rewrite + re-evaluation | C-22 |
| V-03 | Frame-fill as dedicated named phase | Phase 3 produces completed frame string as sole deliverable; unfilled slots block Phase 4 | C-23 |
| V-04 | Lifecycle emphasis + formal register | All three new mechanisms + maximum phase-boundary explicitness + imperative-only phrasing | C-21, C-22, C-23 |
| V-05 | Inertia framing prominence + role sequence | Inertia characterization precedes all planning; roles defined against the inertia story; vocabulary bucketed through inertia lens | C-20, C-21, C-23 |
