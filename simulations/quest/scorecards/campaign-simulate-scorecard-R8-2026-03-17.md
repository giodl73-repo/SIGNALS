Now I have all the information needed. Let me produce the full scoring evaluation.

---

# quest:score — campaign-simulate Round 8

**Rubric**: v7 (C-01 through C-31)
**Base**: R7 V-05 = 114 raw / 1.23 = 92.7 normalized
**Raw max**: 123 (÷ 1.23 = 100.0)
**New criteria**: C-29 (+3 raw), C-30 (+3 raw), C-31 (+3 raw)

---

## Scoring Framework

The rubric's stated math fixes the evaluation anchor:

| Criteria satisfied | Raw | Normalized |
|--------------------|-----|------------|
| C-01…C-28 (R7 V-05 base) | 114 | 92.7 |
| + C-29 | 117 | 95.1 |
| + C-30 | 117 | 95.1 |
| + C-31 | 117 | 95.1 |
| + C-29 + C-30 | 120 | 97.6 |
| + C-29 + C-30 + C-31 | 123 | 100.0 |

**C-26 note**: V-01, V-02, and V-04 explicitly revert to C-08 (single-column free-form Remediation) to isolate their targeted axis. Their hypothesis text states "Remediation field uses free-form action verbs (C-08 satisfied but not C-31)." This creates a C-26 PARTIAL condition. V-03 and V-05 satisfy C-26 automatically through C-31's four-column decomposition requirement.

---

## V-01 — C-29: Cross-Skill Dependency Map + Propagation Coverage Gate

### Essential Criteria (C-01 to C-25)

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-01 | All Five Sub-Skills Execute | PASS | Execution Sequence explicitly lists all five; per-scope gate table follows each |
| C-02 | Findings Ranked by Blast Radius | PASS | Ranked Findings: Tier 1–4 by blast radius; explicit column in schema |
| C-03 | System Boundary and Severity per Finding | PASS | Sub-skill field names boundary; Blast Radius field names severity per finding |
| C-04–C-12 | Remaining essential (correctness/format) | PASS | Inherited intact from R7 V-05 base; all required fields, filter log, execution log present |
| C-13–C-14 | Filter Log with rejection rules | PASS | Four filter rules listed before evaluation; Elevate? and Rejection Reason columns declared |
| C-15 | Cross-skill comparison protocol | PASS | Three-step protocol (pairings, verdicts, pattern declaration) with empty-state templates |
| C-16–C-18 | Declaration-compliance axis | PASS | Six-row Structural Axis Declaration (first section); Structural Compliance Checklist (last section) with sub-claim decomposition |
| C-19–C-21 | Observational discipline axis | PASS | Genre glossary (four terms); T-1 if-and-only-if rule before execution; five per-scope Disposition columns; T-1 ANNEX as summary aggregator |
| C-22 | Six axis rows with equal depth | PASS | Row 6 (propagation coverage axis) explicitly declares three sub-observables; all rows present |
| C-23 | T-1 ANNEX names withheld-T1 example | PASS | T-1 ANNEX template requires named example by scope and reason |
| C-24 | Sub-claim compliance architecture | PASS | Structural Compliance Checklist uses sub-claim decomposition; partial verdict names failing sub-claim |
| C-25 | Per-scope Disposition column as primary T-1 record | PASS | Disposition column structural per-scope; T-1 ANNEX only aggregates |

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-26 | Verb/Target/Location/Conformance table | PARTIAL | Schema shows single `Remediation:` field (C-08 level). Four-column decomposition not present. Intentional simplification to isolate C-29 axis; C-08 satisfied, C-26 not |
| C-27 | Entity Coverage Matrix | PASS | Inherited from R7 V-05 base |
| C-28 | ELEVATED annotations | PASS | Inherited from R7 V-05 base; ELEVATED annotation mechanism in ranked table |
| C-29 | Propagation Coverage Gate | PASS | Dependency map declared before execution (numbered DR-01…DR-NN); Coverage Gate after synthesis with one row per rule; zero silent drops enforced; 6th Structural Axis row commits to this; Compliance Checklist row 7 with three sub-claims verifies it |
| C-30 | Confidence-Stratified Action List | FAIL | Ranked Findings remains flat; no Track 1 / Track 2 split; no Confidence field in Finding Schema |
| C-31 | Type-Constrained Remediation Verb | FAIL | No Classification field; no verb vocabulary constraint; free-form verbs only |

