Written to `simulations/quest/rubrics/review-code-rubric-v4-2026-03-14.md`.

---

## Two new criteria extracted from V-04

**C-15 — Output fields use machine-parseable key=value template syntax** *(aspirational / format)*

V-04 exclusively. `total=[N] CRIT=[n] MAJ=[n] MIN=[n]`, `spec-gaps=[list or "n/a"]`, `Name: [expert] Signal: [exact code signal]` — key=value syntax creates a parsing contract with downstream tooling. V-03 uses prose templates ("N findings (X CRIT, Y MAJ, Z MIN)") and scores 100 on all other criteria; C-15 is the sole differentiator. A prose template is human-readable but requires a natural-language parser to extract. A key=value template is both.

**C-16 — Failure mode registry extends F-ID coverage to all recommended criteria** *(aspirational / behavior)*

V-04 exclusively. V-04's registry assigns F-IDs to every recommended criterion: C-06→F-10, C-07→F-06, C-08→F-07, C-09→F-08, C-10→F-09. V-03's compact registry (F-01..F-05) covers essential criteria only — recommended criteria are enforced by template structure alone. When output pressure builds mid-generation, a structural template can erode silently; an F-ID anchor re-primes.

---

## Updated scoring

Aspirational grows from 6 to 8 criteria — each worth **1.25 pts** instead of 1.67. Essential+recommended ceiling stays at 90; golden threshold (>= 80) unchanged.

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

**Aspirational progression (extended):**

| Level | Criterion | What it requires |
|-------|-----------|------------------|
| Floor | C-11 | Structural encoding of 2+ criteria |
| Baseline | C-12 | 2+ failure modes named anywhere |
| Local | C-13 | Failure mode labels co-located with enforcement points |
| Indexed | C-14 | Numbered registry (F-IDs) enabling cross-reference |
| Parseable | C-15 | Machine-parseable key=value template syntax |
| Complete | C-16 | F-ID registry extends to all recommended criteria |
 modes named anywhere in the prompt |
| Local | C-13 | Failure mode labels co-located with each enforcement point |
| Indexed | C-14 | Numbered registry (F-IDs) enabling cross-reference without repetition |
| Parseable | C-15 | Machine-parseable key=value template syntax for all structured output fields |
| Complete | C-16 | F-ID registry extends coverage to all recommended criteria, not just essential |

---

## Essential Criteria (60 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | 6 disciplines with explicit PASS/FAIL verdicts | essential | format | Output contains exactly 6 discipline sections (e.g., correctness, security, performance, maintainability, style, architecture) and each section emits an explicit PASS or FAIL verdict. A discipline section that lists findings but omits a verdict label is a fail. A run with fewer than 6 disciplines is a fail. |
| C-02 | Every finding has file:line annotation | essential | format | Every finding includes the source location in `file:line` or `file:start-end` format. Findings that reference only a function name, class, or file without a line number do not pass. Zero findings with no annotation is acceptable only if the discipline section explicitly states "no findings." |
| C-03 | Findings grouped by file | essential | format | Output contains one section or heading per reviewed file, and all findings for that file appear under it. Findings scattered in discipline-only sections without a file-grouping pass are a fail. A hybrid layout (per-discipline with file sub-grouping) passes if every finding appears under its source file within the discipline block. |
| C-04 | At least one cross-file pattern identified and labeled | essential | coverage | Output contains a dedicated patterns section or inline pattern callouts. Each pattern entry names at least two files where the pattern appears and describes what the pattern is (e.g., "error handling inconsistent across 4 files"). A run that lists per-file findings with no cross-file synthesis is a hard fail. |
| C-05 | Domain expert selection disclosed with signal used | essential | behavior | Output explicitly names which domain experts were auto-selected (e.g., "TypeScript expert, React patterns reviewer") and states the signal used to select them (e.g., "package.json contains react@18"). A run that applies domain experts without disclosure, or that applies no domain experts with no explanation, is a hard fail. |

---

## Recommended Criteria (30 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | Spec compliance mapped per discipline when spec is provided | recommended | correctness | When the input includes a spec document, each discipline section identifies which spec sections or requirements it checked and flags any gaps (spec requirement present but not implemented). A run on a specless input passes by default. A run on a spec-provided input that makes no spec references fails. |
| C-07 | Severity label on every finding | recommended | depth | Every individual finding carries a severity label: CRITICAL / MAJOR / MINOR or equivalent three-tier scale. Findings without labels are acceptable only if the discipline summary provides an aggregate count by severity and identifies which findings belong to which tier. A run with no severity differentiation at all fails. |
| C-08 | Finding count summary per discipline with severity breakdown | recommended | format | Each discipline section includes a summary line stating total findings and the breakdown by severity (e.g., "3 findings: 1 CRITICAL, 2 MINOR"). The summary must appear as a distinct element -- not require the reader to count findings manually. |

