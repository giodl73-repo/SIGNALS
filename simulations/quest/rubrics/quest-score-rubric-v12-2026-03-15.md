The user is blocking the file writes — the task asks to **output the rubric as Markdown**, so here it is:

---

## v11 -> v12 summary

Three new aspirational criteria extracted from R12 excellence signals:

**C-33: Anti-pattern anchor -- exhaustive 1:1 failure-mode/mechanism pairing** (enforcement)
- Source: V-01 R12 C-09 evidence: "5 named failure modes (A–E) appears before ROLE 1; each mode shows a typical output and a named closing mechanism (Mechanism 1–5)"
- Failure mode closed: C-09 PASS requires at least one failure mode paired with at least one mechanism; a 5-mode anchor can name 5 failure modes with a single shared mechanism and still satisfy C-09; the 1:1 pairing requirement closes the multi-mode / single-mechanism path and makes the failure-mode→mechanism map explicitly complete and indexable
- Derivation: C-09 sets the positive floor (≥1 failure mode, ≥1 mechanism, all modes have a mechanism per the PARTIAL condition); C-33 requires each failure mode to be paired with its own dedicated closing mechanism, with parallel indexing making the mapping explicit; C-09 PARTIAL condition ("failure modes present but fewer than the count of named mechanisms") anticipates the 1:1 requirement but C-09 PASS does not enforce per-mode pairing -- C-33 does

**C-34: PROHIBITED CONTENT CATEGORIES -- negative completeness assertion** (enforcement)
- Source: V-02 R12 C-28 evidence: "closing statement 'No prohibited content category lacks a named destination'" after all per-entry routing annotations
- Failure mode closed: C-28 PASS requires per-entry routing annotations; a list of N entries can have all N annotated while a later addition silently lacks a destination; the closing assertion converts the list from an open enumeration to a self-verifying set; absence of the assertion leaves the completeness guarantee implicit
- Derivation: C-28 (per-entry routing annotation) closes the collective-routing path; C-34 requires a terminal assertion that no entry is unrouted, closing the implicit-completeness path; C-34 is orthogonal to C-28: a list can have per-entry annotations (C-28 PASS) without a closing assertion (C-34 FAIL), or a closing assertion over a partially-annotated list (C-28 PARTIAL, C-34 FAIL)

**C-35: VERIFIER specificity dimensions -- structurally separated labeled fields** (enforcement)
- Source: V-03 R12 C-29 evidence: "VERIFIER TABLE with labeled columns: Output, Criterion, Scorer evidence, Type-level, Intra-run, Specificity, Revised evidence" -- separate columns for the type-level and intra-run questions
- Failure mode closed: C-29 PASS requires both the type-level and intra-run questions to be explicitly stated; both can appear in a single combined Specificity prose field or review note; when combined, the two questions merge in execution and the model can answer one while appearing to address both; structural separation into distinct labeled slots makes each question an independently auditable output dimension
- Derivation: C-17 (specificity test present) → C-29 (both questions explicitly stated) → C-35 (both questions in structurally distinct labeled slots); C-35 closes the question-merging path that C-29 PASS leaves open; a VERIFIER TABLE that adds a "Dual-specificity" combined column with both questions in one cell satisfies C-29 but not C-35

**Formula update:** `(aspirational_pass/28 * 220)` -- denominator 25 -> 28, max 310 unchanged.

**R12 open aspirationals per variation:**
- V-01: C-33 PASS, C-34 FAIL, C-35 FAIL (also C-28 PARTIAL, C-29 FAIL)
- V-02: C-33 FAIL, C-34 PASS, C-35 FAIL (also C-09 FAIL, C-29 FAIL)
- V-03: C-33 FAIL, C-34 FAIL, C-35 PASS (also C-09 FAIL, C-28 PARTIAL)

