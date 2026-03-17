Now I have everything I need to score all 5 variations. Let me evaluate each criterion carefully.

---

# review-code — Scorecard R3

**Rubric version**: v3 (14 criteria: 5 essential, 3 recommended, 6 aspirational)
**Formula**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/6 * 10)`

---

## V-01 — Co-located Named Labels (C-13 isolation)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | 6 disciplines + PASS/FAIL verdicts | PASS | Section 4 DISCIPLINE VERDICTS block: 6 stock disciplines each with `[PASS\|FAIL]` label |
| C-02 | Every finding has file:line | PASS | Section 3 findings table has `Line` column with `[exact number or range]`; "A row without a Line value is not actionable" |
| C-03 | Findings grouped by file | PASS | Section 3: one table per file; "Organizing this output by discipline instead of by file prevents the per-file view" |
| C-04 | Cross-file pattern identified + labeled | PASS | Section 5: PATTERN blocks with Files + What + Why fields required |
| C-05 | Domain expert selection disclosed with signal | PASS | Section 2 EXPERT DISCLOSURE: "Added: [expert name] -- selected because: [specific code signal]" |
| C-06 | Spec compliance mapped per discipline | PASS | Section 4: "If a spec was provided, append `Spec gaps: [list or 'none']` per discipline" |
| C-07 | Severity label on every finding | PASS | Section 3: `Sev` column `[CRIT\|MAJ\|MIN]` required on every row |
| C-08 | Finding count summary with severity breakdown | PASS | Section 4: "N findings (X CRIT, Y MAJ, Z MIN)" per discipline |
| C-09 | Amend mode scoping disclosed | PASS | Section 6 Amend Scope: Changed files / Disciplines re-run / Disciplines skipped |
| C-10 | Pattern entries include root cause hypothesis | PASS | Section 5: `Why: [root cause hypothesis -- name a structural reason or a process reason]`; "a Why: entry that names a symptom instead of a cause is structurally incomplete" |
| C-11 | 2+ compliance-sensitive criteria format-encoded | PASS | Section 3 table has `Line` column (C-02) and `Sev` column (C-07) — both structurally impossible to omit |
| C-12 | Inertia framing names 2+ failure modes | PASS | 8 failure modes named via `(Prevents: ...)` labels: silent expert selection, line annotations missing, file grouping absent, verdicts absent, finding count not summarized, cross-file synthesis absent, root cause missing, amend scope undisclosed |
| C-13 | Failure mode labels co-located with enforcement points | PASS | Every enforcement section carries a `(Prevents: ...)` label immediately above it: Section 2 (expert), Section 3 (lines + file-grouping), Section 4 (verdicts + counts), Section 5 (synthesis + root cause), Section 6 (amend scope) |
| C-14 | Failure mode registry assigns F-IDs enabling cross-referencing | **FAIL** | No numbered registry. Labels are descriptive strings — no F-01..F-NN identifier system. Cross-referencing without repeating definitions is impossible. By design. |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 5/6

`(5/5 * 60) + (3/3 * 30) + (5/6 * 10) = 60 + 30 + 8.33 = **98.3**`

---

## V-02 — Registry Preamble Only (C-14 boundary test)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | 6 disciplines + PASS/FAIL verdicts | PASS | Step 4 DISCIPLINE VERDICTS: 6 disciplines with `[PASS\|FAIL]` per discipline |
| C-02 | Every finding has file:line | PASS | Step 3 table has `Line` column; "Every row must have a `Line` value" |
| C-03 | Findings grouped by file | PASS | Step 3: one table per file, sorted by line number |
| C-04 | Cross-file pattern identified + labeled | PASS | Step 5: PATTERN blocks with Files, What, Why |
| C-05 | Domain expert selection disclosed with signal | PASS | Step 2 EXPERT DISCLOSURE: "Added: [expert name] -- selected because: [specific code signal]" |
| C-06 | Spec compliance mapped per discipline | PASS | Step 4: "If a spec was provided, append `Spec gaps: [list or 'none']`" |
| C-07 | Severity label on every finding | PASS | Step 3: `Sev` column `[CRIT\|MAJ\|MIN]`; "Every row must have a `Sev` value" |
| C-08 | Finding count summary with severity breakdown | PASS | Step 4: "N findings (X CRIT, Y MAJ, Z MIN)" per discipline |
| C-09 | Amend mode scoping disclosed | PASS | Step 6 Amend Scope block with all three fields |
| C-10 | Pattern entries include root cause hypothesis | PASS | Step 5: `Why: [root cause hypothesis]`; "A `Why:` entry stating a symptom instead of a cause is structurally incomplete" |
| C-11 | 2+ compliance-sensitive criteria format-encoded | PASS | Step 3 table: `Line` (C-02) and `Sev` (C-07) columns present |
| C-12 | Inertia framing names 2+ failure modes | PASS | 10-item FAILURE MODE REGISTRY names all 10 failure modes specifically: F-01 through F-10 |
| C-13 | Failure mode labels co-located with enforcement points | **FAIL** | F-IDs appear only in the preamble registry. Steps 2–6 have no F-IDs or failure mode labels at any enforcement point. The priming window closes before the riskiest output blocks. |
| C-14 | Failure mode registry assigns F-IDs enabling cross-referencing | **FAIL** | Full F-01..F-10 registry defined, but F-IDs never referenced at enforcement points. Rubric requires "identifiers reused at enforcement points throughout the prompt." Registry existence without cross-referencing fails C-14 by design — this is the boundary probe. |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 4/6

`(5/5 * 60) + (3/3 * 30) + (4/6 * 10) = 60 + 30 + 6.67 = **96.7**`

---

## V-03 — Compact Registry + Co-located F-IDs (minimal)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | 6 disciplines + PASS/FAIL verdicts | PASS | Step 4 DISCIPLINE VERDICTS: 6 disciplines with `[PASS\|FAIL]`; "Omitting an explicit PASS/FAIL label per discipline triggers F-01" |
| C-02 | Every finding has file:line | PASS | Step 3 table: `Line` column required; "A row without a `Line` value triggers F-02" |
| C-03 | Findings grouped by file | PASS | Step 3: one table per file; "Organizing this output by discipline instead of by file triggers F-03" |
| C-04 | Cross-file pattern identified + labeled | PASS | Step 5: PATTERN blocks with Files, What, Why required |
| C-05 | Domain expert selection disclosed with signal | PASS | Step 2 EXPERT DISCLOSURE: "Added: [expert name] -- selected because: [specific code signal]"; "triggers F-05" |
| C-06 | Spec compliance mapped per discipline | PASS | Step 4: "If a spec was provided, append `Spec gaps: [list or 'none']`" |
| C-07 | Severity label on every finding | PASS | Step 3: `Sev` column `[CRIT\|MAJ\|MIN]`; "A row without a `Sev` value loses severity differentiation" |
| C-08 | Finding count summary with severity breakdown | PASS | Step 4: "N findings (X CRIT, Y MAJ, Z MIN)" per discipline |
| C-09 | Amend mode scoping disclosed | PASS | Step 6 Amend Scope block with Changed files / Disciplines re-run / Disciplines skipped |
| C-10 | Pattern entries include root cause hypothesis | PASS | Step 5: `Why: [root cause hypothesis]`; "A `Why:` entry that names a symptom instead of a cause is structurally incomplete" |
| C-11 | 2+ compliance-sensitive criteria format-encoded | PASS | Step 3 table: `Line` (C-02) and `Sev` (C-07) columns structurally required |
| C-12 | Inertia framing names 2+ failure modes | PASS | 5-item registry names F-01..F-05 specifically; all exceed the 2-failure-mode threshold |
| C-13 | Failure mode labels co-located with enforcement points | PASS | Every enforcement step carries a co-located F-ID: Step 2 *(F-05)* + "triggers F-05"; Step 3 *(F-02, F-03)* + trigger sentences; Step 4 *(F-01)* + "triggers F-01"; Step 5 *(F-04)* + "triggers F-04" |
| C-14 | Failure mode registry assigns F-IDs enabling cross-referencing | PASS | 5-item registry (F-01..F-05) defined with unique identifiers. F-IDs reused at enforcement points without restating definitions: Step 2→F-05, Step 3→F-02+F-03, Step 4→F-01, Step 5→F-04. Compact registry is sufficient — C-14 does not require 10 items. |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 6/6

`(5/5 * 60) + (3/3 * 30) + (6/6 * 10) = 60 + 30 + 10 = **100**`

---

## V-04 — Full Registry + Co-located F-IDs + Template Blocks

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | 6 disciplines + PASS/FAIL verdicts | PASS | OUTPUT BLOCK 4 DISCIPLINE VERDICTS: 6 disciplines with `[PASS\|FAIL]`; "Omitting PASS/FAIL per discipline triggers F-01" |
| C-02 | Every finding has file:line | PASS | OUTPUT BLOCK 3: `Line` column `[n or n-m]` required; "A row without a `Line` value triggers F-02" |
| C-03 | Findings grouped by file | PASS | OUTPUT BLOCK 3: `File: [path]` header per file; "Organizing by discipline instead of by file triggers F-03" |
| C-04 | Cross-file pattern identified + labeled | PASS | OUTPUT BLOCK 5: Pattern template with Name, Files, What, Why fields |
| C-05 | Domain expert selection disclosed with signal | PASS | OUTPUT BLOCK 2: `Name: [expert]   Signal: [exact code signal]`; "triggers F-05" |
| C-06 | Spec compliance mapped per discipline | PASS | OUTPUT BLOCK 4: `spec-gaps=[list or "n/a"]`; "Omitting `spec-gaps=` when a spec was provided triggers F-10" |
| C-07 | Severity label on every finding | PASS | OUTPUT BLOCK 3: `Sev` column `[CRIT\|MAJ\|MIN]`; "A row without a `Sev` value triggers F-06" |
| C-08 | Finding count summary with severity breakdown | PASS | OUTPUT BLOCK 4: `total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]`; "Omitting `total=` and severity breakdown triggers F-07" |
| C-09 | Amend mode scoping disclosed | PASS | OUTPUT BLOCK 6 AMEND SCOPE *(F-08)*: Changed files / Disciplines re-run / Disciplines skipped; "Omitting this block on an amend run triggers F-08" |
| C-10 | Pattern entries include root cause hypothesis | PASS | OUTPUT BLOCK 5: `Why: [root cause hypothesis]`; "A `Why:` field stating a symptom instead of a cause triggers F-09" |
| C-11 | 2+ compliance-sensitive criteria format-encoded | PASS | All 6 output blocks are named field templates. OUTPUT BLOCK 3: `Line` + `Sev` columns. OUTPUT BLOCK 4: `total=`, `CRIT=`, `MAJ=`, `MIN=` fields. Three or more criteria structurally encoded. |
| C-12 | Inertia framing names 2+ failure modes | PASS | Full 10-item FAILURE MODE REGISTRY + "If you are about to produce output matching any of the above, stop and restructure before continuing" |
| C-13 | Failure mode labels co-located with enforcement points | PASS | Every output block carries co-located F-IDs: Block 2 *(F-05)* + trigger; Block 3 *(F-02, F-03, F-06)* + 3 trigger sentences; Block 4 *(F-01, F-07, F-10)* + 3 trigger sentences; Block 5 *(F-04, F-09)* + triggers; Block 6 *(F-08)* + trigger |
| C-14 | Failure mode registry assigns F-IDs enabling cross-referencing | PASS | Full F-01..F-10 registry defined. F-IDs reused at each enforcement block without restating definitions: Block 2→F-05, Block 3→F-02+F-03+F-06, Block 4→F-01+F-07+F-10, Block 5→F-04+F-09, Block 6→F-08. Complete coverage. |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 6/6

`(5/5 * 60) + (3/3 * 30) + (6/6 * 10) = 60 + 30 + 10 = **100**`

---

## V-05 — All Axes: Full Spectrum

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | 6 disciplines + PASS/FAIL verdicts | PASS | Step 4 DISCIPLINE VERDICTS: 6 disciplines with `[PASS\|FAIL]`; "Omitting any discipline triggers F-01" |
| C-02 | Every finding has file:line | PASS | Step 3 table: `Line` column `[n or n-m]` required; "A row without a `Line` value triggers F-02" |
| C-03 | Findings grouped by file | PASS | Step 3: one table per file; "Organizing this output by discipline instead of by file triggers F-03" |
| C-04 | Cross-file pattern identified + labeled | PASS | Step 5: PATTERN blocks with Files, What, Why; "not an optional appendix" |
| C-05 | Domain expert selection disclosed with signal | PASS | Step 2 EXPERT DISCLOSURE: `Name: [expert]   Signal: [exact code signal]`; "triggers F-05" |
| C-06 | Spec compliance mapped per discipline | PASS | Step 4: `spec-gaps=[list or "n/a"]`; "Omitting `spec-gaps=` when a spec was provided triggers F-10" |
| C-07 | Severity label on every finding | PASS | Step 3: `Sev` column; "A row without a `Sev` value triggers F-06" |
| C-08 | Finding count summary with severity breakdown | PASS | Step 4: `total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]` per discipline |
| C-09 | Amend mode scoping disclosed | PASS | Amend-first lifecycle: AMEND SCOPE block fires before file inventory and expert disclosure, not after. "Producing an amend run that omits this block triggers F-08." Step 4 also handles deferred disciplines: `[Discipline]: DEFERRED -- not in amend scope.` |
| C-10 | Pattern entries include root cause hypothesis | PASS | Step 5: `Why: [root cause hypothesis]`; "A `Why:` entry that names a symptom instead of a cause triggers F-09" |
| C-11 | 2+ compliance-sensitive criteria format-encoded | PASS | Step 3: `Line` + `Sev` columns. Step 4: `total=`, `CRIT=`, `MAJ=`, `MIN=` template fields. Multiple criteria structurally encoded. |
| C-12 | Inertia framing names 2+ failure modes | PASS | Full 10-item FAILURE MODE REGISTRY; "If you are about to produce output matching any of the above, stop and restructure" |
| C-13 | Failure mode labels co-located with enforcement points | PASS | Mode declaration: *(F-08)*; Step 2: *(F-05)* + trigger; Step 3: *(F-02, F-03, F-06)* + 3 triggers; Step 4: *(F-01, F-07, F-10)* + 3 triggers; Step 5: *(F-04, F-09)* + triggers |
| C-14 | Failure mode registry assigns F-IDs enabling cross-referencing | PASS | Full F-01..F-10 registry. F-IDs reused at every enforcement point: Mode declaration→F-08, Step 2→F-05, Step 3→F-02+F-03+F-06, Step 4→F-01+F-07+F-10, Step 5→F-04+F-09 |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 6/6

`(5/5 * 60) + (3/3 * 30) + (6/6 * 10) = 60 + 30 + 10 = **100**`

---

## Score Summary

| Variation | Ess (60) | Rec (30) | Asp (10) | Composite | Golden | Predicted | Delta |
|-----------|----------|----------|----------|-----------|--------|-----------|-------|
| V-01 | 60 | 30 | 8.33 | **98.3** | YES | 98.3 | 0 |
| V-02 | 60 | 30 | 6.67 | **96.7** | YES | 96.7 | 0 |
| V-03 | 60 | 30 | 10.0 | **100** | YES | 100 | 0 |
| V-04 | 60 | 30 | 10.0 | **100** | YES | 100 | 0 |
| V-05 | 60 | 30 | 10.0 | **100** | YES | 100 | 0 |

All five predictions matched exactly.

---

## Isolation Confirmations

| Question | Probe | Result |
|----------|-------|--------|
| Can C-13 pass without C-14? | V-01 (named labels, no registry) | YES — `(Prevents: [name])` labels satisfy C-13 independently |
| Does a preamble-only registry satisfy C-14? | V-02 (registry defined, no enforcement-point refs) | NO — registry existence without cross-referencing fails both C-13 and C-14 |
| What is the minimum viable registry? | V-03 (5-item, essential-only) | 5 F-IDs are sufficient — registry does not need exhaustive coverage |
| Does triple-redundancy improve over dual? | V-04 vs V-03 | No score difference at 100 — but V-04's template enforcement adds structural floor that protects against C-11 regression |

---

## Excellence Signals — Top Scoring Variations (V-03, V-04, V-05)

**1. Compact vocabulary is sufficient for C-14.** V-03 reaches 100 with only 5 F-IDs covering the 5 essential failure modes. More F-IDs (V-04, V-05) add coverage but not score. Smaller registry reduces context dilution while satisfying the criterion.

**2. Amend-first sequencing strengthens C-09 robustness.** V-05's architecture moves the AMEND SCOPE block before file inventory — making scope declaration structurally impossible to defer. V-03 and V-04 put amend scope at the end (Step 6 / Block 6), which passes C-09 but is weaker under output pressure at the end of a long context.

**3. The registry-enforcement-point connection is the mechanism, not the registry itself.** V-02 confirms: a complete 10-item registry with no cross-referencing produces the same result as no registry for C-13 and C-14. The value is in the binding — defining the registry creates vocabulary, but F-IDs at enforcement points are what activate it at generation time.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["compact F-ID vocabulary (5-item) is sufficient for C-14 — registry size does not need to match failure mode count", "amend-first sequencing (scope block before file inventory) structurally prevents C-09 failure under output pressure", "registry existence without enforcement-point cross-referencing fails both C-13 and C-14 — the binding is the mechanism, not the definition"]}
```
