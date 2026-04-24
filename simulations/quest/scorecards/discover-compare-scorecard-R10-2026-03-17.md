## discover-compare R10 Scorecard — Rubric v8

### Criterion-by-Criterion Evaluation

---

#### V-01 — v8 Ceiling Reference (R9 V-04 body unchanged)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Bilateral dimensions | **PASS** | FEAS-A/B, INERT-A/B, RISK-A/B, COMP-A/B all declared as named tokens |
| C-02 | Independent inertia | **PASS** | Separate INERT-A and INERT-B phases each with own TOKEN RECALL + FAULT |
| C-03 | Decision matrix | **PASS** | Table with Option 0 / A / B columns assembled from LEDGER GATE |
| C-04 | Explicit recommendation | **PASS** | `**Recommendation: Option A / B / Neither / Conditional on {X}**` slot |
| C-05 | Build/no-build gate | **PASS** | "If INERT-A = HIGH and INERT-B = HIGH: state 'Build neither is a candidate recommendation.'" |
| C-06 | Differentiated risk | **PASS** | RISK-B slot: "Distinct from RISK-A or explain overlap" |
| C-07 | Actionable AMEND | **PASS** | Three concrete paths with slot structures: Add Option C, Weight dimension, Override register |
| C-08 | Option 0 in matrix | **PASS** | `Option 0: ANCHOR[0]` named column in table |
| C-09 | Audience register calibrated | **PASS** | REG token drives framing throughout + routing block redirects output order by register |
| C-10 | Token ledger cross-check | **PASS** | LEDGER GATE enumerates all 10 tokens; "Assemble from LEDGER GATE tokens" at matrix |
| C-11 | Explicit exclusion rule | **PASS** | "FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error." at each inertia phase |
| C-12 | Named anchor before analysis | **PASS** | `ANCHOR[0]` declared via token slot + section divider before FEAS-A/B phases |
| C-13 | Verbatim anchor recall | **PASS** | TOKEN RECALL with "reproduce exact sentence from above -- do not paraphrase" co-located at both inertia phases |
| C-14 | Failure class co-located | **PASS** | FAULT: label appears co-located with TOKEN RECALL at each inertia phase |
| C-15 | Register before anchor | **PASS** | REG token slot precedes ANCHOR[0] token slot in body |
| C-16 | Blocking ledger gate | **PASS** | "**HALT -- do not proceed if any token is absent.**" |
| C-17 | Output compressed | **PASS** | Pure directives throughout — token declarations, recall instructions, FAULT prohibitions, HALT gates; no explanatory tables or rationale prose |
| C-18 | Dual-polarity FAULT | **PASS** | "compare against ANCHOR[0] only" (positive mandate) + "Option A vs Option B comparison is an error" (negative prohibition) in one line |
| C-19 | AMEND self-contained | **PASS** | All three AMEND paths carry inline TOKEN RECALL + FAULT directives |
| C-20 | Path-scoped TOKEN RECALL | **PASS** | Add-C: ANCHOR[0] only; Weight: ANCHOR[0] only; Override: REG only — no over-recall, no under-recall |
| C-21 | FAULT propagates to AMEND | **PASS** | Each AMEND path carries dual-polarity FAULT: positive mandate + negative prohibition in one line |
| C-22 | Phase structure by token positioning | **PASS** | Section dividers (---) + operative token positions establish phase boundaries; removing section labels would not collapse phases |
| C-23 | Exec leads with recommendation | **PASS** | Routing block: "if REG = exec, produce RECOMMENDATION first, then DECISION MATRIX" — explicit exec-branch instruction |
| C-24 | AMEND path sub-ledgers | **PASS** | All three paths enumerate required tokens by name in mini-ledger before HALT instruction |
| C-25 | Register-gated routing block | **PASS** | "if REG = exec, RECOMMENDATION first, then DECISION MATRIX. If REG = engineering or general, DECISION MATRIX first, then RECOMMENDATION." — both branches, single conditional construct, before output sections |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 18/18 = 10.00 | **Composite: 100.00** | Golden: YES

---

#### V-02 — Exec-Only Routing Branch

Routing block: `Routing: if REG = exec, produce RECOMMENDATION first, then DECISION MATRIX.` Engineering/general branch absent.

| ID | Delta from V-01 | Result | Evidence |
|----|-----------------|--------|----------|
| C-23 | | **PASS** | Exec branch is explicit in routing block — "if REG = exec, produce RECOMMENDATION first" — unambiguous regardless of absent engineering branch |
| C-25 | CHANGE | **PARTIAL** | One register value (exec) covered; engineering/general branch absent from routing construct — "one register value... = partial" per rubric |
| All others | Identical | **PASS** | All token structures, AMEND paths, FAULT forms, ledger gates preserved unchanged |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 17.5/18 = 9.72 | **Composite: 99.72** | Golden: NO

---

#### V-03 — Engineering-Only Routing Branch

Routing block: `Routing: if REG = engineering or general, produce DECISION MATRIX first, then RECOMMENDATION.` Exec branch absent.

**C-23 ruling**: C-23 criterion reads effective output position — "when REG = exec, the recommendation token appears before the decision matrix in the output." In V-03, the RECOMMENDATION section appears before DECISION MATRIX in the prompt body. With no exec-branch routing override, exec-register execution follows body section order: RECOMMENDATION first. Effective exec output is recommendation-first. C-23 PASS via positional ordering. This confirms C-23 is routing-construct-independent.