---

## Aspirational Criteria (10 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Amend mode scoping disclosed when run incrementally | aspirational | behavior | When run in amend mode (changed files only), output contains a disclosure block that names: (a) which files changed, (b) which disciplines were re-run, (c) which disciplines were skipped and why (e.g., "architecture: no structural files changed"). A run in full mode passes by default. An amend run with no scoping disclosure fails. |
| C-10 | Cross-file pattern entries include root cause hypothesis | aspirational | depth | Each identified pattern entry states a root cause hypothesis -- not just a list of occurrences. The hypothesis must name a structural reason (e.g., "shared utility missing, each file implements its own version") or a process reason (e.g., "error handling added post-hoc, before style guide existed"). A pattern entry that only lists files and describes the symptom without a causal claim fails. |
| C-11 | At least two compliance-sensitive criteria are format-encoded | aspirational | format | The prompt encodes at least two of C-02, C-07, C-08 as structural format constraints -- table columns, named field blocks, or output templates -- rather than prose obligations alone. Format-encoded compliance is structurally impossible to omit; a table with a `File:Line` column cannot emit a finding without a location. A prompt that relies entirely on imperative prose without structural enforcement is execution-risk-elevated and fails this criterion. Note: any prompt with a findings table carrying `Line` and `Sev` columns passes -- C-11 is a floor in R2. Evidence: V-02 "format makes omission structurally impossible"; V-05 "table column enforces severity." |
| C-12 | Inertia framing names at least two known failure modes | aspirational | behavior | The prompt explicitly names at least two failure modes it is designed to prevent -- making the failure pattern salient primes the model against regression under output pressure. Naming must be specific enough to recognize as a failure mode (e.g., "naive reviews omit per-discipline verdicts," "silent domain expert selection," "findings without line numbers") -- generic exhortation ("be thorough," "be precise") does not pass. A prompt that only states what to do without naming what to avoid fails. Evidence: V-05 "Verdict block named as one of three things naive reviews leave out"; "Silent expert selection explicitly named as one of three naive-review failures." |
| C-13 | Failure mode labels are co-located with enforcement points | aspirational | behavior | The prompt places failure mode labels -- by name or F-ID -- at the exact enforcement point where regression would occur, not only in a preamble or opening registry. A preamble list alone fails this criterion even if C-12 passes. Each enforcement point (findings table, verdict block, expert disclosure, patterns section) must carry a local label that fires at the moment of generation. A prompt where all failure mode naming is concentrated in the opening and absent at output blocks fails. Evidence: V-02 names F-IDs per-step ("a row without a `Line` value produces F-02"); V-04 annotates each section `(Prevents: X)`. V-01 and V-03 name failure modes in preamble only -- they pass C-12 but fail C-13 and score 97.5. |
| C-14 | Failure mode registry assigns identifiers enabling cross-referencing | aspirational | format | The prompt includes a numbered failure mode registry -- a defined list with unique identifiers (e.g., F-01 through F-NN) -- where each entry names the failure mode, describes the symptom, and identifies the output pattern that triggers it. Identifiers are reused at enforcement points throughout the prompt without restating the full definition. A prompt with named failure modes but no identifier system fails. A prompt with F-IDs defined but not referenced at enforcement points fails. Evidence: V-02 10-item registry (F-01..F-10); "if you find yourself about to produce output matching any of the above failure modes, stop and restructure"; F-IDs appear at each step. |
| C-15 | Output fields use machine-parseable key=value template syntax | aspirational | format | The prompt defines all structured output fields using `key=[value]` syntax -- not prose templates or natural-language formats. Required fields such as finding counts, severity breakdowns, spec gap flags, and expert selection signals must appear as named key=value pairs (e.g., `total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]`, `spec-gaps=[list or "n/a"]`, `Name: [expert]   Signal: [exact code signal]`). A prompt that uses prose templates ("N findings (X CRIT, Y MAJ, Z MIN)") or table columns only -- without key=value field contracts -- fails. Key=value syntax creates a parsing contract that downstream tooling can consume without natural-language extraction. Evidence: V-04 `total=[N] CRIT=[n] MAJ=[n] MIN=[n]`; `spec-gaps=[list or "n/a"]`; `Name: [expert] Signal: [exact code signal]`. V-03 uses prose templates and scores 100 on all other criteria -- C-15 is the sole differentiator. |
| C-16 | Failure mode registry extends F-ID coverage to all recommended criteria | aspirational | behavior | The prompt's numbered failure mode registry assigns F-IDs not only to the 5 essential criteria but to every recommended criterion as well: C-06 (spec compliance), C-07 (severity labels), C-08 (finding count summary), C-09 (amend mode), C-10 (root cause hypothesis). A registry covering only essential criteria (e.g., F-01..F-05) fails. A registry where recommended criteria have no F-ID anchor fails. Full coverage means every output block -- not just the essential five -- has a named failure mode that re-primes at the moment of generation, eliminating partial enforcement gaps. Evidence: V-04 assigns F-06 (severity omission), F-07 (count summary omission), F-08 (amend scope omission), F-09 (symptom-only root cause), F-10 (spec gap omission) and references each at its enforcement point. V-03's compact F-01..F-05 registry passes C-14 but fails C-16. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

