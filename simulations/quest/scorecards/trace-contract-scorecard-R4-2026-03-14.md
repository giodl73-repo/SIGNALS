Scorecard written. Here's the summary:

---

## Round 4 Result — trace-contract

**All five variations: 100/100, Golden**

| Rank | Variation | E | R | A | Score |
|------|-----------|---|---|---|-------|
| 1 | V-01 Role sequence | 5/5 | 3/3 | 12/12 | **100** |
| 1 | V-02 Imperative form | 5/5 | 3/3 | 12/12 | **100** |
| 1 | V-03 Inertia framing | 5/5 | 3/3 | 12/12 | **100** |
| 1 | V-04 V-01 + V-02 | 5/5 | 3/3 | 12/12 | **100** |
| 1 | V-05 Full synthesis | 5/5 | 3/3 | 12/12 | **100** |

**Rubric v4 is saturated.** The ceiling is reached at Round 4. Three new patterns surface that don't yet have criteria:

1. **Per-element justification in GATE 4B** (V-05) — "each element individually justified at that level" is strictly stronger than group-level justification. C-13 and C-09 still pass on group justification; this form doesn't allow it. → Candidate C-21.

2. **CONTRACT DELTA priority annotation from Phase 4B** (V-05) — `breaking → P1, degraded → P2, cosmetic → P3` makes Phase 4B calibration load-bearing downstream. No prior variation made calibration output structurally consequential in the delta. → Candidate C-22.

3. **Inertia-specific anti-contamination in GATE 1** (V-05) — "Do not reference what you know the connector currently does" addresses a contamination path the standard two-clause isolation form (C-12/C-14) doesn't cover: expert runtime knowledge vs. actual output consultation are different paths. → Candidate C-23.

