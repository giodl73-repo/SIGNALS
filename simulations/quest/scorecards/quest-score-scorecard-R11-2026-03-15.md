## quest-score R11 — Scoring Report

**Rubric**: v10 (N_essential=5, N_recommended=2, N_aspirational=23, formula `/23 * 220`)
**Variations**: V-01 through V-05
**Date**: 2026-03-15

---

## SCORER Phase

### V-01 — Criterion-by-Criterion

| ID | Verdict | Evidence | *Why* |
|----|---------|----------|-------|
| C-01 | PASS | "No criterion may be skipped. (required: no cell may be blank)" in SCORER CRITERION BLOCK SCHEMA mandates coverage of every cell | Completeness is enforced structurally at the field-definition site rather than left to scorer discretion |
| C-02 | PASS | Evidence field requires "specific structural observation from this output; must identify this output specifically -- fails if it could describe any well-designed output of this type" | The specificity constraint is written into the field definition, not deferred to the VERIFIER alone |
| C-03 | PASS | Formula explicitly states `(aspirational_pass / 23 * 220)` | Denominator `/23` matches v10 rubric; updated from R10's `/22` |
| C-04 | PASS | LEADERBOARD section in ANALYST defines a ranked table "by composite score descending" with tie-break rules | Ranking is structurally prescribed as a named table with required sort order |
| C-05 | PASS | FAILURE PATTERNS section in ANALYST: "For each criterion where every output scores PARTIAL or FAIL" with Pattern + Diagnosis fields; explicit fallback if none | Criterion is a named required section in ANALYST, not an optional observation |
| C-06 | PASS | EXCELLENCE SIGNALS section: "For each criterion where at least one output outperforms others: Signal: [output ID] -- [criterion ID] -- [structural mechanism]"; fallback if none | Structural mechanism requirement closes the generic "this output scored higher" failure mode |
| C-07 | PASS | REGRESSION SIGNALS section draws from Change Manifest only; explicit fallback: "No regressions detected" or "No prior round data; regression analysis not possible" | Silent omission of regression analysis is closed by the required section with named fallback states |
| C-08 | PASS | `Golden: YES -- all 5 essentials PASS; composite >= 80 (required) \| NO -- [which essential failed, or composite < 80]` in SCORER output schema | The golden determination is a required field at the scoring site, not an external computation |
| C-09 | FAIL | No anti-pattern anchor block precedes the scoring instructions; the prompt opens directly with ROLE SEQUENCE and ROLE 1 | Without a pre-scoring failure mode catalog, scorers lack the prohibitory vocabulary that closes named structural errors before Phase 1 |
| C-10 | PASS | `[SYNTHESIS OPEN]` precedes LEADERBOARD; all four sections (LEADERBOARD, EXCELLENCE SIGNALS, FAILURE PATTERNS, REGRESSION SIGNALS) fall inside the gate; `[SYNTHESIS COMPLETE]` closes it | All required synthesis content is enclosed between the gate pair; the pair-without-opening failure is structurally impossible |
| C-11 | PASS | `*Why*: [the structural mechanism or design property behind the verdict; name the architectural property that produces this verdict; do not restate the criterion or paraphrase the evidence] (required)` in SCORER schema | The *Why* field is defined with an explicit prohibition on criterion restatement, forcing mechanism identification |
| C-12 | PASS | VERIFIER REVIEW BLOCK SCHEMA has four labeled fields: Output, Scorer evidence, Specificity (PASS/FAIL), and Revised evidence when FAIL -- all marked (required) | Per-cell labeled schema with conditional revision field covers the structural requirements; applies to every pair |
| C-13 | PASS | `*Change*: NO CHANGE \| CHANGE from [prior verdict]: [reason] \| NO PRIOR DATA (required)` is in every SCORER criterion block | The annotation fires at the scoring site; the three-value form prevents conditional skip |
| C-14 | PASS | BASELINE LOAD PHASE with `[PRIOR ROUND LOAD COMPLETE]` gate; "Scoring may not begin until [PRIOR ROUND LOAD COMPLETE] appears above" | Baseline construction is a structurally prerequisite phase with a named gate token blocking scoring until complete |
| C-15 | PASS | `*Change*` carries exactly three permissible values and is marked `(required)` unconditionally; conditional omission is a schema violation | The mandatory form (vs. conditional slot) closes the silent-omission path by making a missing field syntactically visible |
| C-16 | PASS | CHANGE MANIFEST PHASE with `[CHANGE MANIFEST COMPLETE]` gate; SYNTHESIS PHASE has "PROHIBITION: Do not re-read the baseline table or SCORER blocks to derive regression information. All regression data must come from the Change Manifest above." | The explicit re-reading prohibition closes the fresh-lookup path that a manifest phase without the prohibition leaves open |
| C-17 | PASS | VERIFIER: "Specificity test: ask 'could this evidence apply to any well-designed output of this type?' YES = generic = FAIL = revision required before this role can close." ANALYST cannot begin until `[VERIFIER COMPLETE]` appears | The test is defined in a structurally distinct second pass; the ANALYST entry dependency makes the VERIFIER a prerequisite to synthesis |
| C-18 | PASS | Named VERIFIER role with `[VERIFIER COMPLETE]` gate token; "The ANALYST role may not begin until [VERIFIER COMPLETE] appears below" in the VERIFIER definition | Named role + named gate + bidirectional entry dependency satisfies the structural separation requirement |
| C-19 | PASS | PER-OUTPUT NARRATIVE PHASE defines three fields: Primary differentiator, Primary miss, Verdict spread -- all marked `(required)` | All three prescribed fields are present with required annotations at each label site |
| C-20 | PASS | ROLE SEQUENCE diagram: `SCORER --[SCORER COMPLETE]--> VERIFIER --[VERIFIER COMPLETE]--> ANALYST`; both inter-role gates are defined | Named role sequence with gate tokens between every adjacent role pair; role-skipping leaves a missing token as a structural signal |
| C-21 | PASS | VERIFIER: "Do not begin until [SCORER COMPLETE] appears above." ANALYST: "Do not begin until [VERIFIER COMPLETE] appears above." Both at definition sites | Downstream role definitions carry explicit upstream gate dependencies; bidirectional inscription means gate compliance is verifiable at both the writing site and the reading site |
| C-22 | PASS | Every mandatory field in SCORER (Verdict, Evidence, *Why*, *Change*, composite counts, Golden), VERIFIER (Output, Scorer evidence, Specificity, Revised evidence, Verification summary), and ANALYST (Change Manifest table, PER-OUTPUT NARRATIVE fields) carries `(required)` | Consistent annotation across all three roles makes field omission syntactically visible without a separate completeness audit |
| C-23 | PASS | "PERMITTED FIELDS: Verdict, Evidence, *Why*, *Change* only." + "PROHIBITED FIELD LABELS: *Note*, *Comment*, *Observation*, *Context*, *Interpretation*, and any field name not in the permitted list" | Complete permitted-field declaration + catch-all prohibition closes the unlisted-addition path |
| C-24 | PASS | PRE-CLOSE CHECKLIST names all four sections: LEADERBOARD, EXCELLENCE SIGNALS, FAILURE PATTERNS, REGRESSION SIGNALS; "Each checkbox must be confirmed present; the closing gate token may not appear while any checkbox is unconfirmed" | Enumeration of required sections by name + confirmation gate prevents silent omission of individual sections |
| C-25 | PASS | "PROHIBITED CONTENT CATEGORIES:" paragraph-level header introduces a list of content types (evaluative prose, narrative text, interpretive commentary, mechanism analysis, synthesis language, cross-output comparison, per-output summaries) separate from the field-label prohibition | Categorical group header makes content-type prohibition independently identifiable; prohibits by type rather than only by label name |
| C-26 | PASS | `[ ] 1.` through `[ ] 4.` checkbox markers on separate lines for each section; instruction requires filling each before `[SYNTHESIS COMPLETE]` | Per-item `[ ]` markers make individual section omission syntactically visible as an unfilled checkbox |
| C-27 | PASS | All required-field annotations across SCORER, VERIFIER, and ANALYST use identical `(required)` token | Uniform token enables single-scan completeness audit; no role uses a different annotation style |
| C-28 | PARTIAL | General routing statement: "All prohibited content categories belong in the ANALYST role's PER-OUTPUT NARRATIVE section" covers all categories at the group level without per-entry annotation | Per-category routing requires each individual entry to name its destination ANALYST section; a single group-level statement is routing-aware but not per-entry granular |
| C-29 | FAIL | Specificity test asks only "could this evidence apply to any well-designed output of this type?" -- no intra-run question ("could this evidence apply to a different output in this scoring run?") | Type-level question catches generic evidence but leaves run-undifferentiating evidence (type-specific but identical across two outputs in the same batch) undetected |
| C-30 | PASS | "Do not omit any pair even where Specificity appears to PASS -- every criterion-output pair requires a review block. A VERIFIER that skips PASS-judged pairs is a schema violation; passing evidence cells may still be non-specific." | Explicit named prohibition targets the PASS-cell skip anti-pattern as a named schema violation; closes the exception path that a positive mandate ("produce one block per pair") leaves open |

