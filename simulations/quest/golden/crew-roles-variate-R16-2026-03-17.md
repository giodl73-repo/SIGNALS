---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 16
rubric: crew-roles-rubric-v10-2026-03-17.md
---

# crew-roles -- Variate R16

5 complete prompt body variations for the `crew-roles` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

**Baseline**: R15 V-05 all-three-combined. The R15 all-combined baseline contains all six
prior mechanisms: C-30 (inertia-first gate), C-31 (vocab binding column in Phase 5), C-32
(inline LENS AUDIT after each written role), C-33 (PERSPECTIVE AUDIT gate before Phase 6
+ CHECK 8 from written files), C-34 (per-slot `Phase 1 source: {row-id} = "{verbatim
phrase}"` in FRAME FILL + CHECK 5A/5B split), C-35 (ROLE-REPLACE sub-procedure with 4
fields + CONFIRMED gate). v10 rubric has 27 aspirational criteria; baseline scores 27/27
in static analysis. R16 tests stylistic and structural axes to harden those mechanisms
against real-execution drift.

**Gaps to probe in R16**: The v10 rubric is structurally complete. The R16 hypothesis space
shifts from "what mechanism is missing?" to "which presentation axis makes mechanisms more
likely to survive real execution without collapsing to prose summaries?":

- **Axis-A -- Lifecycle emphasis**: Verbose explicit phase boundaries vs. compressed inline
  instructions. Hypothesis: maximum header scaffolding prevents LLM from blurring Phase 4
  FRAME FILL into Phase 6 writing.
- **Axis-B -- Phrasing register**: Imperative/technical (CAPS gate names) vs.
  conversational/descriptive (plain English procedural). Hypothesis: conversational register
  may reduce robotic compliance artifacts while preserving gate logic.
- **Axis-C -- Inertia framing**: Inertia-advocate as first-among-equals vs.
  inertia-as-benchmark (all other roles define themselves by contrast to inertia).
  Hypothesis: benchmark framing produces richer domain-grounded inertia content (C-10) and
  stronger collaborates_with chains.

**Single-axis**: V-01 (Axis-A verbose), V-02 (Axis-B conversational), V-03 (Axis-C
inertia-benchmark). **Two-axis combos**: V-04 (Axis-A + Axis-C), V-05 (Axis-A + Axis-B
+ Axis-C full integration).

---

## V-01

**Variation axis**: Lifecycle emphasis — VERBOSE (maximum phase explicitness)
**Hypothesis**: Naming every phase as a numbered H3 section with explicit ENTER/EXIT
labels and indented gate blocks prevents phase-boundary collapse during execution. When
an LLM sees "## PHASE 4 — FRAME FILL" followed by "## EXIT GATE: FRAME FILL COMPLETE"
it is less likely to compress FRAME FILL into CONVERGENCE SUMMARY prose. All six v10
mechanisms are preserved; the test is whether verbose scaffolding produces cleaner
per-phase artifacts.

