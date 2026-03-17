## /quest:score — trace-contract Round 2

### Rubric v2 Criteria (reference)

| ID | Tier | Criterion |
|----|------|-----------|
| C-01 | Essential | Contract named before any output |
| C-02 | Essential | Every mismatch row has severity |
| C-03 | Essential | Every mismatch row has spec ref |
| C-04 | Essential | Every finding has root cause hypothesis |
| C-05 | Essential | Breaking findings distinguished from non-breaking |
| C-06 | Recommended | Three-directory structure explicit (10+/20+/30+) |
| C-07 | Recommended | Automate/Connectors domain engaged |
| C-08 | Recommended | Findings are actionable |
| C-09 | Aspirational | Severity distribution calibrated (output) |
| C-10 | Aspirational | Contract delta summarized for spec update |
| C-11 | Aspirational | Classification-before-analysis gate present |
| C-12 | Aspirational | Negative-constraint on expected phase (isolation, not just ordering) |
| C-13 | Aspirational | Calibration gate enforces severity distribution (mechanism) |

---

## V-01 Scorecard (Lifecycle — Minimal Gate)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | SETUP has Contract field before any section |
| C-02 | PASS | Diff table has Severity column; CLASSIFICATION GATE covers completeness |
| C-03 | PASS | Diff table has Spec Ref column; gate blocks progress if incomplete |
| C-04 | PASS | Findings require "Root cause hypothesis" sub-field |
| C-05 | PASS | Breaking / Degraded / Cosmetic sections are labeled and separate |
| C-06 | PASS | Sections explicitly labeled "10+ INPUT", "20+ EXPECTED OUTPUT", "30+ ACTUAL OUTPUT" |
| C-07 | PASS | Findings scaffold names "connector action, auth token response shape, action parameter mapping, schema from stale swagger, OpenAPI definition" |
| C-08 | PASS | Next step sub-field required; scaffold gives specific actions |
| C-09 | **FAIL** | Three severity sections present but no instruction to check for uniform distribution; model can mark all breaking without challenge |
| C-10 | PASS | CONTRACT DELTA section present with spec clause table |
| C-11 | PASS | Diff section: "STATUS AND SEVERITY CLASSIFICATION ONLY IN THIS SECTION. Do not write root cause hypotheses here." + CLASSIFICATION GATE + explicit "Do not write findings until gate passes" |
| C-12 | **FAIL** | CLASSIFICATION GATE checks coverage (fields from each table) but has no isolation attestation for the expected phase; no "actual not consulted" checkbox |
| C-13 | **FAIL** | No calibration checkpoint before findings finalized; SUMMARY table records the distribution but no gate reviews it |

**E = 5/5 | R = 3/3 | A = 2/5 (C-10, C-11)**

**Score: (5/5 × 60) + (3/3 × 30) + (2/5 × 10) = 60 + 30 + 4 = 94**
**Golden: YES (5/5 essential, composite ≥ 80)**

---

## V-02 Scorecard (Role Sequence — Isolation Declaration)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | SETUP has Contract field |
| C-02 | PASS | Diff table has Severity column; AUTOMATE ENGINEER confirmation attests N mismatches classified |
| C-03 | PASS | Diff table has Spec Ref column |
| C-04 | PASS | "Root cause hypothesis (Automate)" required sub-field per finding |
| C-05 | PASS | Breaking / Degraded / Cosmetic finding sections, role-labeled |
| C-06 | PASS | Three sections by role map to expected → actual → joint diff; rubric requires "clearly separated with labels" — satisfied |
| C-07 | PASS | Role names anchor domain; findings scaffold: "schema version, field rename, type coercion removal, missing action parameter mapping, auth response shape change, connector schema from stale swagger" |
| C-08 | PASS | Next step scaffold: "update OpenAPI definition / add coercion shim / regenerate connector schema / update Parse JSON action schema / file provider API bug" |
| C-09 | **FAIL** | No instruction to check for uniform severity distribution; three sections present but no calibration framing |
| C-10 | PASS | "Contract delta (CONNECTORS EXPERT to action)" bullet list, one line per finding requiring spec change |
| C-11 | PASS | "AUTOMATE ENGINEER classification confirmation: No root cause hypotheses were written during diff construction — classification only. Proceeding to findings analysis." + "Do not begin findings until this confirmation line appears" |
| C-12 | PASS | CONNECTORS EXPERT isolation sign-off: "Actual output was not referenced during this phase — not just ordered after, but not consulted at all." This is an explicit negative-constraint attestation, not a coverage check |
| C-13 | **FAIL** | No calibration gate before findings finalized; role sign-off does not review severity distribution |

**E = 5/5 | R = 3/3 | A = 3/5 (C-10, C-11, C-12)**

**Score: (5/5 × 60) + (3/3 × 30) + (3/5 × 10) = 60 + 30 + 6 = 96**
**Golden: YES**

