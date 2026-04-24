## Round 3 Scorecard — flow-lifecycle

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-05 All axes + Coverage Scan | 5/5 | 3/3 | 3/9 | **93.3** | YES |
| 2 | V-01 As-Is Column Enforcement | 5/5 | 3/3 | 1/9 | **91.1** | YES |
| 2 | V-04 Combined (As-Is + Root-cause) | 5/5 | 3/3 | 1/9 | **91.1** | YES |
| 4 | V-02 Root-Cause Register Schema | 5/5 | 3/3 | 0/9 | **90.0** | YES |
| 4 | V-03 Phase Delta Block | 5/5 | 3/3 | 0/9 | **90.0** | YES |

---

### Critical Finding: Rubric/Variation Mismatch

The R3 variations were designed against a **draft v3 rubric** targeting **As-Is Divergence Anchoring** and **Root-Cause Traceability** as the two new criteria. The **final v3 rubric** replaced those with C-15 (Decision Fallback Coverage), C-16 (Phase-Layer Structural Framing), and C-17 (Quantified Decision Boundaries).

None of the 5 variations target C-15, C-16, or C-17. The 93.3 ceiling is a mismatch artifact — the aspirational floor for R4 should be the ceiling here.

---

### Active Discriminators

**C-12 (Anti-Pattern Negation)**: V-05 PASS. Positioned negations in schema blocks — "Mandatory. Replacing with prose is a fail." in the Phase Delta header; "does not count" rules in Entry/Exit Contracts. V-01–V-04 have preamble-level negations ("generic labels are a fail") that name failure modes without concrete counter-examples.

**C-13 (Sequential Gate Locking)**: V-01, V-04, V-05 PASS. Three distinct gate forms work: explicit "GATE:" label (V-01), completion checklist pre-write (V-04), scan closure gate (V-05).

**C-14 (Terminal Verification Pass)**: V-05 ONLY. Scan Table A verifies per-state terminal reach (T-ID or OPEN). Scan Table B verifies per-exception resolution. Closing gate: "artifact may not be written until Scan Summary shows status CLOSED." V-01/V-04 have closing gates (C-13 PASS) but their gates enforce column population, not per-path terminal reach — gate is necessary but not sufficient for C-14.

---

### Excellence Signals

1. **Coverage scan as per-path terminal verification** — the only structure that passes C-14. Declarative terminal requirements in V-01–V-04 name the constraint but do not verify it. C-14 requires a scan artifact (rows per path, T-ID or OPEN), not an instruction.

2. **R3/rubric mismatch reveals R4 target gap** — C-15 (mechanism-level fallback framing), C-16 (phase table with SLA envelope + completion condition inline), C-17 (quantified threshold requirement in Condition column) are unreachable in R3 because no variation was designed for them. R4 must target all three explicitly.