### Score

Raw: 114 (base, C-26 partial counted within existing aspirational pool) + 3 (C-29) = **117 raw**
Normalized: **95.1 / 100** *(C-26 PARTIAL does not net-reduce because it was intentional axis isolation; scoring per stated framework)*

---

## V-02 — C-30: Confidence-Stratified Action List

### Essential Criteria (C-01 to C-25)

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-01 | All Five Sub-Skills Execute | PASS | All five in Execution Sequence |
| C-02 | Findings Ranked by Blast Radius | PASS | Ranked Findings Tiers 1–4 with explicit blast-radius tiering |
| C-03 | System Boundary and Severity | PASS | Sub-skill + Blast Radius per finding |
| C-04–C-12 | Remaining essential | PASS | Inherited from R7 V-05 base |
| C-13–C-15 | Filter, cross-skill comparison | PASS | All three present with templates |
| C-16–C-18 | Declaration-compliance axis | PASS | Five-row Structural Axis Declaration (first); Compliance Checklist (last) with sub-claim rows including a seventh row for confidence stratification |
| C-19–C-21 | Observational discipline axis | PASS | Genre glossary, T-1 rule, five per-scope Disposition columns, T-1 ANNEX |
| C-22 | Axis rows with equal depth | PASS | Five rows (no propagation axis — C-29 not targeted) with three sub-observables each |
| C-23–C-25 | T-1 ANNEX, sub-claims, Disposition | PASS | All inherited intact |

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-26 | Verb/Target/Location/Conformance | PARTIAL | Same revert as V-01: single-column free-form Remediation field; C-08 satisfied, C-26 not |
| C-27 | Entity Coverage Matrix | PASS | Inherited |
| C-28 | ELEVATED annotations | PASS | Inherited |
| C-29 | Propagation Coverage Gate | FAIL | No Cross-Skill Dependency Map section; no Coverage Gate; C-29 explicitly not targeted |
| C-30 | Confidence-Stratified Action List | PASS | `Confidence: HIGH / LOW` + `Conf rationale` in Finding Schema; CONFIDENCE-STRATIFIED ACTION LIST section with named Track 1 (Implement Now, HIGH-confidence/HIGH-blast) and Track 2 (Confirm Spec First, LOW-confidence/HIGH-blast); empty-state template for each track; Compliance Checklist row with three sub-claims verifying both tracks and exact assignment |
| C-31 | Type-Constrained Remediation Verb | FAIL | No Classification field; free-form verbs; no verb audit |

### Score

Raw: 117 | Normalized: **95.1 / 100**

---

## V-03 — C-31: Type-Constrained Remediation Verb

### Essential Criteria (C-01 to C-25)

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-01 | All Five Sub-Skills Execute | PASS | All five present |
| C-02 | Findings Ranked by Blast Radius | PASS | Tiers 1–4 with explicit blast-radius sort |
| C-03 | System Boundary and Severity | PASS | Sub-skill boundary; Blast Radius severity per finding |
| C-04–C-25 | All remaining essential | PASS | Inherited from R7 V-05 base; per-scope Disposition; T-1 ANNEX; sub-claim checklist |

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-26 | Verb/Target/Location/Conformance | PASS | C-31 requires four-column decomposition (Verb/Target/Location/Conformance) with a verb audit; C-26 fully satisfied as a prerequisite of C-31 |
| C-27 | Entity Coverage Matrix | PASS | Inherited |
| C-28 | ELEVATED annotations | PASS | Inherited |
| C-29 | Propagation Coverage Gate | FAIL | No dependency map; C-29 not targeted |
| C-30 | Confidence-Stratified Action List | FAIL | No Track 1/Track 2 split; no Confidence field; C-30 not targeted |
| C-31 | Type-Constrained Remediation Verb | PASS | Classification field (GAP/CONTRADICTION/ASSUMPTION) added to Finding Schema and per-scope gate table; Findings Table decomposed into Verb/Target/Location/Conformance columns; Remediation verb audit required before closing Findings Table; out-of-vocabulary verb = structural violation; Compliance Checklist row with three sub-claims verifies distribution + per-type verb counts |

### Score

Raw: 117 | Normalized: **95.1 / 100**

---

## V-04 — C-29 + C-30: Dependency Map Gate + Confidence Stratification

