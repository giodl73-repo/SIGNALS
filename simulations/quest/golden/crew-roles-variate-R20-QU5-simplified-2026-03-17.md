---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 20
variant: QU5-simplified
source: crew-roles-variate-R20-2026-03-17.md (V-05)
rubric: crew-roles-rubric-v15-2026-03-17.md
---

# crew-roles -- QU5 Simplified (R20 V-05)

Minimal golden prompt: R20 V-05 reduced by QU5 simplification pass.
All essential rubric criteria preserved. 20-40% word reduction attempted.

## Simplification Report

**Removed (no execution work being done):**

| # | Location | Removed text | Words |
|---|----------|--------------|-------|
| R1 | INERTIA BASELINE | "Each label-phrase pair is a canonical anchor term for forward-reference in STEPS 2-4." | 14 |
| R2 | NON-GENERIC REQUIREMENT | "regardless of context" | 3 |
| R3 | NON-GENERIC REQUIREMENT | "STEP 4 INERTIA ANCHOR CHECK will reference the phrases validated at STEP 1 NON-GENERIC CHECK." | 16 |
| R4 | BASELINE PROPAGATION MAP | ", before building the CANDIDATE ROSTER in STEP 2" | 10 |
| R5 | BASELINE PROPAGATION MAP Rules | "Role names are tentative; update in STEP 2 when candidates are finalized." | 12 |
| R6 | BASELINE PROPAGATION MAP Rules | "This map is the conformance contract for LENS AUDIT item 6 and CROSS-ROLE SPREAD CHECK in STEP 4." | 17 |
| R7 | PHASE STRUCTURE MAPPING STEP 2 | ": inertia-advocate first, FRAME FILL PRE-ANCHOR CHECK, remaining roles" (internal detail) | 9 |
| R8 | EARLY INERTIA ANCHOR CHECK | "If STEP 2 FRAME FILL PRE-ANCHOR CHECK PASS was correctly emitted, this is confirmation." | 15 |
| R9 | STEP 4 INERTIA ANCHOR CHECK | "If not: revise file and re-run CHECK 1, 5A, 5B for the inertia-advocate." (duplicates FAIL branch) | 15 |
| R10 | STEP 4 INERTIA ANCHOR CHECK | "(label + exact phrase, as validated at STEP 1 NON-GENERIC CHECK)" (implied) | 12 |
| R11 | CROSS-ROLE SPREAD CHECK | "(conformance against BASELINE PROPAGATION MAP)" | 5 |
| R12 | CROSS-ROLE SPREAD CHECK | "Count conforming roles." (implied by N of M format) | 3 |
| R13 | CANDIDATE ROSTER | "(e.g., "defends S1", "addresses G2")" | 6 |

**Compressed (shorter phrasing, same meaning):**

| # | Location | Change | Saved |
|---|----------|--------|-------|
| C1 | FRAME FILL PRE-ANCHOR CHECK body | Removed "just written" + compressed "where {phrase} is the exact domain-specific phrase as validated at STEP 1 NON-GENERIC CHECK" → "(exact domain-specific phrase)" | 13 |
| C2 | STEP 2 remaining roles | "include the assigned baseline term from the BASELINE PROPAGATION MAP in lens.verify as the required verbatim entry (G{N}: {exact phrase} or S{N}: {exact phrase}). This satisfies LENS AUDIT item 6 and contributes to CROSS-ROLE SPREAD CHECK." → "include the BASELINE PROPAGATION MAP assigned term verbatim in lens.verify." | 27 |
| C3 | WRITE INERTIA-ADVOCATE | "(same phrase validated at STEP 1 NON-GENERIC CHECK)" removed; merged requirement sentence | 9 |
| C4 | EARLY INERTIA ANCHOR CHECK body | "re-read the inertia-advocate's written lens.verify. Confirm at least one "S{N}: {phrase}" entry appears verbatim (label + exact domain-specific phrase from INERTIA BASELINE)." → "Re-read the inertia-advocate's written lens.verify. Confirm at least one "S{N}: {exact phrase from INERTIA BASELINE}" appears verbatim." | 7 |
| C5 | STEP 2 EXIT GATE FAIL | Compressed remediation list | 7 |
| C6 | STEP 3 EXIT GATE FAIL | Compressed remediation instruction | 9 |

**Total removed: ~219 words. Original: 1675. Simplified: ~1456. Reduction: ~13.1%**

**Why 20% was not reached**: The prompt is structurally dense — every sentence is either
a produce-this instruction, a format constraint, a routing gate, or a check item. The
reinforcement web (S{N}: {phrase} appears at 8 checkpoints) is rubric-required, not
redundant. Reducing below 13% would require removing routing branches (C-44) or
inertia-anchor checkpoints (C-43), which are essential criteria.

**All essential criteria still pass: YES**

---

## Simplified Prompt Body

