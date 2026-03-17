I have all five variations fully read. Now scoring.

---

## Flow-Trigger — Round 4 Scorecard (Rubric v2)

**Rubric**: C-01 through C-13 | **Date**: 2026-03-16
**Pre-score note**: R4 was explicitly designed to close R3 V-05's C-03 gap (missing `Reads:` / `Produces:` / `Writes:` template) and to combine mechanisms from R3's four 100-scoring variations. Starting hypothesis: all five score 100.

---

### Scoring Formula Recap

```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)
Golden threshold: all essential pass AND composite >= 80
```

---

## V-01 — Role Sequence: Authority Contracts

**Axis**: Role sequence + explicit prohibitions per role (mandate + prohibition pairs)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Trigger enumeration | **PASS** | Role B mandate: "a numbered entry for every R-ID in Role A's manifest — whether it fires or not." GATE B checks F + NF = N; unresolved R-IDs are named. Zero silent omissions structurally enforced. |
| C-02 | Execution order stated | **PASS** | Role B specifies: sync plugin steps by pipeline stage → rank; real-time workflows at same stage; async after all sync; business rules at pre-validation. "Within a tier, state the ordering rationale explicitly." |
| C-03 | Inputs and outputs | **PASS** | Firing entry format contains explicit `Reads:`, `Produces:`, `Writes:` labeled slots with examples. Format is mandatory per Role B mandate. No prose substitution permitted. |
| C-04 | Three anomaly verdicts | **PASS** | Role C mandate: "produce exactly three anomaly verdict blocks." GATE C fails if any verdict block is absent or lacks row citations. All three classes named in anomaly definitions. |
| C-05 | Platform grounding | **PASS** | Vocabulary Contract table at top; `[NC: {term used}]` violation markers. Role C inherits the contract governing all trigger-type claims. |
| C-06 | Circular trigger analysis | **PASS** | Role C: "Build the directed edge set: for each firing entry, create an edge to each entry in its Cascades-to field. Determine whether any path contains a back-edge." Graph traversal required. |
| C-07 | Conditional branch paths | **PASS** | Firing entry: `Condition (EXECUTED)` + `Condition (SKIPPED would be)` both required. Gap entry: `Condition (SKIPPED)` + `Condition (WOULD FIRE if)` both required. Both branches structural. |
| C-08 | Anomaly remediation | **PASS** | Verdict block format: `Remediation: {if DETECTED: one named, actionable fix — debounce, registration, cycle-break...}`. Remediation field present for all three verdict blocks. |
| C-09 | Execution tier + latency | **PASS** | Firing entry: `Execution tier: sync \| async \| scheduled` + `Latency: Inline (sync, blocks transaction) OR ~{N} min [{standard \| premium} connector] (async)`. Both slots required in format. |
| C-10 | Cascade completeness | **PASS** | Firing entry: `Cascades-to: {Entry #{N} name, if a Writes field matches another candidate's trigger condition} \| None`. Cascade children exist as manifest candidates (Role A scans all layers), so they appear as their own numbered entries in Role B. |
| C-11 | Denominator declared | **PASS** | Role A output ends with `DENOMINATOR: N = {count} candidates identified.` and `[GATE A: PASSED — N candidates declared, denominator set before enumeration]`. Pre-enumeration by structural placement. |
| C-12 | Gap tokens for non-firing | **PASS** | Gap entry format: `### Entry {#}: [NOT FIRED — {Candidate Name}] [R-ID: R-{NN}]` with reason + skipped + would-fire fields. ENUMERATION CLOSE reconciliation (F + NF = N) names any unresolved R-IDs. |
| C-13 | Verdict evidence citation | **PASS** | Role C mandate: "Each verdict block must cite specific Entry numbers from Role B." Verdict block format: `Rows inspected: Entry {#} through Entry {#}`. GATE C fails explicitly on missing row citations. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/5
**Composite**: (5/5 × 60) + (3/3 × 30) + (5/5 × 10) = **100**
**All essential pass**: YES

**Excellence signal**: The prohibition mechanism is R4 V-01's structural innovation over R3. R3 V-01 had mandates ("your only output is..."); R4 adds explicit SHALL NOT statements. A prohibited action in a role's output is labeled a *structural violation of the authority contract* — this makes scope creep detectable from the output text rather than requiring scorer inference. Role A's prohibition on condition evaluation makes C-11 undecidable by scope alone: Role A literally cannot produce a firing classification even if it wanted to.

