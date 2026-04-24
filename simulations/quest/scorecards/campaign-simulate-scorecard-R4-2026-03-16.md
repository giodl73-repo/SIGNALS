## campaign-simulate — Round 4 Scoring

### Rubric Summary (v4)

| Pool | Criteria | Points |
|------|----------|--------|
| Essential | C-01–C-05 | 10 pts each = 50 pts |
| Recommended | C-06–C-08 | 10 pts each = 30 pts |
| Aspirational | C-09–C-18 | 2 pts each = 20 pts |
| **Total** | | **100 pts / divisor 1.00** |

Golden threshold: all 5 essential pass AND score ≥ 80.

---

## V-01 — Pre-Finding Structural Axis Declaration

**Design:** Adds a model-written `STRUCTURAL AXIS DECLARATION` table as the first output section (3 axes: filtering, empty-state, cross-skill comparison). No compliance checklist. All R3 V-05 mechanisms carry forward.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 Sub-skill sections present | PASS | 5 sub-skills in execution sequence; empty-state template "No findings from [sub-skill]..." covers each |
| C-02 Execution order enforced | PASS | Numbered sequence 1–5 (flow-lifecycle → trace-permissions); output section order declared |
| C-03 Unified findings report | PASS | Single output file with declared section order; all sub-skill results synthesized into one table |
| C-04 Blast radius ranking | PASS | 4-tier ranked findings (System-Wide → Isolated); empty-state template for each tier |
| C-05 ≥1 spec gap or contract violation | PASS | Finding schema includes spec-gap/contract-violation types; Filter Rule 1 enforces named spec location on every elevated observation |
| C-06 Source + Location + Impact | PASS | Schema enforces Sub-skill, Spec location, Impact (standalone FAILURE label); merging Impact into Summary is a labeled failure condition |
| C-07 Cross-sub-skill coverage | PASS | 5 sub-skills in execution sequence; finding IDs attributed by sub-skill in Execution Log |
| C-08 Actionable remediation | PASS | Remediation field in schema; "fix the spec" is a named FAILURE condition; per-finding not just summary |
| C-09 Cross-skill pattern detection | PASS | Steps 1–3 in Cross-Skill Comparison Protocol; compounding promotion format in Step 3 |
| C-10 Blast radius rationale | PASS | BR rationale field in schema (REQUIRED for cross-skill/system-wide); top-3 ranked findings require explicit rationale |
| C-11 Empty-state discipline | PASS | 7 named templates covering sub-skill, filter gate, findings table, ranked tiers, comparison steps, execution log |
| C-12 Compounding elevation | PASS | Step 3 "Promoted from [tier] to [tier] because [cross-skill root cause means...]" format; vacuous pass when C-09 doesn't fire |
| C-13 Discriminating rejection | PASS | Filter log table with Elevate? + Rejection Reason columns; 4 named rules |
| C-14 Vacuous-filter acknowledgment | PASS | Template B explicitly: "Zero rejected. RECALIBRATION REQUIRED..." applied when all rows are "yes" |
| C-15 Active negative comparison | PASS | Steps 1+2 required even when Step 3 has no patterns; cross-skill-patterns empty template requires citing Step 2 pairs |
| C-16 Structural coverage symmetry | PASS | Filtering axis: named rule filter log; empty-state axis: 7 typed templates — both structurally enforced, not judgment-dependent |
| C-17 Pre-finding axis declaration | PASS | STRUCTURAL AXIS DECLARATION is model-written output section, before findings, names 3 axes with mechanisms and sections |
| C-18 End-of-report compliance checklist | **FAIL** | No compliance checklist section in output; V-01 design explicitly leaves C-18 gap open |

**Essential:** 5 × 10 = **50 pts**
**Recommended:** 3 × 10 = **30 pts**
**Aspirational:** 9 × 2 = **18 pts** (C-17 ✓, C-18 ✗)
**V-01 Total: 98 / 100**

---

## V-02 — End-of-Report Structural Compliance Checklist