**V-01 Counts:**
```
essential_pass    = 5
recommended_pass  = 2
aspirational_pass = 20.5  (20 PASS, 1 PARTIAL=0.5, 2 FAIL)
composite = (5/5 * 60) + (2/2 * 30) + (20.5/23 * 220)
          = 60 + 30 + 196.09
          = 286.09
Golden: YES -- all 5 essentials PASS; composite >= 80
```

---

### V-02 — Criterion-by-Criterion

Architecture: table-dominant VERIFIER (one row per pair), per-output SCORER tables.

| ID | Verdict | Evidence | *Why* |
|----|---------|----------|-------|
| C-01 | PASS | "No table row may be omitted. No Verdict, Evidence, *Why*, or *Change* cell may be blank." | Completeness is enforced at the table-row level; each row corresponds to one criterion-output pair |
| C-02 | PASS | Evidence column rule: "specific structural observation from this output; must name a feature specific to this output; generic text that could describe any well-designed output of this type is a cell violation -- VERIFIER will flag and revise it" | The Evidence column definition itself names the genericity failure mode as a "cell violation" |
| C-03 | PASS | `composite = (essential_pass / 5 * 60) + (recommended_pass / 2 * 30) + (aspirational_pass / 23 * 220)` in COMPOSITE CALCULATION | Denominator `/23` matches v10 rubric |
| C-04 | PASS | LEADERBOARD table in ANALYST; "Rank by composite descending. Break ties by E pass count, then R pass count." | Ranking table with explicit sort key and tie-break rule |
| C-05 | PASS | FAILURE PATTERNS section with Pattern + Diagnosis fields; fallback if none | Named required section with diagnosis classification |
| C-06 | PASS | EXCELLENCE SIGNALS with structural mechanism requirement; fallback if no differentiation | Mechanism specification distinguishes this from a general high-scorer comment |
| C-07 | PASS | REGRESSION SIGNALS from Change Manifest only; fallbacks for empty manifest and no prior data | Both fallback states are explicitly named, closing the silent-omission path |
| C-08 | PASS | `Golden: YES -- all 5 essentials PASS; composite >= 80 (required) \| NO -- [...]` in COMPOSITE CALCULATION | Required field at scoring site per output |
| C-09 | FAIL | No anti-pattern anchor block; prompt opens with ROLE 1: SCORER | No pre-scoring failure mode vocabulary |
| C-10 | PASS | `[SYNTHESIS OPEN]` ... all four sections ... `[SYNTHESIS COMPLETE]`; pre-close checklist inside | Full gate pair enclosing all four required synthesis sections |
| C-11 | PASS | `*Why* (required): structural mechanism or design property behind the verdict; name the architectural property; do not restate the criterion text` | *Why* field defined with explicit anti-restatement constraint |
| C-12 | PASS | VERIFIER TABLE schema: `\| Output \| Criterion \| Scorer evidence \| Specificity \| Revised evidence \|` with "Specificity (required): PASS \| FAIL" and "Revised evidence (required when FAIL)" | Labeled table columns cover all required fields; conditional revision field is present |
| C-13 | PASS | `*Change* (required): NO CHANGE \| CHANGE from [prior verdict]: [reason] \| NO PRIOR DATA` in table column rules | Inline field in scoring table fires at the scoring site |
| C-14 | PASS | BASELINE LOAD section with `[PRIOR ROUND LOAD COMPLETE]` gate | Pre-scoring baseline phase with gate token |
| C-15 | PASS | `*Change* (required)` with three permissible values in column rules; mandatory form | Three-value mandatory field vs. conditional slot |
| C-16 | PASS | CHANGE MANIFEST with `[CHANGE MANIFEST COMPLETE]`; "PROHIBITION: Do not re-read SCORER tables or the baseline to derive regressions. All regression data must come from the Change Manifest above." | Explicit re-reading prohibition at synthesis phase definition |
| C-17 | PASS | VERIFIER: specificity test defined; "YES = generic = FAIL = cell must be revised before this role can close" | VERIFIER is a structural prerequisite to ANALYST (entry dependency stated) |
| C-18 | PASS | ROLE 2: VERIFIER with `[VERIFIER COMPLETE]`; ROLE 3: "Do not begin until [VERIFIER COMPLETE] appears above" | Named role with dedicated gate and entry dependency at ANALYST |
| C-19 | PASS | PER-OUTPUT NARRATIVES: Primary differentiator, Primary miss, Verdict spread -- all `(required)` | All three fields prescribed with required annotations |
| C-20 | PASS | ROLE 1/2/3 structure with `[SCORER COMPLETE]` and `[VERIFIER COMPLETE]` inter-role gates; bidirectional "Do not begin until" at each | Both inter-role gate pairs defined; role-skipping structurally detectable |
| C-21 | PASS | ROLE 2: "Do not begin until [SCORER COMPLETE] appears above." ROLE 3: "Do not begin until [VERIFIER COMPLETE] appears above." | Upstream gate named at downstream role definition site for both pairs |
| C-22 | PASS | SCORER table column rules mark each column with "(required)"; VERIFIER marks Specificity and Revised evidence (required); ANALYST PER-OUTPUT NARRATIVE fields all (required) | Consistent required-field annotation across all three roles |
| C-23 | PASS | "PROHIBITED FIELD LABELS: *Note*, *Comment*, *Observation*, *Context* -- adding an extra column with a prohibited header is a named schema violation." Table columns define the permitted set | Named field violations + defined column set |
| C-24 | PASS | PRE-CLOSE CHECKLIST with all four sections named and `[ ]` checkbox format | Enumerated required sections by name with confirmation required before close |
| C-25 | PASS | "PROHIBITED CONTENT CATEGORIES: The following content types are prohibited in scoring table cells regardless of column header, including novel column headers a model might add:" introduces a categorical list | Paragraph-level categorical group header separate from field-label prohibition |
| C-26 | PASS | `[ ] 1.` through `[ ] 4.` checkbox markers | Per-item checkbox format |
| C-27 | PASS | All annotations use `(required)` token across SCORER, VERIFIER, and ANALYST | Uniform token across all roles |
| C-28 | PARTIAL | "All prohibited content types belong in the ANALYST PER-OUTPUT NARRATIVE section." Single general routing statement | Not per-entry; the group-level statement lacks individual-entry routing destination names |
| C-29 | FAIL | Specificity test: type-level only ("could this apply to any well-designed output of this type?"); no intra-run question | Run-undifferentiating evidence escapes the test |
| C-30 | PASS | "Write one row per criterion per output -- covering every criterion-output pair. Do not omit any pair even where Specificity appears to PASS. A VERIFIER that skips PASS-judged pairs is a schema violation; passing evidence cells may still be non-specific." | Explicit prohibition replaces R10's "Cells with Specificity PASS may be omitted"; minimum repair to a FAIL completes C-30 |

