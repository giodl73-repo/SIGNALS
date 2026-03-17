Written to `simulations/quest/rubrics/quest-score-rubric-v18-2026-03-15.md`.

---

## v17 -> v18 changes

**One new criterion -- C-46** extracted from **ES-R18** (anti-pattern anchor coverage pattern):

**C-46: Anti-pattern anchor -- C-45 failure mode as a named entry covering the inline-marker vs dedicated-label distinction** (enforcement)

**Derivation chain:** C-33 -> C-36 -> C-45 -> C-46

**What it closes:** V-01 R18 demonstrates that the anti-pattern anchor carries a named entry (Failure Mode I) for the C-45 failure pattern -- inline "(N)" markers embedded in prose vs dedicated "Req N:" label lines. C-45 PASS requires numbered enumeration at every multi-component definition site but does not require the anti-pattern anchor to name this failure mode. Without a named entry, a reader encountering a draft with inline markers cannot use the anti-pattern anchor to identify the violation pattern by name and trace it to the closing criterion. C-46 closes this by requiring the anti-pattern anchor to include: Req 1 -- a named entry with typical bad output showing inline markers or prose-only requirements; Req 2 -- a closing mechanism citing C-45 (following the C-36 criterion-indexed pattern).

**Formula:** denominator 38 -> 39. `(aspirational_pass/39 x 220)`, max 310 unchanged.

**R18 open aspirationals per variation:**
- V-01 R18: none -- ceiling achieved (310.0), all 38 prior aspirationals PASS; C-46 PASS (Failure Mode I in ANTI-PATTERN ANCHOR already present in V-01 R18 architecture)
- V-02 R18: C-45 PARTIAL; C-46 new
- V-03 R18: C-43 FAIL; C-45 new; C-46 new
- V-04 R18: C-43 PARTIAL (req 3 not met); C-45 new; C-46 new
- V-05 R18: C-43 PARTIAL (req 2 not met); C-45 new; C-46 new

**R19 ceiling target:** single variation inheriting V-01 R18 architecture (all 38 prior aspirationals PASS including C-45 PASS via three-site enumeration + C-46 PASS via Failure Mode I in ANTI-PATTERN ANCHOR with C-45 criterion ID reference in the closing mechanism).

---

**C-43 and C-44 pass conditions updated in v18:** The v17 rubric stated C-43 and C-44's multi-component requirements in prose form -- exactly the failure mode C-45 and C-46 are designed to close. v18 corrects this: C-43's pass condition is enumerated as Req 1 / Req 2 / Req 3 at the definition site; C-44's pass condition is enumerated as Req 1 / Req 2. This makes the rubric itself C-45-compliant.
 new; C-46 new
- V-04 R18: C-43 PARTIAL (req 3 not met); C-45 new; C-46 new
- V-05 R18: C-43 PARTIAL (req 2 not met); C-45 new; C-46 new

**R19 ceiling target:** single variation inheriting V-01 R18 architecture (all 38 prior aspirationals PASS including C-45 PASS via three-site enumeration) and adding anti-pattern anchor coverage of the C-45 failure mode as a named entry with C-45 criterion ID reference in the closing mechanism (C-46 PASS).

---

Here's what was extracted and changed:

## v16 -> v17 changes

**One new criterion -- C-45** extracted from **ES-R17-3** (structural pattern):

> **C-45: Multi-component pass condition -- numbered-requirement enumeration at definition site enabling PARTIAL-by-number citation** (enforcement)

**Derivation chain:** C-43 (three-component conjunction, requirements in prose) -> C-45

**What it closes:** R17 V-04 and V-05 probed C-43's three requirements along orthogonal axes and their PARTIAL verdicts cited "req 1 met / req 2 met / req 3 not met" -- but those numbers were supplied by the scorer from context, not inscribed in C-43's definition. When requirements are prose-only at the definition site, a PARTIAL verdict must describe the missing component by its *effect* rather than by a structural reference. C-45 closes this by requiring multi-component pass conditions (N >= 2 requirements) to enumerate each requirement with an explicit label at the definition site, making PARTIAL verdicts citable by number.

**ES-R17-1 / ES-R17-2 notes:** Both characterize existing C-43/C-44 PASS/PARTIAL/FAIL mechanics -- no new criteria extracted, parallel to ES-R15-1, ES-R15-2, and ES-R16-1.

**Formula:** denominator 37 -> 38. `(aspirational_pass/38 x 220)`, max 310 unchanged.

**R18 ceiling target:** single variation inheriting V-01 R17 architecture (all 37 prior aspirationals PASS) and adding numbered-requirement enumeration in multi-component pass conditions (C-45 PASS).

*ES-R17-1 note:* C-43's three-component wiring (manifest production + VERIFIER key lookup + SYNTHESIS prohibition) as a conjunction where all three must be simultaneously present is the ceiling-enabling mechanism for C-43. V-04 and V-05 confirm that any single missing component drops to PARTIAL; both score identically to V-03 (C-43 FAIL) at 304.1, confirming that PARTIAL is not a scoring advantage over FAIL in the aspirational tier -- its value is diagnostic, not point-bearing. No new criterion extracted; the three-tier PASS/PARTIAL/FAIL structure is already within C-43's existing pass condition. Pattern parallel to ES-R15-1, ES-R15-2, and ES-R16-1.

*ES-R17-2 note:* C-44's symmetric conjunction gate achieves PASS via two symmetric exclusion clauses; V-02's single missing clause is the minimal delta from the ceiling -- one sentence drops C-44 from PASS to PARTIAL and costs 5.9 composite points. No new criterion extracted; the PARTIAL condition is already within C-44's pass condition.

---

**v15 -> v16 changes:**

**Two new criteria extracted** from ES-R16-2 and ES-R16-3:

**C-43: SPECIFICITY AUDIT MANIFEST -- Q1/Q2 keyed-table consolidation closing the full-SA-re-read path** (enforcement)

Derivation chain: C-16 -> C-43. C-16 closed the fresh-baseline-lookup path by sweeping CHANGE annotations into a keyed manifest before SYNTHESIS. C-43 applies the same pattern one layer up: the SPECIFICITY AUDITOR's Q1/Q2 results are dispersed across per-output blocks -- reachable only by re-reading the full SA body. C-43 requires the SA to produce a SPECIFICITY AUDIT MANIFEST table keyed by (Output, Criterion), the VERIFIER to reference results by manifest key, and SYNTHESIS to be explicitly prohibited from re-reading SA blocks. C-42 PASS leaves the dispersed-reread path open; C-43 closes it.