---

## V-02 — Output Format: Full Audit Ledger with Gate-per-Column

**Axis**: Output format — column fill IS the gate check

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Trigger enumeration | **PASS** | Pass 1 allocates all candidates as numbered rows; Pass 2 must produce exactly one entry per row. GATE 1: F + NF = N; unresolved rows named in failure token. |
| C-02 | Execution order stated | **PASS** | Pass 2: "Walk Pass 1 rows in execution order: sync rows first (by pipeline stage, then rank), then async rows (by platform scheduling)." |
| C-03 | Inputs and outputs | **PASS** | Required firing entry columns: `Reads: {Entity}.{Field} = {value}` ("at least one specific field — no 'reads record fields'"), `Produces: {connector — verb — target — state}` ("no 'sends email'"), `Writes: {Entity}.{Field} = {value} \| none` ("not blank"). Column requirements are structural contracts. |
| C-04 | Three anomaly verdicts | **PASS** | Anomaly Verdicts section: "Produce three verdict blocks, one per class." GATE 2 checks all three are present and carry row citations. Templates for all three classes defined. |
| C-05 | Platform grounding | **PASS** | Platform Term Contract: approved terms table + execution tier mapping. `[NC: {term used}]` violation markers apply throughout. |
| C-06 | Circular trigger analysis | **PASS** | Circular Dependency verdict block: `Evidence: directed edge set: Row-NN → Row-MM for each Cascades-to reference` + `Finding: back-edge identified or confirmed absent`. |
| C-07 | Conditional branch paths | **PASS** | Required firing entry columns include both `Condition (EXECUTED): {filter — matched value}` and `Condition (SKIPPED would be): {filter — non-matching condition}`. Gap entry includes `Condition (SKIPPED)` + `Condition (WOULD FIRE if)`. |
| C-08 | Anomaly remediation | **PASS** | Verdict blocks: `Remediation: {named fix if DETECTED; "none required" if NOT DETECTED}`. All three blocks carry this field. |
| C-09 | Execution tier + latency | **PASS** | Required firing entry columns: `Tier: sync \| async \| scheduled` ("Approved term — no other value") + `Latency: Inline \| ~N min [tier]` ("Timing annotation — not blank"). |
| C-10 | Cascade completeness | **PASS** | Required column: `Cascades-to: Row {#}: {name} \| None` ("Row reference if Writes field matches another row's trigger"). Pass 1 allocates all candidates including cascade children; Pass 2 links via row reference. |
| C-11 | Denominator declared | **PASS** | Pass 1 ends with: `DENOMINATOR: {N} rows allocated.` followed by `[GATE 0: PASSED — denominator declared before any condition evaluation]`. Pass 2 cannot begin until Gate 0 is passed. |
| C-12 | Gap tokens for non-firing | **PASS** | Required gap entry columns: `Status: NOT FIRED` (literal). The ledger's `Status` column is a required slot — empty or incorrect value is a visible structural gap without a separate token scan. |
| C-13 | Verdict evidence citation | **PASS** | Each verdict block: `Rows examined: {Row # through Row #}` as required field. GATE 2 explicitly checks "Missing row citations: {list}". |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/5
**Composite**: (5/5 × 60) + (3/3 × 30) + (5/5 × 10) = **100**
**All essential pass**: YES

**Excellence signal**: V-02's structural innovation is the collapse of gate token and column requirement into the same slot. In V-01 and V-04, gate tokens are separate lines in the output that explicitly pass/fail. In V-02, an empty `Reads:` column IS the gate failure — no separate token is needed to surface it. This reduces the compliance surface: a scorer scanning the ledger sees the gap directly in the data layer, not in a separate audit overlay.

---

## V-03 — Phrasing Register: Unified FM + Gate Token System

