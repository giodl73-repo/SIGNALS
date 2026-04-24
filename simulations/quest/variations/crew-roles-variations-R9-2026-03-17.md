## crew-roles — Rubric v6 Variations (R9)

---

### V-01
**Variation axis:** Lifecycle emphasis — named phases with explicit ENTRY / EXIT / BLOCK conditions
**Hypothesis:** Forcing every phase boundary to produce a named structural artifact (vocabulary table, audit table, frame fill output, scope audit, verification gate) makes C-22, C-23, C-24, C-25 structurally unavoidable; phases cannot be skipped because each ENTRY condition references the prior EXIT artifact.

---

# crew-roles

Generate a typed role registry for a domain. Analyze the input to determine which expert perspectives are needed. Each role requires: `orientation` (frame, verify, simplify), `expertise` (description, relevance), `scope`, `collaborates_with`. The inertia-advocate is always included. Write all files to `.roles/{area}/`.

---

## PHASE 1 — VOCABULARY EXTRACTION

**Entry condition:** Domain input received.

Extract terms from the input. Place each term into one of three named buckets:

- **Bucket A — Current-System Terms:** Names for the existing tool, workflow, or approach being displaced.
- **Bucket B — Migration-Cost Terms:** Terms describing transition friction, risk, or breakage.
- **Bucket C — User-Habit Terms:** Terms describing established user behaviors or muscle memory being disrupted.

Produce this table:

| Term | Bucket |
|------|--------|
| [term] | A / B / C |

**Exit condition:** All three buckets contain at least one term.

**BLOCK:** Do not begin Phase 2 until the vocabulary table is complete with all three buckets populated.

---

## PHASE 2 — INERTIA PRE-CHARACTERIZATION

**Entry condition:** Phase 1 vocabulary table complete.

Answer three questions. Each answer must reference a term from its designated bucket:

- **Q1 — Current System (draw from Bucket A):** What specific system, tool, or approach do users currently rely on?
- **Q2 — Migration Cost (draw from Bucket B):** What is the primary friction or cost of transition?
- **Q3 — User Habit (draw from Bucket C):** What established behavior or workflow will be disrupted?

Write each answer as one sentence with the bucket term referenced explicitly.

After writing all three answers, produce the domain-alignment audit table:

| Q | Term Used | Expected Bucket | Match YES/NO |
|---|-----------|-----------------|--------------|
| Q1 | [term] | A (Current-System) | YES/NO |
| Q2 | [term] | B (Migration-Cost) | YES/NO |
| Q3 | [term] | C (User-Habit) | YES/NO |

**Re-evaluation protocol:** If any row shows NO, replace the term in that answer with a correct-bucket term. After any replacement, re-evaluate starting from Q1. Do not re-score only the replaced row. The gate condition is all three rows simultaneously YES in a single evaluation pass. Repeat until that condition is met.

**Exit condition:** Audit table shows YES / YES / YES evaluated as a unit in one pass. No cross-bucket reuse.

**BLOCK:** Do not begin Frame Fill until the audit table reaches all-YES in a single full pass.

---

## PHASE 3 — FRAME FILL

**Entry condition:** Phase 2 audit table complete with YES / YES / YES.

Populate the inertia frame template:

```
"Adopting this approach means abandoning [Q1: current system] — at a cost of [Q2: migration cost] — for users whose workflow depends on [Q3: user habit]."
```

Produce the Frame Fill output with the filled frame string and explicit slot citations:

```
Q1 slot ← Phase 2 Q1: [verbatim answer]
Q2 slot ← Phase 2 Q2: [verbatim answer]
Q3 slot ← Phase 2 Q3: [verbatim answer]
Filled frame: "..."
```

**Slot-source binding check:** Q1 slot populated from Q1 answer only; Q2 slot from Q2 answer only; Q3 slot from Q3 answer only. A cross-slot population (Q2 answer filling Q1 slot) is a blocking error. Replace and re-check before continuing.

**Exit condition:** Filled frame string produced, all three slot citations present, slot-binding check passed.

**BLOCK:** Do not write any role files until Frame Fill exit conditions are fully satisfied.

