Here are the **5 complete R6 variations** for `corps-build`.

---

## What changed from R5 → R6

R5 root cause was a rubric-mismatch: all five variations scored 83/125 because they implemented the NEW C-16/17/18 excellence patterns but missed the v3 structural requirements (C-11, C-13, C-14, C-15) already in the rubric, and had systematic PARTIALs on four basics.

Every R6 variation now carries all of the following:

| Fix | What it resolves |
|-----|-----------------|
| Exact field names: `title`, `role-type`, `area`, `lens`, `expertise` | C-05 PARTIAL → PASS |
| Explicit "validate path against org.yaml BEFORE writing" | C-04 PARTIAL → PASS |
| IA count column in headcount table (6-column format) | C-06 PARTIAL → PASS |
| `standard → specialized → IA` sequence + `role-type` in frontmatter | C-07 PARTIAL → PASS |
| INV-N block declared before steps with downstream references | C-11 FAIL → PASS |
| FM entries targeting C-09, C-10, C-11, C-12 by bracket ID | C-13 FAIL → PASS |
| Dedicated FAILURE MODES pre-step block | C-14 FAIL → PASS |
| Named CHECK-OUTPUT PROTOCOL section with enumerated rules | C-15 FAIL → PASS |
| Phase-exit guard tokens (PARSE-PASS, ROLES-COMPLETE, IA-PHASE-COMPLETE, BUILD-VERIFY-PASS/DRIFT) | C-16 carried forward |
| Per-artifact TRANSCRIPTION-RECEIPT synchronous with each write | C-17 carried forward |
| BUILD-VERIFY as single-purpose phase with content-type prohibition | C-18 carried forward |

## Variation axes

| # | Single/Combined | Axis | Core structural bet |
|---|-----------------|------|---------------------|
| **V-01** | Single | Role Sequence | Phase-exit guards bound to write-order phases; sequence compliance becomes auditable at each team boundary |
| **V-02** | Single | Output Format | All verification emits table rows; TABLE A/B/C architecture makes missing gates a missing row, not a missing sentence |
| **V-03** | Single | Phrasing Register | MUST/PROHIBITED/STOP imperative closes all interpretive latitude; PROHIBITED-N names each wrong pattern before any output |
| **V-04** | Combined | Inertia Framing + Lifecycle | Resistance-profile derivation (`defended-artifact + change-pressure → lens-phrase`) makes C-09 structural — generic IA is a derivation failure by INV-4 definition |
| **V-05** | Combined | Full synthesis | All elements simultaneously — INV-N block + FAILURE MODES + CHECK-OUTPUT PROTOCOL + TABLE A/B/C + phase gates + TRANSCRIPTION-RECEIPT + BUILD-VERIFY isolation + profile derivation + lens BUILD-VERIFY-LENS check |

**The new discriminator in R6**: FM-7 in V-05 (only variation to name BUILD-VERIFY phase contamination as an explicit failure mode) and the `BUILD-VERIFY-LENS` check (verifies IA lens matches the derived profile phrase, not just that a lens field exists).
  WRITE SEQUENCE: Within every team, write in this
       exact order: (a) standard roles, (b) specialized
       roles, (c) Inertia Advocate. Out-of-order writing
       is a hard stop.

INV-5  COUNT MATCH: Expected file count (Step 1) equals
       actual files written (Step 4). Discrepancy must be
       identified and corrected before completion.

---

FAILURE MODES
(Read all before producing any output. These are the
wrong-output patterns this prompt is designed to prevent.
Seeing them after writing is a failure — prevent them now.)

FM-1 [C-09] GENERIC IA: Inertia Advocate lens or expertise
     uses non-domain language: "resists change," "defends
     status quo," "prefers stability." Correct output names
     the specific inertia: which incumbents are defended,
     what this team's switching cost narrative is, what
     "we've always done it this way" means in this domain.

FM-2 [C-10] SILENT COUNT CHECK: Role-file count match is
     performed but no emitted check string appears. "All
     roles generated" appears in prose. Correct output
     includes the literal:
     "Table Total = [n], files written = [n] — [MATCH | MISMATCH]"

FM-3 [C-11] LATE INVARIANT: An invariant first appears
     inside a step body, not in the named INVARIANTS
     section above. Correct output: INV-1 through INV-5
     declared at entry point; referenced by name in steps.

FM-4 [C-12] ASSERTION SUBSTITUTION: Verification appears
     as prose ("all paths correct," "all fields present")
     rather than as an emitted machine-readable string.
     Correct output includes at least one literal
     PASS/FAIL or MATCH/MISMATCH string.

FM-5 [C-16] PHASE SKIP: A phase begins without the
     prior phase's exit gate being emitted. Correct
     output: PARSE-PASS precedes Step 2; STANDARD-PHASE-
     COMPLETE precedes specialized roles; SPECIALIZED-
     PHASE-COMPLETE precedes IA; IA-PHASE-COMPLETE
     precedes next team; ROLES-COMPLETE precedes BUILD-VERIFY.

FM-6 [C-17] RECEIPT OMISSION: A role file is written
     without an immediately following TRANSCRIPTION-RECEIPT.
     Correct output: every file write is followed
     immediately by the receipt string.

---

CHECK-OUTPUT PROTOCOL

All verification is a first-class output obligation.
No rule is optional. No rule is satisfied by prose.

Rule 1 — EMIT, DON'T ASSERT: Every check produces a
         literal emitted string. Prose compliance does
         not satisfy any check in this skill.

Rule 2 — PHASE EXIT GATES: Each major phase emits a
         named exit token before the next phase begins:
           PARSE-PASS | PARSE-FAIL
           STANDARD-PHASE-COMPLETE: {team-name} — [n] files
           SPECIALIZED-PHASE-COMPLETE: {team-name} — [n] files
           IA-PHASE-COMPLETE: {team-name} — {IA title}
           ROLES-COMPLETE — [n] total files
           BUILD-VERIFY-PASS | BUILD-VERIFY-DRIFT

Rule 3 — TRANSCRIPTION-RECEIPT: After writing each file,
         emit immediately:
           "RECEIPT: {path} — VERBATIM | REVISED"
         If REVISED: append "— reason: {reason}"

Rule 4 — COUNT GATE: After all files written, emit:
         "Table Total = [n], files written = [n] —
         [MATCH | MISMATCH]"
         MISMATCH requires correction before proceeding.

Rule 5 — FIELD GATE: Any file with empty or placeholder
         field content: emit
         "INV-2 FAIL: {field} empty — {path} — stopping"
         and stop. Correct before proceeding.

Rule 6 — PATH GATE: Any file with a path not derivable
         from org.yaml: emit
         "INV-1 FAIL: {path} not in org.yaml — stopping"
         and stop.

---

STEP 1 — PARSE AND PLAN

Parse org.yaml completely. Write no files in this step.

a. Map all Division > Team > Sub-group hierarchy.
   Record full structure in write order.

b. For each team, enumerate roles in mandatory sequence
   (INV-4): (i) standard roles, (ii) specialized roles,
   (iii) IA. Record per-team expected file counts.

c. Compute expected total file count (INV-5).

d. Extract all level vocabulary verbatim from org.yaml.
   These exact terms are used in role files and tables.

Emit: PARSE-PASS
(or PARSE-FAIL with specific issue if org.yaml is
incomplete or ambiguous — stop until resolved)

---

STEP 2 — WRITE ROLE FILES

Process teams in org.yaml order. Within each team,
execute three phases in mandatory sequence (INV-4):

--- STANDARD PHASE ---

For each standard role:
  1. Validate path against org.yaml before writing (INV-1).
     Emit INV-1 FAIL and stop on violation (Rule 6).
  2. Write file with all five fields (INV-2):
       title:     Full role title
       role-type: standard
       area:      Verbatim from org.yaml
       lens:      Domain-specific evaluation lens
       expertise: Specific domain knowledge required
     Emit INV-2 FAIL and stop on empty/placeholder (Rule 5).
  3. Emit RECEIPT immediately (Rule 3):
     "RECEIPT: {path} — VERBATIM | REVISED"

