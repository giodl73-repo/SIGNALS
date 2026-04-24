## Quest Score — corps-build R7

### Rubric version: v7 | Variations: 5 | New criteria: C-22, C-23

---

## Per-Variation Scoring

---

### V-01 — C-22 axis: PATH label emitted as output token at execution point

**Hypothesis**: Minimal fix to R6 V-01 — add `CHART-PATH: PATH-A` or `CHART-PATH: PATH-B` emission immediately after TRANSCRIPTION-RECEIPT, before executing the path.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | CROSS-REF confirms files == org.yaml slot count. |
| C-02 | PASS | WRITE-CHART Phase 7: ASCII hierarchy, box-drawing chars, minimum two nesting levels. |
| C-03 | PASS | WRITE-IA phase writes all IA files; IA-PHASE-COMPLETE confirms n/n teams before WRITE-ROLES. |
| C-04 | PASS | CROSS-REF dir-check: areas in org.yaml vs dirs present — explicit MATCH check. |
| C-05 | PASS | WRITE-ROLES: "all five fields, no placeholder text." Scope explicit per role type. |
| C-06 | PASS | ARTIFACT-A (headcount table per area) + ARTIFACT-C (level distribution) both transcribed to org-chart.md. |
| C-07 | PASS | Scope field: "standard -- present in all teams", "specialized -- [team]", "shared -- [group]", "exec office." |
| C-08 | PASS | Phase 7 AMEND has 3 concrete options: `--area` with area list, `--levels` with level vocabulary, `--restructure` with parent > child pairs. |
| C-09 | PASS | PROFILE extracts specific defended-artifact + change-pressure + lens-phrase; BUILD-VERIFY confirms verbatim match. |
| C-10 | PASS | CROSS-REF: slots match, IA files match, dir check, table fidelity — four explicit checks. |
| C-11 | PASS | VALIDATE phase: 4 named checks (V-1 through V-4), VALIDATE-FAIL halts with no files written. |
| C-12 | PASS | "Write all IA files before any standard or specialized role files." IA-PHASE-COMPLETE gates entry to WRITE-ROLES. |
| C-13 | PASS | CONTRACT phase produces ARTIFACT-A before WRITE-IA; WRITE-CHART transcribes verbatim before WRITE-ROLES. |
| C-14 | PASS | ARTIFACT-B: 2-3 sentences, sentence 1 names largest area by %, sentence 3 structural observation. Strong example provided. |
| C-15 | PASS | WRITE-IA: "no generic stability language; no boilerplate applicable to any team." IA-WRITTEN checks expertise concrete. |
| C-16 | PASS | PROFILE phase (Phase 5) before WRITE-IA (Phase 6): defended-artifact, change-pressure, lens-phrase extracted per team. |
| C-17 | PASS | BUILD-VERIFY Phase 9: "confirm every IA lens field opens with exact lens-phrase from Phase 5." VERBATIM/DRIFT per team. |
| C-18 | PASS | CONTRACT-SEAL rule: "These artifacts are FINAL. org-chart.md sections 2-4 are copies — not regenerations." |
| C-19 | PASS | CHART-PATH: PATH-B fires on any REVISED verdict; PATH-B triggers rewrite before CHART-WRITTEN. |
| C-20 | PASS | "SINGLE-PURPOSE GATE... NO file writes, NO structural file-count checks... Any content beyond per-team VERBATIM/DRIFT verdicts is a build error." |
| C-21 | PASS | PATH-B: "This block re-audits every contract artifact in a single pass — including those already VERBATIM before the rewrite. The block covers all three or it does not serve as an exit gate." |
| **C-22** | **PASS** | "Immediately after TRANSCRIPTION-RECEIPT, emit CHART-PATH: PATH-A / CHART-PATH: PATH-B. The `CHART-PATH:` line must appear as an output token before executing the path." Explicit emission instruction at execution point. |
| **C-23** | **FAIL** | No declarative "a correct X contains..." framing for any named block. BUILD-VERIFY uses "is a build error" (procedural), not "is structurally invalid" (declarative). No block-shape correctness rule for AMEND, TRANSCRIPTION-RECEIPT, or TRANSCRIPTION-CLEAR. |

