## review-code — Variations R4

Five variations written to `simulations/quest/variations/review-code-variations-R4-2026-03-14.md`.

---

### Variation Map

| ID | Axis | Predicted Score |
|----|------|-----------------|
| **V-01** | C-15 boundary: prose templates, no key=value | **98.75** |
| **V-02** | C-16 boundary: compact 5-item registry + key=value | **98.75** |
| **V-03** | Phrasing register: conversational/explanatory, all mechanisms intact | **100** |
| **V-04** | Minimal 100/100: strip all redundancy, one mechanism per criterion | **100** |
| **V-05** | Spec-forward: dedicated pre-review spec claims block (Block 3) | **100** |

---

### What R4 probes

**Single-axis isolation (V-01, V-02)** — both are deliberate one-criterion failure probes anchoring the two new R4 criteria:
- V-01 confirms C-15 fires on prose templates: `N findings (X CRIT, Y MAJ, Z MIN)` fails; `total=[N] CRIT=[n]` passes. 1.25 pt delta.
- V-02 confirms C-16 fires on compact registries: F-01..F-05 only fails C-16 even when C-14 and C-15 both pass.

**Register test (V-03)** — the first variation to keep all structural mechanisms but change tone from imperative to explanatory. If V-03 scores below 100, it reveals that some "explanatory" prose in R3 V-04 was load-bearing enforcement, not commentary.

**Minimalism probe (V-04)** — R3 V-04 achieved 100 at high token cost. V-04 strips to bare mechanism: 10-item registry, one F-ID per block, table columns, key=value template. No explanatory bullets, no multi-line cautions. Tests whether the extra prose in R3 V-04 was adding robustness or just weight.

**Spec-forward layout (V-05)** — the only variation that changes the structural layout. Adds a mandatory pre-review spec claims block where each discipline declares ownership of spec sections before reviewing code. A claimed section + no implementation = automatic gap. Qualitatively stronger C-06 enforcement than the current post-hoc `spec-gaps=` verdict field.
ucturally strengthens C-06 beyond the verdict-level `spec-gaps=` field. |

---

### Key design decisions