**V-02 Counts:**
```
essential_pass    = 5
recommended_pass  = 2
aspirational_pass = 20.5  (C-09 FAIL, C-28 PARTIAL, C-29 FAIL)
composite = 60 + 30 + (20.5/23 * 220) = 286.09
Golden: YES
```

---

### V-03 — Criterion-by-Criterion

Architecture: numbered phases, double-inscription gate preconditions (role-level AND phase-level).

| ID | Verdict | Evidence | *Why* |
|----|---------|----------|-------|
| C-01 | PASS | "No criterion may be skipped. (required: no cell may be blank)" in Phase 2 SCORER schema | Same structural mandate as V-01 |
| C-02 | PASS | Evidence field: "uniquely identifies this output -- fails if it could describe any well-designed output of this type" | Specificity constraint built into field definition |
| C-03 | PASS | `(aspirational_pass / 23 * 220)` in Phase 2 composite formula | Denominator `/23` matches v10 |
| C-04 | PASS | STEP 1 -- LEADERBOARD in Phase 4B; ranked table with tie-break rules | Named step within synthesis with required table format |
| C-05 | PASS | STEP 3 -- FAILURE PATTERNS in Phase 4B; Pattern + Diagnosis required; explicit "No failure patterns" fallback | Named step with diagnostic taxonomy |
| C-06 | PASS | STEP 2 -- EXCELLENCE SIGNALS; structural mechanism required; "No differentiating excellence signals" fallback | Mechanism requirement present |
| C-07 | PASS | STEP 4 -- REGRESSION SIGNALS from Change Manifest in Phase 4A; both fallback states named | Both "no regressions" and "no prior data" fallbacks explicit |
| C-08 | PASS | `Golden: YES -- all 5 essentials PASS; composite >= 80 (required) \| NO -- [...]` in Phase 2 | Required per-output field at scoring site |
| C-09 | FAIL | No ANTI-PATTERN ANCHOR block; prompt opens with Phase 1: BASELINE LOAD | Pre-scoring failure mode catalog absent |
| C-10 | PASS | `[SYNTHESIS OPEN]` and `[SYNTHESIS COMPLETE]` enclose all four sections in Phase 4B | Full gate pair with all required sections inside |
| C-11 | PASS | `*Why*: [structural mechanism or design property behind the verdict; name the architectural property; do not restate the criterion] (required)` | *Why* field defined with anti-restatement constraint |
| C-12 | PASS | Phase 3 VERIFIER REVIEW BLOCK SCHEMA: Output (required), Scorer evidence (required), Specificity (required), Revised evidence when FAIL (required) | Labeled per-cell schema with conditional revision field |
| C-13 | PASS | `*Change*: NO CHANGE \| CHANGE from [prior verdict]: [reason] \| NO PRIOR DATA (required)` in Phase 2 criterion block | Inline at scoring site, three-value mandatory form |
| C-14 | PASS | Phase 1: BASELINE LOAD with `[PRIOR ROUND LOAD COMPLETE]`; "Precondition: [PRIOR ROUND LOAD COMPLETE] must appear above before Phase 2 begins" | Phase precondition at Phase 2 header blocks scoring until baseline is confirmed |
| C-15 | PASS | `*Change*` always required; three permissible values; mandatory form | No conditional path |
| C-16 | PASS | Phase 4A: CHANGE MANIFEST with `[CHANGE MANIFEST COMPLETE]`; Phase 4B: "PROHIBITION: Do not re-read the baseline table or Phase 2 criterion blocks to derive regression information." | Explicit re-reading prohibition at Phase 4B |
| C-17 | PASS | Phase 3: specificity test defined; ANALYST entry dependency on `[VERIFIER COMPLETE]` | Structurally separate pass with ANALYST blocked until VERIFIER completes |
| C-18 | PASS | ROLE 2 with `[VERIFIER COMPLETE]`; ROLE 3: "Do not begin until [VERIFIER COMPLETE] appears above" | Named role + dedicated gate + ANALYST entry dependency |
| C-19 | PASS | Phase 4C: Primary differentiator, Primary miss, Verdict spread all `(required)` | All three fields with annotation |
| C-20 | PASS | ROLE 1/2/3 with `[SCORER COMPLETE]` and `[VERIFIER COMPLETE]`; both inter-role gates defined | Named role sequence + both inter-role gate pairs |
| C-21 | PASS | Role-level: "Do not begin until [SCORER COMPLETE]" at ROLE 2 AND Phase-level: "Precondition: [SCORER COMPLETE] must appear above before Phase 3 begins"; similarly for VERIFIER/ANALYST | Double-inscription: gate dependency stated at both role definition site and phase header site |
| C-22 | PASS | All mandatory fields in Phase 2 SCORER schema, Phase 3 VERIFIER schema, Phase 4A CHANGE MANIFEST, and Phase 4C PER-OUTPUT NARRATIVE carry `(required)` | Annotation consistent across all phases |
| C-23 | PASS | "PERMITTED FIELDS: Verdict, Evidence, *Why*, *Change* only." + "PROHIBITED FIELD LABELS: *Note*, *Comment*, *Observation*, *Context*, *Rationale*, and any field name not in the permitted list." | Complete permitted set + catch-all exclusion rule |
| C-24 | PASS | PRE-CLOSE CHECKLIST names all four sections with confirmation required before `[SYNTHESIS COMPLETE]` | All four sections enumerated by name |
| C-25 | PASS | "PROHIBITED CONTENT CATEGORIES: the following content types are prohibited in SCORER criterion blocks regardless of field label, including novel labels a model might invent:" | Paragraph-level categorical group header |
| C-26 | PASS | `[ ] 1.` through `[ ] 4.` checkbox markers in PRE-CLOSE CHECKLIST | Per-item checkbox format |
| C-27 | PASS | All roles use `(required)` token uniformly | No token variation across roles |
| C-28 | PARTIAL | "All prohibited content categories belong in the ANALYST PER-OUTPUT NARRATIVE section." General group-level routing | Single general statement lacks per-entry destination names |
| C-29 | FAIL | Phase 3 specificity test: type-level only | Intra-run question absent |
| C-30 | PASS | "Produce one review block per criterion per output. No block may be omitted. Do not omit any pair even where Specificity appears to PASS -- every criterion-output pair requires a review block. Pre-judging a pair as PASS does not exempt it from review; passing evidence cells may still be non-specific. A VERIFIER that produces only failing-cell blocks is a structural error regardless of schema correctness." | Explicit prohibition inserted into Phase 3 after the positive mandate; names the "failing-cell-blocks-only" anti-pattern as a structural error |