**Axis**: FM codes and gate tokens collapsed into a single `[FM-NN: CLEAR | VIOLATED]` token system

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Trigger enumeration | **PASS** | Section 2: "No candidate may be skipped." FM-02 (Silent Omission) reconciliation check: `[FM-02: CLEAR — F + NF = N]` or `[FM-02: VIOLATED — missing: {list}]`. |
| C-02 | Execution order stated | **PASS** | Section 2: "Walk candidates in execution order: sync entries first by pipeline stage and rank, then async." FM-04 (Order Inversion) in failure mode table detects violations. |
| C-03 | Inputs and outputs | **PASS** | Firing entry template: `Reads:`, `Produces:`, `Writes:` each carry `[FM-03 check]` markers. FM-03 (Payload Vacancy) is the named failure mode for missing payload fields. |
| C-04 | Three anomaly verdicts | **PASS** | Section 3 requires exactly three verdict blocks. `[FM-07: CLEAR — all three verdict blocks present]` or `[FM-07: VIOLATED — missing: {list}]`. Verdict Audit block explicitly summarizes FM-07 + FM-08 coverage. |
| C-05 | Platform grounding | **PASS** | Section 0: platform named, vocabulary contract set, FM-12 (Vocabulary Violation) defined. `[NC: {term used}]` markers for violations. |
| C-06 | Circular trigger analysis | **PASS** | Circular Dependency verdict block: `Directed edge set: {entry # → entry # for each Cascades-to reference}` with `[FM-13: CLEAR if shown]`. FM-13 (Circular Detection Absent) is the failure mode. |
| C-07 | Conditional branch paths | **PASS** | Firing entry: `Condition (EXECUTED)` with `[FM-05: CLEAR if present]`; `Condition (SKIPPED would be)` with `[FM-05: VIOLATED if absent]`. Gap entry: FM-06 markers on both branch fields. |
| C-08 | Anomaly remediation | **PASS** | Verdict blocks: `Remediation:` with `[FM-09: CLEAR if fix present when DETECTED]`. FM-09 (Remediation Gap) defined as: "Verdict is DETECTED but Remediation field is empty." |
| C-09 | Execution tier + latency | **PASS** | Firing entry: `Tier:` + `Latency:` fields with `[FM-10: CLEAR if filled]`. FM-10 (Latency Blind) defined as: "Tier field blank or reads 'async' without any latency window specified." |
| C-10 | Cascade completeness | **PASS** | Firing entry: `Cascades-to:` with `[FM-11 check — non-empty Writes must evaluate downstream]`. FM-11 (Cascade Truncation) defined as: "Cascades-to reads 'None' when a matching candidate is in the candidate list." |
| C-11 | Denominator declared | **PASS** | Section 1 ends with: `Candidate count: N = {count}.` followed by `[FM-01: CLEAR — N = {count} declared at row {last row number}, before Section 2 begins]`. FM-01 in Section 0 pre-announces the requirement. |
| C-12 | Gap tokens for non-firing | **PASS** | Gap entry template: `## {#}. [NOT FIRED — {Candidate Name}] [candidate #{N}]` with condition fields. FM-02 reconciliation check catches any silent omissions. |
| C-13 | Verdict evidence citation | **PASS** | Verdict blocks: `Rows inspected: {#} through {#}` with `[FM-08: CLEAR if row numbers present]`. FM-08 (Uncited Verdict) definition: "Rows inspected field is blank or reads 'all entries' without enumeration." |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/5
**Composite**: (5/5 × 60) + (3/3 × 30) + (5/5 × 10) = **100**
**All essential pass**: YES

**Excellence signal**: V-03's unification collapses two independent compliance systems (FM failure catalog + gate tokens) into a single token vocabulary. Any output from a model following V-03 is fully scannable by searching for the string `VIOLATED`. One scan, complete audit. No separate gate-line check needed. FM-00 (Protocol Skip) as a meta-defect is a structural addition: it makes the act of skipping the protocol itself a named, detectable violation — not just a silent absence.

---

## V-04 — Role Sequence + Lifecycle: Phase-Artifact Pipeline

