## corps-build R5 — Quest Score

### Scoring Framework

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)
```

Aspirational pool: 12 criteria (C-09 through C-20). PARTIAL counts as 0.5.

---

## V-01 — Lifecycle: SINGLE-PURPOSE GATE at BUILD-VERIFY

### Essential (C-01 – C-05)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 Role file completeness | PASS | CROSS-REF confirms "org.yaml slots [n], files written [n] -- MATCH/MISMATCH"; one-to-one check explicit |
| C-02 org-chart.md with ASCII diagram | PASS | Phase 7 WRITE-CHART: "ASCII hierarchy -- box-drawing characters, minimum two nesting levels" |
| C-03 Inertia Advocate in every team | PASS | Phase 6 WRITE-IA writes all IA files before standard/specialized; CROSS-REF "IA files: teams [n], IA files [n]" |
| C-04 org.yaml structural fidelity | PASS | CROSS-REF dir check: "areas in org.yaml [list], dirs present [list] -- MATCH/MISMATCH" |
| C-05 Role file typed fields present | PASS | "All five fields, no placeholder text"; scope explicit per file type |

**Essential: 5/5 → 60 pts**

### Recommended (C-06 – C-08)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-06 Headcount table + level distribution | PASS | CONTRACT ARTIFACT-A (headcount table with Total row) + ARTIFACT-C (level distribution); both present before files |
| C-07 Standard vs specialized distinction | PASS | Scope field explicitly labeled: "standard -- present in all teams", "specialized -- [team name]", "shared -- [group name]", "exec office" |
| C-08 AMEND section three options | PASS | Phase 7 AMEND section: --area, --levels, --restructure with specific values from org.yaml |

**Recommended: 3/3 → 30 pts**

### Aspirational (C-09 – C-20)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-09 IA team-contextualized | PASS | PROFILE phase derives lens-phrase from team-specific defended-artifact + change-pressure; "No two IA files share identical lens or expertise text" |
| C-10 Cross-ref integrity | PASS | CROSS-REF checks slot count, IA file count, dir check, table fidelity; all four MATCH/MISMATCH |
| C-11 Pre-write validation gate | PASS | Phase 2 VALIDATE: 4 checks, "No files written during this phase"; VALIDATE-FAIL halts with no files |
| C-12 IA-first ordering | PASS | "Write all Inertia Advocate files before any standard or specialized role files"; "IA-PHASE-COMPLETE: [n of n] teams covered. All IA files written before standard/specialized roles." |
| C-13 Headcount as build contract | PASS | Phase 3 CONTRACT produces ARTIFACT-A before any files; TABLE-CLOSED count drives file generation; "File generation must produce exactly [n] .roles/ files" |
| C-14 Analytic narrative prose | PASS | ARTIFACT-B: 2-3 sentences; strong/weak example pair; "Name the largest area by headcount and express as percentage"; no generic summaries |
| C-15 IA as person-portrait | PASS | Lens: "no generic stability language; no boilerplate applicable to any team"; orientation: "specific concern, not generic caution"; IA-WRITTEN verifies concrete expertise per file |
| C-16 Resistance profile pre-IA | PASS | Phase 5 PROFILE: defended-artifact + change-pressure + lens-phrase per team; PROFILE-GATE before WRITE-IA; collision check |
| C-17 CROSS-REF lens-phrase at build-complete | PASS | Phase 9 BUILD-VERIFY runs after WRITE-ROLES; explicit "profile lens-phrase vs IA lens field opening" comparison per team; before CROSS-REF |
| C-18 Contract verbatim transcription | PASS | CONTRACT-SEAL RULE: "Do not recalculate headcount. Do not rewrite the analytic prose. Do not reformat the level table. Compliance is audited via TRANSCRIPTION-RECEIPT in Phase 7." |
| C-19 TRANSCRIPTION-RECEIPT self-correcting | **PARTIAL** | Per-artifact VERBATIM/REVISED verdict present; "Any REVISED -> rewrite that section from the sealed artifact. Reemit that receipt line showing VERBATIM before proceeding." "TRANSCRIPTION-PASS: all artifacts VERBATIM" is asserted — but no named TRANSCRIPTION-CLEAR block with an explicit re-audit loop. A model can rewrite one artifact and assert TRANSCRIPTION-PASS without re-auditing the other two. Exit guard is behavioral, not structural. |
| C-20 BUILD-VERIFY single-purpose phase | PASS | SINGLE-PURPOSE GATE declaration at Phase 9 entry: "This phase contains NO file writes, NO structural file-count checks, NO directory comparisons, NO headcount verifications, NO AMEND generation, and NO summary rows. Any content beyond per-team VERBATIM/DRIFT verdicts inside this phase block is a build error." |

**Aspirational: 11.5/12 → 9.58 pts**

**V-01 Composite: 60 + 30 + 9.58 = 99.58 → 99**

---

## V-02 — Output format: TRANSCRIPTION-RECEIPT with phase-exit guard

### Essential / Recommended

All essential and recommended criteria satisfied at the same level as V-01 (same core architecture with equivalent coverage). **5/5 essential → 60 pts | 3/3 recommended → 30 pts**

### Aspirational (C-09 – C-20)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-09 | PASS | PROFILE phase with defended-artifact + change-pressure; lens-phrase required; no two IA files share text |
| C-10 | PASS | CROSS-REF Phase 8: org.yaml slot count, IA file count, dir check, table fidelity |
| C-11 | PASS | Phase 2 VALIDATE: 4 named checks, no files; VALIDATE-FAIL halts |
| C-12 | PASS | Phase 6a writes all IA before Phase 6c standard/specialized; "IA-PHASE-COMPLETE: [n of n] teams" |
| C-13 | PASS | Phase 3 CONTRACT produces ARTIFACT-A before files; explicitly "source for org-chart.md sections 2-4; not rewritten at write time" |
| C-14 | PASS | ARTIFACT-B: 2-3 sentences; "Name specific areas, counts, and findings" |
| C-15 | PASS | Lens "2-3 sentences; no generic stability language"; orientation from defended-artifact; "expertise: anchored to defended-artifact; differs from every other team's IA" |
| C-16 | PASS | Phase 5 PROFILE before Phase 6 WRITE; lens-phrase "cannot be written without knowing both fields" |
| C-17 | PASS | Phase 7 BUILD-VERIFY: "profile lens-phrase vs IA lens field opening" per team; after ROLES-COMPLETE; before CROSS-REF |
| C-18 | PASS | CONTRACT-SEAL RULE: "org-chart.md sections 2-4 ARE these artifacts. Any revision between CONTRACT-SEAL and CHART-WRITTEN is a build failure." |
| C-19 TRANSCRIPTION-RECEIPT self-correcting | PASS | PHASE-EXIT GUARD explicitly named: "Before emitting CHART-WRITTEN, re-audit all three receipt verdicts. If any verdict is not VERBATIM, return to step 1 above for that artifact." TRANSCRIPTION-CLEAR block required: "all three confirmed -- phase exit authorized" followed by CHART-WRITTEN |
| C-20 BUILD-VERIFY single-purpose | PASS | Phase 7 BUILD-VERIFY is a discrete named phase; stated purpose is solely IA lens verification; produces one VERBATIM/DRIFT verdict per team; runs before CROSS-REF; no extraneous content evident in phase definition |

**Aspirational: 12/12 → 10 pts**

**V-02 Composite: 60 + 30 + 10 = 100**

---

## V-03 — Phrasing register: declarative output-forward framing

### Essential / Recommended

Equivalent coverage to V-01/V-02. Parse → Validate → Contract → Seal → Profile → Write IA → Write Roles → Write chart + receipt → BUILD-VERIFY → CROSS-REF. **5/5 essential → 60 pts | 3/3 recommended → 30 pts**

### Aspirational (C-09 – C-20)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-09 | PASS | Stage 5 resistance profiles with team-specific defended-artifact; lens-phrase "cannot be produced without knowing both other fields"; "correct IA file cannot be used for a different team without substantive rewrite" |
| C-10 | PASS | Stage 9 CROSS-REF: org.yaml slots, IA files, table fidelity checks |
| C-11 | PASS | Stage 2 VALIDATE: four conditions checked before any write; "list it and halt" on failure |
| C-12 | PASS | Stage 6 writes all IA files before Stage 7 standard/specialized; "IA-COMPLETE: [n of n] teams" gate |
| C-13 | PASS | "Before any file is written, three contract artifacts are produced"; CONTRACT-DRAFT block; sealed before file generation |
| C-14 | PASS | ARTIFACT-B strong example: specific percentages, specific team names, structural observation; weak example contrasted |
| C-15 | PASS | "A correctly produced IA file: lens opens with the resistance profile lens-phrase verbatim. Expertise names the specific defended-artifact. The file cannot be used for a different team without substantive rewrite." — declarative portrait standard |
| C-16 | PASS | Stage 5 resistance profiles required; "A correct lens-phrase cannot be produced without knowing both defended-artifact and change-pressure" — derivation constraint expressed declaratively |
| C-17 | PASS | Stage 8 BUILD-VERIFY runs after all role files; per-team VERBATIM/DRIFT verdicts; before CROSS-REF |
| C-18 | PASS | "Sections 2-4 are CONTRACT ARTIFACT-A, -B, and -C. The same content, not a rewrite." Explicit in stage description |
| C-19 TRANSCRIPTION-RECEIPT self-correcting | PASS | "CHART-WRITTEN appears only after TRANSCRIPTION-CLEAR, which lists all three artifacts as VERBATIM. **A build that emits CHART-WRITTEN before TRANSCRIPTION-CLEAR is structurally invalid.**" TRANSCRIPTION-CLEAR block as required output shape; per-artifact VERBATIM/REVISED verdicts shown as "correct receipt" example |
| C-20 BUILD-VERIFY single-purpose | PASS | Declarative shape constraint: "The BUILD-VERIFY block contains exactly N lines, where N is the number of teams. Each line is one VERBATIM or DRIFT verdict. **The block contains nothing else**: no file-count checks, no directory checks, no headcount verifications, no summary rows, no other outputs." — constraint expressed as output shape |

**Aspirational: 12/12 → 10 pts**

**V-03 Composite: 60 + 30 + 10 = 100**

---

## V-04 — Combination: C-19 + C-20 together

### Essential / Recommended

Fully equivalent to V-01 structure; same phase sequence; same file/AMEND coverage. **5/5 → 60 pts | 3/3 → 30 pts**

### Aspirational (C-09 – C-20)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-09 | PASS | STEP 5 PROFILE with defended-artifact + change-pressure; lens-phrase "cannot be written without knowing both other fields" |
| C-10 | PASS | STEP 10 CROSS-REF: slot count, IA count, dir check, table fidelity |
| C-11 | PASS | STEP 2 VALIDATE: 4 checks, no files written; VALIDATE-FAIL halts |
| C-12 | PASS | STEP 6 WRITE-IA before STEP 8 WRITE-ROLES; "IA-PHASE-COMPLETE: [n of n] teams" gate |
| C-13 | PASS | STEP 3 CONTRACT produces ARTIFACT-A before files; sealed in STEP 4; "contract cannot be revised" |
| C-14 | PASS | ARTIFACT-B: 2-3 sentences; "No generic summaries. Name specific areas, counts, and findings." |
| C-15 | PASS | Lens: "2-3 sentences; no generic stability language"; orientation "specific concern"; expertise "anchored to defended-artifact; differs from every other team's IA" |
| C-16 | PASS | STEP 5 PROFILE before STEP 6 WRITE-IA; lens-phrase "cannot be written without knowing both other fields" |
| C-17 | PASS | STEP 9 BUILD-VERIFY: profile lens-phrase vs IA lens field opening per team; runs after ROLES-COMPLETE; before CROSS-REF |
| C-18 | PASS | CONTRACT-SEAL RULE: "org-chart.md sections 2-4 are copies of ARTIFACT-A, -B, -C. Any revision is a build failure." |
| C-19 TRANSCRIPTION-RECEIPT self-correcting | PASS | PHASE-EXIT GUARD explicitly in STEP 7: "After all rewrites, re-audit all three receipt verdicts. The phase cannot close until all show VERBATIM." TRANSCRIPTION-CLEAR block: "all three confirmed -- CHART-WRITTEN authorized"; FINAL SUMMARY cites "CLEAR (all three artifacts VERBATIM at phase exit -- C-19 satisfied)" |
| C-20 BUILD-VERIFY single-purpose | PASS | SINGLE-PURPOSE GATE in STEP 9: "exactly one responsibility... exactly one output per team... NO file writes, NO structural checks, NO directory comparisons, NO headcount verifications, and NO summary rows. Any content beyond per-team VERBATIM/DRIFT verdicts is a build error." BUILD-VERIFY-PASS confirms "Phase contained [n] VERBATIM/DRIFT verdicts and no other outputs." |

**Aspirational: 12/12 → 10 pts**

**V-04 Composite: 60 + 30 + 10 = 100**

---

## V-05 — Full integration: all 12 aspirational criteria

### Essential / Recommended

Identical phase coverage to other variations; most explicit per-field descriptions; WRITE-ROLES covers all role types (standard, specialized, shared group, exec office). **5/5 → 60 pts | 3/3 → 30 pts**

### Aspirational (C-09 – C-20)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-09 | PASS | PROFILE phase with generic-profile failure condition: "Generic profiles (e.g., 'defends stability against change') fail this phase"; lens-phrase "cannot be produced without knowing both other fields"; LENS-COLLISION forces revision |
| C-10 | PASS | PHASE 10 CROSS-REF: 4 checks; CROSS-REF-FAIL names specific missing files |
| C-11 | PASS | PHASE 2 VALIDATE: "No files written. Proceeding to CONTRACT." on PASS; "No files written. Halt." on FAIL; 4 explicit checks |
| C-12 | PASS | PHASE 6 WRITE-IA: "IA omission is structurally impossible: an unstarted IA file means the team's entire role set has not begun"; "IA-PHASE-COMPLETE: [n of n] teams covered. IA files written before standard/specialized." |
| C-13 | PASS | PHASE 3 CONTRACT: ARTIFACT-A is first output; TABLE-CLOSED count constrains file count: "File generation must produce exactly [n] .roles/ files"; PHASE 7 WRITE-ROLES enters only after CHART-WRITTEN |
| C-14 | PASS | ARTIFACT-B strong/weak example pair; "a structural observation the table rows alone do not convey"; "referencing the dominant level" in seniority sentence |
| C-15 | PASS | Most explicit portrait language: "No phrase that reads as generic stability language. The lens describes a specific viewpoint anchored to this team's domain — the specific tension, not the general concept." Strong/weak examples for orientation. Expertise: "Names a concrete artifact, system, or practice this person would defend. Not a category." |
| C-16 | PASS | PHASE 5 PROFILE with most explicit requirements: defended-artifact = "a named thing, not a category"; change-pressure = "a named initiative, not a generic force"; generic profiles explicitly fail the phase |
| C-17 | PASS | PHASE 9 BUILD-VERIFY after PHASE 7 WRITE-ROLES; explicit phase entry before CROSS-REF; per-team lens phrase vs profile trace; DRIFT triggers rewrite and re-emit; BUILD-VERIFY-PASS: "Derivation loop closed" |
| C-18 | PASS | "Do not recalculate. Do not reformat. Copy from Phase 3." Three separate "[TRANSCRIBE ... verbatim]" instructions; TRANSCRIPTION-CLEAR required before CHART-WRITTEN |
| C-19 TRANSCRIPTION-RECEIPT self-correcting | PASS | PHASE-EXIT GUARD explicitly: "Re-audit all three receipt verdicts. If any verdict is not VERBATIM, return to step 1 for that artifact. The phase cannot close until all three show VERBATIM." TRANSCRIPTION-CLEAR block required before CHART-WRITTEN; FINAL SUMMARY cites "TRANSCRIPTION-CLEAR (all 3 artifacts VERBATIM at phase exit -- C-18/C-19)" |
| C-20 BUILD-VERIFY single-purpose | PASS | SINGLE-PURPOSE GATE in PHASE 9 with most exhaustive prohibition: "NO file writes, NO structural file-count checks, NO directory comparisons, NO headcount verifications, NO AMEND generation, NO summary rows, **and NO other outputs of any kind.** Any content in this phase beyond per-team VERBATIM/DRIFT verdicts is a build error." FINAL SUMMARY cites "single-purpose phase, no other outputs -- C-17/C-20" |

**Aspirational: 12/12 → 10 pts**

**V-05 Composite: 60 + 30 + 10 = 100**

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60 | 30 | 9.58 (11.5/12) | **99** |
| V-02 | 60 | 30 | 10 (12/12) | **100** |
| V-03 | 60 | 30 | 10 (12/12) | **100** |
| V-04 | 60 | 30 | 10 (12/12) | **100** |
| V-05 | 60 | 30 | 10 (12/12) | **100** |

**Rank**: V-05 = V-04 = V-03 = V-02 (100) > V-01 (99)

The tie at 100 is meaningful: four variations independently reach the ceiling. Differentiation falls to architecture completeness — V-05 is the reference integration; V-03 introduces a novel mechanism (declarative output-forward framing) orthogonal to V-05's lifecycle structure.

---

## Excellence Signals

### Top variation: V-05 (full integration reference)

**Signal 1 — Per-criterion attribution in FINAL SUMMARY**

V-05's FINAL SUMMARY line for each mechanism names the criterion it satisfies:

```
org-chart.md:  TRANSCRIPTION-CLEAR (all 3 artifacts VERBATIM at phase exit -- C-18/C-19)
build-verify:  PASS ([n of n] verdicts; single-purpose phase, no other outputs -- C-17/C-20)
```

This creates auditable output — a reader can verify compliance without the rubric. Criteria satisfied at write time are cited in the artifact itself. No previous variation in R1–R4 included criterion attribution in the FINAL SUMMARY.

**Signal 2 — Exhaustive prohibition list in SINGLE-PURPOSE GATE**

V-05's gate enumerates every prohibited category individually:

> "NO file writes, NO structural file-count checks, NO directory comparisons, NO headcount verifications, NO AMEND generation, NO summary rows, and NO other outputs of any kind."

The phrase "and NO other outputs of any kind" is a catch-all that closes any gap left by the enumeration. V-01 and V-04 use the same structure but V-05 adds "of any kind" as the final term, making the prohibition exhaustively closed rather than exemplary-closed.

**Signal 3 — Structural impossibility framing for IA omission (V-05 on C-12)**

> "IA omission is structurally impossible: an unstarted IA file means the team's entire role set has not begun."

Prior variations said "write IA before standard/specialized." V-05 reframes this as a structural invariant about what "team not yet begun" means. This framing prevents silent skip rather than prohibiting it after the fact.

### Notable from V-03 (declarative output-forward mechanism)

**Signal 4 — Constraints as output shape descriptions**

V-03 expresses structural requirements as descriptions of what correct output looks like rather than instructions for what to do:

> "The BUILD-VERIFY block contains exactly N lines, where N is the number of teams. Each line is one VERBATIM or DRIFT verdict. The block contains nothing else."

> "A build that emits CHART-WRITTEN before TRANSCRIPTION-CLEAR is structurally invalid."

This is a different enforcement mechanism from V-05's prohibition list. Where V-05 instructs what is prohibited, V-03 describes what correct output looks like, making the constraint a format constraint the model matches rather than a behavioral rule it follows. Both reach C-20 PASS; the mechanisms are complementary rather than redundant.

---

## New Patterns for v6 Consideration

Two patterns from the top-scoring variations are not captured by any of C-01 through C-20:

**Pattern A — FINAL SUMMARY per-criterion attribution**
Each mechanism-level line in the FINAL SUMMARY cites the criterion it satisfies (e.g., "-- C-18/C-19", "-- C-17/C-20"). Makes the output self-documenting with respect to the rubric. Currently C-17/C-18/C-19/C-20 require the mechanism to appear in the output; none require the output to declare which criterion it satisfies.

**Pattern B — Declarative output-forward shape constraints**
Expressing structural requirements as descriptions of correct output ("The BUILD-VERIFY block contains exactly N lines") rather than behavioral instructions ("Do not add other content"). Turns enforcement from a procedural rule into a format contract. V-03 demonstrates this achieves C-19 and C-20 PASS at 100 via a different mechanism than V-05's explicit prohibition list.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["FINAL-SUMMARY per-criterion attribution: each mechanism line cites its criterion ID (C-18/C-19, C-17/C-20), making compliance auditable in the output itself without external rubric reference", "Declarative output-forward shape constraints: structural requirements expressed as descriptions of correct output rather than behavioral prohibitions, turning enforcement into a format contract the model matches"]}
```
