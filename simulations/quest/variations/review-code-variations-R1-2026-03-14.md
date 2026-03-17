Written to `simulations/quest/variations/review-code-variations-R1-2026-03-14.md`.

---

## review-code — Variations R1

### Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Role sequence | Architecture-first ordering primes cross-file pattern detection before per-file detail work |
| V-02 | Output format | Table-primary findings mechanically enforce file:line + severity on every row |
| V-03 | Phrasing register | Conversational framing improves depth at the cost of structural compliance |
| V-04 | Role sequence + lifecycle emphasis | Expert-first naming + dedicated synthesis phase improves C-04 and C-05 together |
| V-05 | Output format + inertia framing | Compact table + "what a normal review misses" framing raises the floor on C-02, C-04, C-05 |

---

### Design rationale by variation

**V-01 (role sequence)** — Architecture runs before Correctness/Security/etc. The structural skeleton is established before per-file detail work begins. Hypothesis: this primes C-04 cross-file pattern detection because the model has already mapped dependencies before it encounters individual findings.

**V-02 (output format)** — All findings live in one unified table with columns `File:Line | Severity | Discipline | Finding`. No row can exist without an exact line reference and severity — the format makes C-02 and C-07 failures impossible to produce. Verdicts and patterns follow in separate blocks.

**V-03 (phrasing register)** — Fully conversational: "walk through each discipline and share what you find." Tests whether softer framing improves finding depth or degrades structural compliance. Expected failure mode: C-05 expert disclosure gets buried in prose rather than emitted as a discrete block.

**V-04 (combination: role sequence + lifecycle emphasis)** — Four named lifecycle phases (Setup, Per-Discipline Review, Synthesis, Amend Scope). Experts assembled in Phase 1 before any discipline fires. Synthesis is Phase 3, not a footnote — treated as a required phase with its own heading. Architecture discipline runs first within Phase 2. Targets C-04 and C-05 simultaneously.

**V-05 (combination: output format + inertia framing)** — Opens by naming the three things a naive AI review leaves out (no verdicts, no patterns, silent expert selection), then requires exactly those outputs. Table format per file, verdict block after, pattern block with mandatory `Why:` line. The inertia framing makes the rubric failure modes salient without stating them as rubric criteria.

---

### Scoring predictions

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-07 | C-08 | Expected composite |
|-----------|------|------|------|------|------|------|------|--------------------|
| V-01 | high | high | high | high | high | med | med | ~85 |
| V-02 | high | very high | high | high | high | very high | high | ~90 |
| V-03 | med | med | med | med | med | low | low | ~60 |
| V-04 | high | high | high | very high | very high | high | high | ~90 |
| V-05 | high | very high | high | very high | very high | very high | high | ~95 |

V-03 is the control case — expected to show structural degradation that validates why the imperative forms in V-01/V-02/V-04/V-05 are worth the verbosity cost.
locking calls, unnecessary allocations, hot-path waste
- **Style / Conventions** — naming, formatting, idiom adherence, dead code
- **Testability** — untestable side effects, missing seams, hidden dependencies, coverage gaps

For each discipline: if a spec was provided, identify which spec sections this discipline checked and flag any requirements not implemented.

**Step 5 — Cross-File Patterns**

After all disciplines complete, run a synthesis pass. Identify patterns that appear in two or more files.

For each pattern:
- **Pattern name**: short label
- **Files**: list every file where it appears
- **Description**: what the pattern is
- **Root cause hypothesis**: why it exists (structural reason or process reason)

If no cross-file patterns exist, write: `Cross-file patterns: none identified.`

**Step 6 — Amend Mode (skip if full review)**

If running in amend mode (changed files only):
- List the changed files
- List which disciplines were re-run (with reason)
- List which disciplines were skipped (with reason, e.g., "architecture: no structural files changed")

---

Output order: Inventory → Expert Disclosure → Architecture → [Correctness, Security, Performance, Style, Testability] → Cross-File Patterns → Amend Scope (if applicable).

---

## V-02 — Output Format: Table-Primary Findings

**Axis**: Output format
**Hypothesis**: Structuring findings as rows in a table (with columns for file:line, severity, discipline, and description) mechanically enforces annotation and severity on every finding, eliminating the most common failure modes for C-02 and C-07.

---

You are running a multi-discipline code review. The review covers source files, a PR diff, or a named diff range. If a spec document is provided, each discipline checks compliance against it.

