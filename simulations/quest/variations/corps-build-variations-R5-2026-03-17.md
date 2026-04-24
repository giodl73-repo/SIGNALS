Looking at the rubric v3, the two new structural innovations are:
- **C-14**: All 4 aspirational failure modes front-loaded in a dedicated pre-step block
- **C-15**: Named CHECK-OUTPUT PROTOCOL section as first-class obligation

Let me write 5 complete variations that architect around these new requirements.

---

# corps-build — Variate R5 (V-01 through V-05)

**Rubric**: v3 | **Golden threshold**: 103/125 | **New criteria**: C-14 (dedicated FAILURE MODES pre-step), C-15 (named CHECK-OUTPUT PROTOCOL section)

---

## V-01 — Axis: Role Sequence

**Hypothesis**: Enforcing write-order discipline (standard → specialized → IA) as a named sequence invariant — checked at each team boundary — reduces role-type confusion and prevents specialized roles from being copied from standard with only minor edits.

---

```
/corps-build

Read the confirmed org.yaml and generate the full org.
Outputs: (1) org-chart.md with ASCII box diagram, headcount
by group/area, and level distribution; (2) a .roles/
{area}/{role}.md typed file for every role in the org.

Supports arbitrary group nesting: Division > Team > Sub-group.
Inertia Advocate must appear in every team.

---

INVARIANTS

Declare before any steps. Every invariant is enforced by
name in the step body and AMEND section.

INV-1  PATH FIDELITY: Every role file is written to
       .roles/{area-slug}/{role-slug}.md where
       area-slug and role-slug are derived directly from
       org.yaml. No file is created outside a directory
       that exists in org.yaml.

INV-2  WRITE ORDER: For every team, write in this exact
       sequence: (a) standard roles, (b) specialized roles,
       (c) Inertia Advocate. Never write specialized before
       standard. Never write IA before all standard and
       specialized are complete for that team.

INV-3  IA CLOSURE: Every team must close with exactly one
       Inertia Advocate file. Completing a team without IA
       is a hard error — do not advance to the next team.

INV-4  FIELD COMPLETENESS: Every role file must contain all
       five fields: title, role-type, area, lens, expertise.
       Each field must have a substantive body. Placeholder
       text is a hard error.

INV-5  ROLE COUNT MATCH: Total files declared in the
       summary must equal total files written in Step 2.
       A discrepancy must be identified and corrected before
       the skill declares completion.

---

FAILURE MODES
(Read all five before producing any output. These are the
wrong-output patterns this prompt is designed to prevent.)

FM-1  GENERIC IA: Inertia Advocate lens and expertise use
      generic resistance language ("defends status quo",
      "prefers stability") without drawing from this team's
      domain vocabulary. Correct output names the inertia
      specifically: what incumbents say, what the actual
      switching cost is, what this team's complacency looks
      like.

FM-2  SILENT CROSS-REFERENCE: The org-chart/role-file count
      match is performed but not emitted. Correct output
      includes a literal string: "Table Total = [n], files
      written = [n] — [MATCH | MISMATCH]".

FM-3  LATE INVARIANT: INV-1 through INV-5 appear mid-step
      or are restated inline without entry-point declaration.
      Correct output declares all invariants in a named block
      before Step 1 and references each by name downstream.

FM-4  IMPLICIT VERIFICATION: The model confirms correctness
      through prose assertion ("all roles are present")
      rather than emitting a machine-readable check string.
      Correct output includes at least one [PASS | FAIL] or
      [MATCH | MISMATCH] literal in the final output.

---

CHECK-OUTPUT PROTOCOL

The following rules govern all verification in this skill.
Verification is a first-class output obligation, not a
compliance note.

Rule 1 — EMIT, DON'T ASSERT: Every check produces a
         literal string the user can grep. Prose assertions
         ("all files are present") do not satisfy any check.

Rule 2 — SEQUENCE GATE: INV-2 write-order is checked at
         each team boundary. Emit "[INV-2 PASS: standard
         complete before specialized complete before IA]"
         before advancing.

Rule 3 — IA GATE: Before leaving any team, emit
         "[INV-3 PASS: IA written for {team-name}]" or
         "[INV-3 FAIL: IA missing for {team-name} — stopping]".

Rule 4 — COUNT GATE: After all files are written, emit:
         "Table Total = [n], files written = [n] —
         [MATCH | MISMATCH]"

Rule 5 — FIELD GATE: After writing each file, the five
         required fields must all be present. If any field
         is empty or placeholder, emit "[INV-4 FAIL: {field}
         missing in {path}]" before proceeding.

---

STEP 1 — READ AND PLAN

Parse the org.yaml completely before writing anything.

a. Identify all Division > Team > Sub-group nesting.
   Build the full team list in write order.

b. For each team, enumerate: (i) standard roles,
   (ii) specialized roles, (iii) IA (always last).
   Record this sequence before writing (INV-2).

c. Compute expected file count = sum of all roles across
   all teams. Record this number now (INV-5).

d. Identify the level vocabulary from org.yaml. If the
   org uses custom level terms (e.g., "Principal" instead
   of "Senior"), note them here. Do not substitute.

---

STEP 2 — WRITE ROLE FILES

For each team in write-order (INV-2):

  a. Write all STANDARD roles first.
     Standard roles represent the team's baseline function.
     Each file: .roles/{area-slug}/{role-slug}.md
     Validate path against org.yaml before writing (INV-1).

  b. Write all SPECIALIZED roles second.
     Specialized roles must be substantively distinct from
     standard. A specialized role with only cosmetic name
     changes from a standard role is a hard error.
     role-type: specialized in frontmatter.

  c. Write INERTIA ADVOCATE last.
     IA lens and expertise must draw from this team's
     declared domain vocabulary (FM-1). Generic language
     fails. Name the specific inertia: what incumbent
     vendors say, what the switching cost narrative is,
     what this team's version of "we've always done it
     this way" sounds like.
     Emit gate: "[INV-3 PASS: IA written for {team-name}]"

     Then advance to the next team (INV-2 enforced).

All five fields per file (INV-4):
  title:     Full role title
  role-type: standard | specialized | inertia-advocate
  area:      Verbatim group/team name from org.yaml
  lens:      The primary evaluation lens this role brings
  expertise: Specific domain knowledge required

---

STEP 3 — WRITE org-chart.md

Produce the ASCII org-chart using +-- and | notation.
All names must be verbatim from org.yaml. Nesting must
reflect Division > Team > Sub-group depth.

Example notation (do not alter names to fit — names are fixed):

  +--[Division Name]
     +--[Team Name]
     |  +--[Sub-group Name]
     +--[Team Name]

Below the chart, include:

HEADCOUNT TABLE

| Group | Standard | Specialized | IA | Total | Levels |
|-------|----------|-------------|-----|-------|--------|
| ...   | ...      | ...         | ... | ...   | ...    |

Levels column: list all level terms used in that group.

---

STEP 4 — VERIFY (CHECK-OUTPUT PROTOCOL)

Emit the following in sequence:

1. INV-2 summary: "Write-order discipline: [n] teams
   processed standard → specialized → IA — [PASS | FAIL]"

2. INV-3 summary: "[n] IA files written, [n] teams
   total — [MATCH | MISMATCH]"

3. INV-5 count gate: "Table Total = [n], files written
   = [n] — [MATCH | MISMATCH]"

4. Field completeness: "INV-4: All five fields present
   in all [n] files — [PASS | FAIL]"

If any gate fails, identify the specific team or file
and correct before proceeding.

---

AMEND

Use these options to repair or extend the generated org:

AMEND-A  AREA REGENERATION: Regenerate a specific area.
         Re-run Steps 2–4 for the named area only.
         Re-check INV-1 (path), INV-2 (write order),
         INV-3 (IA closure), INV-4 (field completeness).
         Emit all CHECK-OUTPUT PROTOCOL gates for the
         regenerated area.

AMEND-B  LEVEL VOCABULARY UPDATE: Replace all instances of
         one level term with another across all files in
         the affected area. Emit "[n] files updated — PASS"
         after completion.

AMEND-C  GROUP NODE ADDITION: Insert a new group node into
         the org.yaml-derived hierarchy. Validate new paths
         against INV-1 before writing any files. Run IA
         closure gate (INV-3) for any new teams added.
```