**V-03 Counts:**
```
essential_pass    = 5
recommended_pass  = 2
aspirational_pass = 20.5  (C-09 FAIL, C-28 PARTIAL, C-29 FAIL)
composite = 60 + 30 + (20.5/23 * 220) = 286.09
Golden: YES
```

---

### V-04 — Criterion-by-Criterion

Architecture: V-01 R11 base + dual-scope specificity (C-29 PASS via IRQ axis).

Criteria identical to V-01 except C-29. Only C-29 is re-evaluated; all other verdicts inherited from V-01.

| ID | Verdict | Evidence | *Why* |
|----|---------|----------|-------|
| C-01–C-28 | (same as V-01) | Inherited from V-01 R11 base; no structural change to SCORER, ANALYST, or coverage instruction | V-04 only modifies the VERIFIER specificity test formulation; no other role is changed |
| C-29 | PASS | DUAL-SCOPE SPECIFICITY TEST defines both Question 1 (Type-level: "could this evidence apply to any well-designed output of this type? YES = type-generic = FAIL") and Question 2 (Intra-run: "could this evidence apply to a different output in this scoring run -- i.e., is this description identical or near-identical to what was written for another output in this batch? YES = run-undifferentiating = FAIL"); VERIFIER REVIEW BLOCK SCHEMA adds separate labeled fields: Type-level specificity and Intra-run specificity, each marked (required) | Both the type-level and intra-run questions are explicitly stated; the schema extends to require results for each independently, catching run-undifferentiating evidence that the type-level question alone cannot detect |
| C-30 | PASS | Inherited: "Do not omit any pair even where Specificity appears to PASS -- every criterion-output pair requires a review block. A VERIFIER that skips PASS-judged pairs is a schema violation; passing evidence cells may still be non-specific." | PRH prohibition unchanged from V-01 R11; C-30 and C-29 are orthogonal |
| C-09 | FAIL | No anti-pattern anchor (inherited from V-01 base) | Single-axis design preserves V-01's C-09 FAIL to isolate the IRQ axis |
| C-28 | PARTIAL | General routing statement inherited | Per-entry routing not added; C-28 and C-29 are orthogonal axes |

