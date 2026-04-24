# campaign-simulate — Round 5 Scorecard (Rubric v4)

## Variation Summary

| Variation | Axis | Base Architecture |
|-----------|------|-------------------|
| V-01 | Axis A alone (Exception Path column in unified findings table) | R4 V-04 base |
| V-02 | Axis B alone (Blast Rationale named column) | R4 V-04 base |
| V-03 | Axis C alone (Mandatory Cross-Skill Synthesis Gate) | R4 V-04 base |
| V-04 | Axis A + Axis B | R4 V-05 full architecture |
| V-05 | Axis A + Axis B + Axis C | R4 V-05 full architecture + all three axes |

---

## Essential Criteria (60 pts)

### C-01 — All Five Sub-Skills Execute (12 pts)

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Labeled sections for all five sub-skills; distinct entity lists per skill; severity budget gate enforces trace execution before flow |
| V-02 | PASS | Same structure; five labeled sub-skill sections with budget status gates |
| V-03 | PASS | Identical five-sub-skill architecture; execution order explicit |
| V-04 | PASS | Five sub-skills with severity budget gate; flow blocked until trace gate clears |
| V-05 | PASS | Same; R4 V-05 architecture preserved intact; campaign halts if budget NOT MET without exhaustion rationale |

All five: **PASS — 12 pts each**

---

### C-02 — Findings Ranked by Blast Radius (12 pts)

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Ranked Findings section re-sorts by blast radius (system-wide first), then severity; explicit Blast Radius column in findings table |
| V-02 | PASS | Ranked Findings table with Blast Rationale column; system-wide → cross-skill → component-wide → isolated explicit sort key |
| V-03 | PASS | Ranked Findings section with Rank column and blast radius sort |
| V-04 | PASS | 12-column Ranked Findings table with Blast Radius and Blast Rationale columns |
| V-05 | PASS | Same 12-column ranked findings; "sort by blast radius (system-wide first), then severity within tier" explicit |

All five: **PASS — 12 pts each**

---

### C-03 — System Boundary and Severity per Finding (12 pts)

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | System Boundary (column 3) and Severity (column 7) in every row of 11-column unified table; no blank cells rule |
| V-02 | PASS | Same per the 10-column schema |
| V-03 | PASS | System Boundary and Severity in 10-column unified table |
| V-04 | PASS | 11-column schema; both required per row |
| V-05 | PASS | 11-column schema; both required per row; verification gate includes Severity from four-value set check |

All five: **PASS — 12 pts each**

---

### C-04 — At Least One Spec Gap or Contract Violation (12 pts)

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | `spec-gap` type available to all sub-skills in vocabulary map; trace-contract sub-skill finds "mismatches and undocumented edge case behaviors"; manifest completeness gate surfaces F-00 spec gaps |
| V-02 | PASS | Same vocabulary map; trace-contract walks boundaries for "mismatches and undocumented edge case behaviors" |
| V-03 | PASS | Same vocabulary map; cross-cutting `spec-gap` type |
| V-04 | PASS | Same; trace-contract explicitly finds contract violations; `spec-gap` is the escape type for any sub-skill |
| V-05 | PASS | Same; additionally manifest completeness gate forces F-00 sentinel for empty entity lists |

All five: **PASS — 12 pts each**

---

### C-05 — Single Synthesized Report (12 pts)

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Single unified findings table integrating all five sub-skills; Ranked Findings, Exception Path Coverage Summary, Execution Log are synthesis sections |
| V-02 | PASS | Single 10-column unified table; Ranked Findings with Blast Rationale column; one output file |
| V-03 | PASS | Single unified table; CROSS-SKILL SYNTHESIS GATE is a synthesis step; one output file |
| V-04 | PASS | Single 11-column table; integrated Ranked Findings; Cross-Skill Patterns section |
| V-05 | PASS | 19-section ordered output written to single file; no concatenation of five separate outputs |

All five: **PASS — 12 pts each**

**Essential subtotal: 60 / 60 — all variations**

---

## Recommended Criteria (30 pts)

### C-06 — Exception Paths and Edge Cases Identified (10 pts)

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Exception Path column required per row; all five sub-skills must populate it; Exception Path Coverage Summary enforces >= 2 named paths across report |
| V-02 | PASS | Entity List 4 "Exception Path Defined?" tracks per-phase; flow sub-skill instructions include "verify exception path are fully specified"; Exception Path Coverage Summary absent but vocabulary map guides edge-case types (`missing-exit-state`, `dead-end`, `loop-risk`) |
| V-03 | PASS | Entity List 4 "Exception Path Defined?"; flow-lifecycle verifies exception paths per phase; multiple edge-case type values in vocabulary map |
| V-04 | PASS | Exception Path column in 11-column table; Exception Path Coverage Summary with >= 2 minimum; trace sub-skills name caller-triggered exception paths |
| V-05 | PASS | Same as V-04 plus Exception Path in Trace Findings Brief feeds exception path context into flow sub-skills |