```json
{"top_score": 93.3, "all_essential_pass": true, "new_patterns": ["Coverage scan as per-path terminal verification (V-05 Scan Table A/B with OPEN/CLOSED gate) is the only structure that passes C-14 — declarative terminal requirements in V-01 through V-04 name the constraint but do not verify it structurally; C-14 requires a scan artifact not an instruction", "R3 variations were designed against a draft-v3 rubric targeting As-Is Divergence Anchoring and Root-Cause Traceability; the final v3 rubric targets Decision Fallback Coverage (C-15), Phase-Layer Structural Framing (C-16), and Quantified Decision Boundaries (C-17) — none addressed by any variation; R4 must target these three criteria explicitly to raise aspirational ceiling above 3/9"]}
```
| Cross-Process Handoff is optional ("raise score"); table has Handoff Trigger, Recipient Process, Acceptance Condition but no Direction (inbound/outbound) or explicit coupling state |
| C-10 | SLA and Timing Annotation | FAIL | SLA Annotation has ≥3 nodes with timing and Scenario Breach (Y/N), but no causal bottleneck reference column linking AT-RISK nodes to bottleneck entries |
| C-11 | Role-First Anchoring | FAIL | Step 1 is Domain Role Registry before any state trace (roles-first ordering present); anti-pattern named ("generic labels are a fail"); but no concrete domain-title example provided (e.g., "Senior Credit Analyst") |
| C-12 | Anti-Pattern Negation | FAIL | "Generic labels are a fail" names the failure mode but does not provide a concrete counter-example showing the difference between bad ("Approver") and good ("Senior Credit Analyst") |
| C-13 | Sequential Gate Locking | PASS | Explicit "GATE: Every decision point in the trace must cite an R-ID from this table" labeled instruction enforces role registry completion before any decision point is authored; protects C-05 |
| C-14 | Terminal Verification Pass | FAIL | Terminal Declaration is a declaration, not a per-path structural scan; no coverage verification step confirms each specific path reaches its terminal; no OPEN/CLOSED status |
| C-15 | Decision Fallback Coverage | FAIL | Fallback column present in decision table; but instruction says "provide a fallback path" without specifying mechanism-level impairment (role unavailable, system down, config missing); model will produce process fallbacks, not mechanism-level fallbacks |
| C-16 | Phase-Layer Structural Framing | FAIL | Phase Map table (Ph-ID, Phase Name, Purpose, Receives From) sits above state trace; but table lacks entry trigger, completion condition, and SLA envelope; SLA Annotation is a separate optional section, not integrated into phase table |
| C-17 | Quantified Decision Boundaries | FAIL | Decision table has Condition column but no instruction requiring specific measurable thresholds (amounts, durations, counts); qualitative conditions are not blocked |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 1/9 (C-13)

```
score = (5/5 * 60) + (3/3 * 30) + (1/9 * 10)
      = 60 + 30 + 1.11
      = 91.1
```

**Score: 91.1 / 100 — GOLDEN**

---

#### V-02 — Root-Cause Register Schema Axis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | Section 3 State Trace table with Entry Condition and Exit Transitions (labeled) columns |
| C-02 | Exception Flow Traces | PASS | Section 4 Exception Catalog ≥3 with Phase Origin, Trigger, Deviation, As-Is Handling, Terminal or Recovery |
| C-03 | Terminal State Completeness | PASS | Section 5 Terminal Declaration: "Every traced path and every exception must reach a terminal" |
| C-04 | Bottleneck and Gap Identification | PASS | Sections 7–8: ≥2 bottlenecks + ≥1 gap with source artifact, source field, root cause, and downstream impact columns; exemplars provided |
| C-05 | Domain Role Assignment | PASS | Section 1 Domain Role Registry; "Generic labels are a fail"; every decision cites R-ID |
| C-06 | Parallel Path Modeling | PASS | "Parallel paths: model at least one fork-join with named branches, join condition, and merge owner (R-ID)" |
| C-07 | Decision Point Explicitness | PASS | Decision label condition, name R-ID, name all branches, provide fallback; schema enforced |
| C-08 | Edge Case Enumeration | PASS | Section 6 Edge Case Catalog ≥3 with Trigger, Process Impact, Correct Handling |
| C-09 | Cross-Lifecycle Dependencies | FAIL | Optional cross-process handoff section; lacks Direction (inbound/outbound) column; Acceptance Condition ≠ coupling state (both sides) |
| C-10 | SLA and Timing Annotation | FAIL | SLA Annotation: ≥3 nodes with Expected Duration, At-Risk Threshold, Scenario Breach; but no causal bottleneck reference in SLA table; Phase Exit Gate "Blocked by" and SLA table are unlinked |
| C-11 | Role-First Anchoring | FAIL | Role Registry in Section 1 establishes roles-first ordering; "Generic labels are a fail"; no concrete domain-title example provided |
| C-12 | Anti-Pattern Negation | FAIL | "Generic labels are a fail" + "NONE is not acceptable in 'Blocked by' unless you explicitly justify why"; neither provides a concrete counter-example pairing wrong vs. right |
| C-13 | Sequential Gate Locking | FAIL | No explicit "GATE:" or "do not proceed until" instruction; Phase Exit Gate "Blocked by" is an output-level constraint, not a structural dependency gate with criterion reference |
| C-14 | Terminal Verification Pass | FAIL | No coverage scan; terminal declaration is declarative, not a per-path structural verification |
| C-15 | Decision Fallback Coverage | FAIL | Decision instruction: "label condition, name R-ID, name all branches, provide fallback"; fallback present but not framed as mechanism-level impairment |
| C-16 | Phase-Layer Structural Framing | FAIL | Phase Index table (Ph-ID, Phase Name, Purpose, Receives From) + Phase Exit Gates per phase; but Phase Index lacks SLA envelope and completion condition; Exit Gates are per-phase inline blocks, not a summary table row |
| C-17 | Quantified Decision Boundaries | FAIL | No instruction requiring measurable thresholds in decision conditions |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 0/9

