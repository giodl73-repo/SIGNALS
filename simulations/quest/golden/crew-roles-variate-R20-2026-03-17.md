---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 20
rubric: crew-roles-rubric-v14-2026-03-17.md
---

# crew-roles -- Variate R20

5 complete prompt body variations for the `crew-roles` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

**Baseline**: R19 V-02 (Axis-J: 4-step lifecycle compression). Under v14, V-02 already
satisfies C-42(b) (positional inference unambiguous: NON-GENERIC REQUIREMENT in STEP 1
alongside INERTIA BASELINE; FRAME FILL PRE-ANCHOR CHECK fires immediately after
inertia-advocate block, before remaining-roles loop; INERTIA ANCHOR CHECK back-references
"STEP 1 NON-GENERIC CHECK" by actual name) and C-43 (EARLY INERTIA ANCHOR CHECK includes
explicit dual-branch routing: PASS → proceed to remaining roles; FAIL → revise and
re-check, remaining roles blocked). The baseline scores high on all 35 criteria under
v14. R20 stress-tests three residual risks not yet probed:

- **Risk-L -- C-42 ambiguity under novel domains**: C-42(b) positional inference works
  when a scorer can read the step order and judge it unambiguous. But in novel or
  heavily-customized domains, a scorer may disagree on whether "unambiguously inferrable"
  applies. C-42(a) — an explicit canonical-phase mapping table — eliminates the
  inference requirement entirely, making the satisfaction mechanically verifiable.
  Hypothesis: adding the mapping table converts a C-42 judgment call into a C-42
  certain PASS, with no cost to other criteria (Axis-L -- EXPLICIT PHASE MAPPING TABLE).

- **Risk-M -- Gate routing coverage gap**: C-43 requires dual-branch routing only for
  EARLY INERTIA ANCHOR CHECK. All other EXIT GATE blocks in the baseline say "Do not
  proceed until X" but omit explicit PASS/FAIL routing. An LLM encountering a gate
  with no routing may skip or collapse it. Hypothesis: adding dual-branch routing to
  every blocking gate makes all gates self-contained, reduces the chance any gate is
  treated as advisory, and creates zero scoring conflict with existing criteria since
  C-43 is a layer on top of C-38 (Axis-M -- FULL SELF-ROUTING GATES).

- **Risk-N -- CROSS-ROLE SPREAD CHECK dependency on scan**: C-41 requires at least one
  non-inertia role to reference an INERTIA BASELINE term verbatim; the check fires in
  Phase 7. The baseline enforces this post-hoc. An LLM writing roles without explicit
  assignment may omit baseline references and face a Phase 7 FAIL + cascade revision.
  Hypothesis: constructing a BASELINE PROPAGATION MAP immediately after INERTIA BASELINE
  assigns S/G terms to roles upfront, converting the scan-based C-41 into an
  assignment-based enforcement that prevents the failure mode rather than detecting it
  (Axis-N -- BASELINE PROPAGATION MAP).

**Single-axis**: V-01 (Axis-L), V-02 (Axis-M), V-03 (Axis-N).
**Two-axis**: V-04 (Axis-L + Axis-M). **Three-axis**: V-05 (Axis-L + Axis-M + Axis-N).

---

## V-01

**Variation axis**: EXPLICIT PHASE MAPPING TABLE (Axis-L) -- add canonical-phase mapping
table at structure header to satisfy C-42(a) declaratively
**Hypothesis**: The R19 V-02 baseline satisfies C-42(b) by positional inference. Inference
requires a scorer to judge whether the ordering is "unambiguously inferrable" -- a
subjective threshold. Declaring an explicit PHASE STRUCTURE MAPPING table at the top
satisfies C-42(a) instead, converting the judgment call into a mechanical check. All
other mechanisms are unchanged. Test: does the mapping table produce C-42 PASS without
altering any other criterion score?

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. The inertia-advocate is always included and written first. Roles
without a gap to fill (or a strength to defend) do not belong in this registry.

PHASE STRUCTURE MAPPING (this prompt uses 4 steps; canonical-phase equivalents):
  STEP 1 = canonical Phase 1 (Input Inventory) + canonical Phase 2 (Inertia Baseline)
  STEP 2 = canonical Phase 3 (Candidate Roster) + canonical Phase 4 (Frame Fill:
           inertia-advocate first, FRAME FILL PRE-ANCHOR CHECK, remaining roles)
  STEP 3 = canonical Phase 4 (Planning Table + Audits) + canonical Phase 6 (Write Files)
  STEP 4 = canonical Phase 7 (Verification Checks)

---

### STEP 1 -- INVENTORY AND BASELINE

Read all relevant files. Produce three artifacts before proceeding to STEP 2.

INPUT INVENTORY: table of Row-ID | Source file | Excerpt (<=20 words). Minimum 5 rows.
This table is the sole citation source for STEP 2 frame fill values -- no field may
cite the convergence summary or inertia baseline as its source.

