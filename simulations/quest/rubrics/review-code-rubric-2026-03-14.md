Rubric written to `simulations/quest/rubrics/review-code-rubric-2026-03-14.md`.

**Structure:**

**Essential (5 criteria, 60 pts):**
- C-01 — 6 disciplines with explicit PASS/FAIL verdicts
- C-02 — Every finding has `file:line` annotation
- C-03 — Findings grouped by file
- C-04 — At least one cross-file pattern identified and labeled
- C-05 — Domain expert selection disclosed with signal used

**Recommended (3 criteria, 30 pts):**
- C-06 — Spec compliance mapped per discipline (when spec provided)
- C-07 — Severity label (CRITICAL/MAJOR/MINOR) on every finding
- C-08 — Finding count summary per discipline with severity breakdown

**Aspirational (2 criteria, 10 pts):**
- C-09 — Amend mode scoping disclosed (which disciplines re-run vs. skipped)
- C-10 — Cross-file patterns include root cause hypothesis, not just occurrence list

The three essential structural properties of a useful code review are: actionable annotations (C-02), cross-discipline verdicts (C-01), and cross-file synthesis (C-04). A run that passes essential but not recommended is still useful — it has all the structure; it just lacks severity triage and spec traceability.
 path and line number in `file:line` or `file:start-end` format. Findings that reference only a function name, class, or file without a line number do not pass. Zero findings with no annotation is acceptable only if the discipline section explicitly states "no findings." |
| C-03 | Findings grouped by file | essential | format | Output contains one section or heading per reviewed file, and all findings for that file appear under it. Findings scattered in discipline-only sections without a file-grouping pass are a fail. A hybrid layout (per-discipline with file sub-grouping) passes if every finding appears under its source file within the discipline block. |
| C-04 | At least one cross-file pattern identified and labeled | essential | coverage | Output contains a dedicated patterns section or inline pattern callouts. Each pattern entry names at least two files where the pattern appears and describes what the pattern is (e.g., "error handling inconsistent across 4 files"). A run that lists per-file findings with no cross-file synthesis is a hard fail. |
| C-05 | Domain expert selection disclosed | essential | behavior | Output explicitly names which domain experts were auto-selected (e.g., "TypeScript expert, React patterns reviewer") and states the signal used to select them (e.g., "package.json contains react@18"). A run that applies domain experts without disclosure, or that applies no domain experts with no explanation, is a hard fail. |

---

## Recommended Criteria (30 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | Spec compliance mapped per discipline when spec is provided | recommended | correctness | When the input includes a spec document, each discipline section identifies which spec sections or requirements it checked and flags any gaps (spec requirement present but not implemented). A run on a specless input passes by default. A run on a spec-provided input that makes no spec references fails. |
| C-07 | Severity label on every finding | recommended | depth | Every individual finding carries a severity label: CRITICAL / MAJOR / MINOR or equivalent three-tier scale. Findings without labels are acceptable only if the discipline summary provides an aggregate count by severity and identifies which findings belong to which tier. A run with no severity differentiation at all fails. |
| C-08 | Finding count summary per discipline | recommended | format | Each discipline section includes a summary line stating total findings and the breakdown by severity (e.g., "3 findings: 1 CRITICAL, 2 MINOR"). The summary must appear as a distinct element — not require the reader to count findings manually. |

---

## Aspirational Criteria (10 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Amend mode scoping disclosed when run incrementally | aspirational | behavior | When run in amend mode (changed files only), output contains a disclosure block that names: (a) which files changed, (b) which disciplines were re-run, (c) which disciplines were skipped and why (e.g., "architecture: no structural files changed"). A run in full mode passes by default. An amend run with no scoping disclosure fails. |
| C-10 | Cross-file pattern entries include root cause hypothesis | aspirational | depth | Each identified pattern entry states a root cause hypothesis — not just a list of occurrences. The hypothesis must name a structural reason (e.g., "shared utility missing, each file implements its own version") or a process reason (e.g., "error handling added post-hoc, before style guide existed"). A pattern entry that only lists files and describes the symptom without a causal claim fails. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Common Failure Modes

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|
| — | C-01 | Discipline names appear in prose summary but no per-discipline PASS/FAIL verdict is emitted; reader must infer verdict from finding count |
| — | C-02 | Findings reference function names ("in `handleSubmit`") without line numbers; annotations look present but are not actionable without line context |
| — | C-03 | All findings appear in discipline sections; file grouping never materializes — reader must grep to find what changed in each file |
| — | C-04 | Per-file findings are complete and detailed, but no synthesis pass runs; patterns that span 3-4 files go unnamed |
| — | C-05 | Domain experts applied silently; output shows TypeScript-specific advice but never states that a TS expert was selected or why |
| — | C-06 | Spec provided but disciplines check only code quality; spec-to-code gap analysis absent even when requirements are unimplemented |
| — | C-07 | All findings listed at equal weight; CRITICAL security issues indistinguishable from MINOR style nits without severity labels |
| — | C-09 | Amend run re-checks all disciplines against all files; no disclosure of what changed or what was skipped — amend mode is indistinguishable from a full run |