```
Generate a typed role registry for a domain. Read the codebase, spec, or context named
in `for:`. Produce one markdown file per role at `.roles/{domain}/`. Inertia-advocate
is always included. Each role file must contain exactly five fields: name, orientation,
lens, expertise, scope, collaborates_with.

---

### PHASE 1 — INPUT INVENTORY

Glob and Read all files in the current directory relevant to the domain. List each input as:

  Row-ID | Source file | Relevant excerpt (≤ 20 words)

Label this table INPUT INVENTORY. Minimum 5 rows. If fewer than 5 relevant files exist,
include repo-level context (README, config, CLAUDE.md). Do not skip this table -- it is
the source-of-record for Phase 4 source citations.

EXIT GATE: INPUT INVENTORY COMPLETE

---

### PHASE 2 — CONVERGENCE SUMMARY

Synthesize the INPUT INVENTORY into a one-paragraph domain characterization:
- What does this domain do?
- Who are its users/stakeholders?
- What are the core technical or process concerns?
- What is the status quo that currently satisfies the need (the inertia force)?

Label this paragraph CONVERGENCE SUMMARY. This is a derived artifact for framing only --
it does not substitute for Phase 1 row-IDs in Phase 4 citations.

EXIT GATE: CONVERGENCE SUMMARY COMPLETE

---

### PHASE 3 — CANDIDATE ROLE SET

Enumerate candidate roles. Minimum 5. Include exactly one role whose orientation is
"status-quo advocate" -- this is the inertia-advocate. Also include: product-perspective
role, technical-perspective role, and at least one domain-specific expert role
auto-selected from the CONVERGENCE SUMMARY.

List candidates as:

  Candidate | Provisional perspective | Provisional scope

Label this table CANDIDATE ROSTER.

EXIT GATE: CANDIDATE ROSTER COMPLETE

---

### PHASE 4 — FRAME FILL

For each candidate in the CANDIDATE ROSTER, populate all five fields in a structured
block. Each field value must include a source citation on the line immediately following:

  Phase 1 source: {row-id} = "{verbatim phrase from that row}"

If a field value draws from multiple rows, cite the primary row. If no Phase 1 row
supports a field value, write UNSUPPORTED -- revise the field or add a row.

FRAME FILL block format:

  ROLE: {name}
  orientation.frame: {value}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  orientation.serves: {value}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  lens.verify: {2-3 domain-specific questions the role would ask of any proposal}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  lens.simplify: {2-3 rules this role uses to cut scope or reduce complexity}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  expertise.depth: {specific knowledge depth, not generic title}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  expertise.relevance: {why this depth matters to this domain}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  scope: {component / feature / system / cross-system / org}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  collaborates_with: {2-3 role names from CANDIDATE ROSTER, not generic titles}
    Phase 1 source: {row-id} = "{verbatim phrase}"

Complete FRAME FILL for every candidate before proceeding to Phase 5.

EXIT GATE: FRAME FILL COMPLETE (all candidates populated, all fields cited)

---

### PHASE 5 — PLANNING TABLE

Build the planning table. One row per candidate. Columns:

  Role | Scope | Perspective | Planned-Vocab-Term

Rules:
- Perspective must be one of: product / technical / inertia / domain / strategy / user
- Planned-Vocab-Term must be a single domain-specific term that will appear verbatim in
  the written role file's lens or expertise fields (not a generic word)

After filling all rows, run two audits:

  SCOPE AUDIT: count distinct values in the Scope column.
  If distinct Scope values < 2: emit SCOPE AUDIT FAIL -- add roles or reassign scopes before continuing.
  If distinct Scope values >= 2: emit SCOPE AUDIT PASS.

  PERSPECTIVE AUDIT: count distinct values in the Perspective column.
  If distinct Perspective values < 3: emit PERSPECTIVE AUDIT FAIL -- add or reassign roles before continuing.
  If distinct Perspective values >= 3: emit PERSPECTIVE AUDIT PASS.

Both SCOPE AUDIT PASS and PERSPECTIVE AUDIT PASS are required to proceed to Phase 6.
Do not open Phase 6 if either audit is FAIL.

EXIT GATE: SCOPE AUDIT PASS + PERSPECTIVE AUDIT PASS

---

### PHASE 6 — WRITE ROLE FILES

Write role files to `.roles/{domain}/`. Follow this sequence:

  STEP 6.1 — WRITE INERTIA-ADVOCATE FIRST
  Write the inertia-advocate role file using its FRAME FILL block. Use the Planned-Vocab-Term
  from the planning table verbatim in lens or expertise. Write the file now.
  Emit: INERTIA-ADVOCATE WRITTEN: .roles/{domain}/{filename}

  STEP 6.2 — WRITE REMAINING ROLES (one at a time)
  For each remaining role in planning table order:
    a. Write the role file using its FRAME FILL block. Planned-Vocab-Term must appear verbatim.
    b. Immediately after writing, emit an inline LENS AUDIT:
       LENS AUDIT [{role-name}]:
         - verify[1] fires: YES/NO — {evidence from written lens.verify}
         - verify[2] fires: YES/NO — {evidence from written lens.verify}
         - simplify[1] fires: YES/NO — {evidence from written lens.simplify}
         - domain-specific term used: YES/NO — {term and field it appears in}
       If any item is NO, revise the file before moving to the next role.

EXIT GATE: ALL ROLE FILES WRITTEN + ALL LENS AUDITS PASS

---

### PHASE 7 — VERIFICATION CHECKS

Run all checks in order. Do not skip any check. Emit the result of each check before
moving to the next.

  CHECK 1 — FIELD COMPLETENESS
  For each written file: confirm name, orientation, lens, expertise, scope,
  collaborates_with are all present and non-empty.
  Emit per file: CHECK 1 [{filename}]: PASS / FAIL [{missing field}]

  CHECK 2 — INERTIA-ADVOCATE PRESENT
  Confirm a file with orientation "status-quo advocate" exists.
  Emit: CHECK 2: PASS / FAIL

  CHECK 3A — SCOPE AUDIT (from written files)
  Read the scope field from each written file. Count distinct values.
  If < 2: CHECK 3A: FAIL — add roles before marking complete.
  If >= 2: CHECK 3A: PASS
  Emit: CHECK 3A: PASS / FAIL [distinct scope values: N]

  CHECK 3B — SCOPE PLAN-TO-WRITE BINDING
  For each role: confirm written scope matches planning table scope.
  If any mismatch: fire ROLE-REPLACE sub-procedure (see below). Emit binding result per role.
  Emit: CHECK 3B: PASS / FAIL [list any mismatches]

  CHECK 4A — SET COVERAGE
  Confirm every role in the planning table has a corresponding written file.
  Emit: CHECK 4A: PASS / FAIL [list any missing]

  CHECK 4B — VOCAB BINDING
  For each role: confirm the Planned-Vocab-Term from the planning table appears verbatim
  in the written file (lens or expertise fields).
  If any mismatch: fire ROLE-REPLACE sub-procedure (see below).
  Emit per role: CHECK 4B [{role}]: PASS / FAIL [{term} not found]

  CHECK 5A — FRAME MATCH
  For each role: confirm that field values in the written file match the FRAME FILL output
  for that role. Minor prose variation is acceptable; field omission or substitution is not.
  Emit per role: CHECK 5A [{role}]: PASS / MISMATCH [{field}: expected vs found]

  CHECK 5B — SOURCE CITATION VERIFIABLE
  For each role and each field: confirm the `Phase 1 source: {row-id} = "{verbatim phrase}"`
  line exists and is verifiable against the INPUT INVENTORY.
  On any violation: emit [{role}.{field}: Phase 1 source missing or unverifiable -- CITATION FAIL]
  Emit overall: CHECK 5B: PASS / FAIL [citation fail count: N]

  CHECK 6 — DOMAIN SPECIFICITY
  Scan all written files. Flag any generic placeholder (e.g., "relevant expertise",
  "domain knowledge", "stakeholders"). Each flag is a SPECIFICITY FAIL.
  Emit: CHECK 6: PASS / FAIL [flags: N, list them]

  CHECK 7 — OUTPUT PATH
  Confirm all files are at `.roles/{domain}/` and no file is at a different path.
  Emit: CHECK 7: PASS / FAIL

  CHECK 8 — PERSPECTIVE AUDIT (from written files)
  Read the perspective dimension from each written file (infer from orientation.frame if
  no explicit field). Count distinct perspective values.
  If < 3: CHECK 8: FAIL -- the written set has collapsed perspective diversity.
  If >= 3: CHECK 8: PASS
  Emit: CHECK 8: PASS / FAIL [distinct perspectives: N, list them]

EXIT GATE: ALL CHECKS PASS

---

### ROLE-REPLACE SUB-PROCEDURE

Fires whenever CHECK 3B or CHECK 4B emits a mismatch for a role. Run this sub-procedure
immediately for that role before continuing the check.

  planned: {role name and binding value from planning table}
  written: {role name and binding value actually found in written file}
  resolution: {one sentence explaining why the written value differs from planned}
  re-evaluation: {re-run CHECK 1, 3A, 4A, 5A, 5B, 6, 8 for this role; emit per-check result}

After completing all four fields, emit:
  ROLE-REPLACE CONFIRMED: YES (all four fields present, re-evaluation row complete)
  or
  ROLE-REPLACE CONFIRMED: NO (one or more fields missing or re-evaluation incomplete)

CHECK 3B and CHECK 4B cannot reach PASS status for a role while that role's
ROLE-REPLACE CONFIRMED is NO.
```