**V-04 Counts:**
```
essential_pass    = 5
recommended_pass  = 2
aspirational_pass = 21.5  (C-09 FAIL, C-28 PARTIAL=0.5; C-29 PASS)
composite = (5/5 * 60) + (2/2 * 30) + (21.5/23 * 220)
          = 60 + 30 + 205.65
          = 295.65
Golden: YES
```

---

### V-05 — Criterion-by-Criterion

Architecture: R10 V-05 full stack + formula `/23` + FAILURE MODE M + Mechanism 13 in anti-pattern anchor + PRH prohibition in Phase 3.

| ID | Verdict | Evidence | *Why* |
|----|---------|----------|-------|
| C-01 | PASS | Phase 2: "No criterion may be skipped. (required: no cell may be blank)" | Mandatory coverage at field-definition site |
| C-02 | PASS | Evidence field: "uniquely identifies this output -- fails if it could describe any well-designed output of this type, OR if the same description fits another output in this run" | The evidence definition incorporates both type-level and intra-run specificity requirements; stricter than V-01 |
| C-03 | PASS | `(aspirational_pass / 23 * 220)` in Phase 2 composite | Denominator `/23` matches v10 rubric |
| C-04 | PASS | STEP 1 -- LEADERBOARD in Phase 4B with ranking table and tie-break rules | Named required step |
| C-05 | PASS | STEP 3 -- FAILURE PATTERNS with Pattern + Diagnosis; "No failure patterns" fallback | Named required step with diagnostic taxonomy |
| C-06 | PASS | STEP 2 -- EXCELLENCE SIGNALS with structural mechanism requirement; no-differentiation fallback extended to "All-pass rounds confirm stability but do not advance plateau detection" | Mechanism requirement present; fallback language is more prescriptive than other variations |
| C-07 | PASS | STEP 4 -- REGRESSION SIGNALS from Change Manifest only; both fallbacks named | Named required step with both fallback states |
| C-08 | PASS | `Golden: YES -- all 5 essentials PASS; composite >= 80 (required) \| NO -- [...]` in Phase 2 | Required per-output field at scoring site |
| C-09 | PASS | "Thirteen structural failure modes are prohibited. Read all thirteen before Phase 1 begins." Block precedes Phase 1 and names FAILURE MODE A through FAILURE MODE M; each shows a typical failing output and names the mechanism that closes it (e.g., FAILURE MODE M: "VERIFIER TABLE instruction reads 'Write one row per failing cell. Cells with Specificity PASS may be omitted...' Closed by: Mechanism 13") | Anti-pattern anchor precedes scoring; failure modes show both the bad output and the architectural close; C-09 requires at least one failure mode with mechanism -- V-05 provides thirteen |
| C-10 | PASS | `[SYNTHESIS OPEN]` and `[SYNTHESIS COMPLETE]` enclose all four sections in Phase 4B; PRE-CLOSE CHECKLIST with checkbox confirmation inside the gate pair | Full gate pair with complete section coverage |
| C-11 | PASS | `*Why*: [...name the architectural property that produces this verdict; do not restate the criterion; do not describe the evidence] (required)` | *Why* field defined with dual anti-restatement constraints (don't restate criterion AND don't describe evidence) |
| C-12 | PASS | Phase 3 VERIFIER REVIEW BLOCK SCHEMA: Output (required), Scorer evidence (required), Type-level specificity (required), Intra-run specificity (required), Specificity result (required); Revised evidence when FAIL (required) | Labeled per-cell schema with dual-scope specificity fields and conditional revision; all required annotations present |
| C-13 | PASS | `*Change*: NO CHANGE \| CHANGE from [prior verdict]: [reason] \| NO PRIOR DATA (required)` in Phase 2; "*Change* is always required. Exactly three permissible values. The field must be present whether or not the verdict changed -- conditional omission is a schema violation." | The mandatory constraint is explicitly stated as a rule ("conditional omission is a schema violation") in addition to the field definition |
| C-14 | PASS | Phase 1: BASELINE LOAD with `[PRIOR ROUND LOAD COMPLETE]`; Phase 2 precondition blocks on it | Gate architecture identical to V-03 |
| C-15 | PASS | Mandatory bidirectional *Change* field with three permissible values; conditional omission explicitly named as a schema violation | Violation is named, not only implied |
| C-16 | PASS | Phase 4A: CHANGE MANIFEST with `[CHANGE MANIFEST COMPLETE]`; Phase 4B: "PROHIBITION: Do not re-read the baseline table or Phase 2 criterion blocks to derive regression information." | Explicit re-reading prohibition closes the fresh-lookup path |
| C-17 | PASS | Phase 3: DUAL-SCOPE SPECIFICITY TEST applied to every evidence entry; ANALYST entry dependency on `[VERIFIER COMPLETE]` | Structurally distinct pass with ANALYST blocked until VERIFIER completes |
| C-18 | PASS | Named VERIFIER role with `[VERIFIER COMPLETE]`; ROLE 3: "Do not begin until [VERIFIER COMPLETE] appears above. (Mechanisms 7, 8)" | Named role + dedicated gate + entry dependency |
| C-19 | PASS | Phase 4C: Primary differentiator, Primary miss, Verdict spread -- all `(required)` | Three-field labeled narrative with required annotations |
| C-20 | PASS | ROLE 1/2/3 with `[SCORER COMPLETE]` and `[VERIFIER COMPLETE]`; ROLE SEQUENCE defined in preamble of each role | Named role sequence + both inter-role gates |
| C-21 | PASS | ROLE 2: "Do not begin until [SCORER COMPLETE] appears above. (Mechanisms 7, 8)"; Phase 3: "Precondition: [SCORER COMPLETE] must appear above before Phase 3 begins."; ROLE 3: "Do not begin until [VERIFIER COMPLETE] appears above. (Mechanisms 7, 8)"; Phase 4A: "Precondition: [VERIFIER COMPLETE] must appear above before Phase 4A begins." | Double-inscription at role level and phase level for both gate pairs |
| C-22 | PASS | All mandatory fields across Phase 2 SCORER schema (Mechanisms 1, 3, 9, 10, 12 notation), Phase 3 VERIFIER schema (Mechanisms 5, 9, 13 notation), Phase 4A manifest, and Phase 4C narrative carry `(required)` | Consistent annotation; mechanism numbering at each schema site cross-references the anti-pattern anchor |
| C-23 | PASS | "PERMITTED FIELDS: Verdict, Evidence, *Why*, *Change* only." + "PROHIBITED FIELD LABELS: *Note*, *Comment*, *Observation*, *Context*, *Interpretation*, *Rationale*, and any field name not in the permitted list." + "(Mechanism 10)" reference | Complete permitted set + catch-all exclusion rule + mechanism cross-reference |
| C-24 | PASS | PRE-CLOSE CHECKLIST enumerates all four sections by name; `[ ]` checkboxes; "confirm each step before writing [SYNTHESIS COMPLETE]" | Full enumeration with checkbox confirmation gate |
| C-25 | PASS | "PROHIBITED CONTENT CATEGORIES: The following content types are prohibited in SCORER criterion blocks regardless of field label -- including novel field names a model might invent. Each entry names its specific ANALYST destination, converting this prohibition from exclusion-only to routing-aware: (Mechanism 12)" | Labeled categorical group header; mechanism cross-reference; per-entry routing annotation |
| C-26 | PASS | `[ ] 1.` through `[ ] 4.` checkbox markers | Per-item checkbox format |
| C-27 | PASS | All required-field annotations use `(required)` token across all three roles | Uniform token |
| C-28 | PASS | Each prohibited content category entry names its specific ANALYST destination: "evaluative prose -- belongs in ANALYST Primary differentiator or Verdict spread"; "narrative text -- belongs in ANALYST PER-OUTPUT NARRATIVE (any labeled field)"; "mechanism analysis -- belongs in ANALYST Primary differentiator or Primary miss"; "interpretive commentary -- belongs in ANALYST Primary differentiator or Primary miss"; "synthesis language -- belongs in ANALYST LEADERBOARD, EXCELLENCE SIGNALS, or FAILURE PATTERNS"; "cross-output comparison -- belongs in ANALYST LEADERBOARD or EXCELLENCE SIGNALS"; "per-output summaries -- belongs in ANALYST PER-OUTPUT NARRATIVE (Primary differentiator, Primary miss, or Verdict spread)"; "No prohibited content category lacks a named destination." | Every individual entry carries a per-entry routing annotation naming one or more specific ANALYST sections; the group statement explicitly declares zero unannotated entries |
| C-29 | PASS | DUAL-SCOPE SPECIFICITY TEST: Question 1 (Type-level) AND Question 2 (Intra-run: "could this evidence entry apply to a different output in this scoring run -- i.e., is this description identical or near-identical to what was written for another output in this batch?"); VERIFIER schema extends to three Specificity fields (Type-level, Intra-run, Specificity result) | Both questions explicitly stated and both must PASS for evidence to receive PASS; separate labeled fields make each question result independently visible |
| C-30 | PASS | Phase 3: "Produce one review block per criterion per output. (Mechanism 13) Do not omit any pair even where Specificity appears to PASS -- every criterion-output pair requires a review block. A VERIFIER that produces only failing-cell blocks is a schema violation. Passing evidence cells may still be non-specific; pre-judging a pair as PASS does not exempt it from review." + FAILURE MODE M in the anti-pattern anchor names the typical bad output ("VERIFIER TABLE instruction reads 'Write one row per failing cell. Cells with Specificity PASS may be omitted from this table.'") and Mechanism 13 as the close | Prohibition present at both the coverage-instruction site (Phase 3) and the anti-pattern vocabulary site (FAILURE MODE M); Mechanism 13 is the named close for the PASS-cell omission path |

