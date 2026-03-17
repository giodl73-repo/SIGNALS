systematic regression from R3 that causes C-14 to fail for all variations. The R4 variations focused on adding new mechanisms but orphaned the output template from its pre-execution placement.

---

### V-01 — Labeled Redundancy Layers

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | PASS | Glob `simulations/**/{TOPIC}-*`; `DISK_SIGNALS` assigned; zero case: "Do not infer from memory." |
| C-02 | Coverage percentage | PASS | `FOUND / PLANNED * 100`; consistency check: `COVERAGE_PCT = 100%` AND NOT_PRESENT → halt. |
| C-03 | Gap identification | PASS | `OPEN GAPS` section in template; `{namespace}/{signal-type} — NOT_PRESENT`; zero case explicit. |
| C-04 | Display-only | PASS | "DISPLAY ONLY — terminal output, no files written." [LAYER 3 gate] before Phase 3 render. |
| C-05 | Readiness verdict | PASS | `READY / CONDITIONALLY READY / NOT READY` formula in Phase 2c; connected to gap list. |
| C-06 | Namespace breakdown | PASS | All 9 rows pre-seeded in template; "(All 9 rows always rendered. Zero counts display as `0 / 0 — —`.)" |
| C-07 | Strategy cross-reference | PASS | `Strategy file: {STRATEGY_FILE_PATH}` in template; not-found: "strategy.md not found — planned baseline is empty." |
| C-08 | Recency awareness | PASS | Phase 1c: extract date, flag age > 30 days as `[STALE]`. Staleness log present. |
| C-09 | Actionable next step | PASS | `NEXT STEP: {SKILL_INVOCATION} — closes {signal-name} gap`. |
| C-10 | Structural completeness | PASS | 9-row table physically pre-seeded; zero render instruction present. |
| C-11 | Phase-gated disk-check | PASS | Named phases DISCOVER → COMPUTE → DISPLAY. [LAYER 3 gate] explicit: "If false: halt." |
| C-12 | Gap-first ordering | **FAIL** | Output template: COVERAGE → READINESS → NAMESPACE BREAKDOWN → OPEN GAPS. COVERAGE rendered before OPEN GAPS. Gap-first invariant violated. |
| C-13 | Triple-redundancy guard | **FAIL** | Three labeled layers present but target *three different* invariants (namespace completeness, named coverage, write gate) — not three redundant mechanisms for the same gap-first ordering invariant. Without C-12, the structural layer for gap-first is absent. |
| C-14 | Template-first absorption | **FAIL** | ENFORCEMENT ARCHITECTURE block describes layers but contains no output template. Output template is embedded inside Phase 3 — DISPLAY, after execution phases. |
| C-15 | Per-signal assertion chain | **FAIL** | Phase 2b: "For each signal in PLANNED_SIGNALS not found in DISK_SIGNALS: Record NOT_PRESENT." Per-signal loop present but no explicit residual formula (`GAP LIST = {P : assertion = NOT_PRESENT}`). Matches R3 V-03 failure pattern. |
| C-16 | Consequence-framed verdict | **FAIL** | READINESS section uses `READY / CONDITIONALLY READY / NOT READY`. No "Committing now means shipping without: {list}" sentence. |
| C-17 | Labeled redundancy layers | **FAIL** | Labels [LAYER 1/2/3] are present, but they identify namespace-completeness, per-signal evaluation, and write-gate — not the three C-13 gap-first mechanisms. Pass condition requires "each of the three *C-13 enforcement layers* is explicitly labeled." C-13 fails; therefore C-17 cannot satisfy its implication. |
| C-18 | Assertion table pre-seeded in template | **FAIL** | No per-signal assertion table anywhere in skill. |
| C-19 | Consequence vocabulary saturation | **FAIL** | Section titles: COVERAGE, READINESS, SIGNAL BREAKDOWN BY NAMESPACE, OPEN GAPS, NEXT STEP — standard status vocabulary throughout. |

**Essential:** 4/4 | **Recommended:** 3/3 | **Asp (C-08–C-12):** 4/5 | **Asp-2 (C-13–C-16):** 0/4 | **Asp-3 (C-17–C-19):** 0/3

**Score: 110 / 150**

---

