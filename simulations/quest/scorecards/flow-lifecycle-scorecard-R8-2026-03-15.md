# flow-lifecycle — Round 8 / Rubric v8 Scoring

## Criterion-by-Criterion Evaluation

### Essential Criteria — All Variations

All five variations share the same structural backbone: Role Registry (or equivalent), Phase Map, State Trace (≥6 states, entry/exit per state), Exception Catalog (≥3, trigger/deviation/terminal), Terminal Declaration (success + failure/cancel), Bottleneck Register (≥2, cause + downstream impact), Gap Register (≥1 gap with why-required and risk-if-absent), and domain-qualified roles with decision gate ownership.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 State Transition Coverage | PASS | PASS | PASS | PASS | PASS |
| C-02 Exception Flow Traces | PASS | PASS | PASS | PASS | PASS |
| C-03 Terminal State Completeness | PASS | PASS | PASS | PASS | PASS |
| C-04 Bottleneck and Gap Identification | PASS | PASS | PASS | PASS | PASS |
| C-05 Domain Role Assignment | PASS | PASS | PASS | PASS | PASS |

**Essential: 5/5 all variations.**

---

### Recommended Criteria — All Variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-06 Parallel Path Modeling | PASS | PASS | PASS | PASS | PASS |
| C-07 Decision Point Explicitness | PASS | PASS | PASS | PASS | PASS |
| C-08 Edge Case Enumeration | PASS | PASS | PASS | PASS | PASS |

**Recommended: 3/3 all variations.**

---

### Aspirational Criteria (C-09–C-28) — Per Variation

**C-09 Cross-Lifecycle Dependencies**: All variations include a Cross-Lifecycle Handoff step with trigger, recipient, fields, and acceptance condition. **PASS all.**

**C-10 SLA and Timing Annotation**: All variations include Table 8a (≥3 rows, at-risk flagging with causal reference) and breach verdict table. **PASS all.**

**C-11 Role-First Anchoring** (concrete domain-title example required):
- **V-01 PASS**: Lifecycle Context Declaration lists positive vocabulary per class: "Account Executive, Sales Operations Analyst, Revenue Recognition Specialist, Deal Desk Manager" etc. — concrete domain titles before Step 1 opens.
- **V-02 FAIL**: Role Name column header reads `"Approver" / "Admin" / "User" do not count` — only negative examples; no concrete passing title like "Senior Credit Analyst" provided anywhere.
- **V-03 FAIL**: Role Registry column is bare `Role Name (domain-qualified)` with text note saying generic labels fail — no positive domain-title example.
- **V-04 PASS**: Lifecycle Context Declaration (same as V-01 axis) provides class-specific positive vocabulary.
- **V-05 PASS**: AS-IS ANCHOR for Step 1 names concrete passing titles: *"A passing response names the process function the lifecycle actually uses: 'Accounts Payable Supervisor,' 'Deal Desk Manager,' 'Tax Provision Analyst.'"*

**C-12 Anti-Pattern Negation**: All variations provide concrete counter-examples. V-01/V-03/V-04 use FIELD CONTENT RULES block with "Does NOT qualify — example fail" column. V-02/V-05 use column headers and AS-IS anchors. **PASS all.**

**C-13 Sequential Gate Locking**: All variations have explicit dependency gates referencing the criterion they protect (Role Registry → Phase Map, Phase Map → State Trace, etc.). **PASS all.**

**C-14 Terminal Verification Pass**: All scan tables include a row verifying every traced path (S-ID and E-ID) ends at a named T-ID — per-path structural confirmation, not a count check. **PASS all.**

**C-15 Decision Fallback Coverage**: All variations include a Fallback column in Decision Points with mechanism-impairment language (V-02/V-05: `"escalate" alone does not count`; V-01/V-03/V-04: "fallback path" required). **PASS all.**

**C-16 Phase-Layer Structural Framing** (requires phases aggregate ≥2 states each, not 1:1):
- All variations have phase tables above state trace with entry trigger, completion condition, SLA envelope.
- V-03/V-04 additionally include SLA Risk Declaration blocks linking at-risk phases to anticipated bottlenecks (stronger causal bottleneck annotation).
- V-05 has inline At-Risk Bottleneck column in Phase Map headers.
- **Gap in all**: No variation explicitly enforces "phases aggregate ≥2 states each (not 1:1)."
- **PARTIAL (0.5) all variations.** V-03/V-04/V-05 are marginally stronger on the SLA-risk-to-bottleneck linkage but none cross to full pass.

