## crew-roles — Quest Variate R6 (V-01 through V-05)

---

### V-01

**Variation axis:** Lifecycle emphasis
**Hypothesis:** Naming every phase as a discrete structural unit with an explicit entry precondition and a named exit artifact makes blocking gates unavoidable at execution time, increasing pass rates on C-15, C-17, C-22, C-23, C-24, C-25.

---

Generate a typed role registry for the specified domain.

Output path: `.roles/{area}/`
Each role file requires: `name`, `orientation` (frame, verify, simplify), `expertise` (relevance, depth), `scope`, `collaborates_with`.
The inertia-advocate role is mandatory in every registry.

---

#### PHASE 1 — VOCABULARY EXTRACTION

**Entry precondition:** domain description or codebase context is present.

Read the input and extract domain vocabulary into three named buckets:

- **Current-System Terms** — names of systems, tools, frameworks, or patterns currently in use.
- **Migration-Cost Terms** — terms describing switching costs, integration burden, retraining effort, compatibility gaps.
- **User-Habit Terms** — terms describing established workflows, learned behaviors, or adoption patterns.

Each term is assigned to exactly one bucket at extraction time. Cross-bucket assignment is not permitted. Assign during extraction, not after.

**Phase 1 exit artifact:** three labeled bucket lists, each containing at least 2 terms. Phase 2 does not begin until this artifact is present in the output.

---

#### PHASE 2 — INERTIA PRE-CHARACTERIZATION

**Entry precondition:** Phase 1 exit artifact is present.

Answer three questions, drawing each answer from its designated bucket:

- **Q1 (Current System):** What specific system, tool, or pattern does this domain currently rely on? Answer must use a **Current-System Term**.
- **Q2 (Migration Cost):** What is the primary cost of moving away from that system? Answer must use a **Migration-Cost Term**.
- **Q3 (User Habit):** What established user workflow or habit would be disrupted? Answer must use a **User-Habit Term**.

After answering, produce the Domain-Alignment Audit Table:

| Q-number | Term Used | Expected Bucket | Match YES/NO |
|----------|-----------|-----------------|--------------|
| Q1 | {term} | Current-System | YES/NO |
| Q2 | {term} | Migration-Cost | YES/NO |
| Q3 | {term} | User-Habit | YES/NO |

**Gate condition:** all three rows must show YES simultaneously. Evaluating rows independently does not satisfy the gate.

**If any row shows NO:**
1. Replace the term in that answer with a term drawn from the correct bucket.
2. Restart the audit table from row 1.
3. Re-evaluate all three rows at once.
4. The gate condition is evaluated against the full table, not against the replaced row alone. An incremental re-score of only the replaced row does not satisfy the gate — a replacement term may pass its own row while reusing a term already used in another row or drawing from an adjacent bucket, introducing a cross-row conflict that only a full pass detects.

Repeat until all rows show YES with no cross-bucket reuse before Phase 2 closes.

**Phase 2 exit artifact:** answered Q1/Q2/Q3 + completed audit table (all three rows YES, no cross-bucket reuse). Phase 3 does not begin until this artifact is present.

---

#### PHASE 3 — FRAME FILL

**Entry precondition:** Phase 2 exit artifact is present.

The inertia-advocate's `orientation.frame` uses this template:

> `"[Q1 current system] is the established approach; adoption cost is [Q2 migration cost]. Before adding complexity, prove [Q1 current system] cannot do this."`

Fill both slots from Phase 2 answers. Record slot-source bindings explicitly:

```
Q1 slot ← Phase 2 Q1: [verbatim Q1 answer]
Q2 slot ← Phase 2 Q2: [verbatim Q2 answer]
Completed frame: [filled frame string]
```

**Slot-binding verification:**
- Q1 slot must be drawn from the Q1 answer, not Q2 or Q3.
- Q2 slot must be drawn from the Q2 answer, not Q1 or Q3.
- A mismatch in either binding is a blocking error.

A completed frame string without source citations does not satisfy the Frame Fill phase exit condition.

**Phase 3 exit artifact:** completed frame string + slot-source binding record with citations. Phase 4 does not begin until this artifact is present.

---

#### PHASE 4 — PRE-WRITE SCOPE AUDIT

**Entry precondition:** Phase 3 exit artifact is present.

Before writing any role file, survey the planned role set and assign scope values:

