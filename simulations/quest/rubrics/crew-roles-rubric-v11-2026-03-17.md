Reading the R16 scorecard differential analysis carefully before writing.

**Pattern extracted from R16:**

- **C-36** from V-03/V-04/V-05: Named INERTIA BASELINE artifact in Phase 2 (tool + strengths + gaps) + INERTIA ANCHOR CHECK in Phase 7 verifying verbatim strength terms propagate to `lens.verify` → closes the structural gap in C-10, C-10 moves PARTIAL → PASS

C-34 and C-35 are already in v10; the only new aspirational criterion is C-36. Formula updates to `/28 * 10`.

---

```markdown
# crew-roles rubric — v11

## Changes from v10

One new aspirational criterion extracted from R16 variations V-03, V-04, V-05. Closes the
structural gap that kept C-10 at PARTIAL in V-01 and V-02.

**C-36 — INERTIA BASELINE artifact + INERTIA ANCHOR CHECK** (from V-03/V-04/V-05):
C-10 (aspirational) requires domain-grounded inertia analysis. Asking "What is the status
quo?" inside CONVERGENCE SUMMARY satisfies C-10 only if the response happens to enumerate
both strengths and gaps — no structural mechanism separates them or ensures verbatim terms
survive to Phase 7 validation. V-01 and V-02 each score PARTIAL on C-10 for this reason.
The sufficient condition is a named artifact: INERTIA BASELINE fires in Phase 2, recording
(a) the named incumbent tool or practice, (b) a "strengths it has" enumeration, and (c) a
"gaps it does not solve" enumeration. INERTIA ANCHOR CHECK then fires in Phase 7, verifying
that at least one verbatim strength term from INERTIA BASELINE appears in at least one
written role's lens.verify field. Advancing past Phase 2 without an INERTIA BASELINE
artifact is a blocking error. C-10 requires domain-grounded inertia analysis; C-36 requires
the INERTIA BASELINE artifact ran in Phase 2 and INERTIA ANCHOR CHECK confirmed verbatim
propagation in Phase 7. V-03 (R16): INERTIA BASELINE fires in Phase 2 with named tool,
strengths, and gaps; INERTIA ANCHOR CHECK verifies verbatim propagation; C-10 moves from
PARTIAL to PASS.

**Formula updated**: `aspirational_pass / 28 * 10` (was `/27`). Each full pass = 0.357 pts.

---

## Criteria (full table)

### Essential (5)
C-01 All 5 fields | C-02 Inertia-advocate present | C-03 Correct output path |
C-04 Domain specificity | C-05 Minimum 3 roles

### Recommended (3)
C-06 Lens actionability | C-07 Collaborates_with resolves | C-08 Perspective diversity

### Aspirational (28)

| ID | Criterion | Introduced |
|----|-----------|------------|
| C-09 | Scope gradient | v1 |
| C-10 | Inertia domain-grounded | v1 |
| C-11 | Vocabulary-forced-field | v2 / R1 |
| C-12 | INPUT INVENTORY phase | v3 / R2 |
| C-13 | Slot-level source citation | v3 / R2 |
| C-14 | Planning table before authoring | v3 / R2 |
| C-15 | CHECK 1 input completeness | v4 / R3 |
| C-16 | CHECK 2 inertia-advocate present | v4 / R3 |
| C-17 | CHECK 3A scope re-validation | v4 / R3 |
| C-18 | CHECK 3B vocab binding re-validation | v4 / R3 |
| C-19 | CHECK 4A scope post-write | v4 / R3 |
| C-20 | CHECK 4B vocab binding post-write | v4 / R3 |
| C-21 | CHECK 5 frame-slot match | v4 / R3 |
| C-22 | CHECK 6 output-path verification | v4 / R3 |
| C-23 | CHECK 7 file-count match | v5 / R5 |
| C-24 | Re-evaluation after role replacement | v6 / R7 |
| C-25 | Source citation in FRAME FILL output | v6 / R7 |
| C-26 | FRAME FILL gate blocks Phase 6 | v7 / R9 |
| C-27 | Forensic source-phrase tracing | v7 / R9 |
| C-28 | SCOPE AUDIT gate | v8 / R11 |
| C-29 | Gap-Addressed column in planning table | v8 / R11 |
| C-30 | Inertia-first gate | v9 / R13 |
| C-31 | Vocab binding column | v9 / R13 |
| C-32 | Inline LENS AUDIT | v9 / R13 |
| C-33 | PERSPECTIVE AUDIT + CHECK 8 re-validation | v10 / R15 |
| C-34 | Per-slot Phase 1 source + CHECK 5A/5B split | v10 / R15 |
| C-35 | ROLE-REPLACE sub-procedure (4 fields + CONFIRMED gate) | v10 / R15 |
| C-36 | INERTIA BASELINE artifact + INERTIA ANCHOR CHECK | v11 / R16 |

---

## Criterion Definitions

### Essential

**C-01 — All 5 fields**
Every written role file contains all five required field groups: name, orientation,
perspective, lens (verify + simplify), and collaborates_with. Missing any field group is a
blocking failure regardless of content quality.

**C-02 — Inertia-advocate present**
The written role set includes exactly one role whose orientation value is status-quo advocate.
Zero inertia-advocate roles or more than one is a blocking failure.

**C-03 — Correct output path**
All role files are written to `.roles/{domain}/`. Writing to any other path is a
blocking failure.

**C-04 — Domain specificity**
Role content is specific to the domain supplied in the input. Generic or domain-agnostic
role descriptions that could apply to any domain fail this criterion.

**C-05 — Minimum 3 roles**
The written role set contains at least 3 roles. Fewer than 3 is a blocking failure.

---

### Recommended

**C-06 — Lens actionability**
Each role's lens fields are actionable and non-generic. lens.verify contains a verifiable
claim or test; lens.simplify contains a concrete simplification instruction. LENS AUDIT fires
inline after each role is authored; verify[1]/[2] and simplify[1] are checked per role.

**C-07 — Collaborates_with resolves**
Each role's collaborates_with field lists 2–3 role names drawn from the CANDIDATE ROSTER, not
generic titles or placeholder text. Names must be verifiable against planned or written roles.

**C-08 — Perspective diversity**
The written role set includes ≥ 3 distinct perspective values. PERSPECTIVE AUDIT gate fires
before Phase 6 (see C-33). CHECK 8 in Phase 7 re-validates ≥ 3 distinct perspective values
from the actual written files.

---

### Aspirational

**C-09 — Scope gradient**
The planned role set includes ≥ 2 distinct scope values (e.g., narrow + broad). SCOPE AUDIT
gate fires before Phase 6 (see C-28); CHECK 3A re-validates the scope distribution from the
planning table before authoring begins.

**C-10 — Inertia domain-grounded**
The inertia-advocate role is grounded in a named incumbent tool or practice specific to the
domain. The inertia analysis separates what the incumbent does well (strengths) from what it
fails to address (gaps). See C-36 for the structural enforcement mechanism.

**C-11 — Vocabulary-forced-field**
The skill injects domain vocabulary into at least one field of every written role. A
Planned-Vocab-Term column in the Phase 5 planning table maps each role to its required term.
CHECK 4B verifies verbatim term presence in the written file.

**C-12 — INPUT INVENTORY phase**
A named INPUT INVENTORY phase runs before any analysis or planning. It enumerates all
supplied inputs by row ID and type, confirming completeness before downstream phases open.

**C-13 — Slot-level source citation**
Each FRAME FILL slot includes a source citation tracing it to a specific Phase 1 input row.
See C-25 and C-34 for progressively stronger structural requirements.

**C-14 — Planning table before authoring**
A structured planning table is produced before any file is authored. The table includes at
minimum: role name, orientation, perspective, planned vocab term. Phase 6 cannot open until
the planning table is complete.

**C-15 — CHECK 1 input completeness**
CHECK 1 fires in Phase 7 and verifies that all required inputs were supplied and recorded in
INPUT INVENTORY. Missing input signals emit a named error token.

**C-16 — CHECK 2 inertia-advocate present**
CHECK 2 fires in Phase 7 and verifies that exactly one inertia-advocate role is present in
the written output. Zero or more than one emits a named error token.

**C-17 — CHECK 3A scope re-validation**
CHECK 3A fires in Phase 7 and re-validates that the written role set preserves the scope
gradient planned in the Phase 5 table. Any scope collapse emits `[SCOPE COLLAPSE — CHECK 3A
FAIL]`.

**C-18 — CHECK 3B vocab binding re-validation**
CHECK 3B fires in Phase 7 and re-validates that each role's planned vocab term is present
verbatim in the written file. Any mismatch triggers the ROLE-REPLACE sub-procedure (see
C-35).

**C-19 — CHECK 4A scope post-write**
CHECK 4A fires after all files are written and confirms the scope distribution in written
files matches the planning table. Fires independently of CHECK 3A.

**C-20 — CHECK 4B vocab binding post-write**
CHECK 4B fires after all files are written and re-validates verbatim vocab binding in written
files. Any mismatch triggers the ROLE-REPLACE sub-procedure (see C-35).

**C-21 — CHECK 5 frame-slot match**
CHECK 5 fires in Phase 7 and verifies that each field in the written role file matches the
corresponding FRAME FILL slot. Implemented as CHECK 5A + CHECK 5B (see C-34).

**C-22 — CHECK 6 output-path verification**
CHECK 6 fires in Phase 7 and verifies that each written file exists at the path recorded in
the planning table. File-not-found emits a named error token.

**C-23 — CHECK 7 file-count match**
CHECK 7 fires in Phase 7 and verifies that the count of written files equals the count of
roles in the planning table. Mismatch emits `[FILE COUNT MISMATCH — CHECK 7 FAIL]`.

**C-24 — Re-evaluation after role replacement**
Whenever a role is replaced (scope or vocab binding failure), the full audit table is
re-evaluated for the replacement role before Phase 6 continues. See C-35 for the structural
enforcement mechanism.

**C-25 — Source citation in FRAME FILL output**
Every FRAME FILL slot in the Phase 4 output includes an explicit source citation. Citations
must reference Phase 1 input rows, not derived artifacts. See C-34 for the verbatim-phrase
requirement.

**C-26 — FRAME FILL gate blocks Phase 6**
Phase 6 (file authoring) cannot open until the FRAME FILL gate emits PASS for all planned
roles. An incomplete or ungated FRAME FILL is a blocking error.

**C-27 — Forensic source-phrase tracing**
Each FRAME FILL slot includes a verbatim phrase extracted from the cited Phase 1 input row,
not a paraphrase. The phrase must be verifiable against the original input. See C-34 for
the per-slot structural requirement.

**C-28 — SCOPE AUDIT gate**
A named SCOPE AUDIT gate fires before Phase 6 opens, confirming that the planned role set
includes ≥ 2 distinct scope values. Advancing to Phase 6 without SCOPE AUDIT PASS is a
blocking error.

**C-29 — Gap-Addressed column in planning table**
The Phase 5 planning table includes a Gap-Addressed column mapping each planned role to the
domain gap it is designed to address. Roles without a mapped gap fail this criterion.

**C-30 — Inertia-first gate**
Phase 6 requires the inertia-advocate file to be written first, before any other role file.
A structural gate or named step enforces write order; authoring out of order is a blocking
error.

**C-31 — Vocab binding column**
The Phase 5 planning table includes a Planned-Vocab-Term column explicitly mapping each
planned role to the domain vocabulary term it must use verbatim. The column must be populated
before Phase 6 opens.

**C-32 — Inline LENS AUDIT**
A named LENS AUDIT block fires after each role is authored in Phase 6 (not deferred to
Phase 7). The inline audit checks verify[1]/[2] and simplify[1] for the just-written role
before authoring proceeds to the next role.

**C-33 — PERSPECTIVE AUDIT gate + CHECK 8 re-validation from written files**
C-08 (recommended) requires ≥ 3 distinct perspective values across written roles. The
sufficient structural condition is two-part: (1) a named PERSPECTIVE AUDIT gate fires before
Phase 6 opens, confirming that the planned role set includes ≥ 3 distinct perspective values;
(2) CHECK 8 in Phase 7 re-validates ≥ 3 distinct perspective values by reading the actual
written files, not the planning table. Advancing to Phase 6 without PERSPECTIVE AUDIT PASS
is a blocking error. C-08 requires correct output; C-33 requires the gate ran before
authoring and the check re-validated from written artifacts.

**C-34 — Per-slot Phase 1 source + CHECK 5A/5B split**
C-25 requires source citation in FRAME FILL output and C-27 requires forensic
source-phrase tracing. Citation to a derived artifact (e.g., CONVERGENCE SUMMARY) satisfies
neither. The sufficient structural condition is: each FRAME FILL slot includes a line in
the exact form `Phase 1 source: {row-id} = "{verbatim phrase}"`, where `{row-id}` identifies
a row in the Phase 1 INPUT INVENTORY and `{verbatim phrase}` is extractable from that row.
CHECK 5 splits into CHECK 5A (frame slot matches FRAME FILL output) and CHECK 5B (source
citation present, row ID exists in Phase 1, verbatim phrase verifiable). CHECK 5B must emit
`[{slot}: Phase 1 source missing or unverifiable — CITATION FAIL]` on any violation. C-25
requires source citation; C-27 requires forensic tracing; C-34 requires both are
structurally enforced per slot via CHECK 5B with exact notation.

**C-35 — ROLE-REPLACE sub-procedure (4 fields + CONFIRMED gate)**
C-24 requires full audit-table re-evaluation after any role is replaced. Ad hoc
re-evaluation satisfies C-24 only if it happens to be complete. The sufficient structural
condition is a named sub-procedure: ROLE-REPLACE fires at every CHECK 3B or CHECK 4B
mismatch (scope or vocab binding failure that triggers a role change), recording four
fields — `planned`, `written`, `resolution`, `re-evaluation` — and emitting
`ROLE-REPLACE CONFIRMED: YES` when all four fields are present and the re-evaluation row is
complete, or `ROLE-REPLACE CONFIRMED: NO` otherwise. CHECK 3B and CHECK 4B cannot reach
PASS status while any ROLE-REPLACE CONFIRMED is NO. C-24 requires re-evaluation after
replacement; C-35 requires the ROLE-REPLACE sub-procedure ran and emitted CONFIRMED for
every replacement event.

**C-36 — INERTIA BASELINE artifact + INERTIA ANCHOR CHECK**
C-10 (aspirational) requires domain-grounded inertia analysis. Asking "What is the status
quo?" inside CONVERGENCE SUMMARY satisfies C-10 only if the response happens to enumerate
both strengths and gaps — no structural mechanism separates them or ensures verbatim terms
survive to Phase 7 validation. The sufficient structural condition is a named artifact:
INERTIA BASELINE fires in Phase 2, recording (a) the named incumbent tool or practice
specific to the domain, (b) a "strengths it has" enumeration, and (c) a "gaps it does not
solve" enumeration. Advancing past Phase 2 without an INERTIA BASELINE artifact is a
blocking error. INERTIA ANCHOR CHECK then fires in Phase 7, verifying that at least one
verbatim strength term from INERTIA BASELINE appears in at least one written role's
lens.verify field. C-10 requires domain-grounded inertia analysis; C-36 requires the
INERTIA BASELINE artifact ran in Phase 2 and INERTIA ANCHOR CHECK confirmed verbatim
propagation in Phase 7.

---

## Scoring Formula

```
score = aspirational_pass / 28 * 10
```

Each full PASS = 0.357 pts. Essential and Recommended criteria are pass/fail gates; failure
on any Essential criterion scores 0 regardless of aspirational count.

| Aspirational PASS count | Score |
|-------------------------|-------|
| 28 | 10.00 |
| 27 | 9.64 |
| 26 | 9.29 |
| 25 | 8.93 |
| 24 | 8.57 |
| 23 | 8.21 |

PARTIAL on any criterion counts as 0.5 PASS for scoring purposes.

---

## Gap Closure Lineage

| Gap | Closed by | Enables |
|-----|-----------|---------|
| Gap-A: Perspective diversity not gated | C-33 (v10) | C-08 PARTIAL → PASS |
| Gap-B: Frame slot sources unverifiable | C-34 (v10) | C-25 + C-27 PARTIAL → PASS |
| Gap-C: Role replacement not sub-procedured | C-35 (v10) | C-24 PARTIAL → PASS |
| Gap-D: Inertia analysis not artifact-bound | C-36 (v11) | C-10 PARTIAL → PASS |
```