### V-02 — Assertion Table Pre-Seeded in Template

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | PASS | Glob; `DISK_SIGNALS`; zero case: "If empty: `DISK_SIGNALS = []`." |
| C-02 | Coverage percentage | PASS | `FOUND / PLANNED * 100` from row counts; consistency check: "if `COVERAGE_PCT = 100%` and any row shows `NOT_PRESENT`, recompute." |
| C-03 | Gap identification | PASS | `OPEN GAPS: All NOT_PRESENT rows from assertion table`; zero case: "No gaps — all planned signals present." |
| C-04 | Display-only | PASS | "DISPLAY ONLY — no files written or modified." Phase 4 gate: "If false: halt. Report the write as a skill failure." |
| C-05 | Readiness verdict | PASS | Three-tier formula in Phase 3 (READY / CONDITIONALLY READY / NOT READY) connected to NOT_PRESENT row count. |
| C-06 | Namespace breakdown | PASS | 9-row NAMESPACE BREAKDOWN table pre-seeded; "(All 9 rows rendered. Zero-count rows show `0 / 0 — 0%`.)" |
| C-07 | Strategy cross-reference | PASS | `Strategy file: {PATH}` in display header; not-found case: note in output, `PLANNED_SIGNALS = []`. |
| C-08 | Recency awareness | PASS | Phase 2 assertion table column: `Age: date from filename… Append [STALE] if > 30 days old.` |
| C-09 | Actionable next step | PASS | `NEXT STEP: {SKILL_INVOCATION} — closes highest-priority gap`. |
| C-10 | Structural completeness | PASS | 9-row table in NAMESPACE BREAKDOWN pre-seeded; all 9 rows required. |
| C-11 | Phase-gated disk-check | PASS | Named phases: READ INPUTS → BUILD ASSERTION TABLE → COMPUTE → PRE-DISPLAY GATE → DISPLAY OUTPUT. Gate is an explicit named phase. |
| C-12 | Gap-first ordering | **PASS** | Display output: PER-SIGNAL ASSERTION TABLE → COVERAGE SUMMARY → NAMESPACE BREAKDOWN → OPEN GAPS. The assertion table is the primary gap identification structure (shows PRESENT/NOT_PRESENT per signal) and appears *before* COVERAGE SUMMARY. Coverage is derived from the completed table. Gap enumeration precedes the aggregate number. |
| C-13 | Triple-redundancy guard | **PASS** | Three distinct mechanisms identifiable (labels not required per R3 E-2): *Structural* — assertion table positioned before COVERAGE SUMMARY in display template. *Semantic* — consistency check ("if COVERAGE_PCT = 100% and any row shows NOT_PRESENT, recompute"); coverage computed as row count of PRESENT entries, not file count. *Execution* — Phase 2 instruction: "fill in each column… After filling the table: FOUND = count(rows where Status = PRESENT)… COVERAGE_PCT = FOUND / PLANNED * 100." Gaps must be evaluated row-by-row before coverage can be computed. All three at distinct physical locations serving distinct functions. |
| C-14 | Template-first absorption | **FAIL** | "HOW THIS SKILL WORKS" block appears before Phase 1 but contains procedural steps, not the output template. The actual display template (TOPIC STATUS sections) is at the end after all four execution phases. Template is not physically before execution instructions. |
| C-15 | Per-signal assertion chain | **PASS** | Phase 2: "For each signal in PLANNED_SIGNALS, add one row… Do not skip signals. Do not collapse rows." Fill rule: "Status: PRESENT or NOT_PRESENT." Phase 3 gap derivation: "Gaps: All rows where Status = NOT_PRESENT" — explicit residual formula. Per-signal evaluation enforced by pre-seeded table structure. |
| C-16 | Consequence-framed verdict | **FAIL** | READINESS section: `READY / CONDITIONALLY READY / NOT READY`. No "Committing now means shipping without: {list}" sentence connecting verdict to named missing signals. |
| C-17 | Labeled redundancy layers | **FAIL** | No [LAYER N] labels in skill. |
| C-18 | Assertion table pre-seeded in template | **FAIL** | Assertion table format is embedded in Phase 2 (BUILD ASSERTION TABLE) with [FILL] entries — inside an execution phase, not "physically embedded in the output template before execution instructions" as the pass condition requires. Display output references "(The completed assertion table from Phase 2 goes here)" — it doesn't pre-seed the table in the display template itself. |
| C-19 | Consequence vocabulary saturation | **FAIL** | Section titles: PER-SIGNAL ASSERTION TABLE, COVERAGE SUMMARY, NAMESPACE BREAKDOWN, OPEN GAPS, READINESS, NEXT STEP — standard status vocabulary. |