| Planned Role | Intended Scope |
|-------------|---------------|
| {role name} | team / cross-team / org |
| … | … |

**Gate condition:** at least 2 distinct scope values must appear in the plan before writing begins. If all planned roles share the same scope, identify and revise 1–2 roles until the gate passes. Writing is blocked until the gate passes — this is a prevention step, not a post-write correction.

**Phase 4 exit artifact:** planned role table with confirmed ≥ 2 distinct scope values. Phase 5 does not begin until this artifact is present.

---

#### PHASE 5 — ROLE WRITING

**Entry precondition:** Phase 4 exit artifact is present.

Write each role as a markdown file at `.roles/{area}/{role-name}.md`.

**Required fields in every role file:**

- `name`
- `orientation.frame` — the role's core interpretive lens (one sentence)
- `orientation.verify` — questions only; every item ends with `?`
- `orientation.simplify` — imperatives only; every item is an action phrase
- `expertise.relevance` — must reference at least one vocabulary term from Phase 1
- `expertise.depth`
- `scope` — one of: `team`, `cross-team`, `org`
- `collaborates_with` — list of other role names in this registry

**Inertia-advocate requirements:**
- `orientation.frame`: use the completed frame string from Phase 3 verbatim.
- `orientation.verify` questions must reference at least 2 of the 3 Phase 2 dimensions (current system, migration cost, user habit).
- `expertise.relevance` must reference at least one Phase 1 vocabulary term.

**Registry requirements:**
- Minimum 3 roles total, including the inertia-advocate.
- Roles span at least 3 distinct perspective categories (e.g., product, technical, inertia, domain-specialist).

---

#### PHASE 6 — VERIFICATION GATE

**Entry precondition:** all roles are written.

Run all structural checks as a single named gate. Delivery is blocked until every check shows PASS. A single FAIL blocks delivery regardless of other checks passing.

**CHECK 1 — Registry Summary Table**

Produce a complete table of all written roles:

| Role | Orientation Frame (excerpt) | Scope | Collaborates With |
|------|-----------------------------|-------|-------------------|
| … | … | … | … |

Every written role must appear in this table.

**CHECK 2 — Orphan Reference Check**

For every `collaborates_with` value across all role files: verify the referenced name matches a file in the registry. List each reference and its resolution status. Any unresolved reference is a blocking error.

Result: PASS / FAIL

**CHECK 3 — Scope Gradient Check**

Verify ≥ 2 distinct scope values are present across the registry. If FAIL: identify which roles to revise and revise them before re-running the gate.

Result: PASS / FAIL

**CHECK 4 — Vocabulary Coverage Check**

For every role file, verify `expertise.relevance` references at least one Phase 1 vocabulary term. List each role alongside the vocabulary term it references. Any role without a vocabulary reference is a blocking error.

Result: PASS / FAIL

**Gate condition:** CHECK 1 through CHECK 4 all PASS. Deliver registry only after this condition is confirmed in the output.

---

---

### V-02

**Variation axis:** Inertia framing
**Hypothesis:** Foregrounding the inertia-advocate as the anchor role — establishing its characterization before planning other roles — increases C-10, C-12, C-16, C-19, C-20 pass rates because every subsequent role is defined in explicit contrast to a grounded status-quo analysis rather than defaulting to additive framing.

---

Generate a typed role registry for the specified domain.

Output path: `.roles/{area}/`
Each role file requires: `name`, `orientation` (frame, verify, simplify), `expertise` (relevance, depth), `scope`, `collaborates_with`.

The inertia-advocate is not one role among many. It is the organizing center of the registry. Every other role is defined partly in contrast to the resistance it names. Build the inertia-advocate first; let its characterization anchor the vocabulary and framing choices for the rest.

---

#### STEP 1 — DOMAIN VOCABULARY (Bucketed)

Read the input. Extract domain vocabulary into three named buckets before writing any role content:

**Bucket A — Current-System Terms:** specific names for the systems, tools, or patterns the domain currently depends on.
**Bucket B — Migration-Cost Terms:** terms for switching costs, integration burden, retraining, compatibility gaps.
**Bucket C — User-Habit Terms:** terms for established workflows, learned behaviors, adoption inertia.

Assign each term to exactly one bucket during extraction. No term may appear in two buckets. Minimum 2 terms per bucket.

Output the three buckets in full before proceeding.

---

#### STEP 2 — INERTIA ANCHOR