**R13 ceiling target:** single variation combining V-01 anchor architecture (C-09 PASS, C-33 PASS) + V-02 PROHIBITED completeness assertion (C-28 PASS, C-34 PASS) + V-03 VERIFIER TABLE dual-column schema (C-29 PASS, C-35 PASS).

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
| C-23 | **Field-name exclusion rule** -- the SCORER verdict block schema names a complete permitted field set and includes an explicit prohibition on any field outside that set; a schema that lists permitted fields without prohibiting others leaves the schema open to unlisted additions | enforcement | The SCORER output schema names the complete permitted field list and includes an explicit prohibition naming at least one prohibited field label (e.g., `*Why*`, `*Note*`, `*Comment*`, `*Observation*`) as a named schema violation; the prohibition is stated inside the SCORER role definition; PARTIAL if permitted fields are named without an explicit field-exclusion rule; C-12 (phase-separated narrative) does not satisfy C-23 |
| C-24 | **Pre-close checklist** -- the synthesis gate pair encloses a pre-close checklist enumerating each required synthesis section; the closing gate token cannot be written until each section is confirmed present | enforcement | A `[SYNTHESIS OPEN]` / `[SYNTHESIS COMPLETE]` gate pair encloses a pre-close checklist naming each required synthesis section (LEADERBOARD, EXCELLENCE SIGNALS, FAILURE PATTERNS, REGRESSION SIGNALS); each section must be confirmed before `[SYNTHESIS COMPLETE]` is written; PARTIAL if a checklist exists but omits one or more required sections; a single end-of-phase gate token without a pre-close checklist does not satisfy C-24; C-10 (synthesis gate pair present) does not satisfy C-24 |
| C-25 | **Content-type schema prohibition** -- the SCORER schema prohibition names forbidden content categories (e.g., "evaluative prose", "narrative text", "mechanism analysis") in addition to or instead of specific forbidden field labels; type-category prohibition is enforceable regardless of how the field is labeled -- including novel field names a model might invent | enforcement | The SCORER schema includes at least one explicitly named content category or prose type that is prohibited; the content-type prohibition is introduced by its own labeled group header (`PROHIBITED CONTENT CATEGORIES:`) or equivalent paragraph-level structure making the category independently identifiable without reading all items; PARTIAL if content-type categories are present but co-listed with field labels in a single undifferentiated enumeration without a categorical group label; a prohibition listing only named field labels without any content-type characterization does not satisfy C-25; C-23 (field-name exclusion rule present) does not satisfy C-25 |
| C-26 | **Checkbox-format pre-close confirmation** -- each item in the synthesis pre-close checklist is expressed as a `[ ]` checkbox marker making individual section confirmation syntactically distinct; a numbered list, prose enumeration, or bullet list without per-item `[ ]` markers does not satisfy this criterion | enforcement | The synthesis pre-close checklist contains a `[ ]` checkbox marker for each required synthesis section; each checkbox appears on its own line adjacent to the section label; the instruction requires filling each checkbox before writing `[SYNTHESIS COMPLETE]`; PARTIAL if checkbox format is used but one or more required sections lack a corresponding `[ ]` marker; a numbered list without `[ ]` markers does not satisfy C-26; C-24 (pre-close checklist exists) does not satisfy C-26 |
| C-27 | **Required-field annotation token uniformity** -- all required-field annotations across all role schemas use the same syntactic token (e.g., always `(required)`, always `[required]`); mixed annotation styles across roles defeat single-scan completeness auditing | depth | Every required-field annotation across all role schemas (SCORER, VERIFIER, ANALYST) uses an identical syntactic token; PARTIAL if the annotation appears in all roles but uses different tokens in at least one role; a prompt that annotates required fields in only a subset of roles cannot satisfy C-27 (C-22 prerequisite not met); C-22 (annotation present in every phase) does not satisfy C-27 |
| C-28 | **Per-category placement routing annotation** -- each entry in the PROHIBITED CONTENT CATEGORIES group names the specific ANALYST section where that content type belongs (e.g., "evaluative prose -- belongs in ANALYST Primary differentiator or Verdict spread"); annotation at the entry level converts the prohibition from exclusion-only to routing-aware; a general routing statement covering all categories without per-entry granularity does not satisfy this criterion | enforcement | Each prohibited content category entry in the PROHIBITED CONTENT CATEGORIES group carries an explicit annotation naming at least one specific ANALYST section (LEADERBOARD, EXCELLENCE SIGNALS, FAILURE PATTERNS, REGRESSION SIGNALS, or a PER-OUTPUT NARRATIVE field label) as the canonical destination for that content type; PARTIAL if at least one entry carries a routing annotation but at least one entry is unannotated; a single general statement ("all prohibited content belongs in the Analyst's PER-OUTPUT NARRATIVE section") without per-entry annotations does not satisfy C-28; C-25 (labeled content-type group present) does not satisfy C-28 |
| C-29 | **Intra-run specificity dimension in VERIFIER** -- the VERIFIER specificity test explicitly includes the intra-run disambiguation question ("could this evidence apply to a different output in this scoring run?") in addition to the type-level genericity question ("could this apply to any well-designed output of this type?"); testing only type-level genericity misses evidence that is type-specific but run-undifferentiating | depth | The VERIFIER specificity test explicitly states both the type-level question ("could this evidence apply to any well-designed output of this type?") and the intra-run question ("could this evidence apply to a different output in this scoring run?"); PARTIAL if the intra-run question is implied but not explicitly stated; a specificity test that asks only the type-level question without naming the intra-run dimension does not satisfy C-29; C-17 (specificity test present) does not satisfy C-29 |
| C-30 | **VERIFIER pair-omission prohibition** -- the VERIFIER role definition contains an explicit instruction prohibiting omission of any criterion-output pair from its review, regardless of the Scorer's verdict; a VERIFIER that writes "one row per failing cell, PASS cells may be omitted" leaves all passing evidence cells unaudited for specificity; the explicit prohibition is a distinct requirement from a positive coverage mandate ("produce one block per pair"), which a "...except PASS cells" caveat can still defeat | enforcement | The VERIFIER role definition contains an explicit named prohibition on omitting criterion-output pairs where Specificity appears to PASS (e.g., "Do not omit any pair even where Specificity appears to PASS -- every criterion-output pair requires a review block"); PARTIAL if a positive coverage mandate is present ("for every output, for every criterion, produce one review block") without an explicit skip-prohibition naming the PASS-cell omission pattern as a prohibited deviation; a VERIFIER schema that explicitly permits "PASS cells may be omitted" is FAIL regardless of C-12 schema completeness; C-12 (per-cell schema structure defined and applied) does not satisfy C-30 |
| C-31 | **SCORER Evidence field -- violation type named at definition site** -- the SCORER Evidence field definition names the specificity failure mode as an explicit "cell violation" or equivalent at the field definition site; positive specification alone ("must name a feature specific to this output") without naming the violation type does not satisfy this criterion | enforcement | The SCORER Evidence field definition includes both a positive requirement AND explicitly names what constitutes a violation (e.g., "generic text that could describe any well-designed output of this type is a cell violation -- VERIFIER will flag and revise it"); PARTIAL if the field definition mentions specificity but names the failure consequence as a downstream catch ("VERIFIER will check") without naming the violation type at the definition site; absence of any violation-type language from the SCORER Evidence field definition is FAIL; C-17 (VERIFIER specificity test present) does not satisfy C-31; C-02 (rubric-level evidence requirement) does not satisfy C-31 |
| C-32 | **SCORER *Why* field -- anti-restatement prohibition at definition site** -- the SCORER *Why* field definition contains an explicit prohibition on criterion restatement AND evidence paraphrase at the field definition site; a *Why* field that specifies what mechanism to name without naming what it must not be leaves both restatement and paraphrase paths open | depth | The SCORER *Why* field definition explicitly prohibits criterion restatement AND evidence paraphrase adjacent to the positive requirement (e.g., "name the architectural property that produces this verdict; do not restate the criterion or paraphrase the evidence"); PARTIAL if the field definition includes one of the two prohibitions (restatement or paraphrase) but not both; a *Why* field definition specifying only what the field must contain without naming either anti-pattern is FAIL; C-11 FAIL implies C-32 FAIL; C-11 (field present and positive requirement stated) does not satisfy C-32 |
| C-33 | **Anti-pattern anchor -- exhaustive 1:1 failure-mode/mechanism pairing** -- every named failure mode in the anti-pattern anchor is paired with its own dedicated closing mechanism; parallel indexing makes the failure-mode→mechanism map explicitly complete and indexable; a single shared mechanism covering multiple failure modes does not satisfy this criterion | enforcement | Every failure mode named in the anti-pattern anchor block is paired 1:1 with its own named closing mechanism using parallel indexing (e.g., Mode A / Mechanism 1, Mode B / Mechanism 2); the total count of failure modes equals the total count of named mechanisms; PARTIAL if pairing is present but parallel indexing is absent, or if at least one failure mode shares a mechanism with another; C-09 FAIL implies C-33 FAIL; C-09 PASS (at least one mode/mechanism pair present) does not satisfy C-33 |
| C-34 | **PROHIBITED CONTENT CATEGORIES -- negative completeness assertion** -- after all per-entry routing annotations, the PROHIBITED CONTENT CATEGORIES list concludes with an explicit negative completeness assertion stating that no category lacks a named destination; the assertion converts the list from an open enumeration to a self-verifying set | enforcement | The PROHIBITED CONTENT CATEGORIES section concludes with an explicit assertion of the form "No prohibited content category lacks a named destination" (or equivalent negative completeness claim); the assertion appears after all entries, not in a preamble; PARTIAL if a completeness claim appears in a general preamble rather than as a terminal assertion after all entries; absence of any completeness assertion is FAIL; C-28 FAIL implies C-34 FAIL; C-28 PASS (all entries annotated) does not satisfy C-34 |
| C-35 | **VERIFIER specificity dimensions -- structurally separated labeled fields** -- the type-level and intra-run specificity questions each occupy their own dedicated labeled structural slot (column or required field) in the VERIFIER schema; structural separation makes each question an independently auditable output dimension; both questions present in a single combined Specificity field do not satisfy this criterion | enforcement | The VERIFIER schema defines the type-level question and the intra-run question as structurally distinct labeled slots (e.g., separate table columns labeled `Type-level` and `Intra-run`, or two separate required fields in a block schema); each slot carries its own PASS/FAIL value; PARTIAL if both questions are named in the VERIFIER role instructions but share a single combined Specificity slot in the output schema; C-29 FAIL implies C-35 FAIL; C-29 PASS (both questions explicitly stated) does not satisfy C-35 |