**Essential:** 4/4 | **Recommended:** 3/3 | **Asp (C-08–C-12):** 5/5 | **Asp-2 (C-13–C-16):** 2/4 | **Asp-3 (C-17–C-19):** 0/3

**Score: 125 / 150**

---

### V-03 — Consequence Vocabulary Saturation

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | PASS | Glob; `DISK_SIGNALS`; zero case: "Do not infer signals from memory or prior context." |
| C-02 | Coverage percentage | PASS | `PRESENT_COUNT / PLANNED_COUNT * 100`; contradiction halt present. |
| C-03 | Gap identification | PASS | `COMMIT RISKS (planned evidence not yet gathered)` section; `{namespace}/{signal-type} — UNVERIFIED COMMITMENT`; zero case: "All planned evidence gathered. No commit risks." |
| C-04 | Display-only | PASS | "SIGNAL INTEGRITY AUDIT — terminal display only, no artifacts written." Phase 3: "confirm in writing — 'No file was written or modified.'" |
| C-05 | Readiness verdict | PASS | `COMMIT DECISION: SAFE TO COMMIT / COMMIT WITH KNOWN EXPOSURE / DO NOT COMMIT`. Connected to commit risk list. |
| C-06 | Namespace breakdown | PASS | 9-row SIGNAL EXPOSURE BY NAMESPACE pre-seeded; "(All 9 rows rendered. Zero-coverage rows show as `0 / 0 — UNVERIFIED`.)" |
| C-07 | Strategy cross-reference | PASS | `Signal baseline: simulations/{topic}/strategy.md [FOUND / NOT FOUND]`; not-found: "No planned baseline — commit exposure is unquantifiable." |
| C-08 | Recency awareness | PASS | Phase 1 evidence age scan; `[STALE — evidence may not reflect current system]`. |
| C-09 | Actionable next step | PASS | `HIGHEST PRIORITY RISK: Run /{namespace}:{skill} to gather {signal-name}.` Named skill present. |
| C-10 | Structural completeness | PASS | 9-row namespace table pre-seeded; "(All 9 rows rendered.)" |
| C-11 | Phase-gated disk-check | PASS | Named phases: SIGNAL ACQUISITION → EXPOSURE COMPUTATION → DISPLAY GATE. Display Gate is Phase 3. |
| C-12 | Gap-first ordering | **FAIL** | Display template: COVERAGE EXPOSURE → COMMIT DECISION → SIGNAL EXPOSURE BY NAMESPACE → COMMIT RISKS → HIGHEST PRIORITY RISK. Aggregate coverage (COVERAGE EXPOSURE) appears *before* COMMIT RISKS (gap list). Same ordering failure as R3 V-03, but R3 V-03 had COMMIT RISKS before EVIDENCE GATHERED. R4 V-03 regresses on this point. |
| C-13 | Triple-redundancy guard | **FAIL** | C-12 fails; no structural mechanism for gap-first ordering. Without the template positioning layer, triple-redundancy for the gap-first invariant cannot be established. |
| C-14 | Template-first absorption | **FAIL** | TERMINAL OUTPUT section appears after EXECUTION PHASES 1–3. Template is not before execution instructions. |
| C-15 | Per-signal assertion chain | **FAIL** | Phase 2: "For each planned signal NOT found on disk: Record: `{namespace}/{signal-type}` — UNVERIFIED COMMITMENT." Per-signal loop but no explicit residual formula. "COMMIT RISK LIST is now fixed" ≠ `GAP LIST = {P : assertion = NOT_PRESENT}`. Same failure mode as R3 V-03. |
| C-16 | Consequence-framed verdict | **FAIL** | COMMIT DECISION verdict present. HIGHEST PRIORITY RISK has "Commit impact if ignored." However, no single "Committing now means shipping without: {list all essential missing signals}" sentence. Impact statement covers only the single highest-priority gap, not a consolidated ship-risk enumeration. |
| C-17 | Labeled redundancy layers | **FAIL** | No [LAYER N] labels. |
| C-18 | Assertion table pre-seeded in template | **FAIL** | No pre-seeded assertion table anywhere. |
| C-19 | Consequence vocabulary saturation | **PASS** | Every major output section uses consequence vocabulary: COVERAGE EXPOSURE, COMMIT DECISION, SIGNAL EXPOSURE BY NAMESPACE, COMMIT RISKS, HIGHEST PRIORITY RISK. Audit title: "COMMIT READINESS AUDIT." Mode: "SIGNAL INTEGRITY AUDIT." No standard status vocabulary (READINESS, OPEN GAPS, NEXT STEP) in section headings. Decision frame is architectural. |

