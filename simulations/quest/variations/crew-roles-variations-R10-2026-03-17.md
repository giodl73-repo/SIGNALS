# crew-roles Variations V-01 through V-05 (Rubric v6)

---

## V-01

**Axis**: Lifecycle emphasis
**Hypothesis**: Naming every phase explicitly and requiring a named exit artifact at each boundary forces structural discipline that survives token pressure — skipped phases are visible as missing artifacts, not invisible omissions.

---

You are generating a typed role registry for a domain. Work through the phases below in strict sequence. Each phase produces a named output artifact. The next phase cannot begin until the artifact is complete and shown in output.

---

### PHASE 1 — BUCKETED VOCABULARY EXTRACTION

Read the input (product description, codebase context, or spec).

Extract domain vocabulary into three named buckets:

**Bucket A — Current-System Terms**: Terms that name the existing system, approach, or status quo (tools, patterns, processes currently in use).

**Bucket B — Migration-Cost Terms**: Terms that name what changing from the current system costs (effort, risk, breakage, learning curve, compatibility).

**Bucket C — User-Habit Terms**: Terms that name established user behaviors, muscle memory, or workflow patterns tied to the current system.

Each term belongs to exactly one bucket. Cross-bucket assignment is an error.

**Phase 1 exit artifact — VOCABULARY TABLE**: Three labeled lists with ≥2 terms per bucket. Every `expertise.relevance` field written in Phase 5 must reference at least one term from this table.

Phase 1 is **COMPLETE** when: three buckets exist, each has ≥2 terms, no term appears in two buckets.

---

### PHASE 2 — INERTIA Q&A WITH FULL-RESTART AUDIT

Answer three questions using only terms from the Phase 1 vocabulary. Each answer must draw from the bucket that aligns with its Q-dimension.

**Q1 — Current system**: What is the specific existing system, tool, or approach this domain is replacing or challenging? Answer must reference a Bucket A term.

**Q2 — Migration cost**: What is the primary cost of switching away from the current system? Answer must reference a Bucket B term.

**Q3 — User habit**: What established user behavior or workflow will be disrupted? Answer must reference a Bucket C term.

Immediately after writing Q1/Q2/Q3 answers, produce the **domain-alignment audit table**:

| Q | Term Used | Expected Bucket | Match YES/NO |
|---|-----------|-----------------|--------------|
| Q1 | | A | |
| Q2 | | B | |
| Q3 | | C | |

If any row shows NO: replace the term in that answer with one from the correct bucket. After any replacement, **restart evaluation from Q1** — re-evaluate all three rows simultaneously. Do not re-score only the replaced row; a replacement term may be a synonym already used in another answer, or drawn from an adjacent bucket, passing its own row while introducing a cross-row conflict invisible from a per-row re-score. The gate condition is "all three rows YES in a single full-pass evaluation," not "each row individually YES."

**Phase 2 exit artifact — INERTIA Q&A RECORD**: Q1/Q2/Q3 answers plus audit table showing YES/YES/YES after a full-pass evaluation with no cross-row reuse.

Phase 2 is **COMPLETE** when: INERTIA Q&A RECORD is present in output with all-YES audit table from a full-pass evaluation.

---

### PHASE 3 — FRAME FILL

The inertia-advocate `orientation.frame` uses this template:

> `[Q1: current system] resists replacement because [Q2: migration cost], and users rely on [Q3: user habit].`

Fill each slot from the Phase 2 answers verbatim. Produce:

1. **Completed frame string** (the filled template)
2. **Slot-source citations**:
   - `Q1 slot ← Phase 2 Q1: [verbatim Q1 answer]`
   - `Q2 slot ← Phase 2 Q2: [verbatim Q2 answer]`
   - `Q3 slot ← Phase 2 Q3: [verbatim Q3 answer]`
3. **Slot-binding verification**:
   - Q1 slot drawn from Q1 answer: YES/NO
   - Q2 slot drawn from Q2 answer: YES/NO

The completed frame string without source citations does not satisfy Phase 3 exit. If either binding check shows NO: identify which answer was placed in the wrong slot, correct the substitution, and re-verify. Phase 3 does not close until both binding checks show YES.

**Phase 3 exit artifact — FRAME FILL RECORD**: completed frame string, slot-source citations, slot-binding verification showing YES/YES.

Phase 3 is **COMPLETE** when: FRAME FILL RECORD is present in output with both binding checks YES.

---

### PHASE 4 — PRE-WRITE SCOPE AUDIT

Before writing any role files, plan the role set. For each planned role, assign a scope value.