---

## V-02 — Axis: Output Format

**Hypothesis**: Prescribing explicit table structures for every output (headcount, level distribution, cross-reference, field audit) turns format compliance into a constraint the model checks, not a stylistic choice it makes.

---

```
/corps-build

Read a confirmed org.yaml and generate the complete org.
Two outputs: (1) org-chart.md — ASCII hierarchy + headcount
table + level distribution table; (2) typed role files at
.roles/{area}/{role}.md for every role.

Supports arbitrary nesting depth: Division > Team > Sub-group.
Every team must include an Inertia Advocate.

---

INVARIANTS

INV-A  STRUCTURAL FIDELITY: Role files written only to
       paths derived from org.yaml. Pattern:
       .roles/{area-slug}/{role-slug}.md.
       Pre-write path validation required.

INV-B  TYPED FIELDS: Every role file includes all five
       fields with substantive content: title, role-type,
       area, lens, expertise. Empty or placeholder is error.

INV-C  IA MANDATORY: One Inertia Advocate per team, no
       exceptions. No team is closed until IA is written.

INV-D  COUNT INTEGRITY: Files declared in summary equals
       files written. Verify and emit before completion.

---

FAILURE MODES
(Anchor all output against these. The model must have
encountered each wrong-output pattern before writing.)

FM-A  GENERIC INERTIA ADVOCATE: IA file uses
      non-specific language: "resists change", "defends
      status quo", "prefers established methods". Correct
      output: lens names this team's domain, expertise
      names this team's incumbent stack or process, the
      inertia has a concrete face.

FM-B  PROSE COUNT ASSERTION: The role-count match is
      confirmed in text ("all roles were generated") rather
      than as a formatted table row. Correct output:
      the count check appears as a literal emitted row
      in the AUDIT TABLE.

FM-C  INLINE INVARIANT ONLY: INV-A through INV-D are
      mentioned inside steps but not declared as a named
      group before Step 1. Correct output: invariants are
      named and listed at the top before any steps.

FM-D  SILENT VERIFICATION: The model performs all checks
      but emits no machine-readable status. Correct output:
      every check produces a table row with a PASS/FAIL or
      MATCH/MISMATCH literal.

---

CHECK-OUTPUT PROTOCOL

Verification is a first-class output format requirement.
Every check emits a table row, not a prose sentence.

Table format for all checks:

  | Check    | Expected | Actual | Result              |
  |----------|----------|--------|---------------------|
  | INV-C IA | [n teams]| [n]    | MATCH / MISMATCH    |
  | INV-D    | [n files]| [n]    | MATCH / MISMATCH    |
  | INV-B    | 5 fields | 5      | PASS / FAIL         |

Rule 1 — TABLE ROW: Every gate emits a table row. Prose
         assertions do not satisfy any gate.

Rule 2 — IA ROW: Per-team IA gate appears as a row in
         the AUDIT TABLE before the team is closed.

Rule 3 — FIELD ROW: Any file with a missing or placeholder
         field gets a FAIL row with the specific field named.

Rule 4 — FINAL AUDIT TABLE: Emitted after Step 3,
         consolidating all per-team IA rows and the
         file-count row.

---

STEP 1 — PARSE AND PLAN

Read org.yaml completely. Build the following tables before
writing any files:

PLAN TABLE

| Team | Standard Count | Specialized Count | IA | Total |
|------|---------------|-------------------|----|-------|
| ...  | ...           | ...               | 1  | ...   |

Total row at bottom. This total is the INV-D expected count.

LEVEL TERMS TABLE

| Group | Level Terms Used |
|-------|-----------------|
| ...   | ...             |

If org.yaml uses custom level terms, record them here.
All role files must use these exact terms.

---

STEP 2 — WRITE ROLE FILES

Process teams in org.yaml order. For each team:

  STANDARD ROLES
  Write one file per standard role.
  Path: .roles/{area-slug}/{role-slug}.md (INV-A)
  role-type: standard

  SPECIALIZED ROLES
  Write one file per specialized role.
  Specialized roles must be substantively distinct:
  different lens, different expertise domain.
  role-type: specialized

  INERTIA ADVOCATE
  One IA per team (INV-C).
  Lens and expertise must name this team's domain
  specifically (FM-A). No generic inertia language.

  After writing IA, emit the per-team row:
  | [team name] IA | 1 | 1 | MATCH |

  All files: five fields required (INV-B):
    title:     Full role title
    role-type: standard | specialized | inertia-advocate
    area:      Verbatim name from org.yaml
    lens:      Primary evaluation lens
    expertise: Specific domain knowledge

---

STEP 3 — WRITE org-chart.md

Section 1 — ASCII HIERARCHY
Use +-- and | notation. Verbatim names from org.yaml.
Depth reflects Division > Team > Sub-group structure.

Section 2 — HEADCOUNT TABLE

| Group | Standard | Specialized | IA | Total | Levels |
|-------|----------|-------------|-----|-------|--------|

All rows from PLAN TABLE. Levels column uses terms from
LEVEL TERMS TABLE. Total row at bottom.

Section 3 — LEVEL DISTRIBUTION TABLE

| Level Term | File Count | Groups Using |
|------------|-----------|--------------|

Section 4 — CROSS-REFERENCE TABLE

| Source | Count | Result |
|--------|-------|--------|
| Headcount Table Total | [n] | — |
| Role Files Written | [n] | MATCH / MISMATCH |

---

STEP 4 — FINAL AUDIT TABLE

Emit consolidated audit after all files are written.
Format (CHECK-OUTPUT PROTOCOL, Rule 4):

| Check | Expected | Actual | Result |
|-------|----------|--------|--------|
| IA per team — [team 1] | 1 | [n] | MATCH/MISMATCH |
| IA per team — [team 2] | 1 | [n] | MATCH/MISMATCH |
| ... | | | |
| Total file count | [n] | [n] | MATCH/MISMATCH |
| Five fields per file | 5 | [n] | PASS/FAIL |
| Cross-reference (chart=files) | [n] | [n] | MATCH/MISMATCH |

Any MISMATCH or FAIL row must be resolved before the
skill declares completion.

---

AMEND

AMEND-A  AREA REGENERATION: Regenerate one area.
         Rebuild PLAN TABLE for that area. Re-run Steps
         2–4 for named area. Emit complete AUDIT TABLE
         for the regenerated area (all INV rows).

AMEND-B  LEVEL VOCABULARY: Update one level term across
         all files in affected groups. Re-emit LEVEL
         DISTRIBUTION TABLE after update. Emit "[n] files
         updated — PASS".

AMEND-C  GROUP NODE ADDITION: Add new group node.
         Validate paths against INV-A. Add rows to PLAN
         TABLE. Run Step 2 for new teams. Emit per-team IA
         rows. Re-emit cross-reference AUDIT TABLE row.
```

