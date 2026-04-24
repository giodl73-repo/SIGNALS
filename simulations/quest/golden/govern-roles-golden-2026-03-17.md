Written to `simulations/quest/golden/crew-roles-golden-2026-03-17.md`.

**What's in the file:**

- **Frontmatter**: score 10.0, GOLDEN status, v15 rubric, 20 rounds
- **Prompt body**: V-05 simplified (11% reduction applied) — dead-weight sentences removed, no criterion coverage lost
- **What made it golden** (5 patterns):
  1. PHASE STRUCTURE MAPPING table eliminates C-42 inference ambiguity
  2. BASELINE PROPAGATION MAP converts C-41/CROSS-ROLE SPREAD CHECK from scan to per-role conformance
  3. System-wide EXIT GATE self-routing makes the prompt executor-complete at every boundary
  4. Triple inertia anchor chain (FRAME FILL PRE-ANCHOR + EARLY + final) catches drift at write-time
  5. Full-axis integration held without density failure — the 89% that survived simplification was structurally load-bearing
- **Final rubric summary**: all 45 criteria (5 essential + 3 recommended + 37 aspirational) with introduction round
stry.

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
G-phrases. Revise any failing phrase before continuing. Confirm all phrases pass; emit:
NON-GENERIC CHECK: PASS.

CONVERGENCE SUMMARY: one paragraph covering domain function, users, technical concerns,
and strategic context.

BASELINE PROPAGATION MAP: construct this assignment table immediately after writing the
INERTIA BASELINE, before building the CANDIDATE ROSTER in STEP 2:

  Role (tentative) | Assigned Baseline Term | Required verbatim in lens.verify
  inertia-advocate | S1, S2, S3             | S{N}: {exact phrase} for each label
  [candidate-A]    | G1                     | G1: {exact phrase}
  [candidate-B]    | G2                     | G2: {exact phrase}
  [candidate-C]    | G3 or S1               | {label}: {exact phrase}
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
  Re-read the inertia-advocate lens.verify. Confirm at least one "S{N}: {phrase}"
  entry is present (exact domain-specific phrase from NON-GENERIC CHECK).
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
lens.verify. Confirm at least one "S{N}: {phrase}" entry verbatim.
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

---

## What Made It Golden

V-05 is the full integration of three axes (L + M + N), each closing a distinct structural
gap the R19 baseline left open.