**C-44: VERIFIER entry condition -- symmetric conjunction gate excluding both single-token bypass paths** (enforcement)

Derivation chain: C-21 -> C-42 -> C-44. C-42 requires `[ANALYST COMPLETE] alone does not satisfy this gate` -- closing the forward bypass. The reverse bypass path (`[SPECIFICITY AUDIT COMPLETE]` appearing without `[ANALYST COMPLETE]` having been issued) is not excluded by C-42. C-44 adds the symmetric exclusion clause, making neither token independently sufficient and making the conjunction requirement bidirectionally auditable from the VERIFIER header.

**ES-R16-1 note:** Characterizes C-42's PASS/PARTIAL/FAIL separating mechanics -- no new criterion extracted, parallel to ES-R15-1 and ES-R15-2.

**Formula:** denominator 35 -> 37. `(aspirational_pass/37 x 220)`, max 310 unchanged.

**R17 ceiling target:** single variation combining V-04 architecture (C-43 PASS via SPECIFICITY AUDIT MANIFEST) + V-05 architecture (C-44 PASS via symmetric conjunction gate), with all 35 prior aspirationals inherited.

---

## v14 -> v15 summary

One new criterion extracted from ES-R15-3 (V-05 R15):

**C-42: SPECIFICITY AUDITOR role -- named-gate citation in VERIFIER entry condition making Q1/Q2 separation independently auditable from header** (enforcement)
- Failure mode closed: C-37 leaves open a path where a rubric has a named anchor block + separate Q1/Q2 columns (C-35+C-37 PASS) while the VERIFIER entry condition only lists `[ANALYST COMPLETE]` as its gate -- meaning Q1/Q2 separation is invisible from the VERIFIER header; C-42 closes this by requiring the SPECIFICITY AUDITOR to be a named role with its own gate token, cited verbatim in the VERIFIER entry condition with an explicit exclusion clause (`[ANALYST COMPLETE] alone does not satisfy this gate`)
- Derivation: C-17 -> C-29 -> C-35 -> C-37 -> C-42 (SPECIFICITY AUDITOR named as separate role with own gate token; gate cited verbatim in VERIFIER entry condition; `[ANALYST COMPLETE] alone does not satisfy this gate` makes the dedicated audit verifiable from the VERIFIER header alone); C-37 PASS does not require the Q1/Q2 audit to have its own named role or gate token in the VERIFIER entry condition; C-42 closes the header-unverifiable path that C-37 PASS leaves open

**Formula update:** `(aspirational_pass/35 x 220)` -- denominator 34 -> 35, max 310 unchanged.

**R15 open aspirationals per variation:**
- V-01 R15: (none -- ceiling achieved, all 34 prior aspirationals PASS)
- V-04 R15: C-23 PARTIAL
- V-05 R15: C-23 PARTIAL

**R16 ceiling target:** single variation inheriting V-01 R15 architecture (all 34 prior aspirationals PASS, C-23 full PASS) and adding SPECIFICITY AUDITOR named role with gate cited verbatim in VERIFIER entry condition (C-42 PASS).

*ES-R15-1 note:* The dual-column VERIFIER with named ANCHOR REVIEW BLOCK + per-cell `per Q1 above` / `per Q2 above` references is the complete structural close of C-35 -- the combination of C-35 + C-37 working together. No new criterion extracted.

*ES-R15-2 note:* V-01 C-23 full PASS via specific field-label naming (`*Note*`, `*Comment*`, `*Observation*`) vs V-04/V-05 C-23 PARTIAL with generic exclusion rule. No new criterion extracted; the full-PASS path is already within C-23's pass condition.

---

## v13 -> v14 summary

Three new aspirational criteria extracted from R14 V-01 WHY annotations:

**C-39: Formula -- scoring-site inscription of all formula parameters** (enforcement)
- Source: V-01 R14 C-03 PASS WHY -- formula stated inline at the calculation site with all parameters: `(aspirational_pass / 34 x 220)`; denominator matches the current rubric version
- Failure mode closed: C-03 PASS requires formula-correct arithmetic; the formula can be applied correctly from memory without stating it at the scoring site; when the denominator is not inscribed at the calculation site, a rubric version mismatch passes C-03 if the arithmetic is self-consistent but is structurally undetectable; inscribing the formula with all parameters makes denominator-rubric disagreement detectable at a glance
- Derivation: C-03 (formula-correct composite) -> C-39 (formula stated inline with all parameters at the calculation site); C-03 PASS does not require formula inscription; C-39 closes the silent-arithmetic path; a SCORER that applies the correct formula from memory without stating it at the scoring site satisfies C-03 but not C-39

**C-40: Evidence field -- dual-violation anchor naming both disqualifying patterns at definition site** (enforcement)
- Source: V-01 R14 C-02 PASS WHY -- evidence field definition names two distinct failure types: "fails if it could describe any well-designed output of this type, OR if the same description fits another output in this run"
- Failure mode closed: C-02 PASS requires evidence referencing structural features of the specific output; a single disqualifying pattern leaves the boundary subjectively enforceable; naming a second pattern ("fits another output in this run") adds a within-run distinctness check that is structurally verifiable during VERIFIER review; without both patterns named at the field definition site, cross-output evidence duplication escapes detection as a named schema violation
- Derivation: C-02 (evidence per verdict) -> C-40 (evidence field names both disqualifying violation patterns at field definition site: cross-type genericity AND cross-output duplication within the run); C-02 PASS does not require dual violation anchoring; C-40 closes the cross-output duplication path that C-02 PASS leaves open; evidence that is output-type-specific but duplicated across outputs satisfies C-02 but not C-40

