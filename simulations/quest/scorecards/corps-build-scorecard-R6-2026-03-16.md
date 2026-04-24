## Scorecard: corps-build R6 (Rubric v6)

---

### Scoring Key

- **PASS** = full credit; **PARTIAL** = 0.5 credit; **FAIL** = 0
- Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/13 × 10)`

---

### V-01 — Lifecycle: TRANSCRIPTION-CLEAR covers all artifacts

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | `.roles/{area-slug}/{role-slug}.md` paths, ROLES-COMPLETE tracking vs org.yaml slot count |
| C-02 | PASS | WRITE-CHART Phase 7 produces org-chart.md with ASCII hierarchy, box-drawing characters |
| C-03 | PASS | Dedicated WRITE-IA phase; `IA-PHASE-COMPLETE: [n of n] teams covered. All IA files written before standard/specialized` |
| C-04 | PASS | PARSE emits full group/team tree; VALIDATE checks no duplicate teams, no flattening |
| C-05 | PASS | All five fields listed explicitly for IA and role files; NO placeholder text constraint stated |
| C-06 | PASS | CONTRACT ARTIFACT-A headcount table + ARTIFACT-C level distribution table both produced |
| C-07 | PASS | Scope field values explicit: `standard -- present in all teams`, `specialized -- [team name]`, `shared -- [group name]`, `exec office` |
| C-08 | PASS | AMEND section with `--area [name]`, `--levels [old]:[new]`, `--restructure [team]>[new-parent]`; each names specific mechanism |
| C-09 | PASS | Resistance profiles drive IA content; `no two IA files share identical lens or expertise text`; lens-phrase derived from specific defended-artifact |
| C-10 | PASS | CROSS-REF phase: org.yaml slots vs files written, IA files vs team count, table fidelity check |
| C-11 | PASS | VALIDATE phase explicitly runs before any files are written; four named structural checks |
| C-12 | PASS | WRITE-IA precedes WRITE-ROLES; IA-PHASE-COMPLETE gates entry to WRITE-CHART |
| C-13 | PASS | ARTIFACT-A produced in CONTRACT (no-file phase); ROLES-COMPLETE derives file count from table total |
| C-14 | PASS | ARTIFACT-B: exactly 2-3 sentences; strong vs weak example; references specific area names and counts |
| C-15 | PASS | `no generic stability language; no boilerplate applicable to any team`; lens anchored to defended-artifact; orientation is specific concern not generic caution |
| C-16 | PASS | Dedicated PROFILE phase before WRITE-IA; per-team defended-artifact + change-pressure + lens-phrase with quality bar |
| C-17 | PASS | BUILD-VERIFY Phase 9 — single-purpose, confirms each IA lens opens with Phase 5 lens-phrase verbatim |
| C-18 | PASS | WRITE-CHART explicitly says `[TRANSCRIBE CONTRACT ARTIFACT-A verbatim -- do not recalculate]` for each section |
| C-19 | PASS | TRANSCRIPTION-RECEIPT per-artifact VERBATIM/REVISED; PATH-B rewrites REVISED sections; `phase cannot exit REVISED` |
| C-20 | PASS | `SINGLE-PURPOSE GATE. NO file writes, NO structural file-count checks... Any content beyond per-team VERBATIM/DRIFT verdicts is a build error.` |
| C-21 | PASS | PATH-B step 2: "re-audits every contract artifact in a single pass -- including those that were already VERBATIM before the rewrite. The block covers all three or it does not serve as an exit gate." Exemption explicit in PATH-A. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 13/13 = 10

**V-01 composite: 100.00**

---

### V-02 — Output format: PATH-A / PATH-B named binary structure

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Same path scheme; ROLES-COMPLETE tracking |
| C-02 | PASS | Step 7 produces org-chart.md with ASCII hierarchy |
| C-03 | PASS | WRITE-IA step; `IA-PHASE-COMPLETE: [n of n] teams` |
| C-04 | PASS | PARSE + VALIDATE cover structural fidelity |
| C-05 | PASS | Five fields required; no placeholder text |
| C-06 | PASS | ARTIFACT-A + ARTIFACT-C in CONTRACT step |
| C-07 | PASS | Explicit scope values in WRITE-IA and WRITE-ROLES |
| C-08 | PASS | Three AMEND options with specific mechanisms in Step 7 |
| C-09 | PASS | Resistance profiles drive IA; no-identical-lens rule |
| C-10 | PASS | Step 10 CROSS-REF checks |
| C-11 | PASS | VALIDATE step — no files written, four checks |
| C-12 | PASS | All IA files before standard/specialized |
| C-13 | PASS | CONTRACT produces headcount before any file write |
| C-14 | PASS | ARTIFACT-B analytic prose shape specified |
| C-15 | PASS | `orientation: from defended-artifact -- specific concern`; no generic stability language |
| C-16 | PASS | PROFILE step before WRITE-IA |
| C-17 | PASS | BUILD-VERIFY single-purpose lens-phrase verification |
| C-18 | PASS | `[TRANSCRIBE ARTIFACT-A verbatim]` instructions in WRITE-CHART |
| C-19 | PASS | TRANSCRIPTION-RECEIPT with per-artifact verdicts; PATH-B rewrites REVISED |
| C-20 | PASS | `SINGLE-PURPOSE GATE... NO file writes... Any content beyond per-team verdicts is a build error.` |
| C-21 | PASS | PATH-B post-rewrite: "Emit TRANSCRIPTION-CLEAR. This block re-audits all three artifacts in one pass -- including those that were VERBATIM before the rewrites. CHART-WRITTEN cannot be emitted until this block is present and all three lines show VERBATIM." Path labeling makes exemption (PATH-A) and obligation (PATH-B) structurally distinguishable. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 13/13 = 10

**V-02 composite: 100.00**

---

### V-03 — Phrasing register: declarative output-forward framing

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Stage 7 specifies role file paths and five-field completeness; ROLES-COMPLETE tracking |
| C-02 | PASS | Stage 8 names (1) ASCII hierarchy as first section of org-chart.md |
| C-03 | PASS | Stage 6 — all IA files written before standard/specialized; `IA-COMPLETE: [n of n] teams` |
| C-04 | PASS | Stage 1 parse and Stage 2 validate described as shape constraints; halt on anomalies |
| C-05 | PASS | Stage 7 — "A correct role file contains all five fields... No field is a placeholder." |
| C-06 | PASS | Stage 3 ARTIFACT-A headcount table shape; ARTIFACT-C level distribution shape |
| C-07 | PASS | Stage 7 "Scope names the role type explicitly." |
| C-08 | **PARTIAL** | Stage 8 names "AMEND" as one of five sections but does not specify the three `--area`/`--levels`/`--restructure` options with concrete value placeholders; pass condition requires each option name a specific mechanism |
| C-09 | PASS | Stage 5 resistance profiles with specific defended-artifact bar; stage 6 non-transplantable lens requirement |
| C-10 | PASS | Stage 10 cross-reference block shape |
| C-11 | PASS | Stage 2 — validate block halts on anomalies, no files written |
| C-12 | PASS | Stage 6 explicitly states IA files before standard/specialized |
| C-13 | PASS | Stage 3 produces headcount before any file write; role-file count derived from table |
| C-14 | PASS | Stage 3 shows strong vs incorrect ARTIFACT-B with named area, count, and structural observation |
| C-15 | PASS | Stage 6 — "A correct IA role file is a person-portrait"; no generic stability language; non-transplantable lens required |
| C-16 | PASS | Stage 5 resistance profiles with incorrect-profile examples; PROFILE-GATE before IA writes |
| C-17 | PASS | Stage 9 — BUILD-VERIFY block shape specified; `A BUILD-VERIFY block with non-verdict content is structurally invalid` |
| C-18 | PASS | Stage 8 — "Sections 2-4 are CONTRACT ARTIFACT-A, -B, and -C. The same content. Not a rewrite." |
| C-19 | PASS | Stage 8 TRANSCRIPTION-RECEIPT shape; Shape B shows rewrite of REVISED sections |
| C-20 | PASS | Stage 9 — block shape has exactly N entries, one per team; "The block contains nothing else" |
| C-21 | PASS | Stage 8 Shape B: "A correct TRANSCRIPTION-CLEAR names all three artifacts -- not only the one that was rewritten. A TRANSCRIPTION-CLEAR that names fewer than three artifacts is structurally incomplete. CHART-WRITTEN appears only after TRANSCRIPTION-CLEAR in Shape B." Shape A explicitly shown without TRANSCRIPTION-CLEAR. |

**Essential**: 5/5 = 60 | **Recommended**: 2.5/3 × 30 = 25 | **Aspirational**: 13/13 = 10

**V-03 composite: 95.00**

---

### V-04 — Lifecycle + Inertia: PROFILE before CONTRACT

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Role file paths, ROLES-COMPLETE tracking |
| C-02 | PASS | WRITE-CHART phase produces org-chart.md with ASCII hierarchy |
| C-03 | PASS | WRITE-IA phase; `IA-PHASE-COMPLETE: [n of n] teams. Resistance portraits written from profiles.` |
| C-04 | PASS | PARSE + VALIDATE (four checks) before any files |
| C-05 | PASS | Five fields required; all five named in WRITE-IA and WRITE-ROLES |
| C-06 | PASS | CONTRACT ARTIFACT-A + ARTIFACT-C |
| C-07 | PASS | Explicit scope labels in WRITE-ROLES |
| C-08 | PASS | AMEND section with three specific-mechanism options in WRITE-CHART |
| C-09 | PASS | Resistance profiles extracted per-team before any IA file; lens-phrase uniqueness enforced |
| C-10 | PASS | CROSS-REF phase with four MATCH/MISMATCH checks |
| C-11 | PASS | VALIDATE phase — no files written, four structural checks |
| C-12 | PASS | WRITE-IA before WRITE-ROLES; "all Inertia Advocate files are written from the resistance map — before any standard or specialized role files" |
| C-13 | PASS | CONTRACT phase (no-file phase) produces headcount table before first role file; file-writing derives from table row count |
| C-14 | PASS | ARTIFACT-B: specific area names, counts, structural observation; no generic summaries |
| C-15 | PASS | "IA file is a portrait of a specific kind of person, not a filled-in template"; strong vs weak lens example shown |
| C-16 | PASS | PROFILE is Phase 3 (before CONTRACT) — "Resistance profiles are extracted before the headcount contract is built. The contract is assembled from profiles." This is the deepest C-16 integration yet. |
| C-17 | PASS | BUILD-VERIFY SINGLE-PURPOSE GATE; Phase 3 lens-phrase vs written file |
| C-18 | PASS | `[TRANSCRIBE CONTRACT ARTIFACT-A verbatim]` explicit in WRITE-CHART |
| C-19 | PASS | TRANSCRIPTION-RECEIPT with per-artifact verdicts; REVISED triggers rewrite; all-VERBATIM takes direct path |
| C-20 | PASS | `SINGLE-PURPOSE GATE. This phase confirms... One output per team: VERBATIM or DRIFT. Nothing else inside this phase.` |
| C-21 | PASS | After rewrites: "emit TRANSCRIPTION-CLEAR -- one pass over all three artifacts, not only the ones that changed"; all-three confirmation before CHART-WRITTEN; exemption explicit |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 13/13 = 10

**V-04 composite: 100.00**

---

### V-05 — Full integration: all 13 criteria

**Note on phase sequence**: V-05 uses `WRITE-IA → WRITE-ROLES → WRITE-CHART`, putting WRITE-CHART *after* WRITE-ROLES. This differs from all other variations.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Five fields, no placeholder; ROLES-COMPLETE tracking vs org.yaml |
| C-02 | PASS | WRITE-CHART (Phase 8) produces org-chart.md with ASCII hierarchy |
| C-03 | PASS | WRITE-IA (Phase 6) before WRITE-ROLES (Phase 7); IA-PHASE-COMPLETE confirms n of n teams |
| C-04 | PASS | PARSE + VALIDATE (four checks, no files written) |
| C-05 | PASS | All five fields required; no placeholder text |
| C-06 | PASS | CONTRACT ARTIFACT-A + ARTIFACT-C |
| C-07 | PASS | Explicit scope values |
| C-08 | PASS | AMEND section with three specific options in WRITE-CHART |
| C-09 | PASS | Resistance profiles drive IA content; no-identical-lens rule |
| C-10 | PASS | CROSS-REF phase checks all four dimensions |
| C-11 | PASS | VALIDATE phase — no files written |
| C-12 | PASS | WRITE-IA before WRITE-ROLES; "IA omission is structurally impossible: an unstarted IA file means the team's entire role set has not begun" |
| C-13 | **FAIL** | Pass condition: "headcount table in org-chart.md is written prior to the first role file." In V-05, WRITE-ROLES (Phase 7) executes before WRITE-CHART (Phase 8). The CONTRACT artifact exists before any file write, but org-chart.md is written *after* .roles/ files, inverting the required order. |
| C-14 | PASS | ARTIFACT-B with 2-3 sentences; strong/weak example |
| C-15 | PASS | "IA file is a person-portrait -- not a filled-in template"; no generic language; non-transplantable lens |
| C-16 | PASS | PROFILE phase (Phase 5) before WRITE-IA (Phase 6) |
| C-17 | PASS | BUILD-VERIFY SINGLE-PURPOSE GATE |
| C-18 | PASS | "TRANSCRIBE CONTRACT ARTIFACT-A verbatim" instructions |
| C-19 | PASS | TRANSCRIPTION-RECEIPT with auto-correction; all-VERBATIM exemption explicit |
| C-20 | PASS | "NO file writes, NO structural file-count checks... Any content in this phase beyond per-team VERBATIM/DRIFT verdicts is a build error." BUILD-VERIFY-PASS summary: "Phase produced [n] VERBATIM/DRIFT verdicts and no other outputs." |
| C-21 | PASS | "This named block re-audits every contract artifact in a single pass -- including those that were already VERBATIM before any rewrite. The block must list all three. A block that names fewer than three artifacts does not satisfy the exit gate." |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 12/13 × 10 = 9.23

**V-05 composite: 99.23**

---

## Ranking

| Rank | Var | Score | Deltas vs Prior |
|------|-----|-------|-----------------|
| 1 (tie) | V-01 | 100.00 | C-21 PASS: minimal lifecycle fix from R5 PARTIAL |
| 1 (tie) | V-02 | 100.00 | C-21 PASS: binary PATH-A/PATH-B makes elision structurally visible |
| 1 (tie) | V-04 | 100.00 | C-21 PASS + deepest C-16 integration: PROFILE before CONTRACT |
| 4 | V-05 | 99.23 | C-13 FAIL: phase reordering (WRITE-ROLES before WRITE-CHART) inverts headcount-first contract |
| 5 | V-03 | 95.00 | C-08 PARTIAL: declarative framing omits AMEND option detail |

---

## Excellence Signals

**From V-01/V-02/V-04 (three-way tie at 100):**

1. **C-21 minimal fix confirmed**: The single-axis change (TRANSCRIPTION-CLEAR must re-audit all three artifacts, not only the rewritten one) is sufficient on its own to reach 100. The explicit exemption clause (PATH-A: all VERBATIM first pass, no block required) is load-bearing — without it, C-21 would over-fire.

2. **Binary output shape (V-02 structural innovation)**: PATH-A and PATH-B are not just documentation — they make the two exit shapes visually distinguishable in the output. A model that emits CHART-WRITTEN after a REVISED verdict without TRANSCRIPTION-CLEAR produces output that matches neither path. Non-compliance is visible, not just detectable.

3. **Phase reordering as structural anchor (V-04)**: Placing PROFILE before CONTRACT makes resistance profiles the causal source of contract artifacts. The language "The contract is assembled from profiles, not constructed independently" converts C-15 and C-16 from quality criteria (checked after the fact) into structural invariants (required inputs to the next phase). This is the strongest C-16 coverage seen across all rounds.

4. **V-05 phase-reordering regression**: Reversing WRITE-CHART and WRITE-ROLES to produce BUILD-VERIFY after org-chart.md is written (so BUILD-VERIFY can gate on CHART-WRITTEN rather than IA-PHASE-COMPLETE) violates C-13. The tradeoff is implicit and silent — each phase is individually correct, but the ordering change breaks a cross-phase ordering invariant. This is the first observed case of a correctly motivated reordering producing a new failure.

5. **V-03 declarative axis fully realized**: All 13 aspirational criteria expressed as output shapes. Shape A vs Shape B for TRANSCRIPTION-CLEAR is the cleanest shape-based specification of a conditional invariant seen in this series. The C-08 PARTIAL (AMEND options absent from the shape) shows the axis's limitation: declarative framing requires explicit shape templates for all criteria, including the ones with structured sub-options.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["binary-path-shape: PATH-A vs PATH-B as named output shapes makes TRANSCRIPTION-CLEAR elision structurally visible -- non-compliance produces output matching neither path rather than instructions-not-followed", "profile-before-contract reordering: PROFILE phase placed before CONTRACT makes resistance profiles the causal source of contract artifacts, converting C-15/C-16 from quality criteria to structural inputs", "declarative-output-forward axis fully realized across all 13 aspirational criteria: each criterion described as shape constraint on output; Shape A vs Shape B for TRANSCRIPTION conditional is the canonical shape-based conditional invariant specification", "phase-reorder regression signal: reversing WRITE-CHART and WRITE-ROLES to satisfy BUILD-VERIFY entry condition (CHART-WRITTEN) silently violates C-13 cross-phase ordering invariant -- each phase individually correct but ordering breaks headcount-first contract"]}
```
