Now I have all the data I need. Let me score all five variations against rubric v6.

---

# corps-build — Round 6 Scorecard

**Rubric**: v6 (21 criteria: C-01–C-21)
**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/13 × 10)`
**Max**: 100 pts | **Golden threshold**: all 5 essential PASS + composite ≥ 80

---

## Rubric Reference (v6)

| Pool | Criteria | Weight |
|------|----------|--------|
| Essential | C-01 through C-05 | 5 × must-pass → 60 pts |
| Recommended | C-06 through C-08 | 3 × 10 pts → 30 pts |
| Aspirational | C-09 through C-21 | 13 criteria → 10 pts total |

---

## V-01 — Lifecycle: TRANSCRIPTION-CLEAR re-audit covers all artifacts

**Axis**: Lifecycle emphasis — two explicit exit paths (PATH-A / PATH-B) from TRANSCRIPTION-RECEIPT; PATH-B gates CHART-WRITTEN on TRANSCRIPTION-CLEAR enumerating all three artifacts; all-VERBATIM exemption stated.

### Essential

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | ROLES-COMPLETE: [n] files written + CROSS-REF `org.yaml slots: [n], files written: [n] -- MATCH/MISMATCH` |
| C-02 | **PASS** | WRITE-CHART Phase 6: "ASCII hierarchy -- box-drawing characters, minimum two nesting levels. Group names match org.yaml exactly." |
| C-03 | **PASS** | Phase 6 writes all IA files; IA-PHASE-COMPLETE: "[n of n] teams covered. All IA files written before standard/specialized roles." |
| C-04 | **PASS** | Paths `.roles/{area-slug}/inertia-advocate.md` + `.roles/{area-slug}/{role-slug}.md` derived from org.yaml; CONTRACT phase validates structure before files |
| C-05 | **PASS** | Phase 8: "All five fields, no placeholder text." Fields: orientation, lens, expertise, scope, collaboration pattern |

**Essential = 60/60. All 5 pass.**

### Recommended

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | CONTRACT ARTIFACT-A: headcount table with area rows, Headcount, Standard Roles, Specialized Roles, Levels, Total. ARTIFACT-C: level distribution table |
| C-07 | **PASS** | WRITE-ROLES scope field explicit: `standard -- present in all teams`, `specialized -- [team name]`, etc. |
| C-08 | **PASS** | AMEND section in WRITE-CHART: `--area "[area name]"`, `--levels "[old]:[new]"`, `--restructure "[team] > [new-parent]"` — each with specific org.yaml values |

**Recommended = 30/30.**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Lens opens verbatim with profile lens-phrase; "no generic stability language; no boilerplate applicable to any team"; IA-WRITTEN checks expertise concrete |
| C-10 | **PASS** | CROSS-REF: slots vs files MATCH, IA count MATCH, dir check MATCH, table fidelity MATCH |
| C-11 | **PASS** | VALIDATE phase (no files): 4 checks, halt on failure; explicit entry gate before CONTRACT |
| C-12 | **PASS** | Phase 6 header: "Write all Inertia Advocate files before any standard or specialized role files." IA-PHASE-COMPLETE gate |
| C-13 | **PASS** | CONTRACT phase produces ARTIFACT-A before any file write; TABLE-CLOSED sets file generation target; "no files written during this phase" |
| C-14 | **PASS** | ARTIFACT-B: exactly 2-3 sentences; strong/weak example provided; Sentence 1 names specific area + %; Sentence 3 requires structural observation not in table rows |
| C-15 | **PASS** | "no generic stability language; no boilerplate applicable to any team"; IA-WRITTEN checks expertise concrete; lens must not be transplantable — stated as rule, not verified per-file (+ not ++) |
| C-16 | **PASS** | PROFILE phase before WRITE-IA; defended-artifact + change-pressure + lens-phrase derived; LENS-COLLISION check; PROFILE-GATE before WRITE-IA |
| C-17 | **PASS** | BUILD-VERIFY: SINGLE-PURPOSE GATE; per-team VERBATIM/DRIFT verdict; DRIFT triggers rewrite + re-emit VERBATIM before next team |
| C-18 | **PASS** | WRITE-CHART: "[TRANSCRIBE CONTRACT ARTIFACT-A verbatim -- do not recalculate]"; TRANSCRIPTION-RECEIPT checks drift |
| C-19 | **PASS** | TRANSCRIPTION-RECEIPT emitted after org-chart.md; REVISED verdict triggers rewrite + update before phase closes (++) |
| C-20 | **PASS** | BUILD-VERIFY: "NO file writes, NO structural file-count checks, NO directory comparisons, NO headcount verifications, NO AMEND generation, and NO summary rows" (++) |
| C-21 | **PASS** | PATH-B: "TRANSCRIPTION-CLEAR: ARTIFACT-A: VERBATIM / ARTIFACT-B: VERBATIM / ARTIFACT-C: VERBATIM / all three confirmed — PATH-B exit authorized." Phase cannot close until all three VERBATIM (++) |

**Aspirational = 13/13 PASS → (13/13 × 10) = 10/10**

**V-01 total: 60 + 30 + 10 = 100/100** ✓ Golden

---

## V-02 — Output format: PATH-A / PATH-B named mutually exclusive structure

**Axis**: Binary branching as primary design feature — PATH-A short exit (direct CHART-WRITTEN) vs PATH-B long exit (TRANSCRIPTION-CLEAR mandatory); non-compliance structurally visible since output matches neither path shape.

### Essential / Recommended

Identical coverage to V-01: same 10-step sequence, same field requirements, same path and contract structure.

**Essential = 60/60. Recommended = 30/30.**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-16 | **PASS** (all) | Same mechanisms as V-01; PROFILE step with same quality constraints |
| C-17 | **PASS** | BUILD-VERIFY: SINGLE-PURPOSE GATE; "NO file writes. NO structural checks... Any content beyond per-team verdicts is a build error." (++) |
| C-18 | **PASS** | TRANSCRIBE ARTIFACT-A/B/C verbatim; CONTRACT-SEALED RULE states no recalculation; "Enforcement: TRANSCRIPTION-RECEIPT in Step 6. If any REVISED verdict: TRANSCRIPTION-CLEAR (all three artifacts) required before CHART-WRITTEN. If all VERBATIM on first receipt: CHART-WRITTEN directly." (++) |
| C-19 | **PASS** | REVISED → rewrite + update receipt line → CHART-WRITTEN gates on TRANSCRIPTION-CLEAR (++) |
| C-20 | **PASS** | "One responsibility: confirm each IA lens field opens with the exact lens-phrase from Step 5. One output per team: a VERBATIM or DRIFT verdict." (++) |
| C-21 | **PASS** | PATH-B: "Emit TRANSCRIPTION-CLEAR. This block re-audits all three artifacts in one pass -- including those that were VERBATIM before the rewrites. CHART-WRITTEN cannot be emitted until this block is present." (++) |

**Aspirational = 13/13 → 10/10**

**V-02 total: 60 + 30 + 10 = 100/100** ✓ Golden

---

## V-03 — Phrasing register: declarative output-forward framing (all 13 aspirational)

**Axis**: Every criterion expressed as an output shape constraint, not a behavioral instruction. Incorrect output is visibly wrong (doesn't match described shape) rather than instruction-not-followed.

### Essential / Recommended

Same structural coverage: PARSE, VALIDATE, BUILD CONTRACT, CONTRACT-SEAL, PROFILES, IA ROLE FILES, STANDARD/SPECIALIZED ROLES, org-chart.md + transcription, BUILD-VERIFY, CROSS-REF.

| C-02 | **PASS** | Stage 8: "org-chart.md has five sections: (1) ASCII hierarchy..." |
| C-03 | **PASS** | Stage 6: "A correct build writes all IA files before any standard or specialized role file." |
| C-05 | **PASS** | Stage 7: "A correct role file contains all five fields (orientation, lens, expertise, scope, collaboration pattern). No field is a placeholder. A role file with any omitted or placeholder field is structurally invalid." |

**Essential = 60/60. Recommended = 30/30.**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | "An IA lens that could survive transplanting to a different team without rewrite is incorrect." Non-transplantability framed as structural invalidity (++) |
| C-10–C-13 | **PASS** | CROSS-REF block, VALIDATE block, CONTRACT-before-files, ARTIFACT-A contract |
| C-14 | **PASS** | "A correct ARTIFACT-B interprets the numbers with specific names" + concrete named example + "incorrect ARTIFACT-B contains no area names, no specific counts... invalid even if correct in structure" (++) |
| C-15 | **PASS** | Stage 6: "An orientation that could apply to any team's IA is incorrect. An IA lens that could survive transplanting to a different team without rewrite is incorrect." Portrait framing explicit (++) |
| C-16 | **PASS** | Stage 5: "An incorrect profile has a defended-artifact that names a category rather than a specific thing... An incorrect profile is invalid even if complete in structure." (++) |
| C-17 | **PASS** | Stage 9: "A BUILD-VERIFY block with non-verdict content is structurally invalid even if the verdicts themselves are correct." (++) |
| C-18 | **PASS** | Stage 8: "Sections 2-4 are CONTRACT ARTIFACT-A, -B, and -C. The same content. Not a rewrite. A section that differs from the sealed CONTRACT artifact is structurally incorrect." (++) |
| C-19 | **PASS** | Shape A vs Shape B defined; Shape B includes rewrite + TRANSCRIPTION-CLEAR; "A build that emits CHART-WRITTEN before TRANSCRIPTION-CLEAR after any REVISED verdict is structurally invalid." (++) |
| C-20 | **PASS** | Stage 9: "The block contains nothing else: no file-count checks, no directory checks, no headcount verifications, no summary rows. A BUILD-VERIFY block with non-verdict content is structurally invalid." (++) |
| C-21 | **PASS** | Shape B: "A correct TRANSCRIPTION-CLEAR names all three artifacts -- not only the one that was rewritten. A TRANSCRIPTION-CLEAR that names fewer than three artifacts is structurally incomplete." (++) |

**Aspirational = 13/13 → 10/10**

**V-03 total: 60 + 30 + 10 = 100/100** ✓ Golden

---

## V-04 — Lifecycle + Inertia framing: profiles as structural anchor (profile-first ordering)

**Axis**: PROFILE extracted before CONTRACT — resistance map is foundation from which headcount contract is assembled. Portrait quality and derivation are defining structural properties, not subordinate quality criteria.

**Unique structural bet**: Phase sequence is PARSE → VALIDATE → **PROFILE** → CONTRACT → CONTRACT-SEAL → WRITE-IA → WRITE-CHART → WRITE-ROLES → BUILD-VERIFY → CROSS-REF. Profiles precede the headcount contract.

### Essential / Recommended

| C-01 | **PASS** | ROLES-COMPLETE + CROSS-REF slots check |
| C-02 | **PASS** | ASCII hierarchy in WRITE-CHART |
| C-03 | **PASS** | WRITE-IA: all IA before std/spec; IA-PHASE-COMPLETE gate |
| C-04 | **PASS** | Paths from org.yaml area-slug |
| C-05 | **PASS** | Five fields, no placeholder; "Scope explicit" |

**Essential = 60/60. Recommended = 30/30.**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | "The orientation reads as what this particular person watches for, not what any IA watches for in general." |
| C-10–C-12 | **PASS** | CROSS-REF, VALIDATE, WRITE-IA before WRITE-ROLES |
| C-13 | **PASS** | CONTRACT phase (Phase 4, after PROFILE): produces ARTIFACT-A before file writes; TABLE-CLOSED states contract target |
| C-14 | **PASS** | ARTIFACT-B: 2-3 sentences with specific area names, counts, structural observation |
| C-15 | **PASS** | "The IA file is a person-portrait -- not a filled-in template. It describes the specific kind of person who would occupy this role on this team." IA-WRITTEN adds third check: "lens is team-specific (non-transplantable): YES / NO" (++) |
| C-16 | **PASS** | PROFILE phase before CONTRACT: "Resistance profiles are extracted before the headcount contract is built. The contract is assembled from profiles, not independent of them." Quality bar: category names fail (++) |
| C-17 | **PASS** | BUILD-VERIFY: SINGLE-PURPOSE GATE, VERBATIM/DRIFT per team, DRIFT rewrite before next team |
| C-18 | **PASS** | WRITE-CHART: "[TRANSCRIBE CONTRACT ARTIFACT-A verbatim]"; TRANSCRIPTION-RECEIPT after (++) |
| C-19 | **PASS** | TRANSCRIPTION-RECEIPT; REVISED → rewrite → TRANSCRIPTION-CLEAR (++) |
| C-20 | **PASS** | BUILD-VERIFY: "SINGLE-PURPOSE GATE... One output per team: VERBATIM or DRIFT. Nothing else inside this phase." (++) |
| C-21 | **PASS** | After rewrites: "emit TRANSCRIPTION-CLEAR -- one pass over all three artifacts, not only the ones that changed"; if TRANSCRIPTION-CLEAR shows REVISED: return to step 1 (++) |

**Aspirational = 13/13 → 10/10**

**V-04 total: 60 + 30 + 10 = 100/100** ✓ Golden

---

## V-05 — Full integration: all 13 aspirational criteria C-09 through C-21

**Axis**: Complete architecture — all 13 criteria simultaneously. Phase sequence: PARSE → VALIDATE → CONTRACT → CONTRACT-SEAL → PROFILE → WRITE-IA → **WRITE-ROLES** → **WRITE-CHART** → BUILD-VERIFY → CROSS-REF (WRITE-ROLES before WRITE-CHART, making org-chart.md the final document written from sealed contract artifacts after all role files exist).

### Essential / Recommended

| C-01 | **PASS** | ROLES-COMPLETE + CROSS-REF |
| C-02 | **PASS** | WRITE-CHART Phase 8: "ASCII hierarchy -- box-drawing characters, minimum two nesting levels." |
| C-03 | **PASS** | WRITE-IA Phase 6: "All Inertia Advocate files are written in this phase -- before any standard or specialized role files. IA omission is structurally impossible: an unstarted IA file means the team's entire role set has not begun." |
| C-04 | **PASS** | Paths from org.yaml |
| C-05 | **PASS** | "All five fields required for every file... No placeholder text. Scope explicit." |

**Essential = 60/60. Recommended = 30/30.**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | "No phrase applicable to any team... Strong: 'The schema contract table cannot be rewritten by a migration tool that lacks a dry-run mode.'" with strong/weak example (++) |
| C-10 | **PASS** | CROSS-REF: slots, IA count, dir check, table fidelity all enumerated |
| C-11 | **PASS** | VALIDATE: 4 checks, "No files written during this phase", halt on failures |
| C-12 | **PASS** | Phase 6 WRITE-IA before Phase 7 WRITE-ROLES; "IA omission is structurally impossible: an unstarted IA file means the team's entire role set has not begun" — makes IA prerequisite to all team files (++) |
| C-13 | **PASS** | CONTRACT Phase 3 before WRITE-IA/WRITE-ROLES/WRITE-CHART; TABLE-CLOSED: "File generation must produce exactly [n] .roles/ files" (++) |
| C-14 | **PASS** | ARTIFACT-B: 2-3 sentences; strong/weak example retained from R5; "a structural observation the table rows alone do not convey" (++) |
| C-15 | **PASS** | Portrait framing: "not a filled-in template"; "No phrase applicable to any team"; IA-WRITTEN 3-field check including "lens is team-specific (non-transplantable): YES / NO" (++) |
| C-16 | **PASS** | PROFILE Phase 5: "cannot be produced without knowing both other fields"; generic profiles fail explicitly (++) |
| C-17 | **PASS** | BUILD-VERIFY: SINGLE-PURPOSE GATE; "exactly one responsibility"; "Phase produced [n] VERBATIM/DRIFT verdicts and no other outputs. Derivation loop closed." (++) |
| C-18 | **PASS** | WRITE-CHART: "Do not recalculate. Do not reformat. Copy the sealed artifact from Phase 3." (++) |
| C-19 | **PASS** | TRANSCRIPTION-RECEIPT; REVISED triggers rewrite; "(No TRANSCRIPTION-CLEAR required -- no rewrites occurred.)" for PATH-A (++) |
| C-20 | **PASS** | BUILD-VERIFY: "NO file writes, NO structural file-count checks, NO directory comparisons, NO headcount verifications, NO AMEND generation, NO summary rows, and NO other outputs of any kind. Any content in this phase beyond per-team VERBATIM/DRIFT verdicts is a build error." (++) |
| C-21 | **PASS** | After rewrites: "This named block re-audits every contract artifact in a single pass -- including those that were already VERBATIM before any rewrite. The block must list all three. A block that names fewer than three artifacts does not satisfy the exit gate." All-VERBATIM exemption explicit (++) |

**Aspirational = 13/13 → 10/10**

**V-05 total: 60 + 30 + 10 = 100/100** ✓ Golden

---

## Ranking

| Rank | Variation | Score | Essential | Recommended | Aspirational (13) | ++ density |
|------|-----------|-------|-----------|-------------|-------------------|------------|
| 1 (tie) | **V-05** | **100/100** | 5/5 | 3/3 | 13/13 | 9/13 |
| 1 (tie) | **V-03** | **100/100** | 5/5 | 3/3 | 13/13 | 9/13 |
| 1 (tie) | **V-04** | **100/100** | 5/5 | 3/3 | 13/13 | 7/13 |
| 1 (tie) | **V-02** | **100/100** | 5/5 | 3/3 | 13/13 | 4/13 |
| 1 (tie) | **V-01** | **100/100** | 5/5 | 3/3 | 13/13 | 3/13 |

All five variations achieve perfect score. The rubric v6 is fully saturated — no criterion discriminates between the five variations at the PASS/PARTIAL/FAIL level.

---

## Excellence Signals

The rubric saturation signals rubric exhaustion. New discriminating criteria should be extracted from patterns present in V-04 and V-05 that V-01/V-02/V-03 lack.

### Signal 1 — DERIVATION-LOOP-CLOSED named attestation (V-05 only)

V-05 BUILD-VERIFY-PASS: *"Phase produced [n] VERBATIM/DRIFT verdicts and no other outputs. Derivation loop closed."*

This is new. No other variation uses "Derivation loop closed" as a named structural event. It explicitly closes the C-16→C-17 derivation chain — resistance profile produces lens-phrase (C-16), BUILD-VERIFY confirms lens-phrase survives into written file (C-17), DERIVATION-LOOP-CLOSED attests that the chain is complete as a named observable. V-01–V-04 all have BUILD-VERIFY-PASS but none name the derivation closure explicitly.

Candidate criterion: **C-22 — DERIVATION-LOOP-CLOSED attestation.** BUILD-VERIFY-PASS names the closure of the resistance-profile → IA-lens derivation chain as a structural event. Requires a named token (e.g., "Derivation loop closed") that explicitly bridges Phase 5 (PROFILE) to Phase 9 (BUILD-VERIFY) as a closed loop, not merely as two separate passes.

### Signal 2 — Non-transplantable IA enforcement at write time (V-04 and V-05)

V-04 and V-05 IA-WRITTEN check includes a third field absent from V-01/V-02:
```
lens is team-specific (non-transplantable): YES / NO
```

V-01/V-02 state the non-transplantable rule ("no boilerplate applicable to any team") but verify only `expertise concrete` per file. V-03 frames it declaratively but also has no per-file check. V-04/V-05 enforce the C-15 portrait quality as a per-file gate at write time — a NO halts and requires a rewrite before proceeding to the next team. This converts C-15 from a post-hoc quality criterion to a structural write-time gate.

Candidate criterion: **C-23 — Non-transplantable IA per-file verification.** IA-WRITTEN includes an explicit "lens is team-specific (non-transplantable): YES / NO" check that triggers a rewrite on NO before proceeding to the next team. Transforms C-15 (portrait quality as stated rule) into a structural per-file gate.

---

## Summary

```
ROUND 6 SCORECARD — corps-build
  rubric version:  v6 (C-01 through C-21, 21 criteria)
  variations:      V-01 through V-05
  all essential:   PASS (5/5 each)
  all recommended: PASS (3/3 each)
  all aspirational: PASS (13/13 each)
  scores:          V-01=100, V-02=100, V-03=100, V-04=100, V-05=100
  golden:          all five
  rubric status:   SATURATED — no criterion discriminates at R6
  extraction:      2 signals → C-22 (DERIVATION-LOOP-CLOSED), C-23 (non-transplantable per-file gate)
```

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["DERIVATION-LOOP-CLOSED attestation: BUILD-VERIFY-PASS in V-05 includes 'Derivation loop closed' as a named structural event explicitly closing the C-16->C-17 resistance-profile-to-IA-lens derivation chain; no other variation names this closure as an observable token", "Non-transplantable IA per-file enforcement: V-04 and V-05 IA-WRITTEN add 'lens is team-specific (non-transplantable): YES/NO' as a third per-file check that halts and requires rewrite on NO, converting C-15 portrait quality from a stated rule into a structural write-time gate"]}
```