The inertia-advocate gives the registry its gravity. Before writing any role, answer three characterization questions explicitly. Each answer must use a term from its designated bucket.

**Q1 — Current System** *(draw from Bucket A):* What specific existing system, tool, or pattern does this domain rely on? Name it directly.

**Q2 — Migration Cost** *(draw from Bucket B):* What is the primary cost a team incurs when moving away from that system? Name it directly.

**Q3 — User Habit** *(draw from Bucket C):* What established user workflow or adoption pattern would be disrupted? Name it directly.

After writing Q1/Q2/Q3 answers, produce the Domain-Alignment Audit Table:

| Q-number | Term Used | Required Bucket | Match YES/NO |
|----------|-----------|-----------------|--------------|
| Q1 | {term} | Bucket A (Current-System) | YES/NO |
| Q2 | {term} | Migration-Cost | YES/NO |
| Q3 | {term} | User-Habit | YES/NO |

**Gate:** All three rows YES simultaneously. The gate evaluates all rows at once — not row-by-row.

**If any row shows NO:** replace the term in that answer with a term from the correct bucket, then restart the table from Q1. Re-evaluate all three rows together. Repeat until all rows YES with no cross-bucket reuse. A term that passes its own row but duplicates a term used in another row, or draws from an adjacent bucket, is a cross-row conflict — visible only when the table is evaluated as a unit.

Record the confirmed answers before proceeding.

---

#### STEP 3 — INERTIA FRAME FILL

The inertia-advocate's `orientation.frame` follows this template:

> `"[Q1 current system] is the established approach; adoption cost is [Q2 migration cost]. Before adding complexity, prove [Q1 current system] cannot do this."`

Fill Q1 and Q2 slots from Step 2 answers. Record the binding explicitly:

```
Q1 slot ← Step 2 Q1: [verbatim answer]
Q2 slot ← Step 2 Q2: [verbatim answer]
Completed frame: [filled string]
```

Verification: Q1 slot is drawn from the Q1 answer; Q2 slot is drawn from the Q2 answer. Using a Q2 answer in the Q1 slot, or vice versa, is a binding error that blocks this step. A completed frame without explicit source citations does not satisfy the exit condition of this step.

---

#### STEP 4 — INERTIA-ADVOCATE ROLE (Written First)

Write the inertia-advocate role file at `.roles/{area}/inertia-advocate.md`.

```yaml
name: inertia-advocate
orientation:
  frame: "[completed frame from Step 3]"
  verify:
    - "Has [Q1 current system] been proven insufficient for this use case?"
    - "What is the estimated [Q2 migration cost] if this change is adopted?"
    - "Which [Q3 user habit] must change, and what is the retraining plan?"
    - "[domain-specific verify question]"
  simplify:
    - "Name the specific limitation of [Q1 current system] before proposing a replacement."
    - "Quantify [Q2 migration cost] before the proposal advances."
expertise:
  relevance: "[references at least one Bucket A term, plus domain context]"
  depth: senior
scope: cross-team
collaborates_with:
  - [other roles — to be filled in Step 6 after registry is complete]
```

The verify questions must reference at least 2 of the 3 Step 2 dimensions (Q1 current system, Q2 migration cost, Q3 user habit). The frame is used verbatim from Step 3.

---

#### STEP 5 — REMAINING ROLES (Planned Relative to Inertia-Advocate)

Plan the remaining roles. Each non-inertia role should be describable in terms of what it contributes that the inertia-advocate does not cover — the gap, the forward-looking perspective, the domain expertise the inertia-advocate's resistance sharpens.

**Pre-write scope plan:**

| Planned Role | Perspective Category | Intended Scope |
|-------------|---------------------|---------------|
| inertia-advocate | inertia | cross-team |
| {role} | {category} | team / cross-team / org |
| … | … | … |

**Scope gate:** at least 2 distinct scope values must appear in the plan before writing. If all roles share one scope, revise 1–2 planned roles. Writing is blocked until the gate passes.

Write each additional role at `.roles/{area}/{role-name}.md`. Required fields in every role file:

- `name`
- `orientation.frame` — one-sentence interpretive lens; must differ from the inertia-advocate's frame
- `orientation.verify` — questions only (each ends with `?`)
- `orientation.simplify` — imperatives only (action phrases)
- `expertise.relevance` — must reference at least one term from the Step 1 vocabulary
- `expertise.depth`
- `scope`
- `collaborates_with`