**Aspirational pass**: 14/15 (fails C-23)

**Composite**: (5/5 × 60) + (3/3 × 30) + (14/15 × 10) = 60 + 30 + **9.33** = **99**

---

### V-02 — C-23 axis: Declarative block-shape correctness rules for all named blocks

**Hypothesis**: R6 V-01 architecture + declarative "a correct X contains... an X with non-Y content is structurally invalid" rules adjacent to every named block.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Same as V-01. |
| C-02 | PASS | Same as V-01. |
| C-03 | PASS | Same as V-01. |
| C-04 | PASS | Same as V-01. |
| C-05 | PASS | Same as V-01. |
| C-06 | PASS | Same as V-01. |
| C-07 | PASS | Same as V-01. |
| C-08 | PASS | "A correct AMEND section contains exactly three options, each naming specific mechanisms drawn from org.yaml... An AMEND section with fewer than three options... is structurally incomplete." PASS. |
| C-09 | PASS | PROFILE + BUILD-VERIFY chain. |
| C-10 | PASS | CROSS-REF four checks. |
| C-11 | PASS | VALIDATE with 4 named checks. |
| C-12 | PASS | IA-PHASE-COMPLETE before WRITE-ROLES. |
| C-13 | PASS | CONTRACT before file writes; WRITE-CHART before WRITE-ROLES. |
| C-14 | PASS | ARTIFACT-B 2-3 analytic sentences. |
| C-15 | PASS | "A correct IA role file is a person-portrait... An IA role file containing generic resistance language... is structurally deficient." |
| C-16 | PASS | PROFILE before WRITE-IA. |
| C-17 | PASS | BUILD-VERIFY: per-team VERBATIM/DRIFT verdict. |
| C-18 | PASS | "TRANSCRIBE CONTRACT ARTIFACT-A verbatim — do not recalculate." |
| C-19 | PASS | PATH-B rewrite on REVISED, before CHART-WRITTEN. |
| C-20 | PASS | "A correct BUILD-VERIFY phase contains exactly N entries... A BUILD-VERIFY block containing any content other than per-team VERBATIM/DRIFT verdict entries... is structurally invalid." |
| C-21 | PASS | "A correct TRANSCRIPTION-CLEAR names all three contract artifacts... A TRANSCRIPTION-CLEAR naming fewer than three artifacts is structurally incomplete and does not serve as an exit gate." |
| **C-22** | **FAIL** | PATH-A / PATH-B defined as instruction section headers. No `CHART-PATH:` emission instruction at execution point. Labels appear in FINAL SUMMARY template but not as required output tokens within WRITE-CHART phase execution. Unnamed conditional prose gap: model executing PATH-B may print the label only in summary, not at the moment the path fires. |
| **C-23** | **PASS** | Seven blocks with declarative correctness rules: PROFILE ("structurally underspecified"), IA-WRITTEN ("structurally incomplete"), TRANSCRIPTION-RECEIPT ("structurally incomplete"), TRANSCRIPTION-CLEAR ("structurally incomplete and does not serve as an exit gate"), BUILD-VERIFY ("structurally invalid"), AMEND ("structurally incomplete"), CROSS-REF ("structurally incomplete"). Rules use "a correct X contains..." framing. |

**Aspirational pass**: 14/15 (fails C-22)

**Composite**: (5/5 × 60) + (3/3 × 30) + (14/15 × 10) = 60 + 30 + **9.33** = **99**

---

### V-03 — C-23 narrow fix: AMEND correctness rule added to R6 V-03 declarative architecture

