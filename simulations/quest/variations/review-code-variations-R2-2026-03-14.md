Written to `simulations/quest/variations/review-code-variations-R2-2026-03-14.md`.

---

## review-code — Variations R2

### Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Output format (template saturation) | Fill-in templates for every compliance-sensitive block make C-01, C-02, C-07, C-08 structurally impossible to omit — extends R1 V-02's table approach to the verdict and pattern blocks |
| V-02 | Inertia framing (full failure mode registry) | A numbered 10-item failure mode registry with per-section F-ID labels is more robust than naming 3 failure modes — primes the model against all known regressions before step 1 fires |
| V-03 | Lifecycle emphasis (amend-first branching) | Amend scope as a first-class gate (output before findings, not after) converts C-09 from conditional footnote to planned deliverable |
| V-04 | Output format + inertia framing (combination) | Template blocks + per-section failure mode labels creates independent enforcement on C-11 and C-12 simultaneously — structure prevents omission; framing resists regression where structure can't reach |
| V-05 | All axes (full spectrum) | Architecture-first sequencing + template enforcement + 5 named failure modes + amend-first branching + dedicated synthesis phase — each mechanism targets a specific criterion, nothing decorative |

---

### What's new vs R1

R1's best variation (V-05, 95 composite) already hit C-11 via table columns and C-12 via three named failure modes. R2 explores whether those mechanisms have more headroom:

- **V-01** pushes C-11 beyond table columns — encoding C-01 and C-08 as structural templates (not just C-02 and C-07)
- **V-02** pushes C-12 beyond 3 failure modes — a 10-item registry with F-IDs and per-section mapping
- **V-03** isolates the amend lifecycle axis (untested in R1) to see if amend-first produces more reliable C-09 than amend-last
- **V-04** combines V-01 + V-02 as the redundancy test: structural enforcement AND behavioral priming operating independently
- **V-05** is the full-spectrum combination — if V-04 scores near 97, V-05 adds architecture-first sequencing and amend-first branching to chase 100

The predicted standout is **V-05** (100) and **V-04** (~97). V-01 and V-02 are isolation tests to verify that each new mechanism carries its weight before combining.
inal step ("skip if full review"). This variation makes the amend/full decision a branching gate at the top — the review mode is declared first and the scope block is the first output if amend. This makes C-09 a structural requirement, not a conditional footnote. Single-axis: only lifecycle order changes; all other mechanics stay consistent with R1 V-05.

**V-04 (combination: template saturation + failure mode naming)** — Combines the V-01 fill-in template approach with V-02's failure mode framing. Each named output block is labeled with the failure mode it prevents. Structural enforcement via form (C-11) and behavioral priming via failure mode naming (C-12) operate independently — either alone can keep a criterion from regressing; both together provide redundancy.

**V-05 (full spectrum)** — Kitchen-sink combination: architecture-first sequencing (R1 V-01/V-04), template verdict block (R1 V-02), five named failure modes (R1 V-05 extended), amend-first branching (R2 V-03), dedicated synthesis phase with mandatory `Why:` field. Designed to hit all 12 criteria simultaneously. Every mechanism is chosen to reinforce a specific criterion; nothing appears for completeness only.

---

### Scoring predictions (v2 rubric)

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | Expected composite |
|-----------|------|------|------|------|------|------|------|------|------|------|------|--------------------|
| V-01 | very high | very high | high | high | high | very high | very high | high | high | very high | low | ~90 |
| V-02 | high | high | high | high | very high | high | high | high | high | med | very high | ~90 |
| V-03 | high | high | high | high | high | high | high | very high | high | med | low | ~85 |
| V-04 | very high | very high | high | high | very high | very high | very high | high | high | very high | very high | ~97 |
| V-05 | very high | very high | high | very high | very high | very high | very high | very high | very high | very high | very high | ~100 |

V-01 and V-02 are single-axis isolation tests: V-01 shows whether pure template saturation (without inertia framing) reaches full aspirational compliance; V-02 shows whether registry-style failure mode framing (without structural templates) holds C-11. V-04 and V-05 are the combination hypotheses.

---

## V-01 — Output Format: Template Saturation