Perspective categories must span at least 3 distinct types across the full registry (product, technical, inertia, domain-specialist, etc.). Minimum 3 roles total including the inertia-advocate.

---

#### STEP 6 — VERIFICATION GATE

Run as a single named gate. All checks must PASS before delivery. Any FAIL blocks the registry.

**CHECK 1 — Registry Summary Table**

| Role | Frame (excerpt) | Scope | Collaborates With |
|------|-----------------|-------|-------------------|

Every role must appear. Produce the table now.

**CHECK 2 — Orphan Reference Check**
Verify every `collaborates_with` entry resolves to a file in the registry. PASS / FAIL.
Any unresolved reference is a blocking error.

**CHECK 3 — Scope Gradient Check**
Verify ≥ 2 distinct scope values are present. PASS / FAIL.
If FAIL: revise before redelivering.

**CHECK 4 — Vocabulary Coverage Check**
Verify every `expertise.relevance` field references at least one Step 1 vocabulary term. List role → term pairings. PASS / FAIL.

Gate: CHECK 1–4 all PASS. Deliver only after gate confirmation appears in output.

---

---

### V-03

**Variation axis:** Phrasing register (conversational, second-person, descriptive over imperative)
**Hypothesis:** A conversational phrasing register reduces cognitive friction during execution, making the structural sequence easier to follow without degrading compliance with blocking gates, increasing C-11, C-12, C-13, C-14 pass rates by reducing skip-ahead behavior.

---

You're building a typed role registry for the domain provided. By the time you're done, you'll have a set of markdown role files that give reviewers distinct, domain-grounded perspectives — each one doing something the others don't.

Roles go in `.roles/{area}/`. Every role file needs five things: `name`, `orientation` (which has `frame`, `verify`, and `simplify` subfields), `expertise` (with `relevance` and `depth`), `scope`, and `collaborates_with`. The inertia-advocate is always included — it's the role that asks whether the current approach actually needs replacing.

Work through this in order. Each step needs to finish before the next one begins.

---

#### Step 1: Pull out the domain vocabulary (three buckets)

Start by reading the domain input and extracting terms into three labeled groups:

**Current-System Terms** — what's already being used (tools, systems, frameworks, patterns with names).
**Migration-Cost Terms** — what it costs to move away (switching overhead, integration effort, retraining, compatibility issues).
**User-Habit Terms** — what users are used to doing (workflows, learned behaviors, adoption patterns).

Put each term in one group only — don't double-assign. You need at least two terms per group to continue.

Write out all three groups before moving on.

---

#### Step 2: Answer three questions about the status quo

Before you write any role, you need to understand what the inertia-advocate is defending. Answer these questions — each answer should name a term you just extracted, drawn from its matching group:

- **Q1 (current system):** What's the specific existing system, tool, or pattern this domain depends on right now? Use a Current-System Term.
- **Q2 (migration cost):** What's the biggest cost of moving away from it? Use a Migration-Cost Term.
- **Q3 (user habit):** What established workflow or behavior would need to change? Use a User-Habit Term.

Once you've written your answers, check them against this table:

| Q | Term you used | Group it should come from | Does it match? |
|---|---------------|--------------------------|----------------|
| Q1 | {term} | Current-System | YES / NO |
| Q2 | {term} | Migration-Cost | YES / NO |
| Q3 | {term} | User-Habit | YES / NO |

All three rows need to say YES — and you need to look at all three at the same time, not one by one. Here's why that matters: replacing a term in one row might fix that row while accidentally reusing a term from another row, or pulling from the wrong group. That kind of cross-row issue only shows up when you evaluate the table as a whole.

If anything says NO: swap the term for one from the right group, then rerun the table from Q1. Keep going until all three say YES with no cross-group reuse.

Don't move to Step 3 until your answers and the completed table (all YES) are both in the output.

---

#### Step 3: Fill the inertia frame

The inertia-advocate's frame follows a template with two slots:

> `"[Q1 current system] is the established approach; adoption cost is [Q2 migration cost]. Before adding complexity, prove [Q1 current system] cannot do this."`

Fill both slots from your Step 2 answers and record where each slot came from:

```
Q1 slot ← Step 2 Q1: [your verbatim Q1 answer]
Q2 slot ← Step 2 Q2: [your verbatim Q2 answer]
Completed frame: [the filled sentence]
```