---

## V-03 Scorecard (Domain Emphasis — Contract Element Type Column)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | SETUP has Contract field |
| C-02 | PASS | Diff table has Severity column |
| C-03 | PASS | Diff table has Spec Ref column |
| C-04 | PASS | Root cause hypothesis required in each finding |
| C-05 | PASS | Breaking / Degraded / Cosmetic finding sections |
| C-06 | PASS | Sections labeled "10+ INPUT", "20+ EXPECTED OUTPUT", "30+ ACTUAL OUTPUT" |
| C-07 | PASS | Pre-printed "Contract element type" column with vocabulary: schema-field, auth-handshake, action-payload, trigger-payload, error-shape, metadata. "Connector surface" sub-field in findings names where in the Automate/Connectors stack the fix lives. Strongest domain coverage of any variation |
| C-08 | PASS | "Next step: [Specific action at the named connector surface]" — surface-anchored actionability |
| C-09 | **FAIL** | Three severity sections present but no calibration instruction; no anti-pattern framing or gate |
| C-10 | PASS | CONTRACT DELTA section present as table; includes "Contract element type" column carrying domain context into the delta |
| C-11 | **FAIL** | DIFF TABLE section has no classification gate, no "classification only" label, no gate line. Analysis may be written during diff construction |
| C-12 | **FAIL** | No isolation check on expected phase |
| C-13 | **FAIL** | No calibration gate before findings finalized |

**E = 5/5 | R = 3/3 | A = 1/5 (C-10 only)**

**Score: (5/5 × 60) + (3/3 × 30) + (1/5 × 10) = 60 + 30 + 2 = 92**
**Golden: YES**

---

## V-04 Scorecard (Inertia Framing — Anti-Pattern Warning)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | SETUP has Contract field |
| C-02 | PASS | STEP 3 classification table has Severity column |
| C-03 | PASS | STEP 3 classification table has Spec Ref column |
| C-04 | PASS | Root cause hypothesis required; failure mode 2 warns: "'Field is missing' is an observation. 'Field was renamed in v2.1' is a hypothesis." |
| C-05 | PASS | Breaking / Degraded / Cosmetic finding sections |
| C-06 | PASS | STEP 1 (expected) / STEP 2 (actual) / STEP 3 (classify) mirror the three-directory pattern with explicit labels |
| C-07 | PASS | Root cause scaffold names "API provider renamed field, type coercion removed from connector action, auth token shape changed, field missing from action parameter mapping, schema from stale swagger" |
| C-08 | PASS | Next step scaffold names specific actions at the connector layer |
| C-09 | PASS | Failure mode 3 pre-primes: "If all findings fall into one severity level, that claim must be explicitly justified." STEP 4 reinforces: "Before grouping findings by severity, check the distribution. If all mismatches are the same severity, justify that distribution explicitly." Contrast framing is sufficient for output-level calibration |
| C-10 | PASS | STEP 5 has "Contract delta (spec clauses requiring amendment)" as numbered list |
| C-11 | PASS | STEP 3 header: "STEP 3: CLASSIFY -- STATUS AND SEVERITY ONLY [prevents failure mode 2, classification phase]" + "This step is classification only. Do not write root cause hypotheses here. Do not write findings here." Section break + label = explicit gate in rubric's own terms |
| C-12 | **FAIL** | Failure mode 1 describes isolation as principle but no attestation mechanism. "Do not reference the runtime" is an instruction, not a filled negative-constraint checkpoint |
| C-13 | PASS | STEP 4 contains explicit pre-finalization instruction: "Before grouping findings by severity, check the distribution." The check is named, it fires before findings are grouped, and uniform distribution requires explicit justification. Satisfies "explicit checkpoint before findings are finalized that names the check" |

**E = 5/5 | R = 3/3 | A = 4/5 (C-09, C-10, C-11, C-13)**

**Score: (5/5 × 60) + (3/3 × 30) + (4/5 × 10) = 60 + 30 + 8 = 98**
**Golden: YES**

---