**Design:** Adds a model-written `STRUCTURAL COMPLIANCE CHECKLIST` with 4-column evidence schema (Mechanism, Report Section, Evidence, Status) as the final output section. No model-written declaration section — axes described in prompt preamble text only.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 | PASS | Same as V-01 — sub-skill empty-state templates, execution log |
| C-02 | PASS | Numbered sequence 1–5, output section order declared |
| C-03 | PASS | Single output file with synthesized findings |
| C-04 | PASS | 4-tier blast radius ranking with empty-state templates |
| C-05 | PASS | Schema enforces spec-gap/contract-violation types + spec location anchor |
| C-06 | PASS | Sub-skill, Spec location, Impact (standalone) with FAILURE labels |
| C-07 | PASS | 5 sub-skills attributed; findings tracked in execution log |
| C-08 | PASS | Per-finding Remediation with named FAILURE conditions |
| C-09 | PASS | Steps 1–3 cross-skill comparison protocol |
| C-10 | PASS | BR rationale field + top-3 requirement |
| C-11 | PASS | 7 named empty-state templates |
| C-12 | PASS | Compounding promotion format in Step 3 |
| C-13 | PASS | Named filter rules + rejection columns |
| C-14 | PASS | Template B vacuous-filter recalibration |
| C-15 | PASS | Steps 1+2 required; empty template requires Step 2 citations |
| C-16 | PASS | Both axes structurally enforced |
| C-17 Pre-finding axis declaration | **FAIL** | Axes described in prompt instruction text only ("This report enforces two structural axes simultaneously...") — not a model-written declaration section in the output artifact. Evaluator reading the output file sees no preamble before findings. |
| C-18 End-of-report compliance checklist | PASS | STRUCTURAL COMPLIANCE CHECKLIST as final output section; 4 mechanism rows; Evidence column requires "actual counts and section names" — example shows "4 observations evaluated, 1 rejected at Rule 1" format |

**Essential:** 5 × 10 = **50 pts**
**Recommended:** 3 × 10 = **30 pts**
**Aspirational:** 9 × 2 = **18 pts** (C-17 ✗, C-18 ✓)
**V-02 Total: 98 / 100**

---

## V-03 — Audit Register Axis

**Design:** Full reframe as formal technical audit. Domain vocabulary: AUDIT SCOPE AND STRUCTURAL CONTROLS (first section, C-17 analog), per-check observation logs, OBSERVATION FILTER GATE RESOLUTION, UNIFIED AUDIT FINDINGS TABLE, BLAST RADIUS RANKING, CROSS-CHECK COMPOUNDING ANALYSIS, AUDIT COMPLIANCE SUMMARY (final section, C-18 analog).

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 | PASS | 5 audit checks (AUDIT CHECK 1–5); "Audit check [name] complete. No deficiencies found because [reason]" empty-state template per check |
| C-02 | PASS | Explicit check order 1–5 (flow-lifecycle → trace-permissions); "Run all five checks in the order below" |
| C-03 | PASS | UNIFIED AUDIT FINDINGS TABLE synthesizes across all checks; single output file |
| C-04 | PASS | BLAST RADIUS RANKING: 4 tiers (system-wide, cross-check, component-wide, isolated) + empty-state templates |
| C-05 | PASS | Schema types include spec-gap, contract-violation; Spec reference field: "a finding without a specific reference is an observation -- it does not qualify as an audit finding" |
| C-06 | PASS | Schema: Audit check (source), Spec reference (location), Consequence (standalone FAILURE label); merging Consequence into Deficiency is named failure |
| C-07 | PASS | 5 checks with attributed findings in AUDIT EXECUTION LOG |
| C-08 | PASS | Remediation field; "'update the spec' fails this field" |
| C-09 | PASS | Cross-Check Compounding Analysis Steps 1–3; promotion format in Step 3 |
| C-10 | PASS | BR basis field required for cross-check/system-wide + top-3 rationale in BLAST RADIUS RANKING |
| C-11 | PASS | 6 named templates covering all audit section types |
| C-12 | PASS | "Promoted from [tier] to [tier] because [shared root cause means...]" in Step 3 |
| C-13 | PASS | Per-check observation logs with "Elevate to finding? / rejection rule applied" columns; filter rules embedded per check |
| C-14 | PASS | Template B in OBSERVATION FILTER GATE RESOLUTION: "NOTE: A filter gate with zero rejections provides no evidence of filtering judgment..." |
| C-15 | PASS | Steps 1+2 required; "cross-check-summary-no-compounding template (must cite Step 2 pairs and verdicts by pair number)" |
| C-16 | PASS | Filtering: per-check observation logs + gate resolution with named rules; empty-state: 6 typed templates — both structural |
| C-17 Pre-finding axis declaration | PASS | AUDIT SCOPE AND STRUCTURAL CONTROLS is the first output section; table names 3 controls with Purpose, Mechanism (e.g., "Filter Log with four named rejection rules; Filter Log Resolution block Template A/B"), and Report Section — written by model into output before findings |
| C-18 End-of-report compliance checklist | PASS | AUDIT COMPLIANCE SUMMARY is final section; 3 rows for all declared controls; Evidence column: "cite: N observations, M rejected at Rule K" / "Template applied in [section]: '[first few words]'" — section name + evidence counts required |