One thing to confirm: Q1 is drawn from Q1, and Q2 is drawn from Q2. Using a Q2 answer in the Q1 slot is a mismatch that blocks this step. The frame string alone (without the citations) isn't enough to close this step.

---

#### Step 4: Plan your roles before writing any

List out the roles you intend to write, including the inertia-advocate, and note the scope for each:

| Role | Perspective type | Scope |
|------|-----------------|-------|
| inertia-advocate | inertia | cross-team |
| {role} | {type} | team / cross-team / org |
| … | … | … |

You need at least two different scope values in the plan before you start writing. If everything is the same scope, adjust one or two roles now. This needs to be sorted out before you write any files.

You also need at least three distinct perspective types across the whole set (product, technical, inertia, domain-specialist, or whatever fits the domain).

---

#### Step 5: Write the role files

Write each role to `.roles/{area}/{role-name}.md`.

Every file needs all of these:

- `name`
- `orientation.frame` — one-sentence interpretive lens for this role
- `orientation.verify` — a list of questions (each one ends with `?`)
- `orientation.simplify` — a list of action phrases (imperatives, not questions)
- `expertise.relevance` — ground this in the domain; reference at least one term from your Step 1 vocabulary
- `expertise.depth`
- `scope`
- `collaborates_with` — names of other roles in this registry

For the inertia-advocate specifically:
- `orientation.frame` uses the completed frame from Step 3, word for word.
- `orientation.verify` should touch at least two of the three Step 2 dimensions (current system, migration cost, user habit).
- `expertise.relevance` references at least one Step 1 term.

Minimum three roles total.

---

#### Step 6: Run the verification gate

Before you deliver anything, run these four checks together as a single gate. Every check needs to pass — one failure blocks delivery.

**Check 1 — Registry table**
Write out a summary table:
| Role | Frame (short excerpt) | Scope | Collaborates With |
Every role you wrote should appear here.

**Check 2 — Collaborates-with resolution**
Go through every `collaborates_with` entry across all files. Does each name match an actual file in the registry? Any name that doesn't match is an orphan reference — that's a blocking error. PASS / FAIL.

**Check 3 — Scope variety**
Do you have at least two different scope values across the registry? PASS / FAIL. If not, revise before delivering.

**Check 4 — Vocabulary coverage**
Does every `expertise.relevance` field name a term from Step 1? List each role and the term it references. Any role without a vocabulary tie is a blocking error. PASS / FAIL.

Once all four checks show PASS, deliver the registry.

---

---

### V-04

**Variation axis:** Role sequence + Output format
**Hypothesis:** Ordering roles by scope (team → cross-team → org) and anchoring every phase output as a table creates a naturally traversable output structure, increasing C-09, C-13, C-14, C-17 pass rates by making scope distribution visually scannable throughout execution rather than only at the verification gate.

---

Generate a typed role registry for the specified domain.

Output path: `.roles/{area}/`
Required fields per role file: `name`, `orientation` (frame / verify / simplify), `expertise` (relevance / depth), `scope`, `collaborates_with`.
Inertia-advocate is required. Roles are written in scope order: `team` roles first, `cross-team` roles second, `org` roles last.

---

#### PHASE 1 — BUCKETED VOCABULARY

Extract domain vocabulary. Produce a separate table for each bucket:

**Bucket A — Current-System Terms**

| Term | Where it appears in the domain |
|------|-------------------------------|
| {term} | {brief origin note} |

**Bucket B — Migration-Cost Terms**

| Term | Cost dimension |
|------|---------------|
| {term} | {brief origin note} |

**Bucket C — User-Habit Terms**

| Term | Workflow or behavior |
|------|---------------------|
| {term} | {brief origin note} |

Minimum 2 rows per table. Each term appears in exactly one table.

Phase 1 is complete when all three tables are present. Phase 2 does not begin until they are.

---

#### PHASE 2 — INERTIA CHARACTERIZATION

Produce a single characterization table:

| Question | Answer | Term Used | Required Bucket | Match YES/NO |
|----------|--------|-----------|-----------------|--------------|
| Q1: What is the current system? | {answer} | {term} | A (Current-System) | YES/NO |
| Q2: What is the migration cost? | {answer} | {term} | B (Migration-Cost) | YES/NO |
| Q3: What user habit is at stake? | {answer} | {term} | C (User-Habit) | YES/NO |

Gate condition: all three Match cells YES simultaneously.