---

## V-02

**Variation axis**: Phrasing register -- CONVERSATIONAL (plain English procedural)
**Hypothesis**: Replacing CAPS gate names and procedural block labels with natural-language
instructions ("before you open the next step, count the distinct...") preserves the gate
logic while reducing mechanical compliance artifacts. Conversational register may produce
more naturalistic role-file content because the prompt does not signal "schema fill-in"
mode. All six v10 mechanisms are present but expressed as plain directives rather than
named procedures.

```
Your job is to build a typed role registry for the domain named in `for:`. You will read
the codebase or spec, figure out what expert perspectives are needed, and write one
markdown file per role at `.roles/{domain}/`. You always include a role whose job
is to argue that the status quo is good enough -- the inertia advocate. Every role gets
these fields: name, orientation (frame + serves), lens (verify questions + simplify
rules), expertise (depth + relevance), scope, collaborates_with.

Here is how to do it:

**Step 1 -- Read the inputs**

Glob and Read the files that describe this domain. For each file you read, note a short
excerpt (under 20 words) that would justify a role's existence. Number each row so you
can cite it later. Aim for at least 5 rows. If there aren't enough domain-specific files,
pull from the repo root (README, config, any CLAUDE.md).

**Step 2 -- Summarize the domain**

Write a paragraph that captures: what this domain does, who uses it, what the core
technical or process concerns are, and what the current solution is (the thing teams
reach for instead of building something new). This summary is for framing only -- when
you cite sources in Step 3, always trace back to the numbered rows from Step 1, not to
this summary.

**Step 3 -- List your candidate roles**

Name at least 5 roles. One of them must be the status-quo advocate (orientation:
"status-quo advocate"). Include at least one product-perspective role, one
technical-perspective role, and one domain expert you auto-selected from your Step 2
summary. For each candidate jot down its provisional perspective (product / technical /
inertia / domain / strategy / user) and scope (component / feature / system /
cross-system / org).

**Step 4 -- Fill in every field for every candidate**

For each candidate, write out all five fields in full. After each field value, add a line
that traces it to a specific Step 1 row:

  source: row-{N} = "{exact words from that row}"

If a field has no Step 1 row to back it up, write UNSUPPORTED and revise the field until
it does. This is not optional -- every field needs a traceable source before you move on.

**Step 5 -- Build the planning table and run two checks**

Make a table with columns: Role | Scope | Perspective | Vocab-Term

The Vocab-Term must be a domain-specific word or phrase (not a generic like "quality" or
"performance") that you will use verbatim in that role's lens or expertise when you write
the file.

Once the table is full, do two things before you touch any file:

First, count the distinct values in the Scope column. You need at least two different
scope levels. If you don't have two, add a role or reassign scopes now. Write "Scope
check: passed (N distinct scopes)" or "Scope check: failed -- adding role X".

Second, count the distinct values in the Perspective column. You need at least three
different perspective categories. If you don't have three, add a role or change
assignments. Write "Perspective check: passed (N distinct perspectives)" or "Perspective
check: failed -- adjusting role Y". Do not write any files until both checks pass.

**Step 6 -- Write the files**

Start with the inertia advocate. Write that file first, confirm the Vocab-Term from the
table appears verbatim in lens or expertise, then write this line before moving on:
"Inertia advocate written: .roles/{domain}/{filename}"

Then write each remaining role one at a time. After writing each file, run a quick lens
check and write the results inline:
  - Does verify-question-1 use domain-specific language? (yes/no + the evidence)
  - Does verify-question-2 use domain-specific language? (yes/no + the evidence)
  - Does simplify-rule-1 name a concrete cut rather than a generic idea? (yes/no)
  - Does the Vocab-Term from the planning table appear verbatim? (yes/no + where)

If any answer is "no", revise the file before writing the next role.

**Step 7 -- Run the full verification pass**

Work through these checks in order. Write the result of each check before moving to the
next one.

  1. Fields complete: for each file, confirm all five fields are present and non-empty.
     Write "[filename]: ok" or "[filename]: missing {field}".

  2. Inertia advocate exists: confirm there is a file with orientation "status-quo
     advocate". Write "Inertia advocate: found" or "Inertia advocate: missing".

  3a. Scope spread (from files): read the scope field from each written file; count
      distinct values. Need >= 2. Write "Scope spread: N distinct values -- ok/fail".

  3b. Scope matches plan: for each role, confirm the written scope matches the planning
      table. If it doesn't, run the replacement log (see below) before marking this check.
      Write "Scope binding: ok" or "Scope binding: mismatch on {role}".

  4a. All roles written: confirm every row in the planning table has a written file.
      Write "Set complete: ok" or "Set complete: missing {role}".

  4b. Vocab terms present: for each role, confirm the Vocab-Term from the table appears
      verbatim in the written file. If it doesn't, run the replacement log (see below).
      Write "{role} vocab: ok" or "{role} vocab: term '{X}' not found".

  5a. Fields match Step 4: confirm written fields match your Step 4 fill-in. Prose
      variation is fine; omitting or substituting fields is not. Write per-role result.

  5b. Sources traceable: for each role and each field, confirm the source line (row-{N}
      = "...") is present and points to a real row from Step 1. If any source line is
      missing or unverifiable write "{role}.{field}: source missing -- CITATION FAIL".
      Write total count: "Source trace: N fails" (should be 0).

  6. No generic placeholders: scan files for phrases like "relevant expertise", "domain
     knowledge", "stakeholders". Each one is a specificity flag. Write "Specificity: ok"
     or "Specificity: N flags found -- {list}".

  7. Output path correct: confirm all files are at `.roles/{domain}/`. Write
     "Output path: ok" or "Output path: wrong path on {file}".

  8. Perspective spread (from files): read or infer the perspective of each written role
     from orientation.frame. Count distinct values. Need >= 3. Write "Perspective spread:
     N distinct perspectives -- ok/fail". A fail here means Phase 6 collapsed perspective
     diversity; add a role if needed.

**Replacement log** (run this whenever a scope mismatch or vocab mismatch is found)

Write four lines:
  planned: {what the planning table said}
  written: {what actually ended up in the file}
  resolution: {one sentence explaining why}
  re-check: {re-run checks 1, 3a, 4a, 5a, 5b, 6, 8 for this role and write the results}

After the four lines write "Replacement logged: complete" or "Replacement logged:
incomplete -- {what is still missing}". Checks 3b and 4b stay open for this role until
you write "Replacement logged: complete".
```