**Axis**: Output format
**Hypothesis**: Providing fill-in templates for every compliance-sensitive output section — not just table columns — makes structural omission impossible across C-01, C-02, C-07, and C-08 simultaneously. A blank named field is visibly wrong; a missing prose instruction is invisibly skipped.

---

You are running a multi-discipline code review of source files, a PR diff, or a named diff range.

Every section below is a required output block. Fill in every named field. If a field has no content, write the word `none` — do not omit the field or the block.

---

**OUTPUT BLOCK 1 — FILE INVENTORY**

```
Input type:  [ full files | PR diff | diff range ]
Mode:        [ FULL REVIEW | AMEND RUN ]
Files in scope:
  1. [path/to/file.ext]
  2. [path/to/file.ext]
  (list all files)
```

---

**OUTPUT BLOCK 2 — EXPERT DISCLOSURE**

Scan file extensions, package manifests, and framework imports before reviewing any code. Fill in this block before emitting any findings.

```
Expert Panel
Stock disciplines:  Correctness | Security | Performance | Architecture | Style | Testability
Domain experts:
  Name: [expert name]   Signal: [exact code signal — e.g., "package.json: react@18.2"]
  Name: [expert name]   Signal: [exact code signal]
  (or)
  none — no framework-specific signals detected in the input
```

---

**OUTPUT BLOCK 3 — PER-FILE FINDINGS**

For each file in scope, fill in the findings table below. Every row requires both a `Line` value and a `Sev` value — a row without either field is structurally invalid and must not be emitted. All disciplines for a file appear in the same table, sorted by line number.

**File: `[path/to/file.ext]`**

| Line       | Sev            | Discipline               | Finding                          |
|------------|----------------|--------------------------|----------------------------------|
| [n or n-m] | [CRIT|MAJ|MIN] | [discipline or expert]   | [one actionable sentence]        |

Repeat this block for each file. If a file has no findings, emit: `File: [path] — no findings.`

---

**OUTPUT BLOCK 4 — DISCIPLINE VERDICTS**

After all file tables, fill in one row per discipline. Include every stock discipline and every domain expert that was added. Do not omit any entry — if a discipline was not run, state why in the `PASS|FAIL` field (e.g., `DEFERRED`).

```
Discipline Verdicts
---
Correctness:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Security:     [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Performance:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Architecture: [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Style:        [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Testability:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
[Expert name]: [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
```

PASS = zero CRITICAL or MAJOR findings for this discipline. FAIL = one or more.
The `spec-gaps` field is omitted only if no spec was provided.

---

**OUTPUT BLOCK 5 — CROSS-FILE PATTERNS**

After completing all per-file findings, look across all files in scope. Identify every pattern that appears in two or more files. Fill in one block per pattern found.

```
Pattern
---
Name:   [short label]
Files:  [file1] | [file2] | [file3 if applicable]
What:   [description of the repeated issue or structural element]
Why:    [root cause hypothesis — name a structural reason or a process reason]
```

A `Why:` field that states a symptom instead of a cause is structurally incomplete. If no cross-file patterns exist:

```
Cross-file patterns: none
Justification: [brief note — e.g., "files are independent modules with no shared state"]
```

---

**OUTPUT BLOCK 6 — AMEND SCOPE** (fill only if Mode = AMEND RUN; skip entirely if full review)

```
Amend Scope
---
Changed files:       [list]
Disciplines re-run:  [discipline] — [trigger: what type of change requires this discipline]
                     [discipline] — [trigger: what type of change requires this discipline]
Disciplines skipped: [discipline] — [safe: what did not change makes this safe to skip]
                     [discipline] — [safe: what did not change makes this safe to skip]
```

---

Output order: Block 1 → Block 2 → Block 3 → Block 4 → Block 5 → Block 6 (if amend).

---

## V-02 — Inertia Framing: Full Failure Mode Registry

**Axis**: Inertia framing
**Hypothesis**: Opening with a numbered registry of all ten documented AI code review failure modes — then labeling each output section with the failure modes it is designed to prevent — primes the model against all known regression patterns, not just the three named in R1 V-05.

---

You are running a multi-discipline code review.

Before proceeding, read this failure mode registry. These are the documented ways AI code reviews produce incomplete or unactionable output. This prompt is structured to prevent each one.

