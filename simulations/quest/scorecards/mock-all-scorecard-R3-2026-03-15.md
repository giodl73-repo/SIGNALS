Scorecard written to `simulations/quest/scorecards/mock-all-scorecard-R3-2026-03-15.md`.

---

## Round 3 Scorecard — mock-all

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-01 Named Phases + Stop-Gates | 5/5 | 3/3 | 7/7 | **100** | YES |
| 1 | V-05 Full Ceiling (all three axes) | 5/5 | 3/3 | 7/7 | **100** | YES |
| 3 | V-04 Phases + Pre-Printed Skeleton | 5/5 | 3/3 | 6.5/7 | **99.3** | YES |
| 4 | V-03 Category Vocabulary Mandates | 5/5 | 3/3 | 6/7 | **98.6** | YES |
| 5 | V-02 Pre-Printed Skeleton | 5/5 | 3/3 | 5.5/7 | **97.9** | YES |

All five are GOLDEN. The discriminators are C-14 and C-15 only.

**C-14** separates V-02/V-03 from the top: structural enforcement (pre-printed table) and step-label ordering both fail — the gate must be a surface-level "Do not begin X until Y" sentence the model can read and obey.

**C-15** separates V-02/V-04 (PARTIAL) from the rest: positive vocabulary guidance ("use X language") without a DO NOT prohibition clause allows register drift.