After all standard roles for team:
  Emit: STANDARD-PHASE-COMPLETE: {team-name} — [n] files

--- SPECIALIZED PHASE ---

For each specialized role:
  1. Validate path (INV-1).
  2. Write file with all five fields (INV-2):
       role-type: specialized
     Specialized roles must differ substantively from
     standard: different lens domain, different expertise
     scope. A cosmetic rename is a hard stop.
  3. Emit RECEIPT (Rule 3).

After all specialized roles for team:
  Emit: SPECIALIZED-PHASE-COMPLETE: {team-name} — [n] files

--- IA PHASE ---

Write exactly one Inertia Advocate file (INV-3):
  1. Validate path (INV-1).
  2. Write file with all five fields (INV-2):
       title:     "[Team Domain] Inertia Advocate" or
                  equivalent specific title
       role-type: inertia-advocate
       area:      Verbatim from org.yaml
       lens:      Names this team's specific inertia context —
                  NOT "resists change" or "defends status quo"
                  (FM-1). Name the incumbent vendors, processes,
                  or institutional memory that defines this
                  team's status quo threat.
       expertise: Names the specific incumbents, tools, or
                  legacy context this team's inertia is
                  attached to (FM-1).
  3. Emit RECEIPT (Rule 3).
  4. Emit: IA-PHASE-COMPLETE: {team-name} — {IA title}
     (INV-3, Rule 2)

Advance to next team only after IA-PHASE-COMPLETE.

After all teams complete:
  Emit: ROLES-COMPLETE — [n] total files written

---

STEP 3 — WRITE org-chart.md

Write file: org-chart.md
Emit RECEIPT after writing (Rule 3).

Section 1 — ASCII HIERARCHY
+-- and | notation only. Names verbatim from org.yaml.
Depth reflects Division > Team > Sub-group structure.

  +--[Division]
     +--[Team A]
     |  +--[Sub-group]
     +--[Team B]

Section 2 — HEADCOUNT TABLE (all six columns required)

| Group | Standard | Specialized | IA | Total | Levels |
|-------|----------|-------------|-----|-------|--------|
| ...   | ...      | ...         | ... | ...   | ...    |
| TOTAL | ...      | ...         | ... | [n]   | —      |

Levels column: all level terms from org.yaml for that group.
TOTAL row value = INV-5 expected count.

Section 3 — LEVEL DISTRIBUTION TABLE

| Level Term | Role File Count | Groups Using |
|------------|----------------|--------------|

Section 4 — CROSS-REFERENCE (Count Gate pre-print)

"Table Total = [n], files written = [n] — [MATCH | MISMATCH]"

---

STEP 4 — BUILD-VERIFY

THIS PHASE DOES EXACTLY ONE THING: verify.
No file writes. No new tables. No structural counts.
Content: per-artifact verdicts and the phase-exit token.
Adding any file write or structural count to this phase
is a build error.

For each artifact written in Steps 2–3, emit:
  "BUILD-VERIFY: {path} — VERBATIM | DRIFT"
  If DRIFT: emit "DRIFT DETAIL: {specific difference found}"

After all artifacts:

Count gate (Rule 4):
  "Table Total = [n], files written = [n] — [MATCH | MISMATCH]"
  MISMATCH: identify gap and correct before proceeding.

Field summary (Rule 5):
  "INV-2: All five fields present in all [n] files —
  [PASS | FAIL]"

Path summary (Rule 6):
  "INV-1: All [n] paths derive from org.yaml — [PASS | FAIL]"

Phase-exit token (Rule 2):
  BUILD-VERIFY-PASS  (all VERBATIM, all gates PASS/MATCH)
  BUILD-VERIFY-DRIFT (any DRIFT — list artifact paths)

Skill is complete only when BUILD-VERIFY-PASS is emitted.
Any unresolved DRIFT, MISMATCH, or FAIL suspends completion.

---

AMEND

AMEND-A  AREA REGENERATION: Regenerate a specific area.
         Re-validate INV-1 paths for the area before writing.
         Re-run Steps 2–4 for the named area only.
         Re-emit all per-team phase gates and TRANSCRIPTION
         RECEIPTs for the regenerated area.
         Re-emit BUILD-VERIFY phase for regenerated artifacts.
         Re-emit count gate with corrected totals.

AMEND-B  LEVEL VOCABULARY UPDATE: Replace a level term
         across all files in the affected groups. Update
         LEVEL DISTRIBUTION TABLE. Emit "[n] files updated
         — PASS" after completion.

AMEND-C  GROUP NODE ADDITION: Add a new group node to
         the hierarchy. Validate all new paths against INV-1
         before writing. Run all three sequence phases
         (standard → specialized → IA) for each new team.
         Emit all phase gates and RECEIPTs for new teams.
         Re-emit HEADCOUNT TABLE and count gate.
```

---

## V-02 — Axis: Output Format (Table-Row Audit Architecture)

**Hypothesis**: When every verification gate emits a table row rather than an inline string, the model's audit trail becomes structurally independent of prose output — a missing gate is a missing table row, not a missing sentence. TRANSCRIPTION-RECEIPT implemented as a table column makes omissions immediately visible.

---

```
/corps-build

Read a confirmed org.yaml and generate the complete org.
Two outputs:
  OUTPUT-1: org-chart.md — ASCII hierarchy + headcount table
            + level distribution + cross-reference audit
  OUTPUT-2: Typed role files at .craft/roles/{area}/{role}.md,
            one per role across all teams

Supports arbitrary nesting: Division > Team > Sub-group.
Every team must include exactly one Inertia Advocate.

---

INVARIANTS
(Named block at entry point. All five declared here.
Referenced by name in steps. Never defined inside a step.)

INV-A  PATH DERIVATION: All role files written to paths
       derived from org.yaml. Pattern:
       .craft/roles/{area-slug}/{role-slug}.md.
       Validate path against org.yaml BEFORE writing.
       Non-derivable path is a hard stop.

INV-B  FIVE TYPED FIELDS: Every role file contains all
       five fields with substantive content:
         title:     Full role title
         role-type: standard | specialized | inertia-advocate
         area:      Verbatim name from org.yaml
         lens:      Primary evaluation lens (domain-specific)
         expertise: Specific domain knowledge required
       Empty or placeholder content is a hard stop.

INV-C  IA MANDATORY: One Inertia Advocate per team.
       No team closes until IA is written and the
       per-team IA row appears in the RECEIPT TABLE.

INV-D  WRITE ORDER: Per team: standard roles, then
       specialized roles, then Inertia Advocate.
       The SEQUENCE AUDIT TABLE records sequence compliance.

INV-E  COUNT INTEGRITY: PLAN TABLE total (Step 1) matches
       RECEIPT TABLE total (Step 3). Verified and emitted
       in the FINAL AUDIT TABLE before completion.

---

FAILURE MODES
(All must be read before producing any output. These are
wrong-output patterns this prompt blocks by design.)

FM-A [C-09] GENERIC INERTIA ADVOCATE: IA lens or
     expertise uses non-specific language: "represents
     cautious perspective," "resists new approaches,"
     "defends existing processes." Correct: lens names
     this team's domain context; expertise names the
     specific incumbents, tools, or institutional memory
     that define this team's actual status quo.

FM-B [C-10] PROSE COUNT ASSERTION: Role count match
     confirmed in text ("all roles were generated") rather
     than as a row in the FINAL AUDIT TABLE. Correct:
     count check appears as a table row with Expected,
     Actual, and MATCH/MISMATCH result literal.

FM-C [C-11] INLINE-ONLY INVARIANT: INV-A through INV-E
     are mentioned inside steps but not declared as a
     named group before Step 1. Correct: all invariants
     in this named section, referenced by ID in steps.

