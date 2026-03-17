---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 18
rubric: crew-roles-rubric-v12-2026-03-17.md
---

# crew-roles -- Variate R18

5 complete prompt body variations for the `crew-roles` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

**Baseline**: R17 V-04 (Axis-D + Axis-E). R17 V-04 contains all nine prior mechanisms:
C-30 (inertia-first gate), C-31 (vocab binding column), C-32 (inline LENS AUDIT), C-33
(PERSPECTIVE AUDIT + CHECK 8), C-34 (per-slot `Phase 1 source: {row-id} = "{verbatim
phrase}"` + CHECK 5A/5B split), C-35 (ROLE-REPLACE sub-procedure with 4 fields +
CONFIRMED gate), C-36 (INERTIA BASELINE artifact in Phase 2 with named tool + enumerated
strengths + gaps, plus INERTIA ANCHOR CHECK in Phase 7), C-37 (S1/S2/S3 + G1/G2/G3
labeled terms in INERTIA BASELINE, label-prefixed verbatim propagation required in
forward-references, Phase 2 EXIT GATE verifies S1+G1 with non-generic phrase), C-38
(EARLY INERTIA ANCHOR CHECK as blocking gate immediately after STEP 6.1, Phase 7
INERTIA ANCHOR CHECK retained as confirmation). v12 rubric has 30 aspirational criteria;
baseline scores 30/30 in static analysis.

**Gaps to probe in R18**: C-37 and C-38 are now structural. R18 shifts to stress-testing
whether the labeled-anchor mechanism survives under three new structural risks not
addressed by the current formulation:

- **Risk-3 -- Phase 4 label omission**: FRAME FILL for the inertia-advocate requires
  lens.verify to "name at least two INERTIA BASELINE strengths by S-label and exact
  phrase." But the current formulation places this requirement as a sentence after the
  FRAME FILL template, not as an inline field instruction. An LLM filling Phase 4 may
  write lens.verify without S-labels and discover the gap only at the EARLY ANCHOR CHECK
  in Phase 6.1, forcing a Phase 4 revision mid-execution. Hypothesis: embedding a
  FRAME FILL PRE-ANCHOR CHECK immediately after the inertia-advocate's FRAME FILL block
  (before continuing Phase 4 for other roles) catches the label-omission before Phase 5
  and Phase 6, reducing cascade revision scope (Axis-G -- FRAME FILL PRE-ANCHOR).

- **Risk-4 -- Non-generic drift at Phase 2**: The Phase 2 EXIT GATE says "verify S1 and
  G1 with label+non-generic phrase" but does not define what makes a phrase non-generic.
  An LLM can write S1: "easy to use" and pass the gate. The "non-generic" requirement is
  unenforced without a criterion. Hypothesis: adding an operational definition -- "a
  non-generic phrase contains at least one domain-specific noun or verb that cannot appear
  unchanged in a different domain's INERTIA BASELINE" -- with a negative-example list,
  closes the drift without changing the structural gate (Axis-H -- NON-GENERIC DEFINITION).

