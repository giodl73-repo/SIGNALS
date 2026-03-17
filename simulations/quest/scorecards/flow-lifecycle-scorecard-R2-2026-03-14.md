I have all the data needed. Now I'll write the R2 scorecard.

---

## Round 2 Scorecard — flow-lifecycle

### Rubric v2 Scoring Key

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

Essential: C-01–C-05 (60 pts) | Recommended: C-06–C-08 (30 pts) | Aspirational: C-09–C-14 (10 pts)

Golden threshold: all 5 essential pass AND composite >= 80.

---

### V-01: Output Format Fixed — Flat Table + Decision Supplement Catalog + Role Registry Gate

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | `Entry Condition` and `Exits` columns enforce labeling on every row; exits format `[cond] -> S-[ID]` or `TERMINAL:[name]` makes undeclared exits structurally impossible |
| C-02 | Exception Flow Identification | PASS | Pre-printed 3-row EXCEPTION FLOWS table; `Phase/State Origin` column + `Trigger Condition` + `Trace` + `Handling (R-ID)` + `Terminal` columns; "no generic system error" instruction enforces specificity |
| C-03 | Role Assignment Accuracy | PASS | ROLE REGISTRY table with R-ID/Role Name/Domain/Decision Authority/Anti-Generic Check precedes STATE TRANSITIONS; registry gate checklist; Owner column enforces R-ID (not free-text name) at every state |
| C-04 | Bottleneck and Gap Identification | PASS | BOTTLENECKS table with Cause/Downstream Impact/Owner (R-ID); MISSING: label in gap table with Rationale column and Would-Own (R-ID) |
| C-05 | Terminal State Completeness | PASS | TERMINAL STATES section declared before table; terminal rows use `--` in Owner/Exits; exit format enforces `TERMINAL:[name]` reference |
| C-06 | Parallel Path Modeling | PASS | Pre-printed PARALLEL PATHS section with Fork/branch/Join/Join-type/Join-condition fields; "No parallel paths. Rationale: [why]" fallback prevents silent omission |
| C-07 | Edge Case Enumeration | PASS | Pre-printed 3-row EDGE CASES table; "Must not duplicate any named exception trace" instruction cross-references E-IDs |
| C-08 | Decision Point Explicitness | PASS | DECISION SUPPLEMENT CATALOG requires one block per DECISION-type state; block fields: Condition evaluated/Owner/Branch YES/Branch NO/Fallback:; "Do not write n/a for Fallback:" closes exhaustive-outcome gap that failed R1 V-01 |
| C-09 | Cross-Process Interaction Modeling | PASS | CROSS-PROCESS INTERACTIONS table: Sending State/Receiving Process/Data Payload/Expected Acknowledgment/Handoff Owner (R-ID) |
| C-10 | SLA and Timing Analysis | PASS | SLA ANALYSIS table with At-Risk? and `Bottleneck Cross-Ref` columns; AT-RISK NOTE instruction requires "causal source: B-[ID]" below each at-risk row |
| C-11 | Decision Supplement Block Structure | PASS | DECISION SUPPLEMENT CATALOG provides dedicated named block per DECISION state with explicit `Fallback:` field; catalog must be complete before EXCEPTION FLOWS; "Do not write n/a" enforces non-trivial fallback |
| C-12 | Role Registry Gate | PASS | ROLE REGISTRY with R-ID/Domain/Anti-Generic Check columns precedes STATE TRANSITIONS; three-item registry gate checklist explicitly gates entry to state tracing |
| C-13 | Phase-Scoped Exception Traces | PASS | `Phase/State Origin` column in EXCEPTION FLOWS table: each row carries `S-[ID]: [state name]` anchor; explicit per-trace labeling meets pass condition |
| C-14 | SLA-to-Bottleneck Evidence Chain | PASS | `Bottleneck Cross-Ref` column in SLA ANALYSIS; AT-RISK NOTE below each at-risk row requires B-[ID] citation; one-directional chain (SLA→B) |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/6