FM-D [C-12] SILENT COMPLIANCE: All checks performed but
     no machine-readable status emitted anywhere in the
     output. Correct: every check produces a table row
     with a PASS/FAIL or MATCH/MISMATCH literal in the
     Result column.

FM-E [C-16] UNGATED PHASE TRANSITION: A phase begins
     without a prior phase-exit token in the output.
     Correct: PARSE-PASS in output before Step 2 starts;
     ROLES-COMPLETE in output before BUILD-VERIFY starts.

FM-F [C-17] BATCH-ONLY RECEIPT: All receipts appear in
     a post-hoc summary block rather than synchronously
     with each file write. Correct: the RECEIPT TABLE
     row for each file is emitted immediately after
     writing that file.

---

CHECK-OUTPUT PROTOCOL

Verification in this skill is a table-row obligation.
Every check emits a structured row. No prose assertions.

TABLE FORMAT — used for all checks:

  | Check | Expected | Actual | Result |
  |-------|----------|--------|--------|

Rule 1 — TABLE ROW: Every gate emits a table row in
         the format above. Prose assertions do not satisfy
         any gate in this skill.

Rule 2 — PHASE EXIT: Each major phase emits an exit token
         before the next phase begins:
           PARSE-PASS | PARSE-FAIL
           ROLES-COMPLETE
           BUILD-VERIFY-PASS | BUILD-VERIFY-DRIFT

Rule 3 — RECEIPT ROW: After writing each role file,
         emit a row in the RECEIPT TABLE:
           | {path} | written | verified | VERBATIM | REVISED |

Rule 4 — PER-TEAM IA ROW: After writing each team's IA,
         emit a row in the IA CLOSURE TABLE:
           | {team} | 1 | 1 | MATCH |

Rule 5 — FINAL AUDIT TABLE: Emitted in BUILD-VERIFY,
         consolidates all checks into one table.

---

STEP 1 — PARSE AND BUILD PLAN TABLE

Read org.yaml completely. Build tables before writing files.

PLAN TABLE (drives Steps 2 and 3)

| Team | Standard | Specialized | IA | Total | Path Prefix |
|------|----------|-------------|-----|-------|-------------|
| ...  | ...      | ...         | 1   | ...   | .craft/roles/{area-slug}/ |
| TOTAL | ...     | ...         | ... | [n]   | — |

Path Prefix column: derived from org.yaml area names (INV-A).
Total row value = INV-E expected count.

LEVEL TERMS TABLE

| Group | Level Terms Used |
|-------|-----------------|

Record all level vocabulary from org.yaml. Use verbatim.

SEQUENCE AUDIT TABLE (to be filled during Step 2)

| Team | Standard Done | Specialized Done | IA Done | Order |
|------|---------------|-----------------|---------|-------|

Emit: PARSE-PASS

---

STEP 2 — WRITE ROLE FILES

Process teams in PLAN TABLE order. Per team, enforce
INV-D sequence: standard → specialized → IA.

RECEIPT TABLE (fill synchronously — one row per file written)

| Path | Status | VERBATIM / REVISED | Notes |
|------|--------|--------------------|-------|

STANDARD ROLES (INV-D phase a):
  Write one file per standard role.
  Validate path against PLAN TABLE Path Prefix (INV-A).
  Write all five fields with substantive content (INV-B):
    title, role-type: standard, area, lens, expertise
  After each file: add row to RECEIPT TABLE immediately.

SPECIALIZED ROLES (INV-D phase b):
  Write one file per specialized role.
  Specialized roles must be substantively distinct:
  different lens domain, different expertise scope.
  role-type: specialized
  After each file: add row to RECEIPT TABLE immediately.

INERTIA ADVOCATE (INV-D phase c — INV-C):
  Write one file. role-type: inertia-advocate
  Lens: must name this team's domain context, not generic
  resistance language (FM-A).
  Expertise: must name specific incumbents or legacy context
  this team's inertia is anchored to (FM-A).
  After writing: add row to RECEIPT TABLE.
  Update SEQUENCE AUDIT TABLE row for this team.
  Add row to IA CLOSURE TABLE:
    | {team-name} | Expected: 1 | Actual: 1 | MATCH |

After all teams:
  Emit: ROLES-COMPLETE — [n] files written
  (All RECEIPT TABLE rows must be filled before this emit.)

---

STEP 3 — WRITE org-chart.md

Write file: org-chart.md
Add row to RECEIPT TABLE after writing.

Section 1 — ASCII HIERARCHY
+-- and | notation. Verbatim names from org.yaml.
Nesting matches org.yaml structure depth.

Section 2 — HEADCOUNT TABLE (all six columns required)

| Group | Standard | Specialized | IA | Total | Levels |
|-------|----------|-------------|-----|-------|--------|
| ...   | ...      | ...         | ... | ...   | ...    |
| TOTAL | ...      | ...         | ... | [n]   | — |

IA column required. Total row = INV-E expected count.
Levels: use LEVEL TERMS TABLE values.

Section 3 — LEVEL DISTRIBUTION TABLE

| Level Term | File Count | Groups |
|------------|-----------|--------|

Section 4 — IA CLOSURE TABLE (from Step 2)

| Team | Expected IA | Actual IA | Result |
|------|-------------|-----------|--------|
(All rows from Step 2 IA phase.)

---

STEP 4 — BUILD-VERIFY

THIS PHASE IS VERIFICATION ONLY.
No file writes permitted in this phase.
Any file write in this phase is a build error.

Emit FINAL AUDIT TABLE:

| Check | Expected | Actual | Result |
|-------|----------|--------|--------|
| IA per team (each row) | 1 | [n] | MATCH/MISMATCH |
| Total role files | [n] | [n] | MATCH/MISMATCH |
| Chart S-2 total | [n] | [n] | MATCH/MISMATCH |
| Five fields — all files | all | all | PASS/FAIL |
| All paths from org.yaml | all | all | PASS/FAIL |

RECEIPT TABLE summary row:
  | All artifacts | [n] expected | [n] receipted | MATCH/MISMATCH |

Any MISMATCH or FAIL row: identify the specific team or
file and correct before emitting the phase-exit token.

Emit:
  BUILD-VERIFY-PASS  (all rows MATCH or PASS)
  BUILD-VERIFY-DRIFT (any row MISMATCH or FAIL — list each)

Skill complete only when BUILD-VERIFY-PASS emitted and
all FINAL AUDIT TABLE rows show MATCH or PASS.

---

AMEND

AMEND-A  AREA REGENERATION: Regenerate one area.
         Rebuild PLAN TABLE rows for that area.
         Re-run Steps 2–4 for the named area.
         Emit fresh RECEIPT TABLE rows for all regenerated
         files. Re-emit IA CLOSURE TABLE rows for affected
         teams. Re-emit FINAL AUDIT TABLE.

AMEND-B  LEVEL VOCABULARY: Replace one level term.
         Update LEVEL TERMS TABLE and LEVEL DISTRIBUTION
         TABLE. Emit "[n] files updated — PASS".

AMEND-C  GROUP NODE ADDITION: Add new group node.
         Add rows to PLAN TABLE. Validate new path prefixes
         against INV-A. Run standard → specialized → IA for
         new teams. Emit RECEIPT TABLE and IA CLOSURE TABLE
         rows. Re-emit HEADCOUNT TABLE. Re-emit FINAL AUDIT
         TABLE count rows with updated totals.
```

---

## V-03 — Axis: Phrasing Register (Full Imperative)

**Hypothesis**: Replacing descriptive and conditional language with strict MUST/PROHIBITED/STOP imperatives eliminates interpretive latitude — every rule reads as a hard constraint with no paraphrase-compliant surface. PROHIBITED patterns are named in the FAILURE MODES block before any output is produced.

---

```
/corps-build

COMMAND: Read the confirmed org.yaml and generate the
complete org. Produce exactly two outputs: (1) org-chart.md;
(2) one typed role file per role at .craft/roles/{area}/{role}.md.

