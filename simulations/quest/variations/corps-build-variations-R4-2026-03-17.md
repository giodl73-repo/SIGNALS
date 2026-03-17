File written. Here's the R4 variate summary:

---

## R4 Variations — corps-build (2026-03-17)

**Rubric v2 gap**: R3 V-05 already PASSes C-11 and C-12, but C-13 is PARTIAL — only C-09's failure mode is named ("'Technical perspective' fails"). C-10, C-11, C-12 have no named wrong-output examples. Estimated R3 V-05 score on rubric v2: **112.5/115**.

R4 axes: all three target C-13 completion.

| Variation | Axis | Hypothesis | C-13 target |
|-----------|------|------------|-------------|
| **V-01** | Inline failure modes | Wrong-output examples at instruction site | All 4 criteria, positioned at point of use |
| **V-02** | Dedicated FAILURE MODES block | All 4 failure modes front-loaded at activation | All 4 criteria, read before any step begins |
| **V-03** | CHECK-OUTPUT PROTOCOL block | Formal protocol for check strings + wrong format | C-12 + C-13/C-12 via protocol declaration |
| **V-04** | Inline FM + Check-Output Protocol | C-09 in schema, C-10 in §2, C-11 in INVARIANTS note, C-12 in protocol block | All 4 criteria across positioned sites |
| **V-05** | FAILURE MODES block + Protocol + Invariant forward-reference map | Three entry-point blocks; each invariant names its enforcing steps | All 4 criteria + strongest C-11 via forward-reference map |

**Predicted R4 scoring against rubric v2 (max 115):**
- V-01: ~113 (C-11 failure mode named inline may be awkward, risk PARTIAL)
- V-02: ~115 (all four front-loaded before steps; C-11 wrong structure explicitly named)
- V-03: ~112.5 (check-output protocol covers C-12 + C-13/C-12; C-09/C-10/C-11 failure modes depend on existing R3 schema coverage)
- V-04: ~115 (inline coverage hits all 4; check-output protocol adds redundant C-12 strength)
- V-05: ~115 (strongest structural case; invariant forward-reference map is novel; risk is pre-step declaration density)

**Key test**: whether front-loaded failure modes (V-02/V-05) are more effective than inline positioned examples (V-01/V-04). R3 showed constraint-first outperformed example-driven — V-02's dedicated FAILURE MODES block is structurally parallel to R3's breakthrough.
3 (all 4) |
| CHECK-OUTPUT PROTOCOL block | V-03, V-04, V-05 | C-12, C-13/C-12 |
| Invariant forward-reference map (each INV lists enforcing steps) | V-05 | C-11 strengthening |

---

## V-01 — Inline Failure Modes: Wrong-Output Examples at Instruction Site

**Axis**: Inline failure modes
**Hypothesis**: Adding a concrete wrong-output example immediately after each aspirational
criterion's requirement text gives the model an anti-pattern anchor at the exact point of
instruction. Unlike front-loading all failure modes at the top, inline placement means the
model encounters the wrong-output example at the moment it is about to produce that output.
This should address C-13 for all four aspirational criteria without adding a separate section.
C-09's failure mode is already named in the F-2 schema row (from R3 V-05). C-10, C-11, and
C-12 failure modes need to be added at their respective instruction sites.
Weakest axis: C-13 for C-11 (wrong invariant-block structure) is awkward to name inline in
a step; may only earn PARTIAL for C-11's failure mode.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it.

==== HARD INVARIANTS ====
These conditions must hold when this skill completes. A run that violates any invariant is
incomplete regardless of how much output was produced.

INVARIANT-1 (file completeness): Count of `.craft/roles/` files = total role slots in `org.yaml`.
INVARIANT-2 (ASCII hierarchy): `org-chart.md` contains `+--`/`|` ASCII tree; all `org.yaml`
  area names verbatim; at least two nesting levels.
INVARIANT-3 (IA per team): Every team node has `.craft/roles/{area-slug}/inertia-advocate.md`.
  One per team — not one global IA.
INVARIANT-4 (directory fidelity): `.craft/roles/` subdirectories mirror `org.yaml` area names
  one-to-one. No extras. No area from `org.yaml` absent.
INVARIANT-5 (five typed fields): Every role file has orientation, lens, expertise, scope,
  collaboration-pattern — each with substantive, non-empty, non-"TBD" body text.

Wrong invariant-block structure: restating these requirements inline only within steps,
without this named pre-step declaration block, means the constraints are not active during
write decisions — they surface only as review criteria, too late to catch mid-run gaps.

==== END INVARIANTS ====

==== ROLE FILE SCHEMA (reference contract) ====

| ID  | Field                 | Content requirement |
|-----|-----------------------|---------------------|
| F-1 | orientation           | Team-specific perspective grounded in this team's declared responsibilities. Generic job title framing fails. |
| F-2 | lens                  | The specific domain, system, or practice through which this role evaluates proposals. Must name the actual thing. "Technical perspective" fails. "Schema migration cost at >10M rows" passes. |
| F-3 | expertise             | Concrete systems built, decisions owned, or failures survived. Must name actual systems or decisions. "Deep expertise in engineering" fails. |
| F-4 | scope                 | What this role approves, blocks, recommends, or escalates, and where that authority ends. |
| F-5 | collaboration-pattern | How this role works with other roles on this team: who they lean on, who they push back on. |

Frontmatter required: `role-type` and `area` on every file.
"TBD", empty body text, or one-word answers fail INVARIANT-5 on the corresponding field.

==== END SCHEMA ====

**STEP 1 — PARSE**

Read `org.yaml`. Emit parse manifest:

```
ORG-PARSED:
  org name: [name]
  nesting: [depth, e.g., Division > Team]
  teams: [all team names with full parent path]
  standard roles per team: [names by team]
  specialized roles per team: [names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

Emit invariant targets from the parse:

```
INVARIANT TARGETS FROM PARSE:
  INV-1: [n] files required
  INV-2: [n] areas in hierarchy: [list]
  INV-3: IAs required for: [team list]
  INV-4: subdirectories required: [slug list]
  INV-5: applies to all [n] files
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

**STEP 2 — WRITE ROLE FILES**

For each team in declaration order, write all role files before moving to the next team.

**Category A — Standard roles**
Path: `.craft/roles/{area-slug}/{role-slug}.md`
Frontmatter: `role-type: standard`, `area: {area-slug}`
Populate F-1 through F-5. All fields must satisfy schema content requirements.

**Category B — Specialized roles**
Same path pattern. Frontmatter: `role-type: specialized`, `area: {area-slug}`
F-2 and F-3 must name domain-specific systems that distinguish this role from the standard
roles on the same team. It should not be possible to copy this F-2 into a standard role
file without changing it.

**Category C — Inertia Advocate** (INVARIANT-3: mandatory per team)
Path: `.craft/roles/{area-slug}/inertia-advocate.md`
Frontmatter: `role-type: inertia-advocate`, `area: {area-slug}`

F-1 must express why a senior member of this specific team would rationally resist.
F-2 must name the status-quo system or practice being protected, using this team's
  domain vocabulary. Wrong: "lens: resistance to change in general" — this fails because
  it is not drawn from this team's domain vocabulary and tells the reader nothing about
  what is actually being protected.
F-3 must identify what makes this skepticism credible in this specific domain.
F-4 and F-5 follow standard patterns.

No two Inertia Advocate files may share identical F-2 or F-3 body text. Detect duplication
before continuing to the next team and differentiate.

After all teams:
- Shared-group roles: `.craft/roles/shared/`, `role-type: shared-group`
- Exec-office roles: `.craft/roles/exec-office/`, `role-type: exec-office`
- Skip if not declared in `org.yaml`

After writing all files, confirm INVARIANT-1: count files written. If count does not match
parse manifest total, identify and resolve the gap before Step 3.

**STEP 3 — COVERAGE AUDIT**

Before writing `org-chart.md`, run this audit. Emit all results. Do not skip any check.

```
COVERAGE-AUDIT:

  [A] File count vs INVARIANT-1
      Required: [parse total]
      Written:  [count of .craft/roles/ files, excluding index/README]
      Status:   [PASS | FAIL — list missing or phantom files]

  [B] Inertia Advocate per team vs INVARIANT-3
      [team name]: [PRESENT at .craft/roles/{area}/inertia-advocate.md | MISSING]
      (one line per team)
      Status:   [PASS | FAIL]

  [C] Directory fidelity vs INVARIANT-4
      [area slug]: [EXISTS as .craft/roles/{area-slug}/ | MISSING]
      Extra directories not in org.yaml: [list or "none"]
      Status:   [PASS | FAIL]

  [D] Schema compliance vs INVARIANT-5
      Spot-check F-1..F-5 non-empty in:
        - one standard role (name it)
        - one specialized role (name it, or "none declared")
        - one inertia-advocate.md (name it)
      Status:   [PASS | FAIL — name any file with empty or TBD field]

  [E] IA domain-vocabulary uniqueness
      Verify no two IA files share identical F-2 body text.
      Verify no two IA files share identical F-3 body text.
      Status:   [PASS | FAIL — name any duplicate pair]

  AUDIT RESULT: [PASS | FAIL]
  Gaps to resolve: [list or "none"]
```

Wrong audit format: writing "all checks passed" or "audit complete" without emitting the
literal per-check [PASS | FAIL] strings and the AUDIT RESULT line fails auditable
check-output compliance — the output cannot be parsed to confirm which checks passed.

Resolve all gaps before Step 4. Do not write `org-chart.md` until AUDIT RESULT is PASS.

**STEP 4 — WRITE org-chart.md**

**Section 1 — ASCII Hierarchy** (INVARIANT-2)

Use `+--` and `|`. All names verbatim from `org.yaml`. Minimum two nesting levels.
Every area from the parse manifest must appear.

After drawing the hierarchy, emit: `INVARIANT-2 CHECK: [n] areas drawn, [n] in manifest
— [MATCH | MISMATCH]`

**Section 2 — Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | — | — | — | [n or 0] | — |
| shared | — | — | — | [n or 0] | — |
| **Total** | [n] | [n] | [n teams] | **[= audit [A] written]** | |

Level distribution: if levels declared, show breakdown by level label.

Emit INVARIANT-1 FINAL CHECK: `Table Total = [n], audit [A] written = [n] — [MATCH | MISMATCH]`

Wrong cross-reference format: writing "table total matches file count" or "16 files, correct"
without the literal `Table Total = [n], files written = [n] — [MATCH | MISMATCH]` string
fails the auditable cross-reference check — no human or automated tool can parse the result.

**Section 3 — Coverage Notes**

One line per area: role categories generated; any absent by declaration.

**STEP 5 — AMEND**

```
AMEND:
1. Regenerate area: [name one area from org.yaml] — re-run Step 2 (categories A-C) for
   that area; re-run audit checks [A]-[E] scoped to that area; re-verify INVARIANT-1,
   INVARIANT-3, INVARIANT-4, INVARIANT-5; update headcount table.
2. Adjust level vocabulary: replace "[current level term from org.yaml]" with a new label
   across all role files and the headcount table.
3. Change group structure: move [team name] from [current parent] to [new parent group];
   update hierarchy, role file paths, INVARIANT-4 subdirectory map, and headcount table.
```

---