```
score = (5/5 * 60) + (3/3 * 30) + (0/9 * 10)
      = 60 + 30 + 0
      = 90.0
```

**Score: 90.0 / 100 — GOLDEN**

---

#### V-03 — Phase Delta Block Axis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | State TABLE per phase with Entry Condition, Happy-Path Exit (labeled), Exception Exit columns; ≥6 states across phases |
| C-02 | Exception Flow Traces | PASS | Exception Catalog ≥3 with Phase Origin, Trigger, Deviation, As-Is Handling, Delta Ref, Terminal or Recovery |
| C-03 | Terminal State Completeness | PASS | Terminal Declaration: "Every traced path and every exception must reach a terminal"; T-ID, Type, Reached From columns |
| C-04 | Bottleneck and Gap Identification | PASS | Bottleneck Register ≥2 + Gap Register ≥1; both require source artifact citations (DL-ID or Phase Exit Gate "Blocked by"); root cause and downstream impact columns required |
| C-05 | Domain Role Assignment | PASS | Role Registry at SETUP before Phase Index and all phase content; "Generic labels are a fail"; every decision cites R-ID |
| C-06 | Parallel Path Modeling | PASS | Parallel Path block per phase with fork, branches, join condition, merge owner; "If no parallel execution: state that explicitly" |
| C-07 | Decision Point Explicitness | PASS | Decision Table per phase (D-ID, Decision, Condition, Owner, Branch A, Branch B, Fallback, Delta Ref); schema enforced per phase |
| C-08 | Edge Case Enumeration | PASS | Edge Case Catalog ≥3 with Trigger, Process Impact, As-Is Behavior, Delta Ref, Correct Handling |
| C-09 | Cross-Lifecycle Dependencies | FAIL | Cross-Process Handoff: Trigger, Recipient, Fields, Acceptance Condition, As-Is Gap, Delta source; no Direction column; coupling state not explicitly named on both sides |
| C-10 | SLA and Timing Annotation | FAIL | SLA Annotation table ("raise score") ≥3 nodes; Phase Exit Gates have "Blocked by" (bottleneck) + "Typical duration" (SLA); but SLA table and Phase Exit Gate bottlenecks are not linked — no cross-reference instruction |
| C-11 | Role-First Anchoring | FAIL | Role Registry established before Phase Index; "Generic labels are a fail"; no concrete domain-title example |
| C-12 | Anti-Pattern Negation | FAIL | No explicit failure-mode counter-example; "Generic labels are a fail" names the failure without illustrating it |
| C-13 | Sequential Gate Locking | FAIL | "FOR EACH PHASE, IN THIS EXACT ORDER" enforces phase structure; but no explicit "GATE:" or "do not proceed until" instruction with criterion reference |
| C-14 | Terminal Verification Pass | FAIL | No coverage scan; terminal declaration has "Reached From (Ph-IDs and E-IDs)" field, providing partial traceability, but no per-path structural confirmation |
| C-15 | Decision Fallback Coverage | FAIL | Fallback column in Decision Table present; no mechanism-level framing |
| C-16 | Phase-Layer Structural Framing | FAIL | Phase Index table (Ph-ID, Phase Name, Purpose, Receives From) sits above state traces; Phase Entry Contract per phase provides entry condition; Phase Exit Gate provides completion condition and "Typical duration"; but these are not consolidated into the Phase Index table with SLA envelope |
| C-17 | Quantified Decision Boundaries | FAIL | Condition column in Decision Table; no measurable threshold requirement |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 0/9