YOU MUST read every invariant, failure mode, and protocol
rule before producing any output. Produce no output before
completing this read.

---

INVARIANTS

You MUST declare all invariants before Step 1. You MUST
reference each by name in the step where it is enforced.
Restating an invariant for the first time inside a step
body is PROHIBITED (see FM-3).

INV-1  PATH PROHIBITION: NEVER write a file to any path
       not derivable from org.yaml. Pattern MUST be:
       .craft/roles/{area-slug}/{role-slug}.md. You MUST
       validate the path against org.yaml BEFORE writing.
       STOP on first violation — do not continue writing.

INV-2  FIELD MANDATE: EVERY role file MUST contain all
       five fields with substantive bodies:
         title:     Full role title
         role-type: standard | specialized | inertia-advocate
         area:      Verbatim name from org.yaml
         lens:      Domain-specific evaluation lens
         expertise: Specific domain knowledge required
       YOU MUST NOT write a file with empty or placeholder
       content. STOP on first violation.

INV-3  IA MANDATE: DO NOT close any team without writing
       exactly one Inertia Advocate file. NEVER advance to
       the next team before IA-PHASE-COMPLETE is emitted.
       There are NO exceptions to this rule.

INV-4  SEQUENCE MANDATE: WITHIN every team, write in this
       EXACT order: (a) standard roles, (b) specialized
       roles, (c) Inertia Advocate. You MUST NOT write
       specialized before standard, or IA before all
       standard and specialized are complete for that team.

INV-5  COUNT MANDATE: DO NOT declare the skill complete
       unless the expected file count (Step 1) EXACTLY
       matches the written file count (Step 4). STOP and
       correct any discrepancy before proceeding.

---

FAILURE MODES

YOU MUST read all before writing any output.
These patterns are PROHIBITED. Encountering them after
writing is a failure — prevent them now.

PROHIBITED-1 [C-09] GENERIC IA LANGUAGE: Writing an
  Inertia Advocate file whose lens or expertise uses
  any of the following: "resists change," "defends the
  status quo," "prefers stability," "cautious perspective,"
  "resistant to new approaches." This is a HARD FAILURE.
  IA lens MUST name this team's specific domain inertia.
  IA expertise MUST name the specific incumbent tools,
  vendors, or processes this team's status quo defends.
  You MUST NOT produce a PROHIBITED-1 output.

PROHIBITED-2 [C-10] INVISIBLE COUNT CHECK: Completing
  the skill without emitting a literal count-check string.
  DO NOT use prose assertion ("all roles generated").
  You MUST emit exactly:
  "Table Total = [n], files written = [n] —
  [MATCH | MISMATCH]"

PROHIBITED-3 [C-11] LATE INVARIANT: Mentioning any
  invariant for the first time inside a step body.
  You MUST declare INV-1 through INV-5 in the INVARIANTS
  section above. You MUST NOT define them in steps.
  Reference only. First-time definition in a step body
  is PROHIBITED.

PROHIBITED-4 [C-12] SILENT COMPLIANCE: Performing any
  check without emitting a machine-readable result. Every
  check MUST produce an emitted string with PASS/FAIL
  or MATCH/MISMATCH. Prose descriptions of checks
  DO NOT satisfy this requirement.

PROHIBITED-5 [C-16] UNGATED PHASE TRANSITION: Beginning
  a phase without the prior phase's exit gate in output.
  You MUST emit PARSE-PASS before Step 2 starts.
  You MUST emit ROLES-COMPLETE before BUILD-VERIFY starts.
  You MUST emit IA-PHASE-COMPLETE before advancing to
  next team. Skipping a gate is PROHIBITED.

PROHIBITED-6 [C-17] DEFERRED RECEIPT: Writing a role
  file and emitting its TRANSCRIPTION-RECEIPT anywhere
  except immediately after that specific write.
  Batch receipts are PROHIBITED. Each receipt MUST be
  emitted immediately after its file is written.

---

CHECK-OUTPUT PROTOCOL

This section is mandatory. All six rules MUST be followed.
No rule is optional. No rule may be satisfied by prose.

RULE 1 — EMIT LITERALS ONLY: Every verification result
  MUST be a literal string. You MUST NOT write "the
  counts match" or "all fields are present." You MUST
  write the exact string specified.

RULE 2 — PHASE EXIT GATES: You MUST emit named exit
  tokens at each phase boundary:
    PARSE-PASS | PARSE-FAIL (before Step 2)
    ROLES-COMPLETE (before BUILD-VERIFY)
    BUILD-VERIFY-PASS | BUILD-VERIFY-DRIFT (skill complete)
  OMITTING any gate is PROHIBITED.

RULE 3 — IA GATE: After writing each team's IA file,
  you MUST emit:
    "IA-PHASE-COMPLETE: {team-name} — {IA title}"
  If IA is absent, you MUST emit:
    "IA-PHASE-FAIL: {team-name} — STOPPING"
  and STOP. DO NOT advance to next team without this gate.

RULE 4 — TRANSCRIPTION-RECEIPT: After writing each file,
  you MUST immediately emit:
    "RECEIPT: {path} — VERBATIM | REVISED"
  REVISED MUST be followed by "— reason: {reason}".
  You MUST NOT batch receipts or defer them.

RULE 5 — COUNT GATE: After all files written, you MUST
  emit:
    "Table Total = [n], files written = [n] —
    [MATCH | MISMATCH]"
  MISMATCH requires immediate correction.

RULE 6 — SKILL COMPLETION GATE: You MUST NOT declare
  the skill complete unless BUILD-VERIFY-PASS has been
  emitted and all gates above show PASS or MATCH. Any
  unresolved FAIL, MISMATCH, or DRIFT PROHIBITS completion.

---

STEP 1 — READ AND PLAN (YOU MUST NOT WRITE ANY FILES)

You MUST complete this step in full before writing.

a. Parse the entire org.yaml. Map every Division, Team,
   and Sub-group node. Record the full hierarchy.

b. For every team, enumerate roles in mandatory sequence
   (INV-4): (i) standard, (ii) specialized, (iii) IA.
   NEVER write this list out of sequence.

c. Count total expected files across all teams.
   Record as INV-5 expected count.

d. Identify all level terms in org.yaml.
   You MUST use these exact terms in role files and tables.
   NEVER substitute your own level vocabulary.

Emit: PARSE-PASS
(PARSE-FAIL if org.yaml is ambiguous — STOP until resolved)

---

STEP 2 — WRITE ROLE FILES

For each team in org.yaml order, write in INV-4 mandatory
sequence: standard → specialized → IA.

STANDARD ROLES:
  - Validate path against INV-1 BEFORE writing.
    PROHIBITED if path not in org.yaml (emit INV-1 FAIL, STOP).
  - Write all five fields per INV-2.
    PROHIBITED to leave any field empty or placeholder.
  - role-type: standard (MUST appear in frontmatter)
  - Emit RECEIPT immediately (RULE 4).

SPECIALIZED ROLES:
  - MUST be substantively distinct from standard roles.
  - PROHIBITED: copying a standard role with only name change.
    Lens and expertise MUST differ from any standard role.
  - role-type: specialized (MUST appear in frontmatter)
  - Validate path (INV-1). Emit RECEIPT (RULE 4).

INERTIA ADVOCATE (INV-3 — MANDATORY):
  - One per team. No exceptions. No skipping. No deferral.
  - lens: MUST name this team's domain inertia context.
    PROHIBITED-1 language is not permitted here.
  - expertise: MUST name specific incumbents, tools, or
    processes representing this team's status quo.
    PROHIBITED-1 language is not permitted here.
  - role-type: inertia-advocate (MUST appear in frontmatter)
  - Emit RECEIPT (RULE 4).
  - Emit: "IA-PHASE-COMPLETE: {team-name} — {IA title}"
    (RULE 3 — MUST emit before advancing)

After all teams complete:
  Emit: ROLES-COMPLETE — [n] total files written
  (YOU MUST emit this before BUILD-VERIFY begins)