**Step 1 — Inventory**

List every file under review. For a diff, list only the changed files. State the input type (full files / PR / diff range).

**Step 2 — Domain Expert Selection**

Examine the file extensions, package manifests, and framework imports. Select domain experts appropriate to the stack. Emit:

```
Domain Experts Selected:
- [Expert name] — signal: [what triggered this selection]
```

If no domain expertise beyond stock is needed, state that explicitly.

**Step 3 — Findings Table**

Emit all findings from all disciplines in a single table, grouped by file. Within each file group, findings are sorted by line number.

Table format:

| File:Line | Severity | Discipline | Finding |
|-----------|----------|------------|---------|
| auth/login.ts:42 | CRITICAL | Security | SQL query built via string concatenation — injection risk |
| auth/login.ts:67 | MINOR | Style | Variable `x` should be named `retryCount` |
| utils/fetch.ts:12-18 | MAJOR | Performance | Awaiting inside loop causes sequential fetches |

Rules:
- Every row must have a `File:Line` value in `file:line` or `file:start-end` format. No row may reference only a function name or class.
- Severity must be one of: `CRITICAL`, `MAJOR`, `MINOR`.
- Discipline must be one of: `Correctness`, `Security`, `Performance`, `Architecture`, `Style`, `Testability`, or a named domain expert.
- Finding must be a single actionable sentence.

If no findings exist for a file, do not emit a row for it — instead note it in the per-discipline verdicts below.

**Step 4 — Per-Discipline Verdicts**

After the findings table, emit one verdict block per discipline:

```
Correctness:    PASS | N findings: X CRITICAL, Y MAJOR, Z MINOR
Security:       PASS | N findings: X CRITICAL, Y MAJOR, Z MINOR
Performance:    FAIL | N findings: X CRITICAL, Y MAJOR, Z MINOR
Architecture:   PASS | N findings: X CRITICAL, Y MAJOR, Z MINOR
Style:          PASS | N findings: X CRITICAL, Y MAJOR, Z MINOR
Testability:    FAIL | N findings: X CRITICAL, Y MAJOR, Z MINOR
[Domain Expert: PASS/FAIL | N findings: ...]
```

If a spec was provided, append to each verdict: `Spec sections checked: [list]. Gaps: [list or "none"].`

**Step 5 — Cross-File Patterns**

Identify patterns that appear in two or more files. For each pattern:

```
Pattern: [name]
Files: [file1], [file2], [file3]
Description: [what the pattern is]
Root cause hypothesis: [why it exists — structural or process reason]
```

If no cross-file patterns exist, write: `Cross-file patterns: none identified.`

**Step 6 — Amend Mode (skip if full review)**

If running in amend mode:
- Changed files: [list]
- Disciplines re-run: [list with reason]
- Disciplines skipped: [list with reason]

---

Output order: Inventory → Expert Disclosure → Findings Table → Per-Discipline Verdicts → Cross-File Patterns → Amend Scope (if applicable).

---

## V-03 — Phrasing Register: Conversational / Descriptive

**Axis**: Phrasing register
**Hypothesis**: A descriptive, conversational register ("walk through each discipline and share what you find") may improve finding depth and reading clarity but risks weaker structural compliance than imperative command-form prompts.

---

You're doing a thorough code review across multiple disciplines. Think of yourself as a team of specialists who each look at the code from a different angle, then get together to compare notes.

Start by orienting yourself.

**Get your bearings first.** List all the files you're reviewing. If this is a diff or PR, focus on what changed. Note what kind of input you have — full source, diff, or PR.

**Pick your specialist team.** Look at what's in the files — file types, imports, package manifests, framework clues. Based on what you see, decide which domain experts to bring in beyond the six stock disciplines. Tell the reader who you selected and what in the code told you to bring them in. If nothing special is needed, say so.

**Walk through each discipline.** For each one, share what you found. Organize your findings by file — everything about `auth/login.ts` together, everything about `utils/fetch.ts` together, and so on. For each finding, include a `file:line` reference so the reader can jump straight to it in their editor. Label each finding as CRITICAL, MAJOR, or MINOR so the reader knows what to fix first. At the end of each discipline's section, give a quick verdict (PASS or FAIL) and a count of how many findings you found at each severity level.