---

## V-03 — Axis: Phrasing Register (Full Imperative)

**Hypothesis**: Replacing all descriptive or conditional language with strict imperative directives ("DO NOT", "PROHIBITED", "STOP AND CORRECT") eliminates the model's interpretive latitude on compliance — every rule reads as a hard constraint, not a suggestion.

---

```
/corps-build

COMMAND: Read the confirmed org.yaml. Generate the complete
org. Produce exactly two outputs: (1) org-chart.md; (2) one
typed role file per role at .roles/{area}/{role}.md.

DO NOT begin writing any output until you have read every
invariant, every failure mode, and the CHECK-OUTPUT PROTOCOL
in full. Produce no output before completing this read.

---

INVARIANTS

You MUST declare all invariants before Step 1. You MUST
reference each invariant by name in the step where it is
enforced. Restating an invariant only inline without an
entry-point declaration is PROHIBITED.

INV-1  PATH PROHIBITION: NEVER write a file to any path
       not derivable from org.yaml. Pattern MUST be:
       .roles/{area-slug}/{role-slug}.md. Validate
       every path before writing. STOP on first violation.

INV-2  FIELD MANDATE: EVERY role file MUST contain exactly
       five fields with substantive content: title,
       role-type, area, lens, expertise. DO NOT write a
       file with an empty or placeholder field. STOP on
       first violation.

INV-3  IA PROHIBITION: DO NOT close any team until you have
       written exactly one Inertia Advocate file for that
       team. NEVER advance to the next team before IA is
       complete. There are NO exceptions to this rule.

INV-4  COUNT PROHIBITION: DO NOT declare the skill
       complete unless the file count in the summary
       exactly matches the file count written in Step 2.
       STOP and correct any discrepancy before proceeding.

---

FAILURE MODES
(You MUST read all four before writing any output. These
patterns are PROHIBITED in your output. Encountering them
after writing is a failure — prevent them now.)

PROHIBITED-1  GENERIC IA LANGUAGE: Writing an Inertia
              Advocate file whose lens or expertise uses
              non-domain language: "resists change",
              "prefers the status quo", "defends existing
              processes". This is a hard failure. IA lens
              MUST name this team's specific domain. IA
              expertise MUST name the specific incumbent
              tools, vendors, or processes this team's
              inertia is attached to.

PROHIBITED-2  INVISIBLE COUNT CHECK: Completing the skill
              without emitting a literal count-check string.
              DO NOT use prose assertion. You MUST emit:
              "Table Total = [n], files written = [n] —
              [MATCH | MISMATCH]"

PROHIBITED-3  LATE INVARIANTS: Mentioning any invariant for
              the first time inside a step body. You MUST
              declare INV-1 through INV-4 in the INVARIANTS
              section above Step 1. You MUST reference them
              by name in steps — you MUST NOT define them
              in steps.

PROHIBITED-4  SILENT COMPLIANCE: Performing any check
              without emitting a machine-readable result.
              Every check MUST produce an emitted string
              with PASS/FAIL or MATCH/MISMATCH. Prose
              descriptions of checks do not satisfy this
              requirement.

---

CHECK-OUTPUT PROTOCOL

This section is mandatory. You MUST follow all five rules.
No rule is optional. No rule may be satisfied by prose.

RULE 1 — EMIT LITERALS ONLY: Every verification result
         MUST be a literal string. You MUST NOT write "the
         counts match" or "all fields are present". You
         MUST write the exact string specified.

RULE 2 — PER-TEAM IA GATE: After writing each team's IA
         file, you MUST emit:
         "[INV-3 PASS: IA written — {team-name}]"
         If IA is missing, you MUST emit:
         "[INV-3 FAIL: IA missing — {team-name} — STOPPING]"
         and STOP. DO NOT advance.

RULE 3 — PER-FILE FIELD GATE: After writing each file,
         you MUST verify all five fields are present and
         substantive. If any field fails, you MUST emit:
         "[INV-2 FAIL: {field} missing — {path}]"
         and STOP. DO NOT write the next file.

RULE 4 — FINAL COUNT GATE: After writing all files, you
         MUST emit:
         "Table Total = [n], files written = [n] —
         [MATCH | MISMATCH]"
         MISMATCH requires immediate correction.

RULE 5 — SKILL COMPLETION GATE: You MUST NOT declare the
         skill complete unless all gates above have emitted
         PASS or MATCH. Any unresolved FAIL or MISMATCH
         PROHIBITS completion.

---

STEP 1 — READ AND PLAN (DO NOT WRITE ANY FILES)

You MUST complete this step in full before writing anything.

a. Parse the complete org.yaml. Map every Division, Team,
   and Sub-group. Record the full hierarchy.

b. For every team, enumerate roles in mandatory sequence:
   (i) standard roles, (ii) specialized roles, (iii) IA.
   DO NOT write this list out of order.

c. Count total expected files across all teams.
   Record this number now. This is the INV-4 expected count.

d. Identify all level terms used in org.yaml.
   You MUST use these exact terms in role files.
   NEVER substitute your own level vocabulary.

---

STEP 2 — WRITE ROLE FILES

For each team in org.yaml order, write in INV-3 mandatory
sequence: standard → specialized → IA.

STANDARD ROLES:
  - Validate path against INV-1 before writing
  - Write all five fields per INV-2
  - role-type: standard

SPECIALIZED ROLES:
  - MUST be substantively distinct from standard roles
  - PROHIBITED: Copying a standard role and changing only
    the title. Lens and expertise MUST differ.
  - role-type: specialized

INERTIA ADVOCATE (MANDATORY — INV-3):
  - One per team. No exceptions. No skipping.
  - Lens: MUST name this team's specific domain.
    PROHIBITED-1 language is not permitted here.
  - Expertise: MUST name specific incumbents, tools,
    or processes that represent this team's status quo.
  - Emit: "[INV-3 PASS: IA written — {team-name}]"

FIVE REQUIRED FIELDS (INV-2):
  title:     Full role title (MUST be specific)
  role-type: standard | specialized | inertia-advocate
  area:      Verbatim from org.yaml (MUST NOT paraphrase)
  lens:      Primary evaluation lens (MUST be domain-specific)
  expertise: Domain knowledge required (MUST be specific)

---

STEP 3 — WRITE org-chart.md

You MUST produce all three sections. NONE may be omitted.

SECTION 1 — ASCII HIERARCHY
Use ONLY +-- and | notation.
Names MUST be verbatim from org.yaml.
DO NOT abbreviate, reorder, or reword any name.
Nesting MUST reflect org.yaml hierarchy depth.

SECTION 2 — HEADCOUNT TABLE
Required columns — you MUST NOT omit any column:

| Group | Standard | Specialized | IA | Total | Levels |
|-------|----------|-------------|-----|-------|--------|

Levels column: list all level terms appearing in that group.

SECTION 3 — CROSS-REFERENCE CHECK
Emit as a literal line (RULE 4):
"Table Total = [n], files written = [n] —
[MATCH | MISMATCH]"

---

STEP 4 — FINAL VERIFICATION

You MUST emit all gates before declaring completion.

1. "[INV-3: [n] IA files written, [n] teams — MATCH/MISMATCH]"
2. "Table Total = [n], files written = [n] — MATCH/MISMATCH"
3. "[INV-2: All five fields present in all [n] files — PASS/FAIL]"
4. "[INV-1: All paths derive from org.yaml — PASS/FAIL]"

Any unresolved FAIL or MISMATCH: STOP. Correct. Re-emit.

---

AMEND

AMEND-A  AREA REGENERATION: Regenerate a specific area.
         You MUST re-validate INV-1, INV-2, INV-3 for the
         regenerated area. You MUST re-emit all per-team IA
         gates and the final count gate for that area.

AMEND-B  LEVEL VOCABULARY UPDATE: Replace a level term
         across affected files. EMIT "[n] files updated —
         PASS" after completion.

AMEND-C  GROUP NODE ADDITION: Add a new group node.
         You MUST validate all new paths against INV-1.
         You MUST run IA closure gate for all new teams.
         You MUST emit updated cross-reference count gate.
```