If any cell shows NO: replace the term in that answer with a term from the correct bucket, then rebuild the table from Q1. Re-evaluate all three rows together. The gate condition is evaluated against all rows as a unit — replacing only the failing row and re-scoring it alone does not satisfy the gate, because the replacement term may introduce a cross-row conflict (reuse or adjacent-bucket draw) that only a full table evaluation detects.

Phase 2 is complete when the characterization table shows all YES with no cross-bucket reuse.

---

#### PHASE 3 — FRAME FILL

Produce a frame fill record:

| Slot | Source Question | Verbatim Phase 2 Answer | Filled Value |
|------|----------------|------------------------|-------------|
| Q1 slot | Phase 2 Q1 | {verbatim} | {value used in frame} |
| Q2 slot | Phase 2 Q2 | {verbatim} | {value used in frame} |

Template: `"[Q1 current system] is the established approach; adoption cost is [Q2 migration cost]. Before adding complexity, prove [Q1 current system] cannot do this."`

**Completed frame:** [filled string using the table above]

Slot-binding verification: Q1 slot drawn from Q1 answer; Q2 slot drawn from Q2 answer. Any mismatch is a blocking error. A completed frame without the fill record does not satisfy the Phase 3 exit condition.

---

#### PHASE 4 — SCOPE PLAN

Before writing any role, produce the Scope Plan Table:

| Planned Role | Perspective Category | Scope |
|-------------|---------------------|-------|
| inertia-advocate | inertia | cross-team |
| {role} | {category} | team |
| {role} | {category} | org |
| … | … | … |

**Scope gate:** ≥ 2 distinct scope values must appear in this table before writing begins. If the table shows only one scope value, revise the plan now. Writing is blocked until the gate passes.

Distinct perspective categories required: ≥ 3 across the full planned set (product, technical, inertia, domain-specialist, etc.).

Confirm the gate passes before proceeding.

---

#### PHASE 5 — ROLE WRITING (Scope-Ordered)

Write roles in scope order within Phase 5: all `team`-scope roles first, then `cross-team`, then `org`.

For each role, write to `.roles/{area}/{role-name}.md`.

**Required fields in every role file:**

```yaml
name: {role-name}
orientation:
  frame: "{one-sentence lens}"
  verify:
    - "{question ending with ?}"
  simplify:
    - "{imperative action phrase}"
expertise:
  relevance: "{domain-specific; references at least one Phase 1 vocabulary term}"
  depth: {junior / mid / senior / principal}
scope: {team / cross-team / org}
collaborates_with:
  - {role-name}
```

**Inertia-advocate requirements (write in cross-team section):**
- `orientation.frame`: verbatim completed frame from Phase 3.
- `orientation.verify`: at least 2 questions reference Phase 2 dimensions (Q1 current system, Q2 migration cost, Q3 user habit).
- `expertise.relevance`: references at least one Phase 1 vocabulary term.

Minimum 3 roles total.

---

#### PHASE 6 — VERIFICATION GATE

Produce a single gate output. Every check must show PASS before delivery.

**Registry Summary Table (Check 1)**

| Role | Frame (excerpt, ≤15 words) | Scope | Collaborates With |
|------|-----------------------------|-------|-------------------|
| … | … | … | … |

**Orphan Reference Check (Check 2)**

| `collaborates_with` entry | Resolves to registry file? | PASS/FAIL |
|--------------------------|---------------------------|-----------|
| … | YES / NO | … |

Gate: any NO is a FAIL.

**Scope Gradient Check (Check 3)**

| Scope Value | Roles with this scope |
|-------------|----------------------|
| team | {list} |
| cross-team | {list} |
| org | {list} |

Distinct scope values present: {count}. Requirement: ≥ 2. PASS / FAIL.

**Vocabulary Coverage Check (Check 4)**

| Role | `expertise.relevance` vocabulary term referenced |
|------|------------------------------------------------|
| … | … |

Any role with no vocabulary reference: FAIL.

**Gate condition:** Check 1–4 all PASS. Deliver only after confirming this in the output.

---

---

### V-05

**Variation axis:** Lifecycle emphasis + Inertia framing (combined)
**Hypothesis:** Combining maximum phase-boundary enforcement with inertia-first role design produces a mutually reinforcing structure: the inertia-advocate's characterization populates the vocabulary that Phase 1 is required to extract, and the Frame Fill phase-boundary artifact enforces that every downstream role is written with an anchored status-quo reference, increasing simultaneous pass rates on C-10, C-12, C-16, C-19, C-22, C-23, C-24, C-25.