INERTIA BASELINE: name the status quo solution. List exactly 2-3 strengths: S1: "{exact
phrase}", S2: "{exact phrase}", S3: "{exact phrase}". List exactly 2-3 gaps: G1: "{exact
phrase}", G2: "{exact phrase}", G3: "{exact phrase}". Each label-phrase pair is a
canonical anchor term for forward-reference in STEPS 2-4.

NON-GENERIC REQUIREMENT: each S-phrase must contain at least one noun or verb specific
to this domain that cannot appear unchanged in a different domain's INERTIA BASELINE.
These phrases fail this test regardless of context: "easy to use", "fast", "reliable",
"well-known", "familiar", "low cost", "widely adopted", "stable", "flexible". Apply the
same test to G-phrases. Revise any failing phrase before continuing. Confirm all phrases
pass; emit: NON-GENERIC CHECK: PASS before proceeding. STEP 4 INERTIA ANCHOR CHECK will
reference the phrases validated at STEP 1 NON-GENERIC CHECK.

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

FRAME FILL: for each candidate, fill all five fields with one STEP 1 source citation
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

## V-02

**Variation axis**: FULL SELF-ROUTING GATES (Axis-M) -- add dual-branch routing (PASS
continuation + FAIL remediation) to every blocking gate, not just EARLY INERTIA ANCHOR
CHECK
**Hypothesis**: C-43 requires dual-branch routing for EARLY INERTIA ANCHOR CHECK. The
baseline's other EXIT GATEs say "Do not proceed until X" -- a one-branch structure that
identifies the FAIL condition but not the PASS continuation. An LLM encountering a gate
with no PASS branch may either treat the gate as advisory or must infer the continuation
from surrounding prose. Extending dual-branch routing to every gate makes every gate
executor-complete. Test: does system-wide self-routing strengthen execution fidelity
without creating criterion conflicts or over-specifying the prompt?

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
This table is the sole citation source for STEP 2 frame fill values -- no field may
cite the convergence summary or inertia baseline as its source.

INERTIA BASELINE: name the status quo solution. List exactly 2-3 strengths: S1: "{exact
phrase}", S2: "{exact phrase}", S3: "{exact phrase}". List exactly 2-3 gaps: G1: "{exact
phrase}", G2: "{exact phrase}", G3: "{exact phrase}". Each label-phrase pair is a
canonical anchor term for forward-reference in STEPS 2-4.

NON-GENERIC REQUIREMENT: each S-phrase must contain at least one noun or verb specific
to this domain that cannot appear unchanged in a different domain's INERTIA BASELINE.
These phrases fail this test regardless of context: "easy to use", "fast", "reliable",
"well-known", "familiar", "low cost", "widely adopted", "stable", "flexible". Apply the
same test to G-phrases. Revise any failing phrase before continuing. Confirm all phrases
pass; emit: NON-GENERIC CHECK: PASS. STEP 4 INERTIA ANCHOR CHECK will reference the
phrases validated at STEP 1 NON-GENERIC CHECK.

CONVERGENCE SUMMARY: one paragraph covering domain function, users, technical concerns,
and strategic context.

EXIT GATE:
  STEP 1 EXIT: PASS -- INPUT INVENTORY >= 5 rows AND INERTIA BASELINE complete (name +
    S1-S3 + G1-G3) AND NON-GENERIC CHECK PASS AND CONVERGENCE SUMMARY written.
    Proceed to STEP 2.
  STEP 1 EXIT: FAIL -- complete missing artifacts and re-run NON-GENERIC CHECK before
    proceeding. Do not start STEP 2 while STEP 1 EXIT is FAIL.

---

### STEP 2 -- CANDIDATES AND FRAME FILL

CANDIDATE ROSTER: enumerate at least 5 candidates. For each: the INERTIA BASELINE label
it addresses (e.g., "defends S1", "addresses G2"), provisional perspective (product /
technical / inertia / domain / strategy / user), provisional scope (component / feature
/ system / cross-system / org). The inertia-advocate's reason-to-exist is "defends S1
(and S2, S3)"; every other role must reference at least one G-label.
Table: Candidate | Addresses (S/G label) | Perspective | Scope

FRAME FILL: for each candidate, fill all five fields with one STEP 1 source citation
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
    FRAME FILL PRE-ANCHOR CHECK: PASS -- proceed to fill remaining roles.
    FRAME FILL PRE-ANCHOR CHECK: FAIL -- revise the inertia-advocate lens.verify in this
    block; do not fill any other role's frame fill while this check is FAIL.

For remaining roles, if the candidate's G-label maps to an INERTIA BASELINE gap, the
lens.verify should include at least one "G{N}: {phrase}" reference (advisory here,
enforced at STEP 3 lens audit).