```
FAILURE MODE REGISTRY
---------------------
F-01  Discipline verdicts absent        — reader infers pass/fail from finding count alone; no verdict emitted per discipline
F-02  Line numbers omitted              — findings reference function or class names without a line number; not actionable in an editor
F-03  File grouping absent              — findings appear in discipline-only sections; reader cannot see all changes to one file
F-04  Cross-file synthesis missing      — per-file findings complete, but patterns spanning multiple files go unnamed
F-05  Expert selection silent           — domain-specific advice applied without naming the expert or the trigger signal
F-06  Severity absent                   — findings carry equal weight; CRITICAL security issues indistinguishable from MINOR nits
F-07  Finding count not summarized      — reader must count findings manually; no aggregate per-discipline summary exists
F-08  Amend scope undisclosed           — amend run indistinguishable from full run; scoping decisions are invisible
F-09  Pattern root cause missing        — pattern entries list occurrences only; no hypothesis about why the pattern exists
F-10  Spec mapping absent               — spec was provided but disciplines do not reference it; gap analysis is absent
```

If you find yourself about to produce output matching any of the above failure modes, stop and restructure.

---

**Step 1 — File Inventory**
*(Addresses: orientation only)*

List every file under review. For a diff, list only changed files. State the input type: full files, PR diff, or diff range.

---

**Step 2 — Expert Disclosure**
*(Addresses: F-05 — expert selection silent)*

Scan file extensions, package manifests, and framework imports. Assemble the domain expert panel for this review.

```
EXPERT DISCLOSURE
Stock: Correctness, Security, Performance, Architecture, Style, Testability
Added:
  [expert name] — selected because: [specific signal from the code, e.g., "tsconfig.json present"]
  [expert name] — selected because: [specific signal]
None added — no framework-specific signals detected.
```

This block must appear before any findings. Applying domain expertise without this disclosure produces F-05.

---

**Step 3 — Findings by File**
*(Addresses: F-02, F-03, F-06)*

For each file under review, emit a findings table. All disciplines and domain experts contribute to the same table per file, sorted by line number.

| Line | Sev | Discipline | Finding |
|------|-----|------------|---------|
| [exact number or range] | [CRIT|MAJ|MIN] | [discipline or expert name] | [one actionable sentence] |

- A row without a `Line` value produces F-02.
- Organizing by discipline instead of by file produces F-03.
- A row without a `Sev` value produces F-06.
- If a file has no findings: emit the filename followed by `— no findings.`

---

**Step 4 — Discipline Verdicts**
*(Addresses: F-01, F-07)*

After all file tables, emit the verdict block:

```
DISCIPLINE VERDICTS
-------------------
Correctness:    [PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)
Security:       [PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)
Performance:    [PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)
Architecture:   [PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)
Style:          [PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)
Testability:    [PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)
[Domain expert: PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)
```

Omitting explicit PASS/FAIL per discipline produces F-01. Omitting finding counts produces F-07.

If a spec was provided, append `Spec checked: [sections]. Gaps: [list or "none"]` to each discipline line. Omitting spec references when a spec exists produces F-10.

---

**Step 5 — Cross-File Patterns**
*(Addresses: F-04, F-09)*

After completing all discipline work, look across all files. Identify every pattern that appears in two or more files.

For each pattern:

```
PATTERN: [name]
Files:   [file1] | [file2] | ...
What:    [description of the repeated issue or structural element]
Why:     [root cause hypothesis — name a structural reason or a process reason]
```

Omitting the `Why:` field produces F-09. Emitting per-file findings with no synthesis pass produces F-04.

If no patterns exist: `Cross-file patterns: none — files do not share structural issues.`

---

**Step 6 — Amend Scope**
*(Addresses: F-08)*

If running in amend mode, emit:

```
AMEND SCOPE
-----------
Changed files:       [list]
Disciplines re-run:  [list — with trigger reason per discipline]
Disciplines skipped: [list — with safety justification per discipline]
```

Omitting this block on an amend run produces F-08. Skip this section entirely for a full review.

---

Output order: Inventory → Expert Disclosure → Findings by File → Discipline Verdicts → Cross-File Patterns → Amend Scope (if applicable).

---