```
score = (5/5 * 60) + (3/3 * 30) + (0/9 * 10)
      = 60 + 30 + 0
      = 90.0
```

**Score: 90.0 / 100 — GOLDEN**

---

#### V-04 — Combined (As-Is Column Enforcement + Root-Cause Register Schema)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | Step 3 State Trace with As-Is Divergence (Y/N) and Current Practice columns required; Entry Condition and Exit Transitions (labeled) enforced |
| C-02 | Exception Flow Traces | PASS | Step 5 Exception Catalog ≥3 with Phase Origin, Trigger, Deviation, As-Is Handling, Terminal or Recovery |
| C-03 | Terminal State Completeness | PASS | Step 6 Terminal Declaration: "every traced path and every exception must reach a terminal" |
| C-04 | Bottleneck and Gap Identification | PASS | Steps 8–9: ≥2 bottlenecks + ≥1 gap; Source Artifact + Source Field + Root Cause + Downstream Impact required; exemplar format provided; "empty Source Artifact or empty Root Cause is a fail" |
| C-05 | Domain Role Assignment | PASS | Step 1 Domain Role Registry; "Generic labels are a fail"; every decision cites R-ID |
| C-06 | Parallel Path Modeling | PASS | "for at least one fork-join" with branches, join condition, merge owner, As-Is join |
| C-07 | Decision Point Explicitness | PASS | Decision table D-ID with Condition, Owner, Branch A, Branch B, Fallback, As-Is Owner; schema enforced |
| C-08 | Edge Case Enumeration | PASS | Step 7 Edge Case Catalog ≥3 with As-Is Behavior required; Trigger, Process Impact, Correct Handling |
| C-09 | Cross-Lifecycle Dependencies | FAIL | Optional cross-process handoff table; lacks Direction column |
| C-10 | SLA and Timing Annotation | FAIL | SLA Annotation optional ("raise score"); ≥3 nodes with timing; no causal bottleneck reference linking AT-RISK rows to register entries |
| C-11 | Role-First Anchoring | FAIL | Roles-first ordering present; no concrete domain-title example |
| C-12 | Anti-Pattern Negation | FAIL | Completion checklist: "Any unchecked item in this list is a fail" — names failure mode but the checklist items are completeness requirements, not counter-examples showing what bad looks like |
| C-13 | Sequential Gate Locking | PASS | Completion checklist "before writing" + "Any unchecked item in this list is a fail" constitutes a structural closing gate: artifact cannot be written until all as-is columns and root-cause fields are populated; gate enforces C-04 (bottleneck cause) and C-02/C-08 (as-is handling) |
| C-14 | Terminal Verification Pass | FAIL | Terminal Declaration is declarative; no per-path structural verification scan |
| C-15 | Decision Fallback Coverage | FAIL | Fallback column present; "provide a fallback path" instruction; no mechanism-level framing |
| C-16 | Phase-Layer Structural Framing | FAIL | Phase Map table (Ph-ID, Phase Name, Purpose, Receives From) + Phase Exit Gates inline; no SLA envelope or completion condition in phase table |
| C-17 | Quantified Decision Boundaries | FAIL | No measurable threshold requirement |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 1/9 (C-13)

```
score = (5/5 * 60) + (3/3 * 30) + (1/9 * 10)
      = 60 + 30 + 1.11
      = 91.1
```

**Score: 91.1 / 100 — GOLDEN**

---