**Essential:** 5 × 10 = **50 pts**
**Recommended:** 3 × 10 = **30 pts**
**Aspirational:** 10 × 2 = **20 pts** (all pass)
**V-03 Total: 100 / 100**

---

## V-04 — Combined: C-17 Declaration + C-18 Checklist

**Design:** R3 V-05 base + STRUCTURAL AXIS DECLARATION (first output section, 3-axis table) + STRUCTURAL COMPLIANCE CHECKLIST (final output section, 4 mechanism rows with evidence citations). Adds "compliance-checklist-not-fired" empty-state template.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01–C-08 | PASS (all) | Full schema with Sub-skill / Spec location / Impact standalone / Remediation per-finding; execution sequence 1–5; 4-tier blast radius ranking |
| C-09 | PASS | Steps 1–3 cross-skill comparison protocol |
| C-10 | PASS | BR rationale field + top-3 ranking rationale |
| C-11 | PASS | 8 named templates including "Compliance checklist not fired" meta-template |
| C-12 | PASS | Compounding promotion format in Step 3 |
| C-13 | PASS | Named filter rules + rejection columns |
| C-14 | PASS | Template B recalibration |
| C-15 | PASS | Steps 1+2 required; empty template requires Step 2 citations |
| C-16 | PASS | Both axes structurally enforced |
| C-17 | PASS | STRUCTURAL AXIS DECLARATION written into output as first section; 3-axis table with criteria, mechanisms, and report sections; "An evaluator reading this section must be able to predict what structural mechanisms appear" |
| C-18 | PASS | STRUCTURAL COMPLIANCE CHECKLIST as final output section; 4 rows (Filter Log, Filter Log Resolution, Empty-state templates, Cross-skill comparison); Evidence: "5 observations, 1 rejected at Rule 2: no blast radius estimable" example — actual counts required |

**Essential:** 50 | **Recommended:** 30 | **Aspirational:** 20
**V-04 Total: 100 / 100**

---

## V-05 — Full Integration (Four Structural Axes)