---

STEP 3 — WRITE org-chart.md

YOU MUST produce all four sections. NONE may be omitted.
Emit RECEIPT after writing (RULE 4).

SECTION 1 — ASCII HIERARCHY
  Use ONLY +-- and | notation.
  Names MUST be verbatim from org.yaml.
  DO NOT abbreviate, reorder, or paraphrase any name.
  Nesting MUST reflect org.yaml depth.

SECTION 2 — HEADCOUNT TABLE
  Required columns — you MUST NOT omit any:
  | Group | Standard | Specialized | IA | Total | Levels |
  |-------|----------|-------------|-----|-------|--------|
  IA column: count of IA files for each group.
  Levels column: list all level terms for that group.
  Total row at bottom = INV-5 expected count.

SECTION 3 — LEVEL DISTRIBUTION TABLE
  | Level Term | File Count | Groups Using |
  |------------|-----------|--------------|

SECTION 4 — CROSS-REFERENCE (RULE 5 pre-print)
  "Table Total = [n], files written = [n] —
  [MATCH | MISMATCH]"

---

STEP 4 — BUILD-VERIFY

THIS PHASE IS VERIFICATION ONLY.
YOU MUST NOT write any files in this phase.
YOU MUST NOT add any structural counts in this phase.
Any file write in this phase is a PROHIBITED action.
Content: per-artifact verdicts and the phase-exit token.

For each artifact from Steps 2–3:
  Emit: "BUILD-VERIFY: {path} — VERBATIM | DRIFT"
  If DRIFT: emit "DRIFT DETAIL: {specific difference}"

After all artifacts:

You MUST emit:
  "Table Total = [n], files written = [n] — [MATCH | MISMATCH]"
  MISMATCH: STOP, correct, re-emit.

You MUST emit:
  "INV-2: All five fields in all [n] files — [PASS | FAIL]"

You MUST emit:
  "INV-1: All [n] paths from org.yaml — [PASS | FAIL]"

Phase-exit token (RULE 2 — YOU MUST emit one):
  BUILD-VERIFY-PASS  (all VERBATIM, all gates PASS/MATCH)
  BUILD-VERIFY-DRIFT (any DRIFT — list affected paths)

YOU MUST NOT declare skill complete without BUILD-VERIFY-PASS.

---

AMEND

AMEND-A  AREA REGENERATION: Regenerate a specific area.
  You MUST re-validate INV-1 and INV-2 for regenerated files.
  You MUST re-emit all per-team IA gates (RULE 3) and
  RECEIPTS (RULE 4) for the regenerated area.
  You MUST re-emit BUILD-VERIFY for regenerated artifacts.
  You MUST re-emit count gate with updated totals.

AMEND-B  LEVEL VOCABULARY UPDATE: Replace a level term.
  Update affected files. You MUST emit "[n] files updated
  — PASS" after completion. NEVER omit this confirmation.

AMEND-C  GROUP NODE ADDITION: Add a new group node.
  You MUST validate all new paths against INV-1 before
  writing any files. You MUST run all three phases
  (standard → specialized → IA) for each new team.
  You MUST emit all gates and RECEIPTS for new teams.
  You MUST re-emit HEADCOUNT TABLE and count gate.
```

---

## V-04 — Combined: Inertia Framing + Lifecycle Emphasis

**Hypothesis**: Elevating the Inertia Advocate from a required role to a required **derivation phase** — where a resistance-profile computation (defended-artifact + change-pressure → lens-phrase) is completed before writing any IA file — structurally prevents FM-1 generic IA. The derived lens-phrase becomes the IA file's opening text AND the BUILD-VERIFY comparison anchor, creating a closed derivation loop: profile → write → receipt → BUILD-VERIFY-VERBATIM.

---

```
/corps-build

Read a confirmed org.yaml and generate the complete org.
Two outputs:
  OUTPUT-1: org-chart.md — ASCII hierarchy, headcount table,
            level distribution, cross-reference audit
  OUTPUT-2: One typed role file per role at
            .craft/roles/{area-slug}/{role-slug}.md

Supports arbitrary nesting: Division > Team > Sub-group.
The Inertia Advocate is not merely a required role — it is
a required derivation phase for every team in the org.

---

INVARIANTS
(Named block before any steps. All referenced by ID in steps.
Never first-defined inside a step body.)

INV-1  PATH FIDELITY: Role files written only to
       .craft/roles/{area-slug}/{role-slug}.md. Slugs
       derived directly from org.yaml names. Path validated
       against org.yaml BEFORE each write.

INV-2  FIVE FIELDS: Every role file contains these five
       fields with substantive bodies:
         title:     Full role title
         role-type: standard | specialized | inertia-advocate
         area:      Verbatim name from org.yaml
         lens:      Primary evaluation lens (domain-specific)
         expertise: Specific domain knowledge required
       Empty or placeholder content is a hard stop.

INV-3  PROFILE MANDATE: Before writing any IA file for a
       team, complete the RESISTANCE PROFILE PHASE for that
       team. The profile must produce a lens-phrase that
       cannot be written without knowing both:
         defended-artifact: what this team's current process
                            or toolchain is
         change-pressure:   what external or internal pressure
                            is challenging it
       The lens-phrase derived from these two fields becomes
       the IA file's lens value verbatim.

INV-4  IA LIFECYCLE GATE: Every team runs exactly three
       lifecycle phases: STANDARD-PHASE → SPECIALIZED-PHASE
       → IA-PHASE. IA-PHASE entry requires INV-3 profile
       complete. IA-PHASE exit requires IA-PHASE-COMPLETE
       emitted with the IA title and derived lens-phrase.

INV-5  COUNT MATCH: Expected file count (Step 1) equals
       actual files written (Step 4). Verified and emitted
       in BUILD-VERIFY.

---

FAILURE MODES
(Pre-step. All must be read before any output is produced.)

FM-1 [C-09] INERTIA WITHOUT FACE: The IA file is written
     but the inertia has no face. Lens: "represents the
     cautious perspective." Expertise: "experience with
     legacy systems." This is the most common IA failure
     — it looks correct from outside but teaches nothing
     about the actual competitive threat.
     Correct IA comes from INV-3 derivation:
       defended-artifact answers: what specifically does
         this team depend on today?
       change-pressure answers: what is being asked of them
         that threatens this dependency?
       lens-phrase answers: what is the IA's specific lens
         given BOTH of the above?
     Generic resistance language fails INV-3 by definition.

FM-2 [C-10] INVISIBLE AUDIT: Step 4 runs, files are
     written, no literal count-check string appears.
     "All roles generated" appears in the response.
     Correct output emits:
     "Table Total = [n], files written = [n] —
     [MATCH | MISMATCH]"

FM-3 [C-11] ORPHANED INVARIANTS: INV-1 through INV-5
     appear only inside step bodies, not in a named
     INVARIANTS section before Step 1. Without entry-point
     declaration, invariants cannot be cross-referenced
     and become indistinguishable from inline instructions.

FM-4 [C-12] ASSERTION VERIFICATION: Verification phrases
     appear as prose: "The headcount table matches the
     role files." Correct output includes at least one
     literal emitted check string with PASS/FAIL or
     MATCH/MISMATCH per the CHECK-OUTPUT PROTOCOL.

FM-5 [C-16] UNGUARDED TRANSITION: IA-PHASE begins
     without RESISTANCE PROFILE PHASE being recorded.
     BUILD-VERIFY begins without ROLES-COMPLETE emitted.
     Correct: each phase enters only after prior phase's
     exit gate is in the output.

FM-6 [C-17] LATE RECEIPT: Role file written; receipt
     emitted in a summary block or after other files.
     Correct: TRANSCRIPTION-RECEIPT emitted immediately
     after writing each individual file.

---

CHECK-OUTPUT PROTOCOL

Named obligations. Every obligation emits a literal string.
No obligation is satisfied by prose description.

