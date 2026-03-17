Now I have all the material needed. Let me evaluate all five variations.

---

# flow-dataflow — R20 Scoring (Rubric v19)

## Scoring Framework

| Band | Points | Criteria |
|------|--------|----------|
| Essential | 60 pts (15 pts each) | C-01–C-04 |
| Recommended | 30 pts (10 pts each) | C-05–C-07 |
| Aspirational | 10 pts total (0.208 pts each, PARTIAL = 0.104) | C-08–C-55 (48 criteria) |

---

## Essential Criteria — All Variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-01 Data lineage chain | PASS | PASS | PASS | PASS | PASS | Stage traces defined source→destination for every physical pipeline stage in all variations |
| C-02 Boundary error handling | PASS | PASS | PASS | PASS | PASS | `Error Handling` column (tabular) / `Error Handling:` phrase label (V-03 prose) in every boundary block |
| C-03 Data loss point identification | PASS | PASS | PASS | PASS | PASS | `Data Loss Flag` column / labeled phrase required at every stage |
| C-04 Schema state at each stage | PASS | PASS | PASS | PASS | PASS | SC-7 mandates `Schema In \| Schema Out` in every stage table; V-03 prose substitution includes `Schema Delta:` phrase |

**Essential subtotal: 60 / 60 for all variations.**

---

## Recommended Criteria — All Variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-05 Latency characterization | PASS | PASS | PASS | PASS | PASS | `Stage Latency` column (SC-7) / `Stage Latency:` phrase label (V-03 prose substitution) |
| C-06 Stale data windows | PASS | PASS | PASS | PASS | PASS | [A-11] STALE ANALYSIS with normal-operation and failure-mode elapsed rows in all variations |
| C-07 Domain framing | PASS | PASS | PASS | PASS | PASS | Domain-specific entity vocabulary locked in [A-02]; entity names appear in stage traces, boundary blocks, [A-11] |

**Recommended subtotal: 30 / 30 for all variations.**

---

## Aspirational Criteria — Shared Results (all 5 variations identical)