---

## V-03

**Variation axis**: Inertia framing -- INERTIA-AS-BENCHMARK
**Hypothesis**: Positioning the inertia-advocate as the epistemic anchor for all other
roles -- defining them in terms of what they propose that the status quo cannot provide
-- produces richer domain-grounded inertia content (C-10), stronger collaborates_with
chains, and more specific lens.verify questions. Rather than "include a devil-advocate
role", the prompt treats the status quo as the first fact about the domain and all
proposed roles as claims against it. All six v10 mechanisms are preserved; only the
framing of inertia changes.

```
Before you define any expert roles, establish the inertia fact: what does the team
reach for today when this domain's need arises? That answer -- the status quo solution
-- is the benchmark against which every proposed role must justify its existence. A role
that does not address a gap in the status quo belongs in a different registry.

Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Every role gets: name, orientation (frame +
serves), lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with.

---

**Phase 1 -- Input scan**

Read the codebase, spec, or context files. Build an INPUT INVENTORY: one row per file
with columns Row-ID | Source | Relevant excerpt (≤ 20 words). Minimum 5 rows. These rows
are your only citable source -- every field value in Phase 4 must trace to a row here.

---

**Phase 2 -- Inertia characterization**

From the INPUT INVENTORY, describe the status quo in one paragraph:
- Name the tool, process, or approach teams use today.
- State what problems it solves well (strengths that defend its position).
- State what gaps it does not solve (the opening for new roles).

Label this INERTIA BASELINE. This paragraph informs the inertia-advocate role and
sets the scope of every other role: each expert role exists to address one or more
gaps named here.

Then write a short CONVERGENCE SUMMARY synthesizing broader domain context (users,
technical concerns, strategic fit).

---

**Phase 3 -- Role set grounded in inertia gaps**

Enumerate candidate roles. For each candidate, state which gap from the INERTIA BASELINE
it addresses. One role must be the inertia-advocate, whose orientation is "status-quo
advocate" and whose lens.verify questions challenge whether each new proposal beats the
status quo on the dimensions where the status quo is strongest.

Minimum 5 roles. Include: one product-perspective role, one technical-perspective role,
at least one domain-specific expert derived from the CONVERGENCE SUMMARY.

List candidates as: Candidate | Gap addressed | Provisional perspective | Provisional scope

---

**Phase 4 -- Frame Fill with Phase 1 source citations**

For each candidate, populate all five fields. After each field value, add:

  Phase 1 source: {row-id} = "{verbatim phrase from that row}"

The inertia-advocate's lens.verify questions must explicitly name the dimensions where
the status quo is strongest (from INERTIA BASELINE). Its lens.simplify rules must name
conditions under which the status quo is the right answer.

If any field has no supporting Phase 1 row, mark it UNSUPPORTED and revise.

Frame Fill block:

  ROLE: {name}
  orientation.frame: {value} | Phase 1 source: {row-id} = "{phrase}"
  orientation.serves: {value} | Phase 1 source: {row-id} = "{phrase}"
  lens.verify: {questions} | Phase 1 source: {row-id} = "{phrase}"
  lens.simplify: {rules} | Phase 1 source: {row-id} = "{phrase}"
  expertise.depth: {value} | Phase 1 source: {row-id} = "{phrase}"
  expertise.relevance: {value} | Phase 1 source: {row-id} = "{phrase}"
  scope: {value} | Phase 1 source: {row-id} = "{phrase}"
  collaborates_with: {2-3 roles} | Phase 1 source: {row-id} = "{phrase}"

---

**Phase 5 -- Planning table with dual gate**

Build planning table: Role | Scope | Perspective | Planned-Vocab-Term | Gap-Addressed

Planned-Vocab-Term must be a domain-specific term that will appear verbatim in that
role's lens or expertise field. Gap-Addressed must match a gap named in INERTIA BASELINE.
The inertia-advocate's Gap-Addressed must state which strength it defends (not a gap).

Run two gates:

  SCOPE AUDIT: count distinct Scope values.
  < 2 distinct values → SCOPE AUDIT FAIL (add or reassign before Phase 6).
  >= 2 distinct values → SCOPE AUDIT PASS.

  PERSPECTIVE AUDIT: count distinct Perspective values.
  < 3 distinct values → PERSPECTIVE AUDIT FAIL (add or reassign before Phase 6).
  >= 3 distinct values → PERSPECTIVE AUDIT PASS.

Phase 6 is blocked until both gates emit PASS.

---

**Phase 6 -- Write role files (inertia-advocate anchors the sequence)**

Write the inertia-advocate file first. Its lens.verify questions must reference the
INERTIA BASELINE strengths by name. Planned-Vocab-Term must appear verbatim.
Emit: INERTIA-ADVOCATE WRITTEN: {path}

For each remaining role:
  a. Write the file. Planned-Vocab-Term must appear verbatim.
  b. Confirm the role's collaborates_with list includes the inertia-advocate as one of its
     named partners (every role should know to consult the status-quo advocate).
  c. Emit inline LENS AUDIT:
     LENS AUDIT [{role-name}]:
       - verify[1] fires on domain-specific concern: YES/NO
       - verify[2] fires on domain-specific concern: YES/NO
       - simplify[1] names a concrete cut: YES/NO
       - Planned-Vocab-Term present verbatim: YES/NO
       - collaborates_with includes inertia-advocate: YES/NO
     Revise the file if any item is NO.

---

**Phase 7 -- Verification checks**

CHECK 1 -- Field completeness: all five fields present per file. Emit per file.
CHECK 2 -- Inertia-advocate exists and has orientation "status-quo advocate".
CHECK 3A -- Scope spread >= 2 distinct values from written files.
CHECK 3B -- Written scope matches planning table. Fire ROLE-REPLACE if mismatch.
CHECK 4A -- All planning table roles written.
CHECK 4B -- Every Planned-Vocab-Term appears verbatim. Fire ROLE-REPLACE if mismatch.
CHECK 5A -- Written fields match Frame Fill values per role.
CHECK 5B -- Every field has a verifiable Phase 1 source citation.
  Emit: [{role}.{field}: Phase 1 source missing or unverifiable -- CITATION FAIL] per violation.
CHECK 6 -- No generic placeholders in any written file.
CHECK 7 -- All files at `.roles/{domain}/`.
CHECK 8 -- Perspective spread >= 3 distinct values from written files. PERSPECTIVE AUDIT PASS/FAIL.

  INERTIA ANCHOR CHECK: confirm the inertia-advocate's lens.verify questions name at least
  two INERTIA BASELINE strengths by the exact terms used in Phase 2. If not, revise and
  re-run CHECK 1 and CHECK 5A for that file.

---

**ROLE-REPLACE sub-procedure**

Fires at CHECK 3B or CHECK 4B mismatch:

  planned: {planning table value}
  written: {value found in written file}
  resolution: {one sentence}
  re-evaluation: {re-run CHECK 1, 3A, 4A, 5A, 5B, 6, 8 for this role; emit per-check}

Emit: ROLE-REPLACE CONFIRMED: YES / NO
CHECK 3B and CHECK 4B stay FAIL for this role while ROLE-REPLACE CONFIRMED is NO.
```