OBL-1  RESISTANCE PROFILE RECORD: Before IA-PHASE for
       each team, emit:
       "PROFILE: {team-name} | defended-artifact: {X} |
       change-pressure: {Y} | lens-phrase: {Z}"
       The lens-phrase becomes the IA file's lens field
       verbatim (INV-3).

OBL-2  PHASE EXIT GATES: Named exit tokens per phase:
         PARSE-PASS | PARSE-FAIL
         STANDARD-PHASE-COMPLETE: {team-name} — [n] files
         SPECIALIZED-PHASE-COMPLETE: {team-name} — [n] files
         IA-PHASE-COMPLETE: {team-name} — {IA title} —
                            lens: {lens-phrase}
         ROLES-COMPLETE — [n] total files
         BUILD-VERIFY-PASS | BUILD-VERIFY-DRIFT

OBL-3  TRANSCRIPTION-RECEIPT: After writing each file,
       emit immediately:
       "RECEIPT: {path} — VERBATIM | REVISED"
       REVISED: append "— reason: {reason}"

OBL-4  COUNT GATE: After all files written, emit:
       "Table Total = [n], files written = [n] —
       [MATCH | MISMATCH]"

OBL-5  SKILL COMPLETE GATE: Skill complete only when
       BUILD-VERIFY-PASS emitted and all OBL gates show
       PASS or MATCH. Any unresolved failure suspends
       completion.

---

STEP 1 — PARSE AND SCHEDULE TEAM LIFECYCLES

Read org.yaml. Build lifecycle schedule before writing.

TEAM LIFECYCLE TABLE

| Team | Standard Count | Specialized Count | IA | Total |
|------|---------------|-------------------|----|-------|
| ...  | ...           | ...               | 1  | ...   |
| TOTAL | ...          | ...               | [n] | [n] |

LEVEL TERMS TABLE

| Group | Level Terms |
|-------|-------------|

Record all level vocabulary. Use verbatim in all outputs.

Expected file count = TOTAL row. Record for INV-5.

Emit: PARSE-PASS

---

STEP 2 — EXECUTE TEAM LIFECYCLES

For each team in org.yaml order, run three phases:

--- STANDARD-PHASE ---
Write one file per standard role.
Path validation (INV-1): validate against org.yaml before write.
Five fields required (INV-2): title, role-type: standard,
area, lens, expertise.
Emit RECEIPT after each file (OBL-3).
Emit: STANDARD-PHASE-COMPLETE: {team-name} — [n] files

--- SPECIALIZED-PHASE ---
Write one file per specialized role.
Substantively distinct from standard: different lens domain,
different expertise scope. Not cosmetic renames.
role-type: specialized
Emit RECEIPT after each file (OBL-3).
Emit: SPECIALIZED-PHASE-COMPLETE: {team-name} — [n] files

--- RESISTANCE PROFILE PHASE (INV-3) ---
Before writing the IA file, derive the resistance profile:
  defended-artifact: What does this team depend on today?
                     (name the specific tool, process, or
                     workflow they are being asked to change)
  change-pressure:   What is being asked of them?
                     (name the specific initiative or new
                     requirement creating the change pressure)
  lens-phrase:       Derived from both above. The lens this
                     person brings to every decision because
                     of what they are defending and why.
                     This phrase cannot be "cautious" or
                     "resistant" — it must name the specific
                     inertia context (INV-3, FM-1).
Emit OBL-1: "PROFILE: {team-name} | defended-artifact: {X}
             | change-pressure: {Y} | lens-phrase: {Z}"

--- IA PHASE (INV-4) ---
Write the Inertia Advocate file.
Path validation (INV-1).
Five fields (INV-2):
  title:     Specific IA title reflecting team domain
  role-type: inertia-advocate
  area:      Verbatim from org.yaml
  lens:      Use the derived lens-phrase verbatim (INV-3)
  expertise: Name the specific incumbents, tools, or
             institutional context this IA represents
Emit RECEIPT (OBL-3).
Emit OBL-2: IA-PHASE-COMPLETE: {team-name} — {IA title}
            — lens: {lens-phrase}

Advance to next team.

After all teams:
  Emit: ROLES-COMPLETE — [n] total files written

---

STEP 3 — WRITE org-chart.md

Write file: org-chart.md. Emit RECEIPT (OBL-3).

ASCII HIERARCHY
+-- and | notation. Verbatim org.yaml names.
Depth matches org.yaml nesting.

HEADCOUNT TABLE (all six columns required)

| Group | Standard | Specialized | IA | Total | Levels |
|-------|----------|-------------|-----|-------|--------|
| ...   | ...      | ...         | ... | ...   | ...    |
| TOTAL | ...      | ...         | ... | [n]   | — |

IA column: IA file count per group.
Levels: use LEVEL TERMS TABLE values.

LEVEL DISTRIBUTION TABLE

| Level Term | Count | Groups |
|------------|-------|--------|

CROSS-REFERENCE (OBL-4 pre-print):
"Table Total = [n], files written = [n] — [MATCH | MISMATCH]"

---

STEP 4 — BUILD-VERIFY

SINGLE-PURPOSE PHASE: verification only.
No file writes in this phase.
Content: per-artifact BUILD-VERIFY verdicts and phase-exit.

For each artifact from Steps 2–3:
  "BUILD-VERIFY: {path} — VERBATIM | DRIFT"
  For IA files: also verify "lens matches PROFILE lens-phrase"
    "BUILD-VERIFY-LENS: {team-name} — MATCH | MISMATCH"
  DRIFT: emit "DRIFT DETAIL: {difference found}"

Count gate (OBL-4):
  "Table Total = [n], files written = [n] — [MATCH | MISMATCH]"

Summary gates:
  "INV-2: All five fields in all [n] files — [PASS | FAIL]"
  "INV-1: All paths from org.yaml — [PASS | FAIL]"
  "INV-3: All IA lenses from PROFILE derivation — [PASS | FAIL]"

Phase-exit (OBL-2):
  BUILD-VERIFY-PASS  (all VERBATIM, all gates PASS/MATCH)
  BUILD-VERIFY-DRIFT (any DRIFT or FAIL — list artifacts)

Skill complete only when BUILD-VERIFY-PASS emitted.

---

AMEND

AMEND-A  AREA REGENERATION: Regenerate a specific area.
         Re-run RESISTANCE PROFILE PHASE for each team
         in the area before writing IA files.
         Re-run STANDARD-PHASE, SPECIALIZED-PHASE, IA-PHASE
         for each team. Re-emit all OBL gates and RECEIPTs.
         Re-emit BUILD-VERIFY for regenerated artifacts.

AMEND-B  LEVEL VOCABULARY: Replace a level term.
         Update LEVEL TERMS TABLE. Emit "[n] files updated
         — PASS".

AMEND-C  GROUP NODE ADDITION: Add group node.
         Add rows to TEAM LIFECYCLE TABLE. Run all three
         lifecycle phases plus RESISTANCE PROFILE PHASE
         for each new team. Emit all OBL gates and RECEIPTs.
         Re-emit HEADCOUNT TABLE and count gate.
```

---

## V-05 — Combined: Full Architecture Synthesis

**Hypothesis**: The highest rubric coverage requires all structural elements simultaneously — pre-declared INV-N block with downstream references, FAILURE MODES pre-step targeting all four aspirational criteria, named CHECK-OUTPUT PROTOCOL with table-row verification, phase-exit guards on every phase boundary, synchronous TRANSCRIPTION-RECEIPT per file, BUILD-VERIFY as a single-purpose phase with content-type prohibition, standard → specialized → IA write sequence, and resistance-profile derivation before every IA phase. These are composable — none interferes with another; together they close all known failure modes.

---

```
/corps-build

Read the confirmed org.yaml and generate the complete org.

OUTPUT-1: org-chart.md containing four sections:
  S-1: ASCII hierarchy (Division > Team > Sub-group)
  S-2: Headcount table (6 required columns)
  S-3: Level distribution table
  S-4: Cross-reference audit table