| Planned Role | Perspective Category | Scope |
|--------------|---------------------|-------|

Constraints — all must be satisfied before Phase 5 begins:
- ≥3 roles including inertia-advocate
- ≥3 distinct perspective categories (inertia counts as one; product, technical, domain-specialist are others)
- ≥2 distinct scope values (`team`, `cross-team`, `org`)

If the plan has only one scope value: identify which roles to revise, update their scope, and re-verify the constraint. Writing is structurally blocked until the plan satisfies all three constraints.

**Phase 4 exit artifact — ROLE PLAN TABLE**: table showing ≥3 roles, ≥3 perspective categories, ≥2 scope values.

Phase 4 is **COMPLETE** when: ROLE PLAN TABLE satisfies all three constraints.

---

### PHASE 5 — ROLE WRITING

Write each role from the ROLE PLAN TABLE to `.roles/{area}/`. Required fields per role:

```yaml
name: ...
orientation:
  frame: ...
  verify:
    - "...?"     # must be a question
    - "...?"
  lens: "..."    # must be an imperative (not a question)
expertise:
  domain: ...
  relevance: "..."   # must reference ≥1 Phase 1 vocabulary term
collaborates_with:
  - ...              # names from ROLE PLAN TABLE only
scope: team | cross-team | org   # must match ROLE PLAN TABLE
```

**Inertia-advocate requirements**:
- `orientation.frame`: copy the completed frame string from the FRAME FILL RECORD verbatim. Do not paraphrase.
- `orientation.verify`: at least 2 questions must reference Q1 or Q2 dimensions from Phase 2.
- `expertise.relevance`: must reference a Bucket A term from the VOCABULARY TABLE.

**Phase 5 exit artifact**: all role files written with all required fields.

Phase 5 is **COMPLETE** when: all roles in the ROLE PLAN TABLE are written with complete fields.

---

### PHASE 6 — VERIFICATION GATE

Run all checks as a single named blocking gate. The gate does not PASS until every check shows PASS. Do not deliver output until gate verdict is PASS.

**CHECK 1 — REGISTRY SUMMARY TABLE**

| Role | Frame Excerpt (first 8 words) | Scope | Collaborates With |
|------|-------------------------------|-------|-------------------|

**CHECK 2 — ORPHAN-REFERENCE CHECK**
Every name in every `collaborates_with` list matches a Role name in the registry summary table.
- All match: PASS
- Any mismatch: FAIL (list unresolved names; correct and recheck)

**CHECK 3 — SCOPE-GRADIENT CHECK**
The registry summary table shows ≥2 distinct scope values.
- Confirmed: PASS
- Uniform: FAIL (identify roles to revise; correct and recheck)

**CHECK 4 — VOCABULARY COVERAGE CHECK**
Every `expertise.relevance` references at least one Phase 1 vocabulary term.
- All covered: PASS
- Any gap: FAIL (list roles without vocabulary reference; correct and recheck)

**CHECK 5 — SLOT-BINDING CHECK**
The inertia-advocate `orientation.frame` matches the FRAME FILL RECORD. Q1 slot traces to Phase 2 Q1 answer verbatim. Q2 slot traces to Phase 2 Q2 answer verbatim.
- All correct: PASS
- Any mismatch: FAIL (identify misbound slot; correct and recheck)

**GATE VERDICT**: PASS only when CHECK 1–5 all show PASS.

Phase 6 is **COMPLETE** when: GATE REPORT shows PASS on all five checks.

---

Deliver: FRAME FILL RECORD, ROLE PLAN TABLE, all role files, GATE REPORT. Do not deliver partial output.

---

## V-02

**Axis**: Inertia framing
**Hypothesis**: Anchoring the registry around the inertia-advocate — building it first and deriving all other roles in relation to what it challenges — forces domain specificity across the full role set, because no role can be written generically when the status-quo competitor is already named concretely.

---

You are generating a typed role registry. The inertia-advocate is the foundational role in every registry — it is built first, and the remaining roles are constructed in relation to what it challenges. Follow the steps below in order.

---

### STEP 1 — EXTRACT BUCKETED VOCABULARY

Read the input. Extract terms that name the domain's current state and the forces resisting change. Sort every term into exactly one of three buckets:

**Bucket A — Current-System Terms**: names the existing tool, system, or approach being displaced.
**Bucket B — Migration-Cost Terms**: names the cost of switching away (effort, risk, breakage, compatibility).
**Bucket C — User-Habit Terms**: names behaviors and muscle memory users currently have.

Minimum 2 terms per bucket. No cross-bucket placement.

Output: three labeled lists. This is the VOCABULARY TABLE for the registry.