---

## Weight Summary

| Tier | Criteria | Count | Points |
|------|----------|-------|--------|
| Essential | C-01 -- C-05 | 5 | 60 |
| Recommended | C-06, C-07 | 2 | 30 |
| Aspirational | C-08 -- C-35 | 28 | 220 |
| **Total** | | | **310** |

**Formula**: `(essential_pass / 5 * 60) + (recommended_pass / 2 * 30) + (aspirational_pass / 28 * 220)`

**Golden threshold**: all 5 essentials PASS + composite >= 80

**PARTIAL scoring**: PARTIAL = 0.5 for all tier counts

---

## Scoring Notes

**C-01 (verdict matrix):** Formats vary -- table, indented list, or grouped blocks -- as long as every criterion-output cell has a stated verdict. Implied verdicts ("all PASS" in a notes column) count only if unambiguous.

**C-02 (evidence):** A shared Notes column covering all outputs for a criterion satisfies the requirement if the note is specific enough to verify each output's verdict. Generic notes ("all use the correct form") satisfy C-02 only when the form is narrow and unambiguous.

**C-03 (composite score):** The formula denominator must match the current rubric version: v12 uses `/ 28 * 220`. Using a prior-version formula (e.g., `/ 25 * 220`) is FAIL regardless of correct arithmetic.