- **Risk-5 -- Single-file baseline anchoring**: C-37 and C-38 verify only the
  inertia-advocate's lens.verify for S-label propagation. A registry where only the
  inertia-advocate references INERTIA BASELINE terms is structurally thin -- the baseline
  should shape multiple roles' lenses. Hypothesis: adding a 6th LENS AUDIT item in STEP
  6.2 (does this role's lens.verify reference at least one INERTIA BASELINE S or G term?)
  and a CROSS-ROLE SPREAD CHECK in Phase 7 (at least one non-inertia-advocate role must
  reference an INERTIA BASELINE term verbatim) ensures the baseline genuinely influences
  the registry, not just the inertia-advocate file (Axis-F -- CROSS-ROLE BASELINE SPREAD,
  carried from R17 Axis-F which was not yet crystallized into a rubric criterion).

**Single-axis**: V-01 (Axis-G), V-02 (Axis-H), V-03 (Axis-F). **Two-axis combo**:
V-04 (Axis-G + Axis-H). **Three-axis combo**: V-05 (Axis-G + Axis-H + Axis-F).

---

## V-01

**Variation axis**: FRAME FILL PRE-ANCHOR (Phase 4 blocking check on inertia-advocate
lens.verify before continuing to remaining roles)
**Hypothesis**: The EARLY INERTIA ANCHOR CHECK in Phase 6.1 detects label omissions in
the written file, but by then Phase 5 (planning table) is already complete using Phase 4
content. If Phase 4 lens.verify for the inertia-advocate lacks S-labels, the revision
path is Phase 4 -> written file -> re-check, compounding work. Firing FRAME FILL
PRE-ANCHOR CHECK immediately after the inertia-advocate's FRAME FILL block -- before
continuing Phase 4 for other roles, Phase 5, or Phase 6 -- converts Phase 6.1 from
error-detection to confirmation. All 30 v12 mechanisms are preserved; the test is
whether the pre-anchor shortens revision chains without adding meaningful overhead.

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.craft/roles/{domain}/`. Each role has: name, orientation (frame + serves),
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
  - List exactly 2-3 strengths in labeled format: S1: "{exact phrase}", S2: "{exact
    phrase}", S3: "{exact phrase}". Each label-phrase pair is an anchor term.
  - List exactly 2-3 gaps in labeled format: G1: "{exact phrase}", G2: "{exact phrase}",
    G3: "{exact phrase}". Each gap is a justification slot for a new role.

CONVERGENCE SUMMARY (1 paragraph):
  - Domain function, users, technical concerns, strategic context.

Both are framing artifacts. Phase 4 citations must trace to INPUT INVENTORY rows.
The S-labels and G-labels from INERTIA BASELINE are the canonical anchor terms for
forward-reference throughout Phases 3-7. Generic phrases do not constitute valid anchor
terms; each S-phrase must be specific to this domain.

EXIT GATE: INERTIA BASELINE COMPLETE (name + S1-S3 + G1-G3 all present, each with
           label + non-generic phrase) + CONVERGENCE SUMMARY COMPLETE

---

### PHASE 3 -- CANDIDATE ROSTER

Enumerate at least 5 candidate roles. For each:
  - State which INERTIA BASELINE item it addresses (use the label: e.g., "defends S1",
    "addresses G2").
  - Assign provisional perspective (product / technical / inertia / domain / strategy / user)
  - Assign provisional scope (component / feature / system / cross-system / org)

The inertia-advocate's reason-to-exist is "defends S1 (and S2, S3)". Every other role's
reason references at least one G-label.

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

The inertia-advocate's lens.verify must include at least two entries in the form
"S{N}: {exact phrase from INERTIA BASELINE}" using labels defined in Phase 2.

Complete the inertia-advocate FRAME FILL block first. Then run this check before filling
remaining roles:

  FRAME FILL PRE-ANCHOR CHECK:
  Re-read the inertia-advocate FRAME FILL block lens.verify value just written.
  Confirm at least one "S{N}: {phrase}" entry is present where S{N} is a label from
  INERTIA BASELINE and {phrase} is the exact phrase from that entry.
  FRAME FILL PRE-ANCHOR CHECK: PASS -- continue Phase 4 for remaining roles.
  FRAME FILL PRE-ANCHOR CHECK: FAIL -- revise the inertia-advocate lens.verify in this
  FRAME FILL block before continuing Phase 4. Do not start any other role's FRAME FILL
  while this check is FAIL.

After FRAME FILL PRE-ANCHOR CHECK PASS, complete FRAME FILL for all remaining candidates.
Any field marked UNSUPPORTED must be revised before proceeding.

EXIT GATE: FRAME FILL COMPLETE (all candidates, all fields, all citations present,
           FRAME FILL PRE-ANCHOR CHECK PASS)

---

### PHASE 5 -- PLANNING TABLE + DUAL GATE

Build planning table: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength

Planned-Vocab-Term: a domain-specific term that will appear verbatim in the written file's
lens or expertise. Gap/Strength: must match a label from INERTIA BASELINE (e.g., "G2" or
"defends S1").

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
Write the inertia-advocate role file using its Phase 4 FRAME FILL values. Its lens.verify
must include at least one "S{N}: {phrase}" entry verbatim from INERTIA BASELINE.
Planned-Vocab-Term must appear verbatim in lens or expertise.
Emit: INERTIA-ADVOCATE WRITTEN: {path}

EARLY INERTIA ANCHOR CHECK (blocking gate):
Re-read the inertia-advocate's written lens.verify. Confirm at least one "S{N}: {phrase}"
entry appears verbatim (label + exact phrase from INERTIA BASELINE).
  EARLY INERTIA ANCHOR CHECK: PASS -- proceed to STEP 6.2.
  EARLY INERTIA ANCHOR CHECK: FAIL -- revise inertia-advocate file and re-check before
  STEP 6.2. If Phase 4 FRAME FILL PRE-ANCHOR CHECK PASS was correctly emitted, this
  should be confirmation not correction.
STEP 6.2 is blocked until EARLY INERTIA ANCHOR CHECK PASS.

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
  CHECK 7: All files at .craft/roles/{domain}/. Emit: CHECK 7: PASS/FAIL
  CHECK 8: Perspective spread from written files >= 3. Emit: CHECK 8: PASS/FAIL [N distinct]

  INERTIA ANCHOR CHECK (final confirmation):
  Re-read the inertia-advocate's lens.verify field. Confirm at least one "S{N}: {phrase}"
  entry appears verbatim (label + exact phrase from INERTIA BASELINE). If not: INERTIA
  ANCHOR CHECK FAIL -- revise file and re-run CHECK 1, 5A, 5B for the inertia-advocate.
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

## V-02

**Variation axis**: NON-GENERIC DEFINITION (operational criterion for S-phrase specificity
at Phase 2 EXIT GATE)
**Hypothesis**: The Phase 2 EXIT GATE requires S1+G1 with "non-generic phrase" but the
current formulation leaves "non-generic" to LLM judgment. An LLM can write S1: "easy to
use" or S1: "well-documented" and self-assert that the EXIT GATE passed. Providing an
explicit operational definition -- with negative examples -- closes the definitional gap
without adding structural complexity. The definition targets the judgment call, not the
gate structure. All 30 v12 mechanisms are preserved; the test is whether the definition
eliminates generic S-phrases at Phase 2 without causing over-specificity failures in
practice.

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.craft/roles/{domain}/`. Each role has: name, orientation (frame + serves),
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
  - List exactly 2-3 strengths in labeled format: S1: "{exact phrase}", S2: "{exact
    phrase}", S3: "{exact phrase}". Each label-phrase pair is an anchor term.
  - List exactly 2-3 gaps in labeled format: G1: "{exact phrase}", G2: "{exact phrase}",
    G3: "{exact phrase}". Each gap is a justification slot for a new role.