EXIT GATE:
  STEP 2 EXIT: PASS -- CANDIDATE ROSTER complete (>= 5, all with S/G labels) AND
    FRAME FILL complete (all candidates, all fields, all citations) AND
    FRAME FILL PRE-ANCHOR CHECK PASS. Proceed to STEP 3.
  STEP 2 EXIT: FAIL -- complete missing frame fill blocks or revise inertia-advocate
    lens.verify and re-run FRAME FILL PRE-ANCHOR CHECK. Do not start STEP 3 while
    STEP 2 EXIT is FAIL.

---

### STEP 3 -- PLAN AND WRITE

PLANNING TABLE: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength.
Planned-Vocab-Term appears verbatim in the written file's lens or expertise.
Gap/Strength matches a label from INERTIA BASELINE.

SCOPE AUDIT:
  SCOPE AUDIT: PASS -- distinct Scope values >= 2. Proceed to PERSPECTIVE AUDIT.
  SCOPE AUDIT: FAIL -- fewer than 2 distinct scopes; expand role set or reassign before
    re-running. Do not proceed while SCOPE AUDIT is FAIL.

PERSPECTIVE AUDIT:
  PERSPECTIVE AUDIT: PASS -- distinct Perspective values >= 3. Proceed to write files.
  PERSPECTIVE AUDIT: FAIL -- fewer than 3 distinct perspectives; add roles or reassign
    before re-running. Do not proceed while PERSPECTIVE AUDIT is FAIL.

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
  EARLY INERTIA ANCHOR CHECK: FAIL -- revise inertia-advocate role file and re-run this
    check before proceeding. Remaining roles are blocked until EARLY INERTIA ANCHOR
    CHECK PASS.

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

EXIT GATE:
  STEP 3 EXIT: PASS -- SCOPE AUDIT PASS AND PERSPECTIVE AUDIT PASS AND all role files
    written AND all LENS AUDITS pass. Proceed to STEP 4.
  STEP 3 EXIT: FAIL -- complete failing audits or revise failing lens audits and re-check
    before proceeding. Do not start STEP 4 while STEP 3 EXIT is FAIL.

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
    INERTIA ANCHOR CHECK: PASS -- proceed to CROSS-ROLE SPREAD CHECK.
    INERTIA ANCHOR CHECK: FAIL -- revise inertia-advocate and re-run CHECK 1, 5A, 5B
      before proceeding. Do not run CROSS-ROLE SPREAD CHECK while INERTIA ANCHOR CHECK
      is FAIL.

  CROSS-ROLE SPREAD CHECK:
  For each non-inertia-advocate role, count how many reference at least one INERTIA
  BASELINE term (S or G label + phrase from STEP 1). If count = 0: FAIL -- at least
  one non-inertia-advocate role must reference an INERTIA BASELINE term verbatim.
    CROSS-ROLE SPREAD CHECK: PASS -- all verification complete. Proceed to close.
    CROSS-ROLE SPREAD CHECK: FAIL [N of M non-inertia roles reference a baseline term] --
      revise at least one non-inertia-advocate role to include an INERTIA BASELINE
      term and re-run LENS AUDIT for that role and CROSS-ROLE SPREAD CHECK before
      closing.

EXIT GATE:
  STEP 4 EXIT: PASS -- all checks pass AND INERTIA ANCHOR CHECK PASS AND
    CROSS-ROLE SPREAD CHECK PASS. Registry complete.
  STEP 4 EXIT: FAIL -- address failing checks and re-run before closing.

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

**Variation axis**: BASELINE PROPAGATION MAP (Axis-N) -- construct a propagation
assignment table immediately after INERTIA BASELINE, pre-assigning S/G terms to roles
**Hypothesis**: C-41's CROSS-ROLE SPREAD CHECK fires in Phase 7 (STEP 4) and catches
propagation failures post-hoc, requiring cascade revision. The baseline enforces
propagation at LENS AUDIT item 6 per role, but without upfront assignment an LLM may
write multiple roles before discovering that none reference a baseline term. A BASELINE
PROPAGATION MAP built at the end of STEP 1 (while S/G terms are fresh) assigns each
non-inertia candidate one S/G term to carry forward, converting CROSS-ROLE SPREAD CHECK
from a scan to a conformance check. Test: does upfront assignment reduce LENS AUDIT
item 6 failures and make CROSS-ROLE SPREAD CHECK deterministic without breaking any
other criterion?

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. The inertia-advocate is always included and written first. Roles
without a gap to fill (or a strength to defend) do not belong in this registry.

---

### STEP 1 -- INVENTORY AND BASELINE

Read all relevant files. Produce four artifacts before proceeding to STEP 2.

INPUT INVENTORY: table of Row-ID | Source file | Excerpt (<=20 words). Minimum 5 rows.
This table is the sole citation source for STEP 2 frame fill values -- no field may
cite the convergence summary or inertia baseline as its source.

INERTIA BASELINE: name the status quo solution. List exactly 2-3 strengths: S1: "{exact
phrase}", S2: "{exact phrase}", S3: "{exact phrase}". List exactly 2-3 gaps: G1: "{exact
phrase}", G2: "{exact phrase}", G3: "{exact phrase}". Each label-phrase pair is a
canonical anchor term for forward-reference in STEPS 2-4.