**Essential:** 4/4 | **Recommended:** 3/3 | **Asp (C-08–C-12):** 4/5 | **Asp-2 (C-13–C-16):** 0/4 | **Asp-3 (C-17–C-19):** 1/3

**Score: 115 / 150**

---

### V-04 — Labeled Layers + Pre-Seeded Assertion Table

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | PASS | Glob; `DISK_SIGNALS`; zero case handled. |
| C-02 | Coverage percentage | PASS | `FOUND / PLANNED * 100` from assertion table rows; consistency check present. |
| C-03 | Gap identification | PASS | `OPEN GAPS (NOT_PRESENT rows, priority order)` in template; zero case: "No gaps." |
| C-04 | Display-only | PASS | "DISPLAY ONLY — no files written, no files modified." [LAYER 3 gate] in Phase 4. |
| C-05 | Readiness verdict | PASS | READINESS formula: READY / CONDITIONALLY READY / NOT READY; connected to NOT_PRESENT rows. |
| C-06 | Namespace breakdown | PASS | NAMESPACE SUMMARY labeled `[LAYER 1 — all 9 rows always present]`; 9 rows pre-seeded. |
| C-07 | Strategy cross-reference | PASS | Path in template header and Phase 1b; not-found handled. |
| C-08 | Recency awareness | PASS | Phase 1c: date parse, `[STALE]` flag. Evidence Age column in assertion table. |
| C-09 | Actionable next step | PASS | NEXT STEP: `{SKILL_INVOCATION} — closes {signal-name}`. |
| C-10 | Structural completeness | PASS | NAMESPACE SUMMARY physically pre-seeded with all 9 rows; labeled [LAYER 1]. |
| C-11 | Phase-gated disk-check | PASS | Named phases: READ INPUTS → BUILD ASSERTION TABLE [LAYER 2] → COMPUTE → DISPLAY. [LAYER 3 gate] in Phase 4. |
| C-12 | Gap-first ordering | **PASS** | Display template: PER-SIGNAL ASSERTION TABLE → COVERAGE → NAMESPACE SUMMARY → OPEN GAPS → READINESS → NEXT STEP. Assertion table (primary gap identification structure, showing per-signal PRESENT/NOT_PRESENT) appears before COVERAGE. Coverage derived from table row counts. Gap enumeration precedes aggregate number. |
| C-13 | Triple-redundancy guard | **PASS** | Three distinct mechanisms for gap-first / named-gaps invariant: *Structural* — assertion table physically before COVERAGE in display template. *Semantic* — LAYER 2 description: "A consistency check blocks any output where COVERAGE = 100% and any row is NOT_PRESENT"; coverage computed from rows. *Execution* — Phase 4 render starts with PER-SIGNAL ASSERTION TABLE before COVERAGE. Three mechanism types at distinct physical locations. LAYER labels present on related but differently-framed mechanisms (namespace completeness, per-signal evaluation, write gate). C-13 identifiability does not require labels to be specifically named as "gap-first mechanisms" — identifiability is established by structural distinctness. |
| C-14 | Template-first absorption | **FAIL** | ENFORCEMENT ARCHITECTURE block precedes execution phases but contains layer descriptions, not the output template. Output template sections (TOPIC STATUS through NEXT STEP) are inside Phase 4. Template after execution phases. |
| C-15 | Per-signal assertion chain | **PASS** | Assertion table pre-seeded in Phase 2 with [FILL] entries. Fill rule: "Status: PRESENT (On Disk = YES) or NOT_PRESENT (On Disk = NO). Do not skip or collapse rows." Phase 3: "Gap list: All rows where Status = NOT_PRESENT" — explicit residual formula. |
| C-16 | Consequence-framed verdict | **FAIL** | READINESS verdict: `READY / CONDITIONALLY READY / NOT READY`. No "Committing now means shipping without: {list}" sentence. |
| C-17 | Labeled redundancy layers | **FAIL** | [LAYER 1], [LAYER 2], [LAYER 3] labels present. However, C-17 requires the labels to identify "each of the three *C-13 enforcement layers*." The labeled layers target namespace completeness (L1), per-signal evaluation (L2), and write gate (L3) — not the three C-13 gap-first mechanisms (template position, semantic consistency check, execution render order). The C-13 mechanisms are present but unlabeled as such; the labeled layers address adjacent concerns. C-13 passes; C-17 fails because the labels don't identify the C-13 mechanisms specifically. |
| C-18 | Assertion table pre-seeded in template | **FAIL** | Assertion table with [FILL] entries is in Phase 2 — BUILD ASSERTION TABLE (an execution phase). Pass condition requires "physically embedded in the output template before execution instructions." Display output references "(Completed assertion table from Phase 2 — all rows filled.)" — referencing rather than pre-seeding. |
| C-19 | Consequence vocabulary saturation | **FAIL** | Section titles: PER-SIGNAL ASSERTION TABLE, COVERAGE, NAMESPACE SUMMARY, OPEN GAPS, READINESS, NEXT STEP — standard status vocabulary. No consequence reframe. |