All five: **PASS — 10 pts each**

---

### C-07 — Findings Cross-Reference Source Sub-Skill (10 pts)

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Sub-Skill column (column 2) in unified 11-column table; all rows attributed |
| V-02 | PASS | Sub-Skill column in 10-column unified table |
| V-03 | PASS | Sub-Skill column in 10-column unified table |
| V-04 | PASS | Sub-Skill column in 11-column table |
| V-05 | PASS | Sub-Skill column in 11-column table; Execution Log also confirms attribution per sub-skill |

All five: **PASS — 10 pts each**

---

### C-08 — State Machine Anomalies Explicitly Called Out (10 pts)

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | trace-state walks Entity List 1; explicitly finds "exit-less states, early-firing transitions, unenforced invariants, unreachable states"; type vocabulary includes `unreachable-state`, `invariant-violation`, `transition-guard-missing` |
| V-02 | PASS | Same trace-state instruction and vocabulary |
| V-03 | PASS | Same trace-state instruction and vocabulary |
| V-04 | PASS | Same; severity budget gate guarantees >= 1 CRITICAL/HIGH trace-state finding |
| V-05 | PASS | Same; budget gate halts campaign if not MET without exhaustion rationale |

All five: **PASS — 10 pts each**

**Recommended subtotal: 30 / 30 — all variations**

---

## Aspirational Criteria (13 criteria × 1 pt, capped at 10)

### Criteria C-09 through C-21 — Per-Variation Detail

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Test Scenario Baseline | PASS | PASS | PASS | PASS | PASS |
| C-10 F-NN IDs | PASS | PASS | PASS | PASS | PASS |
| C-11 CRITICAL/HIGH per trace | PASS | PASS | PASS | PASS | PASS |
| C-12 Structured table, no blank cells | PASS | PASS | PASS | PASS | PASS |
| C-13 Flow references trace | PASS | PASS | PASS | PASS | PASS |
| C-14 System Boundary vocabulary | PASS | PASS | PASS | PASS | PASS |
| C-15 Universal sentinel rule | PASS | PASS | PASS | PASS | PASS |
| C-16 No-findings sentinel rows | PASS | PASS | PASS | PASS | PASS |
| C-17 Pre-output verification gate | PASS | PASS | PASS | PASS | PASS |
| C-18 Unified schema closes 4 criteria | PASS | PASS | PASS | PASS | PASS |
| C-19 Finding Type closed vocabulary | PASS | PASS | PASS | PASS | PASS |
| C-20 Blast radius rationale, top-tier | PASS | PASS | PASS | PASS | PASS |
| C-21 Exception Path in named column | PASS | **FAIL** | **FAIL** | PASS | PASS |

**Evidence notes:**

**C-20 (V-01, V-03):** Rationale appears as prose below the row ("add a blast radius rationale sentence below the row naming downstream flows"). Pass condition requires a rationale sentence exist per top-tier finding — the structural location (prose vs. column) is not tested by C-20. PASS.

**C-21 (V-02, V-03 FAIL):** V-02 unified findings table has 10 columns — no Exception Path column. Entity List 4 tracks "Exception Path Defined?" per phase but that is per-manifest-row not per-finding-row. C-21 requires a named column populated for each finding row in the findings table or entity manifest. Entity List 4 per-phase coverage does not satisfy "each finding row." V-03 has the same structure. FAIL.

**C-21 (V-01, V-04, V-05 PASS):** Exception Path is the 10th column of the 11-column unified findings table; "N/A -- [reason]" sentinel for happy-path findings; all rows must be populated. Column scan is the compliance verification path. PASS.

### Aspirational Score Summary

| Variation | Criteria Passing | Aspirational Score (capped at 10) |
|-----------|-----------------|-----------------------------------|
| V-01 | 13 / 13 | 10 |
| V-02 | 12 / 13 | 10 (cap saturated) |
| V-03 | 12 / 13 | 10 (cap saturated) |
| V-04 | 13 / 13 | 10 |
| V-05 | 13 / 13 | 10 |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60 | 30 | 10 | **100** |
| V-02 | 60 | 30 | 10 | **100** |
| V-03 | 60 | 30 | 10 | **100** |
| V-04 | 60 | 30 | 10 | **100** |
| V-05 | 60 | 30 | 10 | **100** |