```
composite = (5/5 * 60) + (3/3 * 30) + (6/6 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

C-08 failure from R1 is fully closed. DECISION SUPPLEMENT CATALOG is the structural fix: dedicated block with `Fallback:` required field eliminates the exhaustive-outcome gap that the DECISION type column left open. C-13 passes via column (Phase/State Origin) rather than structural exception-first ordering — lowest structural reliability within the 100 cluster on this criterion. C-14 is one-directional only.

---

### V-02: Phrasing Register — Conversational-Imperative Questions

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | Each state answered as a question block with labeled sub-fields `Entry condition:` and `Exits:`; blank labeled answer is as visible as a blank table cell in structured question format |
| C-02 | Exception Flow Identification | PASS | 3 exception answer blocks required; each block has `Phase origin:` sub-field, `Trigger:`, `Trace:`, `Handling role (R-ID):`, `Terminal:`; question format forces constructed answer rather than cell fill; predicted highest content specificity |
| C-03 | Role Assignment Accuracy | PASS | Step 2 prohibition-question gate: domain-specific role listing with "not 'Approver'/'Manager' — fix before continuing"; Step 5 confirm gate occurs before state tracing begins; Q2 in each decision block requires R-ID owner |
| C-04 | Bottleneck and Gap Identification | PASS | Bottleneck question blocks with `Cause:`, `Downstream impact:`, `Owner (R-ID):`; gap question block with MISSING: label and `Rationale:` sub-field |
| C-05 | Terminal State Completeness | PASS | Terminal states declared in first question before any state walkthrough; exception trace answer blocks require terminal label |
| C-06 | Parallel Path Modeling | PASS | Parallel paths question section with Fork/branch/Join/type/condition sub-fields |
| C-07 | Edge Case Enumeration | PASS | 3 EC question blocks with `Why problematic:` and `Correct response:` sub-fields; "must not duplicate any E-ID" instruction |
| C-08 | Decision Point Explicitness | PASS | Step 7: 5-question block per DECISION state; Q1=condition evaluated, Q2=owner role (R-ID), Q3=Branch YES, Q4=Branch NO, Q5=FALLBACK (mandatory, no skip) |
| C-09 | Cross-Process Interaction Modeling | PASS | Cross-process question block with `Sending state:`, `Receiving process:`, `Data payload:`, `Expected acknowledgment:`, `Handoff owner (R-ID):` sub-fields |
| C-10 | SLA and Timing Analysis | PASS | SLA annotation question block; AT-RISK citation requirement: "If AT-RISK: cite B-ID — required" enforces B-ID linkage per at-risk answer |
| C-11 | Decision Supplement Block Structure | PASS | Step 7 five-question block per DECISION state constitutes a dedicated block per decision point; Q5 is a mandatory FALLBACK question; evaluation note disqualifies column annotation, not question blocks |
| C-12 | Role Registry Gate | PASS | Step 2 prohibition-question gate precedes state tracing and Step 5 confirm occurs before walkthrough; gate mechanism is structural even if not a registry table; role names must be domain-specific by question constraint |
| C-13 | Phase-Scoped Exception Traces | PASS | `Phase origin: S-[ID]: [state name]` is a required labeled sub-field in each exception answer block; every trace carries explicit phase/state label |
| C-14 | SLA-to-Bottleneck Evidence Chain | PASS | AT-RISK citation requirement per row: "cite B-ID — required" enforces explicit B-ID linkage; one-directional (SLA→B); note flags bidirectional as desirable |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/6

```
composite = (5/5 * 60) + (3/3 * 30) + (6/6 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

C-12 note: prohibition-question gate satisfies the pass condition (gate precedes first state trace; generic names prohibited) but does not produce an R-NN ID registry table. Decision point answers may reference role names rather than R-IDs if Q2 is not explicit about ID format — lower structural guarantee than V-01/V-03/V-05. C-13 passes via required sub-field answer (not a column), which is structurally intermediate: answer can be omitted without blank-cell visibility. Wildcard: question format is the only variation predicted to improve C-02/C-07 content quality through answer construction vs cell-filling.

---

### V-03: Exception-First Lifecycle — Per-Phase Exception Before State Table

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | State table within each phase section has Entry Condition and Exits columns; phase boundary declares entry trigger and exit condition — two independent enforcement surfaces per phase |
| C-02 | Exception Flow Identification | PASS | Exception section structurally precedes state table in every phase section; phase context scopes failure-mode generation; 3+ traces reachable across multi-phase process; each traces to TERMINAL |
| C-03 | Role Assignment Accuracy | PASS | ROLE REGISTRY gate added in R2 with Anti-Generic Check column; Owner field per state; phase Owner field — two surfaces; registry gate precedes first phase section |
| C-04 | Bottleneck and Gap Identification | PASS | BOTTLENECK sections with Phase/cause/downstream impact; MISSING: gap sections with rationale and would-own; phase attribution strengthens bottleneck traceability |
| C-05 | Terminal State Completeness | PASS | Terminal states declared in PROCESS PROFILE; PHASE MAP Downstream Handoff must reference TERMINAL for final phase; exception traces all reach terminal |
| C-06 | Parallel Path Modeling | PASS | Per-phase "Parallel work streams in this phase:" section with Fork/Join/type/condition; "Sequential — no concurrent branches in this phase" label prevents silent omission |
| C-07 | Edge Case Enumeration | PASS | 3 EC blocks with phase-boundary impact framing; "must not duplicate any E-ID traced in phase sections" instruction |
| C-08 | Decision Point Explicitness | PASS | Per-phase "Decision points in this phase:" supplement with Condition:/Owner:/Branch YES:/Branch NO:/Fallback: all labeled and required |
| C-09 | Cross-Process Interaction Modeling | PASS | CROSS-PROCESS INTERACTIONS table with Sending phase/state, Receiving process, Data payload, Expected acknowledgment, Sending role |
| C-10 | SLA and Timing Analysis | PASS | Phase-tagged SLA table with AT-RISK annotation; "cross-ref B-[ID] if bottleneck identified" instruction; Bottleneck Cross-Ref column added in R2 |
| C-11 | Decision Supplement Block Structure | PASS | Per-phase decision supplement blocks with labeled Condition:/Owner:/Branch YES:/Branch NO:/Fallback: — dedicated block per decision point per phase |
| C-12 | Role Registry Gate | PASS | ROLE REGISTRY gate (R2 addition) with Anti-Generic Check column precedes first phase section; two-item gate checklist |
| C-13 | Phase-Scoped Exception Traces | PASS (strongest) | Exception section is structurally positioned BEFORE the state table in each phase section — phase context is architecturally encoded; exceptions cannot be written outside their originating phase; no column needed because structure enforces it |
| C-14 | SLA-to-Bottleneck Evidence Chain | PASS | Bottleneck Cross-Ref column in SLA table (R2 addition); "cross-ref B-[ID]" instruction; one-directional (SLA→B) |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/6

```
composite = (5/5 * 60) + (3/3 * 30) + (6/6 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

V-03 has the second-strongest C-13 enforcement: exception-first structural ordering makes phase anchoring architecturally guaranteed rather than instructionally requested. However, C-14 is one-directional and C-11 uses the same block structure as V-01 without the explicit `(required)` label marker. V-05's adoption of V-03's exception-first axis is the key R2 structural addition to the golden candidate.

---

### V-04: Axes 2+3 — Phrasing Register + Exception-First

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | State questions follow exception questions per phase; entry condition and exits are mandatory labeled question answers per state |
| C-02 | Exception Flow Identification | PASS | Exception questions precede state questions per phase — question ordering encodes phase context; 3+ exception answer blocks required; each reaches terminal |
| C-03 | Role Assignment Accuracy | PASS | Prohibition-question gate before state tracing + Step 5 confirm; R-ID reference in decision question blocks; same structural guarantee level as V-02 |
| C-04 | Bottleneck and Gap Identification | PASS | Bottleneck question blocks with cause/downstream impact/owner; gap question block with MISSING: label |
| C-05 | Terminal State Completeness | PASS | Terminal states declared first; exception answer blocks require terminal label; phase-end question requires TERMINAL reference for final phase |
| C-06 | Parallel Path Modeling | PASS | Parallel work streams question per phase with fork/join/type/condition sub-fields; "Sequential: [rationale]" fallback |
| C-07 | Edge Case Enumeration | PASS | 3 EC question blocks; "must not duplicate any E-ID" instruction |
| C-08 | Decision Point Explicitness | PASS | FALLBACK question mandatory per decision block (Q5); same five-question pattern as V-02 applied per phase |
| C-09 | Cross-Process Interaction Modeling | PASS | Cross-process question block with full handoff contract sub-fields |
| C-10 | SLA and Timing Analysis | PASS | SLA annotation questions; citation requirement + bidirectional note: "If AT-RISK cite B-ID; post-table: confirm every B-ID has an AT-RISK entry" |
| C-11 | Decision Supplement Block Structure | PASS | Five-question block per DECISION state; Q5=FALLBACK mandatory; dedicated per-decision block in question format |
| C-12 | Role Registry Gate | PASS | Prohibition-question gate precedes first phase's state questions; confirm before proceeding; same guarantee level as V-02 |
| C-13 | Phase-Scoped Exception Traces | PASS | Exception questions structurally precede state questions per phase — ordering enforces phase context in question format; `Phase origin:` sub-field also required per exception answer |
| C-14 | SLA-to-Bottleneck Evidence Chain | PASS (bidirectional note) | Citation requirement per AT-RISK row; post-table note: "confirm every B-ID has a corresponding AT-RISK entry" — bidirectional verification flagged as required; not enforced by a column on the B-ID side |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/6

```
composite = (5/5 * 60) + (3/3 * 30) + (6/6 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

V-04 combines V-02's question format with V-03's exception-first axis. C-14 has the strongest bidirectional enforcement within the question-format family (note requires both-direction confirmation). C-13 is strong because both ordering and sub-field reinforce phase anchoring. Structural visibility remains weaker than table-based variations: skipped question answers are less conspicuous than blank table cells.

---

### V-05: Full Synthesis — Golden Candidate

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | Table columns within each phase section enforce Entry Condition per row AND phase-level `Entry trigger:` boundary declaration — two independent enforcement surfaces per state |
| C-02 | Exception Flow Identification | PASS | Per-phase exception traces written before state tables; phase structure scopes failure modes; `None plausible — reason: [why]` label required if no exceptions in phase; no silent omission possible |
| C-03 | Role Assignment Accuracy | PASS | Registry gate checklist + phase `Owner: R-[N]` field + `Owner (R-ID)` column in phase state tables — three independent enforcement surfaces; generic name unavoidable to all three simultaneously |
| C-04 | Bottleneck and Gap Identification | PASS | Phase-sourced bottleneck table with `Phase: state/transition` reference; gap table with phase column and Would-Own (R-ID); bottlenecks explicitly tied to phase context |
| C-05 | Terminal State Completeness | PASS | Terminal states declared before phase sections; PHASE MAP Downstream Handoff must reference TERMINAL for last phase; per-phase `Phase end: [condition] -> [Next phase or TERMINAL:name]` closes every phase path |
| C-06 | Parallel Path Modeling | PASS | Per-phase parallel work streams section with R-ID branch ownership; "Sequential — no concurrent branches in this phase" label required if inapplicable |
| C-07 | Edge Case Enumeration | PASS | Pre-printed 3-row table; "must not overlap with any exception trace from phase sections" instruction referencing all E-IDs |
| C-08 | Decision Point Explicitness | PASS | Per-phase decision supplement: `Condition evaluated:` / `Owner: R-[N]` / `Branch YES:` / `Branch NO:` / `Fallback: (required)` — explicit "(required)" label makes omission structurally visible |
| C-09 | Cross-Process Interaction Modeling | PASS | Table with `Sending Phase: S-ID` format; full handoff contract: payload + acknowledgment + R-ID owner |
| C-10 | SLA and Timing Analysis | PASS | SLA table with Phase column + `Cross-Ref (B-ID)` column; AT-RISK NOTE required with B-ID cross-reference below at-risk rows |
| C-11 | Decision Supplement Block Structure | PASS (strongest) | Per-phase decision supplement blocks with `Fallback: (required)` explicit label; "(required)" text makes non-compliance visible as missing required field, not just missing content |
| C-12 | Role Registry Gate | PASS (strongest) | Registry gate checklist (3 items) + Anti-Generic Check column + three-surface enforcement (gate/phase owner/table column) |
| C-13 | Phase-Scoped Exception Traces | PASS (strongest) | Phase Origin Stamp column in exception table AND structural exception-first ordering within each phase section — two independent mechanisms; column labels the origin, structure encodes it architecturally |
| C-14 | SLA-to-Bottleneck Evidence Chain | PASS (strongest, bidirectional) | B-ID entries declare `SLA Node Affected` column; SLA at-risk entries cross-ref B-IDs; post-table orphan check verifies no unlinked entries on either side — bidirectional closure prevents orphan bottlenecks and ungrounded SLA risks |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/6

```
composite = (5/5 * 60) + (3/3 * 30) + (6/6 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

V-05 is the structural leader on every new aspirational criterion: strongest C-11 (`(required)` label), strongest C-12 (three surfaces), strongest C-13 (column + structural ordering), strongest C-14 (bidirectional check). The V-03 exception-first axis is the key R2 addition to R1's V-05.

---

## Round 2 Summary Table

| Rank | Variation | Essential | Rec. | Asp. | Score | Golden? | C-13 mechanism | C-14 direction |
|------|-----------|-----------|------|------|-------|---------|----------------|----------------|
| 1 | V-05 Full Synthesis | 5/5 | 3/3 | 6/6 | **100** | YES | Column + structural exception-first | Bidirectional (both B→SLA + SLA→B) |
| 2 | V-03 Exception-First | 5/5 | 3/3 | 6/6 | **100** | YES | Structural exception-first only | One-directional |
| 3 | V-04 Phrasing + Exception-First | 5/5 | 3/3 | 6/6 | **100** | YES | Ordering + sub-field (question format) | Bidirectional note (not column) |
| 4 | V-01 Output Format Fixed | 5/5 | 3/3 | 6/6 | **100** | YES | Column (Phase/State Origin) only | One-directional |
| 4 | V-02 Phrasing Register | 5/5 | 3/3 | 6/6 | **100** | YES | Required sub-field (question format) | One-directional citation |

**Discriminators are structural reliability, not score.** All 5 pass all 14 criteria. Discrimination lives in:
1. **C-13**: V-05/V-03 use structural architecture (exception-before-state in phase sections); V-01 uses a column; V-02/V-04 use question sub-fields. Structural order is the strongest form — it makes phase-scoped exceptions the only possible mode of generation.
2. **C-14**: V-05 enforces bidirectionality through columns on both sides (B-ID table has `SLA Node Affected`; SLA table has `Bottleneck Cross-Ref`). V-04 has a bidirectional note. V-01/V-02/V-03 are one-directional.
3. **C-11**: V-05's `Fallback: (required)` label makes the field visually non-skippable; other variations have `Fallback:` without the required marker.

---

## Excellence Signals — Round 2

### E-1: Bidirectional evidence chain closes the orphan-entry failure mode

All R1 variations with a `Bottleneck Cross-Ref` column in the SLA table pass C-14 with one-directional linkage (SLA at-risk → B-ID). But if a bottleneck is identified without a corresponding SLA annotation, or an SLA at-risk row is written referencing a B-ID that doesn't exist, the chain breaks silently. V-05's bidirectional structure — B-ID entries carry a `SLA Node Affected` column AND a post-table orphan check — closes this gap in both directions. No bottleneck can be "stranded" without SLA consequence, and no SLA risk can be "ungrounded" without a causal bottleneck.

**Pattern: Bidirectional cross-reference columns with an explicit post-table orphan check is a stronger C-14 guarantee than a single-direction cross-ref column.**

### E-2: Exception-first structural ordering is an architecturally stronger C-13 guarantee than a labeling column

V-01's `Phase/State Origin` column asks the model to label each exception's origin. V-03/V-05's exception-first ordering inside each phase section makes it structurally impossible to write an exception that isn't already inside a phase section. The column is an instruction; the structural order is a constraint. Under any generation pressure to abbreviate, a constraint holds longer than an instruction.

**Pattern: Writing exceptions before states within each phase section encodes phase-scoped anchoring as architecture, reducing C-13 omission risk more reliably than a labeling column.**

### E-3: `Fallback: (required)` explicit label elevates C-11 visibility beyond `Fallback:` alone

Every variation with a decision supplement block has a `Fallback:` field. V-05's `Fallback: (required)` label adds a compliance signal in the field name itself: omitting the answer leaves a field visibly incomplete. This is the equivalent of a form field marked with an asterisk vs an optional field — same data, different non-compliance visibility.

**Pattern: Appending `(required)` to structured field labels makes non-completion structurally visible without additional instruction overhead.**

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Bidirectional cross-reference columns with explicit post-table orphan check is a stronger C-14 guarantee than one-directional cross-ref: B-ID entries must declare SLA Node Affected and SLA at-risk entries must cite B-ID, with a post-table check that no entry on either side is unlinked", "Exception-first structural ordering within phase sections encodes phase-scoped anchoring as architecture rather than instruction — exceptions cannot be written outside their originating phase, making C-13 omission structurally impossible rather than just instructionally discouraged", "Appending (required) to structured field labels (e.g., Fallback: (required)) makes non-completion visually non-skippable without additional instruction overhead, elevating C-11 compliance signal beyond having a labeled Fallback: field alone"]}
```