#### V-05 — Combined (All Three R3 Axes + Phase Gates + Coverage Scan + Exception Density)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | State Table per phase with Entry Condition, Happy-Path Exit (labeled), Exception Exit, Owner (R-ID), As-Is Divergence (Y/N), Delta Ref columns; ≥6 states across phases; Scan Table A verifies entry condition and labeled exit per state |
| C-02 | Exception Flow Traces | PASS | Exception Catalog ≥3 with Phase Origin, Trigger, Deviation, As-Is Handling, Delta Ref, Terminal or Recovery; Scan Table B verifies As-Is Handling presence per exception |
| C-03 | Terminal State Completeness | PASS | Terminal Declaration + Scan Table A "Reaches Terminal? (T-ID or OPEN)" per state + Scan Table B "Has Terminal or Recovery? (Y/N)" per exception; Scan Summary "States with open paths" + "Exceptions without resolution" |
| C-04 | Bottleneck and Gap Identification | PASS | Bottleneck Register ≥2 + Gap Register ≥1; Source Artifact, Source Field, Root Cause required; Scan Table D verifies source artifact and root cause format; valid source artifacts enumerated |
| C-05 | Domain Role Assignment | PASS | Role Registry in Layer 0 before all phase content; "Generic labels are a fail"; every decision cites R-ID |
| C-06 | Parallel Path Modeling | PASS | Parallel Path block per phase with fork, branches, join condition, merge owner, As-Is join; "If no parallel execution: state that explicitly and identify one parallel path that would improve this phase" |
| C-07 | Decision Point Explicitness | PASS | Decision Table per phase (D-ID, Decision, Condition, Owner, Branch A, Branch B, Fallback, Delta Ref); schema enforced |
| C-08 | Edge Case Enumeration | PASS | Edge Case Catalog ≥3 with Phase, Trigger, Process Impact, As-Is Behavior, Delta Ref, Correct Handling; ≥3 edge cases distinct from exceptions required |
| C-09 | Cross-Lifecycle Dependencies | FAIL | Cross-Process Handoff "(raise score)" block present: Trigger, Recipient, Fields, Acceptance Condition, As-Is Gap, Delta source; no Direction (inbound/outbound) field; coupling state on both sides not explicitly named |
| C-10 | SLA and Timing Annotation | FAIL | SLA Annotation "(raise score)" with ≥3 nodes from Phase Exit Gates or State Tables, timing, Scenario Breach column; Phase Exit Gates have "Blocked by" (causal bottleneck) + "Typical cycle time"; but SLA table does not require cross-reference to bottleneck entry; C-10 requires the AT-RISK annotation to carry the causal bottleneck reference inline |
| C-11 | Role-First Anchoring | FAIL | Layer 0 Role Registry before all phases; "Generic labels are a fail"; no concrete domain-title example (e.g., "Senior Credit Analyst") in role section |
| C-12 | Anti-Pattern Negation | PASS | Multiple concrete anti-pattern negations: (1) "Mandatory. Replacing with prose is a fail." for Phase Delta — names the failure mode (prose substitution) with no inference required; (2) "Information about phase entry that appears only in prose outside this schema does not count for C-11" — names the bypass pattern explicitly; (3) "The artifact may not be written until Scan Summary shows status CLOSED. Every S-ID, E-ID, and Ph-ID must appear in the scan tables. Any unchecked item is a fail." — blocks the most common miss (closing with incomplete paths) |
| C-13 | Sequential Gate Locking | PASS | "The artifact may not be written until Scan Summary shows status CLOSED" is an explicit dependency gate: do not write until coverage scan passes; gate enforces terminal completeness check (the hardest criterion in the artifact); coverage scan is the mechanism it protects |
| C-14 | Terminal Verification Pass | PASS | Scan Table A: one row per S-ID, "Reaches Terminal? (T-ID or OPEN)" column, "Resolution (if OPEN)" column; Scan Table B: one row per E-ID, "Has Terminal or Recovery? (Y/N)" column; Scan Summary: "States with open paths: [N] — list S-IDs"; artifact may not close with status OPEN — this is a per-path structural confirmation, not a count check |
| C-15 | Decision Fallback Coverage | FAIL | Decision Table Fallback column present; no instruction specifying fallback must address mechanism-level impairment (role unavailable, system down, config missing); model will fill process fallbacks |
| C-16 | Phase-Layer Structural Framing | FAIL | Phase Index (Ph-ID, Phase Name, Purpose, Receives From) sits above state traces; Phase Entry Contract per phase provides entry condition; Phase Exit Gate provides completion condition + "Blocked by" + "Typical cycle time"; individually all required fields exist, but they are distributed across per-phase structural blocks rather than consolidated into the Phase Index table with an SLA envelope column |
| C-17 | Quantified Decision Boundaries | FAIL | Decision Table Condition column; no instruction requiring measurable thresholds; Delta Ref column connects to Phase Delta but Phase Delta does not enforce quantified conditions |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 3/9 (C-12, C-13, C-14)