**Design:** Extends V-04 with a 4th declared axis — declaration-compliance (C-17+C-18 as their own structural mechanism). Declaration table names 4 axes. Compliance checklist has 6 rows including self-attestation rows. The structural verification mechanism verifies itself.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01–C-08 | PASS (all) | Same structural foundations as V-04; stronger empty-state template for compliance-checklist-not-fired includes "Impact on report validity: [whether the omission affects any findings]" |
| C-09 | PASS | Steps 1–3 with compounding promotion format; additional note: "A pair is compounding only if fixing the root cause of one also resolves the other" |
| C-10 | PASS | BR rationale field + "name downstream flows, components, or contracts affected and explain why scope reaches that far" in ranked findings |
| C-11 | PASS | 8 named templates including upgraded compliance meta-template |
| C-12 | PASS | Promotion format with explicit expansion: "Promoted from [tier] to [tier] because [cross-skill root cause means that X expands downstream scope from Y to Z]" |
| C-13 | PASS | Filter log with 4 named rules + rejection columns |
| C-14 | PASS | Template B recalibration |
| C-15 | PASS | Steps 1+2 required; "a bare declaration ('no compounding patterns detected') without citing Step 2 pairs fails C-15" |
| C-16 | PASS | Both axes structurally enforced; declaration table itself is structural evidence |
| C-17 | PASS | STRUCTURAL AXIS DECLARATION names 4 axes: filtering, empty-state, cross-skill comparison, **declaration-compliance**; mechanism column for 4th axis: "This Structural Axis Declaration section (before findings) + Structural Compliance Checklist section (after findings) with evidence citations" |
| C-18 | PASS | 6-row STRUCTURAL COMPLIANCE CHECKLIST; rows 5–6 are self-referential: row 5 attests to Declaration presence ("Four axes declared: filtering, empty-state, cross-skill comparison, declaration-compliance"); row 6 attests to Checklist presence ("Present as final section; all mechanisms cited with section names and evidence") |

**Essential:** 50 | **Recommended:** 30 | **Aspirational:** 20
**V-05 Total: 100 / 100**

---

## Rankings

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| T-1 | V-03 Audit Register | 100 | ✓ |
| T-1 | V-04 Combined C-17+C-18 | 100 | ✓ |
| T-1 | V-05 Full Integration | 100 | ✓ |
| T-4 | V-01 C-17 Single-Axis | 98 | ✓ |
| T-4 | V-02 C-18 Single-Axis | 98 | ✓ |

**Differentiation within 100-pt tier:**
- V-05 > V-04 > V-03 on structural sophistication: V-05 introduces self-referential declaration-compliance axis; V-04 adds the "compliance-checklist-not-fired" meta-template; V-03 achieves the same score organically through domain register (no explicit template injection).
- All three are golden candidates. V-05 is the strongest reference implementation; V-03 demonstrates that the same structural discipline can emerge from vocabulary register alone.

---

## Excellence Signals (from top-scoring variations)

**Signal 1 — Self-Referential Structural Compliance (V-05)**
Declaring the declaration-compliance mechanism (C-17+C-18) as its own 4th axis creates a closed loop: the report declares it will declare and verify, then verifies it declared and verified. The compliance checklist row for the checklist itself ("Present as final section; all mechanisms cited") is the first instance in the series of a structural mechanism attesting to its own execution. This pattern eliminates the last residual gap: a report could declare all mechanisms, exercise all mechanisms, but leave the compliance checklist itself unverified. Self-verification closes it.

**Signal 2 — Domain Register as Organic Structural Generator (V-03)**
The audit framing produces C-17 (AUDIT SCOPE AND STRUCTURAL CONTROLS) and C-18 (AUDIT COMPLIANCE SUMMARY) as natural sections of an audit report format — without explicit template injection or rubric-category references in the prompt. The structural discipline emerges from vocabulary register ("control," "audit scope," "compliance summary") rather than from mechanism-naming instructions. This suggests a design principle: domain vocabulary that implies control verification (audit, inspection, certification) can substitute for explicit structural scaffolding, and may be more robust to model paraphrasing because the domain frame reinforces the schema.

**Signal 3 — Meta Empty-State Template for Structural Failures (V-04/V-05)**
Adding "compliance-checklist-not-fired" as a named empty-state template turns structural non-compliance into a disclosed, nameable condition rather than a silent gap. A report that uses the template is structurally better than one that simply omits the checklist: the failure is visible and labeled, not hidden. This extends the empty-state discipline principle from content sections to structural mechanism sections — every declared mechanism, including the verification mechanisms themselves, has a defined failure mode with explicit acknowledgment text.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Self-referential structural compliance: declaring C-17+C-18 as their own axis in the declaration table and having the compliance checklist attest to its own presence — the verification mechanism declares and verifies itself, closing the last residual gap", "Domain register as organic structural generator: audit vocabulary (scope, controls, compliance summary) produces C-17 and C-18 organically without explicit template injection, demonstrating that structural discipline can emerge from domain framing alone"]}
```