All five variations: **100 / 100**. All essential criteria pass. The cap absorbs the C-21 failure in V-02 and V-03 (12 passing still saturates at 10 pts).

---

## Ranking

All variations tie at 100/100. V-05 carries the richest structural architecture (all three axes, plus Remediation Template, plus Exception Path in Trace Findings Brief). Rank by architectural completeness:

1. **V-05** — All three axes + Remediation Template + R4 V-05 full architecture (all 13 criteria pass; every compliance requirement maps to a named structural element)
2. **V-04** — Axis A + B; 13/13 aspirational; Cross-Skill Patterns section present but optional
3. **V-01** — Axis A alone; 13/13 aspirational; Exception Path column covers all five sub-skills; Trace Findings Brief includes Exception Path
4. **V-02** — Axis B alone; 12/13 aspirational (C-21 fail); Blast Rationale column is the mechanical compliance improvement
5. **V-03** — Axis C alone; 12/13 aspirational (C-21 fail); Cross-Skill Gate is the mechanical compliance improvement

---

## Excellence Signals (Patterns Beyond the v4 Rubric Ceiling)

**Pattern 1: Remediation Template closes Remediation column to a named form**

V-05 introduces a Remediation Template with action form (`[VERB] [TARGET] AT [LOCATION] TO [SPEC]`) and research form (`INVESTIGATE [question] BEFORE specifying remediation`). This applies the same structural discipline used for System Boundary (C-14) and Finding Type (C-19) to the Remediation field. The current rubric requires only "specific action at a named location" as prose guidance. The template makes Remediation compliance a copy operation from a named schema — "Fix the spec" or "add validation" become verifiable violations, not style preferences. No criterion in v4 addresses Remediation quality.

**Pattern 2: Exception Path column propagated into the Trace Findings Brief**

V-01, V-04, and V-05 extend the Trace Findings Brief schema to include Exception Path: `| F-ID | Sub-Skill | Type | Summary | Severity | Blast Radius | Exception Path |`. V-02 and V-03 use a 6-column brief without it. When flow sub-skills read the brief, they receive exception path context for each trace finding — not just severity and blast radius. This makes the trace-first execution ordering propagate exception path knowledge forward into flow simulations, producing a richer cross-phase exception path picture than the brief-without-column provides. No current criterion checks the column schema of the Trace Findings Brief.

**Pattern 3: Cross-Skill Synthesis Gate with deterministic blast radius escalation rule**

V-03 and V-05 specify a formal escalation algorithm: "if any constituent finding is system-wide → system-wide; if no constituent is system-wide but two or more are cross-skill → system-wide; otherwise promote one level above the highest constituent finding." This converts the combined blast radius from a model judgment call into a deterministic computation from the inputs. No current criterion checks the Combined Blast Radius assignment logic in the cross-skill patterns table.

**Pattern 4: Test Scenario Baseline carries Exception Path column**

V-01, V-04, and V-05 include Exception Path in the Test Scenario Baseline table: `| Scenario ID | F-ID | Severity | Exception Path | What to Exercise | Acceptance Condition |`. V-02 and V-03 omit it. When the test scenario table includes the exception path being exercised, each test scenario is traceable not just to a finding (C-09: F-ID link) but to the specific exception path the scenario must trigger. This makes test coverage of exception paths verifiable by scanning the Test Scenario Baseline rather than by reading each scenario's prose description.

---

## v5 Candidate Criteria

| ID | Proposed Criterion | Source Pattern |
|----|-------------------|----------------|
| C-22 | Remediation Template closes Remediation to action-form or research-form | R5 V-05 Pattern 1: Remediation Template |
| C-23 | Trace Findings Brief includes Exception Path column | R5 V-01/V-04/V-05 Pattern 2: Exception Path in Brief |
| C-24 | Cross-Skill Synthesis Gate includes deterministic blast radius escalation rule | R5 V-03/V-05 Pattern 3: Escalation rule |

Pattern 4 (Test Scenario Exception Path column) is a structural companion to C-22/C-23 but may not warrant a standalone criterion — it follows as a natural extension once Exception Path is a named column everywhere.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Remediation Template closes Remediation column to action-form or research-form — same prose-to-structural-column discipline as C-14/C-19, making template violations verifiable rather than stylistic", "Exception Path column propagated into Trace Findings Brief — flow sub-skills receive exception path context from trace findings, extending trace-first ordering to include exception path dimension across sub-skill boundary", "Cross-Skill Synthesis Gate includes deterministic blast radius escalation rule — converts combined blast radius from model judgment to a deterministic algorithm from constituent finding tiers", "Test Scenario Baseline carries Exception Path column — links each test scenario to the specific exception path it exercises, making test coverage of exception paths verifiable by column scan"]}
```
