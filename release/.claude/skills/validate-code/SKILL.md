---
name: validate-code
description: "Multi-discipline code review of source files, PRs, or diffs. Per-discipline finding tables with file:line annotations. P1 blocks merge, P2 blocks ship, P3 advisory."
allowed-tools: [Read, Write, Glob, Grep]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


If --compact: run Security + Architecture reviewers only. 2 findings each. Verdict only.

Input type:  [full files | PR diff | diff range]
Mode:        [FULL REVIEW | AMEND RUN]
Files:       [list all files in scope, one per line]

---

## BLOCK 0 — DOMAIN SIGNAL SCAN

Scan the input for language, framework, and domain signals. List each signal found and the
reviewer discipline it activates.

| Signal | Detected value | Activated discipline |
|--------|---------------|----------------------|
| Language | [e.g., TypeScript, Python, Go] | [e.g., Language expert] |
| Framework | [e.g., React, Django, gRPC] | [e.g., Framework expert] |
| Auth/permissions pattern | [present / absent] | Security |
| Data persistence | [present / absent] | Architecture |
| Public API surface | [present / absent] | Documentation |

Spec provided: [YES — path: {spec_path} / NO]

If spec provided: each reviewer checks compliance against it. Note: spec compliance is an
additional lens, not a replacement for the standard lens.

---

## BLOCK 1 — REVIEWER ROSTER

Stock disciplines + any domain experts activated by BLOCK 0 signals.

| # | Reviewer | Focus |
|---|----------|-------|
| 1 | Security | Injection, auth, secrets exposure, input validation, unsafe deserialization |
| 2 | Performance | Hot paths, unnecessary allocations, N+1 queries, blocking calls |
| 3 | Maintainability | Naming clarity, function length, coupling, duplication, cyclomatic complexity |
| 4 | Testing | Coverage gaps, missing edge cases, test isolation, mock fidelity |
| 5 | Documentation | Public API docs, inline comments for non-obvious logic, error messages |
| 6 | Architecture | Layer violations, dependency direction, interface contracts, abstraction fitness |
| [7+] | [Domain expert — activated by BLOCK 0] | [domain-specific lens] |

Total reviewers: [N]

---

## BLOCK 1.5 — ROSTER COMMITMENT

Each reviewer commits before findings are written.

| Reviewer | Committed | Scope Note |
|----------|-----------|------------|
| Security | YES | All files in scope |
| Performance | YES | All files in scope |
| Maintainability | YES | All files in scope |
| Testing | YES | All files in scope |
| Documentation | YES | All files in scope |
| Architecture | YES | All files in scope |
| [Domain experts] | YES | [scope note if narrower] |

Reviewers SHALL NOT skip files because they appear simple or unchanged.

---

## BLOCK 2 — PER-REVIEWER FINDINGS

Each reviewer produces a findings table. Findings are annotated with file:line where applicable.
Group findings by file if multiple files are in scope.

Severity:
- P1 = blocks merge — must fix before this code lands
- P2 = must fix before ship — can merge to a feature branch but not to main/prod
- P3 = should fix — advisory; does not block merge or ship

---

### Security

| ID | File:Line | Finding | Severity | Fix |
|----|-----------|---------|----------|-----|
| SEC-01 | [file:line] | [finding] | [P1/P2/P3] | [concrete fix] |
| SEC-02 | [file:line] | [finding] | [P1/P2/P3] | [concrete fix] |
| ... | | | | |

Patterns identified: [e.g., "input validation absent in 3 handler functions — consistent gap"]
Spec compliance: [PASS / FAIL / N/A]

---

### Performance

| ID | File:Line | Finding | Severity | Fix |
|----|-----------|---------|----------|-----|
| PERF-01 | [file:line] | [finding] | [P1/P2/P3] | [concrete fix] |
| ... | | | | |

Patterns identified: [e.g., "synchronous I/O in async context — appears in 2 files"]
Spec compliance: [PASS / FAIL / N/A]

---

### Maintainability

| ID | File:Line | Finding | Severity | Fix |
|----|-----------|---------|----------|-----|
| MAINT-01 | [file:line] | [finding] | [P1/P2/P3] | [concrete fix] |
| ... | | | | |

Patterns identified: [e.g., "function length exceeds 50 lines in 4 of 7 files"]
Spec compliance: [PASS / FAIL / N/A]

---

### Testing

| ID | File:Line | Finding | Severity | Fix |
|----|-----------|---------|----------|-----|
| TEST-01 | [file:line] | [finding] | [P1/P2/P3] | [concrete fix] |
| ... | | | | |

Patterns identified: [e.g., "happy path only — error branches untested across module"]
Spec compliance: [PASS / FAIL / N/A]

---

### Documentation

| ID | File:Line | Finding | Severity | Fix |
|----|-----------|---------|----------|-----|
| DOC-01 | [file:line] | [finding] | [P1/P2/P3] | [concrete fix] |
| ... | | | | |

Patterns identified: [if any]
Spec compliance: [PASS / FAIL / N/A]

---

### Architecture

| ID | File:Line | Finding | Severity | Fix |
|----|-----------|---------|----------|-----|
| ARCH-01 | [file:line] | [finding] | [P1/P2/P3] | [concrete fix] |
| ... | | | | |

Patterns identified: [if any]
Spec compliance: [PASS / FAIL / N/A]

---

### [Domain Expert — if activated]

| ID | File:Line | Finding | Severity | Fix |
|----|-----------|---------|----------|-----|
| DOM-01 | [file:line] | [finding] | [P1/P2/P3] | [concrete fix] |
| ... | | | | |

Patterns identified: [if any]
Spec compliance: [PASS / FAIL / N/A]

---

## BLOCK 3 — SYNTHESIS AND VERDICT

### Finding Summary

| Severity | Count | Top finding |
|----------|-------|-------------|
| P1 | [N] | [most critical P1 — one sentence] |
| P2 | [N] | [most critical P2] |
| P3 | [N] | [highest-value P3] |
| Total | [N] | |

### Cross-cutting patterns

[Any finding that appears across 2+ disciplines or 2+ files. Name it, quantify it ("3 of 5
files"), and name the discipline that owns the fix. If none: "No cross-cutting patterns detected."]

### Spec compliance summary

[If spec was provided: overall compliance verdict — PASS / CONDITIONAL / FAIL. List which
disciplines failed and what deviations were found. If no spec: "No spec provided."]

### Verdict

[MERGE-READY / CONDITIONAL / BLOCKED]

- MERGE-READY: P1 count = 0
- CONDITIONAL: P1 count = 0 AND P2 count > 0 (must fix before ship, can merge to feature branch)
- BLOCKED: P1 count > 0

Verdict rationale: [One sentence. Name the highest-severity finding that drives the verdict.]

---

## AMEND

AMEND mode: re-run affected disciplines on changed files only.

Changed files: [list files changed since last review]
Disciplines re-run: [list disciplines with findings in changed files]
Findings resolved: [list IDs resolved in this amend run]
Findings added: [list new findings discovered]
Verdict: [updated verdict after amend]

---

Write artifact to: signals/validate/code/{topic}-code-{date}.md

Frontmatter:
```
skill: validate-code
topic: {topic}
date: {date}
reviewer_count: {N}
p1_count: {N}
p2_count: {N}
p3_count: {N}
```