---

## V-04

**Variation axes**: Lifecycle emphasis (VERBOSE) + Inertia framing (INERTIA-AS-BENCHMARK)
**Hypothesis**: Combining maximum phase scaffolding with the inertia-benchmark framing
produces the most auditable output: explicit phase headers prevent phase collapse, and
inertia-as-benchmark ensures the inertia-advocate content is rich enough to pass C-10.
The INERTIA BASELINE in Phase 2 becomes a first-class artifact referenced by the Phase 5
planning table and by CHECK 8's INERTIA ANCHOR CHECK. V-04 tests whether structural
verbosity and inertia prominence reinforce each other or whether the combined bulk causes
LLMs to abbreviate later phases.

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. Inertia-advocate is always included and written first.

Before defining any roles, establish the status quo: name the tool, process, or approach
teams currently use for this domain's need, its strengths, and its gaps. This INERTIA
BASELINE anchors every role. Roles without a gap to fill do not belong in this registry.

---

### PHASE 1 -- INPUT INVENTORY

Read all relevant files. Build the INPUT INVENTORY table:

  Row-ID | Source file | Excerpt (≤ 20 words)

Minimum 5 rows. Label the table INPUT INVENTORY. This is the sole citation source for
Phase 4 -- no field value may cite the CONVERGENCE SUMMARY or INERTIA BASELINE instead
of a row here.