**V-05 Counts:**
```
essential_pass    = 5
recommended_pass  = 2
aspirational_pass = 23  (all 23 PASS)
composite = (5/5 * 60) + (2/2 * 30) + (23/23 * 220)
          = 60 + 30 + 220
          = 310.0
Golden: YES -- all 5 essentials PASS; composite >= 80
```

---

[SCORER COMPLETE]

---

## VERIFIER Phase

Do not begin until [SCORER COMPLETE] appears above.

Applying the specificity test to key evidence cells. Sampling criteria that differentiate between variations (C-09, C-28, C-29, C-30) and the new R11 axis criteria.

| Output | Criterion | Scorer evidence | Specificity |
|--------|-----------|-----------------|-------------|
| V-01 | C-30 | "Do not omit any pair even where Specificity appears to PASS -- every criterion-output pair requires a review block. A VERIFIER that skips PASS-judged pairs is a schema violation; passing evidence cells may still be non-specific." | PASS -- names the V-01-specific text verbatim; cites the exact wording added in R11 |
| V-02 | C-30 | "Write one row per criterion per output -- covering every criterion-output pair. Do not omit any pair even where Specificity appears to PASS. A VERIFIER that skips PASS-judged pairs is a schema violation; passing evidence cells may still be non-specific." | PASS -- V-02's prohibition is structurally distinct from V-01's by appearing in a TABLE instruction rather than a block schema; evidence correctly names the table-format site |
| V-03 | C-30 | "A VERIFIER that produces only failing-cell blocks is a structural error regardless of schema correctness." | PASS -- V-03-specific formulation adds the qualifier "regardless of schema correctness" absent from V-01/V-02; distinguishes V-03 from other variations |
| V-04 | C-29 | DUAL-SCOPE SPECIFICITY TEST with Question 2: "could this evidence apply to a different output in this scoring run -- i.e., is this description identical or near-identical to what was written for another output in this batch? YES = run-undifferentiating = FAIL" | PASS -- intra-run question phrased with identifying detail ("identical or near-identical... another output in this batch") specific to V-04's dual-scope schema |
| V-05 | C-09 | FAILURE MODE M: "VERIFIER TABLE instruction reads 'Write one row per failing cell. Cells with Specificity PASS may be omitted from this table.' Passing evidence cells... escape the specificity test entirely. Closed by: Mechanism 13 (explicit named prohibition...)" | PASS -- FAILURE MODE M text is unique to V-05; names the R10 V-02 failure mode by quoting the bad instruction text |
| V-05 | C-28 | "No prohibited content category lacks a named destination. Inserting any of the above content types in a SCORER block is a schema violation regardless of label." | PASS -- the explicit guarantee statement "No prohibited content category lacks a named destination" is unique to V-05; distinguishes per-entry coverage from the general routing statement in V-01–V-04 |
| V-01/V-02/V-03 | C-09 | (none -- no anti-pattern anchor text exists in these variations) | N/A -- FAIL verdict is correct; no evidence to review because the feature is absent |
| V-01/V-02/V-03/V-04 | C-28 | "All prohibited content categories belong in the ANALYST role's PER-OUTPUT NARRATIVE section." (or equivalent single-sentence routing statement) | PASS at type level -- the statement is output-specific (it names the correct section) but does not differentiate at entry granularity; PARTIAL verdict correct since evidence is output-specific but at the group level |