**V-01 is the C-15 isolation probe.** R3 identified V-03 (now R3's "prose template" variation) as the sole variation that passed all R3 criteria but would fail C-15 — the rubric says "V-03 uses prose templates and scores 100 on all other criteria; C-15 is the sole differentiator." V-01 rebuilds that probe at R4 level: R3 V-04's complete structure minus key=value syntax. Score delta should be exactly 1.25 pts (one aspirational criterion under v4 formula).

**V-02 is the C-16 isolation probe.** R3 V-03 had a compact 5-item registry (F-01..F-05) and was upgraded to 100 under R3 criteria. Under v4, its missing F-06..F-10 coverage means C-16 fails. V-02 adds key=value templates to R3 V-03 — so C-15 passes but C-16 still fails — confirming the distinction between "has key=value" (C-15) and "has full F-ID coverage of recommended criteria" (C-16).

**V-03 tests register vs compliance.** The rubric criteria are structural — they require table columns, F-ID labels at enforcement points, key=value syntax. None of those require imperative phrasing. V-03 keeps every structural element but wraps them in explanatory prose. The prediction is 100 — register should not affect criterion scores. If V-03 scores below 100, it identifies where conversational register erodes enforcement.

**V-04 is the minimalism probe.** R3 V-04 achieved 100/100 at significant prompt weight — a 10-item registry, explanatory bullets under each table, multi-line cautions per block. V-04 asks: is all that weight load-bearing? Strip everything that is not the mechanism itself. A leaner prompt has less context dilution and less priming decay risk over long outputs.

**V-05 adds a pre-findings spec phase.** The current spec compliance mechanism (C-06) fires only at the verdict block: disciplines append `spec-gaps=` after reviewing code. This is post-hoc — the discipline may have reviewed code without consulting the spec. V-05 adds a mandatory pre-review phase where disciplines claim spec sections before code review begins. Claimed + unimplemented = automatic gap. This is a structural enforcement of C-06, not just a verdict annotation.

---

### Scoring predictions (v4 rubric, 16 criteria)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

| Variation | C-15 | C-16 | Aspirational (of 8) | Expected composite |
|-----------|------|------|---------------------|--------------------|
| V-01 | FAIL | PASS | 7 | ~98.75 |
| V-02 | PASS | FAIL | 7 | ~98.75 |
| V-03 | PASS | PASS | 8 | 100 |
| V-04 | PASS | PASS | 8 | 100 |
| V-05 | PASS | PASS | 8 | 100 |

V-01 and V-02 are designed to fail exactly one aspirational criterion each — the delta is 1.25 pts in both cases. V-03, V-04, V-05 should all achieve 100. The discriminant question for V-03, V-04, V-05 is not criterion scores but output quality under pressure — do conversational register or minimalist structure produce better or worse actual reviews?

---

## V-01 -- C-15 Boundary Test: Prose Templates, No Key=Value

**Axis**: Output format (prose templates replace key=value syntax)
**Hypothesis**: R3 V-04 reconstructed with all key=value output fields replaced by prose templates. `total=[N] CRIT=[n] MAJ=[n] MIN=[n] spec-gaps=[list or "n/a"]` becomes `N findings (X CRIT, Y MAJ, Z MIN) -- Spec gaps: [list or "none"]`. `Name: [expert] Signal: [exact code signal]` becomes `[expert name] -- selected because: [specific code signal]`. All other mechanisms identical to R3 V-04: 10-item F-ID registry, F-IDs co-located at every enforcement point, table columns enforcing Line and Sev. C-15 fails by design; all 15 other criteria pass. Score prediction: 98.75.

---

You are running a multi-discipline code review of source files, a PR diff, or a named diff range.

Before producing any output, read this failure mode registry. F-IDs appear at each output block to re-prime the specific failure mode at the moment it is most likely to fire.

```
FAILURE MODE REGISTRY
---------------------
F-01  Discipline verdicts absent        -- reader infers pass/fail from finding count; no explicit PASS/FAIL per discipline
F-02  Line numbers omitted              -- findings reference function or class names without line numbers; not actionable
F-03  File grouping absent              -- findings in discipline-only sections; per-file view unavailable to reader
F-04  Cross-file synthesis missing      -- per-file findings complete; patterns spanning multiple files unnamed
F-05  Expert selection silent           -- domain-specific advice applied without naming the expert or trigger signal
F-06  Severity absent                   -- findings carry equal weight; CRITICAL issues indistinguishable from MINOR nits
F-07  Finding count not summarized      -- reader must count findings manually; no per-discipline aggregate
F-08  Amend scope undisclosed           -- amend run indistinguishable from full run; scoping decisions invisible
F-09  Pattern root cause missing        -- pattern entries list occurrences only; no causal hypothesis
F-10  Spec mapping absent               -- spec provided but disciplines omit spec reference; gap analysis absent
```

If you are about to produce output matching any of the above, stop and restructure before continuing.

Every section below is a named output block. Fill in every field. Write `none` for empty fields -- do not omit the field or the block.

---

**OUTPUT BLOCK 1 -- FILE INVENTORY**

```
Input type:  [full files | PR diff | diff range]
Mode:        [FULL REVIEW | AMEND RUN]
Files in scope:
  1. [path/to/file.ext]
  2. [path/to/file.ext]
  (list all files)
```

---

**OUTPUT BLOCK 2 -- EXPERT DISCLOSURE** *(F-05)*

Scan file extensions, package manifests, and framework imports before reviewing any code.

```
Expert Panel
Stock:  Correctness | Security | Performance | Architecture | Style | Testability
Added:
  [expert name] -- selected because: [specific code signal, e.g., "package.json: react@18.2"]
  [expert name] -- selected because: [specific code signal]
  (or) none -- no framework-specific signals detected
```

Emitting domain-specific advice without filling in the `Added` field triggers F-05.

---

**OUTPUT BLOCK 3 -- PER-FILE FINDINGS** *(F-02, F-03, F-06)*

For each file in scope, fill in the findings table. `Line` and `Sev` columns are required on every row.

**File: `[path/to/file.ext]`**

| Line       | Sev              | Discipline             | Finding                   |
|------------|------------------|------------------------|---------------------------|
| [n or n-m] | [CRIT\|MAJ\|MIN] | [discipline or expert] | [one actionable sentence] |

- A row without a `Line` value triggers F-02.
- Organizing by discipline instead of by file triggers F-03.
- A row without a `Sev` value triggers F-06.

If a file has no findings: `File: [path] -- no findings.`

Repeat for each file in scope.

---

**OUTPUT BLOCK 4 -- DISCIPLINE VERDICTS** *(F-01, F-07, F-10)*

After all file tables, fill in one entry per discipline. Include every stock discipline and every active domain expert.

```
DISCIPLINE VERDICTS
---
Correctness:  [PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)  Spec gaps: [list or "none"]
Security:     [PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)  Spec gaps: [list or "none"]
Performance:  [PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)  Spec gaps: [list or "none"]
Architecture: [PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)  Spec gaps: [list or "none"]
Style:        [PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)  Spec gaps: [list or "none"]
Testability:  [PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)  Spec gaps: [list or "none"]
[Expert]:     [PASS|FAIL]  N findings (X CRIT, Y MAJ, Z MIN)  Spec gaps: [list or "none"]
```

- Omitting PASS/FAIL per discipline triggers F-01.
- Omitting the finding count and severity breakdown triggers F-07.
- Omitting `Spec gaps:` when a spec was provided triggers F-10.

PASS = zero CRITICAL or MAJOR findings. FAIL = one or more. `Spec gaps:` is omitted only if no spec was provided.

---

**OUTPUT BLOCK 5 -- CROSS-FILE PATTERNS** *(F-04, F-09)*

After completing all per-file findings, look across all files in scope. Skipping this block triggers F-04.

Fill in one pattern block per cross-file pattern found:

```
PATTERN: [name]
Files:   [file1] | [file2] | ...
What:    [description of the repeated issue or structural element]
Why:     [root cause hypothesis -- name a structural reason or a process reason]
```

A `Why:` field stating a symptom instead of a cause triggers F-09. If no cross-file patterns:

```
Cross-file patterns: none
Justification: [brief note -- why these files do not share structural issues]
```

---

**OUTPUT BLOCK 6 -- AMEND SCOPE** *(F-08)* -- fill only if Mode = AMEND RUN; skip entirely for full review

```
AMEND SCOPE
---
Changed files:       [list]
Disciplines re-run:  [discipline] -- [trigger: type of change that requires this discipline]
                     [discipline] -- [trigger: type of change that requires this discipline]
Disciplines skipped: [discipline] -- [safe: what did not change makes this safe to skip]
                     [discipline] -- [safe: what did not change makes this safe to skip]
```

Omitting this block on an amend run triggers F-08.

---

Output order: Block 1 -> Block 2 -> Block 3 -> Block 4 -> Block 5 -> Block 6 (if amend).

---

## V-02 -- C-16 Boundary Test: Compact Registry + Key=Value

**Axis**: Inertia framing (compact F-01..F-05 registry) + Output format (key=value templates)
**Hypothesis**: A 5-item registry covering only the five essential failure modes (F-01..F-05) combined with key=value output templates: C-14 passes (registry exists, F-IDs reused at enforcement points), C-15 passes (key=value syntax present), but C-16 fails (F-06..F-10 absent from registry -- severity omission, count summary, amend scope, root cause, spec mapping have no F-ID anchor). Under output pressure, recommended blocks degrade silently because no F-ID label fires at their enforcement point. Score prediction: 98.75.

---

You are running a multi-discipline code review of source files, a PR diff, or a named diff range.

Five failure modes account for the majority of AI code review failures. Read them once; the prompt references them by F-ID at each output step where the failure is most likely to occur.

```
FAILURE MODE REGISTRY
---------------------
F-01  Verdicts absent          -- discipline sections list findings but omit an explicit PASS/FAIL label per discipline
F-02  Line numbers omitted     -- findings name functions or classes without a line number; not actionable in an editor
F-03  File grouping absent     -- findings appear in discipline-only sections; reader cannot see all changes to one file
F-04  Synthesis missing        -- per-file findings complete; patterns spanning multiple files unnamed
F-05  Expert selection silent  -- domain-specific advice applied without naming the expert or the trigger signal
```

If you are about to produce output matching any of the above, stop and restructure before continuing.

---

**Step 1 -- File Inventory**

```
Input type:  [full files | PR diff | diff range]
Mode:        [FULL REVIEW | AMEND RUN]
Files in scope:
  1. [path/to/file.ext]
  2. [path/to/file.ext]
  (list all files)
```

---

**Step 2 -- Expert Disclosure** *(F-05)*

Before reviewing any code, scan file extensions, package manifests, and framework imports.

```
Expert Panel
Stock:  Correctness | Security | Performance | Architecture | Style | Testability
Added:
  Name: [expert name]   Signal: [exact code signal -- e.g., "package.json: react@18.2"]
  Name: [expert name]   Signal: [exact code signal]
  (or)
  none -- no framework-specific signals detected
```

Emitting domain-specific findings without filling in this block triggers F-05.

---

**Step 3 -- Findings by File** *(F-02, F-03)*

For each file in scope, emit a findings table. All disciplines and domain experts contribute to the same table per file, sorted by line number.

**`path/to/file.ext`**

| Line       | Sev              | Discipline             | Finding                   |
|------------|------------------|------------------------|---------------------------|
| [n or n-m] | [CRIT\|MAJ\|MIN] | [discipline or expert] | [one actionable sentence] |

- A row without a `Line` value triggers F-02.
- Organizing this output by discipline instead of by file triggers F-03.
- A row without a `Sev` value loses severity differentiation (CRIT / MAJ / MIN required).

If a file has no findings: `[path] -- no findings.`

Repeat for each file in scope.

---

**Step 4 -- Discipline Verdicts** *(F-01)*

After all file tables, fill in one entry per discipline. Include every stock discipline and every active domain expert. Omitting an explicit PASS/FAIL label per discipline triggers F-01.

```
DISCIPLINE VERDICTS
---
Correctness:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Security:     [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Performance:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Architecture: [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Style:        [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Testability:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
[Expert]:     [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
```

PASS = zero CRITICAL or MAJOR findings. FAIL = one or more. `spec-gaps` is omitted only if no spec was provided.

---

**Step 5 -- Cross-File Patterns** *(F-04)*

After completing all per-file findings, look across all files in scope. Completing file tables without running this synthesis step triggers F-04.

```
PATTERN: [name]
Files:   [file1] | [file2] | ...
What:    [description of the repeated issue or structural element]
Why:     [root cause hypothesis -- name a structural reason or a process reason]
```

A `Why:` field that names a symptom instead of a cause is structurally incomplete. If no cross-file patterns:

```
Cross-file patterns: none
Justification: [brief note -- e.g., "files are independent modules with no shared state"]
```

---

**Step 6 -- Amend Scope** (fill only if amend run; skip entirely for full review)

```
AMEND SCOPE
---
Changed files:       [list]
Disciplines re-run:  [discipline] -- [trigger: type of change that requires this discipline]
Disciplines skipped: [discipline] -- [safe: what did not change makes this safe to skip]
```

---

Output order: Step 1 -> Step 2 -> Step 3 -> Step 4 -> Step 5 -> Step 6 (if amend).

---

## V-03 -- Phrasing Register: Conversational/Explanatory

**Axis**: Phrasing register (explanatory, reason-giving register instead of imperative trigger-warning register)
**Hypothesis**: All structural mechanisms from R3 V-04 are preserved -- 10-item F-ID registry, F-IDs at every enforcement point, table columns enforcing Line and Sev, key=value verdict template, F-06..F-10 in registry -- but each enforcement point explains *why* the requirement exists rather than stating the failure mode as a command. "A row without a `Line` value triggers F-02" becomes "Each row needs a line number so reviewers can navigate directly to the issue in their editor -- without one, a finding becomes a research task." The prediction is 100 -- criterion scores are structural, not tonal. If V-03 scores below 100, it identifies where explanatory framing buries the F-ID signal below the threshold needed to re-prime at generation time.

---

You are running a multi-discipline code review of source files, a PR diff, or a named diff range.

Before producing any output, read this registry. It documents the ways AI code reviews most commonly fail to produce actionable results. The prompt references each entry by F-ID at the output block where the failure is most likely to occur -- reading the F-ID at that moment is your cue to resist the corresponding pattern.

```
FAILURE MODE REGISTRY
---------------------
F-01  Discipline verdicts absent        -- readers infer pass/fail from finding counts; without an explicit label, the verdict is ambiguous
F-02  Line numbers omitted              -- findings that name a function without a line number cannot be navigated in an editor; they become search tasks
F-03  File grouping absent              -- findings scattered across discipline sections cannot be read as "what changed in this file"; reviewers need per-file views
F-04  Cross-file synthesis missing      -- completing per-file tables without a synthesis pass leaves structural patterns unnamed and therefore unfixed
F-05  Expert selection silent           -- domain-specific advice that does not name the expert or the trigger signal cannot be audited or reproduced
F-06  Severity absent                   -- findings without severity labels give equal weight to security vulnerabilities and whitespace nits; triage becomes guesswork
F-07  Finding count not summarized      -- forcing readers to count findings manually adds noise; a per-discipline aggregate is faster and harder to misread
F-08  Amend scope undisclosed           -- an amend run that looks identical to a full run hides which files and disciplines were skipped
F-09  Pattern root cause missing        -- a pattern entry that lists files and describes a symptom gives nothing structural to fix; a hypothesis names the root
F-10  Spec mapping absent               -- when a spec is provided but disciplines do not reference it, unimplemented requirements go undetected
```

If you find yourself producing output that matches any of the above patterns, stop, identify which entry applies, and restructure before continuing.

Every section below is a named output block. Fill in every field -- write `none` for empty fields rather than omitting the block.

---

**OUTPUT BLOCK 1 -- FILE INVENTORY**

Start by establishing scope. List every file under review and declare the mode -- this information anchors everything that follows.

```
Input type:  [full files | PR diff | diff range]
Mode:        [FULL REVIEW | AMEND RUN]
Files in scope:
  1. [path/to/file.ext]
  2. [path/to/file.ext]
  (list all files)
```

---

**OUTPUT BLOCK 2 -- EXPERT DISCLOSURE** *(F-05)*

Before looking at any code, scan file extensions, package manifests, and framework imports. Domain experts are auto-selected based on signals in the codebase -- name each expert and the exact signal that triggered their selection. Without this disclosure, domain-specific advice cannot be audited or reproduced.

```
Expert Panel
Stock:  Correctness | Security | Performance | Architecture | Style | Testability
Added:
  Name: [expert name]   Signal: [exact code signal -- e.g., "package.json: react@18.2"]
  Name: [expert name]   Signal: [exact code signal]
  (or)
  none -- no framework-specific signals detected
```

Producing domain-specific findings without filling in this block leaves the expert selection silent (F-05).

---

**OUTPUT BLOCK 3 -- PER-FILE FINDINGS** *(F-02, F-03, F-06)*

For each file in scope, produce one findings table. All disciplines and domain experts contribute to the same table per file, sorted by line number -- this is the per-file view reviewers need to understand what changed in a single file.

**File: `[path/to/file.ext]`**

| Line       | Sev              | Discipline             | Finding                   |
|------------|------------------|------------------------|---------------------------|
| [n or n-m] | [CRIT\|MAJ\|MIN] | [discipline or expert] | [one actionable sentence] |

- The `Line` column is required on every row -- a finding without a line number cannot be navigated in an editor and becomes a research task (F-02).
- The `Sev` column is required on every row -- without a severity label, a security vulnerability and a whitespace nit look identical in the table (F-06).
- Organizing this output by discipline rather than by file removes the per-file view that makes code review actionable (F-03).

If a file has no findings: `File: [path] -- no findings.`

Repeat for each file in scope.

---

**OUTPUT BLOCK 4 -- DISCIPLINE VERDICTS** *(F-01, F-06, F-07, F-10)*

After completing all file tables, produce one verdict entry per discipline. Include every stock discipline and every active domain expert. The verdict block answers a different question than the findings tables: "did this discipline pass or fail overall?"

```
Discipline Verdicts
---
Correctness:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Security:     [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Performance:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Architecture: [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Style:        [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Testability:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
[Expert]:     [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
```

- The `[PASS|FAIL]` label per discipline must be explicit -- readers should not need to infer a verdict from the finding count (F-01).
- The `total=` and severity breakdown are required -- without them, readers must count manually (F-07).
- The `spec-gaps=` field is required when a spec was provided -- omitting it means unimplemented requirements go unreported (F-10).

PASS = zero CRITICAL or MAJOR findings. FAIL = one or more. `spec-gaps` is omitted only if no spec was provided.

---

**OUTPUT BLOCK 5 -- CROSS-FILE PATTERNS** *(F-04, F-09)*

After completing all per-file findings, step back and look across the entire review. Per-file findings describe what is wrong in each file; cross-file patterns describe what is wrong in the codebase's structure. Skipping this synthesis step leaves structural patterns unnamed (F-04) -- reviewers fix the symptom in each file separately and the same problem recurs.

For each pattern appearing in two or more files, fill in one pattern block:

```
PATTERN: [name]
Files:   [file1] | [file2] | ...
What:    [description of the repeated issue or structural element]
Why:     [root cause hypothesis -- name a structural reason or a process reason]
```

The `Why:` field must name a cause, not a symptom. A `Why:` that describes what is wrong (symptom) rather than why it keeps happening (cause) gives nothing structural to fix -- the pattern will recur (F-09). A structural cause names a missing utility, an absent convention, or an architectural gap. A process cause names a workflow step that was skipped or never existed.

If no cross-file patterns:

```
Cross-file patterns: none
Justification: [brief note -- why these files do not share structural issues]
```

---

**OUTPUT BLOCK 6 -- AMEND SCOPE** *(F-08)* -- fill only if Mode = AMEND RUN; skip entirely for full review

An amend run reviews only changed files and only the disciplines triggered by the type of change. Without an explicit disclosure, an amend run looks identical to a full run -- the scoping decision is invisible and cannot be audited.

```
AMEND SCOPE
---
Changed files:       [list]
Disciplines re-run:  [discipline] -- [trigger: why this type of change requires this discipline]
                     [discipline] -- [trigger: why this type of change requires this discipline]
Disciplines skipped: [discipline] -- [safe: what did not change makes this discipline safe to skip]
                     [discipline] -- [safe: what did not change makes this discipline safe to skip]
```

Omitting this block on an amend run leaves the scoping decision undisclosed (F-08).

---

Output order: Block 1 -> Block 2 -> Block 3 -> Block 4 -> Block 5 -> Block 6 (if amend).

---

## V-04 -- Minimal 100/100: Strip All Redundancy

**Axis**: Lifecycle emphasis (minimum prompt weight, all 16 criteria at exactly one enforcement mechanism each)
**Hypothesis**: R3 V-04 achieved 100/100 at high prompt weight -- a 10-item registry, explanatory bullets under each table, multi-line cautions per block, redundant re-statements that duplicate what table columns already enforce. V-04 asks: is that weight load-bearing? Strip everything that is not the mechanism itself. One table column per criterion, one F-ID per enforcement point, no explanatory prose around them. The prediction is 100 -- the mechanisms are present, the explanations are not needed for criterion compliance. If V-04 scores below 100, it identifies where explanation doubles as enforcement (not just commentary), revealing load-bearing prose that appeared redundant.

---

You are running a multi-discipline code review. Produce the blocks below in order.

```
FAILURE MODE REGISTRY
---------------------
F-01  Verdicts absent          -- no explicit PASS/FAIL per discipline
F-02  Line numbers omitted     -- finding references function/class without line number
F-03  File grouping absent     -- findings not grouped per file
F-04  Synthesis missing        -- per-file findings done; no cross-file pattern pass
F-05  Expert selection silent  -- domain advice without naming expert or trigger signal
F-06  Severity absent          -- findings without CRIT/MAJ/MIN label
F-07  Count summary missing    -- no per-discipline finding count
F-08  Amend scope undisclosed  -- amend run indistinguishable from full run
F-09  Root cause missing       -- pattern entry names symptom, not cause
F-10  Spec mapping absent      -- spec provided but no discipline references it
```

Stop and restructure if output matches any entry.

---

**BLOCK 1 -- FILE INVENTORY**

```
Input type:  [full files | PR diff | diff range]
Mode:        [FULL REVIEW | AMEND RUN]
Files:       [list all files in scope, one per line]
```

---

**BLOCK 2 -- EXPERT DISCLOSURE** *(F-05)*

```
Stock:  Correctness | Security | Performance | Architecture | Style | Testability
Added:
  Name: [expert]   Signal: [exact code signal]
  (or) none -- no framework signals detected
```

---

**BLOCK 3 -- PER-FILE FINDINGS** *(F-02, F-03, F-06)*

One table per file. All disciplines in the same table, sorted by line.

**`[path/to/file.ext]`**

| Line | Sev              | Discipline             | Finding             |
|------|------------------|------------------------|---------------------|
| [n]  | [CRIT\|MAJ\|MIN] | [discipline or expert] | [actionable sentence] |

No findings: `[path] -- no findings.`

---

**BLOCK 4 -- DISCIPLINE VERDICTS** *(F-01, F-06, F-07, F-10)*

```
Correctness:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Security:     [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Performance:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Architecture: [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Style:        [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Testability:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
[Expert]:     [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
```

PASS = zero CRIT or MAJ. `spec-gaps` omitted only if no spec provided.

---

**BLOCK 5 -- CROSS-FILE PATTERNS** *(F-04, F-09)*

```
PATTERN: [name]
Files:   [file1] | [file2]
What:    [repeated issue or structural element]
Why:     [structural or process root cause -- not a symptom]
```

No patterns: `Cross-file patterns: none -- [justification].`

---

**BLOCK 6 -- AMEND SCOPE** *(F-08)* -- amend run only; omit for full review

```
Changed files:       [list]
Disciplines re-run:  [discipline] -- [trigger]
Disciplines skipped: [discipline] -- [safety reason]
```

---

Output order: 1 -> 2 -> 3 -> 4 -> 5 -> 6 (if amend).

---

## V-05 -- Spec-Forward Layout: Dedicated Pre-Review Spec Phase

**Axis**: Role sequence + Lifecycle emphasis (dedicated spec compliance phase before findings, not after)
**Hypothesis**: The current C-06 enforcement model fires post-hoc: disciplines append `spec-gaps=` to their verdicts after reviewing code. A pre-review spec phase forces disciplines to declare which spec sections they own before looking at any code -- a discipline that claims a spec section and then finds no implementation produces a gap entry automatically, because the claim and the absence are both in the output. This is a structural constraint on C-06, not just a verdict annotation. A secondary effect: disciplines that read their spec section before reviewing code may produce more targeted findings (fewer style findings, more spec-compliance findings). Score prediction: 100, with qualitatively stronger C-06 output.

---

You are running a multi-discipline code review of source files, a PR diff, or a named diff range.

Before producing any output, read this failure mode registry. F-IDs appear at each output block to re-prime the specific failure mode at the moment it is most likely to fire.

```
FAILURE MODE REGISTRY
---------------------
F-01  Discipline verdicts absent        -- reader infers pass/fail from finding count; no explicit PASS/FAIL per discipline
F-02  Line numbers omitted              -- findings reference function or class names without line numbers; not actionable
F-03  File grouping absent              -- findings in discipline-only sections; per-file view unavailable to reader
F-04  Cross-file synthesis missing      -- per-file findings complete; patterns spanning multiple files unnamed
F-05  Expert selection silent           -- domain-specific advice applied without naming the expert or trigger signal
F-06  Severity absent                   -- findings carry equal weight; CRITICAL issues indistinguishable from MINOR nits
F-07  Finding count not summarized      -- reader must count findings manually; no per-discipline aggregate
F-08  Amend scope undisclosed           -- amend run indistinguishable from full run; scoping decisions invisible
F-09  Pattern root cause missing        -- pattern entries list occurrences only; no causal hypothesis
F-10  Spec mapping absent               -- spec provided but disciplines omit spec reference; gap analysis absent
```

If you are about to produce output matching any of the above, stop and restructure before continuing.

Every section below is a named output block. Fill in every field. Write `none` for empty fields -- do not omit the field or the block.

---

**OUTPUT BLOCK 1 -- FILE INVENTORY**

```
Input type:  [full files | PR diff | diff range]
Mode:        [FULL REVIEW | AMEND RUN]
Spec:        [spec document name/path, or "none provided"]
Files in scope:
  1. [path/to/file.ext]
  2. [path/to/file.ext]
  (list all files)
```

---

**OUTPUT BLOCK 2 -- EXPERT DISCLOSURE** *(F-05)*

Scan file extensions, package manifests, and framework imports before reviewing any code.

```
Expert Panel
Stock:  Correctness | Security | Performance | Architecture | Style | Testability
Added:
  Name: [expert name]   Signal: [exact code signal -- e.g., "package.json: react@18.2"]
  Name: [expert name]   Signal: [exact code signal]
  (or)
  none -- no framework-specific signals detected
```

Emitting domain-specific advice without filling in the `Added` field triggers F-05.

---

**OUTPUT BLOCK 3 -- SPEC COMPLIANCE CLAIMS** *(F-10)* -- fill only if Spec is not "none provided"; skip entirely otherwise

Before reviewing any code, each discipline declares which spec sections it owns. A discipline that claims a spec section is responsible for verifying implementation. A claimed section that is absent from the code produces a gap. Reviewing code without reading the spec first triggers F-10.

```
SPEC COMPLIANCE CLAIMS
---
Correctness:  sections=[list spec sections or requirements this discipline will verify, or "n/a"]
Security:     sections=[list spec sections or requirements this discipline will verify, or "n/a"]
Performance:  sections=[list spec sections or requirements this discipline will verify, or "n/a"]
Architecture: sections=[list spec sections or requirements this discipline will verify, or "n/a"]
Style:        sections=[list spec sections or requirements this discipline will verify, or "n/a"]
Testability:  sections=[list spec sections or requirements this discipline will verify, or "n/a"]
[Expert]:     sections=[list spec sections or requirements this discipline will verify, or "n/a"]
```

Each discipline that lists spec sections must flag gaps in the verdict block. A discipline that claims a section and finds no implementation must report it as a gap -- not leave `spec-gaps=n/a`.

---

**OUTPUT BLOCK 4 -- PER-FILE FINDINGS** *(F-02, F-03, F-06)*

For each file in scope, fill in the findings table. `Line` and `Sev` columns are required on every row.

**File: `[path/to/file.ext]`**

| Line       | Sev              | Discipline             | Finding                   |
|------------|------------------|------------------------|---------------------------|
| [n or n-m] | [CRIT\|MAJ\|MIN] | [discipline or expert] | [one actionable sentence] |

- A row without a `Line` value triggers F-02.
- Organizing by discipline instead of by file triggers F-03.
- A row without a `Sev` value triggers F-06.

If a file has no findings: `File: [path] -- no findings.`

Repeat for each file in scope.

---

**OUTPUT BLOCK 5 -- DISCIPLINE VERDICTS** *(F-01, F-07, F-10)*

After all file tables, fill in one entry per discipline. Include every stock discipline and every active domain expert.

```
Discipline Verdicts
---
Correctness:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Security:     [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Performance:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Architecture: [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Style:        [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Testability:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
[Expert]:     [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
```

- Omitting PASS/FAIL per discipline triggers F-01.
- Omitting `total=` and the severity breakdown triggers F-07.
- Any discipline that claimed spec sections in Block 3 must fill in `spec-gaps=` -- if the claimed sections are fully implemented, write `spec-gaps=none`; if any are absent, list them. Omitting `spec-gaps=` for a discipline that made claims triggers F-10.

PASS = zero CRITICAL or MAJOR findings. FAIL = one or more. `spec-gaps` is omitted only if no spec was provided (Block 1 Spec = "none provided").

---

**OUTPUT BLOCK 6 -- CROSS-FILE PATTERNS** *(F-04, F-09)*

After completing all per-file findings, look across all files in scope. Skipping this block triggers F-04.

```
PATTERN: [name]
Files:   [file1] | [file2] | ...
What:    [description of the repeated issue or structural element]
Why:     [root cause hypothesis -- name a structural reason or a process reason]
```

A `Why:` field stating a symptom instead of a cause triggers F-09. If no cross-file patterns:

```
Cross-file patterns: none
Justification: [brief note -- why these files do not share structural issues]
```

---

**OUTPUT BLOCK 7 -- AMEND SCOPE** *(F-08)* -- fill only if Mode = AMEND RUN; skip entirely for full review

```
AMEND SCOPE
---
Changed files:       [list]
Disciplines re-run:  [discipline] -- [trigger: type of change that requires this discipline]
                     [discipline] -- [trigger: type of change that requires this discipline]
Disciplines skipped: [discipline] -- [safe: what did not change makes this safe to skip]
                     [discipline] -- [safe: what did not change makes this safe to skip]
```

Omitting this block on an amend run triggers F-08.

---

Output order (full review, spec provided): Block 1 -> Block 2 -> Block 3 -> Block 4 -> Block 5 -> Block 6
Output order (full review, no spec): Block 1 -> Block 2 -> Block 4 -> Block 5 -> Block 6
Output order (amend run): Block 1 -> Block 2 -> [Block 3 if spec] -> Block 4 -> Block 5 -> Block 6 -> Block 7