OUTPUT-2: One typed role file per role at
  .craft/roles/{area-slug}/{role-slug}.md
  Written in mandatory sequence within each team.

Supports arbitrary nesting depth.
Inertia Advocate mandatory in every team.

---

INVARIANTS
(Declared here. Referenced by ID in steps. Never first-
defined inside a step body — that is FM-3.)

INV-1  PATH DERIVATION: All file paths derived from
       org.yaml slugs. Pattern:
       .craft/roles/{area-slug}/{role-slug}.md
       Validate path against org.yaml BEFORE each write.
       Non-derivable path: hard stop.

INV-2  FIVE TYPED FIELDS: Every role file contains:
         title:     Full role title
         role-type: standard | specialized | inertia-advocate
         area:      Verbatim name from org.yaml
         lens:      Domain-specific evaluation lens
         expertise: Specific domain knowledge required
       All five fields required. Substantive content required.
       Empty or placeholder: hard stop.

INV-3  IA LIFECYCLE: Every team runs three phases in order:
       STANDARD-PHASE → SPECIALIZED-PHASE → IA-PHASE.
       IA-PHASE entry requires RESISTANCE PROFILE completion.
       IA-PHASE exit requires IA-PHASE-COMPLETE emitted.
       Phase sequence is non-negotiable.

INV-4  PROFILE DERIVATION: Before writing any IA file,
       compute the resistance profile for that team:
         defended-artifact + change-pressure → lens-phrase
       The derived lens-phrase is used verbatim as the IA
       file's lens field. Generic resistance language
       ("resists change," "defends status quo") cannot
       result from a correct derivation and therefore
       structurally fails INV-4.

INV-5  COUNT INTEGRITY: PLAN TABLE total (Step 1) equals
       files written total (Step 4). Emit before completion.

---

