---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 17
rubric: crew-roles-rubric-v11-2026-03-17.md
---

# crew-roles -- Variate R17

5 complete prompt body variations for the `crew-roles` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

**Baseline**: R16 V-04 (VERBOSE + INERTIA-AS-BENCHMARK). R16 V-04 contains all seven
prior mechanisms: C-30 (inertia-first gate), C-31 (vocab binding column), C-32 (inline
LENS AUDIT), C-33 (PERSPECTIVE AUDIT + CHECK 8), C-34 (per-slot `Phase 1 source:
{row-id} = "{verbatim phrase}"` + CHECK 5A/5B split), C-35 (ROLE-REPLACE sub-procedure
with 4 fields + CONFIRMED gate), C-36 (INERTIA BASELINE artifact in Phase 2 with named
tool + enumerated strengths + enumerated gaps, plus INERTIA ANCHOR CHECK in Phase 7
verifying verbatim propagation to lens.verify). v11 rubric has 28 aspirational criteria;
baseline scores 28/28 in static analysis.

**Gaps to probe in R17**: C-36 is now structural. The INERTIA BASELINE + INERTIA ANCHOR
CHECK mechanism is established in V-04. R17 shifts to stress-testing whether C-36 survives
under three structural risks not addressed by the current formulation:

- **Risk-1 -- Accidental verbatim**: The INERTIA BASELINE lists strengths in prose ("fast
  and easy to deploy"). The LLM writes "easy to deploy" in lens.verify. INERTIA ANCHOR
  CHECK passes, but the match was heuristic, not structural. If the strength phrase is
  generic, the check is gameable. Hypothesis: labeling each strength with a discrete
  identifier (S1/S2/S3) and requiring the label + term to appear verbatim in lens.verify
  makes the anchor non-accidental and auditable.

- **Risk-2 -- Late detection**: INERTIA ANCHOR CHECK fires only in Phase 7. If the
  inertia-advocate was written in Phase 6 Step 6.1 without INERTIA BASELINE strength terms
  in its lens.verify, the error is caught only after all other roles are written, requiring
  cascade revisions. Hypothesis: firing INERTIA ANCHOR CHECK immediately after Step 6.1
  catches the error before other roles are written, reducing revision scope.

- **Risk-3 -- Single-file anchoring**: INERTIA ANCHOR CHECK verifies only the
  inertia-advocate's lens.verify. A registry where only the inertia-advocate references the
  baseline is structurally thin -- the baseline should shape multiple roles' perspectives.
  Hypothesis: requiring at least one non-inertia-advocate role's lens.verify to reference an
  INERTIA BASELINE term (strength or gap) validates that the baseline has genuinely
  influenced the registry, not just the inertia-advocate file.

**New axes**:
- **Axis-D -- Labeled strength terms**: INERTIA BASELINE numbers each strength S1/S2/S3
  and each gap G1/G2/G3. Forward-references must use the label + exact term. INERTIA
  ANCHOR CHECK verifies label-prefixed terms, not unanchored prose matches.
- **Axis-E -- Early INERTIA ANCHOR CHECK (Phase 6.1)**: Fires immediately after the
  inertia-advocate is written, before any other role. Blocks Phase 6 continuation if FAIL.
  Phase 7 INERTIA ANCHOR CHECK is retained as a second confirmation pass.
- **Axis-F -- Cross-role baseline spread**: LENS AUDIT gains a sixth item checking that
  each remaining role's lens.verify references at least one INERTIA BASELINE term (strength
  or gap). INERTIA ANCHOR CHECK extended with CROSS-ROLE SPREAD CHECK in Phase 7.

**Single-axis**: V-01 (Axis-D), V-02 (Axis-E), V-03 (Axis-F). **Two-axis combo**: V-04
(Axis-D + Axis-E). **Three-axis combo**: V-05 (Axis-D + Axis-E + Axis-F).

---

## V-01