**V-01 surprise:** V-01 was designed as lifecycle-emphasis only but accidentally incorporated per-category MUST/DO NOT vocabulary rules in its PHASE 2 block, satisfying C-15 as a side effect. This confirms vocabulary DO NOT rules are independently sufficient for C-15 without structural table-column anchoring.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Stop-gate completeness specification: gate phrases that enumerate specific required output fields (all nine namespaces, named field types) rather than generic completion signals make gates self-checkable and resistant to partial-output bypass", "Vocabulary-column anchoring: embedding MUST/DO NOT vocabulary rules as columns in the classification table registers category-appropriate register constraints at the category assignment step, before any artifact body is written"]}
```
header blocks | PASS | Nine prescribed section templates each with MOCK ARTIFACT header |
| C-02 | Category classification correct for every namespace | PASS | PHASE 1 classification table with all nine namespaces before any artifact body |
| C-03 | REAL-REQUIRED flag on all EVIDENCE-HEAVY namespaces | PASS | PHASE 3 flag rules: REAL-REQUIRED -- all EVIDENCE-HEAVY namespaces, all tiers |
| C-04 | Coverage summary table with correct columns | PASS | PHASE 3 prescribes Namespace / Category / Flag / Recommended Next Step |
| C-05 | Final line follows prescribed handoff pattern | PASS | PHASE 4 HANDOFF: Next: /mock:review topic simulations/mock/topic-mock-date.md |
| C-06 | Tier 2/3 critical namespaces flagged | PASS | TIER-CRITICAL flag rule for trace-*, scout-feasibility, listen-* at tier >= 2 |
| C-07 | Each namespace section has plausible artifact body | PASS | PHASE 2 provides section template with vocabulary-guided body slot per namespace |
| C-08 | Compliance-tagged topics pre-flagged | PASS | COMPLIANCE flag rule: scout-compliance, trace-permissions when context active |
| C-09 | Tier flag scopes output when --tier supplied | PASS | Tier captured and referenced in TIER-CRITICAL conditional logic |
| C-10 | Recommended next steps are actionable and namespace-specific | PASS | name the exact skill call -- exact identifier required |
| C-11 | Classification table generated before any artifact body | PASS | Gate: Do not begin PHASE 2 until the classification table is complete and all nine namespaces have an assigned Category, Tier 2/3 Critical value, and Compliance-Tagged value. |
| C-12 | Handoff instruction isolated in dedicated, explicitly-labelled section | PASS | PHASE 4 -- HANDOFF. This section contains only the handoff instruction. No artifact bodies, no table rows. Anti-placeholder: Do not write the literal placeholder string this-file. |
| C-13 | REAL-REQUIRED flag accompanied by explanatory rationale | PASS | PHASE 3 rationale preamble scoped to all placements: A synthetic artifact cannot substitute for real signal in EVIDENCE-HEAVY namespaces. |
| C-14 | Explicit stop-gate phrase at each phase boundary | PASS | Three explicit gate sentences at CLASSIFY->GENERATE, GENERATE->SUMMARIZE, SUMMARIZE->HANDOFF. Each: Do not begin PHASE N until [specific output completeness criteria]. |
| C-15 | Artifact body content matches namespace category | PASS | PHASE 2 vocabulary rules block: HIGH-STRUCTURE -- Do not use interview language; EVIDENCE-HEAVY -- Do not use specification language. Per-category MUST/DO NOT explicit. |

```
composite = (5/5 x 60) + (3/3 x 30) + (7/7 x 10) = 100
```

**Score: 100 / 100 -- GOLDEN**

---

#### V-02 -- Pre-Printed Classification Skeleton

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All nine namespaces with MOCK ARTIFACT header blocks | PASS | Nine pre-printed section blocks with MOCK ARTIFACT header pre-filled |
| C-02 | Category classification correct for every namespace | PASS | Pre-printed table with prove/listen/trace categories fixed; others as bracketed choice |
| C-03 | REAL-REQUIRED flag on all EVIDENCE-HEAVY namespaces | PASS | prove/listen sections have REAL-REQUIRED note pre-printed; coverage table row pre-filled |
| C-04 | Coverage summary table with correct columns | PASS | Coverage summary pre-printed with all four columns |
| C-05 | Final line follows prescribed handoff pattern | PASS | HANDOFF block pre-printed with prescribed Next: line |
| C-06 | Tier 2/3 critical namespaces flagged | PASS | Coverage table: trace TIER-CRITICAL if tier >= 2, listen REAL-REQUIRED + TIER-CRITICAL pre-printed |
| C-07 | Each namespace section has plausible artifact body | PASS | Each section template has artifact body slot with category-appropriate hints in brackets |
| C-08 | Compliance-tagged topics pre-flagged | PASS | Coverage table flag rules include COMPLIANCE conditional |
| C-09 | Tier flag scopes output when --tier supplied | PASS | Tier captured; conditional logic in table rows |
| C-10 | Recommended next steps are actionable and namespace-specific | PASS | Recommended Next Step: exact skill call. Example: /trace:component topic |
| C-11 | Classification table generated before any artifact body | PASS | Pre-printed table is the first content block; structural guarantee: model fills table before writing artifact sections |
| C-12 | Handoff instruction isolated in dedicated, explicitly-labelled section | PASS | HANDOFF pre-printed as final section, isolated; anti-placeholder language present |
| C-13 | REAL-REQUIRED flag accompanied by explanatory rationale | PASS | prove section: REAL-REQUIRED: A synthetic artifact cannot substitute for real signal. listen section: equivalent. Full rationale at each application point. |
| C-14 | Explicit stop-gate phrase at each phase boundary | FAIL | No named phases. Prefatory instruction is not in the prescribed gate form (Do not begin X until Y is complete). Structural enforcement cannot substitute for the surface-level gate sentence C-14 requires. |
| C-15 | Artifact body content matches namespace category | PARTIAL | Positive guidance in brackets: use study/data/interview framing, use interface/contract language. No DO NOT prohibition clauses. Model directed toward correct register but not prohibited from incorrect register. |

```
composite = (5/5 x 60) + (3/3 x 30) + (5.5/7 x 10) = 60 + 30 + 7.86 = 97.86
```

**Score: 97.9 / 100 -- GOLDEN**

---

#### V-03 -- Category Vocabulary Mandates

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All nine namespaces with MOCK ARTIFACT header blocks | PASS | Section format prescribes MOCK ARTIFACT header for all nine |
| C-02 | Category classification correct for every namespace | PASS | STEP 1 classification table with MUST use / DO NOT use columns per namespace |
| C-03 | REAL-REQUIRED flag on all EVIDENCE-HEAVY namespaces | PASS | REAL-REQUIRED rule in STEP 1 and STEP 3 flag rules |
| C-04 | Coverage summary table with correct columns | PASS | STEP 3 coverage summary with all four columns |
| C-05 | Final line follows prescribed handoff pattern | PASS | STEP 4 HANDOFF section with correct Next: pattern |
| C-06 | Tier 2/3 critical namespaces flagged | PASS | TIER-CRITICAL rule in STEP 3 |
| C-07 | Each namespace section has plausible artifact body | PASS | Artifact body required per namespace in STEP 2 |
| C-08 | Compliance-tagged topics pre-flagged | PASS | COMPLIANCE flag rule present in STEP 3 |
| C-09 | Tier flag scopes output when --tier supplied | PASS | Tier captured; conditional flag logic in STEP 3 |
| C-10 | Recommended next steps are actionable and namespace-specific | PASS | exact skill call -- DO NOT write generic advice |
| C-11 | Classification table generated before any artifact body | PASS | Before writing any artifact body, assign every namespace to a category. Explicit ordering instruction with classification table as STEP 1 output. |
| C-12 | Handoff instruction isolated in dedicated, explicitly-labelled section | PASS | HANDOFF explicitly labeled, DO NOT write any other content in this section. Anti-placeholder present. |
| C-13 | REAL-REQUIRED flag accompanied by explanatory rationale | PASS | STEP 1 REAL-REQUIRED rule: Rationale embedded at rule invocation point, not as post-hoc annotation. |
| C-14 | Explicit stop-gate phrase at each phase boundary | FAIL | STEP 1-4 labels establish ordering but no explicit Do not begin STEP N+1 until STEP N output is complete gate sentences appear at boundaries. |
| C-15 | Artifact body content matches namespace category | PASS | Classification table has MUST use / DO NOT use columns per namespace row. STEP 2: Every artifact body MUST comply. Explicit prohibition: DO NOT use specification language in any EVIDENCE-HEAVY artifact body. |

```
composite = (5/5 x 60) + (3/3 x 30) + (6/7 x 10) = 60 + 30 + 8.57 = 98.57
```

**Score: 98.6 / 100 -- GOLDEN**

---

#### V-04 -- Named Phases + Pre-Printed Classification Skeleton

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All nine namespaces with MOCK ARTIFACT header blocks | PASS | Nine pre-printed section blocks with MOCK ARTIFACT header per phase order |
| C-02 | Category classification correct for every namespace | PASS | Pre-printed PHASE 1 table with prove/listen/trace categories fixed; fill-in for others |
| C-03 | REAL-REQUIRED flag on all EVIDENCE-HEAVY namespaces | PASS | prove/listen sections have REAL-REQUIRED inline; coverage table has REAL-REQUIRED pre-set |
| C-04 | Coverage summary table with correct columns | PASS | PHASE 3 coverage summary pre-printed with all four columns |
| C-05 | Final line follows prescribed handoff pattern | PASS | PHASE 4 HANDOFF block pre-printed with correct Next: pattern |
| C-06 | Tier 2/3 critical namespaces flagged | PASS | Coverage table conditional pre-printed for trace and listen |
| C-07 | Each namespace section has plausible artifact body | PASS | All nine sections have artifact body slots with category-specific bracket hints |
| C-08 | Compliance-tagged topics pre-flagged | PASS | COMPLIANCE flag rule in coverage table |
| C-09 | Tier flag scopes output when --tier supplied | PASS | Tier captured; conditional logic in PHASE 1 and coverage table rows |
| C-10 | Recommended next steps are actionable and namespace-specific | PASS | exact skill call /skill:subskill topic instruction in PHASE 3 |
| C-11 | Classification table generated before any artifact body | PASS | Doubly guaranteed: pre-printed table is first content block (structural) + gate Do not begin PHASE 2 until all nine rows in the Classification Table are filled (procedural). |
| C-12 | Handoff instruction isolated in dedicated, explicitly-labelled section | PASS | PHASE 4 HANDOFF pre-printed; isolated; anti-placeholder present. |
| C-13 | REAL-REQUIRED flag accompanied by explanatory rationale | PASS | prove/listen sections: REAL-REQUIRED rationale inline at each application point. |
| C-14 | Explicit stop-gate phrase at each phase boundary | PASS | Three explicit gates: Do not begin PHASE 2 / Do not begin PHASE 3 / Do not begin PHASE 4. Each references specific completeness criteria. |
| C-15 | Artifact body content matches namespace category | PARTIAL | Category-specific bracket hints (e.g., HIGH-STRUCTURE: state transitions, trigger conditions). No DO NOT prohibition clauses. Guidance toward correct register without prohibition of incorrect register. |

```
composite = (5/5 x 60) + (3/3 x 30) + (6.5/7 x 10) = 60 + 30 + 9.29 = 99.29
```

**Score: 99.3 / 100 -- GOLDEN**

---

#### V-05 -- Full Ceiling (Pre-Printed + Stop-Gates + Vocabulary Mandates)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All nine namespaces with MOCK ARTIFACT header blocks | PASS | Nine pre-printed section blocks with MOCK ARTIFACT header |
| C-02 | Category classification correct for every namespace | PASS | Pre-printed PHASE 1 table with prove/listen/trace/topic categories fixed |
| C-03 | REAL-REQUIRED flag on all EVIDENCE-HEAVY namespaces | PASS | REAL-REQUIRED inline in prove/listen; coverage table pre-set; PHASE 1 rule block |
| C-04 | Coverage summary table with correct columns | PASS | PHASE 3 coverage summary pre-printed with all four columns |
| C-05 | Final line follows prescribed handoff pattern | PASS | PHASE 4 HANDOFF pre-printed with correct Next: pattern |
| C-06 | Tier 2/3 critical namespaces flagged | PASS | Coverage table conditional pre-printed for trace and listen |
| C-07 | Each namespace section has plausible artifact body | PASS | All nine sections have artifact body slots with vocabulary-enforcement brackets |
| C-08 | Compliance-tagged topics pre-flagged | PASS | COMPLIANCE flag rule in PHASE 3 |
| C-09 | Tier flag scopes output when --tier supplied | PASS | Tier captured; conditional logic in table rows |
| C-10 | Recommended next steps are actionable and namespace-specific | PASS | DO NOT write generic advice + exact skill identifier required |
| C-11 | Classification table generated before any artifact body | PASS | Pre-printed table is first content block (structural) + Do not begin PHASE 2 until every cell in the Classification Table is filled. Doubly guaranteed. |
| C-12 | Handoff instruction isolated in dedicated, explicitly-labelled section | PASS | PHASE 4 HANDOFF pre-printed; Do not add artifact bodies, table rows, or other content here; anti-placeholder present. |
| C-13 | REAL-REQUIRED flag accompanied by explanatory rationale | PASS | PHASE 1 rule block: prove and listen are EVIDENCE-HEAVY. A synthetic artifact cannot substitute for real signal. Embedded before any application point. |
| C-14 | Explicit stop-gate phrase at each phase boundary | PASS | Three explicit stop-gate sentences at CLASSIFY->GENERATE, GENERATE->SUMMARIZE, SUMMARIZE->HANDOFF. GENERATE gate specifies vocabulary-compliant artifact bodies as completeness criterion. |
| C-15 | Artifact body content matches namespace category | PASS | Strongest C-15 mechanism: MUST use / DO NOT use columns in PHASE 1 table (visible at point of category assignment). PHASE 2 section brackets reinforce with explicit DO NOT per namespace. Rules present at both assignment and generation. |

```
composite = (5/5 x 60) + (3/3 x 30) + (7/7 x 10) = 100
```

**Score: 100 / 100 -- GOLDEN**

---

### C-14/C-15 Discriminator Map

| Variation | C-14 | C-15 | Score delta vs ceiling |
|-----------|------|------|----------------------|
| V-01 | PASS (stop-gate phrases) | PASS (DO NOT rules in vocabulary block) | 0 |
| V-02 | FAIL (no gate phrases, no named phases) | PARTIAL (bracket hints only) | -2.14 |
| V-03 | FAIL (STEP labels, no gate phrases) | PASS (MUST/DO NOT table columns) | -1.43 |
| V-04 | PASS (stop-gate phrases) | PARTIAL (bracket hints, no DO NOT) | -0.71 |
| V-05 | PASS (stop-gate phrases) | PASS (table columns + section bracket DO NOT) | 0 |

The failing pattern: V-02 and V-03 use structural or table-based ordering but omit explicit Do not begin X until Y gate sentences. C-14 cannot be satisfied by implied ordering -- the gate must be a surface-level instruction in that specific imperative form.

The partial C-15 pattern: V-02 and V-04 provide positive vocabulary guidance but omit prohibition. Explicit DO NOT prohibition is required to close C-15.

---

### V-01 Surprise Finding

V-01 was designed as a single-axis lifecycle-emphasis variation targeting C-14. Its PHASE 2 vocabulary rules block includes explicit per-category MUST use / DO NOT use rules that also satisfy C-15 -- a criterion V-01 was not designed to target. This confirms that vocabulary DO NOT rules are independently sufficient for C-15 without structural table-column anchoring. V-03 single-axis result confirms the same finding.

Round 4 question: Does V-01 global vocabulary block (one rules block for all namespaces) produce as reliable C-15 compliance as V-05 per-section DO NOT rules in live model runs? Both score identically on prompt design, but V-05 structural anchoring should reduce model-drift risk in execution.

---

### New Patterns

**Pattern 1 -- Stop-gate completeness specification:** V-01/V-04/V-05 gate phrases enumerate specific required output fields (all nine namespaces have an assigned category, vocabulary rules, Tier 2/3 Critical value, and Compliance-Tagged value) rather than generic completion (until the table is done). Specificity makes the gate self-checkable. V-05 GENERATE gate adds vocabulary-compliant artifact bodies as an explicit completeness criterion, extending the gate to cover C-15 compliance at the phase boundary.

**Pattern 2 -- Vocabulary-column anchoring in classification table:** V-05 embeds MUST use / DO NOT use vocabulary rules as columns in the PHASE 1 classification table itself. Rules are visible at the same moment the model assigns categories. This is a stronger structural guarantee than a separate vocabulary block (V-01) or per-section bracket hints (V-02/V-04), because the model cannot proceed past PHASE 1 without seeing the vocabulary rules for every namespace it will write.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Stop-gate completeness specification: gate phrases that enumerate specific required output fields (all nine namespaces, named field types) rather than generic completion signals make gates self-checkable and resistant to partial-output bypass", "Vocabulary-column anchoring: embedding MUST/DO NOT vocabulary rules as columns in the classification table registers category-appropriate register constraints at the category assignment step, before any artifact body is written"]}
```