---

### STEP 2 — CHARACTERIZE THE STATUS QUO

Before the inertia-advocate can be written, answer three questions that ground its framing in the specific domain. Each answer must draw a term from its aligned bucket.

| Q | Question | Required Bucket |
|---|----------|-----------------|
| Q1 | What is the specific current system or approach being displaced? | Bucket A |
| Q2 | What is the primary cost of switching away from it? | Bucket B |
| Q3 | What established user behavior will be disrupted? | Bucket C |

After writing all three answers, produce the **domain-alignment audit table**:

| Q | Term Used | Expected Bucket | Match YES/NO |
|---|-----------|-----------------|--------------|

If any row is NO: replace the term with one from the correct bucket. After any replacement, **restart the audit from Q1** — re-evaluate all three rows together in a single pass. A per-row re-score cannot detect cross-row reuse or adjacent-bucket substitution. The gate condition is all three rows YES in a single full-pass evaluation.

Step 2 is complete when: Q1/Q2/Q3 answers exist and the audit table shows YES/YES/YES from a full-pass evaluation with no cross-row reuse.

---

### STEP 3 — FILL THE INERTIA FRAME (WITH SOURCE CITATIONS)

The inertia-advocate `orientation.frame` is built from a template:

> `[Q1: current system] resists replacement because [Q2: migration cost], and users rely on [Q3: user habit].`

Fill the template using the Step 2 answers verbatim. Produce:

**Completed frame string**: `[Q1 answer] resists replacement because [Q2 answer], and users rely on [Q3 answer].`

**Slot-source citations** (required — frame string without these does not close this step):
```
Q1 slot ← Step 2 Q1: [verbatim Q1 answer]
Q2 slot ← Step 2 Q2: [verbatim Q2 answer]
Q3 slot ← Step 2 Q3: [verbatim Q3 answer]
```

**Slot-binding verification**:
- Q1 slot drawn from Q1 answer: YES/NO
- Q2 slot drawn from Q2 answer: YES/NO

If either binding check is NO: identify the misplaced answer, correct the slot, re-verify. Step 3 does not close until both checks are YES.

---

### STEP 4 — PLAN THE ROLE SET

Sketch the full registry before writing any files. The inertia-advocate is already established; plan the remaining roles in relation to what it challenges.

| Role Name | Perspective Category | Scope | Relationship to inertia-advocate |
|-----------|---------------------|-------|----------------------------------|
| inertia-advocate | inertia | | [anchor] |
| | | | |
| | | | |

Constraints — all must be met before writing begins:
- ≥3 roles total (inertia-advocate counts)
- ≥3 distinct perspective categories
- ≥2 distinct scope values (`team`, `cross-team`, `org`)

If the scope column contains only one value: revise 1–2 roles before continuing. Writing is blocked until all three constraints are satisfied.

---

### STEP 5 — WRITE THE INERTIA-ADVOCATE FIRST

Write the inertia-advocate to `.roles/{area}/`. Required fields:

```yaml
name: inertia-advocate
orientation:
  frame: "[use the Step 3 completed frame string verbatim]"
  verify:
    - "[question referencing Q1 dimension — what makes current system sticky?]?"
    - "[question referencing Q2 dimension — what is the real switching cost?]?"
    - "[question referencing Q3 dimension — what will users resist giving up?]?"
  lens: "[imperative: challenge the assumption that the new approach is superior]"
expertise:
  domain: "[domain name]"
  relevance: "[reference at least one Bucket A term from VOCABULARY TABLE]"
collaborates_with:
  - "[other role names from the plan]"
scope: "[from plan]"
```

`orientation.verify` items must be questions ending in `?`. `orientation.lens` must be an imperative, not a question.

---

### STEP 6 — WRITE REMAINING ROLES

For each remaining role in the plan, write to `.roles/{area}/`. Each role must:

- Contain all 5 required fields (`name`, `orientation`, `expertise`, `collaborates_with`, `scope`)
- Have `orientation.verify` items as questions (`?`) and `orientation.lens` as an imperative
- Reference at least one Phase 1 vocabulary term in `expertise.relevance`
- List `collaborates_with` using only names present in the Step 4 plan
- Be positioned relative to the inertia-advocate's challenge: what perspective does this role bring to bear on the problem the inertia-advocate names?

---

### STEP 7 — VERIFICATION GATE

All checks run as a single blocking gate. Do not deliver output until gate verdict is PASS.

**CHECK 1 — REGISTRY SUMMARY TABLE**

| Role | Frame Excerpt (first 8 words) | Scope | Collaborates With |
|------|-------------------------------|-------|-------------------|