**Axis**: Four phases each produce a named artifact; compliance is verifiable from artifact presence

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Trigger enumeration | **PASS** | Phase 2 mandate: "a numbered entry for every Manifest-ID, in execution order." PHASE 2 GATE: F + NF = N; unresolved M-IDs listed in failure token. Phase 3 cannot begin until Phase 2 gate passes. |
| C-02 | Execution order stated | **PASS** | Phase 2: sync by pipeline stage → rank; real-time workflows at their registered stage; async after all sync; business rules at pre-validation. Ordering must be stated explicitly. |
| C-03 | Inputs and outputs | **PASS** | Phase 2 firing entry format: explicit `Reads:`, `Produces:`, `Writes:` labeled slots with annotation requirements. Phase 2 prohibition prevents prose substitution. |
| C-04 | Three anomaly verdicts | **PASS** | Phase 4 mandate: "Produce the Verdict Bundle — three verdict blocks, one per anomaly class." PHASE 4 GATE fails if any verdict block is absent or lacks row citations or Phase 3 references. |
| C-05 | Platform grounding | **PASS** | Vocabulary Contract governs all four phases. `[NC: {term used}]` markers for violations anywhere in output. Platform named before Phase 1 begins. |
| C-06 | Circular trigger analysis | **PASS** | Phase 3 Analysis C: directed edge set, traversal log, back-edge detection — explicit and structured. Phase 4 verdict cites "Analysis C, findings: {summary}". Strongest graph analysis structure among all five variations. |
| C-07 | Conditional branch paths | **PASS** | Phase 2 firing entry: `Condition (EXECUTED):` + `Condition (SKIPPED...):` both required. Gap entry: `Condition (SKIPPED):` + `Condition (WOULD FIRE):` both required. |
| C-08 | Anomaly remediation | **PASS** | Phase 4 verdict format: `Remediation: {if DETECTED: one named, actionable fix}`. Phase 3 prohibition explicitly bars remediation from appearing there — remediation is structurally quarantined to Phase 4. |
| C-09 | Execution tier + latency | **PASS** | Phase 2 firing entry: `Execution tier: sync \| async \| scheduled` + `Latency: Inline (sync, blocks transaction) \| ~{N} min [{standard\|premium}] (async)`. |
| C-10 | Cascade completeness | **PASS** | Phase 2 firing entry: `Cascades-to: Entry {#}: {name}, if Writes matches a Manifest trigger condition \| None`. Phase 3 Analysis C builds edge set from Cascades-to fields — cascade chains are traced to termination. |
| C-11 | Denominator declared | **PASS** | Phase 1 (Manifest artifact): `Denominator: N = {count} candidates.` PHASE 1 GATE verifies "N declared" before Phase 2 begins. Gate blocks Phase 2 if Manifest is incomplete. |
| C-12 | Gap tokens for non-firing | **PASS** | Phase 2 gap entry: `## Entry {#}: [NOT FIRED — {Candidate Name}] [M-{NN}]` with both condition fields. PHASE 2 GATE reconciliation names unresolved M-IDs. |
| C-13 | Verdict evidence citation | **PASS** | Phase 4 verdict format: `Ledger rows inspected: Entry {#} through Entry {#}` (mandatory) + `Phase 3 analysis cited: Analysis {A\|B\|C}, findings: {summary}`. PHASE 4 GATE checks for both "Missing row citations" and "Missing Phase 3 references." Dual citation requirement is the most demanding of any variation. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/5
**Composite**: (5/5 × 60) + (3/3 × 30) + (5/5 × 10) = **100**
**All essential pass**: YES

**Excellence signal**: V-04 introduces the only two-artifact evidence chain among all five variations. Phase 3 (Analysis Bundle) and Phase 4 (Verdict Bundle) are separate artifacts with separate roles and prohibitions. Phase 3 may not issue verdicts; Phase 4 may not perform original analysis. This structural separation makes the reasoning chain auditable independently of the verdict — a scorer can read Phase 3 and independently verify whether Phase 4's verdict follows. The Phase 3 prohibition on verdicts prevents analysis-verdict conflation, which is a common gap in informal trigger analysis. C-13 achieves its strongest form here: Phase 4 verdicts must cite both Ledger row ranges AND Phase 3 analysis references.

---

## V-05 — Inertia Framing + Format Blocks: Override Model