---

## PHASE 4 — PRE-WRITE SCOPE AUDIT

**Entry condition:** Frame Fill complete.

Before writing any role file, plan the full role set. Assign a scope value to each planned role:

| Planned Role | Scope |
|--------------|-------|
| inertia-advocate | [team / cross-team / org] |
| [role 2] | [scope] |
| [role 3] | [scope] |

Count distinct scope values. If all planned roles share one scope value, revise 1–2 planned roles to introduce a second distinct value.

**Exit condition:** Scope plan shows ≥ 2 distinct scope values.

**BLOCK:** Do not write any role file until scope diversity is confirmed in the plan.

---

## PHASE 5 — ROLE WRITING

**Entry condition:** Pre-write scope audit passed with ≥ 2 distinct scope values.

Write at least 3 role files. Each file must contain all 5 required fields:

```markdown
# [Role Name]

## orientation
**frame:** [perspective this role brings]
**verify:** [question ending with ?]
**simplify:** [imperative phrase]

## expertise
**description:** [domain expertise]
**relevance:** [domain-specific; must reference at least one Phase 1 vocabulary term]

## scope
[team / cross-team / org]

## collaborates_with
- [role-filename-without-extension]
```

**Inertia-advocate requirements:**
- `orientation.frame` must be the filled frame string from Phase 3.
- `orientation.verify` must pose questions that reference at least 2 of the 3 Q dimensions (current system, migration cost, user habit).
- `expertise.relevance` must name the specific current system or habit from Phase 2.

**Perspective diversity:** Roles must span at least 3 distinct categories (e.g., product, technical, inertia, domain-specialist). No category monopoly.

**Output path:** `.roles/{area}/` where `{area}` is derived from the input domain.

---

## PHASE 6 — VERIFICATION GATE

**Entry condition:** All role files written.

**GATE: CREW-ROLES VERIFICATION** — all three checks must pass simultaneously before delivery.

**Check 1 — Registry Summary Table:**

| Role | Frame (excerpt, 10 words) | Scope | Collaborates With |
|------|---------------------------|-------|-------------------|
| [name] | [excerpt] | [scope] | [names] |

For every `collaborates_with` value: confirm a matching file exists in the registry. Any unresolved reference blocks the gate.

**Check 2 — Scope Gradient:**

Count distinct scope values across all written roles. If fewer than 2 distinct values, revise 1–2 roles before re-running the gate.

**Check 3 — Vocabulary Coverage:**

For every `expertise.relevance` field: confirm it references at least one Phase 1 vocabulary term. Any role missing vocabulary coverage blocks the gate.

**Gate exit condition:** Check 1 PASS + Check 2 PASS + Check 3 PASS, evaluated simultaneously. Deliver only after all three pass.

---

## Delivery Confirmation

```
Output path: .roles/{area}/
Roles written: [N]
Scope values: [list]
Phase 1 vocabulary terms used: [list]
```

---

---

### V-02
**Variation axis:** Output format — every required artifact defined as a named table schema upfront; instructions are organized as "complete Schema S-N"
**Hypothesis:** Pre-defining all output schemas as named tables converts procedural steps into fill-in structures; omission becomes visible as an empty table cell rather than a skipped instruction, reducing silent non-compliance across C-11, C-13, C-21, C-22, C-25.

---

# crew-roles

Generate a typed role registry for a domain. Analyze the input to determine what expert perspectives are needed. Each role contains: `orientation` (frame, verify, simplify), `expertise` (description, relevance), `scope`, `collaborates_with`. The inertia-advocate is always included. Output: `.roles/{area}/`.

**All required output artifacts are defined below as named schemas. Complete each schema in order. An incomplete schema is a blocking error at the schema's gate.**

---

## Output Schema Registry

| Schema | Purpose | Gate |
|--------|---------|------|
| S-1 | Bucketed vocabulary | Phase 1 exit |
| S-2 | Inertia Q&A answers | Phase 2 input |
| S-3 | Domain-alignment audit table | Phase 2 exit |
| S-4 | Frame Fill output with slot citations | Phase 3 exit |
| S-5 | Pre-write scope plan | Phase 4 exit |
| S-6 | Role file set | Phase 5 output |
| S-7 | Registry summary table + gate results | Phase 6 exit |