---

## V-04 — Combined: Inertia Framing + Lifecycle Emphasis

**Hypothesis**: Treating the Inertia Advocate as a named first-class lifecycle phase ("IA PHASE") — not just a required role — and expanding lifecycle phase boundaries with explicit entry/exit criteria eliminates the most common IA failure: correct file written, wrong content.

---

```
/corps-build

Read a confirmed org.yaml and generate the complete org.
Two outputs:
  OUTPUT-1: org-chart.md — ASCII hierarchy, headcount table,
            level distribution, cross-reference check
  OUTPUT-2: .roles/{area}/{role}.md — one typed file
            per role across all teams

Supports arbitrary nesting: Division > Team > Sub-group.
The Inertia Advocate is not just a required role — it is a
required phase of every team's generation lifecycle.

---

INVARIANTS

All invariants declared here. Referenced by name in steps.

INV-1  PATH FIDELITY: Role files written only to
       .roles/{area-slug}/{role-slug}.md. Slugs
       derived directly from org.yaml names. Validated
       before write.

INV-2  TYPED FIELDS: Every role file contains five fields
       with substantive content: title, role-type, area,
       lens, expertise.

INV-3  IA PHASE GATE: Every team runs exactly three phases:
       STANDARD PHASE → SPECIALIZED PHASE → IA PHASE.
       IA PHASE is not optional. No team exits IA PHASE
       without a written, domain-grounded IA file.

INV-4  COUNT INTEGRITY: Expected file count (from Step 1
       planning) matches written file count (from Step 2
       execution). Verified and emitted before completion.

---

FAILURE MODES
(Pre-step. All four must be read before any output is
produced. These patterns invalidate the run.)

FM-1  INERTIA WITHOUT FACE: The IA file is written but
      the inertia has no face. Lens: "represents the
      cautious perspective." Expertise: "experience with
      legacy systems." This is the most common IA failure.
      It looks correct from the outside but teaches nothing
      about the actual competitive threat.

      Correct IA grounds the inertia in this team's work:
      What do the incumbent vendors say in sales calls?
      What does "we've always done it this way" mean
      specifically for this domain? What is the actual
      switching cost narrative users invoke?

FM-2  INVISIBLE COUNT AUDIT: Step 3 runs, files are
      written, no count-check string is emitted. "All roles
      generated" appears in the response. This is a silent
      failure. Correct output emits:
      "Table Total = [n], files written = [n] —
      [MATCH | MISMATCH]"

FM-3  ORPHANED INVARIANTS: INV-1 through INV-4 appear only
      in steps, not in a named pre-step section. Without
      entry-point declaration, the invariants cannot be
      referenced by name and become prose requirements
      indistinguishable from suggestions.

FM-4  VERIFICATION BY ASSERTION: Verification appears as
      prose: "The headcount table matches the role files."
      Correct output includes at least one literal emitted
      check string per protocol (PASS/FAIL or
      MATCH/MISMATCH).

---

CHECK-OUTPUT PROTOCOL

Named obligations. Every obligation emits a literal string.

OBL-1  IA PHASE CLOSE: On completing each team's IA PHASE,
       emit:
       "[INV-3 IA PHASE CLOSED: {team-name} — {IA title}]"
       This must name the actual title written, not a
       placeholder.

OBL-2  TEAM LIFECYCLE CLOSE: On completing all three phases
       for a team, emit:
       "[TEAM CLOSED: {team-name} — standard={n},
       specialized={n}, IA=1]"

OBL-3  COUNT GATE: After all teams are complete, emit:
       "Table Total = [n], files written = [n] —
       [MATCH | MISMATCH]"

OBL-4  FIELD GATE: Any file with empty or placeholder
       fields emits:
       "[INV-2 FAIL: {field} missing — {path}]"

OBL-5  SKILL COMPLETE: The skill is complete only when
       all OBL-1 through OBL-3 have been emitted with
       PASS or MATCH, and no OBL-4 failures are unresolved.

---

STEP 1 — PARSE AND SCHEDULE

Read org.yaml. Build the team lifecycle schedule.

For each team, record:
  Team name (verbatim from org.yaml)
  STANDARD PHASE: list of standard roles
  SPECIALIZED PHASE: list of specialized roles
  IA PHASE: 1 (always — INV-3)

Record total expected file count.

Note level terms: use verbatim throughout.

---

STEP 2 — EXECUTE TEAM LIFECYCLES

For each team in org.yaml order, run three phases:

--- STANDARD PHASE ---
Write one file per standard role.
Path: .roles/{area-slug}/{role-slug}.md (INV-1)
All five fields required (INV-2).
role-type: standard

--- SPECIALIZED PHASE ---
Write one file per specialized role.
Specialized roles must differ substantively from standard:
different lens, different expertise domain, different
level of depth. A cosmetic rename fails.
role-type: specialized

--- IA PHASE ---
Write the Inertia Advocate file.
This phase is what separates a complete org from an
incomplete one. The IA represents the competitive threat
that comes from doing nothing: the real alternative to
adopting this team's function is sticking with what
already exists.

IA GROUNDING REQUIREMENTS:
  lens: Name the team's domain specifically.
        What perspective does the incumbent bring?
        E.g., not "operational perspective" but
        "enterprise procurement conservatism" or
        "incumbent CRM loyalty."
  expertise: Name the specific incumbent context.
        E.g., not "legacy system experience" but
        "10-year Salesforce deployment inertia" or
        "org memory of the failed 2019 migration."

The IA file must pass the FM-1 test: it must name
specific inertia, not generic resistance.

On completion:
  Emit OBL-1: "[INV-3 IA PHASE CLOSED: {team-name} —
  {IA title}]"
  Emit OBL-2: "[TEAM CLOSED: {team-name} — standard={n},
  specialized={n}, IA=1]"

---

STEP 3 — WRITE org-chart.md

ASCII HIERARCHY
+-- and | notation. Verbatim org.yaml names.
Depth reflects org.yaml nesting.

HEADCOUNT TABLE

| Group | Standard | Specialized | IA | Total | Levels |
|-------|----------|-------------|-----|-------|--------|

All five columns required. Levels column: list level terms.

LEVEL DISTRIBUTION TABLE

| Level Term | Count | Groups |
|------------|-------|--------|

Emit OBL-3: "Table Total = [n], files written = [n] —
[MATCH | MISMATCH]"

---

STEP 4 — LIFECYCLE AUDIT

Emit all team close strings in sequence:
  [TEAM CLOSED: {team-1} — ...]
  [TEAM CLOSED: {team-2} — ...]
  ...

Emit final gates:
  OBL-3 count gate
  "[INV-2: All five fields present — PASS/FAIL]"
  "[INV-1: All paths from org.yaml — PASS/FAIL]"

---

AMEND

AMEND-A  AREA REGENERATION: Re-run the full team lifecycle
         (STANDARD → SPECIALIZED → IA PHASE) for the
         named area. Re-emit OBL-1 and OBL-2 for each team.
         Re-emit OBL-3 for the regenerated area.

AMEND-B  LEVEL VOCABULARY: Update level terms across files.
         Emit "[n] files updated — PASS" after completion.

AMEND-C  GROUP NODE ADDITION: Add group node to hierarchy.
         Schedule new teams into lifecycle. Run all three
         phases per new team. Emit all close strings.
```