**C-04 (leaderboard):** A final ranking list, a score table sorted by score, or a "Ranking" section all satisfy C-04. The ranking must be explicit.

**C-05 (failure patterns):** A criterion failing in all outputs signals either a rubric gap or a systematic skill design issue. Surfacing this is the primary diagnostic value of batch scoring.

**C-06 (excellence signals):** An excellence signal requires a specific output-criterion pairing with the structural mechanism named. A general comment that one output scored highest overall does not satisfy C-06.

**C-07 (regression signals):** N/A in round 1 (no prior data). Outputs should receive PARTIAL rather than FAIL if they explicitly state "no prior round data available." Silence on regressions is FAIL.

**C-08 (golden threshold):** The golden field must be present as a required output field in the SCORER schema, not computed externally. Each output block must contain it.

**C-09 (anti-pattern anchor):** The anchor must precede the scoring instructions. The failure mode shown must be specific to at least one essential criterion -- a generic "be thorough" warning does not qualify.

**C-10 (synthesis gate pair):** The gate must cover all four synthesis sections. A gate covering only some sections is PARTIAL. A single `[ANALYST COMPLETE]` token without `[SYNTHESIS OPEN]` is FAIL.

**C-11 (*Why* field):** A `*Why*:` field asking "what structural feature does this demonstrate?" satisfies C-11. A field asking only for "more detail" does not. The mechanism must be tied to the verdict, not just the criterion text.