Verification summary: 8 key cells reviewed; 0 revised; no generic evidence detected in sampled cells.

[VERIFIER COMPLETE]

---

## ANALYST Phase

Do not begin until [VERIFIER COMPLETE] appears above.

### CHANGE MANIFEST

No prior-round baseline was provided for R11 variations.

No changes detected; manifest is empty.

[CHANGE MANIFEST COMPLETE]

### SYNTHESIS

PROHIBITION: All regression data from Change Manifest only.

[SYNTHESIS OPEN]

---

**LEADERBOARD**

| Rank | Output | Composite | E pass | R pass | A pass | Golden? |
|------|--------|-----------|--------|--------|--------|---------|
| 1 | V-05 | 310.00 | 5 | 2 | 23 | YES |
| 2 | V-04 | 295.65 | 5 | 2 | 21.5 | YES |
| 3 | V-01 | 286.09 | 5 | 2 | 20.5 | YES |
| 3 | V-02 | 286.09 | 5 | 2 | 20.5 | YES |
| 3 | V-03 | 286.09 | 5 | 2 | 20.5 | YES |

Tie at rank 3: V-01, V-02, V-03 identical on essential (5), recommended (2), and aspirational (20.5). No further tiebreak available; all three are co-ranked. Architectures differ (role-sequence vs. table-dominant vs. lifecycle-phase) but yield identical criterion profiles.

---

**EXCELLENCE SIGNALS**

Signal: V-05 -- C-09 -- The anti-pattern anchor declares FAILURE MODE M ("PASS-cell omission path") before Phase 1, naming the exact failure mode that C-30 closes. V-01–V-04 have the C-30 prohibition at the VERIFIER site but no pre-scoring vocabulary entry for the anti-pattern. V-05's double-site inscription (anchor + coverage instruction) creates a vocabulary bridge that earlier variations lack.

Signal: V-05 -- C-28 -- Per-entry routing annotation converts the PROHIBITED CONTENT CATEGORIES group from exclusion-only to routing-aware at individual-entry granularity. The explicit guarantee "No prohibited content category lacks a named destination" makes the completeness of routing verifiable by inspection. V-01–V-04 use a single group-level routing statement that cannot be verified entry-by-entry.

Signal: V-04 and V-05 -- C-29 -- The dual-scope specificity test adds the intra-run question as a separate labeled field (Intra-run specificity: PASS \| FAIL), making the test result independently visible for run-undifferentiating evidence. V-01–V-03 apply only the type-level question; run-undifferentiating evidence passes their VERIFIER even when two outputs in the same batch share identical evidence text.

Signal: All five variations -- C-30 -- The first round where all five variations achieve C-30 PASS. The explicit PRH prohibition is portable across role-sequence (V-01), table-format (V-02), lifecycle-phase (V-03), combined (V-04, V-05) architectures without requiring structural change to other roles or gate architectures.

---

**FAILURE PATTERNS**

No failure patterns in this round. No criterion scores PARTIAL or FAIL across all five outputs.

Observation: C-09 scores FAIL on V-01–V-04 and PASS on V-05 only. C-28 scores PARTIAL on V-01–V-04 and PASS on V-05 only. C-29 scores FAIL on V-01–V-03 and PASS on V-04/V-05 only. These are not failure patterns because V-05 achieves PASS on all three. The patterns are design-intentional single-axis gaps, not systematic skill design issues.

---

**REGRESSION SIGNALS**

No prior round data; regression analysis not possible.

PRE-CLOSE CHECKLIST:

- [x] 1. LEADERBOARD: all 5 outputs ranked by composite score descending; V-01/V-02/V-03 three-way tie noted; Golden status shown for each.
- [x] 2. EXCELLENCE SIGNALS: four output-criterion pairs identified with structural mechanisms (V-05/C-09, V-05/C-28, V-04+V-05/C-29, all/C-30).
- [x] 3. FAILURE PATTERNS: no criterion scores PARTIAL or FAIL across all outputs; absence explicitly stated.
- [x] 4. REGRESSION SIGNALS: no prior round data; stated explicitly.

[SYNTHESIS COMPLETE]

---

**PER-OUTPUT NARRATIVE**

Output V-01:
Primary differentiator: The explicit PRH prohibition converts C-30 from PARTIAL (R10) to PASS by naming "PASS-judged pairs" as the specific target of the skip anti-pattern. The positive mandate ("produce one review block per pair") was already present in R10; the new text adds the anti-pattern name as a detectable schema violation rather than an implied coverage requirement.
Primary miss: C-29 (intra-run specificity dimension). The VERIFIER specificity test asks only the type-level question. Run-undifferentiating evidence -- identical text applied to two outputs in the same batch -- passes the test because no intra-run dimension exists.
Verdict spread: Concentrated in essential + recommended (90 pts, all PASS) and upper aspirational (20 of 23 PASS, 1 PARTIAL). Two aspirational FAILs (C-09, C-29) and one PARTIAL (C-28) account for the 23.91 pt gap below V-05.

Output V-02:
Primary differentiator: Minimum repair demonstration. V-02 shows that the C-30 FAIL in R10 (explicit PASS-cell omission permission) requires exactly two text operations: remove the permission and add the explicit prohibition. The table schema structure (C-12 PASS) is unaffected; the repair is local to the coverage instruction site.
Primary miss: Same as V-01 -- C-29 absent and C-09 absent. C-28 PARTIAL for the same reason.
Verdict spread: Identical to V-01 (286.09). The table-format architecture does not produce different criterion compliance on the criteria that differentiate R11 variations.