Inertia-advocate appears first.

**CHECK 2 — ORPHAN-REFERENCE CHECK**
Every `collaborates_with` value maps to a Role name in the summary table.
- All map: PASS
- Any unresolved: FAIL (list names; fix and recheck)

**CHECK 3 — SCOPE-GRADIENT CHECK**
Table shows ≥2 distinct scope values.
- Confirmed: PASS
- Uniform: FAIL (revise and recheck)

**CHECK 4 — VOCABULARY COVERAGE CHECK**
Every `expertise.relevance` references a Step 1 vocabulary term.
- All covered: PASS
- Any gap: FAIL (list roles; fix and recheck)

**CHECK 5 — SLOT-BINDING CHECK**
Inertia-advocate frame matches Step 3 completed frame string. Q1 slot traces to Step 2 Q1 verbatim. Q2 slot traces to Step 2 Q2 verbatim.
- All correct: PASS
- Any mismatch: FAIL (identify misbound slot; fix and recheck)

Gate verdict: PASS only when all five checks show PASS.

---

Deliver: Step 3 FRAME FILL RECORD, Step 4 ROLE PLAN TABLE, role files (inertia-advocate first), GATE REPORT.

---

## V-03

**Axis**: Role sequence
**Hypothesis**: Deriving the role authoring sequence from the discovery outputs — vocabulary analysis drives which roles to write, and domain weighting determines order — prevents generic role templates from being filled in before the domain is understood.

---

You are generating a typed role registry. Roles are not written until vocabulary, Q&A, and scope planning are complete. The writing sequence is derived from what discovery reveals, not from a fixed template.

Execute in order. Each numbered step must complete before the next begins.

---

### 1. VOCABULARY EXTRACTION

Scan the input for domain-specific terms. Sort them into three named buckets:

- **Current-System Terms (Bucket A)**: names the existing tool, system, or approach
- **Migration-Cost Terms (Bucket B)**: names what switching costs
- **User-Habit Terms (Bucket C)**: names what users are currently accustomed to doing

Minimum 2 terms per bucket. No term in two buckets.

Output: three labeled lists. This is the VOCABULARY TABLE.

---

### 2. INERTIA Q&A WITH FULL-RESTART GATE

Answer Q1, Q2, Q3. Each answer uses a term from its required bucket.

- **Q1** — current system → Bucket A
- **Q2** — migration cost → Bucket B
- **Q3** — user habit → Bucket C

After writing all three answers, produce the audit table:

| Q | Term Used | Expected Bucket | Match YES/NO |
|---|-----------|-----------------|--------------|
| Q1 | | A | |
| Q2 | | B | |
| Q3 | | C | |

If any row shows NO: replace the term in that answer with a correct-bucket term. Then re-run the audit **from Q1** — evaluate all three rows together in a single pass, not only the replaced row. A replaced term may be drawn from an adjacent bucket or may already appear in another answer; a per-row re-score cannot detect these cross-row conflicts. Repeat until a full-pass evaluation shows YES/YES/YES with no reuse.

Proceed only when the complete audit table shows all-YES from a full-pass evaluation.

---

### 3. FRAME FILL

Fill the inertia template with Step 2 answers verbatim:

**Template**: `[Q1 answer] resists replacement because [Q2 answer], and users rely on [Q3 answer].`

Produce:

1. **Completed frame string** (filled template)
2. **Slot-source citations**:
   - `Q1 slot ← Step 2 Q1: [verbatim Q1 answer]`
   - `Q2 slot ← Step 2 Q2: [verbatim Q2 answer]`
   - `Q3 slot ← Step 2 Q3: [verbatim Q3 answer]`
3. **Slot-binding verification**:
   - Q1 slot drawn from Q1 answer: YES/NO
   - Q2 slot drawn from Q2 answer: YES/NO

The completed frame string without citations does not satisfy this step. If either binding check is NO: correct the misplaced slot and re-verify. Step 3 does not close until both checks are YES.

---

### 4. ROLE DISCOVERY AND SCOPE PLAN

Before writing files, enumerate the roles implied by the domain vocabulary. Ask: what expert perspectives does the vocabulary demand?

| # | Role Name | Perspective Category | Scope | Derived From |
|---|-----------|---------------------|-------|--------------|

**Derived From** column: note which vocabulary bucket or Q-dimension suggested this role.

Constraints — all must be satisfied before Step 5:
- ≥3 roles including inertia-advocate
- ≥3 distinct perspective categories
- ≥2 distinct scope values (`team`, `cross-team`, `org`)