**Axis**: Inertia naming (describes default failure) + FORMAT BLOCK (shows required output shape) per override

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Trigger enumeration | **PASS** | Override 0 + Override 1 together enforce: pre-scan produces candidate list with denominator, then every non-firing candidate gets a gap token AT ITS SEQUENCE POSITION. RECONCILIATION section checks F + NF = N. |
| C-02 | Execution order stated | **PASS** | Explicit EXECUTION ORDER section: 6-step ordered list (business rules → sync plugin steps → real-time workflows → async plugin steps → background/automated flows → instant/scheduled flows). |
| C-03 | Inputs and outputs | **PASS** | Override 2 FORMAT BLOCK: `{#}. {Trigger Name}` with explicit `Reads:`, `Produces:`, `Writes:` slots. Each slot has specificity requirements (e.g., "at least one specific field — 'the record' does not count"). Directly closes R3 V-05's C-03 gap. |
| C-04 | Three anomaly verdicts | **PASS** | Override 5 FORMAT BLOCK: `Section 3 — Anomaly Verdicts` with all three verdict blocks (Storm, Missing Trigger, Circular Dependency). `Rows inspected:` field present in each. |
| C-05 | Platform grounding | **PASS** | Platform Setup section: platform named, approved terms listed, `[NC: {term used}]` for violations. |
| C-06 | Circular trigger analysis | **PASS** | Override 5 FORMAT BLOCK for Circular Dependency: `Directed edges: Entry #{#} → Entry #{#} [one per Cascades-to reference]; Entry #{#} → None [terminals]` + `Finding: back-edge found and path named \| confirmed absent`. |
| C-07 | Conditional branch paths | **PASS** | Override 3 explicitly requires "both the taken branch (EXECUTED or SKIPPED) and the opposite branch." References Override 2 FORMAT BLOCK (`Condition (EXECUTED)` + `Condition (SKIPPED would be)`) and Override 1 FORMAT BLOCK (gap entry both-branch fields). |
| C-08 | Anomaly remediation | **PASS** | Override 5 FORMAT BLOCK: `Remediation: {one named, actionable fix \| "none required"}` in each verdict block. |
| C-09 | Execution tier + latency | **PASS** | Override 6 explicitly addresses: execution tier, timing window for async (standard ~5–15 min, premium ~1–3 min), throttling/concurrency/24-hour re-trigger deferral. Override 2 FORMAT BLOCK includes `Execution tier:` and `Latency:` as labeled slots. |
| C-10 | Cascade completeness | **PASS** | Override 4: "When an entry's `Writes` field is non-empty, evaluate whether the written field matches any Section 0 candidate's trigger condition. If it does, add that candidate as the NEXT NUMBERED ENTRY in the sequence." Cascade insertion is explicitly mandated. |
| C-11 | Denominator declared | **PASS** | Override 0 FORMAT BLOCK: `Candidate count: N = {count}. ← SHALL appear here, before Section 1 begins.` Arrow annotation emphasizes pre-enumeration placement. |
| C-12 | Gap tokens for non-firing | **PASS** | Override 1 FORMAT BLOCK: `{#}. [NOT FIRED — {Candidate Name}] [candidate #{N} from Section 0]` with both condition fields. Override 1 narration: "insert a gap token AT THE CANDIDATE'S POSITION IN THE EXECUTION-ORDER SEQUENCE — not in a reconciliation table at the end." |
| C-13 | Verdict evidence citation | **PASS** | Override 5 FORMAT BLOCK: `Rows inspected: Entry {#} through Entry {#}` in each verdict block. Override 5 narration: "Clean verdicts cite the row range that was found clean. Positive findings cite the rows involved in the anomaly." |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/5
**Composite**: (5/5 × 60) + (3/3 × 30) + (5/5 × 10) = **100**
**All essential pass**: YES

**Excellence signal**: The format block mechanism is R4 V-05's structural contribution. R3 V-05 named defaults and described requirements — R4 V-05 shows the required output shape. The difference: a model reading "your firing entry must include explicit inputs and outputs" can still omit `Reads:` / `Produces:` by producing prose. A model reading an override FORMAT BLOCK that literally shows labeled slots cannot omit those slots without structurally diverging from the template. The format block converts a *descriptive* requirement into a *prescriptive* one. Override 4 also introduces the explicit mandate to insert cascade children "as the NEXT NUMBERED ENTRY in the sequence" — this is the clearest statement of C-10's cascade insertion requirement across all five variations.