**Essential:** 4/4 | **Recommended:** 3/3 | **Asp (C-08–C-12):** 5/5 | **Asp-2 (C-13–C-16):** 2/4 | **Asp-3 (C-17–C-19):** 0/3

**Score: 125 / 150**

---

### V-05 — Full Structural Closure (C-17 + C-18 + C-19)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | PASS | Glob; `DISK_SIGNALS`; zero case: "If empty: `DISK_SIGNALS = []`." |
| C-02 | Coverage percentage | PASS | `VERIFIED / TOTAL * 100`; consistency gate: `COVERAGE = 100%` AND any COMMIT RISK row → halt. |
| C-03 | Gap identification | PASS | `OPEN COMMIT RISKS` section; `{namespace}/{signal-type} — COMMIT RISK`; zero case: "No commit risks — all planned signals verified." |
| C-04 | Display-only | PASS | "COMMIT RISK AUDIT — terminal display only, no artifacts produced." [LAYER 3 gate] in Phase 4. |
| C-05 | Readiness verdict | PASS | COMMIT DECISION: SAFE TO COMMIT / COMMIT WITH KNOWN EXPOSURE / DO NOT COMMIT. Connected to COMMIT RISK row count. |
| C-06 | Namespace breakdown | PASS | COMMIT RISKS BY NAMESPACE labeled `[LAYER 1 — all 9 rows always present]`; 9 rows pre-seeded. |
| C-07 | Strategy cross-reference | PASS | `Commit baseline: {PATH}` in output header; not-found: "exposure unquantifiable." |
| C-08 | Recency awareness | PASS | Phase 1 evidence age scan; "Evidence Age" column in COMMIT RISK TABLE; `[STALE]` append. |
| C-09 | Actionable next step | PASS | HIGHEST PRIORITY RISK: `Closes with: {SKILL_INVOCATION}`. Named skill present. |
| C-10 | Structural completeness | PASS | COMMIT RISKS BY NAMESPACE pre-seeded with all 9 rows; "(All 9 rows always rendered. Zero rows show `0 / 0 — UNVERIFIED`.)" |
| C-11 | Phase-gated disk-check | PASS | Named phases: SIGNAL ACQUISITION → BUILD COMMIT RISK TABLE [LAYER 2] → COMPUTE COMMIT EXPOSURE → DISPLAY COMMIT AUDIT. [LAYER 3 gate] at Phase 4. |
| C-12 | Gap-first ordering | **FAIL** | Display template: COVERAGE EXPOSURE → COMMIT RISK TABLE → COMMIT RISKS BY NAMESPACE → OPEN COMMIT RISKS → COMMIT DECISION → HIGHEST PRIORITY RISK. COVERAGE EXPOSURE (aggregate %) appears *before* COMMIT RISK TABLE (per-signal assessment). Gap information does not precede the aggregate number. Critical ordering failure. |
| C-13 | Triple-redundancy guard | **FAIL** | C-12 fails; structural layer for gap-first ordering is absent. Three labeled layers target different concerns; none enforce gap-before-coverage. Without the structural mechanism, triple-redundancy for the gap-first invariant cannot be established. |
| C-14 | Template-first absorption | **FAIL** | ENFORCEMENT ARCHITECTURE precedes execution phases but doesn't contain the output template. Commit audit display sections appear inside/after Phase 4. Template after execution. |
| C-15 | Per-signal assertion chain | **PASS** | COMMIT RISK TABLE pre-seeded in Phase 2 with [FILL] entries. Fill rule: "Risk: COMMIT RISK (Verified = NO) or CLEARED (Verified = YES)." Phase 3: "Open commit risks (gap list): All rows where Risk = COMMIT RISK" — explicit residual. |
| C-16 | Consequence-framed verdict | **FAIL** | COMMIT DECISION verdict present. HIGHEST PRIORITY RISK: "Commit consequence if ignored: {what decision rests on unverified ground}" — consequence frame for single highest-priority gap only. No consolidated "Committing now means shipping without: {list all essential gaps}" sentence. The verdict names the count ({N} unverified) but not the specific signals in the verdict itself. |
| C-17 | Labeled redundancy layers | **FAIL** | [LAYER 1/2/3] labels present. Same failure as V-04: labels identify namespace completeness (L1), per-signal commit-risk evaluation (L2), write gate (L3) — not the three C-13 gap-first mechanisms. C-13 fails here anyway, so C-17 cannot satisfy its implication (C-17 => C-13). |
| C-18 | Assertion table pre-seeded in template | **FAIL** | COMMIT RISK TABLE with [FILL] entries appears in Phase 2 (BUILD COMMIT RISK TABLE) — an execution phase. Pass condition requires physical embedding in the output template before execution instructions. Display output: "COMMIT RISK TABLE [LAYER 2 — per-signal]: _(Completed commit risk table from Phase 2 — all rows populated.)_" — references the Phase 2 table rather than pre-seeding it. |
| C-19 | Consequence vocabulary saturation | **PASS** | Every major output section uses consequence vocabulary: COVERAGE EXPOSURE, COMMIT RISK TABLE [LAYER 2], COMMIT RISKS BY NAMESPACE [LAYER 1], OPEN COMMIT RISKS, COMMIT DECISION, HIGHEST PRIORITY RISK. Audit title: "COMMIT AUDIT." Mode: "COMMIT RISK AUDIT." No standard status vocabulary (READINESS, OPEN GAPS, COVERAGE %) in section headings. Full consequence frame architecturally embedded. |

