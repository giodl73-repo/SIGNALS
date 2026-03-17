## Round 1 Scorecard — flow-lifecycle

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-02 Role Registry First | 5/5 | 3/3 | 2/2 | **100** | YES |
| 1 | V-03 Lifecycle Emphasis | 5/5 | 3/3 | 2/2 | **100** | YES |
| 1 | V-04 State Table + Registry | 5/5 | 3/3 | 2/2 | **100** | YES |
| 1 | V-05 Full Synthesis | 5/5 | 3/3 | 2/2 | **100** | YES |
| 5 | V-01 State Table Only | 5/5 | 2/3 | 2/2 | **90** | YES |

---

**The single discriminator: C-08 (Decision Point Explicitness)**

V-01 fails C-08. The DECISION type column in the state table and the exits format encourage labeled conditions but do not structurally require an exhaustive outcome set or a fallback branch. The other four variations all include a dedicated decision supplement block with an explicit `Fallback:` or `Fallback branch:` field — and all four pass C-08 unconditionally.

**Within the 100 cluster**, structural guarantees differ:
- **C-03**: V-05 (3 surfaces) > V-04 (2 surfaces) > V-02 (registry gate) > V-03 (role-list hint, no gate)
- **C-02 specificity**: V-05/V-03 (phase-contained traces) > V-04/V-02 (flat exception table/blocks)
- **C-10 coherence**: V-02/V-04/V-05 (SLA↔bottleneck cross-ref column) > V-01/V-03 (SLA section, no cross-ref)

**Recommended golden candidate: V-05** — role registry gate + per-phase state tables + per-phase decision supplement combine without contradiction; no axis trades off a criterion to enable another.

**Excellence signals:**
1. Decision supplement with explicit fallback field is the structural requirement for C-08 — type column annotation alone is not sufficient
2. Role registry gate with checklist prevents C-03 generic-name failure more reliably than role-list hints
3. Phase-contained exception traces improve C-02 specificity by scoping failure-mode generation to phase context
4. SLA-to-bottleneck cross-reference column creates a closed evidence chain that V-01/V-03 lack

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Decision supplement block with explicit fallback field is necessary for C-08 pass; DECISION type column annotation and exits format alone are structurally insufficient for exhaustive outcome coverage", "Role registry gate with explicit checklist prevents C-03 generic-name failure more reliably than column hints or role-list suggestions in a PROCESS PROFILE section", "Phase-contained exception traces improve C-02 specificity by scoping failure-mode generation to phase context without additional instructions", "SLA-to-bottleneck cross-reference column creates a closed evidence chain linking timing risk to identified bottleneck causation"]}
```
01 with `MISSING:` label and `Rationale` field |
| C-05 | Terminal State Completeness | PASS | `TERMINAL STATES` declared before table; exit format requires `TERMINAL:[name]` reference; terminal rows with `Type=TERMINAL` close all paths |
| C-06 | Parallel Path Modeling | PASS | Pre-printed `PARALLEL PATHS` section with Fork/Join/Join-type/Join-condition fields |
| C-07 | Edge Case Enumeration | PASS | Pre-printed 3-row EDGE CASES table with "must not duplicate named exception flows" instruction |
| C-08 | Decision Point Explicitness | **FAIL** | DECISION type column present; exits format encourages labeled conditions. No dedicated decision supplement block; no explicit fallback branch requirement. Model can produce DECISION rows without exhaustive outcome coverage. |
| C-09 | Cross-Process Interaction Modeling | PASS | Pre-printed 5-column CROSS-PROCESS INTERACTIONS table |
| C-10 | SLA and Timing Analysis | PASS | Pre-printed 3-row SLA ANALYSIS table with `At-Risk?` and `Risk Reason` columns |

**Essential**: 5/5 | **Recommended**: 2/3 | **Aspirational**: 2/2

```
composite = (5/5 * 60) + (2/3 * 30) + (2/2 * 10)
          = 60 + 20 + 10
          = 90