NON-GENERIC REQUIREMENT: Each S-phrase must be domain-specific. A phrase is non-generic
if and only if it contains at least one noun or verb that is specific to this domain and
cannot appear unchanged in a different domain's INERTIA BASELINE. Phrases that fail this
test: "easy to use", "fast", "reliable", "well-documented", "familiar to teams", "low
cost", "widely adopted" (these could describe any tool in any domain). If any S-phrase is
generic by this test, revise it before passing the EXIT GATE. The same specificity
requirement applies to G-phrases.

CONVERGENCE SUMMARY (1 paragraph):
  - Domain function, users, technical concerns, strategic context.

Both are framing artifacts. Phase 4 citations must trace to INPUT INVENTORY rows.
The S-labels and G-labels from INERTIA BASELINE are the canonical anchor terms for
forward-reference throughout Phases 3-7.

EXIT GATE: INERTIA BASELINE COMPLETE (name + S1-S3 + G1-G3 all present) +
           NON-GENERIC CHECK (each S-phrase and G-phrase passes the domain-specificity
           test above -- no phrase from the generic-fail list or equivalent) +
           CONVERGENCE SUMMARY COMPLETE

---

### PHASE 3 -- CANDIDATE ROSTER

Enumerate at least 5 candidate roles. For each:
  - State which INERTIA BASELINE item it addresses (use the label: e.g., "defends S1",
    "addresses G2").
  - Assign provisional perspective (product / technical / inertia / domain / strategy / user)
  - Assign provisional scope (component / feature / system / cross-system / org)

The inertia-advocate's reason-to-exist is "defends S1 (and S2, S3)". Every other role's
reason references at least one G-label.

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