**Hypothesis**: R6 V-03 (95 pts — PARTIAL on C-08 for missing AMEND block-shape rule) + one addition: declarative AMEND correctness rule with concrete option shapes. Stage A / Stage B naming satisfies C-22.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | CROSS-REF slots check. |
| C-02 | PASS | ASCII hierarchy in WRITE-CHART. |
| C-03 | PASS | WRITE-IA before WRITE-ROLES; IA-COMPLETE confirms n/n. |
| C-04 | PASS | CROSS-REF dir check. |
| C-05 | PASS | WRITE-ROLES all five fields. |
| C-06 | PASS | ARTIFACT-A + ARTIFACT-C transcribed to org-chart.md. |
| C-07 | PASS | Scope field explicit per role type. |
| C-08 | PASS | New AMEND correctness rule: "A correct AMEND section contains exactly three options, each citing specific values drawn from org.yaml... An AMEND section with fewer than three options... is structurally incomplete." The R6 PARTIAL is resolved. |
| C-09 | PASS | PROFILE (Stage 3, before CONTRACT) with correct/incorrect example pair. |
| C-10 | PASS | CROSS-REF four checks with declarative correctness rule. |
| C-11 | PASS | VALIDATE: "A correct VALIDATE block carries four named checks... A VALIDATE block with fewer than four checks... is structurally invalid." |
| C-12 | PASS | "All IA files before any standard or specialized role files." |
| C-13 | PASS | CONTRACT (Stage 4) after PROFILE, before WRITE-IA; WRITE-CHART before WRITE-ROLES. |
| C-14 | PASS | ARTIFACT-B: "A correct ARTIFACT-B names the largest area... An ARTIFACT-B with generic language... is structurally deficient." |
| C-15 | PASS | "A correct IA role file is a person-portrait... An IA role file containing generic resistance language... is structurally deficient." |
| C-16 | PASS | PROFILE is Stage 3 — before CONTRACT, before WRITE-IA. Deepest extraction point. |
| C-17 | PASS | BUILD-VERIFY: "A correct BUILD-VERIFY block with any content other than per-team lens-phrase comparison entries... is structurally invalid." |
| C-18 | PASS | SEAL rule: "org-chart.md sections 2-4 are the same content — not rewrites, not reformats." |
| C-19 | PASS | Shape B: rewrite on REVISED, update receipt row to VERBATIM. |
| C-20 | PASS | BUILD-VERIFY declarative rule: "contains nothing else." |
| C-21 | PASS | Shape B: "A correct TRANSCRIPTION-CLEAR names all three contract artifacts — not only the ones that were rewritten. A Shape-B exit that emits CHART-WRITTEN before TRANSCRIPTION-CLEAR is structurally invalid." |
| **C-22** | **FAIL** | Shape A / Shape B are section headers in the prompt. No instruction to emit `SHAPE: SHAPE-A` or equivalent token at execution point within WRITE-CHART. Labels appear in FINAL SUMMARY template only. Variate design note claims "equivalent named identifiers" satisfies C-22, but the emission-at-execution-point requirement is not met — same gap as R6 PATH-A/PATH-B instruction-level headers. |
| **C-23** | **PASS** | Extensive declarative framing across all blocks: PARSE, VALIDATE, PROFILE, CONTRACT, ARTIFACT-B, IA role file, TRANSCRIPTION-RECEIPT, TRANSCRIPTION-CLEAR, BUILD-VERIFY, AMEND (new addition), CROSS-REF — all have "a correct X contains..." rules with named invalidity conditions. Strongest C-23 implementation of the five variations. |

**Aspirational pass**: 14/15 (fails C-22)

**Composite**: (5/5 × 60) + (3/3 × 30) + (14/15 × 10) = 60 + 30 + **9.33** = **99**

---

### V-04 — Combined: PATH label emission + declarative block-shape correctness rules (C-22 + C-23)