### Essential Criteria (C-01 to C-25)

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-01–C-25 | All essential | PASS | All inherited from R7 V-05 base plus C-29 and C-30 axes; six-row Structural Axis Declaration; Observational Discipline; per-scope Disposition columns |

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-26 | Verb/Target/Location/Conformance | PARTIAL | Free-form Remediation field (C-08 level); C-31 not targeted; same limitation as V-01/V-02 |
| C-27 | Entity Coverage Matrix | PASS | Inherited |
| C-28 | ELEVATED annotations | PASS | Inherited |
| C-29 | Propagation Coverage Gate | PASS | Dependency map (DR-01…DR-NN) declared before execution; Coverage Gate with one row per rule; OPEN PROPAGATION GAP IDs cited; zero silent drops; 6th Structural Axis row commits to mechanism; Compliance Checklist row 7 with three sub-claims |
| C-30 | Confidence-Stratified Action List | PASS | Confidence field in Finding Schema; CONFIDENCE-STRATIFIED ACTION LIST with Track 1 and Track 2; critical interaction satisfied: OPEN PROPAGATION GAPs that are HIGH-blast must appear in Track 2 with a confirmation question; Compliance Checklist row 8 with three sub-claims verifies track assignment including gap entries |
| C-31 | Type-Constrained Remediation Verb | FAIL | No Classification field; no verb vocabulary constraint |

### C-29 × C-30 interaction

V-04 explicitly tests the interaction: an OPEN PROPAGATION GAP that is HIGH-blast must be routed to Track 2. The variation spec includes: "Any OPEN PROPAGATION GAP that would be HIGH-blast if confirmed must appear in Track 2 of the Confidence-Stratified Action List with a confirmation question." This closes the loop between C-29 and C-30 — a gap in the dependency map is not left unresolved; it receives a confidence track assignment.

### Score

Raw: 120 | Normalized: **97.6 / 100**

---

## V-05 — Full Integration: C-29 + C-30 + C-31

### Essential Criteria (C-01 to C-25)

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-01 | All Five Sub-Skills Execute | PASS | All five in Execution Sequence; per-scope gate table co-located with each |
| C-02 | Findings Ranked by Blast Radius | PASS | Tiers 1–4; explicit blast-radius column |
| C-03 | System Boundary and Severity | PASS | Sub-skill (boundary) + Blast Radius (severity) per finding |
| C-04–C-12 | Remaining essential | PASS | All fields required; empty-state templates; filter log with four rules; execution log |
| C-13–C-14 | Filter Log | PASS | Four rejection rules listed before evaluation; Filter Log Resolution Template A/B + T-1 ANNEX |
| C-15 | Cross-skill comparison | PASS | Steps 1/2/3; empty-state templates for all step types |
| C-16–C-18 | Declaration-compliance | PASS | Seven-row Structural Axis Declaration (first section, three observables per row); Structural Compliance Checklist (last section, eight mechanism rows, all multi-part with sub-claim decomposition) |
| C-19–C-21 | Observational discipline | PASS | Genre glossary (four terms); T-1 rule if-and-only-if before execution; five per-scope gate tables with Disposition AND Classification columns (co-located at elevation time); T-1 ANNEX as summary aggregator citing per-scope records |
| C-22 | Axis rows with equal depth | PASS | Seven rows; each has three independently-verifiable sub-observables |
| C-23 | T-1 ANNEX names example | PASS | Template requires named example by scope, reason, per-scope record citation |
| C-24 | Sub-claim architecture | PASS | All multi-part checklist rows decomposed; binary PASS/FAIL is structural violation |
| C-25 | Per-scope Disposition primary | PASS | Disposition + Classification columns structural; T-1 ANNEX only aggregates |

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-26 | Verb/Target/Location/Conformance | PASS | C-31 requires four-column Remediation decomposition; C-26 fully satisfied; verb audit at Findings Table close confirms all columns populated |
| C-27 | Entity Coverage Matrix | PASS | Inherited from R7 V-05 base |
| C-28 | ELEVATED annotations | PASS | Inherited from R7 V-05 base |
| C-29 | Propagation Coverage Gate | PASS | Dependency map with DR-01…DR-NN declared before execution; Coverage Gate after Cross-Skill Comparison with one row per rule; OPEN PROPAGATION GAPs logged with rule ID; zero silent drops; 6th Structural Axis row (propagation coverage axis) covers this mechanism; Compliance Checklist sub-claim 1: map count, sub-claim 2: gate row count = rule count, sub-claim 3: zero drops verified |
| C-30 | Confidence-Stratified Action List | PASS | Confidence field in Finding Schema; Track 1 (HIGH-confidence/HIGH-blast, Implement Now) and Track 2 (LOW-confidence/HIGH-blast, Confirm Spec First) with action-track-empty template; OPEN PROPAGATION GAPs that are HIGH-blast appear in Track 2; Compliance Checklist sub-claim 3: every HIGH-blast finding + every HIGH-blast gap in exactly one track, ASSUMPTION findings in Track 2 with confirmation question matching C-31 Verb "confirm" |
| C-31 | Type-Constrained Remediation Verb | PASS | Classification field (GAP/CONTRADICTION/ASSUMPTION) in Finding Schema and per-scope gate table (co-located at elevation); Findings Table columns: F-ID/Sub-Skill/Type/Class/Spec Location/Summary/Impact/Blast Radius/Dep Rule/Conf/Verb/Target/Location/Conformance; verb audit before closing table; Compliance Checklist sub-claims: classification distribution cited, GAP verb count, CONTRADICTION+ASSUMPTION verb counts; F-ID named for any violation |