## V-05 Scorecard (Full Synthesis — Phases + Columns + Isolation)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | SETUP has Contract field before any phase |
| C-02 | PASS | Phase 3 diff table has Severity column + GATE 3 checkbox: "[ ] No Severity cells blank on mismatch rows" |
| C-03 | PASS | Phase 3 diff table has Spec Ref column + GATE 3 checkbox: "[ ] No Spec Ref cells blank on mismatch rows." + "See spec' alone does not qualify" |
| C-04 | PASS | Findings require Root cause hypothesis sub-field; GATE 4 checkbox: "[ ] No finding is missing root cause hypothesis or next step" |
| C-05 | PASS | Breaking / Degraded / Cosmetic sections; GATE 4 ensures all mismatches covered |
| C-06 | PASS | PHASE 1 (expected), PHASE 2 (actual), PHASE 3 (diff) — labeled phase separation mirrors three-directory pattern |
| C-07 | PASS | Findings scaffold names "connector action, auth token response shape, action parameter mapping, schema generated from stale swagger, provider API version mismatch between spec and connector definition" |
| C-08 | PASS | Next step scaffold: "update OpenAPI definition / add type coercion shim / regenerate connector schema from updated swagger / update Parse JSON schema in flow / file provider API bug report with field path and version evidence" |
| C-09 | PASS | GATE 4 checkbox: "[ ] Severity distribution reviewed before finalizing — not all one level unless explicitly justified: '[State justification if uniform, or confirm distribution is multi-level as expected]'" |
| C-10 | PASS | CONTRACT DELTA section present as table; notes to separate spec amendments from provider-side fixes |
| C-11 | PASS | GATE 3: "[ ] No root cause hypotheses or analysis text in this section — classification only" + "Do not begin PHASE 4 until GATE 3 passes with all five checkboxes confirmed" |
| C-12 | PASS | GATE 1 has dedicated checkbox: "[ ] Actual output was not referenced during this phase — not just ordered after, but not consulted at all (isolation check: the actual block was not read at this point)." Two-line phrasing distinguishes ordering from isolation explicitly |
| C-13 | PASS | GATE 4 checkbox fires before findings are finalized and names the check: "Severity distribution reviewed before finalizing — not all one level unless explicitly justified." Gate must be confirmed before artifact is complete |

**E = 5/5 | R = 3/3 | A = 5/5**

**Score: (5/5 × 60) + (3/3 × 30) + (5/5 × 10) = 60 + 30 + 10 = 100**
**Golden: YES**

---

## Ranking

| Rank | V | Score | Golden | A criteria passed |
|------|---|-------|--------|-------------------|
| 1 | **V-05** | **100** | YES | C-09, C-10, C-11, C-12, C-13 |
| 2 | **V-04** | **98** | YES | C-09, C-10, C-11, C-13 |
| 3 | **V-02** | **96** | YES | C-10, C-11, C-12 |
| 4 | **V-01** | **94** | YES | C-10, C-11 |
| 5 | **V-03** | **92** | YES | C-10 |

All five variations are Golden (all essential pass, composite ≥ 80).

---

## Excellence Signals — V-05

**1. Two-clause isolation checkbox (C-12 solution)**
GATE 1 uses two-part language: "not just ordered after, but not consulted at all." Single-clause ordering checks ("expected before actual") allow look-ahead contamination. The two-clause form makes the negative-constraint explicit as a distinct condition from ordering, and it is confirmable as a checkbox rather than inferred from section position. V-02 achieved C-12 via role attestation prose; V-05 achieves it as a structural gate that must be checked.

**2. Column completeness enforced at gate level, not instruction level (C-02/C-03 structural guarantee)**
GATE 3 contains "[ ] No Severity cells blank on mismatch rows" and "[ ] No Spec Ref cells blank on mismatch rows." Other variations have these columns but only instruction text requiring them. V-05 makes a blank cell a gate failure condition — the model cannot mark GATE 3 PASS while any mismatch row is incomplete. This converts C-02 and C-03 from instruction compliance to structural enforcement.

**3. Machine-readable gate result in frontmatter**
`gate1_isolation_confirmed: true` in the artifact frontmatter converts the gate outcome into a queryable field. Downstream automation can filter isolation-confirmed runs without parsing prose. This pattern is new in Round 2 and is not present in any other variation.

**Discriminator resolutions:**

- **C-12 test (V-02 role attestation vs V-05 checkbox):** Both pass C-12. Role-semantic isolation (V-02) is equivalent in rubric terms — the isolation attestation is explicit and uses the negative-constraint framing. Gate-level isolation (V-05) is stronger for automation but both satisfy the criterion.
- **C-13 test (V-04 contrast framing vs named gate):** V-04 PASSES C-13. The STEP 4 pre-check instruction ("Before grouping findings by severity, check the distribution") names the check explicitly and fires before findings are grouped, satisfying the rubric's "explicit checkpoint before findings are finalized." Contrast framing is a valid lighter-weight mechanism.
- **C-07 test (V-03 category column vs role naming):** V-03's pre-printed "Contract element type" column produces STRONGER domain coverage than role-label anchoring. Every field row carries a domain category. For Round 3 synthesis, V-03's category column is a candidate addition.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Two-clause isolation checkpoint: phrasing 'not just ordered after, but not consulted at all' separates negative-constraint isolation from ordering check, making C-12 confirmable as a gate rather than inferred from section position", "Column completeness gated at GATE level: Severity and Spec Ref blank cells are a gate failure condition, not just an instruction violation — structural guarantee for C-02 and C-03", "Machine-readable gate result in frontmatter: gate1_isolation_confirmed:true enables downstream automation to filter isolation-confirmed runs without prose parsing"]}
```