If scope is uniform: revise 1–2 roles to restore gradient. Writing is blocked until plan satisfies all three constraints.

---

### 5. ROLE AUTHORING SEQUENCE

Write roles in this derived order:

1. **Inertia-advocate** — anchors all other roles; uses the Step 3 frame verbatim
2. **Highest vocabulary-density role** — the role whose domain touches the most Bucket A terms
3. **User-facing role** — the role most directly tied to the Q3 user-habit dimension
4. **Remaining roles** — in any order from the discovery plan

Write each role to `.roles/{area}/`. Required fields:

```yaml
name: ...
orientation:
  frame: "..."
  verify:
    - "...?"     # question ending in ?
    - "...?"
  lens: "..."    # imperative
expertise:
  domain: "..."
  relevance: "..."   # ≥1 term from VOCABULARY TABLE
collaborates_with:
  - "..."            # names from Step 4 plan only
scope: team | cross-team | org
```

**Inertia-advocate**: `orientation.frame` must be the Step 3 completed frame string verbatim. `orientation.verify` must include at least 2 questions referencing Q1 or Q2 dimensions. `expertise.relevance` must reference a Bucket A term.

---

### 6. VERIFICATION GATE

All checks run as a single named gate before any output is delivered.

**REGISTRY SUMMARY TABLE**

| Role | Frame Excerpt (first 8 words) | Scope | Collaborates With |
|------|-------------------------------|-------|-------------------|

**CHECK A — ORPHAN REFERENCES**
Every `collaborates_with` entry matches a name in the registry summary table.
- All match: PASS  |  Any miss: FAIL (list; fix and recheck)

**CHECK B — SCOPE GRADIENT**
Table shows ≥2 distinct scope values.
- Confirmed: PASS  |  Uniform: FAIL (revise and recheck)

**CHECK C — VOCABULARY COVERAGE**
Every `expertise.relevance` cites at least one Step 1 vocabulary term.
- All covered: PASS  |  Any gap: FAIL (list; fix and recheck)

**CHECK D — SLOT-BINDING**
Inertia-advocate frame matches Step 3 completed frame string. Q1 slot traces to Step 2 Q1 verbatim. Q2 slot traces to Step 2 Q2 verbatim.
- Correct: PASS  |  Mismatch: FAIL (identify; fix and recheck)

Gate verdict: PASS only when all four checks show PASS. Resolve FAILs before delivering.

---

Deliver: Step 3 FRAME FILL RECORD, Step 4 discovery plan, role files in authoring sequence, GATE REPORT.

---

## V-04

**Axis**: Phrasing register (conversational) + Output format (table-heavy)
**Hypothesis**: Surfacing structural requirements as explicit table shapes rather than prose conditions reduces the chance constraints are glossed over — an empty cell in a required table is a visible gap; a missed prose instruction is invisible.

---

You're building a typed role registry for a domain. Work through the six sections below in order. Each section asks you to fill in a specific table or record — don't move on until it's complete.

---

### Section 1: Build the vocabulary table

Read the input and pull out the terms that matter for this domain. Sort them into three buckets — you need at least 2 in each.

| Bucket | What goes here | Your terms |
|--------|----------------|------------|
| **A: Current-System** | The existing tool, system, or approach being displaced | |
| **B: Migration-Cost** | The cost of switching away (effort, risk, compatibility) | |
| **C: User-Habit** | What users currently do — behaviors, muscle memory, workflow | |

Each term goes in exactly one bucket. If a term fits two, pick the better one and note why.

---

### Section 2: Answer three questions

These three questions feed into the inertia-advocate role. Each answer needs to use a term from the right bucket.

**Write the answers here first:**

| Q | Question | Your answer | Bucket it must use |
|---|----------|-------------|-------------------|
| Q1 | What's the specific current system or approach being displaced? | | A: Current-System |
| Q2 | What's the main cost of switching away from it? | | B: Migration-Cost |
| Q3 | What user behavior or habit will be disrupted? | | C: User-Habit |

**Then run this check:**

| Q | Term you used | Bucket it should come from | Match? |
|---|---------------|---------------------------|--------|
| Q1 | | A | YES / NO |
| Q2 | | B | YES / NO |
| Q3 | | C | YES / NO |

If you've got any NO: replace the term in that answer and rerun the check table **from Q1** — go through all three rows again in a single pass, not just the row you changed. A replacement term might already appear in one of the other rows, or it might be from a neighboring bucket that passes its own row but breaks the set. You need all three YES in one pass before moving on.

---

### Section 3: Fill in the inertia frame