```
score = (5/5 * 60) + (3/3 * 30) + (3/9 * 10)
      = 60 + 30 + 3.33
      = 93.3
```

**Score: 93.3 / 100 — GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Score | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 |
|------|-----------|-----------|-------------|--------------|-------|------|------|------|------|------|------|
| 1 | V-05 All axes + Coverage Scan | 5/5 | 3/3 | 3/9 | **93.3** | PASS | PASS | PASS | FAIL | FAIL | FAIL |
| 2 | V-01 As-Is columns | 5/5 | 3/3 | 1/9 | **91.1** | FAIL | PASS | FAIL | FAIL | FAIL | FAIL |
| 2 | V-04 As-Is + Root-cause | 5/5 | 3/3 | 1/9 | **91.1** | FAIL | PASS | FAIL | FAIL | FAIL | FAIL |
| 4 | V-02 Root-cause registers | 5/5 | 3/3 | 0/9 | **90.0** | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |
| 4 | V-03 Phase Delta blocks | 5/5 | 3/3 | 0/9 | **90.0** | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |

All essential criteria pass across all 5 variations. Discrimination lives entirely in aspirational. C-12/C-13/C-14 are the active discriminators in Round 3.

C-15, C-16, and C-17 score 0/5 across all variations — this is the rubric/variation mismatch consequence.

---

## Structural Guarantee Differences Within 93.3 Cluster

V-05 is the sole top scorer. Its three passing aspirational criteria each have a distinct structural mechanism:

| Criterion | V-05 mechanism | Structural guarantee |
|-----------|---------------|----------------------|
| C-12 (Anti-Pattern Negation) | "Mandatory. Replacing with prose is a fail." + "does not count for C-11" in Entry/Exit Contracts | Author cannot bypass Phase Delta with prose; the negation is structurally positioned in the schema, not in a preamble |
| C-13 (Sequential Gate Locking) | "The artifact may not be written until Scan Summary shows status CLOSED" | Closing gate is in the OUTPUT section — the model must pass coverage scan before writing; gate cannot be skipped |
| C-14 (Terminal Verification Pass) | Scan Table A (per-state T-ID or OPEN), Scan Table B (per-exception terminal/recovery), Scan Summary open-path count | Per-path structural confirmation, not a count; OPEN status prevents closing |

---

## Excellence Signals — Round 3

### E-1: Coverage Scan is the only mechanism that passes C-14

The Terminal Verification Pass criterion requires an explicit per-path structural confirmation that every traced path reaches a named terminal — not a count. V-05's three-scan architecture (Scan Table A per state, Scan Table B per exception, Scan Summary with CLOSED/OPEN status) is the only structure in any of the 5 variations that satisfies this requirement. V-01 through V-04 have declarative terminal requirements ("every traced path must reach a terminal") that are instructions to the author, not verifications of the output.

**Design principle**: Per-path verification must be a structural artifact within the output (a scan table), not an instruction about what to produce. Instructions describe intent; scan tables enforce it.

### E-2: Anti-pattern negations must be schema-positioned to pass C-12

V-01/V-02/V-03/V-04 all name failure modes ("generic labels are a fail", "empty cell is a fail") but position them in general instructions or rule lists. V-05 positions negations inside schema blocks: "Mandatory. Replacing with prose is a fail." appears in the PHASE DELTA section header, at the exact point where the failure would occur. "Information about phase entry that appears only in prose outside this schema does not count" appears in the PHASE ENTRY CONTRACT block, where bypass would happen.