---

## V-05 — Combined: Role Sequence + Output Format

**Hypothesis**: The tightest structural compliance comes from combining prescribed write-order invariants with mandated output table formats — every sequence gate and every count gate has a fixed table row format that makes both the model's sequence and its verification visible in the final document.

---

```
/corps-build

Read the confirmed org.yaml and generate the complete org.

OUTPUT-1: org-chart.md containing four sections:
  S-1: ASCII org hierarchy
  S-2: Headcount-by-group table (6 columns)
  S-3: Level distribution table
  S-4: Cross-reference audit table

OUTPUT-2: Typed role files at .roles/{area}/{role}.md,
  one per role, in mandatory sequence within each team.

Supports arbitrary nesting: Division > Team > Sub-group.
Inertia Advocate mandatory in every team.

---

INVARIANTS

Declared before any steps. Referenced by name in steps.

INV-S1  WRITE SEQUENCE: Within each team, write in this
        exact order: (a) standard roles, (b) specialized
        roles, (c) Inertia Advocate. Sequence is enforced
        by emitting a SEQUENCE TABLE row after each phase.

INV-S2  PATH DERIVATION: All file paths derived from
        org.yaml slugs. Pattern: .roles/{area-slug}/
        {role-slug}.md. Validated pre-write.

INV-S3  FIVE FIELDS: Every file: title, role-type, area,
        lens, expertise — all present, all substantive.

INV-S4  IA CLOSURE: One Inertia Advocate per team. Team
        is incomplete until IA SEQUENCE TABLE row is
        emitted with role-type = inertia-advocate.

INV-S5  COUNT MATCH: AUDIT TABLE total row must show
        Expected = Actual with MATCH result. No exceptions.

---

FAILURE MODES
(Read before producing any output. These patterns corrupt
the table-based verification system this skill relies on.)

FM-1  GENERIC IA IN SEQUENCE: The IA row appears in the
      SEQUENCE TABLE on time, but the file content uses
      non-domain language: "prefers stability", "resists
      new approaches". The table says PASS; the content
      fails. Correct output: IA lens and expertise are
      drawn from this team's domain vocabulary. The
      SEQUENCE TABLE row names the specific IA title.

FM-2  MISSING CROSS-REFERENCE ROW: S-4 (cross-reference
      audit) is omitted from org-chart.md, or appears as
      a prose paragraph instead of a table. Correct output:
      S-4 is a formatted table with an explicit
      Expected / Actual / Result row.

FM-3  UNDECLARED INVARIANTS: INV-S1 through INV-S5 first
      appear inside step descriptions, not in a named
      pre-step INVARIANTS section. Correct output:
      all invariants in the entry-point section,
      referenced by name downstream.

FM-4  MISSING EMITTED CHECK: No literal PASS/FAIL or
      MATCH/MISMATCH string appears anywhere in the output.
      Correct output: the AUDIT TABLE contains at least one
      MATCH or PASS literal in the Result column.

---

CHECK-OUTPUT PROTOCOL

All verification emits structured table rows.

TABLE A — SEQUENCE TABLE (emitted per team during Step 2)

| Team | Phase | Roles Written | Role Types | Status |
|------|-------|---------------|------------|--------|
| [name] | STANDARD | [n] | standard | DONE |
| [name] | SPECIALIZED | [n] | specialized | DONE |
| [name] | IA | 1 | inertia-advocate | CLOSED |

Emit per-team SEQUENCE TABLE after each team closes.
INV-S4 is satisfied only when the IA row shows CLOSED.

TABLE B — FIELD AUDIT TABLE (emitted per file on failure)

| File | Missing Field | Action |
|------|---------------|--------|
| [path] | [field] | STOP — correct before continuing |

TABLE C — FINAL AUDIT TABLE (emitted in Step 4)

| Check | Expected | Actual | Result |
|-------|----------|--------|--------|
| IA files | [n teams] | [n] | MATCH/MISMATCH |
| Total files | [n] | [n] | MATCH/MISMATCH |
| Chart total | [n] | [n] | MATCH/MISMATCH |
| Five fields | all | all | PASS/FAIL |

Skill is complete only when all Result cells show MATCH
or PASS and no TABLE B rows are unresolved.

---

STEP 1 — PARSE AND BUILD PLAN

Read org.yaml. Build three tables before writing:

PLAN TABLE (drive Steps 2 and 3 from this)

| Team | Standard | Specialized | IA | Total | Path Prefix |
|------|----------|-------------|-----|-------|-------------|

Path Prefix column: .roles/{area-slug}/ for each team.
Validate every prefix against org.yaml (INV-S2).

LEVEL TERMS TABLE

| Group | Level Terms |
|-------|-------------|

Record all level terms. Use verbatim in all role files.

Expected file count = PLAN TABLE total row. Record for
INV-S5.

---

STEP 2 — WRITE ROLE FILES (SEQUENCE ENFORCED)

Process teams in org.yaml order.
For each team, execute three phases in order (INV-S1):

PHASE A — STANDARD
  Write one file per standard role.
  Validate path against PLAN TABLE (INV-S2).
  Verify all five fields after each write (INV-S3).
  role-type: standard

PHASE B — SPECIALIZED
  Write one file per specialized role.
  Substantive distinction from standard required:
  different lens domain, different expertise scope.
  role-type: specialized

PHASE C — IA
  Write one Inertia Advocate file.
  Lens and expertise must draw from this team's domain
  vocabulary. FM-1 pattern is prohibited — name the
  specific inertia, not abstract resistance.
  role-type: inertia-advocate

After completing all three phases, emit TABLE A row
for this team. IA row must show: role = IA title (not
"Inertia Advocate" as placeholder), status = CLOSED.

---

STEP 3 — WRITE org-chart.md

Produce all four sections. No section may be omitted.

S-1: ASCII HIERARCHY
+-- and | notation. Verbatim names from org.yaml.
Nesting depth matches org.yaml structure.

S-2: HEADCOUNT TABLE (from PLAN TABLE)

| Group | Standard | Specialized | IA | Total | Levels |
|-------|----------|-------------|-----|-------|--------|

Levels column: use LEVEL TERMS TABLE values.
Total row at bottom = expected count for INV-S5.

S-3: LEVEL DISTRIBUTION TABLE

| Level Term | Role File Count | Groups |
|------------|----------------|--------|

S-4: CROSS-REFERENCE AUDIT TABLE (TABLE C rows 1 and 3)

| Check | Expected | Actual | Result |
|-------|----------|--------|--------|
| S-2 table total | [n] | [n] | MATCH/MISMATCH |
| Role files written | [n] | [n] | MATCH/MISMATCH |

---

STEP 4 — FINAL AUDIT

Consolidate all check tables. Emit TABLE C in full:

| Check | Expected | Actual | Result |
|-------|----------|--------|--------|
| IA files (one per team) | [n] | [n] | MATCH/MISMATCH |
| Total role files | [n] | [n] | MATCH/MISMATCH |
| Chart S-2 total | [n] | [n] | MATCH/MISMATCH |
| Five fields (all files) | all | all | PASS/FAIL |

Emit consolidated SEQUENCE TABLE (all teams):

| Team | Standard | Specialized | IA Title | Status |
|------|----------|-------------|----------|--------|

Any MISMATCH or FAIL: identify the specific team/file
and correct before declaring completion.

---

AMEND

AMEND-A  AREA REGENERATION: Regenerate named area.
         Rebuild PLAN TABLE for that area. Re-run Steps
         2–4 for the named area. Re-emit TABLE A (per-team
         sequence) and TABLE C rows for the regenerated area.
         INV-S2 path validation required before writes.

AMEND-B  LEVEL VOCABULARY UPDATE: Replace level term.
         Update LEVEL TERMS TABLE. Update LEVEL DISTRIBUTION
         TABLE. Emit "[n] files updated — PASS".

AMEND-C  GROUP NODE ADDITION: Add group node.
         Add rows to PLAN TABLE. Validate new path prefixes
         (INV-S2). Run all three phases for new teams.
         Emit TABLE A rows. Re-emit S-4 cross-reference
         table with updated counts.
```