**C-41: Leaderboard -- deterministic tie-break protocol inscribed at definition site** (enforcement)
- Source: V-01 R14 C-04 PASS WHY -- "Tie-breaking protocol at the leaderboard definition site makes ranking deterministic; the pre-close checklist item #1 enforces it before synthesis gate closure"
- Failure mode closed: C-04 PASS requires ranked ordering with ties broken or noted; the protocol for breaking ties can be left implicit or decided ad hoc at synthesis time; when the tie-break rule is not inscribed at the leaderboard definition site, identical scores across synthesis passes may be broken differently; the inscribed protocol makes tie-break resolution a structural check; "ties are noted" satisfies C-04 but is not deterministic
- Derivation: C-04 (ranked leaderboard, ties broken or noted) -> C-41 (tie-break protocol explicitly defined at leaderboard definition site with named secondary and tertiary ranking dimensions); C-04 PASS does not require the protocol to be inscribed at the definition site; C-41 closes the ad-hoc-tie-break path; a leaderboard that breaks ties correctly but without an inscribed protocol satisfies C-04 but not C-41

**Formula update:** `(aspirational_pass/34 x 220)` -- denominator 31 -> 34, max 310 unchanged.

**R14 open aspirationals per variation:**
- V-01: C-35 FAIL (C-39 PASS, C-40 PASS, C-41 PASS in R14 V-01)

**R15 ceiling target:** single variation inheriting V-01 R14 architecture (all current PASSes including C-34, C-36, C-37, C-38, C-39, C-40, C-41) and adding VERIFIER dual-column separation (C-35 PASS).

---

## v12 -> v13 summary

Three new aspirational criteria extracted from R13 V-01 excellence signals:

**C-36: Anti-pattern anchor -- criterion-indexed closing mechanism** (enforcement)
- Source: V-01 R13 C-09/C-33 PASS evidence -- each closing mechanism description in the anti-pattern anchor explicitly names the criterion ID that enforces it: "Closing mechanism: C-33 requires each failure mode to be paired with its own dedicated, separately-named mechanism"; "C-34 requires a terminal assertion after all entries"; "C-35 requires structurally separated labeled columns"
- Failure mode closed: C-33 requires a dedicated named mechanism per failure mode; a mechanism description can correctly characterize the enforcement rule behaviorally without identifying which criterion enforces it; without a criterion ID reference the reader cannot verify coverage of the criterion system or trace backward from a criterion violation to its anti-pattern entry; the criterion-index closes the backward-traceability gap that C-33 PASS leaves open
- Derivation: C-09 -> C-33 -> C-36 (mechanism description carries a criterion ID reference enabling bidirectional traceability); C-33 PASS does not require criterion IDs in mechanism descriptions; C-36 closes the traceability gap; a mechanism named "per-mode dedicated naming" satisfies C-33 but not C-36

**C-37: VERIFIER anchor block -- dual-question verbatim pre-statement** (enforcement)
- Source: V-01 R13 C-29 PASS change evidence -- "both type-level and intra-run questions explicitly stated in V-01 R13 anchor review block"; the phrase "anchor review block" names a structural element that pre-states both questions verbatim before any per-cell review begins
- Failure mode closed: C-29 requires both questions to be explicitly stated; C-35 requires structurally separated labeled columns; both can be satisfied by embedding questions inside per-cell row entries; without a central verbatim anchor, per-cell restatements can silently deviate from the intended question wording across rows; the anchor block closes the question-drift path
- Derivation: C-17 -> C-29 -> C-35 -> C-37 (questions verbatim-anchored in a named pre-pass block before per-cell review begins); C-29 PASS and C-35 PASS do not require a central verbatim anchor block; C-37 closes the per-cell drift path; a VERIFIER that re-quotes both questions inline in each cell satisfies C-29 but not C-37

**C-38: Baseline load table -- per-variation open-item decomposition** (enforcement)
- Source: V-01 R13 Baseline Load section -- baseline presented as a table with one row per variation, each row naming the variation identifier and listing its specific open aspirationals from the prior round; the per-variation row structure makes change tracking a mechanical keyed lookup
- Failure mode closed: C-14 requires a baseline table with a gate token; the table can be a flat list of all open criteria across all variations, requiring textual search to isolate per-variation state; the flat structure makes it possible to miss a variation's open item; per-variation decomposition closes the cross-variation lookup gap
- Derivation: C-14 (baseline load gate + table present) -> C-38 (table is decomposed per-variation with variation identifiers as row keys); C-14 PASS with a flat baseline does not satisfy C-38; the per-variation structure enables inline CHANGE annotations to be verified by variation-keyed row lookup rather than a full-table scan

**Formula update:** `(aspirational_pass/31 x 220)` -- denominator 28 -> 31, max 310 unchanged.

**R13 open aspirationals per variation:**
- V-01: C-34 FAIL, C-35 FAIL (C-36 PASS, C-37 PASS, C-38 PASS in R13 V-01)

**R14 ceiling target:** single variation inheriting V-01 R13 architecture (all current PASSes including C-33, C-36, C-37, C-38) and adding PROHIBITED terminal assertion (C-34 PASS) + VERIFIER dual-column separation (C-35 PASS).

---

## v11 -> v12 summary

Three new aspirational criteria extracted from R12 excellence signals:

**C-33: Anti-pattern anchor -- exhaustive 1:1 failure-mode/mechanism pairing** (enforcement)
- Source: V-01 R12 C-09 evidence: "5 named failure modes (A-E) appears before ROLE 1; each mode shows a typical output and a named closing mechanism (Mechanism 1-5)"
- Failure mode closed: C-09 PASS requires at least one failure mode paired with at least one mechanism; a 5-mode anchor can name 5 failure modes with a single shared mechanism and still satisfy C-09; the 1:1 pairing requirement closes the multi-mode / single-mechanism path
- Derivation: C-09 sets the positive floor; C-33 requires each failure mode to be paired with its own dedicated closing mechanism with parallel indexing; C-09 PASS does not enforce per-mode pairing -- C-33 does

**C-34: PROHIBITED CONTENT CATEGORIES -- negative completeness assertion** (enforcement)
- Source: V-02 R12 C-28 evidence: "closing statement 'No prohibited content category lacks a named destination'" after all per-entry routing annotations
- Failure mode closed: C-28 PASS requires per-entry routing annotations; a list of N entries can have all N annotated while a later addition silently lacks a destination; the closing assertion converts the list from an open enumeration to a self-verifying set
- Derivation: C-28 -> C-34 (terminal assertion that no entry is unrouted); C-28 PASS does not require a closing assertion; C-34 closes the implicit-completeness path