The inertia-advocate's lens.verify must include at least two entries in the form
"S{N}: {exact phrase from INERTIA BASELINE}" using labels defined in Phase 2. Any field
marked UNSUPPORTED must be revised before proceeding.

EXIT GATE: FRAME FILL COMPLETE (all candidates, all fields, all citations present)

---

### PHASE 5 -- PLANNING TABLE + DUAL GATE

Build planning table: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength

Planned-Vocab-Term: a domain-specific term that will appear verbatim in the written file's
lens or expertise. Gap/Strength: must match a label from INERTIA BASELINE (e.g., "G2" or
"defends S1").

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
Write the inertia-advocate role file using its Phase 4 FRAME FILL values. Its lens.verify
must include at least one "S{N}: {phrase}" entry verbatim from INERTIA BASELINE. Planned-
Vocab-Term must appear verbatim in lens or expertise.
Emit: INERTIA-ADVOCATE WRITTEN: {path}

EARLY INERTIA ANCHOR CHECK (blocking gate):
Re-read the inertia-advocate's written lens.verify. Confirm at least one "S{N}: {phrase}"
entry appears verbatim, where S{N} is a label defined in INERTIA BASELINE and {phrase} is
the exact domain-specific phrase from that entry (as validated at Phase 2 EXIT GATE).
  EARLY INERTIA ANCHOR CHECK: PASS -- proceed to STEP 6.2.
  EARLY INERTIA ANCHOR CHECK: FAIL -- revise inertia-advocate and re-check before STEP 6.2.
STEP 6.2 is blocked until EARLY INERTIA ANCHOR CHECK PASS.

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
  CHECK 7: All files at .craft/roles/{domain}/. Emit: CHECK 7: PASS/FAIL
  CHECK 8: Perspective spread from written files >= 3. Emit: CHECK 8: PASS/FAIL [N distinct]

  INERTIA ANCHOR CHECK (final confirmation):
  Re-read the inertia-advocate's lens.verify field. Confirm at least one "S{N}: {phrase}"
  entry appears verbatim (label + exact domain-specific phrase from INERTIA BASELINE as
  validated at Phase 2 EXIT GATE NON-GENERIC CHECK). If not: INERTIA ANCHOR CHECK FAIL
  -- revise file and re-run CHECK 1, 5A, 5B for the inertia-advocate.
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

## V-03