Use this template to build the inertia-advocate's orientation frame:

> `[Q1 answer] resists replacement because [Q2 answer], and users rely on [Q3 answer].`

**Fill it in:**

> `_____ resists replacement because _____, and users rely on _____.`

**Then write these three lines** (the frame is not complete without them):

```
Q1 slot ← Q1 answer: [paste Q1 answer verbatim]
Q2 slot ← Q2 answer: [paste Q2 answer verbatim]
Q3 slot ← Q3 answer: [paste Q3 answer verbatim]
```

**Slot check** (answer YES or NO):

| Slot | Drawn from correct answer? |
|------|---------------------------|
| Q1 slot | YES / NO |
| Q2 slot | YES / NO |

If either is NO: find the mix-up, fix the slot, recheck. Don't move on until both are YES.

---

### Section 4: Plan out your roles

Before writing any files, lay out the full role set here:

| # | Role name | Perspective category | Scope |
|---|-----------|---------------------|-------|
| 1 | inertia-advocate | inertia | |
| 2 | | | |
| 3 | | | |
| ... | | | |

**Check your plan against these constraints:**

| Constraint | Met? |
|------------|------|
| At least 3 roles total (inertia-advocate counts) | YES / NO |
| At least 3 different perspective categories | YES / NO |
| At least 2 different scope values in the Scope column | YES / NO |

If any constraint isn't met: fix the plan first. If the scope column is all the same value, adjust 1–2 roles. Writing is blocked until all three are YES.

---

### Section 5: Write the role files

Write each role to `.roles/{area}/`. Here's the format each file needs:

```yaml
name: ...
orientation:
  frame: "..."           # what this role is here to say
  verify:
    - "...?"             # must be a question
    - "...?"             # must be a question
  lens: "..."            # must be an imperative (do X, not should we X?)
expertise:
  domain: "..."
  relevance: "..."       # include at least one term from Section 1
collaborates_with:
  - "..."                # only names from your Section 4 plan
scope: team | cross-team | org   # must match your Section 4 plan
```

**For the inertia-advocate specifically:**
- `orientation.frame`: paste the Section 3 completed frame string word-for-word. Don't paraphrase.
- `orientation.verify`: at least 2 questions should push back on the Q1 or Q2 assumptions.
- `expertise.relevance`: use a Bucket A term from Section 1.

---

### Section 6: Run the verification checks

Don't deliver anything until all four checks pass.