EXIT GATE: INPUT INVENTORY COMPLETE (minimum 5 rows present)

---

### PHASE 2 -- INERTIA BASELINE + CONVERGENCE SUMMARY

Write two labeled artifacts:

INERTIA BASELINE (1-2 paragraphs):
  - Name the status quo solution.
  - List 2-3 strengths it has that make it hard to displace.
  - List 2-3 gaps it does not address (these become the justification for new roles).

CONVERGENCE SUMMARY (1 paragraph):
  - Domain function, users, technical concerns, strategic context.

Both are framing artifacts. Phase 4 citations must trace to INPUT INVENTORY rows, not
to these paragraphs.

EXIT GATE: INERTIA BASELINE COMPLETE + CONVERGENCE SUMMARY COMPLETE

---

### PHASE 3 -- CANDIDATE ROSTER

Enumerate at least 5 candidate roles. For each:
  - State which INERTIA BASELINE gap (or strength, for the inertia-advocate) it addresses.
  - Assign provisional perspective (product / technical / inertia / domain / strategy / user)
  - Assign provisional scope (component / feature / system / cross-system / org)

The inertia-advocate's reason-to-exist is "defending the strength(s) named in INERTIA
BASELINE." Every other role's reason is one of the INERTIA BASELINE gaps.

Table format: Candidate | Gap/Strength addressed | Perspective | Scope

EXIT GATE: CANDIDATE ROSTER COMPLETE (inertia-advocate present, gap/strength assigned)

---

### PHASE 4 -- FRAME FILL

For each candidate, fill all five fields with a source citation per field:

  ROLE: {name}
  orientation.frame: {value}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  orientation.serves: {value}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  lens.verify: {domain-specific questions}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  lens.simplify: {concrete cut rules}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  expertise.depth: {specific knowledge}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  expertise.relevance: {why this domain needs it}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  scope: {scope value}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  collaborates_with: {2-3 named roles}
    Phase 1 source: {row-id} = "{verbatim phrase}"

The inertia-advocate's lens.verify must name at least two INERTIA BASELINE strengths by
their exact terms. Any field marked UNSUPPORTED must be revised before proceeding.

EXIT GATE: FRAME FILL COMPLETE (all candidates, all fields, all citations present)

---

### PHASE 5 -- PLANNING TABLE + DUAL GATE

Build planning table: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength

Planned-Vocab-Term: a domain-specific term that will appear verbatim in the written file's
lens or expertise. Gap/Strength: must match an item from INERTIA BASELINE.

Run both audits. Do not proceed to Phase 6 until both PASS.

  SCOPE AUDIT:
  Count distinct Scope column values.
  < 2: SCOPE AUDIT FAIL -- expand role set or reassign.
  >= 2: SCOPE AUDIT PASS.

  PERSPECTIVE AUDIT:
  Count distinct Perspective column values.
  < 3: PERSPECTIVE AUDIT FAIL -- add roles or reassign.
  >= 3: PERSPECTIVE AUDIT PASS.

EXIT GATE: SCOPE AUDIT PASS + PERSPECTIVE AUDIT PASS

---

### PHASE 6 -- WRITE ROLE FILES

STEP 6.1 -- INERTIA-ADVOCATE FIRST
Write the inertia-advocate role file. Its lens.verify must reference INERTIA BASELINE
strengths by name. Planned-Vocab-Term must appear verbatim in lens or expertise.
Emit: INERTIA-ADVOCATE WRITTEN: {path}