**Variation axis**: CROSS-ROLE BASELINE SPREAD (LENS AUDIT 6th item + CROSS-ROLE SPREAD
CHECK in Phase 7)
**Hypothesis**: C-37 and C-38 verify only the inertia-advocate's lens.verify for
S-label propagation. A registry where only the inertia-advocate references INERTIA
BASELINE terms is structurally thin -- the status quo analysis should shape how all roles
ask questions, not just the role defending it. Adding a 6th LENS AUDIT item in STEP 6.2
(does this role's lens.verify reference at least one S or G term?) and a CROSS-ROLE
SPREAD CHECK in Phase 7 (at least one non-inertia-advocate role must pass) validates that
the INERTIA BASELINE has genuinely influenced the registry. All 30 v12 mechanisms are
preserved; the test is whether the spread check produces richer, more domain-grounded
lens.verify content across all roles.

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.craft/roles/{domain}/`. Each role has: name, orientation (frame + serves),
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
  - List exactly 2-3 strengths in labeled format: S1: "{exact phrase}", S2: "{exact
    phrase}", S3: "{exact phrase}". Each label-phrase pair is an anchor term.
  - List exactly 2-3 gaps in labeled format: G1: "{exact phrase}", G2: "{exact phrase}",
    G3: "{exact phrase}". Each gap is a justification slot for a new role.

CONVERGENCE SUMMARY (1 paragraph):
  - Domain function, users, technical concerns, strategic context.

Both are framing artifacts. Phase 4 citations must trace to INPUT INVENTORY rows.
The S-labels and G-labels from INERTIA BASELINE are the canonical anchor terms for
forward-reference throughout Phases 3-7. Generic phrases do not constitute valid anchor
terms.

EXIT GATE: INERTIA BASELINE COMPLETE (name + S1-S3 + G1-G3 all present, each with
           label + non-generic phrase) + CONVERGENCE SUMMARY COMPLETE

---

### PHASE 3 -- CANDIDATE ROSTER

Enumerate at least 5 candidate roles. For each:
  - State which INERTIA BASELINE item it addresses (use the label: e.g., "defends S1",
    "addresses G2").
  - Assign provisional perspective (product / technical / inertia / domain / strategy / user)
  - Assign provisional scope (component / feature / system / cross-system / org)

The inertia-advocate's reason-to-exist is "defends S1 (and S2, S3)". Every other role's
reason references at least one G-label.

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

The inertia-advocate's lens.verify must include at least two entries in the form
"S{N}: {exact phrase from INERTIA BASELINE}" using labels defined in Phase 2.

For all remaining roles, consider whether each role's concern connects to an INERTIA
BASELINE gap or strength. If so, the FRAME FILL lens.verify should reference that G or S
term (label + phrase). This is advisory in Phase 4 but enforced by LENS AUDIT in Phase 6.

Any field marked UNSUPPORTED must be revised before proceeding.

EXIT GATE: FRAME FILL COMPLETE (all candidates, all fields, all citations present)

---

### PHASE 5 -- PLANNING TABLE + DUAL GATE

Build planning table: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength

Planned-Vocab-Term: a domain-specific term that will appear verbatim in the written file's
lens or expertise. Gap/Strength: must match a label from INERTIA BASELINE (e.g., "G2" or
"defends S1").

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
Write the inertia-advocate role file using its Phase 4 FRAME FILL values. Its lens.verify
must include at least one "S{N}: {phrase}" entry verbatim from INERTIA BASELINE. Planned-
Vocab-Term must appear verbatim in lens or expertise.
Emit: INERTIA-ADVOCATE WRITTEN: {path}

EARLY INERTIA ANCHOR CHECK (blocking gate):
Re-read the inertia-advocate's written lens.verify. Confirm at least one "S{N}: {phrase}"
entry appears verbatim (label + exact phrase from INERTIA BASELINE).
  EARLY INERTIA ANCHOR CHECK: PASS -- proceed to STEP 6.2.
  EARLY INERTIA ANCHOR CHECK: FAIL -- revise inertia-advocate and re-check before STEP 6.2.
STEP 6.2 is blocked until EARLY INERTIA ANCHOR CHECK PASS.

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
       - references INERTIA BASELINE term (S or G label + phrase): YES/NO + which term
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
  CHECK 7: All files at .craft/roles/{domain}/. Emit: CHECK 7: PASS/FAIL
  CHECK 8: Perspective spread from written files >= 3. Emit: CHECK 8: PASS/FAIL [N distinct]

  INERTIA ANCHOR CHECK (final confirmation):
  Re-read the inertia-advocate's lens.verify field. Confirm at least one "S{N}: {phrase}"
  entry appears verbatim (label + exact phrase from INERTIA BASELINE). If not: INERTIA
  ANCHOR CHECK FAIL -- revise file and re-run CHECK 1, 5A, 5B for the inertia-advocate.
  Emit: INERTIA ANCHOR CHECK: PASS/FAIL

  CROSS-ROLE SPREAD CHECK:
  For each non-inertia-advocate role, re-read its written lens.verify. Count how many
  reference at least one INERTIA BASELINE term (S or G label + phrase from Phase 2).
  If count = 0 (no non-inertia role references baseline): CROSS-ROLE SPREAD CHECK FAIL
  -- at least one non-inertia-advocate role must reference an INERTIA BASELINE term.
  Emit: CROSS-ROLE SPREAD CHECK: PASS/FAIL [N non-inertia roles with baseline reference]

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

**Variation axes**: FRAME FILL PRE-ANCHOR (Axis-G) + NON-GENERIC DEFINITION (Axis-H)
**Hypothesis**: The two risk vectors that remain open after C-37 and C-38 are: (1) the
Phase 4 FRAME FILL for inertia-advocate may omit S-labels, causing a Phase 6.1 revision
cascade; and (2) the Phase 2 S-phrases may be generic, making the label mechanism
technically present but semantically vacuous. V-04 combines the pre-anchor check (Axis-G)
with the non-generic definition (Axis-H). Together they form a two-barrier pattern: Phase
2 gates phrase quality, Phase 4 gates label discipline, Phase 6.1 confirms execution.
Each barrier is lightweight; the combination tests whether they are mutually reinforcing
without creating overhead that causes LLMs to skip later phases.

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.craft/roles/{domain}/`. Each role has: name, orientation (frame + serves),
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
  - List exactly 2-3 strengths in labeled format: S1: "{exact phrase}", S2: "{exact
    phrase}", S3: "{exact phrase}". Each label-phrase pair is an anchor term.
  - List exactly 2-3 gaps in labeled format: G1: "{exact phrase}", G2: "{exact phrase}",
    G3: "{exact phrase}". Each gap is a justification slot for a new role.

