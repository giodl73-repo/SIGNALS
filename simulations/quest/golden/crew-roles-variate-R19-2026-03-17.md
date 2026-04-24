---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 19
rubric: crew-roles-rubric-v13-2026-03-17.md
---

# crew-roles -- Variate R19

5 complete prompt body variations for the `crew-roles` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

**Baseline**: R18 V-05 (Axis-G + Axis-H + Axis-F). Carries all 33 criteria including
C-39 (FRAME FILL PRE-ANCHOR CHECK in Phase 4 as blocking gate), C-40 (NON-GENERIC
REQUIREMENT with operational definition + NON-GENERIC CHECK in Phase 2 EXIT GATE),
C-41 (6th LENS AUDIT item + CROSS-ROLE SPREAD CHECK in Phase 7). v13 formula: /33 * 10.

**Gaps to probe in R19**: C-39, C-40, C-41 are now structural in the baseline. R19
stress-tests whether they survive under three surface-level structural variations not
previously tested:

- **Risk-6 -- Register shift**: Blocking gates use uppercase LABEL: PASS/FAIL format.
  The format creates enforcement authority -- LLMs treat uppercase colon-separated gate
  labels as non-optional checkpoints. Converting to direct prose ("check that...if not,
  revise before continuing") may soften the gate, letting LLMs treat it as advisory
  rather than blocking. Hypothesis: content survives register shift but gate authority
  weakens (Axis-I -- PHRASING REGISTER).

- **Risk-7 -- Phase compression**: Current formulation has 7 phases + explicit EXIT
  GATE labels + cross-phase back-references (Phase 7 INERTIA ANCHOR CHECK references
  "as validated at Phase 2 NON-GENERIC CHECK"). Compressing to 4 steps risks dropping
  cross-phase chain-of-custody references -- the explicit back-reference in Phase 7 to
  Phase 2 is what closes the definitional loop for C-40. Compression may break that
  chain without removing any mechanism (Axis-J -- LIFECYCLE COMPRESSION).

- **Risk-8 -- Inertia front-loading**: C-39 places the FRAME FILL PRE-ANCHOR CHECK
  in Phase 4, after Phase 3 (candidate roster). Promoting the inertia-advocate's
  entire FRAME FILL to Phase 2 (before candidates are enumerated) converts the Phase 4
  check to a Phase 2 ANCHOR VALIDATION. The three-checkpoint chain becomes Phase 2
  (detection) -> Phase 6.1 (confirmation) -> Phase 7 (final). This is structurally
  stronger but deviates from the rubric's "Phase 4" placement of C-39. Hypothesis:
  front-loading strengthens the mechanism but may technically conflict with C-39's
  "in Phase 4" specification (Axis-K -- INERTIA FRONT-LOADING).

**Single-axis**: V-01 (Axis-I), V-02 (Axis-J), V-03 (Axis-K).
**Two-axis**: V-04 (Axis-I + Axis-J). **Three-axis**: V-05 (Axis-I + Axis-J + Axis-K).

---

## V-01

**Variation axis**: PHRASING REGISTER -- convert uppercase gate labels to direct
imperative prose
**Hypothesis**: Uppercase labels (FRAME FILL PRE-ANCHOR CHECK: PASS, NON-GENERIC CHECK,
CROSS-ROLE SPREAD CHECK) create enforcement authority by signaling to LLMs that these
are required protocol steps. Expressing the same gates as natural prose sentences
("after writing the inertia-advocate, check that lens.verify contains... if not,
revise before continuing") may soften perceived authority. All 33 mechanisms are
content-identical; the test is whether prose register preserves gate enforcement or
degrades it from blocking to advisory.

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. The inertia-advocate is always included and written first. Roles
without a gap to fill (or a strength to defend) do not belong in this registry.

---

### Phase 1 -- Input Inventory

Read all relevant files. Build a table labeled INPUT INVENTORY:

  Row-ID | Source file | Excerpt (<=20 words)

Include at least 5 rows. This table is the sole citation source for Phase 4 field
values -- no field may cite the convergence summary or inertia baseline as its source.

Do not proceed to Phase 2 until at least 5 rows are present.

---

### Phase 2 -- Inertia Baseline and Convergence Summary

Write two labeled artifacts:

INERTIA BASELINE (1-2 paragraphs):
  - Name the status quo solution.
  - List exactly 2-3 strengths in labeled format: S1: "{exact phrase}", S2: "{exact
    phrase}", S3: "{exact phrase}". Each is a canonical anchor term.
  - List exactly 2-3 gaps in labeled format: G1: "{exact phrase}", G2: "{exact phrase}",
    G3: "{exact phrase}". Each is a justification slot for a new role.

Before writing any S-phrase, apply this specificity test: a phrase is non-generic if
and only if it contains at least one noun or verb specific to this domain and cannot
appear unchanged in a different domain's INERTIA BASELINE. These phrases fail regardless
of context: "easy to use", "fast", "reliable", "well-known", "familiar", "low cost",
"widely adopted", "stable", "flexible". Apply the same test to G-phrases. If any phrase
fails, revise it before continuing. Confirm every S-phrase and G-phrase passes before
leaving Phase 2 -- this confirmation is the non-generic check that Phase 7 will
reference back to.

CONVERGENCE SUMMARY (1 paragraph): domain function, users, technical concerns,
strategic context.

Do not proceed to Phase 3 until: INERTIA BASELINE is complete (name + S1-S3 + G1-G3),
every S-phrase and G-phrase passes the specificity test above, and CONVERGENCE SUMMARY
is written.

---

### Phase 3 -- Candidate Roster

Enumerate at least 5 candidate roles. For each:
  - State which INERTIA BASELINE item it addresses (label: "defends S1", "addresses G2").
  - Assign provisional perspective (product / technical / inertia / domain / strategy / user)
  - Assign provisional scope (component / feature / system / cross-system / org)

The inertia-advocate's reason-to-exist is "defends S1 (and S2, S3)". Every other role's
reason must reference at least one G-label.

Table: Candidate | Addresses (S/G label) | Perspective | Scope

Do not proceed to Phase 4 until the inertia-advocate is present and every row has an
S/G label assigned.

---

### Phase 4 -- Frame Fill

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

The inertia-advocate's lens.verify must include at least two entries of the form
"S{N}: {exact phrase from INERTIA BASELINE}" using the labels from Phase 2.

For remaining roles, if the candidate's G-label maps to an INERTIA BASELINE gap, the
lens.verify should include at least one "G{N}: {phrase}" reference. This is advisory
here and enforced at the Phase 6 lens audit.

Fill the inertia-advocate's block first. After writing it, before filling any other
role, do this check: read back the inertia-advocate lens.verify text just written and
confirm it contains at least one entry in the form "S{N}: {phrase}" where S{N} is a
label from INERTIA BASELINE and {phrase} is the exact domain-specific phrase confirmed
non-generic in Phase 2. If yes, continue to the remaining roles. If no, revise the
inertia-advocate lens.verify in this block -- do not fill any other role's frame fill
until the inertia-advocate lens.verify contains a qualifying S-label entry.

After that check passes, complete frame fill for all remaining candidates. Any field
you cannot support from the input inventory must be revised before proceeding.

Do not proceed to Phase 5 until all candidates have complete frame fill with citations
and the inertia-advocate lens.verify check passed.

---

### Phase 5 -- Planning Table and Dual Gate

Build the planning table:

  Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength

Planned-Vocab-Term: a domain-specific term that will appear verbatim in the written
file's lens or expertise. Gap/Strength: must match a label from INERTIA BASELINE.

Run both audits before proceeding:
  Scope audit: count distinct Scope values. Fewer than 2 -- expand or reassign, then
  re-count. Two or more -- proceed.
  Perspective audit: count distinct Perspective values. Fewer than 3 -- add roles or
  reassign, then re-count. Three or more -- proceed.

Do not proceed to Phase 6 until both audits show passing counts.

---

### Phase 6 -- Write Role Files

Step 6.1 -- Write the inertia-advocate first.

Write the inertia-advocate role file using its Phase 4 frame fill values. Its
lens.verify must include at least one "S{N}: {phrase}" entry verbatim from INERTIA
BASELINE (the same domain-specific phrase confirmed non-generic in Phase 2).
Planned-Vocab-Term must appear verbatim in lens or expertise.
Emit: INERTIA-ADVOCATE WRITTEN: {path}

After writing the file, re-read the inertia-advocate's lens.verify. Confirm at least
one "S{N}: {phrase}" entry appears verbatim (label + exact domain-specific phrase from
INERTIA BASELINE). If yes, proceed to Step 6.2. If no, revise the inertia-advocate
file and re-read before starting Step 6.2. Note: if the Phase 4 inertia-advocate
lens.verify check passed correctly, this re-read should be a confirmation not a
correction. Do not start Step 6.2 until this confirmation is complete.

Step 6.2 -- Write remaining roles in planning table order.

For each remaining role:
  a. Write the file using Phase 4 frame fill values. Planned-Vocab-Term must appear
     verbatim.
  b. Confirm collaborates_with includes the inertia-advocate by name.
  c. Check these items before writing the next role:
       - Is verify[1] domain-specific? Yes / No + evidence
       - Is verify[2] domain-specific? Yes / No + evidence
       - Is simplify[1] a concrete cut rule? Yes / No + evidence
       - Does Planned-Vocab-Term appear verbatim? Yes / No + location
       - Does collaborates_with include the inertia-advocate? Yes / No
       - Does lens.verify reference at least one INERTIA BASELINE term
         (S or G label + phrase from Phase 2)? Yes / No + which term
     Revise the file if any answer is No before writing the next role.

Do not proceed to Phase 7 until all role files are written and all check items above
show Yes for every role.

---

### Phase 7 -- Verification Checks

Emit each check result before running the next.

  Check 1: Field completeness per file. Emit per file: PASS or FAIL [missing field]
  Check 2: Inertia-advocate present with orientation = "status-quo advocate".
    Emit: PASS or FAIL
  Check 3A: Scope spread from written files >= 2. Emit: PASS or FAIL [N distinct]
  Check 3B: Written scope matches planning table. Run role-replace sub-procedure if
    mismatch.
  Check 4A: All planning table roles written. Emit: PASS or FAIL
  Check 4B: Planned-Vocab-Terms present verbatim in written files. Run role-replace
    sub-procedure if mismatch.
  Check 5A: Written field values match frame fill per role. Emit per role.
  Check 5B: Phase 1 source citations verifiable per field. Emit per violation:
    [{role}.{field}: citation missing or unverifiable]
  Check 6: No generic placeholders remain. Emit: PASS or FAIL [N flags]
  Check 7: All files are at .roles/{domain}/. Emit: PASS or FAIL
  Check 8: Perspective spread from written files >= 3. Emit: PASS or FAIL [N distinct]

  Inertia anchor check: re-read the inertia-advocate's lens.verify field. Confirm at
  least one "S{N}: {phrase}" entry appears verbatim (label + exact domain-specific
  phrase, as confirmed non-generic in Phase 2). If not, revise the file and re-run
  Check 1, 5A, 5B for the inertia-advocate. Emit: PASS or FAIL.

  Cross-role spread check: for each non-inertia-advocate role, re-read its written
  lens.verify. Count how many reference at least one INERTIA BASELINE term (S or G
  label + phrase from Phase 2). If that count is zero, at least one non-inertia-advocate
  role must be revised to reference a baseline term before closing. Emit: PASS or FAIL
  [N non-inertia roles with baseline reference, list them].

Do not close until all checks pass, the inertia anchor check passes, and the cross-role
spread check passes.

---

### Role-Replace Sub-Procedure

Fires when Check 3B or Check 4B finds a mismatch.

  planned: {planning table value for this role}
  written: {value found in written file}
  resolution: {one sentence}
  re-evaluation: {re-run Check 1, 3A, 4A, 5A, 5B, 6, 8, inertia anchor check, and
                  cross-role spread check for this role; emit per-check result}

Emit: ROLE-REPLACE CONFIRMED: YES / NO
Check 3B and Check 4B stay failed for this role while CONFIRMED is NO.
```

---

## V-02

**Variation axis**: LIFECYCLE COMPRESSION -- collapse 7 phases to 4 steps while
preserving all 33 mechanisms
**Hypothesis**: The cross-phase chain-of-custody for C-40 depends on Phase 7 INERTIA
ANCHOR CHECK explicitly naming "as validated at Phase 2 NON-GENERIC CHECK." Compressing
to 4 numbered steps replaces phase numbers with step numbers, which may break the
back-reference chain if the LLM uses the new step numbers inconsistently. Additionally,
compressing EXIT GATE labels into inline step completions risks making the FRAME FILL
PRE-ANCHOR CHECK (C-39) appear as part of a run-on instruction block rather than a
clearly-scoped blocking gate. All mechanisms are present; the test is whether the
chain-of-custody and gate authority survive compaction.

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. The inertia-advocate is always included and written first. Roles
without a gap to fill (or a strength to defend) do not belong in this registry.

---

### STEP 1 -- INVENTORY AND BASELINE

Read all relevant files. Produce three artifacts before proceeding to STEP 2.

INPUT INVENTORY: table of Row-ID | Source file | Excerpt (<=20 words). Minimum 5 rows.
This table is the sole citation source for STEP 2 frame fill values.

INERTIA BASELINE: name the status quo solution. List exactly 2-3 strengths: S1: "{exact
phrase}", S2: "{exact phrase}", S3: "{exact phrase}". List exactly 2-3 gaps: G1: "{exact
phrase}", G2: "{exact phrase}", G3: "{exact phrase}". Each label-phrase pair is a
canonical anchor term for forward-reference in STEPS 2-4.

NON-GENERIC REQUIREMENT: each S-phrase must contain at least one noun or verb specific
to this domain that cannot appear unchanged in a different domain's INERTIA BASELINE.
These phrases fail this test regardless of context: "easy to use", "fast", "reliable",
"well-known", "familiar", "low cost", "widely adopted", "stable", "flexible". Apply the
same test to G-phrases. Revise any failing phrase before continuing. Confirm all phrases
pass; emit: NON-GENERIC CHECK: PASS before proceeding. STEP 3 INERTIA ANCHOR CHECK will
reference the phrases validated here.

CONVERGENCE SUMMARY: one paragraph covering domain function, users, technical concerns,
and strategic context.

EXIT GATE: INPUT INVENTORY >= 5 rows + INERTIA BASELINE complete (name + S1-S3 + G1-G3)
+ NON-GENERIC CHECK PASS + CONVERGENCE SUMMARY written.

---

### STEP 2 -- CANDIDATES AND FRAME FILL

CANDIDATE ROSTER: enumerate at least 5 candidates. For each: the INERTIA BASELINE label
it addresses (e.g., "defends S1", "addresses G2"), provisional perspective (product /
technical / inertia / domain / strategy / user), provisional scope (component / feature
/ system / cross-system / org). The inertia-advocate's reason-to-exist is "defends S1
(and S2, S3)"; every other role must reference at least one G-label.
Table: Candidate | Addresses (S/G label) | Perspective | Scope

FRAME FILL: for each candidate, fill all five fields with one Phase 1 source citation
per field (format: `Phase 1 source: {row-id} = "{verbatim phrase}"`):
  orientation.frame | orientation.serves | lens.verify | lens.simplify |
  expertise.depth | expertise.relevance | scope | collaborates_with (2-3 named roles)

The inertia-advocate's lens.verify must include at least two entries of the form
"S{N}: {exact phrase from INERTIA BASELINE}" using STEP 1 labels. Fill the
inertia-advocate's block first. Then, before filling any other role, run this check:

  FRAME FILL PRE-ANCHOR CHECK:
  Re-read the inertia-advocate FRAME FILL lens.verify just written. Confirm at least one
  "S{N}: {phrase}" entry is present where {phrase} is the exact domain-specific phrase
  as validated at STEP 1 NON-GENERIC CHECK.
    FRAME FILL PRE-ANCHOR CHECK: PASS -- proceed to remaining roles.
    FRAME FILL PRE-ANCHOR CHECK: FAIL -- revise the inertia-advocate lens.verify in this
    block; do not start any other role's frame fill while this check is FAIL.

For remaining roles, if the candidate's G-label maps to an INERTIA BASELINE gap, the
lens.verify should include at least one "G{N}: {phrase}" reference (advisory here,
enforced at STEP 3 lens audit).

EXIT GATE: CANDIDATE ROSTER complete + FRAME FILL complete (all candidates, all fields,
all citations) + FRAME FILL PRE-ANCHOR CHECK PASS.

---

### STEP 3 -- PLAN AND WRITE

PLANNING TABLE: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength.
Planned-Vocab-Term appears verbatim in the written file's lens or expertise.
Gap/Strength matches a label from INERTIA BASELINE.

SCOPE AUDIT: count distinct Scope values. < 2: fail, expand or reassign. >= 2: pass.
PERSPECTIVE AUDIT: count distinct Perspective values. < 3: fail, add or reassign. >= 3:
pass. Both audits must pass before writing any role file.

WRITE INERTIA-ADVOCATE (first):
Write the file from STEP 2 frame fill values. lens.verify must include at least one
"S{N}: {phrase}" entry verbatim from INERTIA BASELINE (same phrase validated at STEP 1
NON-GENERIC CHECK). Planned-Vocab-Term must appear verbatim.
Emit: INERTIA-ADVOCATE WRITTEN: {path}

EARLY INERTIA ANCHOR CHECK (blocking gate): re-read the inertia-advocate's written
lens.verify. Confirm at least one "S{N}: {phrase}" entry appears verbatim (label +
exact domain-specific phrase from INERTIA BASELINE). If STEP 2 FRAME FILL PRE-ANCHOR
CHECK PASS was correctly emitted, this is confirmation.
  EARLY INERTIA ANCHOR CHECK: PASS -- proceed to remaining roles.
  EARLY INERTIA ANCHOR CHECK: FAIL -- revise file and re-check before proceeding.
Remaining roles are blocked until EARLY INERTIA ANCHOR CHECK PASS.

WRITE REMAINING ROLES in planning table order. For each:
  a. Write the file from STEP 2 frame fill values. Planned-Vocab-Term must appear verbatim.
  b. Confirm collaborates_with includes the inertia-advocate by name.
  c. Emit inline LENS AUDIT:
     LENS AUDIT [{role-name}]:
       - verify[1] domain-specific: YES/NO + evidence
       - verify[2] domain-specific: YES/NO + evidence
       - simplify[1] concrete cut: YES/NO + evidence
       - Planned-Vocab-Term verbatim: YES/NO + location
       - collaborates_with inertia-advocate: YES/NO
       - references INERTIA BASELINE term (S or G label + phrase): YES/NO + which term
     Revise before writing the next role if any item is NO.

EXIT GATE: SCOPE AUDIT PASS + PERSPECTIVE AUDIT PASS + all role files written + all
lens audits pass.

---

### STEP 4 -- VERIFY

Emit each check result before running the next.

  CHECK 1: Field completeness per file. Emit: CHECK 1 [{filename}]: PASS/FAIL [{field}]
  CHECK 2: Inertia-advocate present, orientation = "status-quo advocate". PASS/FAIL
  CHECK 3A: Scope spread >= 2. PASS/FAIL [N distinct]
  CHECK 3B: Written scope matches planning table. Fire ROLE-REPLACE if mismatch.
  CHECK 4A: All planning table roles written. PASS/FAIL
  CHECK 4B: Planned-Vocab-Terms verbatim in written files. Fire ROLE-REPLACE if mismatch.
  CHECK 5A: Written fields match frame fill per role. Emit per role.
  CHECK 5B: STEP 1 citations verifiable per field.
    Emit per violation: [{role}.{field}: CITATION FAIL]
  CHECK 6: No generic placeholders. PASS/FAIL [N flags]
  CHECK 7: All files at .roles/{domain}/. PASS/FAIL
  CHECK 8: Perspective spread >= 3. PASS/FAIL [N distinct]

  INERTIA ANCHOR CHECK (final validation):
  Re-read the inertia-advocate's lens.verify. Confirm at least one "S{N}: {phrase}"
  entry verbatim (label + exact phrase, as validated at STEP 1 NON-GENERIC CHECK). If
  not: revise file and re-run CHECK 1, 5A, 5B for the inertia-advocate.
  Emit: INERTIA ANCHOR CHECK: PASS/FAIL

  CROSS-ROLE SPREAD CHECK:
  For each non-inertia-advocate role, count how many reference at least one INERTIA
  BASELINE term (S or G label + phrase from STEP 1). If count = 0: FAIL -- at least
  one non-inertia-advocate role must reference an INERTIA BASELINE term verbatim.
  Emit: CROSS-ROLE SPREAD CHECK: PASS/FAIL [N non-inertia roles with baseline reference,
        list them]

EXIT GATE: all checks pass + INERTIA ANCHOR CHECK PASS + CROSS-ROLE SPREAD CHECK PASS.

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

---

## V-03

**Variation axis**: INERTIA FRONT-LOADING -- promote inertia-advocate's complete
FRAME FILL to Phase 2 (before candidate roster)
**Hypothesis**: C-39 places the FRAME FILL PRE-ANCHOR CHECK after the inertia-advocate's
FRAME FILL in Phase 4, before continuing to other roles. The intent is catching label
omission before Phase 5 and Phase 6 are built. Front-loading goes further: by completing
the inertia-advocate's FRAME FILL in Phase 2 -- before Phase 3 candidates are enumerated
-- the anchor is established even before the planning table is conceived. The Phase 2
ANCHOR VALIDATION (equivalent to Phase 4 FRAME FILL PRE-ANCHOR CHECK) fires earlier,
giving Phase 6.1 EARLY INERTIA ANCHOR CHECK a longer confirmation window. The structural
question: does "Phase 2" placement satisfy C-39's "in Phase 4" specification, or does
the rubric require the check to fire within the Phase 4 block specifically?

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. The inertia-advocate is always included and written first. Roles
without a gap to fill (or a strength to defend) do not belong in this registry.

---

### PHASE 1 -- INPUT INVENTORY

Read all relevant files. Build the INPUT INVENTORY table:

  Row-ID | Source file | Excerpt (<=20 words)

Minimum 5 rows. Label the table INPUT INVENTORY. This is the sole citation source for
all FRAME FILL values -- no field value may cite the CONVERGENCE SUMMARY or INERTIA
BASELINE instead of a row here.

EXIT GATE: INPUT INVENTORY COMPLETE (minimum 5 rows present)

---

### PHASE 2 -- INERTIA BASELINE + INERTIA-ADVOCATE FRAME FILL

This phase fully defines the inertia-advocate before any other role is enumerated.
The anchor is committed here; Phases 3-6 build around it.

Step 2.1 -- Write INERTIA BASELINE (1-2 paragraphs):
  - Name the status quo solution.
  - List exactly 2-3 strengths: S1: "{exact phrase}", S2: "{exact phrase}",
    S3: "{exact phrase}". Each label-phrase pair is a canonical anchor term.
  - List exactly 2-3 gaps: G1: "{exact phrase}", G2: "{exact phrase}",
    G3: "{exact phrase}". Each gap is a justification slot for a new role.

NON-GENERIC REQUIREMENT: each S-phrase must contain at least one noun or verb specific
to this domain and cannot appear unchanged in a different domain's INERTIA BASELINE.
These phrases fail regardless of context: "easy to use", "fast", "reliable",
"well-known", "familiar", "low cost", "widely adopted", "stable", "flexible". Apply
the same test to G-phrases. If any phrase fails, revise before continuing.

NON-GENERIC CHECK: confirm each S-phrase and G-phrase passes the domain-specificity
test. Record the validated phrase for each label -- these are the anchor terms that
all forward-references must use verbatim.
Emit: NON-GENERIC CHECK: PASS (with each validated S-label: phrase and G-label: phrase)

Step 2.2 -- Write CONVERGENCE SUMMARY (1 paragraph): domain function, users, technical
concerns, strategic context.

Step 2.3 -- Fill INERTIA-ADVOCATE FRAME FILL:
  ROLE: inertia-advocate
  orientation.frame: status-quo advocate; evaluates proposals against established {S1 phrase}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  orientation.serves: {value}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  lens.verify: must include at least two entries in the form "S{N}: {exact phrase}"
    using labels defined at Step 2.1 -- e.g.:
    S1: "{exact phrase from INERTIA BASELINE, as validated at Step 2.1 NON-GENERIC CHECK}"
    S2: "{exact phrase from INERTIA BASELINE, as validated at Step 2.1 NON-GENERIC CHECK}"
    {additional domain-specific verify questions}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  lens.simplify: {concrete cut rules}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  expertise.depth: {specific knowledge}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  expertise.relevance: {why this domain needs it}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  scope: {scope value}
    Phase 1 source: {row-id} = "{verbatim phrase}"
  collaborates_with: {2-3 role names -- placeholder names acceptable; resolve in Phase 3}
    Phase 1 source: {row-id} = "{verbatim phrase}"

Step 2.4 -- PHASE 2 ANCHOR VALIDATION (blocking gate):
Re-read the inertia-advocate FRAME FILL lens.verify just written. Confirm at least one
"S{N}: {phrase}" entry is present where S{N} is a label from INERTIA BASELINE and
{phrase} is the exact domain-specific phrase validated at Step 2.1 NON-GENERIC CHECK.
  PHASE 2 ANCHOR VALIDATION: PASS -- proceed to Phase 3.
  PHASE 2 ANCHOR VALIDATION: FAIL -- revise the inertia-advocate FRAME FILL lens.verify
  before proceeding to Phase 3. The inertia-advocate must be fully anchored before any
  other role is enumerated.

EXIT GATE: INERTIA BASELINE COMPLETE + NON-GENERIC CHECK PASS + CONVERGENCE SUMMARY
COMPLETE + INERTIA-ADVOCATE FRAME FILL COMPLETE + PHASE 2 ANCHOR VALIDATION PASS

---

### PHASE 3 -- CANDIDATE ROSTER (other roles only)

Enumerate at least 4 additional candidate roles (the inertia-advocate is committed in
Phase 2). For each:
  - State which INERTIA BASELINE item it addresses (label: "addresses G1", "addresses G2").
  - Assign provisional perspective (product / technical / domain / strategy / user)
  - Assign provisional scope (component / feature / system / cross-system / org)

Every candidate must reference at least one G-label. Update collaborates_with in the
inertia-advocate FRAME FILL if placeholder names can now be resolved.

Table: Candidate | Addresses (G-label) | Perspective | Scope

EXIT GATE: CANDIDATE ROSTER COMPLETE (minimum 4 candidates, all G-labels assigned)

---

### PHASE 4 -- FRAME FILL (other roles only)

For each candidate from Phase 3, fill all five fields with a Phase 1 source citation
per field:

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
  collaborates_with: {2-3 named roles, must include inertia-advocate}
    Phase 1 source: {row-id} = "{verbatim phrase}"

If the role's G-label maps to an INERTIA BASELINE gap, include at least one
"G{N}: {phrase}" reference in lens.verify (advisory here, enforced by LENS AUDIT in
Phase 6). Any field marked UNSUPPORTED must be revised before proceeding.

EXIT GATE: FRAME FILL COMPLETE (all Phase 3 candidates, all fields, all citations)

---

### PHASE 5 -- PLANNING TABLE + DUAL GATE

Build planning table including the inertia-advocate (from Phase 2) and all Phase 3
candidates:

  Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength

Planned-Vocab-Term: a domain-specific term that will appear verbatim in the written
file's lens or expertise. Gap/Strength: must match a label from INERTIA BASELINE.

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
Write the inertia-advocate role file using its Phase 2 FRAME FILL values. Its
lens.verify must include at least one "S{N}: {phrase}" entry verbatim from INERTIA
BASELINE (the same phrase validated at Phase 2 NON-GENERIC CHECK). Planned-Vocab-Term
must appear verbatim in lens or expertise.
Emit: INERTIA-ADVOCATE WRITTEN: {path}

EARLY INERTIA ANCHOR CHECK (blocking gate):
Re-read the inertia-advocate's written lens.verify. Confirm at least one "S{N}: {phrase}"
entry appears verbatim (label + exact domain-specific phrase from INERTIA BASELINE).
  EARLY INERTIA ANCHOR CHECK: PASS -- proceed to STEP 6.2.
  EARLY INERTIA ANCHOR CHECK: FAIL -- revise inertia-advocate and re-check before
  STEP 6.2. Since Phase 2 ANCHOR VALIDATION already confirmed this pattern in the FRAME
  FILL, this check should confirm file fidelity, not discover a new omission.
STEP 6.2 is blocked until EARLY INERTIA ANCHOR CHECK PASS.

STEP 6.2 -- REMAINING ROLES
For each remaining role in planning table order:
  a. Write the file using Phase 4 FRAME FILL values. Planned-Vocab-Term must appear
     verbatim.
  b. Confirm collaborates_with includes the inertia-advocate by name.
  c. Emit inline LENS AUDIT:
     LENS AUDIT [{role-name}]:
       - verify[1] domain-specific: YES/NO + evidence
       - verify[2] domain-specific: YES/NO + evidence
       - simplify[1] concrete cut: YES/NO + evidence
       - Planned-Vocab-Term verbatim: YES/NO + location
       - collaborates_with inertia-advocate: YES/NO
       - references INERTIA BASELINE term (S or G label + phrase): YES/NO + which term
     Revise before proceeding if any item is NO.

EXIT GATE: ALL ROLE FILES WRITTEN + ALL LENS AUDITS PASS

---

### PHASE 7 -- VERIFICATION CHECKS

Emit each check result before running the next.

  CHECK 1: Field completeness per file. Emit: CHECK 1 [{filename}]: PASS / FAIL [{field}]
  CHECK 2: Inertia-advocate exists (orientation = "status-quo advocate"). CHECK 2: PASS/FAIL
  CHECK 3A: Scope spread from written files >= 2. CHECK 3A: PASS/FAIL [N distinct]
  CHECK 3B: Written scope matches planning table. Fire ROLE-REPLACE if mismatch.
  CHECK 4A: All planning table roles written. CHECK 4A: PASS/FAIL
  CHECK 4B: Planned-Vocab-Terms present verbatim. Fire ROLE-REPLACE if mismatch.
  CHECK 5A: Written fields match Frame Fill per role. Emit per role.
  CHECK 5B: Phase 1 source citations verifiable per field.
    Emit: [{role}.{field}: Phase 1 source missing or unverifiable -- CITATION FAIL]
  CHECK 6: No generic placeholders. CHECK 6: PASS/FAIL [N flags]
  CHECK 7: All files at .roles/{domain}/. CHECK 7: PASS/FAIL
  CHECK 8: Perspective spread from written files >= 3. CHECK 8: PASS/FAIL [N distinct]

  INERTIA ANCHOR CHECK (final validation):
  Re-read the inertia-advocate's lens.verify field. Confirm at least one "S{N}: {phrase}"
  entry appears verbatim (label + exact domain-specific phrase, as validated at Phase 2
  NON-GENERIC CHECK). If not: INERTIA ANCHOR CHECK FAIL -- revise file and re-run
  CHECK 1, 5A, 5B for the inertia-advocate.
  Emit: INERTIA ANCHOR CHECK: PASS/FAIL

  CROSS-ROLE SPREAD CHECK:
  For each non-inertia-advocate role, re-read its written lens.verify. Count how many
  reference at least one INERTIA BASELINE term (S or G label + phrase from Phase 2).
  If count = 0: CROSS-ROLE SPREAD CHECK FAIL -- at least one non-inertia-advocate role
  must reference an INERTIA BASELINE term verbatim.
  Emit: CROSS-ROLE SPREAD CHECK: PASS/FAIL [N non-inertia roles with baseline reference,
        list them]

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

---

## V-04

**Variation axes**: PHRASING REGISTER (Axis-I) + LIFECYCLE COMPRESSION (Axis-J)
**Hypothesis**: Axis-I and Axis-J compound rather than cancel. Axis-I softens gate
authority by removing uppercase labels; Axis-J removes explicit phase boundaries that
separate gate scopes. Together they risk collapsing the three-checkpoint chain for
C-39 (the phase transitions that give each checkpoint distinct identity: Phase 4
detection -> Phase 6.1 confirmation -> Phase 7 final) into an undifferentiated list
of prose instructions where LLMs may perform all three as one sweep. The cross-phase
back-reference for C-40 ("as confirmed non-generic in Step 1") is retained but appears
in a lower-authority register. Combined test: does the mechanism survive when both
structural identity and phrasing authority are reduced simultaneously?

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. The inertia-advocate is always included and written first. Roles
without a gap to fill (or a strength to defend) do not belong in this registry.

---

### Step 1 -- Inventory and Baseline

Read all relevant files. Produce three artifacts before moving to Step 2.

Build a table labeled INPUT INVENTORY with columns Row-ID | Source file |
Excerpt (<=20 words). Include at least 5 rows. This table is the only citation source
for Step 2 frame fill values -- no field may cite the convergence summary or inertia
baseline as its source. Do not proceed to Step 2 until 5+ rows are present.

Write the INERTIA BASELINE. Name the status quo solution. List exactly 2-3 strengths
in labeled format: S1: "{exact phrase}", S2: "{exact phrase}", S3: "{exact phrase}".
List exactly 2-3 gaps: G1: "{exact phrase}", G2: "{exact phrase}", G3: "{exact phrase}".
Each is a canonical anchor term for forward-reference in Steps 2-4.

Before committing any S-phrase, apply this test: a phrase is non-generic if and only
if it contains at least one noun or verb specific to this domain and cannot appear
unchanged in a different domain's INERTIA BASELINE. These phrases fail the test: "easy
to use", "fast", "reliable", "well-known", "familiar", "low cost", "widely adopted",
"stable", "flexible". Apply the same test to G-phrases. If any phrase fails, revise
it. Confirm all phrases pass this non-generic test and record which phrases were
validated -- Step 4 inertia anchor check will reference these specific validated phrases.

Write the CONVERGENCE SUMMARY: one paragraph on domain function, users, technical
concerns, and strategic context.

Do not move to Step 2 until all three artifacts are complete and every S-phrase and
G-phrase has been confirmed non-generic.

---

### Step 2 -- Candidates and Frame Fill

List at least 5 candidate roles. For each: the INERTIA BASELINE label it addresses
(e.g., "defends S1", "addresses G2"), provisional perspective, provisional scope. The
inertia-advocate's reason-to-exist is "defends S1 (and S2, S3)"; every other role must
reference at least one G-label. Table: Candidate | Label | Perspective | Scope. Do not
continue until the inertia-advocate is present and every row has a label.

Fill frame fill blocks for all candidates, inertia-advocate first. For each, provide
all five fields with one Step 1 source citation per field:
  orientation.frame / orientation.serves / lens.verify / lens.simplify /
  expertise.depth / expertise.relevance / scope / collaborates_with (2-3 named roles)

The inertia-advocate's lens.verify must include at least two entries: "S{N}: {exact
phrase from INERTIA BASELINE}" using the labels from Step 1. After writing the
inertia-advocate's frame fill block -- before filling any other role -- read it back
and check: does lens.verify contain at least one "S{N}: {phrase}" entry where {phrase}
is the exact domain-specific phrase confirmed non-generic in Step 1? If yes, continue
to the other roles. If no, revise the inertia-advocate lens.verify before writing any
other role's frame fill.

For other roles, if the candidate's G-label maps to an INERTIA BASELINE gap, include
at least one "G{N}: {phrase}" reference in lens.verify (advisory here, enforced at
Step 3 lens check).

Do not proceed to Step 3 until all candidates have complete frame fill with citations
and the inertia-advocate lens.verify back-read passed.

---

### Step 3 -- Plan and Write

Build the planning table: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength.
Planned-Vocab-Term appears verbatim in the written file's lens or expertise. Gap/Strength
matches a label from INERTIA BASELINE.

Count distinct Scope values -- if fewer than 2, expand or reassign before continuing.
Count distinct Perspective values -- if fewer than 3, add roles or reassign before
continuing. Confirm both counts pass before writing any role file.

Write the inertia-advocate first. Its lens.verify must include at least one
"S{N}: {phrase}" entry verbatim from INERTIA BASELINE (the same phrase validated in
Step 1). Planned-Vocab-Term must appear verbatim. After writing it, re-read its
lens.verify and confirm the S-label entry is present. If yes, proceed to remaining
roles. If no, revise and re-read before continuing. Do not write other roles until
this confirmation is complete.

For each remaining role in planning table order: write the file, confirm
collaborates_with includes the inertia-advocate, then run this checklist before the
next role:
  - Is verify[1] domain-specific? Yes / No + evidence
  - Is verify[2] domain-specific? Yes / No + evidence
  - Is simplify[1] a concrete cut rule? Yes / No + evidence
  - Does Planned-Vocab-Term appear verbatim? Yes / No + location
  - Does collaborates_with include the inertia-advocate? Yes / No
  - Does lens.verify reference at least one INERTIA BASELINE term
    (S or G label + phrase from Step 1)? Yes / No + which term
Revise the file if any answer is No.

Do not proceed to Step 4 until scope and perspective counts both pass, all role files
are written, and all checklists show Yes.

---

### Step 4 -- Verify

Emit each check before running the next.

  Check 1: Field completeness per file. Emit per file: PASS or FAIL [missing field]
  Check 2: Inertia-advocate present, orientation = "status-quo advocate". PASS/FAIL
  Check 3A: Scope spread >= 2. PASS/FAIL [N distinct]
  Check 3B: Written scope matches planning table. Run role-replace if mismatch.
  Check 4A: All planned roles written. PASS/FAIL
  Check 4B: Planned-Vocab-Terms verbatim in written files. Run role-replace if mismatch.
  Check 5A: Written fields match frame fill per role. Emit per role.
  Check 5B: Step 1 citations verifiable per field. Emit per violation:
    [{role}.{field}: citation missing or unverifiable]
  Check 6: No generic placeholders. PASS/FAIL [N flags]
  Check 7: All files at .roles/{domain}/. PASS/FAIL
  Check 8: Perspective spread >= 3. PASS/FAIL [N distinct]

  Inertia anchor check: re-read the inertia-advocate's lens.verify. Confirm at least
  one "S{N}: {phrase}" entry appears verbatim (label + exact phrase, as confirmed
  non-generic in Step 1). If not, revise and re-run Check 1, 5A, 5B for the
  inertia-advocate. Emit: PASS or FAIL.

  Cross-role spread check: for each non-inertia-advocate role, count how many reference
  at least one INERTIA BASELINE term (S or G label + phrase from Step 1). If count is
  zero, at least one non-inertia-advocate role must reference a baseline term verbatim
  before closing. Emit: PASS or FAIL [N non-inertia roles with reference, list them].

Do not close until all checks pass, inertia anchor check passes, and cross-role spread
check passes.

---

### Role-Replace Sub-Procedure

Fires when Check 3B or Check 4B finds a mismatch.

  planned: {planning table value for this role}
  written: {value found in written file}
  resolution: {one sentence}
  re-evaluation: {re-run Check 1, 3A, 4A, 5A, 5B, 6, 8, inertia anchor check, and
                  cross-role spread check for this role; emit per-check result}

Emit: ROLE-REPLACE CONFIRMED: YES / NO
Check 3B and Check 4B stay failed for this role while CONFIRMED is NO.
```

---

## V-05

**Variation axes**: PHRASING REGISTER (Axis-I) + LIFECYCLE COMPRESSION (Axis-J) +
INERTIA FRONT-LOADING (Axis-K) -- full integration
**Hypothesis**: All three surface changes together. Axis-K restructures phase flow
(inertia-advocate committed in Step 1 before candidates), Axis-J compresses to 4 steps,
Axis-I expresses all gates as prose. The combined effect converts the three-checkpoint
C-39 chain from Phase 4 -> Phase 6.1 -> Phase 7 into Step 1 -> Step 3 (confirmation)
-> Step 4 (final). The anchor validation fires at the earliest possible point (before
candidates are enumerated, Step 1). The cross-phase C-40 back-reference still names
"as confirmed non-generic in Step 1." Step 3's inertia-advocate write-and-confirm
becomes a file-fidelity check rather than a new-discovery gate. Test: does the
front-loading architecture produce a fully traceable audit chain in compressed prose
form, or does combining all three axes produce a prompt where the three checkpoints
collapse into a single sweep?

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. The inertia-advocate is always included and written first. Roles
without a gap to fill (or a strength to defend) do not belong in this registry.

---

### Step 1 -- Inventory, Baseline, and Inertia-Advocate

This step fully commits the inertia-advocate before any other role is considered.

Read all relevant files. Build a table labeled INPUT INVENTORY with columns Row-ID |
Source file | Excerpt (<=20 words), at least 5 rows. This table is the only source for
all frame fill citations -- do not cite the convergence summary or inertia baseline
as a frame fill source. Do not proceed past this point until 5+ rows exist.

Write the INERTIA BASELINE. Name the status quo solution. List exactly 2-3 strengths
in labeled format: S1: "{exact phrase}", S2: "{exact phrase}", S3: "{exact phrase}".
List exactly 2-3 gaps: G1: "{exact phrase}", G2: "{exact phrase}", G3: "{exact phrase}".
Each label-phrase pair is a canonical anchor term.

Apply this non-generic test to every S-phrase and G-phrase: a phrase is non-generic
if and only if it contains at least one noun or verb specific to this domain and cannot
appear unchanged in a different domain's baseline. These phrases fail regardless of
context: "easy to use", "fast", "reliable", "well-known", "familiar", "low cost",
"widely adopted", "stable", "flexible". Revise any failing phrase. Confirm all phrases
pass and record the validated label-phrase pairs; Step 4 inertia anchor check will
reference these exact phrases.

Write the CONVERGENCE SUMMARY: domain function, users, technical concerns, strategic
context. One paragraph.

Fill the inertia-advocate frame fill block now, before any candidates are listed:
  orientation.frame: status-quo advocate evaluating proposals against established {S1 phrase}
    Step 1 source: {row-id} = "{verbatim phrase}"
  orientation.serves: {value} | Step 1 source: {row-id} = "{verbatim phrase}"
  lens.verify: include at least two entries: S1: "{exact validated phrase}" and
    S2: "{exact validated phrase}", plus domain-specific verify questions
    Step 1 source: {row-id} = "{verbatim phrase}"
  lens.simplify: {cut rules} | Step 1 source: {row-id} = "{verbatim phrase}"
  expertise.depth: {knowledge} | Step 1 source: {row-id} = "{verbatim phrase}"
  expertise.relevance: {why} | Step 1 source: {row-id} = "{verbatim phrase}"
  scope: {value} | Step 1 source: {row-id} = "{verbatim phrase}"
  collaborates_with: {2-3 names -- placeholder names acceptable, resolve in Step 2}
    Step 1 source: {row-id} = "{verbatim phrase}"

After writing the inertia-advocate frame fill, before listing any candidates, read
back the lens.verify text and confirm it contains at least one "S{N}: {phrase}" entry
where {phrase} is the exact domain-specific phrase confirmed non-generic above. If yes,
the anchor is set -- proceed to Step 2. If no, revise the inertia-advocate lens.verify
now, before Step 2. The anchor must be established at this point.

Do not proceed to Step 2 until: INPUT INVENTORY has 5+ rows, INERTIA BASELINE is
complete (name + S1-S3 + G1-G3 all non-generic), CONVERGENCE SUMMARY is written,
inertia-advocate frame fill is complete with all citations, and the lens.verify
back-read passed.

---

### Step 2 -- Other Candidates and Frame Fill

List at least 4 additional candidate roles (the inertia-advocate is already committed
in Step 1). For each: the INERTIA BASELINE G-label addressed (e.g., "addresses G1"),
provisional perspective (product / technical / domain / strategy / user), provisional
scope (component / feature / system / cross-system / org). Every candidate must
reference at least one G-label. Update the inertia-advocate collaborates_with if
placeholder names can now be resolved.

Table: Candidate | Addresses (G-label) | Perspective | Scope

Fill frame fill for each Step 2 candidate. For each, provide all five fields with one
Step 1 source citation per field (format: `Step 1 source: {row-id} = "{verbatim phrase}"`):
  orientation.frame / orientation.serves / lens.verify / lens.simplify /
  expertise.depth / expertise.relevance / scope /
  collaborates_with (2-3 named roles, must include inertia-advocate)

If the candidate's G-label maps to an INERTIA BASELINE gap, include at least one
"G{N}: {phrase}" reference in lens.verify (advisory here, enforced at Step 3 lens check).
Any field you cannot support must be revised before proceeding.

Do not move to Step 3 until candidate roster has 4+ entries with G-labels and all
frame fill blocks are complete with citations.

---

### Step 3 -- Plan and Write

Build the planning table including the inertia-advocate (Step 1) and all Step 2
candidates: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength.
Planned-Vocab-Term appears verbatim in the written file's lens or expertise.
Gap/Strength matches a label from INERTIA BASELINE.

Count distinct Scope values -- if fewer than 2, expand or reassign before continuing.
Count distinct Perspective values -- if fewer than 3, add roles or reassign before
continuing. Both counts must pass.

Write the inertia-advocate first using its Step 1 frame fill values. Its lens.verify
must include at least one "S{N}: {phrase}" entry verbatim from INERTIA BASELINE (same
phrase confirmed non-generic in Step 1). Planned-Vocab-Term must appear verbatim.
After writing it, re-read the lens.verify and confirm the S-label entry is present --
since the Step 1 back-read already confirmed the frame fill, this is a file-fidelity
confirmation. If the entry is absent (file fidelity failure), revise and re-read before
continuing. Do not write other roles until this confirmation is complete.

For each remaining role in planning table order: write the file, confirm
collaborates_with includes the inertia-advocate, then check before writing the next:
  - Is verify[1] domain-specific? Yes / No + evidence
  - Is verify[2] domain-specific? Yes / No + evidence
  - Is simplify[1] a concrete cut rule? Yes / No + evidence
  - Does Planned-Vocab-Term appear verbatim? Yes / No + location
  - Does collaborates_with include the inertia-advocate? Yes / No
  - Does lens.verify reference at least one INERTIA BASELINE term
    (S or G label + phrase from Step 1)? Yes / No + which term
Revise the file if any answer is No.

Do not proceed to Step 4 until scope and perspective counts pass, all role files are
written, and all checklists show Yes.

---

### Step 4 -- Verify

Emit each check before running the next.

  Check 1: Field completeness per file. Emit per file: PASS or FAIL [missing field]
  Check 2: Inertia-advocate present, orientation = "status-quo advocate". PASS/FAIL
  Check 3A: Scope spread >= 2. PASS/FAIL [N distinct]
  Check 3B: Written scope matches planning table. Run role-replace if mismatch.
  Check 4A: All planning table roles written. PASS/FAIL
  Check 4B: Planned-Vocab-Terms verbatim in written files. Run role-replace if mismatch.
  Check 5A: Written fields match frame fill per role. Emit per role.
  Check 5B: Step 1 citations verifiable per field. Emit per violation:
    [{role}.{field}: citation missing or unverifiable]
  Check 6: No generic placeholders. PASS/FAIL [N flags]
  Check 7: All files at .roles/{domain}/. PASS/FAIL
  Check 8: Perspective spread >= 3. PASS/FAIL [N distinct]

  Inertia anchor check: re-read the inertia-advocate's lens.verify. Confirm at least
  one "S{N}: {phrase}" entry appears verbatim (label + exact phrase, as confirmed
  non-generic in Step 1). If not, revise and re-run Check 1, 5A, 5B for the
  inertia-advocate. Emit: PASS or FAIL.

  Cross-role spread check: for each non-inertia-advocate role, count how many reference
  at least one INERTIA BASELINE term (S or G label + phrase from Step 1). If count is
  zero, at least one must be revised to include a reference before closing. Emit: PASS
  or FAIL [N non-inertia roles with reference, list them].

Do not close until all checks pass, inertia anchor check passes, and cross-role spread
check passes.

---

### Role-Replace Sub-Procedure

Fires when Check 3B or Check 4B finds a mismatch.

  planned: {planning table value for this role}
  written: {value found in written file}
  resolution: {one sentence}
  re-evaluation: {re-run Check 1, 3A, 4A, 5A, 5B, 6, 8, inertia anchor check, and
                  cross-role spread check for this role; emit per-check result}

Emit: ROLE-REPLACE CONFIRMED: YES / NO
Check 3B and Check 4B stay failed for this role while CONFIRMED is NO.
```