**Hypothesis**: R6 V-02 step architecture (strongest PATH-A/PATH-B design) + explicit `CHART-PATH:` emission instruction + declarative correctness rules for all seven named blocks.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | CROSS-REF four checks including file count match. |
| C-02 | PASS | WRITE-CHART: ASCII hierarchy, box-drawing, minimum two nesting levels. |
| C-03 | PASS | "All IA files before any standard or specialized role files." IA-PHASE-COMPLETE gate. |
| C-04 | PASS | CROSS-REF dir check: areas in org.yaml vs dirs present. |
| C-05 | PASS | All five fields, no placeholder text, scope explicit. |
| C-06 | PASS | ARTIFACT-A (headcount) + ARTIFACT-C (level distribution) → org-chart.md. |
| C-07 | PASS | Scope field four values including exec office. |
| C-08 | PASS | "A correct AMEND section contains exactly three options, each naming specific mechanisms drawn from org.yaml... An AMEND section with fewer than three options, or with options that do not cite specific org.yaml values, is structurally incomplete." |
| C-09 | PASS | PROFILE: defended-artifact + change-pressure + lens-phrase. BUILD-VERIFY confirms verbatim. |
| C-10 | PASS | CROSS-REF four checks including table fidelity. |
| C-11 | PASS | VALIDATE: 4 named checks, no files written, halts on FAIL. |
| C-12 | PASS | IA-PHASE-COMPLETE before CHART-WRITTEN; WRITE-ROLES gated by CHART-WRITTEN. |
| C-13 | PASS | CONTRACT (Step 3) before WRITE-IA (Step 6). WRITE-CHART (Step 7) before WRITE-ROLES (Step 8). Table is pre-write contract. |
| C-14 | PASS | ARTIFACT-B three-sentence template with strong/weak contrast in CONTRACT phase. |
| C-15 | PASS | WRITE-IA: "no generic stability language; phrase not applicable to any team without rewrite." IA-WRITTEN binary checks. |
| C-16 | PASS | PROFILE (Step 5) before WRITE-IA (Step 6): specific defended-artifact, change-pressure, lens-phrase per team. |
| C-17 | PASS | BUILD-VERIFY (Step 9): profile lens-phrase vs IA lens field opening, VERBATIM/DRIFT per team. |
| C-18 | PASS | "TRANSCRIBE ARTIFACT-A/B/C verbatim." CONTRACT-SEAL rule: "No recalculation. No rewrite." |
| C-19 | PASS | PATH-B: "For each REVISED artifact: Rewrite that section in org-chart.md from the sealed CONTRACT artifact." Phase cannot exit REVISED. |
| C-20 | PASS | "A correct BUILD-VERIFY phase contains exactly N entries... A BUILD-VERIFY block with any content other than per-team VERBATIM/DRIFT verdict entries is structurally invalid." |
| C-21 | PASS | PATH-B: "A correct TRANSCRIPTION-CLEAR names all three contract artifacts... A TRANSCRIPTION-CLEAR naming fewer than three artifacts is structurally incomplete and does not serve as a PATH-B exit gate. CHART-WRITTEN may not follow PATH-B until TRANSCRIPTION-CLEAR is present and all three lines show VERBATIM." |
| **C-22** | **PASS** | "Evaluate the receipt. Emit the path you are entering as the next output line: `CHART-PATH: PATH-A` or `CHART-PATH: PATH-B`." PATH-A execution labeled "emit after CHART-PATH: PATH-A" — the label gates the execution block. Both paths named as peer structures with explicit emission before path fires. |
| **C-23** | **PASS** | Seven blocks with declarative correctness rules: PROFILE ("structurally underspecified"), IA-WRITTEN ("structurally incomplete"), TRANSCRIPTION-RECEIPT ("structurally incomplete"), TRANSCRIPTION-CLEAR ("structurally incomplete and does not serve as a PATH-B exit gate"), AMEND ("structurally incomplete"), BUILD-VERIFY ("structurally invalid"), CROSS-REF ("structurally incomplete"). Declarative framing: "a correct X contains..." throughout. |

**Aspirational pass**: 15/15

**Composite**: (5/5 × 60) + (3/3 × 30) + (15/15 × 10) = 60 + 30 + **10** = **100**

---

### V-05 — Full integration: PROFILE-before-CONTRACT + PATH label emission + declarative correctness rules

