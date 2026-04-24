Written to `simulations/quest/rubrics/review-code-rubric-v2-2026-03-14.md`.

---

**What changed from v1:**

**C-11 — At least two compliance-sensitive criteria are format-encoded** *(aspirational / format)*

Drawn from V-02 and V-05. Both scored 90 — and both achieved C-02/C-07/C-08 as PASS because table columns and named field blocks made omission structurally impossible rather than merely prohibited. V-03 failed all three of those criteria using the same *requirements* stated in prose form. The delta isn't what is required; it's how it's enforced. A `File:Line` table column cannot produce a finding without a location. Prose cannot make the same guarantee under output pressure.

**C-12 — Inertia framing names at least two known failure modes** *(aspirational / behavior)*

Drawn from V-05 exclusively. V-05 is the only variant that named its own failure modes ("one of three things naive reviews leave out," "silent expert selection explicitly named as one of three naive-review failures"). The scorecard attributes C-05's reliable pass in V-05 partly to this priming — the model is told what the failure looks like before it fires. This is distinct from C-11 (structural encoding): inertia framing works on behaviors that are hard to format-encode, like expert disclosure phrasing or synthesis depth.

**Scoring formula update**: `aspirational_pass / 4 * 10` (was `/ 2 * 10`). Essential+recommended ceiling stays at 90, so the 80-pt golden threshold remains reachable without any aspirational passes.
tion name, class, or file without a line number do not pass. Zero findings with no annotation is acceptable only if the discipline section explicitly states "no findings." |
| C-03 | Findings grouped by file | essential | format | Output contains one section or heading per reviewed file, and all findings for that file appear under it. Findings scattered in discipline-only sections without a file-grouping pass are a fail. A hybrid layout (per-discipline with file sub-grouping) passes if every finding appears under its source file within the discipline block. |
| C-04 | At least one cross-file pattern identified and labeled | essential | coverage | Output contains a dedicated patterns section or inline pattern callouts. Each pattern entry names at least two files where the pattern appears and describes what the pattern is (e.g., "error handling inconsistent across 4 files"). A run that lists per-file findings with no cross-file synthesis is a hard fail. |
| C-05 | Domain expert selection disclosed with signal used | essential | behavior | Output explicitly names which domain experts were auto-selected (e.g., "TypeScript expert, React patterns reviewer") and states the signal used to select them (e.g., "package.json contains react@18"). A run that applies domain experts without disclosure, or that applies no domain experts with no explanation, is a hard fail. |

---

## Recommended Criteria (30 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | Spec compliance mapped per discipline when spec is provided | recommended | correctness | When the input includes a spec document, each discipline section identifies which spec sections or requirements it checked and flags any gaps (spec requirement present but not implemented). A run on a specless input passes by default. A run on a spec-provided input that makes no spec references fails. |
| C-07 | Severity label on every finding | recommended | depth | Every individual finding carries a severity label: CRITICAL / MAJOR / MINOR or equivalent three-tier scale. Findings without labels are acceptable only if the discipline summary provides an aggregate count by severity and identifies which findings belong to which tier. A run with no severity differentiation at all fails. |
| C-08 | Finding count summary per discipline with severity breakdown | recommended | format | Each discipline section includes a summary line stating total findings and the breakdown by severity (e.g., "3 findings: 1 CRITICAL, 2 MINOR"). The summary must appear as a distinct element — not require the reader to count findings manually. |

---

## Aspirational Criteria (10 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Amend mode scoping disclosed when run incrementally | aspirational | behavior | When run in amend mode (changed files only), output contains a disclosure block that names: (a) which files changed, (b) which disciplines were re-run, (c) which disciplines were skipped and why (e.g., "architecture: no structural files changed"). A run in full mode passes by default. An amend run with no scoping disclosure fails. |
| C-10 | Cross-file pattern entries include root cause hypothesis | aspirational | depth | Each identified pattern entry states a root cause hypothesis — not just a list of occurrences. The hypothesis must name a structural reason (e.g., "shared utility missing, each file implements its own version") or a process reason (e.g., "error handling added post-hoc, before style guide existed"). A pattern entry that only lists files and describes the symptom without a causal claim fails. |
| C-11 | At least two compliance-sensitive criteria are format-encoded | aspirational | format | The prompt encodes at least two of C-02, C-07, C-08 as structural format constraints — table columns, named field blocks, or output templates — rather than prose obligations alone. Format-encoded compliance is structurally impossible to omit; a table with a `File:Line` column cannot emit a finding without a location. A prompt that relies entirely on imperative prose ("every finding must have a line number") without any structural enforcement is execution-risk-elevated and fails this criterion. Evidence: V-02 "format makes omission structurally impossible"; V-05 "table column enforces severity." |
| C-12 | Inertia framing names at least two known failure modes | aspirational | behavior | The prompt explicitly names at least two failure modes it is designed to prevent — making the failure pattern salient primes the model against regression under output pressure. Naming must be specific enough to recognize as a failure mode (e.g., "naive reviews omit per-discipline verdicts," "silent domain expert selection," "findings without line numbers") — generic exhortation ("be thorough," "be precise") does not pass. A prompt that only states what to do without naming what to avoid fails. Evidence: V-05 "Verdict block named as one of three things naive reviews leave out — framing primes it"; "Silent expert selection explicitly named as one of three naive-review failures — model is primed to disclose." |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

> Note: Adding C-11 and C-12 divides the aspirational 10 pts across 4 criteria (2.5 pts
> each). The essential+recommended ceiling remains 90, so the 80-pt golden threshold
> is achievable without any aspirational passes.

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
| — | C-11 | Prompt states "every finding must include a line number" in prose but provides no table or template; model drops line numbers on long outputs where instruction pressure fades |
| — | C-12 | Prompt states all requirements affirmatively; model produces compliant output on easy inputs but regresses on complex ones where no failure-mode priming exists to resist |