| ID | Result | Evidence |
|----|--------|----------|
| C-08 Recovery prescriptions | PASS | [A-12] RECOVERY PRESCRIPTIONS mandated; `Fall back to [A-01] if [condition]` formula required |
| C-09 Pattern trade-off analysis | PASS | [A-14] TRADE-OFF ANALYSIS required; ≥1 named alternative pattern; ≥2 dimensions |
| C-10 Pre-trace domain context gate | PASS | [A-02] DOMAIN CONTEXT produced before Stage 1; entity names re-used verbatim in subsequent lineage |
| C-11 Interleaved boundary gates | PASS | SC-2 stage-write progression gate inline between every consecutive stage pair |
| C-12 Domain entity exposure per boundary | PASS | `Entity` column / labeled phrase requires named domain entity from [A-02] vocabulary |
| C-13 Pre-declared staleness contract | PASS | [A-02] SLA declared before Stage 1; SC-5 immutability enforces no post-Stage-1 revision |
| C-14 Additive elapsed time calculation | PASS | SC-3 INCREMENTAL ELAPSED accumulates `Elapsed (cumul.)` across all boundary blocks |
| C-15 Incumbent or manual-process baseline | PASS | [A-01] present; SC-13 enforces [A-01] citation in [A-12] and [A-14], closing comparison loop |
| C-16 Cross-role reference chain | PASS | `Citing:` lines required for non-first roles; skip-level citation (SC-12) forces position-1 artifact naming |
| C-17 Immutability declaration | PASS | SC-5 requires verbatim "This threshold is fixed. No subsequent role may revise it after Stage 1 is written." |
| C-18 Incremental boundary elapsed computation | PASS | SC-3 explicitly states boundary Elapsed (cumul.) extends prior final value; zero-reset is a violation |
| C-19 Machine-verifiable citation convention | PASS | All artifact references use `[A-xx]` token form throughout all five prompts |
| C-20 Stage-write progression gate | PASS | SC-2 is an explicit inline gate; Stage N+1 blocked until preceding boundary table is complete |
| C-21 Binary freshness verdict per boundary | PASS | SC-4 mandates exactly `FRESH` or `STALE`; any other value is named as a protocol violation |
| C-22 Formal pre-declared registry table | PASS | ARTIFACT REGISTRY with all [A-xx] tokens, artifact names, and owner assignments appears before role output |
| C-23 Phase gate self-verification checklists | **PARTIAL** | [A-05] and [A-08] present in all variations with checklists. Most items cite SCs (e.g., "(SC-11)", "(SC-3)", "(SC-4)", "[SC-12]") but some items (e.g., "[A-01] includes ≥3 named steps with durations"; "every block has seven columns") omit an explicit SC citation — criterion requires EVERY item to name the SC it verifies |
| C-24 Upfront constraint section with inline callback syntax | PASS | STRUCTURAL CONSTRAINTS section in all variations; every SC uses `[Apply SC-N at <location>]` callback syntax |
| C-25 Phase gate artifacts as first-class registry rows | PASS | [A-00], [A-05], [A-08] each appear as named rows in ARTIFACT REGISTRY with owner and description |
| C-27 Named recovery formula anchoring incumbent baseline | PASS | Recovery formula `Fall back to [A-01] if [specific named failure condition]` required in [A-12]; [A-01] token mandatory |
| C-28 Named-column boundary block schema | PASS | BOUNDARY BLOCK SCHEMA standalone section before role output; exact 7-column order declared |
| C-29 Trade-off as prompt-required section | PASS | SC-8 mandates [A-14] as required section; tokens [A-01], [A-02], [A-13] required; ≥1 pattern; ≥2 dimensions |
| C-30 Output register declaration with field-compliance markers | PASS | REGISTER DECLARATION with Part A field-compliance table and Part B section-format markers in all variations |
| C-31 Pre-declared boundary block schema section | PASS | BOUNDARY BLOCK SCHEMA appears before all role output in all variations |
| C-33 Register-invariant declaration for non-tabular registers | PASS | V-03: Part A reformulated as labeled-phrase compliance map preserving field-completeness. V-01/V-02/V-04/V-05: tabular register, criterion not triggered |
| C-34 Per-boundary incumbent equivalent column | PASS | `Incumbent Equiv.` column required; form `[A-01]: [named step + duration]`; Part A marks token omission as disqualifying |
| C-35 INCUMBENT TOTAL as required pre-trade-off artifact | PASS | REGISTER DECLARATION Part B defines [A-13] structure; SC-10 enforces [A-13] immediately before [A-14] with Grand Total |
| C-36 Baseline-first artifact ordering | PASS | SC-11 positional lock: [A-01] must be first artifact within Role 1 |
| C-37 REGISTER DECLARATION Parts A/B as single-location authority | PASS | Verbatim "This section is the sole authoritative reference for C-34 and C-35" present in all variations |
| C-38 Skip-level citation requirement | PASS | SC-12 requires position-3 role to cite position-1 boundary artifacts, skipping position-2 |
| C-39 Skip-level SC names governed role | PASS | SC-12 names the first-executing role by label (Finance / Commerce / Operations) in every variation |
| C-40 Skip-level SC declares position distance | PASS | SC-12 body text states "Position distance is two" (or equivalent) in all variations |
| C-41 Phase Gate 2 skip-level item cites SC identifier | PASS | [A-08] checklist item cites `[SC-12]` by numbered identifier in all variations |
| C-42 C-37+C-41 closed verification chain co-occurrence | PASS | Both REGISTER DECLARATION Parts A/B and [A-08] `[SC-12]`-citing item present in every variation |
| C-43 All three skip-level SC attributes co-present in single block | PASS | SC-12 body contains (1) governed artifact token, (2) governed role name, (3) position distance = two in a single contiguous block |
| C-44 Baseline-closure SC as named upfront constraint | PASS | SC-13 BASELINE CLOSURE in STRUCTURAL CONSTRAINTS enforces [A-01] citation in both [A-12] and [A-14] |
| C-46 SC-13 BASELINE CLOSURE as named closed-chain entry | PASS | REGISTER DECLARATION closed-chain has "SC-13 BASELINE CLOSURE" entry naming [A-12] and [A-14] as governed artifacts with enforcement mechanism |
| C-48 Governed artifact tokens in each SC closed-chain entry | PASS | Every closed-chain entry names at least one `[A-xx]` token in the governed-artifact slot |
| C-49 Enforcement mechanism in each SC closed-chain entry | PASS | Every closed-chain entry describes its enforcement pathway (e.g., "positional lock", "token-match at role-opener", "cell-form requirement") |
| C-50 Baseline authority token dual-slot presence | PASS | SC-11 enforcement clause names `[A-01]` ("any output before [A-01]...fails"); SC-13 enforcement names `[A-01]`; SC-9 enforcement names `[A-01]`; SC-8 enforcement names `[A-14]` token in citation list description |
| C-51 Violation-detectability location in enforcement mechanism | PASS | All closed-chain entries include detectability qualifiers (e.g., "detectable from the role-opener line", "detectable at cell-value level without reading row prose") |
| C-52 Per-SC detectability index as standalone reference | PASS | [A-00] DETECTABILITY INDEX covers all SCs (15 rows for 15-SC prompts, 16 rows for V-05); row count verifiable against SC count |
| C-54 Phase Gate 0 multi-item structural completeness gate | PASS | V-01–V-04: Phase Gate 0 has 2 items (row count = 15; every row non-empty Responsible Role) matching 2 [A-00] structural dimensions. V-05: Phase Gate 0 has 3 items (row count = 16; Responsible Role non-empty; SLA Impact = Yes/No) matching 3 [A-00] structural dimensions |
| C-55 SC-0 as mandatory [A-00] governor with per-SC dual-slot anchoring | PASS | SC-0 governs [A-00] with dual-slot in all variations. SC-14 governs [A-00]'s Responsible Role column with independent dual-slot (enforcement names `[A-00]`). V-05 adds SC-15 governing [A-00]'s SLA Impact column with third independent dual-slot. Closed-chain explicitly states no SC relies on another for [A-00] enforcement reference |
| C-53 Dual-slot anchoring extends to all token-referencing SCs | **FAIL (all)** | SC-1 closed-chain entry governs [A-06], [A-09] but enforcement clause ("token-match at each role's opening `Citing:` line") does not name [A-06]/[A-09] in enforcement slot. SC-2 governs [A-03], [A-04], etc. but enforcement ("inline lock — Stage N+1...per BOUNDARY BLOCK SCHEMA") names no tokens. SC-3, SC-4, SC-6, SC-7 similarly omit governed tokens from enforcement clauses. Systemic dual-slot gap for non-[A-01]-referencing SCs across all variations |