**C-12 (structured verification block):** The labeled schema must cover every criterion-output pair, not only suspect cells. A VERIFIER that applies the specificity test only to cells it flags as potentially generic does not satisfy C-12. Note: C-12 PARTIAL + C-30 FAIL is a coherent combination (V-02 R10): schema structure present with labeled fields, but coverage instruction explicitly authorizes omitting PASS cells.

**C-13 (inline *Change*):** The CHANGE note must be written at the point of scoring the criterion, not compiled retrospectively in synthesis.

**C-14 (baseline load gate):** N/A (scored PARTIAL, not FAIL) when no prior round data exists and the output explicitly states this. When prior data is available, absence of a load gate is FAIL.

**C-15 (mandatory *Change* field):** A conditional CHANGE slot does not satisfy C-15. The `NO PRIOR DATA` third value is required -- without it, first-round scoring cannot fill the field. C-15 tightens C-13: a conditional slot (C-13) allows silent skip; a mandatory field (C-15) does not.

**C-16 (Change Manifest phase):** The manifest phase must precede SYNTHESIS entirely. The explicit prohibition on re-reading the baseline table or SCORER blocks during SYNTHESIS is required for PASS; absent prohibition is PARTIAL. C-16 tightens C-13 on the fresh-lookup axis.

**C-17 (evidence specificity test):** A general instruction to "write specific evidence" in the scoring phase does not satisfy C-17. The criterion requires a structurally distinct second pass that revisits completed evidence cells with an explicit test.

**C-18 (VERIFIER role with gate):** The VERIFIER must be a named role with its own gate token. A prompt where verification is embedded in the ANALYST role without a separate gate does not satisfy C-18.

**C-19 (three-field narrative):** All three prescribed fields are required. The verdict spread must explain distribution, not just total score: why did this output cluster points in aspirational rather than recommended, or vice versa?

**C-20 (inter-role gate architecture):** A synthesis gate (C-10) is not an inter-role gate. A prompt with only `[ANALYST COMPLETE]` has zero inter-role gates and is FAIL on C-20.

**C-21 (bidirectional gate inscription):** "SCORER writes `[SCORER COMPLETE]` when done" satisfies C-20 but not C-21. "VERIFIER: Do not begin until `[SCORER COMPLETE]` appears above" satisfies both.

**C-22 (required-field annotation):** The annotation must be adjacent to the field label, not only in a preamble. PARTIAL if some but not all mandatory fields across all roles carry the annotation.

**C-23 (field-name exclusion rule):** "Include Verdict and Evidence" without "no other fields are permitted" does not satisfy C-23. PARTIAL if a field-exclusion rule exists but applies to only some SCORER blocks.

**C-24 (pre-close checklist):** The checklist must enumerate each required synthesis section by name. A checklist that says "confirm synthesis is complete" without naming the individual sections does not satisfy C-24.

**C-25 (content-type schema prohibition):** Requires a labeled categorical group header or paragraph-level structure making the category independently identifiable. A single FORBIDDEN list mixing field labels and content categories without a categorical group label is PARTIAL.

**C-26 (checkbox format):** The `[ ]` format makes section-skipping visible as an unfilled box. A numbered list without per-item `[ ]` markers does not satisfy C-26 even if all sections are named.

**C-27 (token uniformity):** Mixed tokens across roles (e.g., `(required)` in SCORER, "mandatory" in VERIFIER) are PARTIAL. The scan rule fails when different tokens are used.

**C-28 (per-category routing):** Each individual entry in PROHIBITED CONTENT CATEGORIES must name its destination ANALYST section. A general statement ("all prohibited content belongs in PER-OUTPUT NARRATIVE") is PARTIAL, not PASS. C-28 tightens C-25: a prompt can pass C-25 (categorical group labeled) while failing C-28 (entries lack routing annotations).

**C-29 (intra-run specificity):** Both questions must be present for PASS: the type-level question ("could this apply to any well-designed output?") AND the intra-run question ("could this apply to a different output in this scoring run?"). C-29 tightens C-17: a prompt can pass C-17 (specificity test present) while failing C-29 (intra-run question absent).

**C-30 (pair-omission prohibition):** The prohibition must be explicit and name the PASS-cell skip pattern as the target deviation. "For every output, for every criterion, produce one review block" is a positive coverage mandate (satisfies C-12, earns C-30 PARTIAL). "Do not omit any pair even where Specificity appears to PASS -- a VERIFIER that writes only failing-cell rows is a schema violation" is the explicit prohibition required for C-30 PASS. C-30 tightens C-12: a prompt can pass C-12 while scoring C-30 PARTIAL.