> Note: Adding C-15 and C-16 divides the aspirational 10 pts across 8 criteria (1.25 pts each).
> The essential+recommended ceiling remains 90, so the 80-pt golden threshold is achievable
> without any aspirational passes.

---

## Aspirational Criterion Relationships

C-11 through C-16 form a progression -- each builds on the previous:

| Level | Criterion | What it requires |
|-------|-----------|------------------|
| Floor | C-11 | Structural encoding of at least 2 criteria (table columns, named field blocks) |
| Baseline | C-12 | At least 2 failure modes named anywhere in the prompt |
| Local | C-13 | Failure mode labels co-located with each enforcement point (not preamble-only) |
| Indexed | C-14 | Numbered registry (F-IDs) enabling cross-reference without repetition |
| Parseable | C-15 | Machine-parseable key=value template syntax for all structured output fields |
| Complete | C-16 | F-ID registry extends coverage to all recommended criteria, not just essential |

A prompt that passes C-16 necessarily passes C-14 (registry exists with identifiers) and C-12
(registry names failure modes). C-15 is independent of C-13 and C-14: a prompt can have key=value
templates without a registry (fails C-14, passes C-15) or a full registry without key=value syntax
(passes C-14, fails C-15). The highest-scoring pattern combines all six: table columns (C-11),
named failure modes (C-12), co-located labels (C-13), F-ID registry (C-14), key=value templates
(C-15), full registry coverage (C-16).

---

## Common Failure Modes

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|
| -- | C-01 | Discipline names appear in prose summary but no per-discipline PASS/FAIL verdict is emitted; reader must infer verdict from finding count |
| -- | C-02 | Findings reference function names ("in `handleSubmit`") without line numbers; annotations look present but are not actionable without line context |
| -- | C-03 | All findings appear in discipline sections; file grouping never materializes -- reader must grep to find what changed in each file |
| -- | C-04 | Per-file findings are complete and detailed, but no synthesis pass runs; patterns that span 3-4 files go unnamed |
| -- | C-05 | Domain experts applied silently; output shows TypeScript-specific advice but never states that a TS expert was selected or why |
| -- | C-06 | Spec provided but disciplines check only code quality; spec-to-code gap analysis absent even when requirements are unimplemented |
| -- | C-07 | All findings listed at equal weight; CRITICAL security issues indistinguishable from MINOR style nits without severity labels |
| -- | C-09 | Amend run re-checks all disciplines against all files; no disclosure of what changed or what was skipped -- amend mode is indistinguishable from a full run |
| -- | C-11 | Prompt states "every finding must include a line number" in prose but provides no table or template; model drops line numbers on long outputs where instruction pressure fades |
| -- | C-12 | Prompt states all requirements affirmatively; model produces compliant output on easy inputs but regresses on complex ones where no failure-mode priming exists to resist |
| -- | C-13 | Prompt lists failure modes in the opening paragraph; none appear again at the findings table, verdict block, or patterns section; model has passed the priming window before the riskiest output blocks are generated |
| -- | C-14 | Prompt names failure modes with natural-language labels only; different sections use different phrasings for the same failure mode; no shared identifier system exists to enforce consistency across enforcement points |
| -- | C-15 | Prompt uses prose templates ("N findings (X CRIT, Y MAJ, Z MIN)") that are human-readable but require natural-language parsing to extract; downstream tooling cannot consume the output without a parser |
| -- | C-16 | Registry covers F-01..F-05 (essential only); recommended criteria such as severity labels and finding count summaries have no F-ID anchor; when output pressure builds, these blocks degrade silently without a failure mode label to re-prime |