**Design principle**: Anti-pattern negations pass C-12 when they are positioned at the structural point of failure, not in a preamble or rule list. The negation blocks the miss at the moment of authoring.

### E-3: C-15, C-16, C-17 remain unaddressed — R4 target gap

The rubric was extended to C-17 with three new criteria between when R3 variations were designed and when scoring occurred. None of the 5 variations address:
- **C-15 (Decision Fallback Coverage)**: Adding "Fallback" columns without mechanism-level framing (role unavailable, system down, config missing) does not satisfy this criterion. R4 must frame fallbacks explicitly as mechanism-level: "What happens when the decision owner is unavailable?"
- **C-16 (Phase-Layer Structural Framing)**: The Phase Index table needs three additional columns: entry trigger, completion condition, SLA envelope. Currently these exist in per-phase blocks (Entry Contract, Exit Gate) but not in the summary table.
- **C-17 (Quantified Decision Boundaries)**: Decision Condition columns accept qualitative conditions. R4 needs an instruction like "decision conditions must name specific measurable thresholds (amounts, durations, counts)."

---

## Round 3 Findings

### F-01: The rubric/variation mismatch is the ceiling constraint

All 5 variations earn 90.0 on essential + recommended (60 + 30 = 90), and the only aspiration points in play are C-12, C-13, C-14 — which V-05 addresses via Coverage Scan and schema-positioned negations. C-15, C-16, C-17 are unreachable in R3 because no variation targets them. The 93.3 ceiling is an artifact of late rubric extension, not variation weakness.

### F-02: C-13 is achievable by closing-gate pattern alone

V-01 passes C-13 via an explicit "GATE:" instruction. V-04 passes via a "completion checklist before writing." V-05 passes via "artifact may not be written until scan status CLOSED." All three are structurally distinct gate forms, and all pass. The minimum required: any explicit instruction that blocks the author from proceeding until a named condition is true, where the condition maps to a correctness requirement.

### F-03: C-14 requires an artifact scan, not an instruction

V-01/V-04 both have closing gates (C-13 PASS) but neither passes C-14. The difference: their gates enforce column population, not terminal reach per path. C-14 requires a scan artifact (rows per path, T-ID or OPEN) that structurally confirms each path's terminal. The closing gate is necessary but not sufficient for C-14; the scan table is the additional requirement.

### F-04: All 5 variations achieve golden threshold

Floor established in R2 holds: essential 5/5 and composite ≥ 80 for all. The golden threshold is non-discriminating at R3; discrimination requires the aspirational tier.

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate:
- Highest composite score (93.3/100)
- Three aspirational criteria pass with structural guarantees (schema-positioned negations, closing scan gate, per-path scan tables)
- Coverage Scan is the most complete verification mechanism across all R3 variations
- Phase Delta + Delta Ref system closes the loop between structural tables and registers

**Gap to full aspirational score**: V-05 misses C-15, C-16, C-17. For R4, V-05 should be augmented with: (1) mechanism-level framing in Fallback column instructions; (2) SLA envelope + entry trigger + completion condition added to Phase Index summary table; (3) measurable threshold requirement in Decision Condition column.

```json
{"top_score": 93.3, "all_essential_pass": true, "new_patterns": ["Coverage scan as per-path terminal verification (V-05 Scan Table A/B with OPEN/CLOSED gate) is the only structure that passes C-14 — declarative terminal requirements in V-01 through V-04 name the constraint but do not verify it structurally; C-14 requires a scan artifact not an instruction", "R3 variations were designed against a draft-v3 rubric targeting As-Is Divergence Anchoring and Root-Cause Traceability; the final v3 rubric targets Decision Fallback Coverage (C-15), Phase-Layer Structural Framing (C-16), and Quantified Decision Boundaries (C-17) — none addressed by any variation; R4 must target these three criteria explicitly to raise aspirational ceiling above 3/9"]}
```