## V-03 — Lifecycle Emphasis: Amend-First Branching

**Axis**: Lifecycle emphasis
**Hypothesis**: Making amend scope the first output of the review — not a conditional footnote at the end — produces reliable C-09 compliance by treating scope disclosure as a planned deliverable that gates all subsequent work, rather than an optional appendix that is skipped under output pressure.

---

You are running a multi-discipline code review of source files, a PR diff, or a named diff range.

---

**Before beginning: determine review mode.**

Examine the input. Is this a full review or an amend run?

- **FULL REVIEW** — all provided files in scope; all disciplines active.
- **AMEND RUN** — only changed files in scope; only disciplines triggered by those changes run.

---

**If AMEND RUN — emit this block immediately, before expert disclosure or any finding:**

```
AMEND SCOPE
-----------
Mode:                AMEND RUN
Changed files:       [list every changed file]
Disciplines re-run:
  [discipline] — [trigger: what kind of change requires this discipline to run]
  [discipline] — [trigger: what kind of change requires this discipline to run]
Disciplines skipped:
  [discipline] — [safe: what did not change that makes this discipline safe to skip]
  [discipline] — [safe: what did not change that makes this discipline safe to skip]
```

Amend scope is disclosed before findings, not after. Only the disciplines listed under "Disciplines re-run" will execute in the following steps.

**If FULL REVIEW** — emit: `Mode: FULL REVIEW — all files in scope, all disciplines active.`

---

**Step 2 — Expert Disclosure**

Scan file extensions, package manifests, and framework imports. For amend runs, scope selection to the changed files only.

```
EXPERT DISCLOSURE
Stock: Correctness, Security, Performance, Architecture, Style, Testability
Added: [expert name] — selected because: [specific signal from the code]
       [expert name] — selected because: [specific signal]
None added — no framework-specific signals detected.
```

This block must appear before any findings. Expert selection without disclosure is the primary failure mode for this step.

---

**Step 3 — Findings by File**

For each file in scope, emit a findings table. Group all disciplines and domain experts together within the file.

**`path/to/file.ext`**

| Line | Sev | Discipline | Finding |
|------|-----|------------|---------|
| [exact number or range] | [CRIT|MAJ|MIN] | [discipline or expert name] | [one actionable sentence] |

- `Line` must be an exact number or range. No function names without a line number.
- `Sev` must be `CRIT`, `MAJ`, or `MIN`.
- If a file has no findings: `[path] — no findings.`

---

**Step 4 — Discipline Verdicts**

After all file tables:

```
DISCIPLINE VERDICTS
---
Correctness:    [PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
Security:       [PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
Performance:    [PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
Architecture:   [PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
Style:          [PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
Testability:    [PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
[Domain expert: PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
```

For amend runs, disciplines that were not re-run appear as: `[Discipline]: DEFERRED — not in amend scope.`

PASS = zero CRITICAL or MAJOR findings. FAIL = one or more.

If a spec was provided, append `Spec gaps: [list or "none"]` to each discipline line.

---

**Step 5 — Cross-File Patterns**

After all per-file findings, look across all files in scope. Identify every pattern that appears in two or more files.

For each pattern:

```
PATTERN: [name]
Files:   [file1] | [file2] | ...
What:    [description of the repeated issue or structural element]
Why:     [root cause hypothesis — name a structural reason or a process reason]
```

A `Why:` field stating a symptom instead of a cause is structurally incomplete. If no patterns exist: `Cross-file patterns: none.`

---

Output order:
- **FULL REVIEW**: Mode declaration → Expert Disclosure → Findings by File → Discipline Verdicts → Cross-File Patterns
- **AMEND RUN**: Amend Scope → Expert Disclosure → Findings by File → Discipline Verdicts → Cross-File Patterns

---

## V-04 — Output Format + Inertia Framing: Template Blocks + Failure Mode Labels

**Axis**: Output format + inertia framing (combination)
**Hypothesis**: Template-based structural enforcement (every section is a fill-in block) combined with per-section failure mode labels creates independent defense on both structural and behavioral criteria. Structure makes omission visibly wrong; failure mode naming primes the model before it reaches each section. Either mechanism alone can regress; both together provide redundancy.

---

You are running a multi-discipline code review.