**C-17 Quantified Decision Boundaries** (specific measurable threshold types named):
- **V-02 PASS**: Decision Condition column header: `measurable threshold (dollar amount, day count, retry count); qualitative condition alone does not count` — explicitly enumerates the threshold types.
- **V-05 PASS**: AS-IS ANCHOR for Decision Points: *"A passing condition names a measurable threshold (e.g., 'Order value > $25,000')"* — concrete dollar-amount example.
- **V-01 PARTIAL (0.5)**: Column label says "(measurable threshold)" — present but no specific threshold types or inline fail-language.
- **V-03 PARTIAL (0.5)**: Same as V-01.
- **V-04 PARTIAL (0.5)**: Same as V-01/V-03.

**C-18 Schema-Inline Anti-Pattern Placement** (≥2 anti-pattern rules in column headers using "does not count," "Mandatory," or "is a fail"):
- **V-02 PASS**: Maximum schema density — every column header carries fail-language: `"process begins" does not count`, `"work is done" does not count`, `"as soon as possible" does not count`, `qualitative condition alone does not count`, `"escalate" alone does not count`, etc. Well over ≥2.
- **V-05 PASS**: Same as V-02 axis for column headers: `generic labels (Approver, Manager, User, Admin) are a fail`, `"process starts" does not count`, `"phase is done" does not count`, `"large amount" does not count`, etc. Well over ≥2.
- **V-01 FAIL**: Most constraints live in the FIELD CONTENT RULES preamble block. Only the Handler column header carries inline fail-language (1 instance — satisfies C-26/C-28 but not C-18's ≥2 requirement).
- **V-03 FAIL**: Same as V-01 — FIELD CONTENT RULES preamble; only Handler inline.
- **V-04 FAIL**: Same as V-01/V-03.

**C-19 Artifact-Level Production Gate**: All variations have an explicit production gate blocking artifact write until all Scan Summary rows are CLOSED. **PASS all.**

**C-20 Per-Step Sequential Gate Coverage** (≥3 gates distributed across full schema):
- V-01: GATE 0 (lifecycle context → role registry), GATE A (role registry → phase map), GATE B (phase map → state trace), production gate. 4 gates. **PASS.**
- V-02: GATE A (role registry → phase map), GATE B (phase map → state trace), GATE C (exception catalog → terminal declaration), production gate. 4 gates. **PASS.**
- V-03: GATE A (phase map → role registry), GATE B (role registry → state trace), production gate. 3 gates. Minimum met. **PASS.**
- V-04: GATE 0 (lifecycle context → phase map), GATE A (phase map → role registry), GATE B (role registry → state trace), production gate. 4 gates. **PASS.**
- V-05: GATE A (role registry → phase map), GATE B (phase map → state trace), GATE C (state trace/decisions → exception catalog), GATE D (exception catalog → terminal declaration), production gate. 5 gates — highest gate density. **PASS.**

**C-21 Exception Flow Handling Role**: All variations assign Handler (R-ID) in the Exception Catalog, traced to Role Registry. **PASS all.**

**C-22 Production Gate Failure Declaration**: All gates include "is a structural fail" inline. **PASS all.**

**C-23 Exception Handler Authority Pre-Certification**: All variations include Exception Handler (Y/N) column in Role Registry with rule that N roles may not appear in Handler cells. **PASS all.**

**C-24 Gate Violation Remediation Instruction**: All gates include "must be discarded and rebuilt from the failing step." **PASS all.**

**C-25 Gate Failure Causal Mechanism**: All production gates name the structural defect the violating artifact carries (inline enumeration of defect types). **PASS all.**

**C-26 Exception Authority Inline Schema Enforcement**: All Handler column headers contain the backward-trace rule at point of use. **PASS all.**

**C-27 Scan-Table Defect Taxonomy**: All variations have a "Defect Type if OPEN" column in the scan table; all production gate sentences reference "the Defect Type column" by name and enumerate ≥3 defect categories:
- V-01: 5 categories (unanchored role, generic role, uncertified exception handler, unterminated path, breach analysis disconnected from SLA evidence)
- V-02: 5 categories
- V-03: 5 categories
- V-04: 6 categories (adds unresolvable phase boundary, unanchored roles)
- V-05: 5 categories

**PASS all.**

**C-28 Handler Authority Fail-Declaration Co-Location**: All Handler column headers contain both the backward-trace rule and `Mandatory; blank or uncertified role is a fail` at the same header cell. **PASS all.**

---

### Aspirational Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-10 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-11 | 1.0 | **0** | **0** | 1.0 | 1.0 |
| C-12 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-13 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-14 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-15 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-16 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| C-17 | 0.5 | **1.0** | 0.5 | 0.5 | **1.0** |
| C-18 | **0** | **1.0** | **0** | **0** | **1.0** |
| C-19 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-20 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-21 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-22 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-23 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-24 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-25 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-26 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-27 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-28 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| **Total** | **18.0** | **18.5** | **17.0** | **18.0** | **19.5** |

---

## Composite Scores

```
formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/20 * 10)
```

| Variation | Essential | Recommended | Aspirational | Score |
|-----------|-----------|-------------|--------------|-------|
| V-01 Role Sequence | 5/5 → 60 | 3/3 → 30 | 18.0/20 → 9.0 | **99.0** |
| V-02 Max Schema Density | 5/5 → 60 | 3/3 → 30 | 18.5/20 → 9.25 | **99.25** |
| V-03 Phase-First | 5/5 → 60 | 3/3 → 30 | 17.0/20 → 8.5 | **98.5** |
| V-04 Role Seq + Phase-First | 5/5 → 60 | 3/3 → 30 | 18.0/20 → 9.0 | **99.0** |
| V-05 Max Density + AS-IS | 5/5 → 60 | 3/3 → 30 | 19.5/20 → 9.75 | **99.75** |

**Ranking: V-05 > V-02 > V-01 = V-04 > V-03**

All variations exceed the golden threshold (all essential pass + composite ≥ 80).

---

## Excellence Signals from V-05

V-05 scores higher than V-02 (its closest competitor) on C-11 and C-17. Both pass C-18. The distinguishing mechanism is the **AS-IS ANCHOR**.

**Signal 1 — AS-IS ANCHOR provides positive-vocabulary anchoring where column headers cannot**

V-02 achieves maximum inline fail-language but fails C-11. Its Role Name column reads `"Approver" / "Admin" / "User" do not count` — it names the forbidden patterns but never shows what a correct domain title looks like. An author who doesn't already know what "domain-qualified" means is told what fails, not what passes.

V-05's AS-IS ANCHOR for Step 1 names *"Accounts Payable Supervisor," "Deal Desk Manager," "Tax Provision Analyst"* as passing examples, explicitly contrasted with the failing examples. The positive vocabulary appears at the exact section where role titles are entered, not in a pre-step preamble block. This closes C-11 for a rubric without a lifecycle-class preamble.

The structural insight: column headers close the negative space (what fails); AS-IS anchors close the positive space (what passes). C-18 requires inline fail-language; C-11 requires a positive concrete example. A column-header-only rubric (V-02) can pass C-18 but fail C-11 because column headers are better suited to declaring failures than to exemplifying the correct vocabulary.

**Signal 2 — AS-IS ANCHOR for decision points provides a specific threshold example that activates C-17**

V-02 passes C-17 by enumerating threshold types in the column header: `(dollar amount, day count, retry count)`. V-05 passes C-17 by a different mechanism — the AS-IS ANCHOR names a concrete threshold value: *"A passing condition names a measurable threshold (e.g., 'Order value > $25,000')."* The column header in V-05 only says `measurable threshold required; "large amount" does not count` — without the AS-IS anchor, V-05 would be PARTIAL on C-17 (like V-01/V-03/V-04). The AS-IS anchor carries the specificity that the column header omits.

This reveals a complementary relationship: V-02 encodes the threshold taxonomy in the column header; V-05 encodes a concrete passing example in the AS-IS anchor. Both reach C-17 pass by different paths. The AS-IS anchor path is new — not previously required by any criterion.

**What's uncaptured by C-01–C-28:**

The AS-IS ANCHOR mechanism itself — a per-section prose block immediately before each section's table that presents a complete weak response at that section and a complete passing response — is not captured by any existing criterion. C-12 requires ≥1 anti-pattern with counter-example somewhere in the rubric. C-18 requires inline fail-language in column headers. Neither captures a structure where:
- Every section entry has a named failing response (complete, not just a cell value)
- Some section entries also name the corresponding passing response vocabulary
- The exemplar appears as a structural block before the table, not as a column header constraint

This is the next excellence ceiling.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Per-section AS-IS ANCHOR block: each section opens with a named complete weak response at that section before the table opens, providing full-response-level failure modeling distributed across every section entry — distinct from C-12 (≥1 anti-pattern anywhere) and C-18 (cell-level fail-language in column headers) by requiring a complete-response exemplar at the section boundary rather than a single-cell constraint", "Positive-vocabulary anchoring via AS-IS anchor: the Role Registry AS-IS anchor names concrete passing domain titles (e.g., Accounts Payable Supervisor, Deal Desk Manager) at the section entry point, closing C-11 in rubrics without a lifecycle-class preamble — column-header-only rubrics (V-02) pass C-18 but fail C-11 because column headers name what does not count but cannot anchor the vocabulary of what does count with specific functional-title examples"]}
```