NON-GENERIC REQUIREMENT: each S-phrase must contain at least one noun or verb specific
to this domain that cannot appear unchanged in a different domain's INERTIA BASELINE.
These phrases fail this test regardless of context: "easy to use", "fast", "reliable",
"well-known", "familiar", "low cost", "widely adopted", "stable", "flexible". Apply the
same test to G-phrases. Revise any failing phrase before continuing. Confirm all phrases
pass; emit: NON-GENERIC CHECK: PASS before proceeding. STEP 4 INERTIA ANCHOR CHECK will
reference the phrases validated at STEP 1 NON-GENERIC CHECK.

CONVERGENCE SUMMARY: one paragraph covering domain function, users, technical concerns,
and strategic context.

BASELINE PROPAGATION MAP: immediately after writing the INERTIA BASELINE and before
building the CANDIDATE ROSTER in STEP 2, construct this assignment table:

  Role (tentative) | Assigned Baseline Term | Required verbatim in lens.verify
  inertia-advocate | S1, S2, S3             | S{N}: {exact phrase} for each label
  [candidate-A]    | G1                     | G1: {exact phrase}
  [candidate-B]    | G2                     | G2: {exact phrase}
  [candidate-C]    | G3 or S1              | {label}: {exact phrase}
  (add rows for all anticipated candidates -- at minimum, assign each G-term to one role)

Rules for the BASELINE PROPAGATION MAP:
  - inertia-advocate always carries S1, S2, S3.
  - Every G-term in INERTIA BASELINE must be assigned to at least one non-inertia role.
  - Role names in this table are tentative; update them when CANDIDATE ROSTER is finalized
    in STEP 2.
  - This map is the assignment contract: LENS AUDIT item 6 and CROSS-ROLE SPREAD CHECK
    in STEP 4 verify that each role's written file contains the assigned term verbatim.

EXIT GATE: INPUT INVENTORY >= 5 rows + INERTIA BASELINE complete (name + S1-S3 + G1-G3)
+ NON-GENERIC CHECK PASS + CONVERGENCE SUMMARY written + BASELINE PROPAGATION MAP
complete (every G-term assigned to at least one role).

---

### STEP 2 -- CANDIDATES AND FRAME FILL

CANDIDATE ROSTER: enumerate at least 5 candidates. For each: the INERTIA BASELINE label
it addresses (e.g., "defends S1", "addresses G2"), provisional perspective (product /
technical / inertia / domain / strategy / user), provisional scope (component / feature
/ system / cross-system / org). The inertia-advocate's reason-to-exist is "defends S1
(and S2, S3)"; every other role must reference at least one G-label. Update the
BASELINE PROPAGATION MAP role names if they have changed from tentative.
Table: Candidate | Addresses (S/G label) | Perspective | Scope

FRAME FILL: for each candidate, fill all five fields with one STEP 1 source citation
per field (format: `Phase 1 source: {row-id} = "{verbatim phrase}"`):
  orientation.frame | orientation.serves | lens.verify | lens.simplify |
  expertise.depth | expertise.relevance | scope | collaborates_with (2-3 named roles)

The inertia-advocate's lens.verify must include entries for each assigned S-term from
the BASELINE PROPAGATION MAP: "S{N}: {exact phrase from INERTIA BASELINE}". Fill the
inertia-advocate's block first. Then, before filling any other role, run this check:

  FRAME FILL PRE-ANCHOR CHECK:
  Re-read the inertia-advocate FRAME FILL lens.verify just written. Confirm at least one
  "S{N}: {phrase}" entry is present where {phrase} is the exact domain-specific phrase
  as validated at STEP 1 NON-GENERIC CHECK.
    FRAME FILL PRE-ANCHOR CHECK: PASS -- proceed to remaining roles.
    FRAME FILL PRE-ANCHOR CHECK: FAIL -- revise the inertia-advocate lens.verify in this
    block; do not start any other role's frame fill while this check is FAIL.

For each remaining role: include the assigned baseline term from the BASELINE PROPAGATION
MAP in lens.verify as "G{N}: {exact phrase}" or "S{N}: {exact phrase}". This is the
mechanism enforced by LENS AUDIT item 6 and CROSS-ROLE SPREAD CHECK.