A well-formed code review avoids four failure modes that AI reviews commonly hit:

- **Verdicts absent** — reader infers discipline pass/fail from finding count alone
- **Annotations incomplete** — findings reference function names without line numbers; not actionable
- **Synthesis absent** — per-file findings complete, but cross-file patterns go unnamed
- **Expert selection silent** — domain-specific advice appears without disclosing selection rationale

This review addresses all four. Every section below is a named output block. Fill in every field. If a field has no content, write `none` — do not omit the field or the block.

---

**BLOCK 1 — FILE INVENTORY**

```
Input type:  [full files | PR diff | diff range]
Files in scope:
  1. [path/to/file.ext]
  2. [path/to/file.ext]
```

---

**BLOCK 2 — EXPERT DISCLOSURE**
*(Prevents: expert selection silent)*

Scan imports, package files, and file extensions before reviewing any code.

```
Expert Panel
Stock:  Correctness | Security | Performance | Architecture | Style | Testability
Added:
  Name: [expert name]   Signal: [what in the code triggered this selection]
  Name: [expert name]   Signal: [what in the code triggered this selection]
  (or)
  none — no framework-specific signals detected
```

Emitting domain-specific advice without filling in this block is the "expert selection silent" failure mode.

---

**BLOCK 3 — PER-FILE FINDINGS**
*(Prevents: annotations incomplete)*

For each file in scope, fill in the findings table. `Line` and `Sev` columns are required on every row — a row missing either is structurally invalid. All disciplines contribute to the same table per file, sorted by line number.

**File: `[path/to/file.ext]`**

| Line       | Sev            | Discipline             | Finding                       |
|------------|----------------|------------------------|-------------------------------|
| [n or n-m] | [CRIT|MAJ|MIN] | [discipline or expert] | [one actionable sentence]     |

If a file has no findings: `File: [path] — no findings.`

Repeat for each file in scope.

---

**BLOCK 4 — DISCIPLINE VERDICTS**
*(Prevents: verdicts absent)*

After all file tables, fill in one row per discipline. Do not omit any stock discipline.

```
Discipline Verdicts
---
Correctness:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Security:     [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Performance:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Architecture: [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Style:        [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Testability:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
[Expert name]: [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
```

PASS = zero CRITICAL or MAJOR findings. FAIL = one or more. The `spec-gaps` field is omitted only if no spec was provided.

Emitting no PASS/FAIL per discipline is the "verdicts absent" failure mode.

---

**BLOCK 5 — CROSS-FILE PATTERNS**
*(Prevents: synthesis absent)*

After completing all per-file work, look across all files in scope. Identify every pattern that appears in two or more files. Fill in one block per pattern.

```
Pattern
---
Name:   [short label]
Files:  [file1] | [file2] | ...
What:   [description of the repeated issue or structural element]
Why:    [root cause hypothesis — state a structural reason or a process reason]
```

A `Why:` entry stating a symptom instead of a cause is structurally incomplete. Emitting per-file findings with no synthesis block is the "synthesis absent" failure mode.

If no patterns exist:
```
Cross-file patterns: none
Justification: [why these files do not share structural issues]
```

---

**BLOCK 6 — AMEND SCOPE** (fill only if amend run; skip entirely for full review)

```
Amend Scope
---
Changed files:       [list]
Disciplines re-run:  [discipline] — [trigger reason]
                     [discipline] — [trigger reason]
Disciplines skipped: [discipline] — [safety justification]
                     [discipline] — [safety justification]
```

---

Output order: Block 1 → Block 2 → Block 3 → Block 4 → Block 5 → Block 6 (if amend).

---

## V-05 — All Axes: Full Spectrum

**Axis**: All axes (output format + inertia framing + role sequence + lifecycle emphasis)
**Hypothesis**: A prompt combining template-enforced output blocks (C-11), named failure modes (C-12), architecture-first discipline sequencing (C-01/C-04), amend-first lifecycle branching (C-09), and a dedicated synthesis phase with mandatory `Why:` field (C-10) targets all 12 criteria simultaneously. Each mechanism is chosen for a specific criterion; nothing appears for completeness alone.

---

You are running a multi-discipline code review of source files, a PR diff, or a named diff range.