**6A: Registry summary table** (build this first — you'll use it for the checks)

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|----------------------|-------|-------------------|

**6B: Four checks**

| Check | What to verify | PASS / FAIL |
|-------|----------------|-------------|
| Orphan references | Every name in every "Collaborates With" cell matches a Role in the table above | |
| Scope gradient | Table shows at least 2 different scope values | |
| Vocabulary coverage | Every "relevance" field names at least one Section 1 term | |
| Slot binding | Inertia frame Q1/Q2 slots match Q1/Q2 answers from Section 2 | |

If any check is FAIL: fix the problem, rerun that check. Deliver only when all four show PASS.

---

Deliver: Section 3 frame record, Section 4 role plan, role files, Section 6 summary table and checks.

---

## V-05

**Axis**: Lifecycle emphasis + C-24/C-25 synthesis
**Hypothesis**: Promoting C-24 (restart-from-Q1 after any NO) and C-25 (slot-source citations with binding verification) to explicit named phase-exit conditions — rather than inline reminders — closes both gaps by treating them as structural artifacts that block the phase boundary, making violations impossible to overlook rather than possible to omit under pressure.

---

You are generating a typed role registry for a domain. Execute the six phases below in strict sequence. Each phase has a named entry condition, a process, and a named exit artifact. The next phase cannot begin until its exit artifact is shown in output.

---

### PHASE 1 — VOCABULARY EXTRACTION
**Entry condition**: domain input (product description, spec, codebase context)
**Exit artifact**: VOCABULARY TABLE

Scan the input. Classify every relevant term into exactly one of three buckets:

| Bucket | Definition |
|--------|------------|
| **A: Current-System Terms** | Names the existing tool, system, or workflow pattern being displaced |
| **B: Migration-Cost Terms** | Names the cost of switching away (effort, risk, compatibility, breakage) |
| **C: User-Habit Terms** | Names established user behaviors or muscle memory tied to the current system |

Rules:
- Minimum 2 terms per bucket
- Each term belongs to exactly one bucket
- Cross-bucket assignment blocks Phase 1 exit

**VOCABULARY TABLE format**:
```
Bucket A — Current-System Terms: [term 1], [term 2], ...
Bucket B — Migration-Cost Terms: [term 1], [term 2], ...
Bucket C — User-Habit Terms:     [term 1], [term 2], ...
```

**PHASE 1 COMPLETE** when: VOCABULARY TABLE is present with three labeled buckets, ≥2 terms each, no cross-bucket duplicates.

---

### PHASE 2 — INERTIA Q&A WITH FULL-RESTART AUDIT
**Entry condition**: VOCABULARY TABLE from Phase 1
**Exit artifact**: INERTIA Q&A RECORD

Answer three questions. Each answer must use a term drawn from the specified bucket.

| Q | Question | Required Bucket |
|---|----------|-----------------|
| Q1 | What is the specific current system or approach being displaced? | Bucket A |
| Q2 | What is the primary cost of switching away from it? | Bucket B |
| Q3 | What established user behavior will be disrupted? | Bucket C |

Write the three answers, then immediately produce the **domain-alignment audit table**:

| Q | Term Used | Expected Bucket | Match YES/NO |
|---|-----------|-----------------|--------------|
| Q1 | | A | |
| Q2 | | B | |
| Q3 | | C | |

**If any row shows NO — FULL-RESTART PROTOCOL**:
1. Replace the term in the failing answer with a term from the correct bucket.
2. **Restart the audit from Q1.** Re-evaluate all three rows together in a single pass.
3. Do not re-score only the replaced row. A replaced term may be: (a) a synonym already present in another answer, creating cross-row reuse; (b) drawn from an adjacent bucket, passing its own row while violating the bucket constraint on a different row. Neither error is detectable from a per-row re-score.
4. Repeat the full-restart cycle until a single pass of Q1→Q2→Q3 shows YES on all three rows simultaneously with no cross-row reuse.

The gate condition is **all three rows YES in a single full-pass evaluation** — not "each row individually YES after its own correction."

**INERTIA Q&A RECORD format**:
```
Q1: [answer] (term: [term], bucket: A)
Q2: [answer] (term: [term], bucket: B)
Q3: [answer] (term: [term], bucket: C)

Audit table: [Q | Term | Expected Bucket | YES/NO]
Full-pass result: YES/YES/YES
```

**PHASE 2 COMPLETE** when: INERTIA Q&A RECORD is present with audit table showing YES/YES/YES from a documented full-pass evaluation.

---

### PHASE 3 — FRAME FILL WITH SLOT-SOURCE BINDING
**Entry condition**: INERTIA Q&A RECORD from Phase 2
**Exit artifact**: FRAME FILL RECORD

**Template**:
> `[Q1: current system] resists replacement because [Q2: migration cost], and users rely on [Q3: user habit].`

Substitute each slot with its Phase 2 answer verbatim. Then produce the FRAME FILL RECORD containing all three components:

**Component 1 — Completed frame string**:
> `[Q1 answer] resists replacement because [Q2 answer], and users rely on [Q3 answer].`

**Component 2 — Slot-source citations** (required; frame string without citations does not satisfy Phase 3 exit):
```
Q1 slot ← Phase 2 Q1: [verbatim Q1 answer]
Q2 slot ← Phase 2 Q2: [verbatim Q2 answer]
Q3 slot ← Phase 2 Q3: [verbatim Q3 answer]
```

**Component 3 — Slot-binding verification**:
```
Q1 slot drawn from Q1 answer: YES / NO
Q2 slot drawn from Q2 answer: YES / NO
```

If either binding check shows NO: identify which Phase 2 answer was placed in the wrong slot, correct the substitution, and re-verify. A completed frame string that uses Q2's answer in the Q1 slot is superficially correct but structurally wrong; it cannot be detected without this explicit binding check. Phase 3 does not close until both binding checks show YES.

**PHASE 3 COMPLETE** when: FRAME FILL RECORD contains all three components (frame string, citations, binding verification) with both binding checks showing YES.

---

### PHASE 4 — PRE-WRITE SCOPE AUDIT
**Entry condition**: VOCABULARY TABLE; INERTIA Q&A RECORD; FRAME FILL RECORD
**Exit artifact**: ROLE PLAN TABLE

Before writing any role files, enumerate the planned role set and assign scope values:

| # | Role Name | Perspective Category | Scope | Vocabulary Anchor |
|---|-----------|---------------------|-------|-------------------|

**Vocabulary Anchor column**: note at least one Phase 1 term that anchors this role's `expertise.relevance`.

**Constraints — all must be satisfied before Phase 5 begins**:

| Constraint | Required | Check |
|------------|----------|-------|
| Total roles | ≥3 (inertia-advocate counts) | |
| Distinct perspective categories | ≥3 | |
| Distinct scope values | ≥2 (`team` / `cross-team` / `org`) | |

If the scope column contains only one value: identify which 1–2 roles to revise, update their scope in the table, and re-verify the constraint. Role writing is structurally blocked until all three constraints show ✓.

**PHASE 4 COMPLETE** when: ROLE PLAN TABLE is present satisfying all three constraints.

---

### PHASE 5 — ROLE WRITING
**Entry condition**: ROLE PLAN TABLE; FRAME FILL RECORD; VOCABULARY TABLE
**Exit artifact**: role files at `.roles/{area}/`

Write each role from the ROLE PLAN TABLE. Required fields:

```yaml
name: ...
orientation:
  frame: "..."           # perspective statement
  verify:
    - "...?"             # must be a question (ends in ?)
    - "...?"
  lens: "..."            # must be an imperative (not a question)
expertise:
  domain: "..."
  relevance: "..."       # must reference ≥1 Phase 1 vocabulary term
collaborates_with:
  - "..."                # names from ROLE PLAN TABLE only; no placeholders
scope: team | cross-team | org   # must match ROLE PLAN TABLE
```

**Inertia-advocate requirements**:
- `orientation.frame`: copy the completed frame string from the FRAME FILL RECORD verbatim. Do not paraphrase or rephrase.
- `orientation.verify`: ≥2 questions referencing Q1 or Q2 dimensions from Phase 2
- `expertise.relevance`: must reference a Bucket A term from the VOCABULARY TABLE

**PHASE 5 COMPLETE** when: all roles in the ROLE PLAN TABLE are written with all required fields; inertia-advocate `orientation.frame` matches FRAME FILL RECORD verbatim.

---

### PHASE 6 — VERIFICATION GATE
**Entry condition**: all role files; ROLE PLAN TABLE; VOCABULARY TABLE; FRAME FILL RECORD
**Exit artifact**: GATE REPORT (all checks PASS)

All checks run as a single named blocking gate. The gate does not PASS until every check shows PASS. Do not deliver any output until gate verdict is PASS.

**CHECK 1 — REGISTRY SUMMARY TABLE** (produce this first; all other checks read from it)

| Role | Frame Excerpt (first 8 words) | Scope | Collaborates With |
|------|-------------------------------|-------|-------------------|

**CHECK 2 — ORPHAN-REFERENCE CHECK**
Every name in every `collaborates_with` list matches a Role name in the registry summary table.
- All match → PASS
- Any unresolved name → FAIL: list each unresolved name; correct the role file; recheck

**CHECK 3 — SCOPE-GRADIENT CHECK**
Registry summary table shows ≥2 distinct scope values.
- Confirmed → PASS
- Uniform scope → FAIL: identify which roles to revise; update; recheck

**CHECK 4 — VOCABULARY COVERAGE CHECK**
Every `expertise.relevance` references at least one Phase 1 vocabulary term from the VOCABULARY TABLE.
- All covered → PASS
- Any role without a vocabulary reference → FAIL: list the roles; add vocabulary reference; recheck

**CHECK 5 — SLOT-BINDING CHECK**
The inertia-advocate `orientation.frame` matches the FRAME FILL RECORD completed frame string character-for-character. Q1 slot in the frame traces to Phase 2 Q1 verbatim. Q2 slot in the frame traces to Phase 2 Q2 verbatim.
- All correct → PASS
- Frame text does not match FRAME FILL RECORD → FAIL
- Q1 slot bound to wrong Phase 2 answer → FAIL
- Q2 slot bound to wrong Phase 2 answer → FAIL
- For any FAIL: identify the specific mismatch; correct; recheck

**GATE VERDICT**:
```
CHECK 1 — REGISTRY SUMMARY TABLE: PASS / FAIL
CHECK 2 — ORPHAN-REFERENCE:       PASS / FAIL
CHECK 3 — SCOPE-GRADIENT:         PASS / FAIL
CHECK 4 — VOCABULARY COVERAGE:    PASS / FAIL
CHECK 5 — SLOT-BINDING:           PASS / FAIL

GATE: PASS (all checks PASS) / FAIL (list failing checks)
```

**PHASE 6 COMPLETE** when: GATE REPORT shows PASS on all five checks.

---

Deliver in this order:
1. FRAME FILL RECORD (Phase 3 exit artifact)
2. ROLE PLAN TABLE (Phase 4 exit artifact)
3. Role files (Phase 5 exit artifact)
4. GATE REPORT (Phase 6 exit artifact)

Do not deliver partial output. All four artifacts must be present.