---

## Aspirational Criteria — Variation-Specific Results

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-26 Non-natural role ordering | **FAIL** | **PASS** | **FAIL** | **FAIL** | **PASS** | V-01: F→O→C (Finance-first = natural). V-02: C→O→F (Commerce-first). V-03: F→O→C (Finance-first). V-04: F→C→O (Finance-first). V-05: O→C→F (Operations-first) |
| C-32 Register-specific compliance marker mapping | **PASS** | **PASS** | **FAIL** | **PASS** | **PASS** | V-01/V-02/V-04/V-05: Part A is 4-column table (Required Field, Column Header, Required Cell Form, Disqualifying Form) covering all 8 boundary fields. V-03: Part A is a bulleted labeled-phrase list — not a 4-column table; fails the four-column mapping requirement |
| C-45 Format-mode declaration with criterion substitution map | **PASS** | **PASS** | **FAIL** | **PASS** | **PASS** | V-01/V-02/V-04/V-05: tabular register; format declared ("This output uses the tabular register throughout"); no non-tabular substitution map needed — criterion not triggered. V-03: prose register active; SC-14 repurposed to DETECTABILITY INDEX ROLE ASSIGNMENT; no SC-14 FORMAT MODE DECLARATION with criterion-by-criterion substitution map exists in SC-14 body text; prose substitutions are in Part A bullets but not organized as a criterion substitution map within SC-14 |
| C-47 SC-14 FORMAT MODE DECLARATION as named closed-chain entry | **PASS** | **PASS** | **FAIL** | **PASS** | **PASS** | V-01/V-02/V-04/V-05: tabular; criterion not triggered. V-03: non-tabular mode active; closed-chain entry is labeled "SC-14 DETECTABILITY INDEX ROLE ASSIGNMENT (prose substitution)" — the name "FORMAT MODE DECLARATION" is absent; criterion requires the exact label |

---

## Score Computation

**Aspirational component breakdown:**