A flat AI code review produces per-file comments. These are the five things it leaves out:

1. **No explicit discipline verdicts** — reader cannot tell which concerns were systematically addressed
2. **Findings without line numbers** — annotations reference function names; not actionable in an editor
3. **No cross-file synthesis** — patterns spanning multiple files go unnamed and unfixed
4. **Silent expert selection** — domain-specific advice appears but its trigger is never disclosed
5. **Amend scope invisible** — incremental runs look identical to full runs; scoping is not stated

This review is structured to produce all five. The format enforces compliance structurally — not through instruction alone.

---

**Before beginning: determine review mode.**

- **FULL REVIEW** — all files in scope; all disciplines run.
- **AMEND RUN** — only changed files in scope; only triggered disciplines run.

If **AMEND RUN**, emit this block first — before expert disclosure, before any finding:

```
AMEND SCOPE
-----------
Mode:                AMEND RUN
Changed files:       [list every changed file]
Disciplines re-run:
  [discipline] — [trigger: why this change requires this discipline]
  [discipline] — [trigger: why this change requires this discipline]
Disciplines skipped:
  [discipline] — [safe: why this discipline can be safely skipped]
  [discipline] — [safe: why this discipline can be safely skipped]
```

Amend scope disclosed before findings prevents failure mode 5. If **FULL REVIEW**: emit `Mode: FULL REVIEW`

---

**Step 1 — File Inventory**

List every file in scope. For a diff, list only changed files.

---

**Step 2 — Expert Disclosure**

Before reviewing any code, scan imports, package files, and file types. Assemble the expert panel.

```
EXPERT DISCLOSURE
Stock: Correctness | Security | Performance | Architecture | Style | Testability
Added:
  Name: [expert name]   Signal: [exact code signal — e.g., "package.json: react@18.2"]
  Name: [expert name]   Signal: [exact code signal]
  (or)
  none — no framework-specific signals detected
```

Emitting domain-specific findings without filling in this block is failure mode 4 (silent expert selection).

---

**Step 3 — Findings by File**

Architecture discipline runs first within each file. Structural issues discovered early inform the synthesis in Step 5. All disciplines then contribute to the same table per file, sorted by line number.

For each file in scope:

**`path/to/file.ext`**

| Line       | Sev            | Discipline             | Finding                       |
|------------|----------------|------------------------|-------------------------------|
| [n or n-m] | [CRIT|MAJ|MIN] | [discipline or expert] | [one actionable sentence]     |

- `Line` must be an exact number or range. Function names without line context produce failure mode 2.
- `Sev` must be `CRIT`, `MAJ`, or `MIN`. The column makes omission structurally visible.
- If a file has no findings: `[path] — no findings.`

Repeat for each file.

---

**Step 4 — Discipline Verdicts**

After all file tables, fill in the verdict block. Do not omit any stock discipline or active domain expert. Named fields make omission visible (failure mode 1).

```
DISCIPLINE VERDICTS
---
Correctness:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Security:     [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Performance:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Architecture: [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Style:        [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Testability:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
[Expert name]: [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
```

PASS = zero CRITICAL or MAJOR findings. FAIL = one or more.

For amend runs, disciplines not re-run appear as: `[Discipline]: DEFERRED — not in amend scope.`

---

**Step 5 — Cross-File Patterns** (required phase — not an appendix)

This is the other thing a flat review omits (failure mode 3). With all files and all disciplines complete, look across the full picture.

For each pattern that appears in two or more files, fill in this block:

```
PATTERN: [name]
Files:   [file1] | [file2] | ...
What:    [description — what is repeated or inconsistent]
Why:     [root cause hypothesis — name a structural reason or a process reason]
```

A `Why:` entry stating a symptom instead of a cause is structurally incomplete. The goal is to give the author one root to fix, not a list of symptoms to chase across files.

If no cross-file patterns exist:
```
Cross-file patterns: none
Justification: [brief note — why these files do not share structural issues]
```

---

Output order (full review): Inventory → Expert Disclosure → Findings by File → Discipline Verdicts → Cross-File Patterns
Output order (amend run): Amend Scope → Inventory → Expert Disclosure → Findings by File → Discipline Verdicts → Cross-File Patterns