The six disciplines to cover:
- **Correctness** — is the logic right? are APIs used correctly? are assumptions valid?
- **Security** — injection, auth gaps, unsafe operations, data exposure
- **Performance** — N+1s, blocking calls, hot-path waste, unnecessary work
- **Architecture** — structural coherence, layering, dependency direction, coupling
- **Style / Conventions** — naming, idioms, dead code, formatting
- **Testability** — can this code be tested? are there hidden dependencies or side effects that make testing hard?

If a spec was provided, each discipline should note which spec requirements it checked and whether any requirements are missing from the code.

**Look for patterns across files.** After you've been through all the disciplines, step back and look at the whole picture. What patterns show up in more than one file? Name each pattern, list the files where it appears, describe what it is, and — this is the important part — offer a hypothesis about why it exists. Is there a shared utility that should exist but doesn't? Was this code added post-hoc before a style guide was in place? Give the reader something to act on, not just a list of occurrences.

**If this is an incremental amend run**, tell the reader which files changed, which disciplines you re-ran because of those changes, and which disciplines you skipped and why.

---

Work through this in order: orient yourself, pick your team, cover each discipline file-by-file, synthesize patterns, handle amend scope if applicable.

---

## V-04 — Role Sequence + Lifecycle Emphasis: Expert-First + Dedicated Synthesis Phase

**Axis**: Role sequence + lifecycle emphasis (combination)
**Hypothesis**: Naming domain experts at the top of the run (before any discipline work) and treating the synthesis pass as a named, mandatory lifecycle phase — not an appendix — improves both C-05 (domain expert disclosure) and C-04 (cross-file patterns) simultaneously. Expert identity shapes all subsequent discipline output when established early.

---

You are running a multi-discipline code review. The review covers source files, a PR diff, or a named diff range.

The review has four mandatory lifecycle phases. Do not skip or merge phases.

---

### Phase 1 — Setup

**1a. Inventory**
List every file under review. For a diff, list only changed files. State the input type.

**1b. Expert Panel Assembly**
This step runs before any discipline work begins. Examine the file extensions, package manifests, framework imports, and dependency lists. Assemble the expert panel for this review.

Emit a panel declaration:

```
Expert Panel for this Review
-----------------------------
Stock disciplines: Correctness, Security, Performance, Architecture, Style, Testability
Domain experts added:
  - [Expert name]: [specific signal that triggered selection — e.g., "package.json contains react@18.2"]
  - [Expert name]: [specific signal]
(or)
Domain experts: none — no framework-specific signals detected
```

Every discipline output in Phase 2 will carry the expert's name or discipline label. The panel declaration is the only place where selection rationale is stated.

**1c. Spec Inventory (if spec provided)**
List the spec sections and requirements you will check against. This list will be used in Phase 2 for per-discipline spec mapping.

---

### Phase 2 — Per-Discipline Review

For each discipline in the panel (stock + domain experts), run a complete discipline pass.

Structure each discipline section as follows:

```
## [Discipline Name]: [PASS | FAIL]
Summary: N findings — X CRITICAL, Y MAJOR, Z MINOR
[Spec coverage: sections checked / gaps found — omit if no spec provided]

### [filename]
- [SEVERITY] file:line — [finding]
- [SEVERITY] file:line — [finding]

### [filename]
- [SEVERITY] file:line — [finding]
```

Rules for Phase 2:
- Every finding must carry `file:line` or `file:start-end`. No function-name-only references.
- Severity is `CRITICAL`, `MAJOR`, or `MINOR` on every finding.
- Findings are grouped under their source file within the discipline section.
- If a discipline finds nothing, write: `No findings.` Do not omit the section.

Discipline sequence: Architecture → Correctness → Security → Performance → Style → Testability → [domain experts in order of addition].

Architecture runs first because structural issues discovered in Phase 2 inform the synthesis work in Phase 3.

---

### Phase 3 — Synthesis

This phase runs after all discipline passes complete. It is not an appendix — it is a required review phase.

**3a. Cross-File Patterns**

Identify every pattern that appears in two or more files.

For each pattern, emit:
```
Pattern: [short label]
Appears in: [file1], [file2], [file3, ...]
What it is: [description of the repeated issue or structural element]
Root cause hypothesis: [why does this exist? name a structural or process reason]
```

If no patterns exist, emit: `Cross-file patterns: none — files do not share structural issues.`

A synthesis pass that finds no patterns after reviewing N files warrants a brief justification (e.g., "files are independent modules with no shared state").

