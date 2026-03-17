## Round 4 Scorecard — prove-intelligence

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-05 All three combined | 5/5 | 3/3 | 11/11 | **100** | YES |
| 2 | V-04 C-17 + C-18 | 5/5 | 3/3 | 10/11 | **99.1** | YES |
| 3 | V-02 C-17 single-axis | 5/5 | 3/3 | 9/11 | **98.2** | YES |
| 4 (tie) | V-01 C-19 single-axis | 5/5 | 3/3 | 7/11 | **96.4** | YES |
| 4 (tie) | V-03 C-18 single-axis | 5/5 | 3/3 | 7/11 | **96.4** | YES |

All five GOLDEN. Floor 96.4 (new /11 denominator).

---

**The single discriminator pattern**: V-04 vs V-05 isolates C-19 cleanly. V-04 has C-17+C-18 and advisory gate; V-05 adds halt semantics with Option A/B contract. The 0.9pt gap is entirely C-19.

**Aspirational profile per variation:**
- V-01 misses C-15, C-16, C-17, C-18 (four misses, step-based format without schema contract or multi-state ledger)
- V-02 misses C-16, C-18 (schema contract without lifecycle)
- V-03 misses C-12, C-15, C-17, C-19 (lifecycle without schema or halt semantics)
- V-04 misses C-19 only (intentional)
- V-05 misses nothing