EXIT GATE: CANDIDATE ROSTER complete + FRAME FILL complete (all candidates, all fields,
all citations) + FRAME FILL PRE-ANCHOR CHECK PASS + BASELINE PROPAGATION MAP role names
resolved to final candidate names.

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
  b. Include the BASELINE PROPAGATION MAP assigned term verbatim in lens.verify.
  c. Confirm collaborates_with includes the inertia-advocate by name.
  d. Emit inline LENS AUDIT:
     LENS AUDIT [{role-name}]:
       - verify[1] domain-specific: YES/NO + evidence
       - verify[2] domain-specific: YES/NO + evidence
       - simplify[1] concrete cut: YES/NO + evidence
       - Planned-Vocab-Term verbatim: YES/NO + location
       - collaborates_with inertia-advocate: YES/NO
       - references INERTIA BASELINE term per PROPAGATION MAP assignment
         ({label}: {phrase}): YES/NO + which term
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

  CROSS-ROLE SPREAD CHECK (conformance against BASELINE PROPAGATION MAP):
  For each non-inertia-advocate role, verify the assigned term from the BASELINE
  PROPAGATION MAP appears verbatim in the written lens.verify. Count how many roles
  satisfy their assignment. If count < total non-inertia roles with assignments: FAIL.
  Emit: CROSS-ROLE SPREAD CHECK: PASS/FAIL [N of M non-inertia roles satisfy propagation
        assignment, list any failing roles]

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

## V-04

**Variation axes**: EXPLICIT PHASE MAPPING TABLE (Axis-L) + FULL SELF-ROUTING GATES
(Axis-M)
**Hypothesis**: Axis-L satisfies C-42(a) declaratively; Axis-M extends dual-branch
routing to all gates. Together they produce a prompt where every structural boundary is
mapped (no inference required) and every gate is self-contained (no prose consultation
required). The mapping table and self-routing interact without conflict -- the mapping
table is a header artifact; the gate routing is per-gate text. Test: does the combination
produce a measurably cleaner audit chain than either axis alone?

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. The inertia-advocate is always included and written first. Roles
without a gap to fill (or a strength to defend) do not belong in this registry.

PHASE STRUCTURE MAPPING (this prompt uses 4 steps; canonical-phase equivalents):
  STEP 1 = canonical Phase 1 (Input Inventory) + canonical Phase 2 (Inertia Baseline)
  STEP 2 = canonical Phase 3 (Candidate Roster) + canonical Phase 4 (Frame Fill:
           inertia-advocate first, FRAME FILL PRE-ANCHOR CHECK, remaining roles)
  STEP 3 = canonical Phase 4 (Planning Table + Audits) + canonical Phase 6 (Write Files)
  STEP 4 = canonical Phase 7 (Verification Checks)

---

### STEP 1 -- INVENTORY AND BASELINE

Read all relevant files. Produce three artifacts before proceeding to STEP 2.

INPUT INVENTORY: table of Row-ID | Source file | Excerpt (<=20 words). Minimum 5 rows.
This table is the sole citation source for STEP 2 frame fill values -- no field may
cite the convergence summary or inertia baseline as its source.

INERTIA BASELINE: name the status quo solution. List exactly 2-3 strengths: S1: "{exact
phrase}", S2: "{exact phrase}", S3: "{exact phrase}". List exactly 2-3 gaps: G1: "{exact
phrase}", G2: "{exact phrase}", G3: "{exact phrase}". Each label-phrase pair is a
canonical anchor term for forward-reference in STEPS 2-4.

NON-GENERIC REQUIREMENT: each S-phrase must contain at least one noun or verb specific
to this domain that cannot appear unchanged in a different domain's INERTIA BASELINE.
These phrases fail this test regardless of context: "easy to use", "fast", "reliable",
"well-known", "familiar", "low cost", "widely adopted", "stable", "flexible". Apply the
same test to G-phrases. Revise any failing phrase before continuing. Confirm all phrases
pass; emit: NON-GENERIC CHECK: PASS. STEP 4 INERTIA ANCHOR CHECK will reference the
phrases validated at STEP 1 NON-GENERIC CHECK.

CONVERGENCE SUMMARY: one paragraph covering domain function, users, technical concerns,
and strategic context.

EXIT GATE:
  STEP 1 EXIT: PASS -- INPUT INVENTORY >= 5 rows AND INERTIA BASELINE complete (name +
    S1-S3 + G1-G3) AND NON-GENERIC CHECK PASS AND CONVERGENCE SUMMARY written.
    Proceed to STEP 2.
  STEP 1 EXIT: FAIL -- complete missing artifacts and re-run NON-GENERIC CHECK before
    proceeding. Do not start STEP 2 while STEP 1 EXIT is FAIL.

---

### STEP 2 -- CANDIDATES AND FRAME FILL

CANDIDATE ROSTER: enumerate at least 5 candidates. For each: the INERTIA BASELINE label
it addresses (e.g., "defends S1", "addresses G2"), provisional perspective (product /
technical / inertia / domain / strategy / user), provisional scope (component / feature
/ system / cross-system / org). The inertia-advocate's reason-to-exist is "defends S1
(and S2, S3)"; every other role must reference at least one G-label.
Table: Candidate | Addresses (S/G label) | Perspective | Scope

FRAME FILL: for each candidate, fill all five fields with one STEP 1 source citation
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
    FRAME FILL PRE-ANCHOR CHECK: PASS -- proceed to fill remaining roles.
    FRAME FILL PRE-ANCHOR CHECK: FAIL -- revise the inertia-advocate lens.verify in this
    block; do not fill any other role's frame fill while this check is FAIL.