**Minor structural note (not a gap)**: Override 5's FORMAT BLOCK instructs the model to open anomaly slots "before Section 1 (BEFORE any enumeration begins)" — but this instruction appears inside Override 5, which is read after Overrides 0–4. There is no separate pre-enumeration slot table in the protocol structure itself. Compare to V-01 (slots in Role B before Entry 1), V-02 (slots before Pass 2 rows), V-04 (slots before Phase 2 Entry 1). V-05 relies on the model honoring the instruction's timing claim rather than the protocol's structural placement. This does not produce a criterion failure but is the weakest pre-enumeration slot anchor among the five variations.

---

## Summary Scorecard

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | Score | All Ess. |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|---------|
| V-01 Authority Contracts | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** | YES |
| V-02 Gate-per-Column | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** | YES |
| V-03 FM+Gate Unified | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** | YES |
| V-04 Phase-Artifact | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** | YES |
| V-05 Override+Format | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** | YES |

**All five variations achieve the golden threshold (all essential pass, composite 100).**

---

## Round 4 Analysis

### Root Finding

R4's design goal was realized: all five mechanisms that were independent 100-scoring paths in R3 can be combined without creating new gaps, and the one gap variation (R3 V-05, C-03 partial at 94) is fully closed by the format block mechanism. R4 provides five independent structural strategies for achieving full rubric compliance, all at ceiling.

### Excellence Signals (R4 — New Over R3)

| Signal | Source | R3 Gap It Closes or Extends |
|--------|--------|----------------------------|
| **Named prohibitions as structural violations** | V-01 | R3 V-01 used mandates only. R4 adds SHALL NOT clauses where prohibited content appearing in output is a named structural violation — scope creep is detectable, not inferred. |
| **Columnar gate-per-slot** | V-02 | R3 kept ledger format and gate tokens as separate mechanisms. R4 collapses them: empty required column = visible structural gap, no secondary gate token scan needed. |
| **FM-gate token unification** | V-03 | R3 V-03 FM codes were catalog references; R3 V-04 gate tokens were checkpoint markers. R4 unifies into `[FM-NN: CLEAR\|VIOLATED]` — one string pattern surfaces all compliance failures. |
| **Analysis-verdict artifact separation** | V-04 | R3 V-04 had phases but no named artifacts. R4 makes Phase 3 (Analysis Bundle) and Phase 4 (Verdict Bundle) independent artifacts with independent prohibitions — C-13's dual citation requirement (row range + Phase 3 reference) is the strongest evidence chain achieved by any variation across all rounds. |
| **Format block as structural contract** | V-05 | R3 V-05 described requirements; R4 shows them. FORMAT BLOCK converts a descriptive requirement into a prescriptive template that a model cannot deviate from without a visible structural departure. |

### Top Variation

**V-04** for novel structural depth: the Phase 3 / Phase 4 separation is the only mechanism across all four rounds that creates a citable intermediate evidence artifact. Every other variation goes directly from enumeration to verdict; V-04 inserts an analysis step whose output is independently reviewable. The dual-citation requirement in C-13 (Ledger row range + Phase 3 analysis reference) is the most demanding compliance assertion in R4. If C-13 is the hardest criterion for a model to satisfy, V-04 enforces it most completely.

**V-01** ranks second for the prohibition mechanism — the most structurally durable way to enforce role boundaries discovered across all four rounds.

### Round Conclusion

R4 confirms that all five structural strategies from R3 generalize to combinations without regression. The rubric v2 ceiling has been reached by all five independent paths. Future rounds should either (a) raise the rubric ceiling with new criteria, or (b) test adversarial scenarios where the scenario contains deliberate anomalies (storm, cycle, missing trigger) to verify that the 100-scoring variations also produce correct anomaly verdicts, not just structurally correct output forms.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named prohibitions as structural violations: adding SHALL NOT clauses to each role makes scope creep detectable from output content rather than inferred from absence — prohibited content appearing in a role's output is a named structural violation, not an instruction miss", "Analysis-verdict artifact separation: Phase 3 Analysis Bundle and Phase 4 Verdict Bundle are independent named artifacts with independent prohibitions, creating a citable evidence chain where verdicts must reference prior analysis — the strongest C-13 enforcement achieved across all rounds", "Format blocks as structural contracts: showing the required output shape in each override section converts a descriptive requirement into a prescriptive template a model cannot deviate from without a visible structural departure — closes the R3 gap where inertia naming described requirements without enforcing output form"]}
```