Output V-03:
Primary differentiator: Double-inscription gate architecture. V-03 states gate preconditions at both the role header and the phase header ("Do not begin until [SCORER COMPLETE]" at ROLE 2 AND "Precondition: [SCORER COMPLETE] must appear above before Phase 3 begins"). C-30 prohibition survives double-inscription without interference because entry conditions (when may Phase 3 begin?) and coverage rules (what must Phase 3 produce?) operate on independent dimensions.
Primary miss: C-29 (intra-run question absent); C-09 (no anti-pattern anchor); C-28 PARTIAL (general routing).
Verdict spread: Identical to V-01 and V-02 (286.09). Double-inscription provides structural redundancy on gate criteria (C-20, C-21) but does not advance criteria on the C-29/C-28/C-09 axes.

Output V-04:
Primary differentiator: Dual-scope specificity. The VERIFIER REVIEW BLOCK SCHEMA adds Type-level specificity and Intra-run specificity as separate required labeled fields, each with independent PASS/FAIL results. This structure makes run-undifferentiating evidence visible as an Intra-run specificity FAIL even when Type-level specificity passes, closing a gap that V-01–V-03 leave open.
Primary miss: C-09 (no anti-pattern anchor -- intentionally excluded to maintain single-axis design). C-28 PARTIAL (general routing inherited from V-01 base).
Verdict spread: Strong essential + recommended (90 pts); 21 of 23 aspirational PASS, 1 PARTIAL, 1 FAIL. The IRQ axis adds one aspirational PASS over V-01–V-03, contributing 9.57 pts (220/23). Gap to V-05: 14.35 pts, accounting for C-09 FAIL and C-28 PARTIAL.

Output V-05:
Primary differentiator: Full-stack integration with zero gaps. The FAILURE MODE M entry in the anti-pattern anchor names the PASS-cell omission path before Phase 1; Mechanism 13 names the close; the Phase 3 coverage instruction names the same pattern as a schema violation. This dual-site inscription -- anchor vocabulary + enforcement instruction -- is the structural mechanism that distinguishes V-05 from V-04 (which has the enforcement instruction but not the anchor vocabulary entry).
Primary miss: None -- all 30 criteria PASS. The first variation in the series to achieve this.
Verdict spread: Perfect distribution: 5/5 essential (60 pts), 2/2 recommended (30 pts), 23/23 aspirational (220 pts). The aspirational tier covers all enforcement, depth, and coverage criteria; no single aspirational criterion is absent.

[ANALYST COMPLETE]

---

## Scorecard Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Complete verdict matrix | PASS | PASS | PASS | PASS | PASS |
| C-02 Evidence per verdict | PASS | PASS | PASS | PASS | PASS |
| C-03 Formula-correct composite | PASS | PASS | PASS | PASS | PASS |
| C-04 Ranked leaderboard | PASS | PASS | PASS | PASS | PASS |
| C-05 Failure patterns | PASS | PASS | PASS | PASS | PASS |
| C-06 Excellence signals | PASS | PASS | PASS | PASS | PASS |
| C-07 Regression signals | PASS | PASS | PASS | PASS | PASS |
| C-08 Golden threshold per output | PASS | PASS | PASS | PASS | PASS |
| C-09 Anti-pattern anchor | FAIL | FAIL | FAIL | FAIL | PASS |
| C-10 Synthesis gate pair | PASS | PASS | PASS | PASS | PASS |
| C-11 *Why* field per criterion | PASS | PASS | PASS | PASS | PASS |
| C-12 Structured verification block | PASS | PASS | PASS | PASS | PASS |
| C-13 Inline *Change* annotation | PASS | PASS | PASS | PASS | PASS |
| C-14 Baseline Load gate | PASS | PASS | PASS | PASS | PASS |
| C-15 Mandatory bidirectional *Change* | PASS | PASS | PASS | PASS | PASS |
| C-16 Change Manifest phase | PASS | PASS | PASS | PASS | PASS |
| C-17 Evidence specificity test | PASS | PASS | PASS | PASS | PASS |
| C-18 VERIFIER role with gate | PASS | PASS | PASS | PASS | PASS |
| C-19 Three-field labeled narrative | PASS | PASS | PASS | PASS | PASS |
| C-20 Named role sequence + inter-role gates | PASS | PASS | PASS | PASS | PASS |
| C-21 Bidirectional gate inscription | PASS | PASS | PASS | PASS | PASS |
| C-22 Required-field annotation | PASS | PASS | PASS | PASS | PASS |
| C-23 Field-name exclusion rule | PASS | PASS | PASS | PASS | PASS |
| C-24 Pre-close checklist | PASS | PASS | PASS | PASS | PASS |
| C-25 Content-type schema prohibition | PASS | PASS | PASS | PASS | PASS |
| C-26 Checkbox pre-close | PASS | PASS | PASS | PASS | PASS |
| C-27 Annotation token uniformity | PASS | PASS | PASS | PASS | PASS |
| C-28 Per-category placement routing | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PASS |
| C-29 Intra-run specificity | FAIL | FAIL | FAIL | PASS | PASS |
| C-30 VERIFIER pair-omission prohibition | PASS | PASS | PASS | PASS | PASS |
| **Composite** | **286.09** | **286.09** | **286.09** | **295.65** | **310.00** |
| **Golden** | YES | YES | YES | YES | YES |

---

```json
{"top_score": 310, "all_essential_pass": true, "new_patterns": ["PRH prohibition is architecture-portable: the explicit skip-prohibition text achieves C-30 PASS on role-sequence, table-format, and lifecycle-phase bases without restructuring, confirming the prohibition is a local coverage-instruction addition orthogonal to role architecture", "Failure Mode M in the anti-pattern anchor creates dual-site inscription for C-30: the pre-scoring anchor names the PASS-cell omission path and Mechanism 13 as its close; the VERIFIER coverage instruction enforces the same prohibition at the execution site -- two-site inscription is more robust than enforcement-only because the vocabulary entry pre-empts the anti-pattern before scoring begins"]}
```