For remaining roles, if the candidate's G-label maps to an INERTIA BASELINE gap, the
lens.verify should include at least one "G{N}: {phrase}" reference (advisory here,
enforced at STEP 3 lens audit).

EXIT GATE:
  STEP 2 EXIT: PASS -- CANDIDATE ROSTER complete (>= 5, all with S/G labels) AND
    FRAME FILL complete (all candidates, all fields, all citations) AND
    FRAME FILL PRE-ANCHOR CHECK PASS. Proceed to STEP 3.
  STEP 2 EXIT: FAIL -- complete missing frame fill or revise inertia-advocate and
    re-run FRAME FILL PRE-ANCHOR CHECK. Do not start STEP 3 while STEP 2 EXIT is FAIL.

---

### STEP 3 -- PLAN AND WRITE

PLANNING TABLE: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength.
Planned-Vocab-Term appears verbatim in the written file's lens or expertise.
Gap/Strength matches a label from INERTIA BASELINE.

SCOPE AUDIT:
  SCOPE AUDIT: PASS -- distinct Scope values >= 2. Proceed to PERSPECTIVE AUDIT.
  SCOPE AUDIT: FAIL -- fewer than 2 distinct scopes; expand or reassign and re-run.
    Do not proceed while SCOPE AUDIT is FAIL.

PERSPECTIVE AUDIT:
  PERSPECTIVE AUDIT: PASS -- distinct Perspective values >= 3. Proceed to write files.
  PERSPECTIVE AUDIT: FAIL -- fewer than 3 distinct perspectives; add roles or reassign
    and re-run. Do not proceed while PERSPECTIVE AUDIT is FAIL.

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
  EARLY INERTIA ANCHOR CHECK: FAIL -- revise inertia-advocate role file and re-run this
    check before proceeding. Remaining roles are blocked until EARLY INERTIA ANCHOR
    CHECK PASS.

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

EXIT GATE:
  STEP 3 EXIT: PASS -- SCOPE AUDIT PASS AND PERSPECTIVE AUDIT PASS AND all role files
    written AND all LENS AUDITS pass. Proceed to STEP 4.
  STEP 3 EXIT: FAIL -- address failing audits or revise failing lens audits before
    proceeding. Do not start STEP 4 while STEP 3 EXIT is FAIL.

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
    INERTIA ANCHOR CHECK: PASS -- proceed to CROSS-ROLE SPREAD CHECK.
    INERTIA ANCHOR CHECK: FAIL -- revise inertia-advocate and re-run CHECK 1, 5A, 5B.
      Do not run CROSS-ROLE SPREAD CHECK while INERTIA ANCHOR CHECK is FAIL.

  CROSS-ROLE SPREAD CHECK:
  For each non-inertia-advocate role, count how many reference at least one INERTIA
  BASELINE term (S or G label + phrase from STEP 1). If count = 0: FAIL -- at least
  one non-inertia-advocate role must reference an INERTIA BASELINE term verbatim.
    CROSS-ROLE SPREAD CHECK: PASS -- registry complete.
    CROSS-ROLE SPREAD CHECK: FAIL [N of M non-inertia roles reference a baseline term] --
      revise at least one non-inertia-advocate role to include an INERTIA BASELINE term,
      re-run that role's LENS AUDIT, and re-run CROSS-ROLE SPREAD CHECK before closing.

EXIT GATE:
  STEP 4 EXIT: PASS -- all checks pass AND INERTIA ANCHOR CHECK PASS AND
    CROSS-ROLE SPREAD CHECK PASS. Registry complete.
  STEP 4 EXIT: FAIL -- address failing checks before closing.

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

## V-05

**Variation axes**: EXPLICIT PHASE MAPPING TABLE (Axis-L) + FULL SELF-ROUTING GATES
(Axis-M) + BASELINE PROPAGATION MAP (Axis-N) -- full integration
**Hypothesis**: All three axes address distinct gaps: Axis-L eliminates C-42 inference
ambiguity; Axis-M makes every gate executor-complete; Axis-N converts C-41 enforcement
from post-hoc scan to upfront assignment. Together they produce the highest structural
defensibility -- every phase boundary is declared, every gate is self-routing, every
baseline term has a pre-committed owner. The interaction risk is prompt length: adding
the mapping table header, per-gate routing branches, and a propagation map table may
push the prompt to a length where LLMs begin to skip sections. Test: does full
integration hold all 35 criteria or does density introduce execution skipping?

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. The inertia-advocate is always included and written first. Roles
without a gap to fill (or a strength to defend) do not belong in this registry.

PHASE STRUCTURE MAPPING (this prompt uses 4 steps; canonical-phase equivalents):
  STEP 1 = canonical Phase 1 (Input Inventory) + canonical Phase 2 (Inertia Baseline)
  STEP 2 = canonical Phase 3 (Candidate Roster) + canonical Phase 4 (Frame Fill:
           inertia-advocate first, FRAME FILL PRE-ANCHOR CHECK, remaining roles)
  STEP 3 = canonical Phase 4 (Planning Table + Audits) + canonical Phase 6 (Write Files)
  STEP 4 = canonical Phase 7 (Verification Checks)