---

Generate a typed role registry for the specified domain.

Output path: `.roles/{area}/`
Each role file requires: `name`, `orientation` (frame / verify / simplify), `expertise` (relevance / depth), `scope`, `collaborates_with`.

**Architectural note:** This skill is organized around the inertia-advocate. The status quo is real, it has a name, it has a cost, and it has a user. Build it precisely before building anything else. Every other role in the registry exists in explicit relation to what the inertia-advocate names.

---

### PHASE 1 — DOMAIN VOCABULARY EXTRACTION

**Phase entry:** domain description or codebase context is available.

Read the input. Extract vocabulary into three named Q-domain buckets. Assign each term during extraction — not retroactively.

---

**BUCKET 1 — Current-System Terms**

Systems, tools, frameworks, or patterns currently deployed in this domain. Name them as they are named in the input.

| Term | Source in input |
|------|----------------|
| … | … |

---

**BUCKET 2 — Migration-Cost Terms**

Terms describing switching costs, integration burden, retraining overhead, compatibility gaps, or adoption friction.

| Term | Cost dimension |
|------|---------------|
| … | … |

---

**BUCKET 3 — User-Habit Terms**

Terms describing established workflows, learned behaviors, or usage patterns that exist independent of whether they are ideal.

| Term | Habit or behavior |
|------|------------------|
| … | … |

---

**Phase 1 exit condition:** all three buckets are present in the output, each containing ≥ 2 terms. No term appears in more than one bucket.

**Phase 2 does not begin until the Phase 1 exit condition is confirmed.**

---

### PHASE 2 — INERTIA CHARACTERIZATION

**Phase entry:** Phase 1 exit condition confirmed.

Answer three questions. Each answer uses a term drawn from its designated bucket.

**Q1 — Current System** *(Bucket 1 only):* What specific system, tool, or pattern does this domain depend on right now?

**Q2 — Migration Cost** *(Bucket 2 only):* What is the primary cost a team incurs when moving away from it?

**Q3 — User Habit** *(Bucket 3 only):* What established workflow or learned behavior would be disrupted?

Record answers, then immediately produce the Phase 2 Audit Table:

| Q | Answer | Term Used | Required Bucket | Match YES/NO |
|---|--------|-----------|-----------------|--------------|
| Q1 | {answer} | {term} | Bucket 1 (Current-System) | YES/NO |
| Q2 | {answer} | {term} | Bucket 2 (Migration-Cost) | YES/NO |
| Q3 | {answer} | {term} | Bucket 3 (User-Habit) | YES/NO |

**Phase 2 gate:** all three Match cells YES, evaluated simultaneously as a unit.

**If any cell shows NO:**

1. Identify the row with NO.
2. Replace the term in that answer with a term from the correct bucket.
3. **Restart the audit table from Q1.** Do not re-score only the replaced row. The replacement term may pass its own row while introducing a cross-row conflict — a synonym of a term used in another answer, or a term drawn from an adjacent bucket, that is invisible until the full table is re-evaluated. The gate condition requires all three rows to show YES simultaneously after full re-evaluation, not per-row incremental confirmation.
4. Repeat until the table shows all YES with no cross-bucket reuse across any row.

**Phase 2 exit artifact:** Q1/Q2/Q3 answers + completed audit table (all YES, full re-evaluation confirmed). The audit table is a structural output artifact — it is not an inline comment or a mental note. Phase 3 does not begin until the Phase 2 exit artifact is present in the output.

---

### PHASE 3 — INERTIA FRAME FILL

**Phase entry:** Phase 2 exit artifact present.

**Frame template:**

> `"[Q1 current system] is the established approach; adoption cost is [Q2 migration cost]. Before adding complexity, prove [Q1 current system] cannot do this."`

This phase produces the Frame Fill Record:

```
Q1 slot ← Phase 2 Q1: [verbatim Q1 answer, word for word]
Q2 slot ← Phase 2 Q2: [verbatim Q2 answer, word for word]

Completed frame: "[Q1 answer] is the established approach; adoption cost is [Q2 answer]. Before adding complexity, prove [Q1 answer] cannot do this."
```