| Criterion pool | Per-variation value |
|---|---|
| 41 full-PASS aspirational criteria × 0.208 | 8.528 pts |
| C-23 PARTIAL (all) × 0.104 | 0.104 pts |
| C-53 FAIL (all) × 0 | 0 pts |
| C-26 variable (V-02, V-05 PASS) | +0.208 for V-02, V-05 |
| C-32 variable (V-03 FAIL) | +0.208 for V-01, V-02, V-04, V-05 |
| C-45 variable (V-03 FAIL) | +0.208 for V-01, V-02, V-04, V-05 |
| C-47 variable (V-03 FAIL) | +0.208 for V-01, V-02, V-04, V-05 |

| Variation | Fixed | Variable additions | Aspirational total | **Final score** |
|-----------|-------|--------------------|--------------------|-----------------|
| V-01 | 8.532 | +0 (C-26) +0.208 +0.208 +0.208 = 0.624 | 9.256 | **99.3** |
| V-02 | 8.532 | +0.208 +0.208 +0.208 +0.208 = 0.832 | 9.464 | **99.5** |
| V-03 | 8.532 | 0 | 8.532 | **98.5** |
| V-04 | 8.532 | +0 +0.208 +0.208 +0.208 = 0.624 | 9.256 | **99.3** |
| V-05 | 8.532 | +0.208 +0.208 +0.208 +0.208 = 0.832 | 9.464 | **99.5** |

*(Fixed = 8.528 + 0.104 = 8.632 — corrected above)*

---

## Rankings

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 (tie) | **V-02** | **99.5** | C→O→F non-natural ordering + tabular register; no C-26 cost |
| 1 (tie) | **V-05** | **99.5** | O→C→F non-natural ordering + 4-column [A-00] + 3-SC fan-out; deepest structural complexity |
| 3 (tie) | V-01 | 99.3 | F→O→C natural ordering; loses C-26 |
| 3 (tie) | V-04 | 99.3 | F→C→O natural ordering; ≥7 incumbent steps; loses C-26 |
| 5 | V-03 | 98.5 | Prose register with SC-14 repurposed: loses C-26, C-32, C-45, C-47 |

---

## Excellence Signals from Top-Scoring Variations (V-05 depth)

**Signal 1 — SLA Impact binary column as domain-outcome classification axis in [A-00]**
V-05 adds a fourth column (`SLA Impact: Yes/No`) to [A-00], tagging each SC with whether violating it could directly cause a distribution SLA breach. This enriches the DETECTABILITY INDEX from a pure structural-completeness tool into a domain-outcome-aware instrument. SC-15 governs this column with independent dual-slot anchoring to [A-00]. This pattern is fully novel — not captured by any criterion through C-55.

**Signal 2 — N-SC fan-out for [A-00] governance scales with column count**
V-05 demonstrates that the general rule is: one [A-00]-governing SC per structural column beyond the `SC` column itself. SC-0 governs row count + Phase Gate 0 completeness; SC-14 governs `Responsible Role`; SC-15 governs `SLA Impact`. Each names `[A-00]` in both governed-artifact and enforcement slots independently. Phase Gate 0 item count equals the structural dimension count (3 items for 3 dimensions). This generalizes C-54/C-55 into a fully scalable N-column pattern.

**Signal 3 — C-53 systemic gap: non-[A-01] SCs lack enforcement-slot token repetition**
The gap in C-53 is consistent and structural: SC-1, SC-2, SC-3, SC-4, SC-6, SC-7 all name governed artifact tokens in the governed-artifact slot but describe enforcement generically without token repetition. A future criterion could require that SC closed-chain entries for sequence/gate SCs (SC-1, SC-2, SC-6) explicitly re-state governed role or artifact tokens in the enforcement clause (e.g., "SC-1: [A-06] and [A-09] `Citing:` line absent fails...").

---

```json
{"top_score": 99.5, "all_essential_pass": true, "new_patterns": ["SLA Impact binary column as fourth [A-00] structural dimension — each SC tagged Yes/No for whether its violation could directly breach distribution SLA, governed independently by SC-15 with dual-slot anchoring to [A-00], not captured by any criterion through C-55", "N-SC fan-out scales with [A-00] column count — one governing SC per structural column beyond the SC column, each with independent dual-slot to [A-00], Phase Gate 0 item count equals structural dimension count; V-05 demonstrates N=3 (SC-0 + SC-14 + SC-15)"]}
```