NON-GENERIC REQUIREMENT: Each S-phrase must be domain-specific. A phrase is non-generic
if and only if it contains at least one noun or verb that is specific to this domain and
cannot appear unchanged in a different domain's INERTIA BASELINE. The following phrases
fail this test regardless of context: "easy to use", "fast", "reliable", "well-known",
"familiar", "low cost", "widely adopted", "stable", "flexible". If any S-phrase matches
this list or is equivalent in genericity, revise before passing the EXIT GATE.

CONVERGENCE SUMMARY (1 paragraph):
  - Domain function, users, technical concerns, strategic context.

Both are framing artifacts. Phase 4 citations must trace to INPUT INVENTORY rows.
The S-labels and G-labels from INERTIA BASELINE are the canonical anchor terms for
forward-reference throughout Phases 3-7.

EXIT GATE: INERTIA BASELINE COMPLETE (name + S1-S3 + G1-G3 all present) +
           NON-GENERIC CHECK (each S-phrase passes domain-specificity test above) +
           CONVERGENCE SUMMARY COMPLETE

---

### PHASE 3 -- CANDIDATE ROSTER

Enumerate at least 5 candidate roles. For each:
  - State which INERTIA BASELINE item it addresses (use the label: e.g., "defends S1",
    "addresses G2").
  - Assign provisional perspective (product / technical / inertia / domain / strategy / user)
  - Assign provisional scope (component / feature / system / cross-system / org)

The inertia-advocate's reason-to-exist is "defends S1 (and S2, S3)". Every other role's
reason references at least one G-label.

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

The inertia-advocate's lens.verify must include at least two entries in the form
"S{N}: {exact phrase from INERTIA BASELINE}" using labels defined in Phase 2.

Complete the inertia-advocate FRAME FILL block first. Then run:

  FRAME FILL PRE-ANCHOR CHECK:
  Re-read the inertia-advocate FRAME FILL block lens.verify value just written.
  Confirm at least one "S{N}: {phrase}" entry is present where S{N} is a label from
  INERTIA BASELINE and {phrase} is the exact domain-specific phrase (as validated at
  Phase 2 EXIT GATE NON-GENERIC CHECK).
  FRAME FILL PRE-ANCHOR CHECK: PASS -- continue Phase 4 for remaining roles.
  FRAME FILL PRE-ANCHOR CHECK: FAIL -- revise inertia-advocate lens.verify in this FRAME
  FILL block before continuing Phase 4. Do not start any other role's FRAME FILL while
  this check is FAIL.

After FRAME FILL PRE-ANCHOR CHECK PASS, complete FRAME FILL for all remaining candidates.
Any field marked UNSUPPORTED must be revised before proceeding.

EXIT GATE: FRAME FILL COMPLETE (all candidates, all fields, all citations present,
           FRAME FILL PRE-ANCHOR CHECK PASS)

---

### PHASE 5 -- PLANNING TABLE + DUAL GATE

Build planning table: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength

Planned-Vocab-Term: a domain-specific term that will appear verbatim in the written file's
lens or expertise. Gap/Strength: must match a label from INERTIA BASELINE (e.g., "G2" or
"defends S1").

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
Write the inertia-advocate role file using its Phase 4 FRAME FILL values. Its lens.verify
must include at least one "S{N}: {phrase}" entry verbatim from INERTIA BASELINE (the same
domain-specific phrase validated at Phase 2 NON-GENERIC CHECK). Planned-Vocab-Term must
appear verbatim in lens or expertise.
Emit: INERTIA-ADVOCATE WRITTEN: {path}