```
Generate a typed role registry for the domain named in `for:`. Write one markdown file
per role at `.roles/{domain}/`. Each role has: name, orientation (frame + serves),
lens (verify questions + simplify rules), expertise (depth + relevance), scope,
collaborates_with. The inertia-advocate is always included and written first. Roles
without a gap to fill (or a strength to defend) do not belong in this registry.

PHASE STRUCTURE MAPPING (this prompt uses 4 steps; canonical-phase equivalents):
  STEP 1 = canonical Phase 1 (Input Inventory) + canonical Phase 2 (Inertia Baseline)
  STEP 2 = canonical Phase 3 (Candidate Roster) + canonical Phase 4 (Frame Fill)
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
phrase}", G2: "{exact phrase}", G3: "{exact phrase}".

NON-GENERIC REQUIREMENT: each S-phrase must contain at least one noun or verb specific
to this domain that cannot appear unchanged in a different domain's INERTIA BASELINE.
These phrases fail this test: "easy to use", "fast", "reliable", "well-known",
"familiar", "low cost", "widely adopted", "stable", "flexible". Apply the same test to
G-phrases. Revise any failing phrase before continuing. Confirm all phrases pass;
emit: NON-GENERIC CHECK: PASS.

CONVERGENCE SUMMARY: one paragraph covering domain function, users, technical concerns,
and strategic context.

BASELINE PROPAGATION MAP: construct this assignment table immediately after writing the
INERTIA BASELINE:

  Role (tentative) | Assigned Baseline Term | Required verbatim in lens.verify
  inertia-advocate | S1, S2, S3             | S{N}: {exact phrase} for each label
  [candidate-A]    | G1                     | G1: {exact phrase}
  [candidate-B]    | G2                     | G2: {exact phrase}
  [candidate-C]    | G3 or S1              | {label}: {exact phrase}
  (add rows to cover every G-term -- at minimum each G-term must be assigned to one role)

Rules: inertia-advocate always carries S1/S2/S3. Every G-term must be assigned to at
least one non-inertia role.

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
it addresses, provisional perspective (product / technical / inertia / domain /
strategy / user), provisional scope (component / feature / system / cross-system / org).
The inertia-advocate's reason-to-exist is "defends S1 (and S2, S3)"; every other role
must reference at least one G-label. Update the BASELINE PROPAGATION MAP role names to
match final candidate names.
Table: Candidate | Addresses (S/G label) | Perspective | Scope

FRAME FILL: for each candidate, fill all role fields with one STEP 1 source citation
per field (format: `Phase 1 source: {row-id} = "{verbatim phrase}"`):
  orientation.frame | orientation.serves | lens.verify | lens.simplify |
  expertise.depth | expertise.relevance | scope | collaborates_with (2-3 named roles)

The inertia-advocate's lens.verify must include entries for each assigned S-term from
the BASELINE PROPAGATION MAP: "S{N}: {exact phrase from INERTIA BASELINE}". Fill the
inertia-advocate's block first. Then, before filling any other role, run this check:

  FRAME FILL PRE-ANCHOR CHECK:
  Re-read the inertia-advocate FRAME FILL lens.verify. Confirm at least one
  "S{N}: {phrase}" entry is present where {phrase} is the exact domain-specific phrase.
    FRAME FILL PRE-ANCHOR CHECK: PASS -- proceed to fill remaining roles.
    FRAME FILL PRE-ANCHOR CHECK: FAIL -- revise the inertia-advocate lens.verify in this
    block; do not fill any other role's frame fill while this check is FAIL.

For each remaining role: include the BASELINE PROPAGATION MAP assigned term verbatim
in lens.verify.

EXIT GATE:
  STEP 2 EXIT: PASS -- CANDIDATE ROSTER complete (>= 5, all with S/G labels) AND
    FRAME FILL complete (all candidates, all fields, all citations) AND
    FRAME FILL PRE-ANCHOR CHECK PASS AND BASELINE PROPAGATION MAP role names resolved.
    Proceed to STEP 3.
  STEP 2 EXIT: FAIL -- complete missing frame fill, resolve PROPAGATION MAP role names,
    and re-run FRAME FILL PRE-ANCHOR CHECK. Do not start STEP 3 while STEP 2 EXIT
    is FAIL.

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
"S{N}: {phrase}" entry verbatim from INERTIA BASELINE. Planned-Vocab-Term must appear
verbatim. Emit: INERTIA-ADVOCATE WRITTEN: {path}

EARLY INERTIA ANCHOR CHECK (blocking gate): Re-read the inertia-advocate's written
lens.verify. Confirm at least one "S{N}: {exact phrase from INERTIA BASELINE}" appears
verbatim.
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
  STEP 3 EXIT: FAIL -- resolve failing audits/lens audits. Do not start STEP 4 while
    STEP 3 EXIT is FAIL.

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
  entry verbatim.
    INERTIA ANCHOR CHECK: PASS -- proceed to CROSS-ROLE SPREAD CHECK.
    INERTIA ANCHOR CHECK: FAIL -- revise inertia-advocate and re-run CHECK 1, 5A, 5B.
      Do not run CROSS-ROLE SPREAD CHECK while INERTIA ANCHOR CHECK is FAIL.

  CROSS-ROLE SPREAD CHECK:
  For each non-inertia-advocate role, verify the assigned term from the BASELINE
  PROPAGATION MAP appears verbatim in the written lens.verify.
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