**Slot-binding verification (blocking):**
- Q1 slot is populated from the Q1 answer — not Q2, not Q3.
- Q2 slot is populated from the Q2 answer — not Q1, not Q3.
- A swap in either slot binding is a structurally undetectable error in the frame string alone, because the completed frame reads as grammatically correct regardless of which answer fills which slot. The source citations are the only way to confirm correct binding before role writing begins.

A completed frame string without the slot-source citations does not satisfy the Phase 3 exit condition.

**Phase 3 exit artifact:** Frame Fill Record (citations + completed frame string + binding verification). Phase 4 does not begin until this artifact is present in the output.

---

### PHASE 4 — PRE-WRITE SCOPE PLAN

**Phase entry:** Phase 3 exit artifact present.

Plan the full role set. The inertia-advocate is pre-assigned as `cross-team`.

| Planned Role | Perspective Category | Scope |
|-------------|---------------------|-------|
| inertia-advocate | inertia | cross-team |
| {role} | {category} | team / cross-team / org |
| … | … | … |

**Phase 4 gate — Scope diversity:** ≥ 2 distinct scope values must appear in the plan before any role is written. If the plan shows only one scope value, revise 1–2 planned roles until the gate passes.

**Phase 4 gate — Perspective diversity:** ≥ 3 distinct perspective categories must appear in the plan (product, technical, inertia, domain-specialist, etc.).

Writing is blocked until both gate conditions pass. This is a prevention step. Post-write scope correction at the verification gate is not a substitute for this gate.

**Phase 4 exit artifact:** Scope Plan Table with both gate conditions confirmed. Phase 5 does not begin until this artifact is present.

---

### PHASE 5 — ROLE WRITING

**Phase entry:** Phase 4 exit artifact present.

Write each role to `.roles/{area}/{role-name}.md`.

**Write the inertia-advocate first.** Use the completed frame from Phase 3 verbatim in `orientation.frame`. Then write all other roles. Seeing the inertia-advocate's precise characterization before writing other roles ensures every subsequent role's framing is developed in relation to a grounded status-quo analysis, not in isolation.

**Required fields in every role file:**

```yaml
name: {role-name}
orientation:
  frame: "{one-sentence interpretive lens}"
  verify:
    - "{question — must end with ?}"
    - "{question — must end with ?}"
  simplify:
    - "{imperative action phrase}"
    - "{imperative action phrase}"
expertise:
  relevance: "{domain-specific; references at least one Phase 1 vocabulary term}"
  depth: {junior / mid / senior / principal}
scope: {team / cross-team / org}
collaborates_with:
  - {role-name-matching-registry}
```

**Inertia-advocate specific requirements:**
- `orientation.frame`: Phase 3 completed frame, verbatim.
- `orientation.verify`: ≥ 2 questions reference Phase 2 dimensions (Q1 current system, Q2 migration cost, Q3 user habit) by name.
- `expertise.relevance`: references ≥ 1 Phase 1 vocabulary term.
- `collaborates_with`: filled in after all roles are written; names must resolve.

Minimum 3 roles total.

---

### PHASE 6 — VERIFICATION GATE

**Phase entry:** all roles written.

This is a single named gate. All four checks must PASS before delivery. Any FAIL blocks the registry. Checks are not ordered by severity — all four must be confirmed.

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 12 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

Every written role must appear. Missing rows are a blocking error.

---

**CHECK 2 — Orphan Reference Check**

For every `collaborates_with` value in every role file: verify the name resolves to a file in `.roles/{area}/`.

| Reference | Resolves? |
|-----------|----------|
| {name} | YES / NO |

Any NO is a blocking error. Result: PASS / FAIL.

---

**CHECK 3 — Scope Gradient Check**

| Scope | Roles with this scope |
|-------|----------------------|
| team | … |
| cross-team | … |
| org | … |

Distinct scope values present in the registry: {count}. Required: ≥ 2.
If FAIL: identify roles to revise and revise them before rerunning.

Result: PASS / FAIL.

---

**CHECK 4 — Vocabulary Coverage Check**

For every role file, confirm `expertise.relevance` references ≥ 1 Phase 1 vocabulary term.

| Role | Vocabulary term referenced |
|------|---------------------------|
| … | … |

Any role without a vocabulary reference is a blocking error. Result: PASS / FAIL.

---

**Gate condition:** CHECK 1, CHECK 2, CHECK 3, CHECK 4 all PASS. Confirm gate status explicitly in the output. Deliver the registry only after this confirmation.

---
