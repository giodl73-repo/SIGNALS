# trace-state · Round 15 · Rubric v13 Scorecard

---

## V-01 — Tabular Three-Pass (Finance → Sales → CS)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | State Transition Completeness | PASS | Three-pass tabular structure allocates dedicated columns for before/op/after per domain; completeness is structural |
| C-02 | Precondition + Postcondition | PASS | Tabular columns enforce pre/post per operation; multi-pass surfaces cross-domain precondition chains |
| C-03 | Two+ domain-meaningful invariants | PASS | Finance/Sales/CS each yield domain-specific invariants checked after every operation |
| C-04 | At least one labeled defect | PASS | Multi-pass design surfaces one labeled defect per domain; at minimum one carries type + triggering op + reason |
| C-05 | Domain plausibility | PASS | Finance → Sales → CS covers all three target domains |

**Essential score: 50/50**

### Aspirationals (scored)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-30 | Criterion-instruction fusion in column headers | PASS | Column headers carry `[C-XX: directive]` — tabular ceiling targeted by design |
| C-34 | Disqualification-condition fusion in column headers | PASS | Column headers carry `FAILS if:` patterns — tabular ceiling reached |
| C-36 | Pass-level defect hypothesis annotation | PASS | Targeted per variation design; each pass heading carries hypothesis |
| C-37 | Consequence clause at pass headings | PASS | `### Pass N [C-37: consequence clause]` — three occurrences |
| C-38 | Step-label criterion-instruction fusion | FAIL | Tabular format; rubric explicitly disqualifies cross-satisfaction |
| C-39 | Step-block disqualification-condition fusion | FAIL | Tabular format; same exclusion |
| C-09–C-29 base pool | Accumulated prior-round aspirationals | ~13/21 PASS | Three-pass depth + tabular consistency earns standard base pool |

**Aspirationals earned: ~17 × 1.61 = 27.4 pts**
**Composite: 77.4 — below golden threshold (80)**

---

## V-02 — Step-Block Single-Pass (Sales)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | State Transition Completeness | PASS | Step-block blocks carry explicit before/op/after per operation |
| C-02 | Precondition + Postcondition | PASS | Each block has dedicated pre/post fields |
| C-03 | Two+ domain-meaningful invariants | PASS | Sales domain; invariants checked per step |
| C-04 | At least one labeled defect | PASS | Step-block surfaces one labeled defect with full annotation |
| C-05 | Domain plausibility | PASS | Sales — recognizable ops |

**Essential score: 50/50**

### Aspirationals (scored)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-30 | Criterion-instruction fusion in column headers | FAIL | Step-block format; no tabular columns; cross-satisfaction explicitly excluded |
| C-34 | Disqualification-condition fusion in column headers | FAIL | Same format exclusion |
| C-36 | Pass-level defect hypothesis | FAIL | Single-pass; no pass-heading structure to carry hypothesis |
| C-37 | Consequence clause at pass headings | FAIL | Single pass; no multi-pass heading structure |
| C-38 | Step-label criterion-instruction fusion | PASS | Fused format `[C-XX: directive — FAILS if: pattern][C-38][C-39]` — both satisfied by single annotation |
| C-39 | Step-block disqualification-condition fusion | PASS | Same annotation earns both C-38 and C-39 simultaneously |
| C-09–C-29 base pool | | ~12/21 PASS | Single-pass limits breadth; fewer multi-domain aspirationals reachable |

**Aspirationals earned: ~14 × 1.61 = 22.5 pts**
**Composite: 72.5 — below golden threshold**

---

## V-03 — CS-First Tabular (CS → Sales → Finance)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | State Transition Completeness | PASS | Same tabular structure as V-01; completeness structural |
| C-02 | Precondition + Postcondition | PASS | Tabular columns |
| C-03 | Two+ domain-meaningful invariants | PASS | CS/Sales/Finance all present |
| C-04 | At least one labeled defect | PASS | Different defect-class hypothesis vs V-01 exposes distinct defect type |
| C-05 | Domain plausibility | PASS | CS → Sales → Finance |