**One structural gap in V-03:** GATE 1 has 3 items (missing Spec Clause coverage for the expected table). Doesn't fail any criterion but narrows Phase 1 enforcement vs. the other four variations. → Candidate C-24.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["per-element justification requirement in GATE 4B calibration (V-05 GATE 4B item 2: each element individually justified, not group-level)", "priority annotation in CONTRACT DELTA derived from calibrated Phase 4B severity (breaking→P1, degraded→P2, cosmetic→P3)", "inertia-framing-specific anti-contamination clause in GATE 1 preventing expert connector knowledge from constraining expected table construction"]}
```
GATE 1 item 2 uses CONFIRMED/NOT CONFIRMED form with two-clause language |
| C-15 | aspirational | PASS | GATE 3 items 1-2 make blank Severity and Spec Clause cells gate failure conditions |
| C-16 | aspirational | PASS | 4-key frontmatter: gate1_isolation_confirmed, gate2_actual_complete, gate3_diff_complete, gate4b_calibration_confirmed |
| C-17 | aspirational | PASS | Expert owns element-type column at Phase 1 construction; GATE 1 item 3 + GATE 3 item 3 enforce no blank cells |
| C-18 | aspirational | PASS | "Do not merge Phase 4 and Phase 4B"; severity tally table; "CONTRACT DELTA does not begin until GATE 4B passes" |
| C-19 | aspirational | PASS | Four independent frontmatter keys; each gate mapped to its own key |
| C-20 | aspirational | PASS | GATE 3 items 1, 2, 3 cover Severity + Spec Clause + Element Type |

**Score: 5/5 + 3/3 + 12/12 = 100. Golden: YES.**

---

#### V-02: Phrasing Register — Imperative Second-Person

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | "Stop. Do not write Phase 2 until gate1_isolation_confirmed is set to true." |
| C-02 | essential | PASS | GATE 3 item 1; "Blank cells in Element Type, Severity, or Spec Clause are a gate failure condition" |
| C-03 | essential | PASS | GATE 3 item 2 |
| C-04 | essential | PASS | Phase 4 finding scaffold: root cause hypothesis sub-field required |
| C-05 | essential | PASS | CONTRACT DELTA section |
| C-06 | recommended | PASS | GATE 1 item 1: "every spec-defined element has a row — nothing omitted" |
| C-07 | recommended | PASS | Phase 4 scaffold: connector-domain mechanisms listed; "not 'unknown' alone" |
| C-08 | recommended | PASS | "name the spec amendment, schema field, API version, or auth flow step; not 'investigate further' alone" |
| C-09 | aspirational | PASS | GATE 4B item 2: "not all one level unless explicitly justified" |
| C-10 | aspirational | PASS | CONTRACT DELTA gated behind gate4b_calibration_confirmed |
| C-11 | aspirational | PASS | "Stop. Do not write root cause hypotheses anywhere in this phase. Do not explain why a field differs. Classify only. Root causes go in Phase 4. Not here." — strongest C-11 phrasing across all variations |
| C-12 | aspirational | PASS | GATE 1 item 2: two-clause isolation check |
| C-13 | aspirational | PASS | GATE 4B item 2 |
| C-14 | aspirational | PASS | CONFIRMED/NOT CONFIRMED form with two-clause language |
| C-15 | aspirational | PASS | GATE 3 items 1-2 |
| C-16 | aspirational | PASS | 4-key frontmatter |
| C-17 | aspirational | PASS | Element-type vocabulary defined; GATE 1 item 3 + GATE 3 item 3 enforce no blank cells |
| C-18 | aspirational | PASS | "Standalone — Do Not Merge with Phase 4"; severity tally; "Do not write CONTRACT DELTA until gate4b_calibration_confirmed is set to true" |
| C-19 | aspirational | PASS | 4 keys covering all 4 gates |
| C-20 | aspirational | PASS | GATE 3 items 1, 2, 3 |

**Score: 5/5 + 3/3 + 12/12 = 100. Golden: YES.**

---

#### V-03: Inertia Framing — Actual as Status-Quo Default

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | "Do not capture the inertia output until gate1_isolation_confirmed is set" |
| C-02 | essential | PASS | GATE 3 item 1: "No Severity cells blank on any gap row" |
| C-03 | essential | PASS | GATE 3 item 2: "No Spec Clause cells blank on any gap row" |
| C-04 | essential | PASS | Phase 4: "Root cause hypothesis: named connector-domain mechanism driving the inertia gap" |
| C-05 | essential | PASS | CONTRACT DELTA section |
| C-06 | recommended | PASS | GATE 1 item 1: "every spec-defined element has a row" |
| C-07 | recommended | PASS | Phase 4 scaffold: inertia terminology + six connector-domain mechanisms |
| C-08 | recommended | PASS | "specific corrective action that closes the inertia-to-contract gap; name the spec clause, schema field, or API version" |
| C-09 | aspirational | PASS | GATE 4B item 2 + "Inertia framing does not automatically justify all-breaking severity. If all findings are breaking, justify explicitly why inertia structurally violates every contract element" |
| C-10 | aspirational | PASS | CONTRACT DELTA gated behind gate4b_calibration_confirmed |
| C-11 | aspirational | PASS | Phase 3: "Do not write root causes here." GATE 3 item 4 |
| C-12 | aspirational | PASS | GATE 1 item 2: "inertia output was not referenced — not just ordered after, but not consulted at all" |
| C-13 | aspirational | PASS | GATE 4B item 2 with anti-bias framing |
| C-14 | aspirational | PASS | GATE 1 item 2 CONFIRMED/NOT CONFIRMED with two-clause form |
| C-15 | aspirational | PASS | GATE 3 items 1-2 |
| C-16 | aspirational | PASS | 4-key frontmatter |
| C-17 | aspirational | PASS | Element-type column; GATE 1 item 3 + GATE 3 item 3 enforce no blank cells |
| C-18 | aspirational | PASS | "Do not merge Phase 4 and Phase 4B. This phase runs alone." + severity tally + "CONTRACT DELTA does not begin until GATE 4B passes" |
| C-19 | aspirational | PASS | 4 independent keys |
| C-20 | aspirational | PASS | GATE 3 items 1, 2, 3 cover all three required columns |

**V-03 structural note:** GATE 1 has 3 items (completeness, isolation, element-type coverage) — missing Spec Clause coverage for the expected table. V-01/V-02/V-04/V-05 all have 4-item GATE 1s. Spec Clause enforcement in Phase 1 is instruction-level only ("No Spec Clause cell blank" as a table note). This doesn't fail any criterion because C-03 is tested at GATE 3 and C-20 tests the classification table. But it is a Phase 1 enforcement gap vs. all other variations.

**Score: 5/5 + 3/3 + 12/12 = 100. Golden: YES.**

---

#### V-04: Two-Axis Combination (V-01 + V-02)

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | Expert leads Phase 1; "Automate does not activate until gate1_isolation_confirmed is true" + STOP markers |
| C-02 | essential | PASS | GATE 3 item 1 |
| C-03 | essential | PASS | GATE 3 item 2 |
| C-04 | essential | PASS | Phase 4 finding scaffold |
| C-05 | essential | PASS | CONTRACT DELTA |
| C-06 | recommended | PASS | GATE 1 item 1 |
| C-07 | recommended | PASS | Six connector-domain mechanisms + expert taxonomy in Phase 1 |
| C-08 | recommended | PASS | "name the spec clause, schema field, API version, or auth flow step; not 'investigate further' alone" |
| C-09 | aspirational | PASS | GATE 4B item 2 |
| C-10 | aspirational | PASS | CONTRACT DELTA gated behind gate4b_calibration_confirmed |
| C-11 | aspirational | PASS | "Stop. Do not write root causes here. Root causes go in Phase 4. Not here. Classify only." |
| C-12 | aspirational | PASS | GATE 1 item 2: two-clause isolation with "not just ordered after, but not consulted at all" |
| C-13 | aspirational | PASS | GATE 4B item 2 |
| C-14 | aspirational | PASS | CONFIRMED/NOT CONFIRMED form with two-clause language |
| C-15 | aspirational | PASS | GATE 3 items 1-2 |
| C-16 | aspirational | PASS | 4-key frontmatter |
| C-17 | aspirational | PASS | Expert owns element-type column; GATE 1 item 3 + GATE 3 item 3 |
| C-18 | aspirational | PASS | "Standalone — Do Not Merge with Phase 4"; severity tally; GATE 4B gates CONTRACT DELTA |
| C-19 | aspirational | PASS | 4 independent keys |
| C-20 | aspirational | PASS | GATE 3 items 1, 2, 3 |

**Score: 5/5 + 3/3 + 12/12 = 100. Golden: YES.**

---

#### V-05: Full Synthesis (V-01 + V-02 + V-03 + All R3)

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | Expert leads Phase 1 with inertia framing; "Stop. Automate does not activate until gate1_isolation_confirmed is true" |
| C-02 | essential | PASS | GATE 3 item 1 |
| C-03 | essential | PASS | GATE 3 item 2 |
| C-04 | essential | PASS | Phase 4 scaffold with full inertia framing |
| C-05 | essential | PASS | CONTRACT DELTA with priority annotation derived from Phase 4B calibration |
| C-06 | recommended | PASS | GATE 1 item 1 |
| C-07 | recommended | PASS | Full connector-domain vocabulary; inertia framing integrates domain context throughout |
| C-08 | recommended | PASS | "specific corrective action that closes the inertia-to-contract gap; name the spec amendment, schema field, API version, or auth flow step" |
| C-09 | aspirational | PASS | Strongest anti-bias gate: "not all one level unless each element individually justified at that level; inertia framing alone is not sufficient justification" |
| C-10 | aspirational | PASS | CONTRACT DELTA with priority annotation: "breaking → P1, degraded → P2, cosmetic → P3, unless Phase 4B assessment explicitly overrides" |
| C-11 | aspirational | PASS | "Stop. Do not write root causes here. Root causes go in Phase 4. Not here." + GATE 3 item 4 |
| C-12 | aspirational | PASS | GATE 1 item 2 + "Do not reference what you know the connector currently does" (inertia-specific anti-contamination) |
| C-13 | aspirational | PASS | GATE 4B item 2 with per-element justification requirement |
| C-14 | aspirational | PASS | CONFIRMED/NOT CONFIRMED declarations with two-clause language |
| C-15 | aspirational | PASS | GATE 3 items 1-2 |
| C-16 | aspirational | PASS | 4-key frontmatter |
| C-17 | aspirational | PASS | Expert constructs element-type column at Phase 1; GATE 1 item 3 + GATE 3 item 3; inertia framing embeds domain context throughout |
| C-18 | aspirational | PASS | "Standalone — Do Not Merge with Phase 4"; severity tally; GATE 4B; "Critical: Inertia framing is not automatic justification for uniform breaking severity. If all findings are breaking, justify explicitly why inertia structurally violates every single contract element" |
| C-19 | aspirational | PASS | 4 independent keys covering all gates |
| C-20 | aspirational | PASS | GATE 3 items 1, 2, 3 |

**V-05 distinguishing details vs. all others:**
- GATE 4B item 2: per-element justification ("each element individually justified") — stricter than group-level used in V-01/V-02/V-04
- CONTRACT DELTA priority annotation: Phase 4B calibration directly drives amendment priority ordering
- Phase 1: additional anti-contamination clause ("Do not reference what you know the connector currently does") prevents inertia-framing context from priming the expected table toward what the connector can reach

**Score: 5/5 + 3/3 + 12/12 = 100. Golden: YES.**

---

### Within-100 Structural Distinctions

The rubric ceiling is reached by all five variations. Structural differences not yet captured by criteria:

| Signal | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------|------|------|------|------|------|
| GATE 1 item count | 4 | 4 | **3** | 4 | 4 |
| GATE 4B anti-bias strength | basic | basic | explicit | basic | **per-element** |
| CONTRACT DELTA priority annotation | none | none | none | none | **YES** |
| Phase 1 inertia anti-contamination clause | none | none | partial | none | **YES** |
| C-11 STOP phrasing strength | moderate | **strongest** | moderate | strong | strong |

V-03 is the only variation with a 3-item GATE 1 (missing Spec Clause coverage for the expected table). All others enforce Spec Clause completeness at gate level in Phase 1. This is a structural enforcement gap in V-03 that doesn't fail any criterion but represents narrower Phase 1 completeness control.

---

### New Patterns (Round 4 Excellence Signals)

**Pattern 1 — Per-element justification in GATE 4B (V-05)**
V-05 GATE 4B item 2: "not all one level unless each element individually justified at that level; inertia framing alone is not sufficient justification." Group-level justification ("the connector is far from spec, so most are breaking") can still pass C-13. Per-element cannot. This is the strictest form of C-13/C-09 enforcement produced across all rounds. Candidate criterion: C-21.

**Pattern 2 — Priority annotation in CONTRACT DELTA derived from calibrated Phase 4B severity (V-05)**
`*(Priority reflects calibrated severity from Phase 4B: breaking → P1, degraded → P2, cosmetic → P3, unless Phase 4B assessment explicitly overrides.)*` closes the loop between Phase 4B calibration and the amendment workflow. Phase 4B output becomes load-bearing: severity calibration directly drives amendment prioritization in the delta. No prior variation produces a CONTRACT DELTA where Phase 4B calibration has structural consequences downstream. Candidate criterion: C-22.

**Pattern 3 — Inertia-framing-specific anti-contamination clause in GATE 1 (V-05)**
"Do not reference what you know the connector currently does" addresses a contamination path specific to inertia framing: an expert who knows the connector's default behavior may unconsciously constrain the expected table to "what inertia can reach." The standard two-clause form (C-12/C-14) tests whether the actual output was consulted; this clause tests whether the expert's runtime knowledge was consulted. These are different contamination paths. Candidate criterion: C-23.

---

### Rubric Ceiling Assessment

All five variations score 100 under v4. The rubric is saturated for Round 4 designs. Candidate v5 criteria:

| ID | Name | Source | Distinguishes |
|----|------|--------|---------------|
| C-21 | Per-element justification in GATE 4B calibration | V-05 | V-05 vs. V-01/V-02/V-03/V-04 |
| C-22 | CONTRACT DELTA priority annotation from Phase 4B | V-05 | V-05 vs. all others |
| C-23 | Inertia-specific anti-contamination in GATE 1 | V-05 | V-05 vs. all others |
| C-24 | Spec Clause coverage enforced at GATE 1 level | V-01/V-02/V-04/V-05 | Flags V-03 GATE 1 gap |