**3b. Review Summary**

Emit a one-paragraph summary:
- How many total findings, breakdown by severity
- Which disciplines failed
- The most critical pattern (or "no cross-file patterns")
- Recommended first action for the author

---

### Phase 4 — Amend Scope (skip if full review)

If running in amend mode, emit:

```
Amend Scope
-----------
Changed files: [list]
Disciplines re-run: [list — with reason each was triggered]
Disciplines skipped: [list — with reason each was safe to skip]
```

---

Execute phases in order: Setup → Per-Discipline Review → Synthesis → Amend Scope.

---

## V-05 — Output Format + Inertia Framing: Compact Table + "What a Normal Review Misses"

**Axis**: Output format + inertia framing (combination)
**Hypothesis**: Explicitly naming what a naive single-pass review fails to produce — then requiring those exact outputs — raises the structural floor. Combined with a compact table format that enforces annotations mechanically, this variation targets C-02, C-04, and C-05 together by making the failure modes salient.

---

You are running a multi-discipline code review.

A typical AI code review produces a flat list of per-file comments. That leaves three things on the table:

1. **No discipline verdicts** — the reader can't tell which concerns were systematically addressed
2. **No cross-file synthesis** — patterns that span multiple files go unnamed and unfixed
3. **Silent expert selection** — domain-specific advice appears but its source is never disclosed

This review produces all three. Here is the structure.

---

**Step 1 — File Inventory**

List every file under review. For a diff, list only changed files. State whether this is a full review or amend run.

---

**Step 2 — Expert Disclosure**

Before reviewing any code: scan imports, package files, and file types. Select domain experts.

```
EXPERT DISCLOSURE
Stock: Correctness, Security, Performance, Architecture, Style, Testability
Added: [expert name] — selected because: [specific signal from the code]
       [expert name] — selected because: [specific signal from the code]
None added — no framework-specific signals detected.
```

This block must appear before any findings. Experts selected silently is the failure mode.

---

**Step 3 — Findings (table per file)**

For each file under review, emit a findings table. Group all disciplines together within the file.

**`path/to/file.ext`**

| Line | Sev | Discipline | Finding |
|------|-----|------------|---------|
| 42 | CRIT | Security | SQL query via string concat — injection risk |
| 67 | MIN | Style | `x` should be `retryCount` |
| 88-94 | MAJ | Performance | Sequential awaits inside loop |

- `Line` must be a number or range. No function names, no "around line X". Exact lines only.
- `Sev` must be `CRIT`, `MAJ`, or `MIN`.
- `Discipline` names the discipline or domain expert that owns the finding.
- `Finding` is one actionable sentence.

If a file has no findings, emit: **`path/to/file.ext` — no findings.**

---

**Step 4 — Discipline Verdicts**

After all file tables, emit the verdict block. This is what a normal review leaves out.

```
DISCIPLINE VERDICTS
-------------------
Correctness:    [PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
Security:       [PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
Performance:    [PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
Architecture:   [PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
Style:          [PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
Testability:    [PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
[Domain expert: PASS|FAIL]  --  N findings (X CRIT, Y MAJ, Z MIN)
```

PASS = no CRITICAL or MAJOR findings in this discipline. FAIL = at least one CRITICAL or MAJOR.

If a spec was provided, append to each line: `Spec gaps: [list requirements not implemented, or "none"]`.

---

**Step 5 — Cross-File Patterns**

This is the other thing a normal review leaves out. After seeing all files and all disciplines, look across the full picture.

For each pattern that appears in two or more files:

```
PATTERN: [name]
Files:   [file1] | [file2] | [file3]
What:    [description — what is repeated or inconsistent]
Why:     [root cause hypothesis — structural reason or process reason]
```

A pattern entry without a `Why:` line is incomplete. The goal is to give the author one root cause to fix, not a list of symptoms to chase across files.

If no cross-file patterns exist: `CROSS-FILE PATTERNS: none identified — files do not share structural issues.`

---

**Step 6 — Amend Scope (skip if full review)**

```
AMEND SCOPE
-----------
Changed files:       [list]
Disciplines re-run:  [list — why each was triggered]
Disciplines skipped: [list — why each was safe to skip]
```

---

Output order: Inventory → Expert Disclosure → File Tables → Discipline Verdicts → Cross-File Patterns → Amend Scope.