**Essential:** 4/4 | **Recommended:** 3/3 | **Asp (C-08–C-12):** 4/5 | **Asp-2 (C-13–C-16):** 1/4 | **Asp-3 (C-17–C-19):** 1/3

**Score: 120 / 150**

---

## Summary Table

| Rank | Variation | Essential | Rec | Asp (08–12) | Asp-2 (13–16) | Asp-3 (17–19) | Score | All Essential? |
|------|-----------|-----------|-----|-------------|---------------|---------------|-------|----------------|
| 1 | V-02 Assertion Table in Output | 4/4 | 3/3 | 5/5 | 2/4 (C-13, C-15) | 0/3 | **125** | YES |
| 1 | V-04 Labeled Layers + Assertion Table | 4/4 | 3/3 | 5/5 | 2/4 (C-13, C-15) | 0/3 | **125** | YES |
| 3 | V-05 Full Synthesis | 4/4 | 3/3 | 4/5 | 1/4 (C-15) | 1/3 (C-19) | **120** | YES |
| 4 | V-03 Consequence Saturation | 4/4 | 3/3 | 4/5 | 0/4 | 1/3 (C-19) | **115** | YES |
| 5 | V-01 Labeled Layers Only | 4/4 | 3/3 | 4/5 | 0/4 | 0/3 | **110** | YES |

**All variations: R3 ceiling (135) not reached. R4 top score: 125/150.**

---

## Prediction vs. Actual