**C-35: VERIFIER specificity dimensions -- structurally separated labeled fields** (enforcement)
- Source: V-03 R12 C-29 evidence: "VERIFIER TABLE with labeled columns: Output, Criterion, Scorer evidence, Type-level, Intra-run, Specificity, Revised evidence" -- separate columns for the type-level and intra-run questions
- Failure mode closed: C-29 PASS requires both questions to be explicitly stated; both can appear in a single combined Specificity prose field; when combined, the two questions merge in execution; structural separation into distinct labeled slots makes each question independently auditable
- Derivation: C-17 -> C-29 -> C-35 (both questions in structurally distinct labeled slots); C-35 closes the question-merging path that C-29 PASS leaves open

**Formula update:** `(aspirational_pass/28 x 220)` -- denominator 25 -> 28, max 310 unchanged.

**R12 open aspirationals per variation:**
- V-01: C-33 PASS, C-34 FAIL, C-35 FAIL (also C-28 PARTIAL, C-29 FAIL)
- V-02: C-33 FAIL, C-34 PASS, C-35 FAIL (also C-09 FAIL, C-29 FAIL)
- V-03: C-33 FAIL, C-34 FAIL, C-35 PASS (also C-09 FAIL, C-28 PARTIAL)

**R13 ceiling target:** single variation combining V-01 anchor architecture (C-09 PASS, C-33 PASS) + V-02 PROHIBITED completeness assertion (C-28 PASS, C-34 PASS) + V-03 VERIFIER TABLE dual-column schema (C-29 PASS, C-35 PASS).

---

## Scoring formula

```
composite = essential_score + recommended_score + aspirational_score

essential_score    = (essential_pass / 5) x 50         [max 50; each PARTIAL = 0.5]
recommended_score  = (recommended_pass / 2) x 40       [max 40; each PARTIAL = 0.5]
aspirational_score = (aspirational_pass / 39) x 220    [max 220; PARTIAL not counted]

max composite = 310
golden threshold: all 5 essentials PASS AND composite >= 80
```

---

## Criteria

### ESSENTIAL -- output fails without these

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Complete verdict matrix** -- every criterion is scored for every output; no criterion-output cell is blank or omitted | completeness | A verdict (PASS / PARTIAL / FAIL) exists for every criterion x output pair; a cell cannot be empty or skipped |
| C-02 | **Evidence per verdict** -- every verdict cell includes specific evidence naming what the scored output did or did not do to earn the verdict | completeness | Each criterion-output cell contains evidence that references a structural feature of the specific output being scored; a criterion restatement or blank does not satisfy this |
| C-03 | **Formula-correct composite score** -- each output receives a composite score computed from the stated formula; the formula, weights, and counts are applied correctly | format | The formula matches the rubric weight table; the arithmetic is correct; each output's composite score is derivable from its PASS/PARTIAL/FAIL counts |
| C-04 | **Ranked leaderboard** -- all outputs are ranked by composite score, highest to lowest | format | A ranking list or section exists; outputs appear in descending score order; ties are broken or noted |
| C-05 | **Failure patterns called out** -- criteria that fail across ALL scored outputs are identified as failure patterns, or absence of failure patterns is explicitly noted | coverage | A "failure patterns" section (or equivalent) exists; any criterion with zero PASS across all N outputs is surfaced; if no such criterion exists, that absence is stated |

---

### RECOMMENDED -- output is better with these

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Excellence signals** -- outputs scoring unusually high on a specific criterion are identified; any criterion where one output clearly leads the field is named with the structural mechanism | depth | An "excellence signals" section (or equivalent) exists; at least one output-criterion pair is highlighted as an outlier high performer with a structural mechanism explanation; if no outlier exists, that is stated explicitly |
| C-07 | **Regression signals** -- if prior-round score data is available, criterion-output pairs where the verdict degraded are flagged; absence of regressions or prior data is stated explicitly | depth | A regression section exists and identifies any criterion-output pair that degraded from PASS (or PARTIAL) since the prior round; the fallback states "no regressions detected" or "no prior round data" when applicable; a score report that silently omits regression analysis does not satisfy C-07 |

---