## V-02 — Dedicated Failure Modes Block at Entry Point

**Axis**: Dedicated FAILURE MODES block at entry point
**Hypothesis**: Placing all four aspirational failure modes in a dedicated named block
immediately after INVARIANTS — before any procedural steps — front-loads the anti-pattern
anchors at activation time. The model reads all four wrong-output examples before doing any
work, so each write decision is made with the failure modes already in context. This is
structurally parallel to the INVARIANTS block: both are declarative, entry-point, named.
The question is whether front-loading failure modes is more effective than inline placement
(V-01) because the model holds all four failure modes as active constraints during every
decision, or less effective because they are encountered too early and fade from context
by the time the relevant output is produced. Expected to be strongest on C-13 and C-11
(the invariant block's named failure mode is the most structurally awkward to place inline).

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it.

==== HARD INVARIANTS ====
These conditions must hold when this skill completes. A run that violates any invariant is
incomplete regardless of how much output was produced.

INVARIANT-1 (file completeness): Count of `.craft/roles/` files = total role slots in `org.yaml`.
INVARIANT-2 (ASCII hierarchy): `org-chart.md` contains `+--`/`|` ASCII tree; all area names
  verbatim; at least two nesting levels.
INVARIANT-3 (IA per team): Every team node has `.craft/roles/{area-slug}/inertia-advocate.md`.
INVARIANT-4 (directory fidelity): `.craft/roles/` subdirectories mirror `org.yaml` area names
  one-to-one. No extras. No omissions.
INVARIANT-5 (five typed fields): Every role file has orientation, lens, expertise, scope,
  collaboration-pattern — each with substantive, non-empty, non-"TBD" body text.

==== END INVARIANTS ====

==== FAILURE MODES ====
Each of the following names a concrete output that fails a compliance criterion.
Avoid producing these outputs.

FM-09 (Inertia Advocate domain specificity):
  WRONG: `## lens\nResistance to change in general.`
  WRONG: `## expertise\nHas extensive experience with change management.`
  RIGHT: lens and expertise name this team's specific system, practice, or operational
  constraint — not generic change-resistance. "Ingestion SLA reliability under schema change
  pressure" passes. "Resistance to change in general" fails.

FM-10 (Cross-reference integrity):
  WRONG: "Table total matches the number of files written." (no literals, no format)
  WRONG: "16 files — correct." (no comparison string)
  RIGHT: `Table Total = 16, audit [A] written = 16 — MATCH`
  The check string must emit literal numbers and the [MATCH | MISMATCH] token. Any prose
  paraphrase of the same conclusion fails because it cannot be parsed as a verification result.

FM-11 (Named invariant block at entry point):
  WRONG: Constraints stated inline only within steps:
    "For each team, remember to write an Inertia Advocate."
    "Make sure all five fields are present."
  These fail because the model has not committed to the constraint before beginning Step 1.
  RIGHT: Named INVARIANT-N block declared before any steps; each step references the
  invariant by ID ("INVARIANT-3 enforcement: do not close a team's file set without the IA").

FM-12 (Auditable check-output):
  WRONG: "All audit checks passed."
  WRONG: "The coverage audit is complete; no gaps found."
  RIGHT: `AUDIT RESULT: PASS` or `AUDIT RESULT: FAIL — [list gaps]`
  Every check point must emit a parseable literal string. Prose summary of the same
  conclusion is not auditable — no tooling can distinguish pass from fail.

==== END FAILURE MODES ====

==== ROLE FILE SCHEMA (reference contract) ====

| ID  | Field                 | Content requirement |
|-----|-----------------------|---------------------|
| F-1 | orientation           | Team-specific perspective grounded in this team's declared responsibilities. Generic job title framing fails. |
| F-2 | lens                  | Named system, practice, or constraint. "Technical perspective" fails. "Schema migration cost at >10M rows" passes. |
| F-3 | expertise             | Concrete systems, decisions, or incidents. "Deep expertise in engineering" fails. |
| F-4 | scope                 | Approval, block, recommendation, or escalation reach within this team. |
| F-5 | collaboration-pattern | Named interactions with other roles on this team. |

Frontmatter required: `role-type` and `area` on every file.

==== END SCHEMA ====

**STEP 1 — PARSE**

Read `org.yaml`. Emit parse manifest:

```
ORG-PARSED:
  org name: [name]
  nesting: [depth]
  teams: [all team names with full parent path]
  standard roles per team: [names by team]
  specialized roles per team: [names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

Emit invariant targets from parse:

```
INVARIANT TARGETS FROM PARSE:
  INV-1: [n] files required
  INV-2: [n] areas in hierarchy: [list]
  INV-3: IAs required for: [team list]
  INV-4: subdirectories required: [slug list]
  INV-5: applies to all [n] files
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

**STEP 2 — WRITE ROLE FILES**

For each team in declaration order, write all role files before moving to the next team.

**Category A — Standard roles**
Path: `.craft/roles/{area-slug}/{role-slug}.md`. Frontmatter: `role-type: standard`, `area: {area-slug}`.
All five fields F-1..F-5 with substantive body text (see schema).

**Category B — Specialized roles**
Same path. Frontmatter: `role-type: specialized`. F-2 and F-3 must be unduplicated from
standard roles: it should not be possible to copy this file's F-2 into a standard role
without changing it.

**Category C — Inertia Advocate** (INVARIANT-3: mandatory per team)
Path: `.craft/roles/{area-slug}/inertia-advocate.md`.
Frontmatter: `role-type: inertia-advocate`.

F-1 through F-5 required. Apply FM-09: F-2 and F-3 must use this team's domain vocabulary.
No two IA files may share identical F-2 or F-3 body text. Differentiate before proceeding.

INVARIANT-3 enforcement: do not close a team's file set without the IA file written.
INVARIANT-4 enforcement: write only to subdirectories in the parse manifest.

After all teams: shared-group to `.craft/roles/shared/`, exec-office to `.craft/roles/exec-office/`.
Skip if not in `org.yaml`.

Confirm INVARIANT-1 after all writes: count files. If gap, resolve before Step 3.

**STEP 3 — COVERAGE AUDIT**

Run before writing `org-chart.md`. Emit all results.

```
COVERAGE-AUDIT:

  [A] File count vs INVARIANT-1
      Required: [parse total]
      Written:  [count]
      Status:   [PASS | FAIL — list gaps]

  [B] IA per team vs INVARIANT-3
      [team]: [PRESENT | MISSING]
      Status:   [PASS | FAIL]

  [C] Directory fidelity vs INVARIANT-4
      [area slug]: [EXISTS | MISSING]
      Extras not in org.yaml: [list or "none"]
      Status:   [PASS | FAIL]

  [D] Schema spot-check vs INVARIANT-5
      Standard: [name] — [PASS | FAIL]
      Specialized: [name or "none"] — [PASS | FAIL]
      IA: [name] — [PASS | FAIL]
      Status:   [PASS | FAIL]

  [E] IA uniqueness
      F-2 duplicates: [pair names or "none"]
      F-3 duplicates: [pair names or "none"]
      Status:   [PASS | FAIL]

  AUDIT RESULT: [PASS | FAIL]
  Gaps: [list or "none"]
```

Apply FM-12: emit the literal `AUDIT RESULT: [PASS | FAIL]` string — "audit passed" is not
a valid output. Resolve all gaps before Step 4.

**STEP 4 — WRITE org-chart.md**

**Section 1 — ASCII Hierarchy** (INVARIANT-2)

`+--` and `|`, verbatim names, two or more nesting levels. After drawing:
`INVARIANT-2 CHECK: [n] areas drawn, [n] in manifest — [MATCH | MISMATCH]`

**Section 2 — Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | — | — | — | [n or 0] | — |
| shared | — | — | — | [n or 0] | — |
| **Total** | [n] | [n] | [n teams] | **[= audit [A] written]** | |

Apply FM-10: emit `Table Total = [n], audit [A] written = [n] — [MATCH | MISMATCH]`

**Section 3 — Coverage Notes**

One line per area.

**STEP 5 — AMEND**

```
AMEND:
1. Regenerate area: [area name] — re-run Step 2 (A-C); re-run audit [A]-[E] for that area;
   re-verify INVARIANT-1, INVARIANT-3, INVARIANT-4, INVARIANT-5; update table.
2. Adjust level vocabulary: replace "[level term]" across all files and table.
3. Change group structure: move [team] to [new parent]; update hierarchy, paths,
   INVARIANT-4 subdirectory map, table.
```

---

## V-03 — Check-Output Protocol Block

**Axis**: Formal CHECK-OUTPUT PROTOCOL block
**Hypothesis**: Naming the verification string requirement as a dedicated, named block —
declaring exactly which check strings are required, at which step, in which format, and
what wrong format looks like — makes C-12 maximally explicit AND provides the C-13 failure
mode for C-12 as a first-class entry-point declaration. Unlike inline placement (V-01) or
the general FAILURE MODES block (V-02), this block is scoped specifically to the audit
and verification output contract. The model reads it as a commitment: these are the literal
strings I will produce at these points. This should be strongest on C-12 (the explicit
protocol declaration is the paradigm case of auditable check-output) and on C-13/C-12
(the block names the wrong format). Potential risk: this block adds no new material for
C-09/C-10/C-11 failure modes, so C-13 may still be PARTIAL for the other three criteria
unless the schema and invariant blocks already cover them.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it.

==== HARD INVARIANTS ====

INVARIANT-1 (file completeness): Count of `.craft/roles/` files = total role slots in `org.yaml`.
INVARIANT-2 (ASCII hierarchy): `org-chart.md` ASCII tree uses `+--`/`|`; all area names verbatim;
  two or more nesting levels.
INVARIANT-3 (IA per team): One `inertia-advocate.md` per team node — not one global IA.
INVARIANT-4 (directory fidelity): `.craft/roles/` subdirectory names match `org.yaml` area
  slugs one-to-one.
INVARIANT-5 (five typed fields): Every role file has all five schema fields non-empty and
  substantive. An IA whose F-2 reads "resistance to change in general" violates INVARIANT-5
  — the field is not substantive in this team's context.

==== END INVARIANTS ====

==== CHECK-OUTPUT PROTOCOL ====
This skill requires literal verification strings at specific output points.
These strings are not optional prose confirmations — they are parseable check records.

Required check strings, in order:

  STEP 3 — After each per-check block in COVERAGE-AUDIT:
    Format: `Status: [PASS | FAIL]` (one per check [A]-[E])
    Final:  `AUDIT RESULT: [PASS | FAIL]`

  STEP 4 — After drawing the ASCII hierarchy (Section 1):
    Format: `INVARIANT-2 CHECK: [n] areas drawn, [n] in manifest — [MATCH | MISMATCH]`

  STEP 4 — After writing the headcount table (Section 2):
    Format: `Table Total = [n], audit [A] written = [n] — [MATCH | MISMATCH]`

Wrong format — these all fail the check-output protocol:
  - "All audit checks passed."
  - "The counts are correct."
  - "17 files, which matches the table total."
  - "Hierarchy verified."
The literal token [PASS | FAIL] or [MATCH | MISMATCH] must appear in the output string.
Prose summary of the same conclusion is not equivalent.

==== END CHECK-OUTPUT PROTOCOL ====

==== ROLE FILE SCHEMA (reference contract) ====

| ID  | Field                 | Content requirement |
|-----|-----------------------|---------------------|
| F-1 | orientation           | Team-specific perspective. Generic job title framing fails. |
| F-2 | lens                  | Named system or practice. "Technical perspective" fails. "Schema migration cost at >10M rows" passes. |
| F-3 | expertise             | Named systems, decisions, or incidents. "Deep expertise" fails. |
| F-4 | scope                 | Approval, block, escalation reach. |
| F-5 | collaboration-pattern | Named interactions with other roles on this team. |

Frontmatter required: `role-type` and `area` on every file.

==== END SCHEMA ====

**STEP 1 — PARSE**

Read `org.yaml`. Emit parse manifest:

```
ORG-PARSED:
  org name: [name]
  nesting: [depth]
  teams: [all team names with full parent path]
  standard roles per team: [names by team]
  specialized roles per team: [names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

Emit invariant targets:

```
INVARIANT TARGETS FROM PARSE:
  INV-1: [n] files required
  INV-2: [n] areas in hierarchy: [list]
  INV-3: IAs required for: [team list]
  INV-4: subdirectories required: [slug list]
  INV-5: applies to all [n] files
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

**STEP 2 — WRITE ROLE FILES**

For each team in declaration order, write all role files before moving to the next team.

**Category A — Standard roles**
`.craft/roles/{area-slug}/{role-slug}.md`. Frontmatter: `role-type: standard`, `area: {area-slug}`.
All F-1..F-5 with substantive body text.

**Category B — Specialized roles**
Same path. Frontmatter: `role-type: specialized`. F-2 and F-3 must be distinguishable from
standard roles on the same team — unduplicated domain vocabulary required.

**Category C — Inertia Advocate** (INVARIANT-3 mandatory)
`.craft/roles/{area-slug}/inertia-advocate.md`. Frontmatter: `role-type: inertia-advocate`.
F-2 and F-3 must use this team's specific domain vocabulary — generic resistance language
violates INVARIANT-5. No two IA files may share identical F-2 or F-3 body text.
INVARIANT-3 enforcement: do not close a team before writing the IA file.
INVARIANT-4 enforcement: write only to subdirectories in the parse manifest.

After all teams: shared-group to `.craft/roles/shared/`, exec-office to `.craft/roles/exec-office/`.
Skip if not in `org.yaml`. Count files. Resolve INVARIANT-1 gaps before Step 3.

**STEP 3 — COVERAGE AUDIT**

Apply CHECK-OUTPUT PROTOCOL. Emit all results using required check strings.

```
COVERAGE-AUDIT:

  [A] File count vs INVARIANT-1
      Required: [parse total]
      Written:  [count]
      Status:   [PASS | FAIL — list gaps]

  [B] IA per team vs INVARIANT-3
      [team]: [PRESENT | MISSING]
      Status:   [PASS | FAIL]

  [C] Directory fidelity vs INVARIANT-4
      [area]: [EXISTS | MISSING]
      Extras: [list or "none"]
      Status:   [PASS | FAIL]

  [D] Schema spot-check vs INVARIANT-5
      Standard: [name] — [PASS | FAIL]
      Specialized: [name or "none"] — [PASS | FAIL]
      IA: [name] — [PASS | FAIL]
      Status:   [PASS | FAIL]

  [E] IA uniqueness
      F-2 duplicates: [pairs or "none"]
      F-3 duplicates: [pairs or "none"]
      Status:   [PASS | FAIL]

  AUDIT RESULT: [PASS | FAIL]
  Gaps: [list or "none"]
```

Do not write `org-chart.md` until AUDIT RESULT is PASS.

**STEP 4 — WRITE org-chart.md**

**Section 1 — ASCII Hierarchy** (INVARIANT-2)
`+--` and `|`. All names verbatim. Two or more nesting levels. Every area present.
After drawing: `INVARIANT-2 CHECK: [n] areas drawn, [n] in manifest — [MATCH | MISMATCH]`

**Section 2 — Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | — | — | — | [n or 0] | — |
| shared | — | — | — | [n or 0] | — |
| **Total** | [n] | [n] | [n teams] | **[= audit [A] written]** | |

`Table Total = [n], audit [A] written = [n] — [MATCH | MISMATCH]`

**Section 3 — Coverage Notes**
One line per area.

**STEP 5 — AMEND**

```
AMEND:
1. Regenerate area: [area] — re-run Step 2 (A-C); re-run audit [A]-[E] for that area;
   re-verify INVARIANT-1, INVARIANT-3, INVARIANT-4, INVARIANT-5; update table.
2. Adjust level vocabulary: replace "[level term]" across all files and table.
3. Change group structure: move [team] to [new parent]; update hierarchy, paths,
   INVARIANT-4 subdirectory map, table.
```

---

## V-04 — Combination: Inline Failure Modes + Check-Output Protocol Block

**Axis**: Inline failure modes (V-01) + CHECK-OUTPUT PROTOCOL block (V-03)
**Hypothesis**: V-01 places wrong-output examples at instruction sites; V-03 declares a
formal check-output protocol at entry. Combined, they cover all four C-13 failure modes
(C-09 inline in schema, C-10 inline in Section 2, C-11 inline in INVARIANTS block, C-12
via the CHECK-OUTPUT PROTOCOL block) plus the C-12 auditable requirement. The INVARIANTS
block provides the C-11 named wrong structure (invariants inline only, without named block).
The CHECK-OUTPUT PROTOCOL block provides the C-12 named wrong format. The schema provides
the C-09 failure mode. Section 2 provides the C-10 wrong format. Together: C-13 should
reach PASS for all four criteria.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it.

==== HARD INVARIANTS ====
These conditions must hold when this skill completes. Violating any invariant renders the
run incomplete regardless of output volume.

INVARIANT-1 (file completeness): Count of `.craft/roles/` files = total role slots in `org.yaml`.
INVARIANT-2 (ASCII hierarchy): `org-chart.md` ASCII tree uses `+--`/`|`; all area names verbatim;
  two or more nesting levels.
INVARIANT-3 (IA per team): Every team node has `.craft/roles/{area-slug}/inertia-advocate.md`.
INVARIANT-4 (directory fidelity): `.craft/roles/` subdirectories mirror `org.yaml` area names
  one-to-one.
INVARIANT-5 (five typed fields): Every role file has orientation, lens, expertise, scope,
  collaboration-pattern — substantive, non-empty, non-"TBD".

Wrong invariant structure: stating these requirements inline within steps only — "remember
to write an IA for each team" — without this named entry-point block fails because the
constraints are not active from the start; they surface only when the relevant step is
reached, too late to catch accumulating gaps.

==== END INVARIANTS ====

==== CHECK-OUTPUT PROTOCOL ====
This skill requires literal verification strings at three output points. Prose equivalents
are not acceptable — the output must be parseable.

Required strings:
  STEP 3: `Status: [PASS | FAIL]` per check [A]-[E]; then `AUDIT RESULT: [PASS | FAIL]`
  STEP 4 §1: `INVARIANT-2 CHECK: [n] areas drawn, [n] in manifest — [MATCH | MISMATCH]`
  STEP 4 §2: `Table Total = [n], audit [A] written = [n] — [MATCH | MISMATCH]`

Wrong format — all of these fail:
  "All checks passed." / "Audit complete, no gaps." / "Table total is correct." /
  "17 files, matches." — none of these emit a parseable [PASS | FAIL] or [MATCH | MISMATCH]
  token.

==== END CHECK-OUTPUT PROTOCOL ====

==== ROLE FILE SCHEMA (reference contract) ====

| ID  | Field                 | Content requirement |
|-----|-----------------------|---------------------|
| F-1 | orientation           | Team-specific perspective. Generic job title framing fails. |
| F-2 | lens                  | Named system or practice. "Technical perspective" fails. "Schema migration cost at >10M rows" passes. |
| F-3 | expertise             | Named systems, decisions, incidents. "Deep expertise in engineering" fails. |
| F-4 | scope                 | Approval, block, escalation reach within this team. |
| F-5 | collaboration-pattern | Named interactions with other roles on this team. |

Frontmatter required: `role-type` and `area` on every file.

==== END SCHEMA ====

**STEP 1 — PARSE**

Read `org.yaml`. Emit parse manifest:

```
ORG-PARSED:
  org name: [name]
  nesting: [depth]
  teams: [all team names with full parent path]
  standard roles per team: [names by team]
  specialized roles per team: [names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

Emit invariant targets:

```
INVARIANT TARGETS FROM PARSE:
  INV-1: [n] files required
  INV-2: [n] areas in hierarchy: [list]
  INV-3: IAs required for: [team list]
  INV-4: subdirectories required: [slug list]
  INV-5: applies to all [n] files
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

**STEP 2 — WRITE ROLE FILES**

For each team in declaration order, write all role files before moving to the next team.

**Category A — Standard roles**
`.craft/roles/{area-slug}/{role-slug}.md`. `role-type: standard`, `area: {area-slug}`.
All F-1..F-5 with substantive body text.

**Category B — Specialized roles**
Same path. `role-type: specialized`. F-2 and F-3 must be domain-distinct from standard
roles on the same team.

**Category C — Inertia Advocate** (INVARIANT-3: mandatory per team)
`.craft/roles/{area-slug}/inertia-advocate.md`. `role-type: inertia-advocate`.

F-2 must name this team's specific status-quo system or practice. Wrong: "lens: resistance
to change in general" — this fails because it names no concrete system and is
interchangeable across any team. Right: the lens names the actual thing being protected
in this domain.

F-3 must establish credibility in this specific domain, not generic change management.
No two IA files may share identical F-2 or F-3 body text. Differentiate before proceeding.

INVARIANT-3 enforcement: do not close a team before writing the IA file.
INVARIANT-4 enforcement: write only to subdirectories in the parse manifest.

After all teams: shared-group to `.craft/roles/shared/`, exec-office to `.craft/roles/exec-office/`.
Confirm INVARIANT-1 count after all writes. Resolve gaps before Step 3.

**STEP 3 — COVERAGE AUDIT**

Apply CHECK-OUTPUT PROTOCOL throughout. Emit all results with required check strings.

```
COVERAGE-AUDIT:

  [A] File count vs INVARIANT-1
      Required: [parse total]
      Written:  [count]
      Status:   [PASS | FAIL — list gaps]

  [B] IA per team vs INVARIANT-3
      [team]: [PRESENT | MISSING]
      Status:   [PASS | FAIL]

  [C] Directory fidelity vs INVARIANT-4
      [area]: [EXISTS | MISSING]
      Extras: [list or "none"]
      Status:   [PASS | FAIL]

  [D] Schema spot-check vs INVARIANT-5
      Standard: [name] — [PASS | FAIL]
      Specialized: [name or "none"] — [PASS | FAIL]
      IA: [name] — [PASS | FAIL]
      Status:   [PASS | FAIL]

  [E] IA uniqueness
      F-2 duplicates: [pairs or "none"]
      F-3 duplicates: [pairs or "none"]
      Status:   [PASS | FAIL]

  AUDIT RESULT: [PASS | FAIL]
  Gaps: [list or "none"]
```

Do not write `org-chart.md` until AUDIT RESULT is PASS.

**STEP 4 — WRITE org-chart.md**

**Section 1 — ASCII Hierarchy** (INVARIANT-2)
`+--` and `|`. All names verbatim. Two or more nesting levels.
After drawing: `INVARIANT-2 CHECK: [n] areas drawn, [n] in manifest — [MATCH | MISMATCH]`

**Section 2 — Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | — | — | — | [n or 0] | — |
| shared | — | — | — | [n or 0] | — |
| **Total** | [n] | [n] | [n teams] | **[= audit [A] written]** | |

Emit cross-reference check: `Table Total = [n], audit [A] written = [n] — [MATCH | MISMATCH]`
Wrong format: "table total of 16 is correct" — this contains no parseable comparison token
and cannot be verified by inspection.

**Section 3 — Coverage Notes**
One line per area.

**STEP 5 — AMEND**

```
AMEND:
1. Regenerate area: [area] — re-run Step 2 (A-C); re-run audit [A]-[E] scoped to area;
   re-verify INVARIANT-1, INVARIANT-3, INVARIANT-4, INVARIANT-5; update table.
2. Adjust level vocabulary: replace "[level term]" across all files and table.
3. Change group structure: move [team] to [new parent]; update hierarchy, paths,
   INVARIANT-4 subdirectory map, table.
```

---

## V-05 — Full Max-Score: FAILURE MODES Block + Check-Output Protocol + Invariant Forward-Reference Map

**Axis**: Dedicated FAILURE MODES block (V-02) + CHECK-OUTPUT PROTOCOL block (V-03) +
invariant forward-reference map (each invariant lists the steps that enforce it)
**Hypothesis**: Three compounding additions on top of R3 V-05's architecture. The
FAILURE MODES block covers all four C-13 aspirational failure modes as a front-loaded
entry-point declaration. The CHECK-OUTPUT PROTOCOL block formalizes C-12 compliance. The
invariant forward-reference map extends C-11 compliance by making each invariant's
enforcement points explicit in the invariant declaration itself — so the model knows, when
reading INVARIANT-3, that it will be enforced at "Step 2 team close gate, AMEND option 1."
This should produce the strongest C-11 and C-13 scores. Risk: three entry-point blocks
(INVARIANTS, FAILURE MODES, CHECK-OUTPUT PROTOCOL) before any procedural steps is the
longest pre-step declaration of any variation; test whether compounding entry-point
declarations reinforce or dilute each other.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it.

==== HARD INVARIANTS ====
These conditions must hold when this skill completes. Violation of any invariant renders
the run incomplete regardless of output volume.

INVARIANT-1 (file completeness): Count of `.craft/roles/` files = total role slots in `org.yaml`.
  Enforced at: Step 2 post-write count check; Step 4 Section 2 FINAL CHECK.
INVARIANT-2 (ASCII hierarchy): `org-chart.md` ASCII tree uses `+--`/`|`; all area names verbatim;
  two or more nesting levels.
  Enforced at: Step 4 Section 1 hierarchy draw + INVARIANT-2 CHECK string.
INVARIANT-3 (IA per team): Every team node has `.craft/roles/{area-slug}/inertia-advocate.md`.
  Enforced at: Step 2 team close gate (Category C); Step 3 audit check [B].
INVARIANT-4 (directory fidelity): `.craft/roles/` subdirectories mirror `org.yaml` area names
  one-to-one. No extras. No omissions.
  Enforced at: Step 2 pre-write path validation; Step 3 audit check [C].
INVARIANT-5 (five typed fields): Every role file has orientation, lens, expertise, scope,
  collaboration-pattern — substantive, non-empty, non-"TBD".
  Enforced at: Step 2 per-file write; Step 3 audit check [D]; IA domain check in Category C.

==== END INVARIANTS ====

==== FAILURE MODES ====
Concrete examples of wrong output for each aspirational criterion.

FM-09 — Inertia Advocate domain specificity:
  WRONG: `## lens\nResistance to change in general.`
  WRONG: `## expertise\nExperienced with organizational change.`
  These fail because they name no concrete system specific to this team. The IA's
  F-2 and F-3 must use vocabulary drawn from the team's declared domain — not generic
  change-resistance language that could apply to any team in any org.

FM-10 — Cross-reference integrity check format:
  WRONG: "Table total matches files written."
  WRONG: "16 files — looks right."
  WRONG: "INVARIANT-1 satisfied." (no numbers)
  RIGHT: `Table Total = 16, audit [A] written = 16 — MATCH`
  The check string must emit literal count values and a [MATCH | MISMATCH] token.
  Any output that conveys the same conclusion in prose fails because it is not parseable.

FM-11 — Named invariant block at entry point:
  WRONG: Requirements only as inline step reminders:
    "Remember to include an IA for each team." (in Step 2)
    "Make sure all five fields are present." (in Step 2)
    "Check that directories match org.yaml." (in Step 2)
  These fail because the model has not committed to any of these constraints before
  beginning Step 1. An invariant that the model first encounters mid-step is not an
  invariant — it is a reminder, discovered too late to gate earlier decisions.

FM-12 — Auditable check-output format:
  WRONG: "All audit checks passed."
  WRONG: "Coverage audit complete; everything looks good."
  WRONG: "No gaps found." (no literal token)
  RIGHT: `AUDIT RESULT: PASS` or `AUDIT RESULT: FAIL — [gap list]`
  Every verification output point must emit the literal protocol token. Any prose
  confirmation — no matter how accurate — fails because it does not satisfy the
  parseable check-output contract.

==== END FAILURE MODES ====

==== CHECK-OUTPUT PROTOCOL ====
Three required check strings, in order. The literal token [PASS | FAIL] or [MATCH | MISMATCH]
must appear in each output string. Prose equivalents are not acceptable.

  STEP 3: `Status: [PASS | FAIL]` per check [A]-[E]; `AUDIT RESULT: [PASS | FAIL]`
  STEP 4 §1: `INVARIANT-2 CHECK: [n] areas drawn, [n] in manifest — [MATCH | MISMATCH]`
  STEP 4 §2: `Table Total = [n], audit [A] written = [n] — [MATCH | MISMATCH]`

==== END CHECK-OUTPUT PROTOCOL ====

==== ROLE FILE SCHEMA (reference contract) ====

| ID  | Field                 | Content requirement |
|-----|-----------------------|---------------------|
| F-1 | orientation           | Team-specific perspective. Generic job title framing fails. |
| F-2 | lens                  | Named system or practice. "Technical perspective" fails. "Schema migration cost at >10M rows" passes. |
| F-3 | expertise             | Named systems, decisions, incidents. "Deep expertise in engineering" fails. |
| F-4 | scope                 | Approval, block, escalation reach. |
| F-5 | collaboration-pattern | Named interactions with other roles on this team. |

Frontmatter required: `role-type` and `area` on every file.

==== END SCHEMA ====

**STEP 1 — PARSE**

Read `org.yaml`. Emit parse manifest:

```
ORG-PARSED:
  org name: [name]
  nesting: [depth]
  teams: [all team names with full parent path]
  standard roles per team: [names by team]
  specialized roles per team: [names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

Emit invariant targets:

```
INVARIANT TARGETS FROM PARSE:
  INV-1: [n] files required
  INV-2: [n] areas in hierarchy: [list]
  INV-3: IAs required for: [team list]
  INV-4: subdirectories required: [slug list]
  INV-5: applies to all [n] files
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

**STEP 2 — WRITE ROLE FILES**

For each team in declaration order, write all role files before moving to the next team.

**Category A — Standard roles**
`.craft/roles/{area-slug}/{role-slug}.md`. `role-type: standard`, `area: {area-slug}`.
All F-1..F-5. INVARIANT-4 enforcement: path derived from parse manifest only.

**Category B — Specialized roles**
Same path. `role-type: specialized`. F-2 and F-3 unduplicated from standard roles on
this team — domain vocabulary must distinguish the specialized role.

**Category C — Inertia Advocate** (INVARIANT-3: mandatory per team)
`.craft/roles/{area-slug}/inertia-advocate.md`. `role-type: inertia-advocate`.

F-1 through F-5 required.
INVARIANT-5 + FM-09 enforcement: F-2 and F-3 must use this team's domain vocabulary.
IA uniqueness gate: no two IA files may share identical F-2 or F-3 body text. Detect
duplication and differentiate before closing this team.
INVARIANT-3 enforcement: do not close a team without the IA file written.

After all teams: shared-group to `.craft/roles/shared/`, exec-office to `.craft/roles/exec-office/`.
Skip if not in `org.yaml`.

INVARIANT-1 check: count files after all writes. Resolve gap before Step 3.

**STEP 3 — COVERAGE AUDIT**

Apply CHECK-OUTPUT PROTOCOL. Emit all check strings as specified.

```
COVERAGE-AUDIT:

  [A] File count vs INVARIANT-1
      Required: [parse total]
      Written:  [count]
      Status:   [PASS | FAIL — list gaps]

  [B] IA per team vs INVARIANT-3
      [team]: [PRESENT at .craft/roles/{area}/inertia-advocate.md | MISSING]
      Status:   [PASS | FAIL]

  [C] Directory fidelity vs INVARIANT-4
      [area slug]: [EXISTS | MISSING]
      Extras not in org.yaml: [list or "none"]
      Status:   [PASS | FAIL]

  [D] Schema spot-check vs INVARIANT-5
      Standard: [name] — [PASS | FAIL]
      Specialized: [name or "none"] — [PASS | FAIL]
      IA: [name] — [PASS | FAIL]
      Status:   [PASS | FAIL]

  [E] IA domain-vocabulary uniqueness (FM-09)
      F-2 duplicates: [pair names or "none"]
      F-3 duplicates: [pair names or "none"]
      Status:   [PASS | FAIL]

  AUDIT RESULT: [PASS | FAIL]
  Gaps: [list or "none"]
```

Resolve all gaps before Step 4. Do not write `org-chart.md` until AUDIT RESULT is PASS.

**STEP 4 — WRITE org-chart.md**

**Section 1 — ASCII Hierarchy** (INVARIANT-2)
`+--` and `|`. All names verbatim. Two or more nesting levels. Every area present.
After drawing: `INVARIANT-2 CHECK: [n] areas drawn, [n] in manifest — [MATCH | MISMATCH]`

**Section 2 — Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | — | — | — | [n or 0] | — |
| shared | — | — | — | [n or 0] | — |
| **Total** | [n] | [n] | [n teams] | **[= audit [A] written]** | |

Level distribution: if levels declared, show breakdown by level label.

`Table Total = [n], audit [A] written = [n] — [MATCH | MISMATCH]`

**Section 3 — Coverage Notes**
One line per area: categories generated; any absent by declaration.

**STEP 5 — AMEND**

```
AMEND:
1. Regenerate area: [area] — re-run Step 2 (A-C); re-run audit [A]-[E] scoped to area;
   re-verify INVARIANT-1 (enforcement point: Step 4 §2), INVARIANT-3 (Step 2 close gate),
   INVARIANT-4 (pre-write path), INVARIANT-5 (per-file); update headcount table.
2. Adjust level vocabulary: replace "[level term]" across all files and table.
3. Change group structure: move [team] to [new parent]; update hierarchy, role file paths,
   INVARIANT-4 subdirectory map (enforcement point: Step 3 check [C]), headcount table.
```