**Hypothesis**: R6 V-04's PROFILE-before-CONTRACT architecture (deepest C-16 coverage) + both R7 axes.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | CROSS-REF slots match. |
| C-02 | PASS | WRITE-CHART Phase 7: ASCII hierarchy, box-drawing, team leaf nodes show headcount in parentheses. |
| C-03 | PASS | IA-PHASE-COMPLETE: "n/n teams covered. All IA files written before standard/specialized roles." |
| C-04 | PASS | CROSS-REF dir-check match. |
| C-05 | PASS | WRITE-ROLES Phase 8: all five fields, scope explicit, no placeholders. |
| C-06 | PASS | ARTIFACT-A + ARTIFACT-C transcribed verbatim to org-chart.md. |
| C-07 | PASS | Scope field explicit: standard, specialized, shared, exec office. |
| C-08 | PASS | "A correct AMEND section contains exactly three options, each citing specific values drawn from org.yaml... An AMEND section with fewer than three options... is structurally incomplete." |
| C-09 | PASS | PROFILE Phase 3 (before CONTRACT): specific named defended-artifact, change-pressure, lens-phrase. |
| C-10 | PASS | CROSS-REF: four checks including table fidelity against CONTRACT-SEALED. |
| C-11 | PASS | VALIDATE Phase 2: 4 named checks, VALIDATE-FAIL halts all file writes. |
| C-12 | PASS | WRITE-IA Phase 6 before WRITE-CHART Phase 7 before WRITE-ROLES Phase 8. |
| C-13 | PASS | CONTRACT Phase 4 (after PROFILE, before WRITE-IA) produces ARTIFACT-A before any file writes. WRITE-CHART before WRITE-ROLES. |
| C-14 | PASS | ARTIFACT-B: 3 analytic sentences with strong example, "A correct ARTIFACT-B names the largest area... An ARTIFACT-B with language applicable to any org is structurally deficient." |
| C-15 | PASS | "A correct IA role file is a person-portrait... An IA role file containing generic resistance language... is structurally deficient." |
| C-16 | PASS | PROFILE is Phase 3 — before CONTRACT. CONTRACT-SEAL rule: "PATH selection at TRANSCRIPTION-RECEIPT determines exit shape" acknowledges profiles as causal source. FINAL SUMMARY: "profiles are causal source of CONTRACT artifacts." Deepest integration. |
| C-17 | PASS | BUILD-VERIFY Phase 9: per-team VERBATIM/DRIFT verdict against Phase 3 lens-phrase. |
| C-18 | PASS | "TRANSCRIBE CONTRACT ARTIFACT-A/B/C verbatim — do not recalculate / do not rewrite." CONTRACT-SEAL RULE: "These artifacts are FINAL... No recalculation. No rewrite." |
| C-19 | PASS | CHART-PATH: PATH-B triggers rewrite loop; phase cannot exit with any REVISED artifact. |
| C-20 | PASS | "A BUILD-VERIFY block containing any content other than per-team VERBATIM/DRIFT verdict entries — file writes, structural checks, directory comparisons, headcount verifications, summary rows, or any other output — is structurally invalid." Exhaustive invalidity enumeration. |
| C-21 | PASS | "A correct TRANSCRIPTION-CLEAR names all three contract artifacts... A TRANSCRIPTION-CLEAR naming fewer than three artifacts is structurally incomplete and does not serve as a PATH-B exit gate." |
| **C-22** | **PASS** | "Immediately after TRANSCRIPTION-RECEIPT, emit the path you are entering: `CHART-PATH: PATH-A` / `CHART-PATH: PATH-B`. The `CHART-PATH:` line must appear as an output token before executing the path." FINAL SUMMARY: "[CHART-PATH: PATH-A -- all VERBATIM, no re-audit required | CHART-PATH: PATH-B -- TRANSCRIPTION-CLEAR, all three artifacts confirmed]" — label visible in summary trace. |
| **C-23** | **PASS** | Full declarative coverage: PROFILE, ARTIFACT-B, IA role file, IA-WRITTEN receipt, TRANSCRIPTION-RECEIPT, TRANSCRIPTION-CLEAR, BUILD-VERIFY, AMEND, CROSS-REF — all have "a correct X contains..." rules with named invalidity conditions ("structurally underspecified", "structurally deficient", "incomplete", "structurally invalid"). |

**Aspirational pass**: 15/15

**Composite**: (5/5 × 60) + (3/3 × 30) + (15/15 × 10) = 60 + 30 + **10** = **100**

---

## Summary Table