**1. PHASE STRUCTURE MAPPING table (Axis-L)**
An explicit 4-row table maps each STEP to its canonical-phase equivalents at the prompt
header. This converts C-42 from a scorer judgment call ("is the phase placement
unambiguously inferrable?") into a mechanical check: the table either exists and is
correct, or it does not. The R19 baseline relied on positional inference (C-42(b)), which
is correct but fragile under novel domains or strict scorers.

**2. BASELINE PROPAGATION MAP (Axis-N)**
Rather than scanning post-hoc in STEP 4 for baseline-term coverage, the MAP pre-assigns
a specific S/G label to every role at the end of STEP 1 -- before any candidate is
enumerated. This shifts CROSS-ROLE SPREAD CHECK from open scan ("does any role reference
a baseline term?") to per-role conformance report ("does this role carry its MAP-assigned
term?"). The MAP also propagates into LENS AUDIT item 6 and the STEP 2 remaining-role
instruction, creating three enforcement points instead of one.

**3. System-wide EXIT GATE self-routing (Axis-M)**
C-43 required dual-branch routing only at EARLY INERTIA ANCHOR CHECK. V-05 extends this
to every structural boundary: all four STEP EXIT GATEs, SCOPE AUDIT, PERSPECTIVE AUDIT,
INERTIA ANCHOR CHECK, and CROSS-ROLE SPREAD CHECK each emit a PASS->continue branch and
a FAIL->remediate+recheck branch. An executor can resolve any gate result to its next
action without reading surrounding prose. The prompt is executor-complete at every
structural boundary.

**4. Triple inertia anchor chain**
FRAME FILL PRE-ANCHOR CHECK (STEP 2, write-time) + EARLY INERTIA ANCHOR CHECK (STEP 3,
file-write gate) + INERTIA ANCHOR CHECK (STEP 4, final verification) creates a three-
checkpoint chain. Anchor drift is caught at the moment of introduction, not after all
files are written. Each checkpoint names the expected format (S{N}: {exact phrase})
rather than leaving verification open-ended.

**5. Full-axis integration without density failure**
The hypothesis risk for V-05 was that combining all three axes would push prompt length
to where LLMs begin skipping sections. R20 showed this did not occur: all 35 v14
criteria pass. Simplification then removed 11% of words (explanatory justifications,
duplicate instructions, forward-reference reassurances) without losing criterion
coverage. The 89% that remained was structurally load-bearing.

---

## Final Rubric Criteria Summary (v15)

**Formula**: aspirational_pass / 37 * 10 = 0.270 pts per PASS

### Essential (5)

| ID | Criterion |
|----|-----------|
| C-01 | All 5 required role fields present (name, orientation, lens, simplify, collaborates_with) |
| C-02 | Inertia-advocate role present with orientation: status-quo advocate |
| C-03 | Output path is .roles/{domain}/ |
| C-04 | Role content is domain-specific (no generic placeholders) |
| C-05 | Minimum 3 roles in the role-set |

### Recommended (3)

| ID | Criterion |
|----|-----------|
| C-06 | lens.verify items are actionable (each item is a testable check, not a description) |
| C-07 | collaborates_with references resolve to named roles in the same role-set |
| C-08 | Perspective diversity: roles represent distinct functional or stakeholder viewpoints |

### Aspirational (37)

| ID | Criterion | Introduced |
|----|-----------|------------|
| C-09 | INPUT INVENTORY table with Row-ID/Source/Excerpt; >= 5 rows; EXIT GATE before STEP 2 | R1 |
| C-10 | Input inventory sole citation source; frame fill may not cite summary or baseline | R2 |
| C-11 | STEP 1 EXIT GATE states INPUT INVENTORY >= 5 rows as exit condition | R3 |
| C-12 | S1/S2/S3 in S{N}: "{exact phrase}" format | R4 |
| C-13 | G1/G2/G3 in G{N}: "{exact phrase}" format | R4 |
| C-14 | CANDIDATE ROSTER with S/G label column; inertia-advocate "defends S1 (and S2, S3)" | R5 |
| C-15 | FRAME FILL all five fields with Phase 1 source: {row-id} = "{verbatim phrase}" citations | R5 |
| C-16 | PLANNING TABLE: Role / Scope / Perspective / Planned-Vocab-Term / Gap-Strength | R6 |
| C-17 | SCOPE AUDIT with threshold (< 2: fail) + consequence | R6 |
| C-18 | PERSPECTIVE AUDIT with threshold (< 3: fail) + consequence | R6 |
| C-19 | "WRITE INERTIA-ADVOCATE (first)" labeled write instruction | R7 |
| C-20 | "Emit: INERTIA-ADVOCATE WRITTEN: {path}" stated | R7 |
| C-21 | LENS AUDIT block with all 6 check items per non-inertia role | R8 |
| C-22 | Item 1: verify[1] domain-specific: YES/NO + evidence | R8 |
| C-23 | Item 2: verify[2] domain-specific: YES/NO + evidence | R8 |
| C-24 | Item 3: simplify[1] concrete cut: YES/NO + evidence | R8 |
| C-25 | Item 4: Planned-Vocab-Term verbatim: YES/NO + location | R8 |
| C-26 | CHECK 1 per file with PASS/FAIL [missing field] emission | R9 |
| C-27 | CHECK 2: inertia-advocate orientation check | R9 |
| C-28 | CHECK 3A: scope spread >= 2 | R9 |
| C-29 | CHECK 3B: ROLE-REPLACE fires on scope mismatch | R9 |
| C-30 | CHECK 4A: all planning table roles written | R9 |
| C-31 | CHECK 4B: Planned-Vocab-Terms verbatim; ROLE-REPLACE fires on mismatch | R9 |
| C-32 | CHECK 5A: written fields match frame fill per role | R9 |
| C-33 | CHECK 5B: citations verifiable against INPUT INVENTORY; per-violation emission | R9 |
| C-34 | CHECK 6: no generic placeholders | R9 |
| C-35 | CHECK 7: all files at .roles/{domain}/ | R9 |
| C-36 | CHECK 8: perspective spread >= 3 | R9 |
| C-37 | INERTIA ANCHOR CHECK re-reads lens.verify; PASS/FAIL emission; FAIL triggers revision | R14 |
| C-38 | EARLY INERTIA ANCHOR CHECK with explicit PASS/FAIL label + blocking statement | R15 |
| C-39 | FRAME FILL PRE-ANCHOR CHECK in STEP 2; explicit label emitted; FAIL halts frame fill | R16 |
| C-40 | NON-GENERIC REQUIREMENT in STEP 1 with operational def + negative-example list + NON-GENERIC CHECK PASS emission | R17 |
| C-41 | LENS AUDIT item 6: references INERTIA BASELINE term per role; CROSS-ROLE SPREAD CHECK with PASS/FAIL [N of M] emission | R18 |
| C-42 | C-42(a): explicit PHASE STRUCTURE MAPPING table at header mapping each STEP to canonical phases | R19/R20 |
| C-43 | EARLY INERTIA ANCHOR CHECK: PASS->proceed; FAIL->revise + recheck; remaining roles blocked until PASS | R19 |
| C-44 | System-wide EXIT GATE self-routing: every blocking gate (all STEP EXIT GATEs, SCOPE AUDIT, PERSPECTIVE AUDIT, INERTIA ANCHOR CHECK, CROSS-ROLE SPREAD CHECK) emits PASS->continue and FAIL->remediate branches | R20 |
| C-45 | BASELINE PROPAGATION MAP: table at STEP 1 pre-assigns S/G term per role; LENS AUDIT item 6 and CROSS-ROLE SPREAD CHECK verify per-role conformance against MAP; MAP completeness is STEP 1 EXIT GATE condition | R20 |