**C-31 (Evidence field violation naming):** The violation-type language must appear inside the Evidence field definition in the SCORER schema -- not only in the VERIFIER role or in a general preamble. "Specific structural observation from this output" (positive) does not satisfy C-31. "Generic text that could describe any well-designed output of this type is a cell violation -- VERIFIER will flag and revise it" (positive + named violation) satisfies C-31. C-31 tightens C-02 and C-17: a prompt can pass both while leaving the Evidence field definition as positive-only (C-31 FAIL).

**C-32 (*Why* field anti-restatement):** Both prohibited modes must be named at the field definition site: (1) criterion restatement and (2) evidence paraphrase. Naming only one is PARTIAL. The prohibition must appear within the *Why* field definition in the SCORER schema -- not only in the rubric's evaluation criteria or in a preamble. C-32 tightens C-11: a prompt can pass C-11 (field present, names mechanism) while leaving the field definition as positive-only (C-32 FAIL).

**C-33 (exhaustive 1:1 pairing):** Every failure mode must be paired with its own mechanism -- not shared across modes. Parallel indexing (A/1, B/2, ...) is required to make the mapping auditable. A 5-mode anchor with mechanisms labeled 1--5 but no explicit A/1...E/5 pairing structure is PARTIAL. C-33 tightens C-09: a prompt can pass C-09 (at least one mode/mechanism pair) while failing C-33 (modes share a mechanism or pairing is not indexed).

**C-34 (negative completeness assertion):** The assertion must appear as a terminal statement after all entries in the PROHIBITED CONTENT CATEGORIES section -- not in a preamble or general routing note. "All prohibited content is routed to ANALYST" in a preamble is not a terminal assertion. "No prohibited content category lacks a named destination" after the last entry satisfies C-34. C-34 requires C-28 PASS as a prerequisite: a terminal assertion over an incompletely annotated list does not satisfy C-34.

**C-35 (dual-scope structural separation):** Structural separation means two distinct output slots, not two questions embedded in one field. A VERIFIER TABLE with a single "Specificity" column that poses both questions in its header does not satisfy C-35 -- the column is still a single slot. Two columns ("Type-level" / "Intra-run"), or two required fields ("Specificity -- type-level:" / "Specificity -- intra-run:") in a block schema, satisfy C-35. C-35 tightens C-29: a prompt can pass C-29 (both questions stated) while failing C-35 (questions share a single output slot).

**C-29/C-30/C-31/C-32/C-33/C-34/C-35 independence:** C-29 and C-35 both operate on VERIFIER specificity scope, but at different layers (C-29: both questions stated; C-35: both questions structurally separated). C-30 operates on VERIFIER coverage instruction. C-31 operates on SCORER Evidence field definition. C-32 operates on SCORER *Why* field definition. C-33 operates on anchor pairing completeness. C-34 operates on PROHIBITED CONTENT terminal assertion. All seven are mutually orthogonal: a prompt can pass any subset while failing the remainder.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-15 | Initial -- 8 criteria; total max 100 |
| v2 | 2026-03-15 | Add C-09/C-10/C-11 from R1; aspirational 40 pts; total max 130 |
| v3 | 2026-03-15 | Add C-12/C-13/C-14 from R2; aspirational 70 pts; total max 160 |
| v4 | 2026-03-15 | Add C-15/C-16 from R3; aspirational 90 pts; total max 180 |
| v5 | 2026-03-15 | Add C-17/C-18 from R5; aspirational 110 pts; total max 200 |
| v6 | 2026-03-15 | Add C-19/C-20 from R6; aspirational 130 pts; total max 220 |
| v7 | 2026-03-15 | Add C-21/C-22/C-23/C-24 from R7; aspirational 170 pts; total max 260 |
| v8 | 2026-03-15 | Add C-25/C-26/C-27 from R8; aspirational 200 pts; total max 290 |
| v9 | 2026-03-15 | Add C-28/C-29 from R9; aspirational 220 pts; total max 310 |
| v10 | 2026-03-15 | Add C-30 from R10; aspirational denominator 22->23; total max 310 (unchanged) |
| v11 | 2026-03-15 | Add C-31/C-32 from R11; aspirational denominator 23->25; total max 310 (unchanged) |
| v12 | 2026-03-15 | Add C-33/C-34/C-35 from R12; aspirational denominator 25->28; total max 310 (unchanged) |