---

### STEP 1 -- INVENTORY AND BASELINE

Read all relevant files. Produce four artifacts before proceeding to STEP 2.

INPUT INVENTORY: table of Row-ID | Source file | Excerpt (<=20 words). Minimum 5 rows.
This table is the sole citation source for STEP 2 frame fill values -- no field may
cite the convergence summary or inertia baseline as its source.

INERTIA BASELINE: name the status quo solution. List exactly 2-3 strengths: S1: "{exact
phrase}", S2: "{exact phrase}", S3: "{exact phrase}". List exactly 2-3 gaps: G1: "{exact
phrase}", G2: "{exact phrase}", G3: "{exact phrase}". Each label-phrase pair is a
canonical anchor term for forward-reference in STEPS 2-4.

NON-GENERIC REQUIREMENT: each S-phrase must contain at least one noun or verb specific
to this domain that cannot appear unchanged in a different domain's INERTIA BASELINE.
These phrases fail this test regardless of context: "easy to use", "fast", "reliable",
"well-known", "familiar", "low cost", "widely adopted", "stable", "flexible". Apply the
same test to G-phrases. Revise any failing phrase before continuing. Confirm all phrases
pass; emit: NON-GENERIC CHECK: PASS. STEP 4 INERTIA ANCHOR CHECK will reference the
phrases validated at STEP 1 NON-GENERIC CHECK.

CONVERGENCE SUMMARY: one paragraph covering domain function, users, technical concerns,
and strategic context.

BASELINE PROPAGATION MAP: construct this assignment table immediately after writing the
INERTIA BASELINE, before building the CANDIDATE ROSTER in STEP 2:

  Role (tentative) | Assigned Baseline Term | Required verbatim in lens.verify
  inertia-advocate | S1, S2, S3             | S{N}: {exact phrase} for each label
  [candidate-A]    | G1                     | G1: {exact phrase}
  [candidate-B]    | G2                     | G2: {exact phrase}
  [candidate-C]    | G3 or S1              | {label}: {exact phrase}
  (add rows to cover every G-term -- at minimum each G-term must be assigned to one role)

Rules: inertia-advocate always carries S1/S2/S3. Every G-term must be assigned to at
least one non-inertia role. Role names are tentative; update in STEP 2 when candidates
are finalized. This map is the conformance contract for LENS AUDIT item 6 and
CROSS-ROLE SPREAD CHECK in STEP 4.

EXIT GATE:
  STEP 1 EXIT: PASS -- INPUT INVENTORY >= 5 rows AND INERTIA BASELINE complete (name +
    S1-S3 + G1-G3) AND NON-GENERIC CHECK PASS AND CONVERGENCE SUMMARY written AND
    BASELINE PROPAGATION MAP complete (every G-term assigned). Proceed to STEP 2.
  STEP 1 EXIT: FAIL -- complete missing artifacts, re-run NON-GENERIC CHECK, and complete
    BASELINE PROPAGATION MAP before proceeding. Do not start STEP 2 while STEP 1 EXIT
    is FAIL.

---

### STEP 2 -- CANDIDATES AND FRAME FILL

CANDIDATE ROSTER: enumerate at least 5 candidates. For each: the INERTIA BASELINE label
it addresses (e.g., "defends S1", "addresses G2"), provisional perspective (product /
technical / inertia / domain / strategy / user), provisional scope (component / feature
/ system / cross-system / org). The inertia-advocate's reason-to-exist is "defends S1
(and S2, S3)"; every other role must reference at least one G-label. Update the
BASELINE PROPAGATION MAP role names to match final candidate names.
Table: Candidate | Addresses (S/G label) | Perspective | Scope

FRAME FILL: for each candidate, fill all five fields with one STEP 1 source citation
per field (format: `Phase 1 source: {row-id} = "{verbatim phrase}"`):
  orientation.frame | orientation.serves | lens.verify | lens.simplify |
  expertise.depth | expertise.relevance | scope | collaborates_with (2-3 named roles)

The inertia-advocate's lens.verify must include entries for each assigned S-term from
the BASELINE PROPAGATION MAP: "S{N}: {exact phrase from INERTIA BASELINE}". Fill the
inertia-advocate's block first. Then, before filling any other role, run this check:

  FRAME FILL PRE-ANCHOR CHECK:
  Re-read the inertia-advocate FRAME FILL lens.verify just written. Confirm at least one
  "S{N}: {phrase}" entry is present where {phrase} is the exact domain-specific phrase
  as validated at STEP 1 NON-GENERIC CHECK.
    FRAME FILL PRE-ANCHOR CHECK: PASS -- proceed to fill remaining roles.
    FRAME FILL PRE-ANCHOR CHECK: FAIL -- revise the inertia-advocate lens.verify in this
    block; do not fill any other role's frame fill while this check is FAIL.