| Variation | Axis | C-22 | C-23 | Aspirational | Score | Rank |
|-----------|------|------|------|-------------|-------|------|
| V-04 | C-22 + C-23 combined | PASS | PASS | 15/15 | 100 | 1 |
| V-05 | Full integration | PASS | PASS | 15/15 | 100 | 1 |
| V-01 | C-22 only | PASS | FAIL | 14/15 | 99 | 3 |
| V-02 | C-23 only | FAIL | PASS | 14/15 | 99 | 3 |
| V-03 | C-23 narrow fix | FAIL | PASS | 14/15 | 99 | 3 |

**Golden threshold check**: All 5 variations pass all essential criteria and exceed 80. All are golden-eligible. V-04 and V-05 achieve perfect score.

---

## Failure Analysis

**Why V-01 fails C-23**: The R6 V-01 base architecture uses procedural framing throughout. BUILD-VERIFY's "is a build error" is a validity statement but not in declarative register. No "a correct X contains..." rule exists for any block (AMEND, TRANSCRIPTION-RECEIPT, TRANSCRIPTION-CLEAR, PROFILE, CROSS-REF). Adding C-22 emission alone does not lift the framing register of surrounding blocks.

**Why V-02 fails C-22**: PATH-A/PATH-B labels are instruction-level section headers in WRITE-CHART. No emission instruction (`CHART-PATH: PATH-A`) is present at execution point. The labels exist only as structural labels in the prompt and as alternation in the FINAL SUMMARY template. A model correctly executing PATH-B may never emit "PATH-B" within the WRITE-CHART phase output — only in the post-build summary.

**Why V-03 fails C-22**: Same structural gap as V-02. Shape A/Shape B are section headers, not emitted output tokens. The variate design note claims "the pass condition accepts equivalent named identifiers" — this is correct but addresses only the naming requirement, not the emission-at-execution-point requirement. FINAL SUMMARY contains the label but that is post-execution.

**Why V-04 = V-05 both achieve 100**: The two new criteria (C-22: emission at execution point; C-23: declarative block-shape rules) are orthogonal. V-04 combines them on R6 V-02's step architecture. V-05 combines them on the PROFILE-before-CONTRACT architecture. Both solve both gaps fully.

---

## Excellence Signals

**From V-04 and V-05 (tied top scorers):**

**Signal 1 — Orthogonal axis combination**: C-22 and C-23 address independent dimensions (path label as output token; block validity as declarative rule). V-04 demonstrates that combining orthogonal axes on a proven base architecture produces full coverage without interaction effects. Neither change interferes with the other. The combined variation is additive.

**Signal 2 — Emission instruction placement**: V-04 and V-05 both use "Emit the path you are entering as the next output line:" immediately after TRANSCRIPTION-RECEIPT, with the execution block labeled "PATH-A execution (emit after CHART-PATH: PATH-A):" — the label gates the execution. This makes path identity enforced by output structure, not by instruction memory.

**Signal 3 — Block-shape rules at definition site**: In V-04 and V-05, each correctness rule appears adjacent to the block template it describes ("a correct TRANSCRIPTION-RECEIPT contains exactly three artifact rows... A TRANSCRIPTION-RECEIPT with fewer than three rows is structurally incomplete" — placed immediately before the TRANSCRIPTION-RECEIPT template). This makes the block self-describing. No preamble is needed to determine what makes a valid instance.

**Signal 4 — Invalidity enumeration exhaustiveness** (V-05 C-20): "A BUILD-VERIFY block containing any content other than per-team VERBATIM/DRIFT verdict entries — file writes, structural checks, directory comparisons, headcount verifications, summary rows, or any other output — is structurally invalid." The exhaustive list of prohibited content types prevents ambiguity about what "nothing else" means. V-04 uses a shorter form; V-05's form is more complete.

**Signal 5 — Causal architecture in FINAL SUMMARY** (V-05): "profiles: [n of n] teams -- specific artifact + specific pressure + lens-phrase (profiles are causal source of CONTRACT artifacts)" — the FINAL SUMMARY traces the causal chain, not just the execution sequence. This makes the PROFILE-before-CONTRACT architecture's purpose legible from the output trace alone.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