FAILURE MODES
(Read all before producing any output. These wrong-output
patterns are what this prompt's architecture prevents.)

FM-1 [C-09] GENERIC IA CONTENT: IA lens or expertise
     uses non-domain language: "resists change," "defends
     status quo," "prefers stability," "cautious approach."
     Correct output results from INV-4 derivation: a
     lens-phrase that cannot be written without knowing
     both the defended-artifact and the change-pressure
     for this specific team. Generic resistance language
     is a derivation failure, not just a content failure.

FM-2 [C-10] SILENT CROSS-REFERENCE: Role-file count match
     performed but S-4 audit table contains prose instead
     of table rows. Correct S-4: a formatted table with
     Expected, Actual, and MATCH/MISMATCH literal in the
     Result column. See CHECK-OUTPUT PROTOCOL TABLE C.

FM-3 [C-11] UNDECLARED INVARIANTS: INV-1 through INV-5
     first appear inside step bodies, not in the named
     INVARIANTS section above. Correct output: all
     invariants in the entry-point INVARIANTS section,
     referenced by ID downstream, never first-defined
     in step bodies.

FM-4 [C-12] ASSERTION SUBSTITUTION: Verification appears
     as prose assertion: "All paths correct," "All fields
     present," "The counts match." Correct output: every
     check emits a table row with a PASS/FAIL or
     MATCH/MISMATCH literal in the Result column.

FM-5 [C-16] PHASE SKIP: Phase N+1 begins without Phase
     N's exit gate in the output. Correct: PARSE-PASS
     before Step 2; ROLES-COMPLETE before BUILD-VERIFY;
     IA-PHASE-COMPLETE before next team begins.

FM-6 [C-17] DEFERRED RECEIPT: TRANSCRIPTION-RECEIPT
     emitted in a batch summary block instead of
     immediately after each individual file write.
     Correct: receipt emitted synchronously per file —
     the receipt row for file N appears before file N+1
     begins writing.

FM-7 [C-18] VERIFY-PHASE CONTAMINATION: File writes or
     structural counts appear inside the BUILD-VERIFY
     phase. Correct: BUILD-VERIFY contains only per-
     artifact VERBATIM/DRIFT verdicts and the phase-exit
     token. Any other content is a phase contamination.

---

CHECK-OUTPUT PROTOCOL

All verification emits structured table rows.
All phases emit named exit tokens.
No check is satisfied by prose.

TABLE A — RECEIPT TABLE (filled synchronously during Step 2)

| Path | Role-Type | VERBATIM / REVISED | Notes |
|------|-----------|-------------------|-------|

One row per file. Emitted immediately after each write.

TABLE B — IA CLOSURE TABLE (filled per team during Step 2)

| Team | Defended-Artifact | Lens-Phrase | IA Title | Status |
|------|------------------|-------------|----------|--------|
| ...  | ...              | ...         | ...      | CLOSED |

One row per team. Emitted after each team's IA-PHASE-COMPLETE.

TABLE C — FINAL AUDIT TABLE (emitted in Step 4)

| Check | Expected | Actual | Result |
|-------|----------|--------|--------|
| IA files (per team) | [n] | [n] | MATCH/MISMATCH |
| Total role files | [n] | [n] | MATCH/MISMATCH |
| S-2 headcount total | [n] | [n] | MATCH/MISMATCH |
| Five fields (all files) | all | all | PASS/FAIL |
| All paths from org.yaml | all | all | PASS/FAIL |
| IA lenses from PROFILE | all | all | PASS/FAIL |

PHASE EXIT TOKENS (required at each boundary):
  PARSE-PASS | PARSE-FAIL (end of Step 1)
  STANDARD-PHASE-COMPLETE: {team} — [n] files
  SPECIALIZED-PHASE-COMPLETE: {team} — [n] files
  IA-PHASE-COMPLETE: {team} — {IA title} — lens: {phrase}
  ROLES-COMPLETE — [n] total files (before BUILD-VERIFY)
  BUILD-VERIFY-PASS | BUILD-VERIFY-DRIFT (skill complete)

---

STEP 1 — PARSE AND BUILD PLAN

Read org.yaml completely. Build tables before writing files.

PLAN TABLE (drives Step 2)

| Team | Standard | Specialized | IA | Total | Path Prefix |
|------|----------|-------------|-----|-------|-------------|
| ...  | ...      | ...         | 1   | ...   | .craft/roles/{area-slug}/ |
| TOTAL | ...     | ...         | [n] | [n]   | — |

Path Prefix: derived from org.yaml area names (INV-1).
TOTAL = INV-5 expected count.

LEVEL TERMS TABLE

| Group | Level Terms |
|-------|-------------|

All level vocabulary verbatim from org.yaml.

Emit: PARSE-PASS

---

STEP 2 — EXECUTE TEAM LIFECYCLES

Process teams in PLAN TABLE order.
Each team runs three phases in order (INV-3).

--- RESISTANCE PROFILE (INV-4) — compute before IA-PHASE ---

For each team, before IA-PHASE begins, derive:
  defended-artifact: the specific tool, process, or workflow
                     this team currently depends on
  change-pressure:   the specific initiative or new demand
                     that threatens this dependency
  lens-phrase:       derived from both — names the specific
                     inertia perspective this IA holds
Record in TABLE B (row filled after IA-PHASE-COMPLETE).

--- STANDARD-PHASE ---
Write one file per standard role.
  Validate path prefix (INV-1).
  Write five fields (INV-2): role-type: standard
  Emit TABLE A row immediately (FM-6).
Emit: STANDARD-PHASE-COMPLETE: {team-name} — [n] files

--- SPECIALIZED-PHASE ---
Write one file per specialized role.
  Substantively distinct from standard: different lens,
  different expertise domain. Not cosmetic renames.
  role-type: specialized
  Emit TABLE A row immediately (FM-6).
Emit: SPECIALIZED-PHASE-COMPLETE: {team-name} — [n] files

--- IA-PHASE (INV-3) ---
Complete RESISTANCE PROFILE first (INV-4).
Write one Inertia Advocate file:
  title:     Specific to team domain
  role-type: inertia-advocate
  area:      Verbatim from org.yaml (INV-2)
  lens:      The derived lens-phrase verbatim (INV-4)
  expertise: Names specific incumbents or legacy context
Emit TABLE A row immediately (FM-6).
Emit TABLE B row: {team} | {defended-artifact} |
  {lens-phrase} | {IA title} | CLOSED
Emit: IA-PHASE-COMPLETE: {team-name} — {IA title}
      — lens: {lens-phrase}

After all teams:
  Emit: ROLES-COMPLETE — [n] total files written

---

STEP 3 — WRITE org-chart.md

Write file: org-chart.md. Emit TABLE A row immediately.

S-1: ASCII HIERARCHY
+-- and | notation. Verbatim names from org.yaml.
Nesting matches org.yaml depth.

  +--[Division]
     +--[Team A]
     |  +--[Sub-group]
     +--[Team B]

S-2: HEADCOUNT TABLE (all six columns required; FM-2 basis)

| Group | Standard | Specialized | IA | Total | Levels |
|-------|----------|-------------|-----|-------|--------|
| ...   | ...      | ...         | ... | ...   | ...    |
| TOTAL | ...      | ...         | ... | [n]   | — |

IA column: count of IA files per group. Required.
Levels: use LEVEL TERMS TABLE values per group.
TOTAL = INV-5 expected count.

S-3: LEVEL DISTRIBUTION TABLE

| Level Term | Role File Count | Groups Using |
|------------|----------------|--------------|

S-4: CROSS-REFERENCE AUDIT TABLE (TABLE C rows 3 and 2)

| Check | Expected | Actual | Result |
|-------|----------|--------|--------|
| S-2 headcount total | [n] | [n] | MATCH/MISMATCH |
| Role files written | [n] | [n] | MATCH/MISMATCH |

---

STEP 4 — BUILD-VERIFY

SINGLE-PURPOSE PHASE. THIS PHASE CONTAINS NO FILE WRITES.
Any content other than per-artifact verdicts and TABLE C
is a phase contamination (FM-7).

For each artifact from Steps 2–3:
  "BUILD-VERIFY: {path} — VERBATIM | DRIFT"
  For IA files, also emit:
  "BUILD-VERIFY-LENS: {team-name} — VERBATIM | DRIFT"
  DRIFT: "DRIFT DETAIL: {specific difference found}"

Emit TABLE C in full after all artifact verdicts.
Any MISMATCH or FAIL row: identify and correct before
emitting the phase-exit token.

Emit consolidated TABLE B (all teams):
| Team | Defended-Artifact | Lens-Phrase | IA Title | Status |
All rows must show CLOSED.

Phase-exit token:
  BUILD-VERIFY-PASS  (all VERBATIM, TABLE C all MATCH/PASS)
  BUILD-VERIFY-DRIFT (any DRIFT or FAIL — list artifact paths)

Skill is complete only when BUILD-VERIFY-PASS emitted and
TABLE C shows no unresolved MISMATCH or FAIL rows.

---

AMEND

AMEND-A  AREA REGENERATION: Regenerate a specific area.
         Re-run RESISTANCE PROFILE for each team in the area.
         Re-run STANDARD-PHASE, SPECIALIZED-PHASE, IA-PHASE
         for each team. Re-emit TABLE A and TABLE B rows
         for regenerated artifacts. Re-emit BUILD-VERIFY
         for regenerated area. Re-emit TABLE C with updated
         counts.

AMEND-B  LEVEL VOCABULARY UPDATE: Replace a level term.
         Update LEVEL TERMS TABLE. Update all affected files.
         Update S-3 LEVEL DISTRIBUTION TABLE. Emit
         "[n] files updated — PASS".

AMEND-C  GROUP NODE ADDITION: Add new group node.
         Validate new path prefixes against INV-1 before
         writing. Add rows to PLAN TABLE. Run all three
         phases plus RESISTANCE PROFILE for each new team.
         Emit TABLE A and TABLE B rows for new teams.
         Re-emit S-2 HEADCOUNT TABLE with new group rows.
         Re-emit TABLE C with updated total counts.
```

---

## Variation Summary

| # | Axis | Core Bet | C-11 Architecture | C-14/C-13 Architecture | C-15 Architecture | C-16 Coverage | C-17 Coverage | C-18 Coverage |
|---|------|----------|-------------------|----------------------|-------------------|---------------|---------------|---------------|
| V-01 | Role Sequence | Per-phase sequence gates bind INV-4 write order to named exit tokens | INV-1 through INV-5 declared before steps | FM-1 through FM-6 block; FM-1/2/3/4 target C-09/10/11/12 | CHECK-OUTPUT PROTOCOL Rules 1–6 | 5 named gates: PARSE-PASS, STANDARD/SPECIALIZED/IA-PHASE-COMPLETE, ROLES-COMPLETE, BUILD-VERIFY-PASS | RECEIPT emitted per file, Rule 3 | STEP 4 single-purpose, content-type described |
| V-02 | Output Format | Table-row-only verification makes missing gates structurally visible | INV-A through INV-E declared before steps | FM-A through FM-F block; FM-A/B/C/D target C-09/10/11/12 | CHECK-OUTPUT PROTOCOL Rules 1–5 with TABLE FORMAT | PARSE-PASS, ROLES-COMPLETE, BUILD-VERIFY-PASS tokens; IA rows in RECEIPT TABLE | RECEIPT TABLE row emitted per file synchronously (FM-F) | STEP 4 labeled VERIFICATION ONLY; no file writes permitted |
| V-03 | Phrasing Register | MUST/PROHIBITED language makes every constraint a hard stop | INV-1 through INV-5 declared; first-definition in step body PROHIBITED | PROHIBITED-1 through PROHIBITED-6 block; PROHIBITED-1/2/3/4 target C-09/10/11/12 | CHECK-OUTPUT PROTOCOL RULES 1–6 with MUST/PROHIBITED language | RULE 2 names 4 gates; PROHIBITED-5 names phase skip as prohibited | RULE 4 TRANSCRIPTION-RECEIPT; PROHIBITED-6 names deferred receipt | STEP 4: "THIS PHASE: no file writes… adding file write is PROHIBITED" |
| V-04 | Inertia + Lifecycle | Resistance-profile derivation (INV-4) prevents generic IA by making it a computation, not an instruction | INV-1 through INV-5 with INV-3/INV-4 as lifecycle phase invariants | FM-1 through FM-6 block; FM-1 is richest — names derivation failure | CHECK-OUTPUT PROTOCOL OBL-1 through OBL-5 named obligations | OBL-2 names 6 gates including lens-match phase | OBL-3 TRANSCRIPTION-RECEIPT per file; FM-6 names deferred receipt failure | STEP 4 SINGLE-PURPOSE; content prohibition: "only verdicts and phase-exit token" |
| V-05 | Full Synthesis | All structural elements simultaneously — they compose without interference | INV-1 through INV-5 + INV-4 profile derivation | FM-1 through FM-7 block; FM-7 adds phase contamination for C-18 | CHECK-OUTPUT PROTOCOL with TABLE A/B/C and PHASE EXIT TOKENS | TABLE C PHASE EXIT TOKENS section names all 7 gates | TABLE A RECEIPT TABLE filled synchronously per file; FM-6 names failure | STEP 4: "SINGLE-PURPOSE PHASE. THIS PHASE CONTAINS NO FILE WRITES." |

**What V-04 and V-05 add over V-01/V-02/V-03**:
V-04's RESISTANCE PROFILE derivation (INV-3/INV-4 together) makes C-09 compliance structural — the lens-phrase cannot be generic because it is computed from two domain-specific inputs. V-05 carries this derivation AND adds TABLE B to track lens-phrase provenance across all teams, making lens fidelity auditable at BUILD-VERIFY via the BUILD-VERIFY-LENS check. FM-7 in V-05 (phase contamination) is the only variation to explicitly name BUILD-VERIFY contamination as a failure mode.