For each remaining role: include the assigned baseline term from the BASELINE PROPAGATION
MAP in lens.verify as the required verbatim entry (G{N}: {exact phrase} or S{N}: {exact
phrase}). This satisfies LENS AUDIT item 6 and contributes to CROSS-ROLE SPREAD CHECK.

EXIT GATE:
  STEP 2 EXIT: PASS -- CANDIDATE ROSTER complete (>= 5, all with S/G labels) AND
    FRAME FILL complete (all candidates, all fields, all citations) AND
    FRAME FILL PRE-ANCHOR CHECK PASS AND BASELINE PROPAGATION MAP role names resolved.
    Proceed to STEP 3.
  STEP 2 EXIT: FAIL -- complete missing frame fill, revise inertia-advocate, or resolve
    PROPAGATION MAP role names and re-run FRAME FILL PRE-ANCHOR CHECK. Do not start
    STEP 3 while STEP 2 EXIT is FAIL.

---

### STEP 3 -- PLAN AND WRITE

PLANNING TABLE: Role | Scope | Perspective | Planned-Vocab-Term | Gap/Strength.
Planned-Vocab-Term appears verbatim in the written file's lens or expertise.
Gap/Strength matches a label from INERTIA BASELINE.

SCOPE AUDIT:
  SCOPE AUDIT: PASS -- distinct Scope values >= 2. Proceed to PERSPECTIVE AUDIT.
  SCOPE AUDIT: FAIL -- fewer than 2 distinct scopes; expand or reassign and re-run.
    Do not proceed while SCOPE AUDIT is FAIL.

PERSPECTIVE AUDIT:
  PERSPECTIVE AUDIT: PASS -- distinct Perspective values >= 3. Proceed to write files.
  PERSPECTIVE AUDIT: FAIL -- fewer than 3 distinct perspectives; add roles or reassign
    and re-run. Do not proceed while PERSPECTIVE AUDIT is FAIL.

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
  EARLY INERTIA ANCHOR CHECK: FAIL -- revise inertia-advocate role file and re-run this
    check before proceeding. Remaining roles are blocked until EARLY INERTIA ANCHOR
    CHECK PASS.

WRITE REMAINING ROLES in planning table order. For each:
  a. Write the file from STEP 2 frame fill values. Planned-Vocab-Term must appear verbatim.
  b. Include the BASELINE PROPAGATION MAP assigned term verbatim in lens.verify.
  c. Confirm collaborates_with includes the inertia-advocate by name.
  d. Emit inline LENS AUDIT:
     LENS AUDIT [{role-name}]:
       - verify[1] domain-specific: YES/NO + evidence
       - verify[2] domain-specific: YES/NO + evidence
       - simplify[1] concrete cut: YES/NO + evidence
       - Planned-Vocab-Term verbatim: YES/NO + location
       - collaborates_with inertia-advocate: YES/NO
       - references INERTIA BASELINE term per PROPAGATION MAP assignment
         ({label}: {phrase}): YES/NO + which term
     Revise before writing the next role if any item is NO.

EXIT GATE:
  STEP 3 EXIT: PASS -- SCOPE AUDIT PASS AND PERSPECTIVE AUDIT PASS AND all role files
    written AND all LENS AUDITS pass. Proceed to STEP 4.
  STEP 3 EXIT: FAIL -- address failing audits or revise failing lens audits before
    proceeding. Do not start STEP 4 while STEP 3 EXIT is FAIL.

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
    INERTIA ANCHOR CHECK: PASS -- proceed to CROSS-ROLE SPREAD CHECK.
    INERTIA ANCHOR CHECK: FAIL -- revise inertia-advocate and re-run CHECK 1, 5A, 5B.
      Do not run CROSS-ROLE SPREAD CHECK while INERTIA ANCHOR CHECK is FAIL.

  CROSS-ROLE SPREAD CHECK (conformance against BASELINE PROPAGATION MAP):
  For each non-inertia-advocate role, verify the assigned term from the BASELINE
  PROPAGATION MAP appears verbatim in the written lens.verify. Count conforming roles.
    CROSS-ROLE SPREAD CHECK: PASS [N of M non-inertia roles satisfy propagation
      assignment, list all] -- registry complete.
    CROSS-ROLE SPREAD CHECK: FAIL [N of M non-inertia roles satisfy assignment; list
      failing roles] -- revise each failing role to include its assigned INERTIA BASELINE
      term, re-run that role's LENS AUDIT, and re-run CROSS-ROLE SPREAD CHECK before
      closing.

EXIT GATE:
  STEP 4 EXIT: PASS -- all checks pass AND INERTIA ANCHOR CHECK PASS AND
    CROSS-ROLE SPREAD CHECK PASS. Registry complete.
  STEP 4 EXIT: FAIL -- address failing checks before closing.

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