---

## S-1 — Bucketed Vocabulary Table

Complete before any other schema.

From the input, extract terms into three named buckets. Every term belongs to exactly one bucket.

| Term | Bucket (A / B / C) |
|------|---------------------|
| | |

**Bucket definitions:**
- **A — Current-System:** The existing tool, workflow, or pattern being displaced.
- **B — Migration-Cost:** Friction, risk, or breakage in transition.
- **C — User-Habit:** Established behaviors or routines being disrupted.

**Gate S-1:** All three buckets (A, B, C) contain at least one term. Empty bucket → extract more terms before continuing.

---

## S-2 — Inertia Q&A Answers

Complete after S-1. Each answer references a term from its designated bucket.

| Q | Answer (1 sentence) | Bucket Term Used |
|---|---------------------|-----------------|
| Q1 — Current System (Bucket A) | | |
| Q2 — Migration Cost (Bucket B) | | |
| Q3 — User Habit (Bucket C) | | |

Write each answer before proceeding to S-3.

---

## S-3 — Domain-Alignment Audit Table

Complete after S-2. Produced at Phase 2 exit.

| Q | Term Used | Expected Bucket | Match YES/NO |
|---|-----------|-----------------|--------------|
| Q1 | | A (Current-System) | |
| Q2 | | B (Migration-Cost) | |
| Q3 | | C (User-Habit) | |

**Re-evaluation rule:** Any NO in column 4 triggers term replacement. After any replacement, re-fill S-3 starting from Q1 — not just the replaced row. Re-fill continues until all three rows simultaneously show YES in a single pass through the table.

**Gate S-3:** All three rows YES in a single evaluation pass. Cross-bucket reuse fails this gate.

---

## S-4 — Frame Fill Output

Complete after S-3 gate passes. Use the filled template:

```
"Adopting this approach means abandoning [Q1: current system] — at a cost of [Q2: migration cost] — for users whose workflow depends on [Q3: user habit]."
```

Populate S-4:

| Slot | Source (Q#) | Verbatim Phase 2 Answer | Filled Slot Text |
|------|-------------|------------------------|-----------------|
| Q1 (current system) | Q1 | | |
| Q2 (migration cost) | Q2 | | |
| Q3 (user habit) | Q3 | | |

**Completed frame string:**
```
[Full filled frame text]
```

**Slot-binding check:** Q1 slot populated from Q1 answer; Q2 from Q2; Q3 from Q3. Cross-slot population is a blocking error — correct and re-check.

**Gate S-4:** All slot citations present; completed frame string produced; slot-binding check passed.

---

## S-5 — Pre-Write Scope Plan

Complete after S-4 gate. Before writing any role file, plan the full role set with scope values assigned.

| Planned Role | Category | Scope |
|--------------|----------|-------|
| inertia-advocate | inertia | |
| [role 2] | [category] | |
| [role 3] | [category] | |

**Gate S-5:** At least 2 distinct scope values appear in column 3; at least 3 distinct categories in column 2. If scope is homogeneous, revise planned roles before writing.

---

## S-6 — Role Files

Write role files only after S-5 gate passes. Each file to `.roles/{area}/`. Minimum 3 roles.

Each file schema:

```markdown
# [Role Name]

## orientation
**frame:** [perspective]
**verify:** [question?]
**simplify:** [imperative]

## expertise
**description:** [expertise]
**relevance:** [references ≥1 S-1 vocabulary term]

## scope
[team / cross-team / org]

## collaborates_with
- [filename]
```

**Inertia-advocate specifics:** `orientation.frame` = filled frame string from S-4. `orientation.verify` questions reference ≥ 2 of Q1/Q2/Q3 dimensions. `expertise.relevance` names the specific current system from Q1.

---

## S-7 — Registry Summary Table + Gate Results

After all role files written, complete S-7 as the delivery gate.

**Registry Summary:**

| Role | Frame (first 10 words) | Scope | Collaborates With |
|------|------------------------|-------|-------------------|
| | | | |

**Gate checks — all three must show PASS:**

| Check | Description | Result |
|-------|-------------|--------|
| Orphan check | Every collaborates_with value matches a file in this table | PASS / FAIL |
| Scope gradient | ≥ 2 distinct scope values present | PASS / FAIL |
| Vocabulary coverage | Every expertise.relevance references ≥ 1 S-1 term | PASS / FAIL |

Any FAIL in S-7 blocks delivery. Resolve the failing check, re-run only the affected rows, then re-confirm all three simultaneously.

**Delivery:** Only after S-7 shows three PASSes simultaneously.

---

---

### V-03
**Variation axis:** Inertia framing — the inertia-advocate is the anchor; the skill is organized as "map the displacement first, build the constellation of witnesses around it"
**Hypothesis:** Leading with inertia computation forces Q1/Q2/Q3 answers to be grounded in real domain specifics before any vocabulary extraction occurs; the extraction in Phase 1 becomes purposeful (supporting the characterization already in progress) rather than speculative; improves C-10, C-12, C-16, C-19, C-20, C-21.

---

# crew-roles

Every change displaces something. Before you can write an honest role registry, you need to know what is being displaced, who depends on it, and what it will cost them. Start there. The inertia-advocate speaks for that cost. The other roles exist in relation to it.

Output: `.roles/{area}/` with at least 3 role files. Each role requires: `orientation` (frame, verify, simplify), `expertise` (description, relevance), `scope`, `collaborates_with`.

---

## Step 1 — Read the displacement landscape

Read the input. Do not extract a vocabulary list yet. Instead, answer this before anything else:

> *What is currently in place, and what does it cost users to move away from it?*

Identify three things from the input:

1. **The current system or approach** — what users have now that this displaces.
2. **The cost of transition** — friction, breakage, or migration burden users will bear.
3. **The habit being disrupted** — the workflow or behavior users will need to change.

Write these down as three raw observations. These are your Q1, Q2, Q3 seed answers. They do not need to be final — you will refine them in Step 2.

---

## Step 2 — Extract bucketed vocabulary from the input

Now extract domain vocabulary from the input. Assign each term to the bucket it belongs to:

- **Bucket A — Current-System Terms:** Vocabulary naming what exists today.
- **Bucket B — Migration-Cost Terms:** Vocabulary naming friction, risk, or transition burden.
- **Bucket C — User-Habit Terms:** Vocabulary naming established behaviors or routines.

| Term | Bucket |
|------|--------|
| [term] | A / B / C |

All three buckets must be non-empty before continuing.

---

## Step 3 — Refine Q1/Q2/Q3 against vocabulary buckets

Revisit your Step 1 raw observations. Refine each into one sentence that explicitly uses a term from its designated bucket:

- **Q1 (Current System):** References a Bucket A term.
- **Q2 (Migration Cost):** References a Bucket B term.
- **Q3 (User Habit):** References a Bucket C term.

After refining, run the domain-alignment audit:

| Q | Term Used | Expected Bucket | Match YES/NO |
|---|-----------|-----------------|--------------|
| Q1 | [term] | A (Current-System) | YES/NO |
| Q2 | [term] | B (Migration-Cost) | YES/NO |
| Q3 | [term] | C (User-Habit) | YES/NO |

If any row is NO: replace the term with a term from the correct bucket and re-run the audit table from Q1. Re-evaluation always restarts from row 1 — never from the replaced row alone. Continue until all three rows simultaneously show YES in a single pass.

All three rows YES in one pass is required before continuing.

---

## Step 4 — Fill the inertia frame

The inertia-advocate's orientation frame is a template with three named slots:

```
"Adopting this approach means abandoning [Q1: current system] — at a cost of [Q2: migration cost] — for users whose workflow depends on [Q3: user habit]."
```

Fill it now. Show your work:

```
Q1 slot ← Q1 answer: [verbatim]
Q2 slot ← Q2 answer: [verbatim]
Q3 slot ← Q3 answer: [verbatim]

Filled frame: "..."
```

Confirm: Q1 slot drawn from Q1 answer, Q2 slot from Q2 answer, Q3 slot from Q3 answer. Cross-slot population is an error — replace and re-confirm before continuing. The filled frame with explicit slot citations is the output of this step.

---

## Step 5 — Design the inertia-advocate role

Write the inertia-advocate role file before any other role. The inertia-advocate is the center of gravity for the registry.

**Requirements:**
- `orientation.frame` = the filled frame string from Step 4.
- `orientation.verify` = two questions that together reference at least 2 of the 3 Q dimensions (current system, migration cost, user habit). Each ends with `?`.
- `orientation.simplify` = one imperative: what to pare away to make migration viable.
- `expertise.relevance` = names the specific current system from Q1 and at least one Step 2 vocabulary term.
- `scope` = value from `{team, cross-team, org}`.
- `collaborates_with` = at least one other role (to be resolved after the full registry is written).

Write the file to `.roles/{area}/inertia-advocate.md`.

---

## Step 6 — Design the supporting constellation

Now design the other roles. Each exists in relation to what the inertia-advocate identified. You need at least 2 more roles for a minimum registry of 3.

**Constellation design questions:**
- Who evaluates whether the transition cost is worth it? (product or business perspective)
- Who ensures the technical implementation actually reduces the migration burden? (engineering perspective)
- Who speaks for the users whose habits are being disrupted? (UX or domain-specialist perspective)

Pick at least 2 from this space. You may add more.

**For each role:**
- `orientation.frame` = the perspective this role brings relative to the displacement.
- `orientation.verify` = question(s) ending with `?` probing the role's specific concern.
- `orientation.simplify` = imperative reducing unnecessary complexity in the role's domain.
- `expertise.relevance` = domain-specific; references at least one Step 2 vocabulary term.
- `scope` = value from `{team, cross-team, org}`.
- `collaborates_with` = at least one other role.

**Scope rule:** The full role set must span at least 2 distinct scope values. Before writing the first supporting role, check the planned scope values: if inertia-advocate and all planned roles share one scope value, revise the plan to introduce a second value.

**Perspective rule:** Roles must span at least 3 distinct perspective categories. No category monopoly.

Write files to `.roles/{area}/`.

---

## Step 7 — Verification gate

After all roles are written, run the CREW-ROLES VERIFICATION gate. All three checks must pass simultaneously:

**Registry summary table:**

| Role | Frame (first 10 words) | Scope | Collaborates With |
|------|------------------------|-------|-------------------|
| inertia-advocate | | | |
| [other roles] | | | |

**Check 1 — Orphan references:** Every `collaborates_with` value matches a role name in the table. Any unresolved reference: fix before delivering.

**Check 2 — Scope gradient:** Count distinct scope values. Fewer than 2 → revise 1–2 roles, re-run gate.

**Check 3 — Vocabulary coverage:** Every `expertise.relevance` references at least one Step 2 vocabulary term. Any gap → revise and re-run gate.

Do not deliver until all three checks pass simultaneously.

---

---

### V-04
**Variation axis:** Lifecycle emphasis + Output format combined — named phases with BLOCK conditions, every phase exit requires a completed table schema
**Hypothesis:** Phase gates prevent advancement; pre-defined table schemas prevent omission within each phase; the combination closes both failure modes simultaneously, producing the highest structural compliance across all 25 criteria with minimal instruction ambiguity.

---

# crew-roles

Generate a typed role registry for a domain. Each role requires: `orientation` (frame, verify, simplify), `expertise` (description, relevance), `scope`, `collaborates_with`. Inertia-advocate always included. Output path: `.roles/{area}/`.

Execute phases in order. Each phase produces a named table. Each phase has a BLOCK — the next phase cannot begin until the current phase's table is complete and its gate condition is satisfied.

---

## PHASE 1 — VOCABULARY EXTRACTION
**Produces: T-VOCAB**

Extract domain terms from the input. Assign each to one of three named buckets.

**T-VOCAB:**

| Term | Bucket (A=Current-System / B=Migration-Cost / C=User-Habit) |
|------|--------------------------------------------------------------|
| [term] | |

**BLOCK 1:** T-VOCAB must have at least one row in each bucket value. Do not begin Phase 2 until T-VOCAB is complete with A, B, and C all represented.

---

## PHASE 2 — INERTIA PRE-CHARACTERIZATION
**Produces: T-QA + T-AUDIT**

**Step 2a — Write Q&A answers (T-QA):**

Draw one term per answer from the designated bucket:

**T-QA:**

| Q | Answer (1 sentence) | Term from Bucket |
|---|---------------------|-----------------|
| Q1 — Current System | | A |
| Q2 — Migration Cost | | B |
| Q3 — User Habit | | C |

**Step 2b — Domain-alignment audit (T-AUDIT):**

| Q | Term Used | Expected Bucket | Match YES/NO |
|---|-----------|-----------------|--------------|
| Q1 | | A | |
| Q2 | | B | |
| Q3 | | C | |

**Re-evaluation rule:** Any NO row in T-AUDIT triggers full restart. Replace the term in the NO answer, then re-fill T-AUDIT starting from Q1. Continue until all three rows simultaneously show YES in a single pass through T-AUDIT.

**BLOCK 2:** T-AUDIT must show YES / YES / YES evaluated as a unit in one pass. An all-YES result achieved row-by-row across multiple passes does not satisfy this gate. Do not begin Phase 3 until a single-pass all-YES result is produced.

---

## PHASE 3 — FRAME FILL
**Produces: T-FRAME**

Fill the inertia frame template. Each slot must cite its Phase 2 source verbatim.

**Frame template:**
```
"Adopting this means abandoning [Q1: current system] — at a cost of [Q2: migration cost] — for users whose workflow depends on [Q3: user habit]."
```

**T-FRAME:**

| Slot | Source Q | Verbatim Phase 2 Answer | Filled Slot Text |
|------|----------|------------------------|-----------------|
| Q1 (current system) | Q1 | | |
| Q2 (migration cost) | Q2 | | |
| Q3 (user habit) | Q3 | | |

**Completed frame string:** `"[full filled text]"`

**Slot-binding check:** Column 2 (Source Q) must match the slot. Q1 slot ← Q1 answer only; Q2 slot ← Q2 answer only; Q3 slot ← Q3 answer only. A cross-slot entry in any row is a blocking error: correct and re-confirm.

**BLOCK 3:** T-FRAME complete with all slot citations present; completed frame string produced; slot-binding check passed. Do not write any role file until BLOCK 3 is cleared.

---

## PHASE 4 — PRE-WRITE SCOPE AUDIT
**Produces: T-SCOPE-PLAN**

Before writing any role, plan the full role set and assign scope values.

**T-SCOPE-PLAN:**

| Planned Role | Perspective Category | Scope |
|--------------|---------------------|-------|
| inertia-advocate | inertia | |
| | | |
| | | |

**BLOCK 4:** T-SCOPE-PLAN must show ≥ 2 distinct scope values in column 3 and ≥ 3 distinct perspective categories in column 2. If scope is homogeneous, revise roles in the plan before writing. Do not write any role file until T-SCOPE-PLAN satisfies both conditions.

---

## PHASE 5 — ROLE WRITING

Write role files only after BLOCK 4 is cleared. All files to `.roles/{area}/`. Minimum 3 roles.

**Role file format:**

```markdown
# [Role Name]

## orientation
**frame:** [perspective]
**verify:** [question?]
**simplify:** [imperative]

## expertise
**description:** [expertise description]
**relevance:** [must reference ≥1 T-VOCAB term]

## scope
[team / cross-team / org]

## collaborates_with
- [filename]
```

**Inertia-advocate requirements:**
- `orientation.frame` = completed frame string from T-FRAME.
- `orientation.verify` = references ≥ 2 of Q1/Q2/Q3 dimensions.
- `expertise.relevance` = names the specific current system from Q1.

---

## PHASE 6 — VERIFICATION GATE
**Produces: T-REGISTRY + T-GATE**

**T-REGISTRY:**

| Role | Frame (first 10 words) | Scope | Collaborates With |
|------|------------------------|-------|-------------------|
| | | | |

**T-GATE:**

| Check | Description | PASS / FAIL |
|-------|-------------|-------------|
| Orphan check | All collaborates_with values resolve to rows in T-REGISTRY | |
| Scope gradient | ≥ 2 distinct scope values in T-REGISTRY | |
| Vocabulary coverage | Every expertise.relevance references ≥ 1 T-VOCAB term | |

**BLOCK 6:** T-GATE must show PASS / PASS / PASS simultaneously. Any FAIL: resolve the issue, update the affected role file, and re-run the full T-GATE (not just the failing row). Deliver only after a single pass of T-GATE shows all three PASSes.

---

---

### V-05
**Variation axis:** Inertia framing + Lifecycle emphasis combined, with C-24 re-evaluation restart and C-25 slot-source citations embedded as named first-class subsections
**Hypothesis:** Combining inertia-first orientation with rigid phase structure and explicitly naming the two new v6 mechanisms (RE-EVALUATION RESTART PROTOCOL and SLOT-SOURCE BINDING CITATIONS) as dedicated subsections — rather than burying them in gate prose — produces the highest probability of C-24 and C-25 compliance because each mechanism is independently labeled and verifiable.

---

# crew-roles

A role registry is a map of who cares about what, and why the current approach isn't enough. Before you can write that map honestly, you need to know what is being displaced.

Start with the displacement. Characterize it precisely. Then build the registry around it.

Output: `.roles/{area}/`. Required fields per role: `orientation` (frame, verify, simplify), `expertise` (description, relevance), `scope`, `collaborates_with`. Inertia-advocate always included.

---

## PHASE 1 — DISPLACEMENT VOCABULARY

The vocabulary you extract here powers every phase that follows. Organize it by domain from the start.

From the input, extract terms into three named buckets:

| Term | Bucket |
|------|--------|
| [term] | A (Current-System) / B (Migration-Cost) / C (User-Habit) |

**Bucket definitions:**
- **A — Current-System:** What exists now that will be displaced.
- **B — Migration-Cost:** The friction and cost of transition.
- **C — User-Habit:** The behaviors and routines users will need to change.

**Phase 1 exit:** All three buckets non-empty. Incomplete buckets block Phase 2.

---

## PHASE 2 — INERTIA CHARACTERIZATION

Characterize the displacement in three answers. This is the factual foundation for the inertia-advocate role.

**Answers:**

- **Q1 — Current System:** What is the specific system or approach users rely on today? *(Use a Bucket A term.)*
- **Q2 — Migration Cost:** What is the primary cost or friction of transition? *(Use a Bucket B term.)*
- **Q3 — User Habit:** What established behavior will be disrupted? *(Use a Bucket C term.)*

Write each answer as one sentence, with the bucket term named explicitly.

---

### DOMAIN-ALIGNMENT AUDIT TABLE

After writing all three answers, produce:

| Q | Term Used | Expected Bucket | Match YES/NO |
|---|-----------|-----------------|--------------|
| Q1 | [term] | A (Current-System) | |
| Q2 | [term] | B (Migration-Cost) | |
| Q3 | [term] | C (User-Habit) | |

---

### RE-EVALUATION RESTART PROTOCOL *(C-24)*

If any row shows NO:

1. Replace the term in the NO answer with a term from the correct bucket.
2. **Restart evaluation from Q1.** Do not re-evaluate only the replaced row.
3. Rebuild the full audit table from Q1 through Q3 with all revised answers.
4. The gate condition is: **all three rows simultaneously YES in a single evaluation pass through the rebuilt table.**
5. Continue until that condition is met in one pass.

Rationale: Re-scoring only the replaced row can introduce a cross-row conflict (a replacement term that is a synonym of the term used in another answer, or drawn from the adjacent bucket) that is invisible from the replaced row alone. Only a full-table pass detects it.

**Phase 2 exit:** Audit table shows YES / YES / YES in a single full evaluation pass, with no cross-bucket reuse.

---

## PHASE 3 — FRAME FILL

The inertia-advocate's orientation frame is a template with named Q-slots. Populate it now, before writing any role.

**Frame template:**

```
"Adopting this approach means abandoning [Q1: current system] — at a cost of [Q2: migration cost] — for users whose workflow depends on [Q3: user habit]."
```

---

### SLOT-SOURCE BINDING CITATIONS *(C-25)*

For each slot, record its verbatim source:

```
Q1 slot ← Phase 2 Q1: [verbatim answer]
Q2 slot ← Phase 2 Q2: [verbatim answer]
Q3 slot ← Phase 2 Q3: [verbatim answer]

Filled frame: "..."
```

**Slot-binding verification:** 

| Slot | Populated From | Correct? |
|------|---------------|----------|
| Q1 (current system) | Q1 answer | YES/NO |
| Q2 (migration cost) | Q2 answer | YES/NO |
| Q3 (user habit) | Q3 answer | YES/NO |

Any NO in the slot-binding table is a blocking error. Replace the incorrectly-sourced slot, update the citations, and re-verify before continuing.

**Phase 3 exit:** Filled frame string produced; all three slot citations present; slot-binding table shows YES / YES / YES. The completed frame string without citations does not satisfy Phase 3 exit.

**BLOCK:** No role file is written until Phase 3 exit conditions are fully satisfied.

---

## PHASE 4 — SCOPE PLAN

Before writing roles, plan the full set with scope values assigned.

| Planned Role | Perspective Category | Scope |
|--------------|---------------------|-------|
| inertia-advocate | inertia | |
| | | |
| | | |

**Scope gate:** At least 2 distinct scope values in column 3; at least 3 distinct perspective categories in column 2. If scope is homogeneous, revise the plan to introduce diversity. Writing is blocked until the plan satisfies both conditions.

---

## PHASE 5 — ROLE WRITING

Write role files only after Phase 4 scope plan is approved. All files to `.roles/{area}/`. Minimum 3 roles.

```markdown
# [Role Name]

## orientation
**frame:** [perspective]
**verify:** [question?]
**simplify:** [imperative]

## expertise
**description:** [expertise]
**relevance:** [references ≥1 Phase 1 vocabulary term]

## scope
[team / cross-team / org]

## collaborates_with
- [filename]
```

**Inertia-advocate:**
- `orientation.frame` = filled frame string from Phase 3 (verbatim, not paraphrased).
- `orientation.verify` = questions referencing ≥ 2 of the Q1/Q2/Q3 dimensions. Each ends with `?`.
- `orientation.simplify` = imperative focused on reducing migration friction.
- `expertise.relevance` = names the specific current system from Q1, plus ≥ 1 Phase 1 vocabulary term.

**Supporting roles:** Each `expertise.relevance` references ≥ 1 Phase 1 vocabulary term. Together, all roles span ≥ 3 distinct perspective categories.

---

## PHASE 6 — VERIFICATION GATE

**GATE: CREW-ROLES VERIFICATION** — runs after all roles are written.

**Registry summary table:**

| Role | Frame (first 10 words) | Scope | Collaborates With |
|------|------------------------|-------|-------------------|
| inertia-advocate | | | |
| [others] | | | |

**Gate checks (all three must pass simultaneously):**

| # | Check | PASS / FAIL |
|---|-------|-------------|
| 1 | Orphan check — every `collaborates_with` resolves to a name in the registry table | |
| 2 | Scope gradient — ≥ 2 distinct scope values present | |
| 3 | Vocabulary coverage — every `expertise.relevance` references ≥ 1 Phase 1 vocabulary term | |

If any check fails: resolve the issue, revise the affected role file, and re-run the full gate. Do not re-run only the failing check. Deliver only after a single gate pass shows three simultaneous PASSes.

---

## Delivery

```
Output path:  .roles/{area}/
Roles:        [N] files written
Scopes:       [distinct values]
Vocabulary:   [Phase 1 terms used in expertise.relevance fields]
Frame fill:   [Q1 / Q2 / Q3 slot sources confirmed]
```

---