EARLY INERTIA ANCHOR CHECK (blocking gate):
Re-read the inertia-advocate's written lens.verify. Confirm at least one "S{N}: {phrase}"
entry appears verbatim (label + exact domain-specific phrase from INERTIA BASELINE).
  EARLY INERTIA ANCHOR CHECK: PASS -- proceed to STEP 6.2.
  EARLY INERTIA ANCHOR CHECK: FAIL -- revise inertia-advocate and re-check before STEP 6.2.
  If Phase 4 FRAME FILL PRE-ANCHOR CHECK PASS was correctly emitted, this is confirmation.
STEP 6.2 is blocked until EARLY INERTIA ANCHOR CHECK PASS.

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
  CHECK 7: All files at .craft/roles/{domain}/. Emit: CHECK 7: PASS/FAIL
  CHECK 8: Perspective spread from written files >= 3. Emit: CHECK 8: PASS/FAIL [N distinct]

  INERTIA ANCHOR CHECK (final confirmation):
  Re-read the inertia-advocate's lens.verify field. Confirm at least one "S{N}: {phrase}"
  entry appears verbatim (label + exact domain-specific phrase from INERTIA BASELINE, as
  validated at Phase 2 NON-GENERIC CHECK). If not: INERTIA ANCHOR CHECK FAIL -- revise
  file and re-run CHECK 1, 5A, 5B for the inertia-advocate.
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