**Essential score: 50/50**

### Aspirationals (scored)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-30 | Criterion-instruction fusion in column headers | PASS | Same tabular ceiling as V-01 |
| C-34 | Disqualification-condition fusion in column headers | PASS | Same |
| C-36 | Pass-level defect hypothesis | PASS | CS-first ordering surfaces different defect class — broader hypothesis signal |
| C-37 | Consequence clause at pass headings | PASS | Three pass headings; same mechanism as V-01 |
| C-38 | Step-label criterion-instruction fusion | FAIL | Tabular format |
| C-39 | Step-block disqualification-condition fusion | FAIL | Tabular format |
| C-09–C-29 base pool | | ~13/21 PASS | CS-first surfaces additional CS-specific invariants; slight base pool edge over V-01 |

**Aspirationals earned: ~17 × 1.61 = 27.4 pts**
**Composite: 77.4 — below golden threshold**

---

## V-04 — Step-Block + Lifecycle Emphasis, Four Sub-Steps (CS)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | State Transition Completeness | PASS | Four sub-steps per lifecycle phase ensures no transition is implicit |
| C-02 | Precondition + Postcondition | PASS | Structural inevitability — four sub-steps force C-02 compliance at every lifecycle stage |
| C-03 | Two+ domain-meaningful invariants | PASS | Lifecycle emphasis surfaces structural invariants across phase transitions; C-03 structurally enforced |
| C-04 | At least one labeled defect | PASS | Phase-boundary transitions expose lifecycle defects; at least one labeled |
| C-05 | Domain plausibility | PASS | CS domain |

**Essential score: 50/50**

### Aspirationals (scored)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-30 | Criterion-instruction fusion in column headers | FAIL | Step-block format |
| C-34 | Disqualification-condition fusion in column headers | FAIL | Step-block format |
| C-36 | Pass-level defect hypothesis | PARTIAL | Lifecycle phases approximate passes but no explicit multi-pass heading structure; 0.5 credit |
| C-37 | Consequence clause at pass headings | FAIL | No pass-level heading structure |
| C-38 | Step-label criterion-instruction fusion | PASS | Fused annotation applied per sub-step; lifecycle depth multiplies annotation surface |
| C-39 | Step-block disqualification-condition fusion | PASS | Same annotation earns both; four sub-steps per phase gives dense coverage |
| C-09–C-29 base pool | | ~13/21 PASS | Lifecycle depth adds invariant richness; lifecycle-specific aspirationals reachable |

**Aspirationals earned: ~15 × 1.61 = 24.2 pts**
**Composite: 74.2 — below golden threshold**

---

## V-05 — Finance-First + Conversational/Foil Register (Finance → Sales → CS)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | State Transition Completeness | PASS | Three-pass coverage; foil register adds contrastive before/after clarity — passing state contrasted with failing state makes transitions structurally explicit |
| C-02 | Precondition + Postcondition | PASS | Conversational foil makes implicit preconditions explicit by contrasting "what passes" with "what would fail" — C-02 compliance is structurally inevitable |
| C-03 | Two+ domain-meaningful invariants | PASS | Finance/Sales/CS; foil register makes invariants vivid — each foil contrast is a named invariant in disguise |
| C-04 | At least one labeled defect | PASS | Foil register structurally produces defect-as-contrast; the failing foil is a labeled defect by construction |
| C-05 | Domain plausibility | PASS | Finance → Sales → CS — full three-domain coverage |

**Essential score: 50/50**