**Variation axis**: Labeled strength terms -- INERTIA BASELINE with S1/S2/S3 and G1/G2/G3
**Hypothesis**: When INERTIA BASELINE strengths are listed as prose, the INERTIA ANCHOR
CHECK can pass on accidental verbatim overlap between generic phrases. Numbering each
strength as S1/S2/S3 and each gap as G1/G2/G3 and requiring the label-prefixed term to
appear verbatim in the inertia-advocate's lens.verify converts a heuristic check into an
auditable one. All 28 v11 mechanisms are preserved; the test is whether label-prefixed
anchoring produces cleaner verbatim propagation through Phase 4, Phase 5 Gap/Strength
column, Phase 6.1, and Phase 7 INERTIA ANCHOR CHECK.

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. Inertia-advocate is always included and written first.

Before defining any roles, establish the status quo: name the tool, process, or approach
teams currently use for this domain's need, its strengths, and its gaps. This INERTIA
BASELINE anchors every role. Roles without a gap to fill (or a strength to defend) do not
belong in this registry.

---

### PHASE 1 -- INPUT INVENTORY

Read all relevant files. Build the INPUT INVENTORY table:

  Row-ID | Source file | Excerpt (<=20 words)

Minimum 5 rows. Label the table INPUT INVENTORY. This is the sole citation source for
Phase 4 -- no field value may cite the CONVERGENCE SUMMARY or INERTIA BASELINE instead
of a row here.

EXIT GATE: INPUT INVENTORY COMPLETE (minimum 5 rows present)

---

### PHASE 2 -- INERTIA BASELINE + CONVERGENCE SUMMARY

Write two labeled artifacts:

INERTIA BASELINE (1-2 paragraphs):
  - Name the status quo solution.
  - List exactly 2-3 strengths using labeled format: S1: "{exact phrase}", S2: "{exact
    phrase}", S3: "{exact phrase}". Each label-phrase pair is an anchor term. Use specific
    language, not generic descriptors.
  - List exactly 2-3 gaps using labeled format: G1: "{exact phrase}", G2: "{exact phrase}",
    G3: "{exact phrase}". Each gap is a justification slot for a new role.

CONVERGENCE SUMMARY (1 paragraph):
  - Domain function, users, technical concerns, strategic context.

Both are framing artifacts. Phase 4 citations must trace to INPUT INVENTORY rows.
The S-labels and G-labels from INERTIA BASELINE are the canonical anchor terms for
forward-reference throughout Phases 3-7.

EXIT GATE: INERTIA BASELINE COMPLETE (name + S1-S3 + G1-G3 all present) +
           CONVERGENCE SUMMARY COMPLETE

---

### PHASE 3 -- CANDIDATE ROSTER

Enumerate at least 5 candidate roles. For each:
  - State which INERTIA BASELINE item it addresses (use the label: e.g., "defends S1", "addresses G2").
  - Assign provisional perspective (product / technical / inertia / domain / strategy / user)
  - Assign provisional scope (component / feature / system / cross-system / org)

The inertia-advocate's reason-to-exist is "defends S1 (and S2, S3)". Every other role's
reason references a G-label.

Table format: Candidate | Addresses (S/G label) | Perspective | Scope

EXIT GATE: CANDIDATE ROSTER COMPLETE (inertia-advocate present, all S/G labels assigned)

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

The inertia-advocate's lens.verify must include at least two INERTIA BASELINE strength
terms by their label-prefixed form: the verify question must name "S1: {exact phrase}"
and "S2: {exact phrase}" verbatim as the dimensions the proposal must beat.
Any field marked UNSUPPORTED must be revised before proceeding.

EXIT GATE: FRAME FILL COMPLETE (all candidates, all fields, all citations present;
           inertia-advocate lens.verify contains S-label terms)

---

### PHASE 5 -- PLANNING TABLE + DUAL GATE

Build planning table: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength

Planned-Vocab-Term: a domain-specific term that will appear verbatim in that role's lens
or expertise. Gap/Strength: must use S-label or G-label notation (e.g., "G2" or "defends
S1, S2"). The inertia-advocate's entry must read "defends S1, S2 (and S3 if present)".

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
Write the inertia-advocate role file. Its lens.verify must name at least two INERTIA
BASELINE strengths using their label-prefixed terms ("S1: {phrase}", "S2: {phrase}")
verbatim. Planned-Vocab-Term must appear verbatim in lens or expertise.
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
  strength labels and their exact terms (e.g., "S1: {phrase}", "S2: {phrase}") appear
  verbatim in that field. Partial label match (label without exact phrase, or exact phrase
  without label) does not count.
  If not: INERTIA ANCHOR CHECK FAIL -- revise file and re-run CHECK 1, 5A, 5B for the
  inertia-advocate.
  Emit: INERTIA ANCHOR CHECK: PASS/FAIL [labels found: {list}]

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

## V-02

**Variation axis**: Early INERTIA ANCHOR CHECK -- fires in PHASE 6 STEP 6.1 before any
other roles are written
**Hypothesis**: The current C-36 implementation fires INERTIA ANCHOR CHECK only in Phase 7.
If the inertia-advocate's lens.verify is missing INERTIA BASELINE strength terms, the error
is caught only after all other roles have been written, requiring cascade revisions. Moving
the check to immediately after Step 6.1 -- as a blocking gate before STEP 6.2 -- catches
the error at minimum cost. The Phase 7 INERTIA ANCHOR CHECK is retained as a confirmation
pass. All 28 v11 mechanisms are preserved; the only structural change is check timing.

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

  Row-ID | Source file | Excerpt (<=20 words)

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

Both are framing artifacts. Phase 4 citations must trace to INPUT INVENTORY rows.

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

The inertia-advocate's lens.verify must explicitly name at least two dimensions where
the status quo is strongest (exact terms from INERTIA BASELINE). Its lens.simplify must
name conditions under which the status quo is the right answer.
Any field marked UNSUPPORTED must be revised before proceeding.

EXIT GATE: FRAME FILL COMPLETE (all candidates, all fields, all citations present)

---

### PHASE 5 -- PLANNING TABLE + DUAL GATE

Build planning table: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength

Planned-Vocab-Term: a domain-specific term that will appear verbatim in that role's lens
or expertise. Gap/Strength: must match an item from INERTIA BASELINE.
The inertia-advocate's Gap/Strength entry must name which strength(s) it defends.

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

Immediately after writing, run the EARLY INERTIA ANCHOR CHECK before proceeding to
STEP 6.2:

  EARLY INERTIA ANCHOR CHECK:
  Re-read the written inertia-advocate file's lens.verify field. Confirm at least two
  INERTIA BASELINE strength terms appear verbatim in that field.
  If YES: emit EARLY INERTIA ANCHOR CHECK: PASS -- proceed to STEP 6.2.
  If NO: emit EARLY INERTIA ANCHOR CHECK: FAIL [{missing terms}] -- revise the
  inertia-advocate file now. Do not open STEP 6.2 until EARLY INERTIA ANCHOR CHECK: PASS.

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

EXIT GATE: EARLY INERTIA ANCHOR CHECK PASS + ALL ROLE FILES WRITTEN + ALL LENS AUDITS PASS

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
  Emit: INERTIA ANCHOR CHECK: PASS/FAIL [terms confirmed: {list}]

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

## V-03

**Variation axis**: Cross-role baseline spread -- INERTIA BASELINE terms must appear in
at least one non-inertia-advocate role's lens.verify
**Hypothesis**: The current INERTIA ANCHOR CHECK verifies only the inertia-advocate's
lens.verify. A registry where the inertia-advocate alone references the baseline is
structurally thin -- the baseline should shape the perspective of every expert role, not
just the defender role. Adding a CROSS-ROLE SPREAD CHECK to the LENS AUDIT (each role's
lens.verify must reference at least one INERTIA BASELINE term) and to Phase 7 (confirming
at least one non-inertia-advocate passes) validates that the INERTIA BASELINE has genuinely
influenced the registry. All 28 v11 mechanisms are preserved; the change extends C-36
to require distributed baseline propagation.

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

  Row-ID | Source file | Excerpt (<=20 words)

Minimum 5 rows. Label the table INPUT INVENTORY. This is the sole citation source for
Phase 4 -- no field value may cite the CONVERGENCE SUMMARY or INERTIA BASELINE instead
of a row here.

EXIT GATE: INPUT INVENTORY COMPLETE (minimum 5 rows present)

---

### PHASE 2 -- INERTIA BASELINE + CONVERGENCE SUMMARY

Write two labeled artifacts:

INERTIA BASELINE (1-2 paragraphs):
  - Name the status quo solution.
  - List 2-3 strengths it has that make it hard to displace. Use specific phrases that
    can be quoted verbatim in role lens.verify fields.
  - List 2-3 gaps it does not address (these become the justification for new roles).

CONVERGENCE SUMMARY (1 paragraph):
  - Domain function, users, technical concerns, strategic context.

Both are framing artifacts. Phase 4 citations must trace to INPUT INVENTORY rows.

EXIT GATE: INERTIA BASELINE COMPLETE + CONVERGENCE SUMMARY COMPLETE

---

### PHASE 3 -- CANDIDATE ROSTER

Enumerate at least 5 candidate roles. For each:
  - State which INERTIA BASELINE gap (or strength, for the inertia-advocate) it addresses.
  - Assign provisional perspective (product / technical / inertia / domain / strategy / user)
  - Assign provisional scope (component / feature / system / cross-system / org)

The inertia-advocate defends INERTIA BASELINE strengths. Every other role addresses one
or more INERTIA BASELINE gaps -- their lens.verify questions should reflect what the gap
demands of any proposal that claims to close it.

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
  lens.verify: {domain-specific questions -- must reference at least one INERTIA BASELINE
    term (strength or gap name) verbatim}
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

The inertia-advocate's lens.verify must name at least two INERTIA BASELINE strengths
by their exact terms. Each other role's lens.verify must name the INERTIA BASELINE gap
it addresses by its exact term from Phase 2.
Any field marked UNSUPPORTED must be revised before proceeding.

EXIT GATE: FRAME FILL COMPLETE (all candidates, all fields, all citations, all lens.verify
           fields contain at least one INERTIA BASELINE term)

---

### PHASE 5 -- PLANNING TABLE + DUAL GATE

Build planning table: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength

Planned-Vocab-Term: a domain-specific term that will appear verbatim in that role's lens
or expertise. Gap/Strength: must match an item from INERTIA BASELINE.

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
       - INERTIA BASELINE term in lens.verify: YES/NO + {term and field}
     Revise before proceeding if any item is NO.

EXIT GATE: ALL ROLE FILES WRITTEN + ALL LENS AUDITS PASS (including INERTIA BASELINE term
           item for each non-inertia-advocate role)

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
  Emit: INERTIA ANCHOR CHECK: PASS/FAIL [terms confirmed: {list}]

  CROSS-ROLE SPREAD CHECK:
  Scan the lens.verify field of every non-inertia-advocate written role. Confirm at least
  one such role contains an INERTIA BASELINE term (strength or gap) verbatim.
  If no non-inertia-advocate role references the baseline: CROSS-ROLE SPREAD CHECK FAIL --
  revise the weakest-anchored role's lens.verify and re-run CHECK 5A, 5B for that role.
  Emit: CROSS-ROLE SPREAD CHECK: PASS/FAIL [roles with baseline anchor: {list}]

EXIT GATE: ALL CHECKS PASS + INERTIA ANCHOR CHECK PASS + CROSS-ROLE SPREAD CHECK PASS

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

## V-04

**Variation axes**: Labeled strength terms (Axis-D) + Early INERTIA ANCHOR CHECK (Axis-E)
**Hypothesis**: Combining labeled S1/S2/S3 anchor terms with early Phase 6.1 detection
produces the strongest C-36 formulation: the labels make verbatim propagation non-accidental
(Axis-D), and the early check catches propagation failure before cascade revision cost
accumulates (Axis-E). The Phase 7 INERTIA ANCHOR CHECK becomes a confirmation pass for a
mechanism that was already validated in Phase 6. V-04 tests whether this combination of
structural precision (labels) and timing (early detection) is mutually reinforcing or
whether the added specificity in Phase 2 makes Phase 6.1 harder to satisfy without a
longer revision loop.

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. Inertia-advocate is always included and written first.

Before defining any roles, establish the status quo: name the tool, process, or approach
teams currently use for this domain's need. Label its strengths S1/S2/S3 and its gaps
G1/G2/G3. Every role justifies itself against a labeled gap; the inertia-advocate defends
the labeled strengths. Roles without a labeled gap to fill do not belong in this registry.

---

### PHASE 1 -- INPUT INVENTORY

Read all relevant files. Build the INPUT INVENTORY table:

  Row-ID | Source file | Excerpt (<=20 words)

Minimum 5 rows. Label the table INPUT INVENTORY. This is the sole citation source for
Phase 4 -- no field value may cite the CONVERGENCE SUMMARY or INERTIA BASELINE instead
of a row here.

EXIT GATE: INPUT INVENTORY COMPLETE (minimum 5 rows present)

---

### PHASE 2 -- INERTIA BASELINE + CONVERGENCE SUMMARY

Write two labeled artifacts:

INERTIA BASELINE (1-2 paragraphs):
  - Name the status quo solution.
  - List exactly 2-3 strengths using labeled format:
      S1: "{exact strength phrase}"
      S2: "{exact strength phrase}"
      S3: "{exact strength phrase}" (if applicable)
  - List exactly 2-3 gaps using labeled format:
      G1: "{exact gap phrase}"
      G2: "{exact gap phrase}"
      G3: "{exact gap phrase}" (if applicable)
  Use specific language for each label. Generic phrases ("flexible", "easy") do not
  constitute valid anchor terms. The S-labels and G-labels are canonical forward-reference
  identifiers used throughout Phases 3-7.

CONVERGENCE SUMMARY (1 paragraph):
  - Domain function, users, technical concerns, strategic context.

Both are framing artifacts. Phase 4 citations must trace to INPUT INVENTORY rows.

EXIT GATE: INERTIA BASELINE COMPLETE (name + S1-S3 labels + G1-G3 labels all present,
           each label has a specific non-generic phrase) + CONVERGENCE SUMMARY COMPLETE

---

### PHASE 3 -- CANDIDATE ROSTER

Enumerate at least 5 candidate roles. For each:
  - State the addressed item using its label (e.g., "defends S1, S2", "addresses G2").
  - Assign provisional perspective (product / technical / inertia / domain / strategy / user)
  - Assign provisional scope (component / feature / system / cross-system / org)

The inertia-advocate's addressed item must read "defends S1, S2 (and S3 if present)".
Every other candidate must reference at least one G-label.

Table format: Candidate | Addresses (S/G label) | Perspective | Scope

EXIT GATE: CANDIDATE ROSTER COMPLETE (inertia-advocate present, all S/G labels assigned,
           no candidate without a label)

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

The inertia-advocate's lens.verify must include at least two label-prefixed strength terms
verbatim (e.g., "S1: {exact phrase}" and "S2: {exact phrase}"). The verify questions
must be framed around whether any proposal beats the status quo on these labeled dimensions.
Any field marked UNSUPPORTED must be revised before proceeding.

EXIT GATE: FRAME FILL COMPLETE (all candidates, all fields, all citations present;
           inertia-advocate lens.verify contains at least two S-label terms verbatim)

---

### PHASE 5 -- PLANNING TABLE + DUAL GATE

Build planning table: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength

Planned-Vocab-Term: a domain-specific term that will appear verbatim in that role's lens
or expertise. Gap/Strength: must use S-label or G-label notation (e.g., "G1, G2" or
"defends S1, S2"). No entry may be blank or use prose without a label.

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
Write the inertia-advocate role file. Its lens.verify must include at least two S-label
terms verbatim ("S1: {exact phrase}", "S2: {exact phrase}"). Planned-Vocab-Term must
appear verbatim in lens or expertise.
Emit: INERTIA-ADVOCATE WRITTEN: {path}

Immediately after writing, run the EARLY INERTIA ANCHOR CHECK before opening STEP 6.2:

  EARLY INERTIA ANCHOR CHECK:
  Re-read the written inertia-advocate file's lens.verify field. Confirm at least two
  S-label terms (e.g., "S1: {phrase}", "S2: {phrase}") appear verbatim. Label alone
  without exact phrase does not pass. Exact phrase without label does not pass.
  If YES: emit EARLY INERTIA ANCHOR CHECK: PASS [labels confirmed: {list}] -- proceed.
  If NO: emit EARLY INERTIA ANCHOR CHECK: FAIL [missing: {list}] -- revise the
  inertia-advocate file now. Re-run this check. Do not open STEP 6.2 until PASS.

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

EXIT GATE: EARLY INERTIA ANCHOR CHECK PASS + ALL ROLE FILES WRITTEN + ALL LENS AUDITS PASS

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
  Re-read the inertia-advocate's lens.verify field. Confirm at least two S-label terms
  ("S1: {exact phrase}", "S2: {exact phrase}") appear verbatim. This is the confirmation
  pass for the EARLY INERTIA ANCHOR CHECK run in Phase 6.
  If not: INERTIA ANCHOR CHECK FAIL -- revise file and re-run CHECK 1, 5A, 5B.
  Emit: INERTIA ANCHOR CHECK: PASS/FAIL [S-labels confirmed: {list}]

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

**Variation axes**: Labeled strength terms (Axis-D) + Early INERTIA ANCHOR CHECK (Axis-E)
+ Cross-role baseline spread (Axis-F) -- full integration
**Hypothesis**: The three-axis combination is the most structurally hardened C-36
formulation: S-labels make anchor terms non-accidental (D), early detection prevents
cascade revision (E), and cross-role spread validates that the INERTIA BASELINE has
influenced the entire registry rather than just the inertia-advocate file (F). V-05 tests
whether the combination introduces execution overhead that causes LLMs to abbreviate
Phase 7 checks, or whether the layered structure reinforces compliance at each phase
boundary. If V-05 scores equal to V-04 (Axis-D + Axis-E), Axis-F is confirmed as an
independent addition. If it degrades, the three-axis combination has a brittleness that
needs decomposition.

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. Inertia-advocate is always included and written first.

Before defining any roles, establish the status quo: name the tool, process, or approach
teams currently use. Label its strengths S1/S2/S3 and its gaps G1/G2/G3. These labels
anchor every role: the inertia-advocate defends S-labels, all other roles address G-labels,
and at least one non-inertia-advocate role must reference an INERTIA BASELINE term in its
lens.verify. A registry where only the inertia-advocate touches the baseline is incomplete.

---

### PHASE 1 -- INPUT INVENTORY

Read all relevant files. Build the INPUT INVENTORY table:

  Row-ID | Source file | Excerpt (<=20 words)

Minimum 5 rows. Label the table INPUT INVENTORY. This is the sole citation source for
Phase 4 -- no field value may cite the CONVERGENCE SUMMARY or INERTIA BASELINE instead
of a row here.

EXIT GATE: INPUT INVENTORY COMPLETE (minimum 5 rows present)

---

### PHASE 2 -- INERTIA BASELINE + CONVERGENCE SUMMARY

Write two labeled artifacts:

INERTIA BASELINE (1-2 paragraphs):
  - Name the status quo solution.
  - List exactly 2-3 strengths using labeled format:
      S1: "{exact strength phrase}"
      S2: "{exact strength phrase}"
      S3: "{exact strength phrase}" (if applicable)
  - List exactly 2-3 gaps using labeled format:
      G1: "{exact gap phrase}"
      G2: "{exact gap phrase}"
      G3: "{exact gap phrase}" (if applicable)
  Use specific, quotable language. Generic phrases ("easy", "fast") invalidate the label.
  The S-labels and G-labels are canonical anchor identifiers for all downstream references.

CONVERGENCE SUMMARY (1 paragraph):
  - Domain function, users, technical concerns, strategic context.

Both are framing artifacts. Phase 4 citations must trace to INPUT INVENTORY rows.

EXIT GATE: INERTIA BASELINE COMPLETE (name + S1-S3 + G1-G3, each label non-generic) +
           CONVERGENCE SUMMARY COMPLETE

---

### PHASE 3 -- CANDIDATE ROSTER

Enumerate at least 5 candidate roles. For each:
  - State the addressed item using its label (e.g., "defends S1, S2", "addresses G1, G3").
  - Assign provisional perspective (product / technical / inertia / domain / strategy / user)
  - Assign provisional scope (component / feature / system / cross-system / org)
  - For non-inertia-advocate roles: note which INERTIA BASELINE term will appear verbatim
    in that role's lens.verify.

The inertia-advocate addresses "defends S1, S2 (and S3 if present)".

Table format: Candidate | Addresses (S/G label) | Perspective | Scope | Baseline term in lens

EXIT GATE: CANDIDATE ROSTER COMPLETE (inertia-advocate present, all labels assigned,
           at least one non-inertia-advocate role has a baseline term noted in lens column)

---

### PHASE 4 -- FRAME FILL

For each candidate, fill all five fields with a source citation per field:

  ROLE: {name}
  orientation.frame: {value}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  orientation.serves: {value}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  lens.verify: {domain-specific questions -- for the inertia-advocate: must include
    "S1: {phrase}" and "S2: {phrase}" verbatim; for all other roles: must include at
    least one INERTIA BASELINE term (S-label or G-label) verbatim}
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

Any field marked UNSUPPORTED must be revised before proceeding.

EXIT GATE: FRAME FILL COMPLETE (all candidates, all fields, all citations; inertia-advocate
           lens.verify has >=2 S-labels verbatim; at least one other role's lens.verify
           has at least one INERTIA BASELINE term verbatim)

---

### PHASE 5 -- PLANNING TABLE + DUAL GATE

Build planning table:
Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength | Baseline-term-in-lens

Planned-Vocab-Term: a domain-specific term appearing verbatim in lens or expertise.
Gap/Strength: S-label or G-label notation.
Baseline-term-in-lens: the specific INERTIA BASELINE term (S or G label + phrase) that
will appear in that role's lens.verify. For the inertia-advocate: "S1: {phrase}, S2:
{phrase}". For other roles: at least one term; may be NONE only if another role already
covers cross-role spread.

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
Write the inertia-advocate role file. Its lens.verify must include "S1: {exact phrase}"
and "S2: {exact phrase}" verbatim. Planned-Vocab-Term must appear verbatim.
Emit: INERTIA-ADVOCATE WRITTEN: {path}

Run EARLY INERTIA ANCHOR CHECK immediately after writing, before STEP 6.2:

  EARLY INERTIA ANCHOR CHECK:
  Re-read the written inertia-advocate file's lens.verify. Confirm at least two S-label
  terms appear verbatim (label + exact phrase required; neither alone is sufficient).
  If YES: emit EARLY INERTIA ANCHOR CHECK: PASS [labels: {list}] -- proceed to STEP 6.2.
  If NO: emit EARLY INERTIA ANCHOR CHECK: FAIL [missing: {list}] -- revise now.
  Do not open STEP 6.2 until EARLY INERTIA ANCHOR CHECK: PASS.

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
       - INERTIA BASELINE term in lens.verify: YES/NO + {label:phrase}
     Revise before proceeding if any item is NO.

EXIT GATE: EARLY INERTIA ANCHOR CHECK PASS + ALL ROLE FILES WRITTEN + ALL LENS AUDITS PASS
           (including INERTIA BASELINE term item for each non-inertia-advocate role)

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
  Re-read the inertia-advocate's lens.verify. Confirm at least two S-label terms appear
  verbatim (confirmation pass for EARLY INERTIA ANCHOR CHECK).
  If not: INERTIA ANCHOR CHECK FAIL -- revise and re-run CHECK 1, 5A, 5B.
  Emit: INERTIA ANCHOR CHECK: PASS/FAIL [S-labels: {list}]

  CROSS-ROLE SPREAD CHECK:
  Scan the lens.verify field of every non-inertia-advocate written role. Confirm at least
  one such role contains an INERTIA BASELINE term (any S-label or G-label + exact phrase)
  verbatim in its lens.verify.
  If no non-inertia-advocate role references the baseline: CROSS-ROLE SPREAD CHECK FAIL --
  identify the role whose Phase 3 "Baseline term in lens" column was non-NONE, revise its
  lens.verify, and re-run CHECK 5A, 5B for that role.
  Emit: CROSS-ROLE SPREAD CHECK: PASS/FAIL [anchored roles: {list with terms}]

EXIT GATE: ALL CHECKS PASS + INERTIA ANCHOR CHECK PASS + CROSS-ROLE SPREAD CHECK PASS

---

### ROLE-REPLACE SUB-PROCEDURE

Fires at CHECK 3B or CHECK 4B mismatch.

  planned: {planning table value for this role}
  written: {value found in written file}
  resolution: {one sentence}
  re-evaluation: {re-run CHECK 1, 3A, 4A, 5A, 5B, 6, 8, INERTIA ANCHOR CHECK, and
                  CROSS-ROLE SPREAD CHECK for this role; emit per-check result}

Emit: ROLE-REPLACE CONFIRMED: YES / NO
CHECK 3B and CHECK 4B stay FAIL for this role while ROLE-REPLACE CONFIRMED is NO.
```