**Variation axes**: FRAME FILL PRE-ANCHOR (Axis-G) + NON-GENERIC DEFINITION (Axis-H) +
CROSS-ROLE BASELINE SPREAD (Axis-F) -- full integration
**Hypothesis**: The three axes address three distinct gaps in the current mechanism: Phase
2 phrase quality (Axis-H), Phase 4 label discipline (Axis-G), and registry-wide baseline
influence (Axis-F). V-05 tests whether combining all three creates a fully traceable audit
chain: Phase 2 validates phrase quality -> Phase 4 pre-anchors labels in FRAME FILL ->
Phase 6.1 confirms label propagation to written file -> LENS AUDIT confirms spread to
remaining roles -> Phase 7 CROSS-ROLE SPREAD CHECK verifies the registry is collectively
anchored, not just locally. The risk is that three stacked mechanisms produce mechanical
outputs; the test is whether the combination yields richer content rather than rote
compliance.

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.craft/roles/{domain}/`. Each role has: name, orientation (frame + serves),
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
  - List exactly 2-3 strengths in labeled format: S1: "{exact phrase}", S2: "{exact
    phrase}", S3: "{exact phrase}". Each label-phrase pair is an anchor term.
  - List exactly 2-3 gaps in labeled format: G1: "{exact phrase}", G2: "{exact phrase}",
    G3: "{exact phrase}". Each gap is a justification slot for a new role.

NON-GENERIC REQUIREMENT: Each S-phrase must be domain-specific. A phrase is non-generic
if and only if it contains at least one noun or verb that is specific to this domain and
cannot appear unchanged in a different domain's INERTIA BASELINE. The following phrases
fail this test regardless of context: "easy to use", "fast", "reliable", "well-known",
"familiar", "low cost", "widely adopted", "stable", "flexible". If any S-phrase matches
this list or is equivalent in genericity, revise before passing the EXIT GATE. The same
specificity requirement applies to G-phrases.

CONVERGENCE SUMMARY (1 paragraph):
  - Domain function, users, technical concerns, strategic context.

Both are framing artifacts. Phase 4 citations must trace to INPUT INVENTORY rows.
The S-labels and G-labels from INERTIA BASELINE are the canonical anchor terms for
forward-reference throughout Phases 3-7.

EXIT GATE: INERTIA BASELINE COMPLETE (name + S1-S3 + G1-G3 all present) +
           NON-GENERIC CHECK (each S-phrase and G-phrase passes domain-specificity test) +
           CONVERGENCE SUMMARY COMPLETE

---

### PHASE 3 -- CANDIDATE ROSTER

Enumerate at least 5 candidate roles. For each:
  - State which INERTIA BASELINE item it addresses (use the label: e.g., "defends S1",
    "addresses G2").
  - Assign provisional perspective (product / technical / inertia / domain / strategy / user)
  - Assign provisional scope (component / feature / system / cross-system / org)

The inertia-advocate's reason-to-exist is "defends S1 (and S2, S3)". Every other role's
reason references at least one G-label.

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

The inertia-advocate's lens.verify must include at least two entries in the form
"S{N}: {exact phrase from INERTIA BASELINE}" using labels defined in Phase 2.

For all remaining roles, if the role's CANDIDATE ROSTER G-label maps to an INERTIA
BASELINE gap, the FRAME FILL lens.verify should include at least one reference to that
"G{N}: {phrase}" term. This is advisory in Phase 4 but enforced by LENS AUDIT in Phase 6.

Complete the inertia-advocate FRAME FILL block first. Then run:

  FRAME FILL PRE-ANCHOR CHECK:
  Re-read the inertia-advocate FRAME FILL block lens.verify value just written.
  Confirm at least one "S{N}: {phrase}" entry is present where S{N} is a label from
  INERTIA BASELINE and {phrase} is the exact domain-specific phrase (as validated at
  Phase 2 EXIT GATE NON-GENERIC CHECK).
  FRAME FILL PRE-ANCHOR CHECK: PASS -- continue Phase 4 for remaining roles.
  FRAME FILL PRE-ANCHOR CHECK: FAIL -- revise inertia-advocate lens.verify in this FRAME
  FILL block before continuing Phase 4. Do not start any other role's FRAME FILL while
  this check is FAIL.

After FRAME FILL PRE-ANCHOR CHECK PASS, complete FRAME FILL for all remaining candidates.
Any field marked UNSUPPORTED must be revised before proceeding.

EXIT GATE: FRAME FILL COMPLETE (all candidates, all fields, all citations present,
           FRAME FILL PRE-ANCHOR CHECK PASS)

---

### PHASE 5 -- PLANNING TABLE + DUAL GATE

Build planning table: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength

Planned-Vocab-Term: a domain-specific term that will appear verbatim in the written file's
lens or expertise. Gap/Strength: must match a label from INERTIA BASELINE (e.g., "G2" or
"defends S1").

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
Write the inertia-advocate role file using its Phase 4 FRAME FILL values. Its lens.verify
must include at least one "S{N}: {phrase}" entry verbatim from INERTIA BASELINE (the same
domain-specific phrase validated at Phase 2 NON-GENERIC CHECK). Planned-Vocab-Term must
appear verbatim in lens or expertise.
Emit: INERTIA-ADVOCATE WRITTEN: {path}

EARLY INERTIA ANCHOR CHECK (blocking gate):
Re-read the inertia-advocate's written lens.verify. Confirm at least one "S{N}: {phrase}"
entry appears verbatim (label + exact domain-specific phrase from INERTIA BASELINE).
  EARLY INERTIA ANCHOR CHECK: PASS -- proceed to STEP 6.2.
  EARLY INERTIA ANCHOR CHECK: FAIL -- revise inertia-advocate and re-check before STEP 6.2.
  If Phase 4 FRAME FILL PRE-ANCHOR CHECK PASS was correctly emitted, this is confirmation.
STEP 6.2 is blocked until EARLY INERTIA ANCHOR CHECK PASS.

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
       - references INERTIA BASELINE term (S or G label + phrase): YES/NO + which term
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
  CHECK 7: All files at .craft/roles/{domain}/. Emit: CHECK 7: PASS/FAIL
  CHECK 8: Perspective spread from written files >= 3. Emit: CHECK 8: PASS/FAIL [N distinct]

  INERTIA ANCHOR CHECK (final confirmation):
  Re-read the inertia-advocate's lens.verify field. Confirm at least one "S{N}: {phrase}"
  entry appears verbatim (label + exact domain-specific phrase from INERTIA BASELINE, as
  validated at Phase 2 NON-GENERIC CHECK). If not: INERTIA ANCHOR CHECK FAIL -- revise
  file and re-run CHECK 1, 5A, 5B for the inertia-advocate.
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
                  CROSS-ROLE SPREAD CHECK; emit per-check result}

Emit: ROLE-REPLACE CONFIRMED: YES / NO
CHECK 3B and CHECK 4B stay FAIL for this role while ROLE-REPLACE CONFIRMED is NO.
```