**R12 excellence source:**

| ID | Name | Source | Failure mode closed |
|----|------|--------|---------------------|
| C-33 | Anti-pattern anchor -- exhaustive 1:1 failure-mode/mechanism pairing | V-01 R12 C-09 evidence: "5 named failure modes (A-E) appears before ROLE 1; each mode shows a typical output and a named closing mechanism (Mechanism 1-5)" | **Anchor shared-mechanism path** -- C-09 PASS requires at least one failure mode with at least one mechanism, and PARTIAL fires when failure modes outnumber named mechanisms; this implies a coverage direction but does not require per-mode dedicated pairing; a 5-mode anchor with 5 mechanisms where all modes reference Mechanism 1 satisfies C-09; C-33 closes this path by requiring the pairing to be exhaustive and indexed |
| C-34 | PROHIBITED CONTENT CATEGORIES -- negative completeness assertion | V-02 R12 C-28 evidence: "closing statement 'No prohibited content category lacks a named destination'" after all per-entry routing annotations | **Open-enumeration path** -- C-28 PASS requires every entry to carry a routing annotation; a fully-annotated list at time of writing leaves the completeness guarantee implicit: a future addition can silently lack a destination; the terminal negative assertion converts the list from an open enumeration to a self-verifying set, making incompleteness visible at the list boundary rather than detectable only by re-reading all entries |
| C-35 | VERIFIER specificity dimensions -- structurally separated labeled fields | V-03 R12 C-29 evidence: "VERIFIER TABLE with labeled columns: Output, Criterion, Scorer evidence, Type-level, Intra-run, Specificity, Revised evidence" -- separate columns for each specificity dimension | **Question-merging path** -- C-29 PASS requires both the type-level and intra-run questions to be explicitly stated; both can appear as prose instructions within a single combined Specificity column or field; when combined, a model filling the field can answer the type-level question alone while appearing to address both; structural separation into distinct labeled slots makes each question an independently auditable output slot whose PASS/FAIL value is independently recorded |

---

**R12 structural observations (not new criteria):**

1. **C-33/C-34/C-35 as enumeration-completeness closers:** All three new criteria operate at the same structural level -- they require completeness guarantees to be made explicit at the boundary of a collection (anchor block, prohibition list, VERIFIER schema), not only at individual item level. C-33 closes the anchor's failure-mode→mechanism map. C-34 closes the prohibition list's routing coverage. C-35 closes the VERIFIER schema's question coverage. Each prior criterion (C-09, C-28, C-29) specified what items must contain; each new criterion specifies that the collection must be complete and explicitly assert so.

2. **No single R12 variation achieves all three new criteria:** V-01 passes C-33 (5 paired anchor modes) but fails C-34 (no terminal assertion) and C-35 (no separated VERIFIER columns). V-02 passes C-34 (terminal assertion present) but fails C-33 (no anchor) and C-35 (type-level-only VERIFIER). V-03 passes C-35 (dual-column VERIFIER TABLE) but fails C-33 (no anchor) and C-34 (no terminal assertion). The R13 ceiling target is a single variation combining all three architectural features.

3. **Formula denominator shift:** Adding C-33, C-34, and C-35 changes the aspirational denominator (25 -> 28) without changing the maximum points (220). Each aspirational criterion is now worth 220/28 ~= 7.86 points at PASS, down from 8.8. Scores from v11 and v12 are not directly comparable; v12 re-scoring is required for cross-version leaderboard comparisons. Golden threshold (composite >= 80) is unchanged.

---

## Machine-Readable Footer

A conformant `quest-score` output ends with:

```json
{"top_score": <float>, "all_essential_pass": <bool>, "new_patterns": [<string>, ...]}
```

The rubric does not score for this footer, but scorers should note its presence as a signal of output completeness and machine-parseability.

---

**Three new criteria, one structural theme.** C-33/C-34/C-35 all close the same class of failure: a collection whose items satisfy their individual requirements but whose completeness is never explicitly asserted. The C-09 anchor, the C-28 routing list, and the C-29 VERIFIER specificity dimensions each had per-item requirements; v12 requires each collection to seal itself with a completeness claim at its boundary. R13's ceiling target is the first variation to combine all three.