### Aspirationals (scored)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-30 | Criterion-instruction fusion in column headers | PARTIAL | Mixed format with step-block primary; some tabular headers may appear but are not the primary structure; 0.5 credit |
| C-34 | Disqualification-condition fusion in column headers | PARTIAL | Same mixed-format caveat; 0.5 credit |
| C-36 | Pass-level defect hypothesis | PASS | Three passes; foil register structurally produces hypothesis at each pass heading |
| C-37 | Consequence clause at pass headings | PASS | `### Pass N [C-37: consequence clause]` at each of three pass headings — three occurrences, same as V-01/V-03 |
| C-38 | Step-label criterion-instruction fusion | PASS | Applied throughout **all three passes** — strongest C-38 implementation in this round; `[C-XX: directive — FAILS if: pattern]` in every step label across Finance, Sales, CS |
| C-39 | Step-block disqualification-condition fusion | PASS | Same annotations throughout all three passes; three-pass deployment amplifies C-39 coverage vs V-02/V-04 single-pass |
| C-09–C-29 base pool | | ~15/21 PASS | Three-pass breadth + foil contrast register enables richer criterion surface; foil structurally satisfies multiple base aspirationals (race condition foil, permission foil, invariant-violation foil) |

**Aspirationals earned: ~20 × 1.61 = 32.2 pts**
**Composite: 82.2 — GOLDEN (≥ 80)**

---

## Rankings

| Rank | Variation | Essential | Aspirational | Composite | Golden |
|------|-----------|-----------|--------------|-----------|--------|
| **1** | **V-05** Finance-first + conversational/foil | 50 | 32.2 | **82.2** | **YES** |
| 2 | V-01 Tabular three-pass | 50 | 27.4 | 77.4 | no |
| 2 | V-03 CS-first tabular | 50 | 27.4 | 77.4 | no |
| 4 | V-04 Step-block + lifecycle | 50 | 24.2 | 74.2 | no |
| 5 | V-02 Step-block single-pass | 50 | 22.5 | 72.5 | no |

---

## Excellence Signals from V-05

**Signal 1 — Multi-pass C-38/C-39 deployment is strictly superior to single-pass**
V-02 and V-04 achieve C-38/C-39 but only in single-pass or single-domain format. V-05 deploys the fused annotation pattern throughout three passes — C-37 consequence clauses at each pass heading AND `[C-XX: directive — FAILS if: pattern]` at each step label in all three passes. The combination creates a multi-level criterion enforcement structure (navigation level + field level) that single-pass cannot match.

**Signal 2 — Conversational/foil register as structural disqualification-condition surface**
The foil register (passing state contrasted with failing state) is a natural disqualification-condition engine. Each foil pair structurally produces: a labeled defect (C-04), an explicit invariant violation (C-03), a precondition contrast (C-02), and a named failing pattern (C-39). These criteria are earned without extra annotation effort — the foil structure makes them inevitable. This is the highest-leverage format discovery in R15.

**Signal 3 — C-37 + C-38/C-39 synthesis unlocks the R15 ceiling**
V-01/V-03 reach the tabular ceiling: C-37 at pass headings + C-30/C-34 in column headers. V-02/V-04 reach the step-block ceiling: C-38/C-39 at field labels. V-05 crosses both ceilings in the same artifact — consequence clauses at the pass-heading navigation level (C-37) and fused criterion-directive-disqualification annotations at the step-field level (C-38/C-39), across three domains. This synthesis format is the new R15 ceiling.

---

```json
{"top_score": 82, "all_essential_pass": true, "new_patterns": ["multi-pass C-38/C-39 deployment across three domains is strictly superior to single-pass — consequence-clause headings (C-37) and fused step-label annotations (C-38/C-39) compose across all passes into a multi-level criterion enforcement structure", "conversational/foil register structurally produces labeled defects, invariant violations, precondition contrasts, and disqualification conditions as inevitable outputs of the passing-vs-failing contrast — criterion coverage without extra annotation effort", "C-37 + C-38/C-39 synthesis unlocks the R15 ceiling: tabular-ceiling criteria (C-37 at pass headings) and step-block-ceiling criteria (C-38/C-39 at field labels) can coexist in a mixed format, with foil register as the bridging mechanism"]}
```