| Variation | Predicted | Actual | Analysis |
|-----------|-----------|--------|----------|
| V-01: targeted C-17 | ~130–135 | **110** | All R3 tier-2 criteria lost. Labeled layers target wrong invariants for C-17; C-12 failure (COVERAGE before OPEN GAPS) cascades to C-13, C-16 misses. |
| V-02: targeted C-18 | ~135–140 | **125** | C-14 lost (template after phases). C-18 fails (table in Phase 2, not before Phase 1). But C-12+C-13 pass via assertion-table-before-coverage pattern. |
| V-03: targeted C-19 | ~130–135 | **115** | C-19 passes. C-12 regresses vs. R3 V-03 (COVERAGE before COMMIT RISKS in R4). C-15 fails same way as R3. |
| V-04: targeted C-17+C-18 | ~140–145 | **125** | C-14 lost. C-17 fails (labels target different concerns). C-18 fails (table in execution). C-12+C-13 pass via assertion table ordering. |
| V-05: targeted all three | ~145–150 | **120** | C-12 regression (COVERAGE first) collapses C-13, C-17. C-14, C-16, C-18 all lost. C-15+C-19 pass. |

**Dominant failure mode:** All R4 variations placed the output template *after* execution phases. This single structural choice costs C-14 for all five variations. Combined with C-12 ordering regressions in three variations, R4 underperforms R3 on tier-2 criteria while partially succeeding on tier-3.

---

## Excellence Signals

### E-1: Pre-display assertion table satisfies C-12 without a dedicated OPEN GAPS-before-COVERAGE section

When PER-SIGNAL ASSERTION TABLE is the first display section (before COVERAGE), it satisfies the gap-before-coverage invariant at the display level. The assertion table IS the primary gap identification structure — showing PRESENT/NOT_PRESENT per signal before the aggregate number appears. The OPEN GAPS section becomes a filtered summary that can appear after COVERAGE without violating C-12. V-02 and V-04 exploit this: assertion table first → C-12 passes even though OPEN GAPS is later. This is a new mechanism that wasn't present in R3 variations.

### E-2: C-17 requires labels on the *C-13 enforcement mechanisms*, not on independently chosen layers

V-01 and V-04 have explicit [LAYER 1/2/3] labels, yet both fail C-17. The failure: their labels identify namespace completeness, per-signal evaluation, and write gate — not the three mechanisms that constitute C-13's triple-redundancy for gap-first ordering (structural template position, semantic consistency check, execution render order). C-17's pass condition says "each of the three *C-13 enforcement layers* is explicitly labeled." If a variation applies labels to different mechanisms than the ones C-13 evaluates, C-17 fails even though the visual form (labeled layers) is correct. Label placement must be on the right mechanisms.

### E-3: C-12 ordering is the load-bearing criterion for R4 tier-2 collapse

Three of five R4 variations (V-01, V-03, V-05) placed aggregate coverage before the gap list in their output templates, causing C-12 to fail. Since C-13 requires three mechanisms for the gap-first invariant, losing C-12 (which provides the structural mechanism) typically causes C-13 to cascade-fail. The R4 design process appears to have treated output template section ordering as an afterthought while focusing on adding labeled layers and consequence vocabulary — resulting in top-tier (tier-2 + tier-3) scores being lower than R3's floor.

---

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["Pre-display assertion table achieves C-12 gap-first ordering without a dedicated OPEN GAPS section before COVERAGE: when PER-SIGNAL ASSERTION TABLE is the first display section, it satisfies gap-before-coverage at display level because the assertion table IS the primary gap list; the downstream OPEN GAPS section is a filtered summary and can appear after COVERAGE without violating the invariant", "C-17 requires labels on the C-13 enforcement mechanisms specifically — not on any three labeled layers: variations with [LAYER 1/2/3] labels on namespace-completeness, per-signal evaluation, and write-gate fail C-17 because those labels do not identify the three C-13 gap-first mechanisms (structural template position, semantic consistency check, execution render order); visual form matches but semantic referent does not", "C-14 failure pattern: placing output templates inside execution phases (Phase 2 or Phase 4) rather than before Phase 1 blocks the absorption guarantee for all R4 variations; C-18 fails by the same mechanism — pre-seeding the assertion table in Phase 2 is not equivalent to embedding it in the output template before execution instructions"]}
```