### ASPIRATIONAL -- raise the bar once essential/recommended are stable

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-08 | **Golden threshold per output** -- each output block concludes with an explicit golden-threshold determination declaring YES (all 5 essentials PASS and composite >= 80) or NO with the reason; the determination is a required field, not inferred from the score table | enforcement | Each output block in the SCORER output contains an explicit golden-threshold field with form `Golden: YES -- all 5 essentials PASS; composite >= 80` or `NO -- [reason]`; the field is marked required; omitting the golden determination for any output is a structural gap that cannot be compensated by a correct score table |
| C-09 | **Anti-pattern anchor** -- named failure modes with typical bad-output examples appear before scoring begins; each failure mode names the structural mechanism that closes it | enforcement | A pre-scoring block exists naming at least one failure mode, showing a typical failing output, and naming the mechanism that closes it; the block precedes the scoring instructions; PARTIAL if failure modes are present but fewer than the count of named mechanisms; C-09 PASS does not require exhaustive mechanism-to-failure-mode pairing -- that is C-33's criterion |
| C-10 | **Synthesis gate pair** -- the required synthesis sections are enclosed in a `[SYNTHESIS OPEN]` / `[SYNTHESIS COMPLETE]` gate pair; a single end-of-phase token without an opening gate does not satisfy this criterion | enforcement | `[SYNTHESIS OPEN]` appears before the first required synthesis section; `[SYNTHESIS COMPLETE]` appears after the last; all four required synthesis sections (LEADERBOARD, EXCELLENCE SIGNALS, FAILURE PATTERNS, REGRESSION SIGNALS) are inside the gate; omitting a section leaves the gate structurally incomplete; a single end-of-phase token without a gate pair is FAIL |
| C-11 | ***Why* field per criterion** -- each SCORER criterion block contains a `*Why*:` field requiring the scorer to name the structural mechanism or design property behind the verdict, not merely describe the evidence | depth | Every criterion block in SCORER output carries a `*Why*:` field after Evidence; the field must name the structural mechanism or design property driving the verdict; a restatement of the criterion or a paraphrase of the evidence does not satisfy the field requirement; PARTIAL if a subset of criterion blocks carries the field; absence of the field from the SCORER schema is FAIL |
| C-12 | **Structured verification block** -- the VERIFIER role uses a per-cell review block schema with explicitly labeled fields covering the output identifier, criterion identifier, copied scorer evidence, and a PASS/FAIL specificity result; free-text verification without labeled fields does not satisfy this criterion | enforcement | The VERIFIER role defines a per-cell review block schema with at minimum: output identifier, criterion ID, copied Scorer evidence field, and a Specificity PASS/FAIL field; when Specificity is FAIL, a revised evidence field is required; the schema applies to every criterion-output pair; PARTIAL if the VERIFIER applies the specificity test but uses free-text review without a labeled per-cell schema; C-17 (specificity test present) does not satisfy C-12 |
| C-13 | **Inline *Change* annotation** -- when a verdict differs from the prior-round baseline, a CHANGE note is written at the scoring site during the scoring pass, not deferred to synthesis; regression detection is a concurrent constraint, not a retrospective lookup | enforcement | Each criterion block in the scoring phase contains an inline `*Change*:` slot that fires at the scoring site when the verdict differs from baseline; the synthesis regression section draws from these inline annotations; no fresh baseline lookup occurs in synthesis; PARTIAL if inline annotations are present for some but not all criterion blocks |
| C-14 | **Baseline Load gate** -- prior-round verdict data is confirmed loaded via a gate token before any output is scored; the baseline table is a structural prerequisite to scoring, not assembled retrospectively | enforcement | A dedicated pre-scoring phase builds a baseline table of all prior-round verdicts; a gate token (e.g., `[PRIOR ROUND LOAD COMPLETE]`) must appear before the first scoring block; scoring may not begin while the gate is open; PARTIAL if no prior data exists and the output explicitly states this; absence of the gate when prior data is available is FAIL |
| C-15 | **Mandatory bidirectional *Change* field** -- the inline CHANGE annotation is always required, not conditional; every criterion block carries the field with exactly three permissible values: `NO CHANGE`, `CHANGE from [prior verdict]: [reason]`, or `NO PRIOR DATA`; silent omission is syntactically visible | enforcement | Every criterion block in the scoring phase contains a `*Change*:` field with exactly three permissible values; the field is present regardless of whether a change occurred; a conditional prompt ("write here if verdict changes") does not satisfy this criterion; the mandatory form closes the omission path that a conditional slot leaves open; C-13 (conditional slot present) does not satisfy C-15 |
| C-16 | **Change Manifest phase** -- all inline CHANGE annotations are swept into a dedicated structured table before SYNTHESIS begins; the SYNTHESIS regression section draws exclusively from this manifest; an explicit prohibition prevents SYNTHESIS from re-reading the baseline table or SCORER blocks | enforcement | A dedicated pre-SYNTHESIS phase collects every `*Change*: CHANGE` annotation into a structured manifest table; a gate token (e.g., `[CHANGE MANIFEST COMPLETE]`) marks the phase boundary; the SYNTHESIS regression section draws from the manifest exclusively; an explicit instruction prohibits re-reading the baseline table or SCORER blocks during SYNTHESIS; PARTIAL if the manifest phase exists but lacks the explicit re-reading prohibition; the manifest closes the fresh-lookup path that C-13 alone leaves open; C-13 (inline annotations written) does not satisfy C-16 |
| C-17 | **Evidence specificity test** -- a dedicated VERIFIER role applies a specificity test to every evidence cell after the scoring pass; any cell whose evidence could describe any well-designed output of this type triggers a required revision before synthesis begins | enforcement | A VERIFIER role or verification phase explicitly states and applies the specificity test; evidence cells that fail require a revised entry; the VERIFIER is a structural prerequisite to synthesis -- ANALYST cannot begin until the VERIFIER gate token appears; a general instruction to "be specific" in the scoring phase does not satisfy C-17 |
| C-18 | **VERIFIER role with gate** -- a named VERIFIER role is defined with its own gate token (`[VERIFIER COMPLETE]`) separating it from both SCORER and ANALYST; the ANALYST role explicitly cannot begin until the gate token appears | enforcement | A named VERIFIER role exists as a distinct role with a `[VERIFIER COMPLETE]` gate token; the ANALYST role contains an explicit instruction that it cannot begin until `[VERIFIER COMPLETE]` appears; PARTIAL if a verification step is present but not as a named role with a dedicated gate; C-20 (inter-role gate architecture) does not satisfy C-18 |
| C-19 | **Three-field labeled narrative** -- the per-output narrative section contains exactly three required labeled fields: (1) Primary differentiator -- the structural feature explaining why this output scored differently; (2) Primary miss -- the criterion or structural mechanism most clearly absent; (3) Verdict spread -- where the output concentrated its points and why | depth | Each per-output narrative section contains all three prescribed labeled fields; each field carries a "(required)" or equivalent annotation at the label site; a narrative that addresses one or two fields is PARTIAL; addressing all three fields without "(required)" annotation at each label site satisfies C-19 but not C-22; C-07 (per-output notes present) does not satisfy C-19 |
| C-20 | **Named role sequence + inter-role gates** -- a named role sequence (SCORER -> VERIFIER -> ANALYST) is defined; each adjacent role pair is separated by a gate token in prescribed order; role-skipping is structurally detectable | enforcement | The prompt defines a named role sequence with at least SCORER, VERIFIER, and ANALYST; each adjacent pair has a gate token (e.g., `[SCORER COMPLETE]` before VERIFIER, `[VERIFIER COMPLETE]` before ANALYST); PARTIAL if some but not all inter-role gate pairs are defined; C-10 (synthesis gate) does not satisfy C-20 |
| C-21 | **Bidirectional gate inscription** -- each downstream role definition contains an explicit entry condition naming the upstream gate token that must appear above before it begins; gate dependencies are bidirectionally explicit | enforcement | Each downstream role (VERIFIER, ANALYST) contains an explicit "Do not begin until [gate token] appears above" instruction naming the specific upstream gate token; the instruction appears within the downstream role definition; PARTIAL if some but not all downstream roles carry the prerequisite inscription; C-20 (inter-role gates defined upstream) does not satisfy C-21 |
| C-22 | **Required-field annotation** -- each mandatory field within every phase's output schema carries an explicit "(required)" annotation (or equivalent) adjacent to the field label; the annotation makes field omission syntactically visible without a separate completeness audit | depth | Every mandatory field in every phase output schema (SCORER, VERIFIER, ANALYST) is annotated inline as required at the field label; PARTIAL if some but not all mandatory fields carry the annotation, or if annotation is present in some roles but absent in others; C-19 (three fields prescribed) does not satisfy C-22 |
| C-23 | **Field-name exclusion rule** -- the SCORER verdict block schema names a complete permitted field set and includes an explicit prohibition naming at least one specific prohibited field label (e.g., `*Note*`, `*Comment*`, `*Observation*`) as a named schema violation; a schema that lists permitted fields without prohibiting named others leaves the schema open to unlisted additions | enforcement | The SCORER output schema names the complete permitted field list and includes an explicit prohibition naming at least one prohibited field label (e.g., `*Why*`, `*Note*`, `*Comment*`, `*Observation*`) as a named schema violation; the prohibition is stated inside the SCORER role definition; PARTIAL if content-type categories are excluded without naming specific prohibited field labels; C-12 (phase-separated narrative) does not satisfy C-23 |
| C-24 | **Pre-close checklist** -- the synthesis gate pair encloses a pre-close checklist enumerating each required synthesis section; the closing gate token cannot be written until each section is confirmed present | enforcement | A `[SYNTHESIS OPEN]` / `[SYNTHESIS COMPLETE]` gate pair encloses a pre-close checklist naming each required synthesis section (LEADERBOARD, EXCELLENCE SIGNALS, FAILURE PATTERNS, REGRESSION SIGNALS); each section must be confirmed before `[SYNTHESIS COMPLETE]` is written; PARTIAL if a checklist exists but omits one or more required sections; a single end-of-phase gate token without a pre-close checklist does not satisfy C-24; C-10 (synthesis gate pair present) does not satisfy C-24 |
| C-25 | **Content-type schema prohibition** -- the SCORER schema prohibition names forbidden content categories (e.g., "evaluative prose", "narrative text", "mechanism analysis") in addition to or instead of specific forbidden field labels; type-category prohibition is enforceable regardless of how the field is labeled -- including novel field names a model might invent | enforcement | The SCORER schema includes at least one explicitly named content category or prose type that is prohibited; the content-type prohibition is introduced by its own labeled group header (`PROHIBITED CONTENT CATEGORIES:`) or equivalent paragraph-level structure making the category independently identifiable without reading all items; PARTIAL if content-type categories are present but co-listed with field labels in a single undifferentiated enumeration without a categorical group label; a prohibition listing only named field labels without any content-type characterization does not satisfy C-25; C-23 (field-name exclusion rule present) does not satisfy C-25 |
| C-26 | **Checkbox-format pre-close confirmation** -- each item in the synthesis pre-close checklist is expressed as a `[ ]` checkbox marker making individual section confirmation syntactically distinct; a numbered list, prose enumeration, or bullet list without per-item `[ ]` markers does not satisfy this criterion | enforcement | The synthesis pre-close checklist contains a `[ ]` checkbox marker for each required synthesis section; each checkbox appears on its own line adjacent to the section label; the instruction requires filling each checkbox before writing `[SYNTHESIS COMPLETE]`; PARTIAL if checkbox format is used but one or more required sections lack a corresponding `[ ]` marker; a numbered list without `[ ]` markers does not satisfy C-26; C-24 (pre-close checklist exists) does not satisfy C-26 |
| C-27 | *(pre-existing -- definition not in this input)* | -- | -- |
| C-28 | *(pre-existing -- definition not in this input)* | -- | -- |
| C-29 | *(pre-existing -- definition not in this input)* | -- | -- |
| C-30 | *(pre-existing -- definition not in this input)* | -- | -- |
| C-31 | *(pre-existing -- definition not in this input)* | -- | -- |
| C-32 | *(pre-existing -- definition not in this input)* | -- | -- |
| C-33 | **Anti-pattern anchor -- exhaustive 1:1 failure-mode/mechanism pairing** -- each failure mode in the anti-pattern anchor is paired with its own dedicated, separately-named closing mechanism; parallel indexing makes the per-mode pairing map explicit and complete; a single shared mechanism that closes multiple named failure modes does not satisfy this criterion | enforcement | Every failure mode named in the anti-pattern anchor block has a dedicated closing mechanism that is not shared with any other failure mode; the pairing is made explicit through parallel indexing (e.g., Failure Mode A -> Mechanism 1, B -> 2...); PARTIAL if some but not all failure modes have dedicated mechanisms; a rubric that names 5 failure modes and 1 shared closing mechanism satisfies C-09 PASS but not C-33; C-09 PARTIAL condition does not imply C-33 PARTIAL |
| C-34 | **PROHIBITED CONTENT CATEGORIES -- negative completeness assertion** -- after all per-entry routing annotations are written, a terminal assertion closes the PROHIBITED list as a self-verifying set; the assertion states that no prohibited content category lacks a named destination; absence of the assertion leaves the completeness guarantee implicit | enforcement | A closing assertion appears after all per-entry routing annotations in the PROHIBITED CONTENT CATEGORIES list; the assertion must take a form equivalent to "No prohibited content category lacks a named destination"; the assertion converts the list from an open enumeration to a bounded set; PARTIAL if a completeness comment is present but does not constitute a structural assertion; C-28 PASS (per-entry routing annotations complete) does not satisfy C-34 |
| C-35 | **VERIFIER specificity dimensions -- structurally separated labeled fields** -- the VERIFIER per-cell schema separates the type-level specificity question (Q1) and the intra-run specificity question (Q2) into distinct labeled columns or fields; a single combined "Specificity" field that addresses both questions in one cell satisfies C-29 but not C-35 | enforcement | The VERIFIER per-cell schema contains separate labeled fields or columns for Q1 (type-level) and Q2 (intra-run); each field is independently auditable; PARTIAL if both questions appear in the VERIFIER but in a single combined field without structural separation; a VERIFIER TABLE with a unified "Specificity" column containing both questions in one cell satisfies C-29 but not C-35; C-29 PASS (both questions explicitly stated) does not satisfy C-35 |
| C-36 | **Anti-pattern anchor -- criterion-indexed closing mechanism** -- each closing mechanism description in the anti-pattern anchor names the rubric criterion ID (e.g., "C-33 requires...") that enforces the close; this converts the mechanism from a behavioral description into a traceable criterion pointer enabling bidirectional lookup: failure mode -> mechanism -> criterion ID | enforcement | Every closing mechanism in the anti-pattern anchor block includes an explicit criterion ID reference (e.g., "C-NN requires...") naming which criterion enforces it; PARTIAL if some but not all mechanism descriptions carry a criterion ID reference; a mechanism that correctly characterizes the enforcement rule behaviorally without naming a criterion ID satisfies C-09 and C-33 but not C-36; the criterion ID must appear as an active reference, not merely be adjacent to the mechanism text |
| C-37 | **VERIFIER anchor block -- dual-question verbatim pre-statement** -- a named anchor block precedes the VERIFIER per-cell review and contains both the type-level specificity question and the intra-run specificity question as individually labeled verbatim entries; the per-cell schema references these anchored questions by label; per-cell restatements that diverge from the anchor text are a structural violation | enforcement | A named anchor block (e.g., "anchor review block", "question anchor", or equivalent label) appears before the first VERIFIER per-cell review entry; the block contains both questions as labeled verbatim entries -- not paraphrases; the per-cell schema carries an explicit reference to the anchored questions (e.g., "per Q1 above"); PARTIAL if both questions are explicitly stated before per-cell review but in an unnamed block or without individually labeled verbatim entries; C-29 PASS (both questions stated) does not satisfy C-37; C-35 PASS (structurally separated columns) does not satisfy C-37 |
| C-38 | **Baseline load table -- per-variation open-item decomposition** -- the PRIOR ROUND LOAD phase presents the baseline as a structured table with at least one row per scored variation; each row names the variation as the row key and lists its specific open aspirationals from the prior round; a flat undifferentiated list of all open criteria across all variations satisfies C-14 but not C-38 | enforcement | The baseline load table contains one row per scored variation; each row has the variation identifier as the row key and explicitly lists that variation's open aspirationals from the prior round; PARTIAL if some but not all variations have dedicated rows; new variations with no prior data may appear with a "new in this round" annotation; a flat baseline list without per-variation row structure satisfies C-14 but not C-38; C-14 PASS (gate token present, baseline loaded) does not satisfy C-38 |
| C-39 | **Formula -- scoring-site inscription of all formula parameters** -- the composite score formula is stated inline at the scoring site with all parameters (denominator, weights, counts) making the arithmetic a structural check against the rubric specification; a SCORER that applies the correct formula from memory without stating it at the scoring site satisfies C-03 but not C-39 | enforcement | The composite calculation block contains the formula with all parameters inscribed inline (e.g., `(aspirational_pass / 39 x 220)`); the denominator must match the current rubric version; PARTIAL if the formula is stated but with parameters omitted or described in prose rather than inscribed symbolically; a SCORER that writes only the computed result without the formula expression does not satisfy C-39; C-03 PASS (formula-correct composite) does not satisfy C-39 |
| C-40 | **Evidence field -- dual-violation anchor naming both disqualifying patterns at definition site** -- the evidence field definition at the schema definition site names two distinct disqualifying violation patterns: (1) the evidence could describe any well-designed output of this type (cross-type genericity) and (2) the same description fits another output in this run (cross-output duplication); naming only one pattern leaves the second enforcement boundary implicit | enforcement | The evidence field definition in the SCORER schema explicitly names both violation patterns; each pattern is stated as a named condition that triggers a cell violation; PARTIAL if one violation pattern is named but not the other; a field definition that requires "specific evidence" without naming both disqualifying patterns satisfies C-02 PASS but not C-40; C-22 PASS (required-field annotation present) does not satisfy C-40 |
| C-41 | **Leaderboard -- deterministic tie-break protocol inscribed at definition site** -- the leaderboard definition site contains an explicit tie-break protocol naming the secondary and tertiary ranking dimensions to apply when composite scores are equal; the protocol makes ranking deterministic and unconditionally verifiable; noting ties without a resolution protocol satisfies C-04 but not C-41 | enforcement | The leaderboard definition block contains an explicit tie-break protocol naming at least one secondary ranking dimension (e.g., essential PASS count) and one tertiary dimension (e.g., recommended PASS count); the protocol is inscribed at the leaderboard definition site, not deferred to synthesis; PARTIAL if a tie-break rule is present but covers only one dimension or is described in synthesis prose rather than the definition site; C-04 PASS (ranked leaderboard, ties broken or noted) does not satisfy C-41 |
| C-42 | **SPECIFICITY AUDITOR role -- named-gate citation in VERIFIER entry condition making Q1/Q2 separation independently auditable from header** -- the SPECIFICITY pre-pass is elevated to a named SPECIFICITY AUDITOR role with its own gate token (e.g., `[SPECIFICITY AUDIT COMPLETE]`); the VERIFIER entry condition quotes this gate verbatim and explicitly states that `[ANALYST COMPLETE]` alone does not satisfy it; a reader can confirm the dedicated Q1/Q2 audit completed from the VERIFIER header alone, without reading the SPECIFICITY AUDITOR body | enforcement | A named SPECIFICITY AUDITOR role exists with a dedicated gate token (e.g., `[SPECIFICITY AUDIT COMPLETE]`); the VERIFIER entry condition quotes this gate verbatim as a required prerequisite; the entry condition includes an explicit exclusion clause stating that `[ANALYST COMPLETE]` alone (or any upstream gate other than the SPECIFICITY AUDITOR gate) does not satisfy the entry requirement; PARTIAL if the SPECIFICITY AUDITOR role exists with a gate token but the VERIFIER entry condition does not cite the gate verbatim or omits the exclusion clause; C-35 PASS (structurally separated Q1/Q2 columns) does not satisfy C-42; C-37 PASS (verbatim anchor block pre-stating both questions) does not satisfy C-42; the named-gate citation closes the header-silent path that C-37 PASS leaves open |
| C-43 | **SPECIFICITY AUDIT MANIFEST -- Q1/Q2 keyed-table consolidation closing the full-SA-re-read path** -- the SPECIFICITY AUDITOR produces a SPECIFICITY AUDIT MANIFEST table keyed by (Output, Criterion) as its terminal artifact; the VERIFIER references Q1/Q2 results by manifest key rather than by re-reading the SPECIFICITY AUDITOR blocks; SYNTHESIS is prohibited from re-reading SPECIFICITY AUDITOR blocks; this makes Q1/Q2 results independently retrievable by key lookup without traversing the full SA role body -- structurally parallel to C-16's CHANGE MANIFEST closing the fresh-baseline-lookup path | enforcement | Req 1: A SPECIFICITY AUDIT MANIFEST table exists as a named terminal artifact of the SPECIFICITY AUDITOR role, keyed by (Output, Criterion) with columns for Q1-TypeLevel result, Q2-IntraRun result, and Final action; Req 2: the VERIFIER per-cell schema references manifest rows by key (e.g., `per manifest row [output/C-NN]`) rather than directly re-reading SA body blocks; Req 3: SYNTHESIS includes an explicit prohibition against re-reading SPECIFICITY AUDITOR blocks (parallel to the baseline re-read prohibition in C-16); PARTIAL if req 1 met and req 2 met but req 3 absent, or if req 1 met but req 2 absent; C-42 PASS (named SPECIFICITY AUDITOR role with gate, verbatim cite in VERIFIER entry condition) does not require a manifest artifact; C-43 closes the dispersed-SA-body-reread path that C-42 PASS leaves open; a SPECIFICITY AUDITOR that produces correct per-output Q1/Q2 entries without a consolidated manifest satisfies C-42 but not C-43 |
| C-44 | **VERIFIER entry condition -- symmetric conjunction gate excluding both single-token bypass paths** -- the VERIFIER entry condition explicitly excludes BOTH `[ANALYST COMPLETE] alone` and `[SPECIFICITY AUDIT COMPLETE] alone` as individually sufficient; the exclusion is bidirectional, making the conjunction requirement auditable for both single-token bypass paths from the VERIFIER header; C-42 closes only the forward bypass path ([ANALYST COMPLETE] alone); C-44 closes the reverse bypass path ([SPECIFICITY AUDIT COMPLETE] alone) that C-42 PASS leaves open | enforcement | Req 1: The VERIFIER entry condition contains the exclusion clause `[ANALYST COMPLETE] alone does not satisfy this gate`; Req 2: the VERIFIER entry condition contains the exclusion clause `[SPECIFICITY AUDIT COMPLETE] alone does not satisfy this gate`; both clauses appear in the VERIFIER entry condition header; PARTIAL if req 1 met but req 2 absent; a VERIFIER entry condition that cites both gate tokens and excludes [ANALYST COMPLETE] alone (satisfying C-42) but does not also exclude [SPECIFICITY AUDIT COMPLETE] alone satisfies C-42 but not C-44; C-42 PASS (excluding [ANALYST COMPLETE] alone) does not satisfy C-44; the symmetric clause closes the reverse-token bypass path: a design where [SPECIFICITY AUDIT COMPLETE] might be produced without [ANALYST COMPLETE] having appeared is explicitly excluded at the header |
| C-45 | **Multi-component pass condition -- numbered-requirement enumeration at definition site enabling PARTIAL-by-number citation** -- when a pass condition requires N >= 2 independent structural components, each component is enumerated with an explicit label or number at the definition site (e.g., "Req 1:", "Req 2:", "Req 3:"); the PARTIAL condition cites the specific missing requirement by its label; a reader auditing a PARTIAL verdict can identify the exact missing component by number without re-reading the implementation body -- this closes the description-only-PARTIAL path that C-43 PASS leaves open | enforcement | Every pass condition with N >= 2 independent structural requirements enumerates each requirement as a distinctly numbered or labeled item at the definition site (e.g., Req 1 / Req 2 / Req 3); the PARTIAL condition text cites the missing requirement by its label (e.g., "PARTIAL if req 2 absent" rather than "PARTIAL if VERIFIER does not reference manifest by key"); PARTIAL verdicts in scored outputs reference the specific missing requirement number; PARTIAL if some but not all multi-component pass conditions in the rubric carry numbered enumeration; a pass condition that describes all requirements correctly in prose without labeling them satisfies C-43 PASS but not C-45; a PARTIAL verdict that describes the missing component's effect without citing a requirement number satisfies C-43 PARTIAL but not C-45; inline sequence markers embedded in continuous prose (e.g., "(1) first req (2) second req") do not satisfy C-45 -- the label must be structurally separable from the requirement text as a dedicated line or field |
| C-46 | **Anti-pattern anchor -- C-45 failure mode as a named entry covering the inline-marker vs dedicated-label distinction** -- the anti-pattern anchor includes a named entry for the C-45 failure mode: a multi-component pass condition written with inline sequence markers (e.g., "(1) ... (2) ...") embedded in prose rather than dedicated "Req N:" label lines; the entry names the typical bad output (inline markers in continuous prose) and the closing mechanism references C-45 as the enforcing criterion; C-45 PASS (all multi-component definition sites enumerated with dedicated labels) does not require the anti-pattern anchor to name this failure mode; C-46 closes the anti-pattern-uncovered path that C-45 PASS leaves open -- without a named entry, a reader encountering inline "(N)" markers in a draft rubric cannot use the anti-pattern anchor to identify the violation pattern by name and trace it to the closing criterion | enforcement | The anti-pattern anchor block contains a named entry for the C-45 failure mode: Req 1: the typical bad output example shows a multi-component pass condition written with inline "(N)" sequence markers or prose-only requirements (no dedicated "Req N:" label lines); Req 2: the closing mechanism names C-45 as the criterion that enforces dedicated "Req N:" label lines, following the C-36 criterion-indexed pattern; PARTIAL if req 1 met (failure mode entry present with typical bad output) but req 2 absent (closing mechanism does not carry a C-45 criterion ID reference); C-45 PASS (numbered enumeration at all multi-component definition sites) does not require a corresponding anti-pattern entry; C-36 PASS (criterion-indexed mechanism descriptions for existing entries) does not require coverage of C-45's failure mode as a new named entry; C-46 closes the anti-pattern-coverage gap that C-45 PASS leaves open |