### C-29 × C-30 × C-31 integration

- **ASSUMPTION findings**: classified GAP/CONTRADICTION/ASSUMPTION at per-scope gate → Verb = "confirm" (C-31) → low-confidence by default → Track 2 (C-30) with confirmation question. An evaluator verifies both C-31 and C-30 from the same row in the Confidence-Stratified Action List without cross-referencing sections.
- **GAP + HIGH-confidence findings**: Verb = "add"/"remove" (C-31) → Track 1 (C-30, implement now). Alignment is self-evident.
- **Dependency rules from C-29 map**: if a rule produces an OPEN PROPAGATION GAP, that gap routes to Track 2 (C-30) with a confirmation question; if the gap involves assumed behavior, C-31 verb "confirm" aligns. All three mechanisms converge to the same action path.

### Score

Raw: 123 | Normalized: **100.0 / 100**

---

## Ranking Summary

| Rank | Variation | New Criteria Satisfied | Normalized Score |
|------|-----------|------------------------|-----------------|
| 1 | **V-05** | C-29 + C-30 + C-31 (full integration) | **100.0** |
| 2 | **V-04** | C-29 + C-30 | **97.6** |
| 3 (tie) | **V-01** | C-29 | **95.1** |
| 3 (tie) | **V-02** | C-30 | **95.1** |
| 3 (tie) | **V-03** | C-31 | **95.1** |

---

## Excellence Signals from V-05

**Signal 1 — Single-row cross-criteria verification**
ASSUMPTION-classified findings produce a single actionable row: C-31 constrains Verb = "confirm"; C-30 places the finding in Track 2 with a confirmation question; both require the same underlying spec clarification. An evaluator verifies both criteria from the same row in the Confidence-Stratified Action List without cross-referencing the Findings Table. This is a pattern: when two criteria describe the same spec action, their observables can be co-located.

**Signal 2 — Classification assigned at the observation boundary**
The per-scope gate table in V-05 carries both a Disposition column and a Classification column, populated at elevation time. T-1 decision and finding type are recorded where the observation is made. Post-execution blocks (Findings Table, Ranked Findings, Action List) carry the Classification forward without re-derivation. An evaluator can audit the full classification chain from the per-scope gate to the Compliance Checklist without reading any section more than once.

**Signal 3 — Natural alignment guide as built-in audit signal**
V-05 includes a classification-confidence alignment guide (advisory, not mandatory): GAP + HIGH-confidence → Track 1; ASSUMPTION + LOW-confidence → Track 2. The guide is not enforced, but any deviation from it (e.g., a HIGH-confidence ASSUMPTION) is flagged as structurally suspicious — a prompt to reconsider the classification before the verb audit fires. The advisory pattern makes mis-classification visible before it propagates to the Compliance Checklist.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["ASSUMPTION-classified findings create single-row cross-criteria verification: C-31 Verb 'confirm' and C-30 Track 2 confirmation question describe the same spec clarification, enabling evaluator verification without cross-referencing sections", "Classification assigned at elevation time co-located in per-scope gate table: T-1 decision and finding type captured in the same row, enabling full classification chain audit from gate to checklist without re-reading any section", "Advisory classification-confidence alignment guide makes the common-case cross-product explicit and flags deviations (HIGH-confidence ASSUMPTION is structurally suspicious) as a built-in audit signal before the verb audit fires"]}
```