```

**Score: 90 / 100 -- GOLDEN** (all essential pass, composite >= 80)

---

### V-02: Role Registry Declared Before States

Single axis: role registry gate completed before any state is traced; all decision points reference R-ID.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | State sub-fields (`Entry condition:`, `Exits:`) are labeled and required; prose format but omission visible as blank labeled field |
| C-02 | Exception Flow Identification | PASS | 3 pre-printed exception blocks with `Trigger`, `Trace`, `Handling role`, `Resolution` -- each reaches terminal state |
| C-03 | Role Assignment Accuracy | PASS | Registry gate explicitly prevents generic names before state tracing; R-ID reference required at every decision point; role set matched to process type by auto-select instruction |
| C-04 | Bottleneck and Gap Identification | PASS | Pre-printed `BOTTLENECK B-01/B-02` and `MISSING G-01` blocks with `Cause:`, `Downstream impact:`, `Owner role:` sub-fields |
| C-05 | Terminal State Completeness | PASS | `TERMINAL STATES` declared before walkthrough; walkthrough exits reference terminal names; exception traces all reach terminal |
| C-06 | Parallel Path Modeling | PASS | Pre-printed `PARALLEL PATHS` section with R-ID branch ownership per branch |
| C-07 | Edge Case Enumeration | PASS | 3 pre-printed EC blocks with `Why problematic:` and `Correct response:` sub-fields |
| C-08 | Decision Point Explicitness | PASS | DECISION state annotation explicitly requires `Decision rule:` field and `Fallback branch:` field; both labeled and required in template |
| C-09 | Cross-Process Interaction Modeling | PASS | Pre-printed section with `Sending state`, `Receiving process`, `Data payload`, `Expected acknowledgment`, `Handoff owner` fields |
| C-10 | SLA and Timing Analysis | PASS | Pre-printed 3-row table with `Bottleneck Cross-Ref` column -- links SLA at-risk entries to B-ID findings |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2

```
composite = (5/5 * 60) + (3/3 * 30) + (2/2 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

Note: V-02 uses prose sub-field walkthrough, not a table. Structural risk: the model can omit an entire state from the walkthrough without a blank cell making it visible, unlike V-01/V-04/V-05's table format. C-03 is strongest in this variation.

---

### V-03: Lifecycle Emphasis -- Named Phase Sections

Single axis: each phase is a named section with declared entry trigger, exit condition, and downstream handoff.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | Phase boundary declares entry trigger; states inside phases have labeled sub-fields (`Entry condition:`, `Exits:`). Phase-section structure organizes coverage; sub-fields, not table columns, enforce it. |
| C-02 | Exception Flow Identification | PASS | `Exception traces originating in this phase` required per phase -- phase context increases trace specificity. 3+ traces reachable across multi-phase process; each traces to TERMINAL. |
| C-03 | Role Assignment Accuracy | PASS | `Domain roles (auto-selected from process type)` in PROCESS PROFILE; owner field per state; phase Owner field. No registry gate: moderate generic-name risk (higher than V-02/V-04/V-05, lower than V-01). |
| C-04 | Bottleneck and Gap Identification | PASS | Pre-printed `BOTTLENECK B-01/B-02` and `MISSING G-01` sections with `Phase where it belongs`, `Cause:`, `Downstream impact:` sub-fields |
| C-05 | Terminal State Completeness | PASS | Terminal states declared in PROCESS PROFILE; PHASE MAP `Downstream Handoff` column must reference `TERMINAL:name` for final phase; exception traces all reach terminal |
| C-06 | Parallel Path Modeling | PASS | Per-phase `Parallel work streams in this phase:` section with Fork/Join/type/condition fields |
| C-07 | Edge Case Enumeration | PASS | 3 pre-printed EC blocks with phase-boundary impact framing; "must not duplicate any E-ID traced in phase sections" instruction |
| C-08 | Decision Point Explicitness | PASS | `Decision points in this phase:` supplement with `Condition:`, `Owner:`, `Branch YES:`, `Branch NO:`, `Fallback:` all labeled and required |
| C-09 | Cross-Process Interaction Modeling | PASS | Pre-printed section with `Sending phase/state`, `Receiving process`, `Data payload`, `Expected acknowledgment`, `Sending role` |
| C-10 | SLA and Timing Analysis | PASS | Pre-printed phase-tagged table with `Phase` column; AT-RISK annotation with `cross-ref B-[ID] if bottleneck identified` instruction |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2

```
composite = (5/5 * 60) + (3/3 * 30) + (2/2 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

Note: V-03's C-02 produces higher-quality exception traces than V-01/V-02/V-04 because phase context scopes what failure modes are realistic. C-03 lacks the registry gate; role names that drift toward generic are harder to catch at the point of state authoring.

---

### V-04: State Table + Role Registry First (Axes 1+2)

Combined: role registry gate (V-02 axis) + flat state transition table (V-01 axis).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | Table columns enforce `Entry Condition` and `Exits` per row; decision supplement adds a second enforcement surface |
| C-02 | Exception Flow Identification | PASS | Exception table with R-ID column; 3 pre-printed rows; each reaches terminal |
| C-03 | Role Assignment Accuracy | PASS | Registry gate (with checklist: no generic names, min 3 roles, all gates covered) + Owner column requires R-ID from registry -- dual enforcement eliminates generic name risk |
| C-04 | Bottleneck and Gap Identification | PASS | Pre-printed bottleneck table with `Owner (R-ID)` column; missing-step table with `Would-Own (R-ID)` column |
| C-05 | Terminal State Completeness | PASS | Terminal states declared; table terminal rows with `--` in Owner/Exits; exit format enforces TERMINAL references |
| C-06 | Parallel Path Modeling | PASS | Pre-printed section with `R-[N] owns` per branch annotation |
| C-07 | Edge Case Enumeration | PASS | Pre-printed 3-row table; "non-overlapping with exception table" instruction |
| C-08 | Decision Point Explicitness | PASS | Decision supplement block: `D-[S-ID]: Condition: [rule] \| Fallback branch: [condition] -> S-[ID]` -- explicit fallback requirement |
| C-09 | Cross-Process Interaction Modeling | PASS | Pre-printed 5-column table with `Owner (R-ID)` column |
| C-10 | SLA and Timing Analysis | PASS | Pre-printed 3-row table with `Cross-Ref (B-ID)` column + AT-RISK NOTE instruction below at-risk rows |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2

```
composite = (5/5 * 60) + (3/3 * 30) + (2/2 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

---

### V-05: Full Synthesis (All Three Axes)

Combined: role registry (V-02) + state table format (V-01) + phase sections (V-03).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | Table columns within each phase section enforce `Entry Condition` per row AND phase-level `Entry trigger:` boundary declaration -- two independent surfaces |
| C-02 | Exception Flow Identification | PASS | Per-phase exception traces; phase context scopes realistic failures; each reaches terminal with R-ID; "None plausible" label required if inapplicable -- no silent omission |
| C-03 | Role Assignment Accuracy | PASS | Registry gate checklist + phase `Owner: R-[N]` field + `Owner (R-ID)` column in phase state tables -- three independent surfaces; generic name impossible unless all three surfaces are actively ignored |
| C-04 | Bottleneck and Gap Identification | PASS | Phase-sourced bottleneck table with `Phase: state/transition` reference; gap table with phase column and `Would-Own (R-ID)` -- bottlenecks explicitly tied to phase context |
| C-05 | Terminal State Completeness | PASS | Terminal states declared before phase sections; PHASE MAP `Downstream Handoff` must reference TERMINAL for last phase; per-phase `Phase end: [condition] -> [Next phase or TERMINAL:name]` closes every phase path explicitly |
| C-06 | Parallel Path Modeling | PASS | Per-phase `Parallel work streams in this phase:` section with R-ID branch ownership; "Sequential -- no concurrent branches in this phase" label if inapplicable -- no silent omission |
| C-07 | Edge Case Enumeration | PASS | Pre-printed 3-row table; "must not overlap with any exception trace from phase sections" instruction referencing all E-IDs |
| C-08 | Decision Point Explicitness | PASS | Per-phase decision supplement: `Condition evaluated:`, `Owner: R-[N]`, `Branch YES:`, `Branch NO:`, `Fallback: (required if above branches are not exhaustive)` -- exhaustive coverage enforced per phase |
| C-09 | Cross-Process Interaction Modeling | PASS | Pre-printed table with `Sending Phase: S-ID` format; full handoff contract: payload + acknowledgment + R-ID owner |
| C-10 | SLA and Timing Analysis | PASS | Pre-printed table with `Phase` column and `Cross-Ref (B-ID)` column; AT-RISK NOTE required below at-risk rows with bottleneck cross-reference |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2

```
composite = (5/5 * 60) + (3/3 * 30) + (2/2 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? | C-08 | C-03 guarantee |
|------|-----------|-----------|-------------|--------------|-----------|---------|------|----------------|
| 1 | V-02 Role Registry First | 5/5 | 3/3 | 2/2 | **100** | YES | Decision rule + Fallback sub-fields | Registry gate (strong) |
| 1 | V-03 Lifecycle Emphasis | 5/5 | 3/3 | 2/2 | **100** | YES | Decision supplement with fallback | Role list in PROCESS PROFILE (moderate) |
| 1 | V-04 State Table + Registry | 5/5 | 3/3 | 2/2 | **100** | YES | Decision supplement with fallback | Registry gate + table column (strong) |
| 1 | V-05 Full Synthesis | 5/5 | 3/3 | 2/2 | **100** | YES | Per-phase supplement with fallback | Registry gate + phase owner + table column (strongest) |
| 5 | V-01 State Table Only | 5/5 | 2/3 | 2/2 | **90** | YES | Type column only -- no supplement | Owner column only (weakest) |

**C-08 is the sole discriminator between V-01 and the 100 cluster.** The DECISION type column in V-01's state table encourages labeled exits but does not structurally require an exhaustive outcome set with an explicit fallback branch.

---

## Structural Guarantee Ranking

Within the 100-scoring cluster, structural reliability differs:

| Strength | Variations | Why |
|----------|-----------|-----|
| Strongest | V-05 | Three C-03 surfaces; per-phase decision supplement; per-phase terminal chaining; phase-sourced bottleneck traceability |
| Strong | V-04 | Registry checklist gate + table column for C-03; decision supplement with explicit fallback; AT-RISK cross-ref column |
| Strong | V-02 | Registry gate for C-03; explicit Decision rule + Fallback sub-fields; SLA Bottleneck Cross-Ref column |
| Moderate | V-03 | Phase sections improve C-02 exception specificity; decision supplement with fallback; C-03 relies on role-list hint, not registry gate |

V-03's score reflects design intent. In live runs, C-03 carries a higher generic-name failure probability than V-02/V-04/V-05 because no registry gate blocks generic role names at the point of entry.

---

## Excellence Signals -- Round 1

### E-1: Decision supplement block with explicit fallback is necessary for C-08

V-01 demonstrates the failure mode clearly: a DECISION-type column annotation and exits format are not sufficient for C-08. The rubric requires "exhaustive outcome branches including a fallback branch." Without a dedicated supplement block that labels the fallback as required, the model can produce technically correct-looking exits without covering the implicit "else" path. V-02, V-03, V-04, and V-05 all include a dedicated decision supplement with an explicit fallback field -- and all four pass C-08 unconditionally.

**Pattern: C-08 requires a named decision supplement section, not just a type annotation.**

### E-2: Role registry gate closes the C-03 generic-name failure mode structurally

The critical difference between V-01/V-03 (moderate C-03 risk) and V-02/V-04/V-05 (low C-03 risk) is the registry gate with checklist. Without the gate, a model processing mid-flow can default to "Approver" or "Manager" at a decision point without structural feedback. With the registry gate, the failure is surfaced as a blank checklist item before any state is written. V-05's triple-surface enforcement (gate + phase owner + table column) makes C-03 failure mechanically unavoidable to miss.

**Pattern: Role registry gate with explicit checklist prevents C-03 failure more reliably than column hints or role-list suggestions.**

### E-3: Phase-section framing improves C-02 exception trace specificity without extra instruction

V-03 and V-05's per-phase exception traces are more likely to be process-specific because the phase provides contextual scope for what failure modes are realistic at each stage. V-01's flat exception table provides no such context -- exceptions can be generic cross-process failures rather than phase-specific events. This improvement is structural: phase scope narrows the generation space without requiring additional instructions.

**Pattern: Phase-contained exception traces produce higher C-02 specificity by narrowing failure-mode generation scope to phase context.**

### E-4: SLA cross-reference column creates a coherent risk evidence chain

V-02, V-04, and V-05 include a `Cross-Ref (B-ID)` column in the SLA table that links at-risk timing entries back to identified bottlenecks. This creates a closed evidence chain: bottleneck (B-ID) -> timing risk (SLA table) -> downstream impact (B-ID Downstream Impact field). V-01 and V-03 both have SLA sections but lack this cross-reference, leaving timing risk disconnected from bottleneck causation.

**Pattern: SLA-to-bottleneck cross-reference column elevates C-10 from timing annotation to integrated risk narrative.**

---

## C-08 Failure Analysis

V-01 fails C-08 as a consequence of its single-axis design:

| Design element | C-08 coverage | Why insufficient |
|---------------|---------------|-----------------|
| DECISION type in Type column | Signals this is a decision state | Does not require exhaustive outcomes |
| Exits format `[condition] -> S-[ID]` | Multiple exits possible | Does not require fallback for unhandled conditions |
| No supplement block | No dedicated section | No structural location requiring fallback |

The fix is not instruction phrasing -- it is a structural supplement block. V-01 would need a `Decision point supplement:` section (as in V-02/V-04/V-05) to pass C-08 reliably.

**For V-01 in R2**: If carried forward, add a decision point supplement block below the state table.

---

## Round 1 Findings

### F-01: C-08 is the rubric's sharpest discriminator at the single-axis level

All five variations score identically on C-01 through C-07 and C-09 through C-10. C-08 alone separates V-01 from the 100 cluster. This confirms that decision point explicitness requires a dedicated structural section; format columns alone are insufficient.

### F-02: V-05 vs V-04 open question is not resolvable through template scoring

Both V-05 and V-04 achieve 100 with strong structural guarantees. The design notes' open question -- "does phase-section framing produce more process-specific exception traces (C-02) and edge cases (C-07)?" -- cannot be answered by rubric scoring alone. It requires live model runs against the same process topic.

### F-03: V-03's role-list approach is a lower-confidence path to C-03

V-03 passes C-03 but carries higher structural risk than V-02/V-04/V-05. The PROCESS PROFILE role list is a hint, not a gate. For future single-axis role experiments, the registry gate pattern should be the baseline.

### F-04: All five variations achieve golden threshold

The golden threshold (composite >= 80, all essential pass) is non-discriminating at Round 1. Discrimination lives at C-08 (structural supplement) and within-100 structural strength on C-03 and C-10 cross-referencing.

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate:
- All three axes combine without contradiction
- C-03 triple-surface enforcement eliminates the generic-name failure mode
- Per-phase decision supplement is the strongest C-08 enforcement
- Per-phase terminal chaining via `Phase end:` closes all paths explicitly
- SLA cross-reference column creates a closed evidence chain with bottleneck findings

**V-04** is the closest structural competitor. Key open question: does V-05's phase overhead produce measurably better output on a live P2P or L2O topic?

**V-01** should carry a decision supplement block into R2 to close C-08.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Decision supplement block with explicit fallback field is necessary for C-08 pass; DECISION type column annotation and exits format alone are structurally insufficient for exhaustive outcome coverage", "Role registry gate with explicit checklist prevents C-03 generic-name failure more reliably than column hints or role-list suggestions in a PROCESS PROFILE section", "Phase-contained exception traces improve C-02 specificity by scoping failure-mode generation to phase context without additional instructions", "SLA-to-bottleneck cross-reference column creates a closed evidence chain linking timing risk to identified bottleneck causation"]}
```