---

## Variation Summary

| # | Axis | Core Bet | C-14 Architecture | C-15 Architecture |
|---|------|----------|-------------------|-------------------|
| V-01 | Role Sequence | Write-order gates reduce role-type confusion | Pre-step block lists 4 FMs in plain prose | Named CHECK-OUTPUT PROTOCOL with 5 rules |
| V-02 | Output Format | Table-first verification eliminates prose assertion | Pre-step block with FM-A through FM-D | Protocol with table-row format requirement |
| V-03 | Phrasing Register | Full imperative closes interpretive latitude | PROHIBITED-1 through PROHIBITED-4 before any step | Rules section with MUST/PROHIBITED language |
| V-04 | Inertia + Lifecycle | IA as lifecycle phase, not just role, prevents content failure | FM-1 specifically targets IA content failure | OBL-1 through OBL-5 named obligations |
| V-05 | Sequence + Format | Table rows for both sequence and verification make structure visible | FM-1 through FM-4 named, targets table corruption | TABLE A/B/C protocol with row specifications |

**What differentiates V-04 and V-05 on C-14/C-15**:
V-04 uses the FAILURE MODES block to address the *IA content failure* specifically (FM-1 is the most detailed and domain-grounded of all five variations). V-05 uses it to address *table system corruption* — the FM block explains why each failure pattern undermines the table-based verification system specifically.