**Two new patterns for potential C-20/C-21:**
1. `option-contract-as-halt-resolution-enforcement` — the halt names exactly two valid exits; proceeding without selecting one is a named protocol violation, not just ignored guidance
2. `schema-clean-prerequisite-to-in-progress-emission` — confirming CLEAN before emitting IN-PROGRESS makes the Redirect Agenda structurally guaranteed to reflect schema-verified rows

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["option-contract-as-halt-resolution-enforcement", "schema-clean-prerequisite-to-in-progress-emission"]}
```
nal Criteria (10 pts total)

#### C-09 -- Output identifies at least one internal contradiction

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 7: named conflict format -- "Source A ([path]) and Source B ([path]) disagree on [X]." Negative case explicit. |
| V-02 | **PASS** | B4: row-anchored format -- "Row N ([path]) and Row M ([path]) disagree on [X]." |
| V-03 | **PASS** | Phase D Contradiction Check with source-path anchors. |
| V-04 | **PASS** | Phase 4b Contradiction Check with row-path references. |
| V-05 | **PASS** | Phase 4b Contradiction Check, row-anchored, negative case explicit. |

#### C-10 -- Output recommends follow-up queries for evidence gaps

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 9: three-part format (Query / Where / Addresses), FC-linked, minimum two. |
| V-02 | **PASS** | B5: same three-part format, tied to uncovered FCs. |
| V-03 | **PASS** | Phase D: queries tied to `open` FCs from IN-PROGRESS state -- ledger lifecycle informs query selection. |
| V-04 | **PASS** | Phase 4c: three-part format, tied to `open` FCs from IN-PROGRESS ledger or weakly-evidenced FCs. |
| V-05 | **PASS** | Phase 4c: same -- IN-PROGRESS state directly drives query generation. |

#### C-11 -- Insider advantage treated as a hard exit condition

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 5 Insider Gate: count block + WARNING with "STOP. Do not proceed to Step 6." Named Gate status: PASS / BLOCKED. |
| V-02 | **PASS** | B1 Insider Gate: count block + WARNING with "STOP. Do not proceed to B2." |
| V-03 | **PASS** | Phase C Insider Gate: count block + WARNING block. Gate blocks Phase D entry. |
| V-04 | **PASS** | Phase 3 Insider Gate: count block + WARNING block. Gate blocks Phase 4 entry. |
| V-05 | **PASS** | Phase 3 Insider Gate: count block + WARNING with four explicit prohibitions. Gate blocks Phase 4 entry unconditionally. |

#### C-12 -- Extraction and interpretation are structurally separated

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 3 (Candidate Files table, "do not summarize from memory") precedes Step 4 (Source N blocks with Relevance/Strength). Extraction table is upstream of all interpretation -- two distinct steps with different mandates. |
| V-02 | **PASS** | Archivist Section (table, no interpretation columns by schema) precedes Analyst Section (row-reference analysis blocks only). Named section boundary enforces order. |
| V-03 | **FAIL** | Phase B source blocks combine Excerpt + Relevance + Strength + FC addressed in the same block, written simultaneously per source. In-block ordering. FM-12 active. Intentional single-axis design. |
| V-04 | **PASS** | Phase 2 Archivist (extraction, schema-enforced) precedes Phase 4 Analyst (interpretation, row-reference only). Phase boundary enforces order. |
| V-05 | **PASS** | Phase 2 Archivist mandate: "Verbatim excerpts only. No analysis. No relevance judgments. No strength labels." Phase 4 Analyst mandate: "Reference rows by number. Do not re-read source files. Do not introduce new sources." Dual mandate enforcement. |

#### C-13 -- Falsification ledger is a first-class named artifact

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 6 Falsification Ledger: named table with FC/Criterion/Source(s)/Status. `uncovered` is valid terminal status. |
| V-02 | **PASS** | B3 Falsification Ledger: named table, every FC with sources and status. |
| V-03 | **PASS** | Three named ledger artifacts: DRAFT (Phase A exit), IN-PROGRESS (Phase B exit), FINAL (Phase D exit). |
| V-04 | **PASS** | Three named ledger states: DRAFT (Phase 1), IN-PROGRESS (Phase 2 exit), FINAL (Phase 5). |
| V-05 | **PASS** | Three named ledger states with explicit traceability checks: covered-in-PROGRESS-but-inconclusive-in-FINAL vs. open-in-PROGRESS-and-uncovered-in-FINAL. |

#### C-14 -- Insider gate enforced by blocking WARNING text, not by count field

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Verbatim WARNING: INSIDER GATE NOT MET + "STOP. Do not proceed to Step 6. Do not write a verdict. Do not write synthesis." Three explicit prohibitions. |
| V-02 | **PASS** | Verbatim WARNING: INSIDER GATE NOT MET + "STOP. Do not proceed to B2. Do not begin source analysis or synthesis." |
| V-03 | **PASS** | Verbatim WARNING: INSIDER GATE NOT MET block present. Advisory phrasing fails C-19 but WARNING block satisfies C-14 (C-14 requires blocking text to exist; C-19 requires halt-form phrasing). |
| V-04 | **PASS** | Verbatim WARNING: INSIDER GATE NOT MET block present. Advisory phrasing is the intentional C-19 miss -- C-14 satisfied by the WARNING block. |
| V-05 | **PASS** | Verbatim WARNING: INSIDER GATE NOT MET + "STOP. Do not proceed to Phase 4 (Analyst). Do not begin interpretation. Do not write synthesis, contradiction checks, or follow-up queries." |

#### C-15 -- Structural separation implemented with named roles or phases, not in-block ordering

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | Step 4 Source N blocks co-locate Excerpt + Relevance + Strength + FC in the same block. Steps 1-9 are numbered sequences, not named roles or phases. In-block ordering at source level. FM-12 active. |
| V-02 | **PASS** | Named sections: Archivist Section / Analyst Section. Archivist Evidence Table schema excludes Relevance/Strength by contract. Analyst B2 blocks reference rows by number; no excerpt re-extraction. Schema exclusion makes in-block ordering structurally impossible. |
| V-03 | **FAIL** | Named phases (Phase A/B/C/D) exist, but Phase B source blocks combine Excerpt + Relevance + Strength + FC addressed in the same block. Named phases at document level do not prevent in-block ordering at source block level. FM-12 active. |
| V-04 | **PASS** | Named phases "Phase 2: Archivist (Extraction)" and "Phase 4: Analyst (Interpretation)". Phase 2 table: six columns, no interpretation fields by schema. Phase 4 blocks reference rows by number; no re-extraction. |
| V-05 | **PASS** | Same as V-04 plus: schema mandate explicitly prohibits interpretation phrases ("Do not write 'this suggests', 'this supports', 'this indicates', 'this demonstrates'") in the Archivist Evidence Table. Named phases + schema vocabulary prohibition = dual enforcement. |

#### C-16 -- Falsification ledger exists in multiple lifecycle states tied to phase exits

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | Single ledger state: Step 6 only, written at synthesis. No pre-search DRAFT. No IN-PROGRESS at search completion. Uncovered FCs visible only after verdict is framed. FM-13 active. |
| V-02 | **FAIL** | Single ledger state: B3 only, written in Analyst Section. No DRAFT, no IN-PROGRESS. FM-13 active. |
| V-03 | **PASS** | Three lifecycle states: DRAFT (Phase A exit, all FCs open), IN-PROGRESS (Phase B exit, search complete), FINAL (Phase D exit). Redirect Agenda generated from IN-PROGRESS gaps before gate fires. |
| V-04 | **PASS** | Three lifecycle states: DRAFT (Phase 1 exit), IN-PROGRESS (Phase 2 exit -- emitted as step 2-E2 before gate), FINAL (Phase 5 exit). IN-PROGRESS + Redirect Agenda required before Phase 3 begins. |
| V-05 | **PASS** | Three lifecycle states with four-step Phase 2 exit: 2-E1 (schema clean), 2-E2 (IN-PROGRESS), 2-E3 (Redirect Agenda), 2-E4 (execute/decline). Schema clean confirmed before IN-PROGRESS is emitted. |

#### C-17 -- Extraction table schema physically excludes interpretation columns

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | No schema contract. No Permitted/Prohibited column declaration. Step 3 table has four columns by convention, not named contract. |
| V-02 | **PASS** | "Archivist Evidence Table -- Schema Contract" declared in A3 before table population: Permitted columns listed; Prohibited columns listed (Relevance, Strength, Verdict, Analysis, Confidence, Assessment, Quality); enforcement rationale stated. A5 Schema Verification checks for violations before Analyst Section. |
| V-03 | **FAIL** | No schema contract. Phase B source blocks include Relevance and Strength by design -- schema exclusion not attempted (single-axis for C-18). |
| V-04 | **PASS** | Schema Contract declared in Phase 2 opening before any rows: Permitted/Prohibited column lists; enforcement statement ("remove it before Phase 3 begins"); rationale ("interpretation fields belong to Phase 4"). Schema Verification (Phase 2 exit check) verifies before IN-PROGRESS emission. |
| V-05 | **PASS** | Same as V-04 plus: Insider? annotated as factual field ("does this file exist only inside the repo, inaccessible via public web search or public documentation? yes / no. It is not an interpretation field.") -- grounds schema boundary semantically rather than by designation only. |

#### C-18 -- IN-PROGRESS falsification ledger surfaced before insider gate fires

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | Gate (Step 5) precedes ledger (Step 6). No pre-gate IN-PROGRESS state. No Redirect Agenda. Coverage gaps visible only after gate has already fired. |
| V-02 | **FAIL** | Gate (B1) precedes ledger (B3). No IN-PROGRESS state. No Redirect Agenda. |
| V-03 | **PASS** | Phase B exit: emit IN-PROGRESS ledger, then emit Redirect Agenda (each open FC generates one specific FC-targeted re-search action), then execute/decline. Phase C gate shows "Open FCs at gate (from IN-PROGRESS)" and "Redirect items pending". Gate fires against ledger state, not bare count. |
| V-04 | **PASS** | Phase 2 exit steps 2-E2 (IN-PROGRESS), 2-E3 (Redirect Agenda), 2-E4 (execute/decline). "The IN-PROGRESS ledger and Redirect Agenda must be visible before Phase 3 begins. Phase 3 fires against this state." Phase 3 gate shows Open FCs at gate from IN-PROGRESS. |
| V-05 | **PASS** | Same as V-04 plus step 2-E1 confirms Schema Verification = CLEAN before IN-PROGRESS is emitted. Four-step sequence (CLEAN -> IN-PROGRESS -> Redirect Agenda -> execute) makes IN-PROGRESS a guaranteed output of schema-verified extraction. |

#### C-19 -- Insider gate uses halt semantics, not advisory semantics

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | "STOP." is the leading halt token. Named prohibitions: "Do not proceed to Step 6. Do not write a verdict. Do not write synthesis." Meta-commentary in skill text: "Advisory phrasing... permits implicit continuation after a nominal attempt. Halt semantics require explicit resolution: one of Option A or Option B below must be selected and executed before the artifact continues. Proceeding to Step 6 without completing one of these options is a protocol violation." |
| V-02 | **PASS** | "STOP. Do not proceed to B2. Do not begin source analysis or synthesis." Named halt token + named prohibited next section. |
| V-03 | **FAIL** | "Before proceeding to Phase D synthesis, return to Phase B and re-search..." Advisory phrasing. No STOP. halt token. FM-16 active. Intentional single-axis miss. |
| V-04 | **FAIL** | "Before proceeding to Phase 4 (Analyst), return to Phase 2 and re-search specifically for internal-only artifacts..." Advisory phrasing. No STOP. halt token. Intentional miss to isolate V-05 as C-19 differentiator. FM-16 active. |
| V-05 | **PASS** | "STOP. Do not proceed to Phase 4 (Analyst). Do not begin interpretation. Do not write synthesis, contradiction checks, or follow-up queries." Halt token + four explicit prohibitions. Option A / Option B resolution contract: "There is no implicit continuation path. Proceeding without completing Option A or Option B is a protocol violation." |

---

## Composite Scores

| Variation | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | Asp Pass | Asp Pts | Composite | All Essential? |
|-----------|------|------|------|------|------|------|------|------|------|------|------|----------|---------|-----------|---------------|
| V-01 | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | FAIL | FAIL | FAIL | PASS | 7/11 | 6.36 | **96.4** | YES |
| V-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | FAIL | PASS | 9/11 | 8.18 | **98.2** | YES |
| V-03 | PASS | PASS | PASS | FAIL | PASS | PASS | FAIL | PASS | FAIL | PASS | FAIL | 7/11 | 6.36 | **96.4** | YES |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | 10/11 | 9.09 | **99.1** | YES |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 11/11 | 10.0 | **100** | YES |

**Golden threshold** (all essential pass + composite >= 80): all five pass. Floor 96.4 under the new /11 denominator.

---

## Ranking

| Rank | Variation | Composite | Notes |
|------|-----------|-----------|-------|
| 1 | V-05 | 100 | All 11 aspirationals. V-04 base + halt semantics with Option A/B contract. Schema-clean as prerequisite to IN-PROGRESS emission is the structural addition. |
| 2 | V-04 | 99.1 | 10/11 -- C-19 only miss (advisory phrasing, intentional). C-17 + C-18 together cover 9 of 11 aspirationals. |
| 3 | V-02 | 98.2 | 9/11 -- C-16 and C-18 miss (single ledger state). Strongest C-17 mechanism: Schema Contract as named section before table population. |
| 4 (tie) | V-01 | 96.4 | 7/11 -- C-15, C-16, C-17, C-18 miss. Strongest C-19 meta-commentary: explicitly names advisory/halt distinction in skill text. |
| 4 (tie) | V-03 | 96.4 | 7/11 -- C-12, C-15, C-17, C-19 miss. Only variation to pass C-18 without C-17. Redirect Agenda as first-class named artifact is the R4 increment for C-18. |

---

## Excellence Signals from V-05

### 1. Option contract closes the implicit continuation path

V-01 named the advisory/halt distinction in the skill text. V-05 closes it by requiring explicit selection of Option A or Option B. The meta-statement "There is no implicit continuation path. Proceeding without completing Option A or Option B is a protocol violation" names the bypass as a violation. Option A requires updating the gate count to >= 1 (nominal re-search that finds nothing does not satisfy it). Option B requires the exact reclassification text and labeled section headers. Neither allows continuation without a named, verifiable action. Contrast V-04's advisory: a model can perform one search attempt and proceed.

### 2. Schema clean as prerequisite to IN-PROGRESS emission

V-05's four-step Phase 2 exit: 2-E1 (confirm schema = CLEAN) -> 2-E2 (emit IN-PROGRESS) -> 2-E3 (Redirect Agenda) -> 2-E4 (execute/decline). V-04 has the same steps but does not make CLEAN an explicit prerequisite to ledger emission. If schema check fires after IN-PROGRESS is emitted, the Redirect Agenda could be derived from contaminated rows. V-05 makes this dependency structurally explicit: the IN-PROGRESS ledger reflects schema-verified extraction by construction.

### 3. Insider? declared as factual, not interpretive, in schema rationale

V-05 annotates the Insider? column: "does this file exist only inside the repo, inaccessible via public web search or public documentation? yes / no. It is not an interpretation field." This semantic distinction (factual: exists/doesn't exist in repo vs. interpretive: what it means) grounds why Insider? belongs in extraction alongside Path and Verbatim Excerpt, while Relevance and Strength belong in Phase 4. Prior variations asserted the schema boundary by designation (permitted/prohibited); V-05 grounds it semantically, making it harder to rationalize moving Insider? to the analysis section.

---

## What Changed V-04 to V-05 (the C-19 increment)

V-04 failed only C-19. V-05 adds three things:

1. **Halt token + prohibition chain**: "STOP. Do not proceed to Phase 4 (Analyst). Do not begin interpretation. Do not write synthesis, contradiction checks, or follow-up queries." -- four explicit prohibitions name every Phase 4 entry point.

2. **Option A/B resolution contract with verifiable completion**: Option A requires Insider count >= 1 after re-search and explicitly updating the gate to PASS. Option B requires the exact reclassification text and labeled section headers. Both have completion conditions that can be verified by inspection.

3. **Named protocol violation**: "There is no implicit continuation path. Proceeding without completing Option A or Option B is a protocol violation." The bypass is named, not merely discouraged.

---

## Failure Mode Summary (R4)

| FM | Criterion | Affected Variations | Notes |
|----|-----------|---------------------|-------|
| FM-12 (in-block ordering) | C-15 | V-01, V-03 | V-01: Step 4 blocks co-locate Excerpt + Relevance + Strength. V-03: Phase B blocks co-locate extraction and interpretation. Named steps/phases at document level do not prevent in-block ordering at source block level. |
| FM-13 (single-state ledger) | C-16 | V-01, V-02 | Both produce accurate final ledgers in a single pass at synthesis. Uncovered FCs visible only after verdict is framed. |
| FM-14 (no schema contract) | C-17 | V-01, V-03 | No Permitted/Prohibited column declaration. Column constraints are conventions, not named contracts verifiable against a declared schema. |
| FM-15 (no pre-gate IN-PROGRESS) | C-18 | V-01, V-02 | Gate fires before any ledger state is visible (V-01 gate in Step 5, ledger in Step 6). Coverage gaps not visible at redirect decision point. |
| FM-16 (advisory gate phrasing) | C-19 | V-03, V-04 | "Before proceeding to [Phase N]..." -- advisory form. FM-16 active in V-03 by single-axis design; active in V-04 by intentional isolation to make V-05 the C-19 differentiator. |

---

## New Patterns

Two patterns from V-05 not yet captured as rubric criteria:

1. **option-contract-as-halt-resolution-enforcement** -- Naming exactly two valid resolution exits (Option A: re-search must produce Insider count >= 1 to update gate to PASS; Option B: explicit reclassification text + labeled headers) and declaring "there is no implicit continuation path" converts the halt from an instruction into a protocol with named violation conditions. A model that proceeds after nominal re-search has violated Option A by name, not just ignored an instruction.

2. **schema-clean-prerequisite-to-in-progress-emission** -- Sequencing Phase 2 exit as CLEAN-confirm -> IN-PROGRESS -> Redirect Agenda makes the ledger structurally guaranteed to reflect schema-verified extraction. If the schema was contaminated, the exit sequence blocks IN-PROGRESS emission until the violation is corrected. The Redirect Agenda cannot be derived from rows that leaked interpretation columns.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["option-contract-as-halt-resolution-enforcement", "schema-clean-prerequisite-to-in-progress-emission"]}
```