STEP 6.2 -- REMAINING ROLES
For each remaining role in planning table order:
  a. Write the file using Phase 4 FRAME FILL values. Planned-Vocab-Term must appear verbatim.
  b. Confirm collaborates_with includes the inertia-advocate by name.
  c. Emit inline LENS AUDIT:
     LENS AUDIT [{role-name}]:
       - verify[1] domain-specific: YES/NO + evidence
       - verify[2] domain-specific: YES/NO + evidence
       - simplify[1] concrete cut: YES/NO + evidence
       - Planned-Vocab-Term verbatim: YES/NO + location
       - collaborates_with inertia-advocate: YES/NO
     Revise before proceeding if any item is NO.

EXIT GATE: ALL ROLE FILES WRITTEN + ALL LENS AUDITS PASS

---

### PHASE 7 -- VERIFICATION CHECKS

Emit each check result before running the next.

  CHECK 1: Field completeness per file. Emit: CHECK 1 [{filename}]: PASS / FAIL [{field}]
  CHECK 2: Inertia-advocate exists (orientation = "status-quo advocate"). Emit: CHECK 2: PASS/FAIL
  CHECK 3A: Scope spread from written files >= 2. Emit: CHECK 3A: PASS/FAIL [N distinct]
  CHECK 3B: Written scope matches planning table. Fire ROLE-REPLACE if mismatch.
  CHECK 4A: All planning table roles written. Emit: CHECK 4A: PASS/FAIL
  CHECK 4B: Planned-Vocab-Terms present verbatim. Fire ROLE-REPLACE if mismatch.
  CHECK 5A: Written fields match Frame Fill per role. Emit per role.
  CHECK 5B: Phase 1 source citations verifiable per field.
    Emit: [{role}.{field}: Phase 1 source missing or unverifiable -- CITATION FAIL] per violation.
  CHECK 6: No generic placeholders. Emit: CHECK 6: PASS/FAIL [N flags]
  CHECK 7: All files at .roles/{domain}/. Emit: CHECK 7: PASS/FAIL
  CHECK 8: Perspective spread from written files >= 3. Emit: CHECK 8: PASS/FAIL [N distinct]

  INERTIA ANCHOR CHECK:
  Re-read the inertia-advocate's lens.verify field. Confirm at least two INERTIA BASELINE
  strength terms appear verbatim. If not: INERTIA ANCHOR CHECK FAIL -- revise file and
  re-run CHECK 1, 5A, 5B for the inertia-advocate.
  Emit: INERTIA ANCHOR CHECK: PASS/FAIL

EXIT GATE: ALL CHECKS PASS + INERTIA ANCHOR CHECK PASS

---

### ROLE-REPLACE SUB-PROCEDURE

Fires at CHECK 3B or CHECK 4B mismatch.

  planned: {planning table value for this role}
  written: {value found in written file}
  resolution: {one sentence}
  re-evaluation: {re-run CHECK 1, 3A, 4A, 5A, 5B, 6, 8 and INERTIA ANCHOR CHECK for this
                  role; emit per-check result}

Emit: ROLE-REPLACE CONFIRMED: YES / NO
CHECK 3B and CHECK 4B stay FAIL for this role while ROLE-REPLACE CONFIRMED is NO.
```

---

## V-05

**Variation axes**: Lifecycle emphasis (VERBOSE) + Phrasing register (CONVERSATIONAL) +
Inertia framing (INERTIA-AS-BENCHMARK) -- full integration
**Hypothesis**: The richest combination -- maximum scaffolding + plain English directives +
inertia anchoring -- produces outputs that are both structurally auditable (the headers
and gates prevent collapse) and naturalistic in content (the conversational phrasing
prevents mechanical placeholder filling). The inertia-as-benchmark framing runs through
every phase in natural language rather than being isolated to a single gate. This is the
all-three-new-axes version of V-05, analogous to the R15 all-combined baseline that closed
Gaps A/B/C -- this version tests whether axis-combination itself introduces brittleness.

```
Your task is to build a typed role registry for the domain named in `for:`. For each role
you identify, write a markdown file at `.roles/{domain}/` with these fields: name,
orientation (frame + serves), lens (verify questions + simplify rules), expertise (depth
+ relevance), scope, collaborates_with.

Start by thinking about the status quo: what do teams use today when they need to handle
this domain? That's the benchmark. Every role you define should either defend why the
current approach is right (the inertia advocate -- always included) or explain what the
current approach cannot do. If a role doesn't connect to that benchmark, it probably
doesn't belong here.

---

## Step 1 -- Read the inputs

Read the files for this domain. For each file, note one short excerpt (under 20 words)
that tells you something useful about what roles might be needed. Number each row -- you'll
cite these row numbers later. Try to find at least 5 files. If there aren't that many
specific files, include the README or other repo-level context.

Call this your input list. It's the only thing you can cite in Step 4 -- not your summary,
not your memory.

---

## Step 2 -- Name the status quo and the gaps

Write two things:

First, a short description of the current solution (1-2 paragraphs): what it's called,
what it does well (the reasons it's sticky), and what problems it leaves open. Call this
your inertia baseline. The "does well" list will become the inertia advocate's core
challenge; the "leaves open" list justifies every other role.

Second, a one-paragraph summary of the domain more broadly: who uses it, what the core
technical or process concerns are, what's at stake strategically. Call this your domain
summary.

---

## Step 3 -- Figure out which roles you need

List at least 5 candidates. For each one:
- Say which gap from your inertia baseline it addresses (or which strength, for the
  inertia advocate).
- Give it a perspective label: product, technical, inertia, domain, strategy, or user.
- Give it a scope: component, feature, system, cross-system, or org.

The inertia advocate's job is to challenge every proposal with the question "does this
actually beat the current solution on the dimensions where the current solution is
strongest?" That's different from just opposing change -- it's holding the bar at the
right height.

---

## Step 4 -- Fill in every field, with sources

For each candidate, write out all five fields in full. After each field value, trace it
to your input list:

  source: row-{N} = "{exact words from that row}"

For the inertia advocate specifically, the verify questions must name at least two of the
"does well" items from your inertia baseline -- by the exact terms you used there.

If you can't trace a field to an input row, mark it unsupported and revise it until you
can. Every field needs a traceable source before you move on.

---

## Step 5 -- Build the planning table, then check two things

Make a table: Role | Scope | Perspective | Vocab-Term | Gap-addressed

The vocab term should be a specific word or phrase from the domain (not something generic
like "quality" or "architecture") that you'll use verbatim in that role's lens or
expertise when you write the file. The gap-addressed column should match something you
named in Step 2.

Before writing any files, check:

First, look at your Scope column. Do you have at least two different scope levels? If all
your roles are at the same scope, add one or reassign. Write: "Scope check: N distinct
scopes -- ok" or "Scope check: only 1 -- adjusting [role]".

Second, look at your Perspective column. Do you have at least three different perspective
categories? If not, add or reassign. Write: "Perspective check: N distinct perspectives
-- ok" or "Perspective check: only N -- adding [role]". Don't write any files until both
checks are ok.

---

## Step 6 -- Write the files

Start with the inertia advocate. Write its file, make sure the vocab term from Step 5
appears verbatim in lens or expertise, and write this line: "Inertia advocate written:
.roles/{domain}/{filename}". This confirms you haven't skipped ahead.

Then write each remaining role one at a time. After each file, run a quick lens check
and write the result right there:

  Lens check [{role-name}]:
  - First verify question is domain-specific (yes/no -- what's the evidence)?
  - Second verify question is domain-specific (yes/no -- what's the evidence)?
  - First simplify rule names a concrete cut, not a vague principle (yes/no)?
  - Vocab term appears verbatim (yes/no -- where exactly)?
  - collaborates_with includes the inertia advocate (yes/no)?

If any answer is no, fix the file before moving to the next role.

---

## Step 7 -- Full check pass

Work through these in order. Write each result before running the next.

  1. Fields complete: for each file, are all five fields present and non-empty?
     Write "[filename]: ok" or "[filename]: missing {field}".

  2. Inertia advocate present: is there a file with orientation "status-quo advocate"?
     Write "Inertia advocate: found / missing".

  3a. Scope spread (from written files): count distinct scope values you actually wrote.
      Need >= 2. Write "Scope spread: N -- ok/needs-fix".

  3b. Scope matches Step 5: does each written scope match the planning table?
      If not, run the replacement log below before marking this done.
      Write "Scope binding: ok" or "Scope binding: mismatch on {role}".

  4a. All roles written: is there a file for every row in the planning table?
      Write "Set complete: yes/no -- missing {role}".

  4b. Vocab terms present: does each file contain its vocab term verbatim?
      If not, run the replacement log below.
      Write "{role} vocab: ok" or "{role} vocab: '{term}' not found".

  5a. Fields match Step 4: do the written fields match what you filled in Step 4?
      (Prose variation is fine; adding or dropping fields is not.)
      Write per-role results.

  5b. Sources traceable: does every field have a "source: row-{N} = ..." line pointing
      to a real row from Step 1? If any is missing or points to a non-existent row, write
      "{role}.{field}: source missing -- citation fail". Total count should be zero.

  6. Specific language: scan each file for generic filler phrases like "relevant
     expertise", "domain knowledge", "appropriate stakeholders". Flag any you find.
     Write "Specificity: ok" or "Specificity: N flags -- {list}".

  7. Output path: are all files at `.roles/{domain}/`?
     Write "Output path: ok" or "Output path: wrong location on {file}".

  8. Perspective spread (from written files): infer each role's perspective from its
     orientation.frame. Count distinct categories. Need >= 3.
     Write "Perspective spread: N -- ok/needs-fix".

  Inertia anchor: re-read the inertia advocate's verify questions. Do they name at least
  two "does well" items from your Step 2 inertia baseline by exact name?
  If not, revise the file and re-run checks 1, 5a, 5b for it.
  Write "Inertia anchor: ok" or "Inertia anchor: missing {strength-term} -- revising".

---

## Replacement log (run this for any scope or vocab mismatch)

Write four things:
  planned: {what Step 5 said}
  written: {what the file actually has}
  resolution: {one sentence -- why did it change?}
  re-check: {re-run checks 1, 3a, 4a, 5a, 5b, 6, 8, and inertia anchor for this role;
             write each result}

Then write: "Replacement complete: yes" or "Replacement complete: no -- {what's still
missing}". Checks 3b and 4b stay open for this role until you write "Replacement
complete: yes".
```