| ID | Delta from V-01 | Result | Evidence |
|----|-----------------|--------|----------|
| C-23 | Open question resolved | **PASS** | Exec-register output follows body section order (RECOMMENDATION before DECISION MATRIX); positional ordering satisfies C-23 independently of routing construct |
| C-25 | CHANGE | **PARTIAL** | One register value (engineering/general) covered; exec branch absent — same PARTIAL band as V-02 regardless of which branch is present |
| All others | Identical | **PASS** | All token structures preserved |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 17.5/18 = 9.72 | **Composite: 99.72** | Golden: NO

*C-23/C-25 coupling resolved: C-23 does NOT require explicit exec-branch routing. A partial routing block (engineering-only) leaves exec ordering determined by body section position, which independently satisfies C-23. C-23 and C-25 are orthogonal — C-25 PARTIAL does not create a C-23 gap.*

---

#### V-04 — Prose-Expressed Routing

Routing instruction: "For exec audiences, lead with the recommendation before presenting the decision matrix. For engineering and general audiences, lead with the decision matrix before the recommendation."

Both register values present. Natural-language sentences, no if/then conditional construct.

| ID | Delta from V-01 | Result | Evidence |
|----|-----------------|--------|----------|
| C-23 | | **PASS** | Exec instruction explicit in prose: "lead with the recommendation before presenting the decision matrix" |
| C-25 | CHANGE | **PARTIAL** | Both register values covered but "handled ad-hoc in prose rather than as a unified conditional construct = partial" per rubric |
| All others | Identical | **PASS** | All token structures preserved |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 17.5/18 = 9.72 | **Composite: 99.72** | Golden: NO

*Prose boundary confirmed: two-branch coverage in prose sentences does not satisfy C-25 PASS. The criterion requires a unified conditional construct (`if/then` form), not prose-expressed equivalents.*

---

#### V-05 — No Routing Construct (C-25 Fail Baseline)

No routing block. Recommendation content precedes matrix content in body (always-first ordering, no section labels).

| ID | Delta from V-01 | Result | Evidence |
|----|-----------------|--------|----------|
| C-23 | | **PASS** | Recommendation always precedes matrix in output regardless of register — R9 V-01 confirmed always-first is C-23 PASS |
| C-25 | CHANGE | **FAIL** | No routing construct of any kind present — "No register-gated routing construct = fail" per rubric |
| C-22 | | **PASS** | No section labels present; phase separation via operative token positions and section dividers (---) — structure is already label-independent |
| All others | Identical | **PASS** | All token structures, AMEND paths, FAULT forms preserved |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 17/18 = 9.44 | **Composite: 99.44** | Golden: NO

*C-25 penalty quantified: FAIL vs PASS = 17/18 vs 18/18 = delta of 0.56 composite points (9.44 vs 10.00 on the aspirational band, applied at 10% weight).*

---

### Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| **V-01** | 4/4 = 60.00 | 3/3 = 30.00 | **18/18 = 10.00** | **100.00** | YES |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 17.5/18 = 9.72 | 99.72 | NO |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 17.5/18 = 9.72 | 99.72 | NO |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 17.5/18 = 9.72 | 99.72 | NO |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 17/18 = 9.44 | 99.44 | NO |

**Rank**: V-01 > V-02 = V-03 = V-04 > V-05

---

### Excellence Signals (V-01)

**Pattern: register-gated-routing-both-branches** — The winning form places a single `if/then` conditional routing construct covering both register values (`exec->reco-first, engineering/general->matrix-first`) immediately before the output sections. This single mechanism satisfies C-25 PASS and C-23 PASS simultaneously. The construct is orthogonal to all other criteria; no other directive needs to change to accommodate it. Form: `if REG = exec, produce RECOMMENDATION first, then DECISION MATRIX. If REG = engineering or general, produce DECISION MATRIX first, then RECOMMENDATION.`

---

### New Patterns from R10

**1. c23-positional-independence** — C-23 fires on effective exec output position, not on routing construct presence or completeness. A partial routing block (engineering-only, V-03) leaves exec ordering determined by body section order (RECOMMENDATION precedes DECISION MATRIX in body). That positional ordering satisfies C-23 independently. C-23 is routing-construct-independent: C-25 PARTIAL does not create a C-23 gap. Confirmed V-03 C-23 PASS = V-02 C-23 PASS.

**2. c25-partial-form-agnostic** — C-25 PARTIAL is a flat band. Three structurally distinct partial forms score identically at 17.5/18: exec-only routing (V-02), engineering-only routing (V-03), and two-branch prose (V-04). The PARTIAL band does not sub-grade by how close the form is to PASS, which branch is present, or how many register values are covered by the partial construct. The only exit from PARTIAL is both branches in a single conditional construct.

---

### Projected vs Actual

| Variation | Projected | Actual | Delta | C-23 Open Question |
|-----------|-----------|--------|-------|-------------------|
| V-01 | 100.00 | **100.00** | 0 | n/a |
| V-02 | 99.72 | **99.72** | 0 | PASS (predicted) |
| V-03 | 99.72 or 99.44 | **99.72** | 0 | **Resolved: PASS** — C-23 reads output position |
| V-04 | 99.72 | **99.72** | 0 | n/a |
| V-05 | 99.44 | **99.44** | 0 | n/a |

All projections confirmed. V-03 C-23 resolves to PASS via positional ordering — C-23 is routing-construct-independent.

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["c23-positional-independence", "c25-partial-form-agnostic"]}
```
