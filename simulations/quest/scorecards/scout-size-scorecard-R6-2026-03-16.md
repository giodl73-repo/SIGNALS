## Scout-Size Scorecard — R6

**Variations file**: `simulations/quest/golden/scout-size-variate-R6-2026-03-16.md`
**Rubric**: v6 (C-01 through C-20)

---

### Scoring Key

| Symbol | Meaning | Weight |
|--------|---------|--------|
| PASS | Criterion satisfied | 1.0 |
| PARTIAL | Partially satisfied | 0.5 |
| FAIL | Not satisfied | 0.0 |

---

## V-01 — Role Sequence

### Essential (C-01–C-05)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Section 1.1 names individual integration points with count; format example shows named list + count; "A general description such as 'several API layers'... fails" stated. |
| C-02 | PASS | "Assign exactly one tier: LOW / MEDIUM / HIGH / XL" with explicit "no substitutions" implied by vocabulary section. |
| C-03 | PASS | Section 2.2 requires workaround name AND cost direction; "An output that mentions the workaround without a cost direction fails this field" stated inline. |
| C-04 | PASS | Section 1.5 requires level (HIGH / MEDIUM / LOW) plus what IS established; "A bare 'confidence: HIGH' with no basis fails." |
| C-05 | PASS | "No task breakdowns, sprint assignments, owner names, or milestone dates" in opening paragraph. |

All 5 essential: **PASS** → 60 pts

### Recommended (C-06–C-08)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | "Name the specialist disciplines needed — not just headcount." Format: "1 backend engineer, 1 platform engineer, 0.5 PM." |
| C-07 | PASS | "Give a sprint range. Not a calendar date. Not a single fixed number." Format: "3–5 sprints." |
| C-08 | PASS | "Name the one or two factors that most drive this rating. 'It's complex' is not a complexity driver." |

All 3 recommended: **PASS** → 30 pts

### Aspirational (C-09–C-20)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Section 2.3 requires tier-up and tier-down conditions explicitly. |
| C-10 | PASS | Section 2.4: "State what information or investigation result would materially raise or lower the stated confidence level." |
| C-11 | PASS | Section 2.1: "Name the specific thing that is NOT yet known or verified — the primary source of residual uncertainty." Different-dimension requirement stated. |
| C-12 | PASS | "A single, named, specific scenario — not a list of factors" explicitly required. |
| C-13 | PASS | Format slot `Tier rises to [LEVEL] if:` / `Tier drops to [LEVEL] if:` — destination tier is a named field slot. |
| C-14 | PASS | "Falsifiable — a reader must be able to state what investigation would settle it." |
| C-15 | PASS | Charter violation test: "If your gap says 'X is not confirmed' and the Analyst's basis says 'X is established,' you have violated your charter." Structural prohibition via role charter. |
| C-16 | PASS | "Landing on a tier different from the currently assigned tier" stated as a condition bullet. |
| C-17 | PARTIAL | Abstract charter-violation pattern ("X is not confirmed" / "X is established") covers C-15 failure mode; format example gives CORRECT for C-11 gap but no WRONG. No example for C-16 same-tier failure mode. Two of three required failure modes partially covered — not all three with concrete named WRONG/CORRECT blocks. |
| C-18 | PARTIAL | `[LEVEL]` slot in sensitivity format is partially structural; but the C-16 "must differ" constraint is prose-only (bullet list), not embedded in the field label itself. C-13 partially satisfied by slot; C-16 not encoded as label. |
| C-19 | PASS | All inline descriptions (charter violation test, format examples) appear within their fields, not in a post-output checklist. No end-of-prompt gate section exists. |
| C-20 | PASS | **V-01's defining mechanism.** Phase 1 charter: "Do not produce the confidence gap — that is the Risk Assessor's charter." Phase 2 charter: explicitly prohibited from restating/negating Analyst's confirmed dimension. Conflation = charter violation. |

Aspirational: 10 PASS + 2 PARTIAL → 11.0 / 12 → **9.17 pts**

**V-01 Composite: 60 + 30 + 9.17 = 99.2** | Golden: YES

---

## V-02 — Structural Format Encoding

### Essential (C-01–C-05)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Surface area table with "name individually" column header; Total row required; "Several API interactions is not a named integration point." |
| C-02 | PASS | Field label "Tier [exactly one: LOW / MEDIUM / HIGH / XL]"; downstream parsing cited; failure examples listed. |
| C-03 | PASS | Inertia Check section with Cost direction field; "An output that mentions the workaround without a cost direction fails this field." |
| C-04 | PASS | Confidence Level + Basis fields with non-overlap rule. |
| C-05 | PASS | Signal boundary stated in opening. |

All 5 essential: **PASS** → 60 pts

### Recommended (C-06–C-08)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Specialist Type table with "name the discipline" column header. |
| C-07 | PASS | Sprint range field label "N–M format — not a calendar date, not a single number." |
| C-08 | PASS | Primary driver field "one or two named factors — not 'it's complex'" in field label. |

All 3 recommended: **PASS** → 30 pts

### Aspirational (C-09–C-20)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Sensitivity table with tier-up and tier-down rows. |
| C-10 | PASS | Confidence Calibration section with raise/lower sub-fields. |
| C-11 | PASS | Gap field: "must address a DIFFERENT dimension than the Basis field above" embedded in field label. |
| C-12 | PASS | "Single Named Condition" column header in sensitivity table. |
| C-13 | PASS | Column header "Destination Tier [must differ from current tier: fill with LOW / MEDIUM / HIGH / XL]". |
| C-14 | PASS | "falsifiable — state how to confirm" in sensitivity table column header. |
| C-15 | PASS | Non-overlap rule block under Gap with concrete named WRONG: "A gap that says 'API contract is not yet confirmed' when the basis says 'API contract is established' violates this rule." |
| C-16 | PASS | Column labels "[must be HIGHER than the tier assigned above]" / "[must be LOWER than the tier assigned above]" directly in table. |
| C-17 | PARTIAL | C-15 failure mode has a concrete named WRONG example inline. C-11 gap has the "different dimension" instruction but no WRONG example block. C-16 failure mode is expressed as a structural label rather than a named WRONG/CORRECT pair. Two of three required modes — one covered, one structural, one absent as WRONG/CORRECT. |
| C-18 | PASS | **V-02's defining mechanism.** Sensitivity table column "[must be HIGHER than the tier assigned above]" and "[must be LOWER]" encode C-13 and C-16 as named column labels — violations visible in the skeleton. |
| C-19 | PASS | Non-overlap example appears within the Gap field (not post-output). Sensitivity column labels precede the table rows. No end-of-prompt checklist. |
| C-20 | FAIL | No role separation. Non-overlap rule is stated as inline prose/text, not enforced by a phase charter. A model could violate C-15 without violating any role mandate. |

Aspirational: 10 PASS + 1 PARTIAL + 1 FAIL → 10.5 / 12 → **8.75 pts**

**V-02 Composite: 60 + 30 + 8.75 = 98.8** | Golden: YES

---

## V-03 — Inline Failure Examples

### Essential (C-01–C-05)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Field 1 has WRONG ("touches several API layers") / CORRECT ("API endpoint (auth), event bus subscription (order-placed)... — 4 integration points"). |
| C-02 | PASS | Field 2 has three WRONG examples ("MODERATE", "3/5", "complex feature") and CORRECT ("HIGH"). |
| C-03 | PASS | Field 9 has WRONG ("Users currently use a spreadsheet" — no cost direction) / CORRECT (workaround named + "building is cheaper" + reasoning). |
| C-04 | PASS | Field 5 has WRONG ("Confidence: HIGH" — no basis) / CORRECT with level, basis, and dimension named. |
| C-05 | PASS | Signal boundary in opening paragraph. |

All 5 essential: **PASS** → 60 pts

### Recommended (C-06–C-08)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Field 3: WRONG ("3 engineers") / CORRECT ("1 backend engineer, 1 platform engineer, 0.5 PM"). |
| C-07 | PASS | Field 4: WRONG ("Q3 delivery", "4 sprints") / CORRECT ("3–5 sprints"). |
| C-08 | PASS | Field 2 sub-field: "Primary complexity driver [one or two named factors — not 'it's complex']". |

All 3 recommended: **PASS** → 30 pts

### Aspirational (C-09–C-20)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Fields 7 and 8 with WRONG/CORRECT for each direction. |
| C-10 | PASS | Field 10: "State what would materially raise or lower the stated confidence level." |
| C-11 | PASS | Field 6: WRONG shows same-dimension gap; CORRECT shows different-dimension gap with named delivery semantics. |
| C-12 | PASS | Fields 7-8: "State one single, named, falsifiable condition" with format. |
| C-13 | PASS | Format: "Tier rises to [LEVEL] if:" — destination tier is a named required slot. |
| C-14 | PASS | "falsifiable" in both fields with how-to-confirm format. WRONG examples ("If requirements change") illustrate non-falsifiable failure. |
| C-15 | PASS | Field 6 WRONG/CORRECT explicitly shows same-dimension violation (basis: "API contract is established" → gap: "API contract has not been confirmed"). |
| C-16 | PASS | Fields 7-8 WRONG: "Current tier is HIGH. 'Tier rises to HIGH if offline sync is required.'" — named same-tier WRONG example for both directions. |
| C-17 | PASS | **V-03's defining mechanism.** All three required failure modes have WRONG/CORRECT blocks immediately before their fields: C-11 (Field 6), C-15 (Field 6), C-16 (Fields 7–8). Concrete named examples throughout. |
| C-18 | PARTIAL | Format slots `[LEVEL]` in sensitivity fields are partially structural, but sensitivity is expressed as prose format templates rather than table column headers. C-13 is a named slot; C-16 is embedded in prose instruction rather than a column label. |
| C-19 | PASS | All WRONG/CORRECT blocks appear immediately before their governing fields. Fields proceed in order 1–10; no WRONG/CORRECT block appears after the last field it governs. No post-output checklist. |
| C-20 | FAIL | No role separation. Inline examples guard generation-time drift in individual fields but do not structurally prevent relational conflation via charter architecture. |

Aspirational: 10 PASS + 1 PARTIAL + 1 FAIL → 10.5 / 12 → **8.75 pts**

**V-03 Composite: 60 + 30 + 8.75 = 98.8** | Golden: YES

---

## V-04 — Inertia Framing

### Essential (C-01–C-05)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Step 2: "Name each integration point the feature must touch. Provide a total count." Format provided. |
| C-02 | PASS | Step 3: "Assign exactly one: LOW / MEDIUM / HIGH / XL." |
| C-03 | PASS | **V-04's defining mechanism.** Step 1 Status-Quo Baseline is the first analytical step; explicitly requires workaround name AND cost direction before any surface area or complexity work. "An output that mentions the workaround without a cost direction fails this field." Contextual framing note explains why: "A HIGH complexity signal against a cheap, stable workaround is a strong signal to defer." |
| C-04 | PASS | Step 6: Level, Basis, Gap, Calibration all required. |
| C-05 | PASS | "No task breakdowns, sprint assignments, owner names, or milestone dates." |

All 5 essential: **PASS** → 60 pts

### Recommended (C-06–C-08)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | "Name the specialist disciplines needed. Headcount alone fails." Format provided. |
| C-07 | PASS | "Give a sprint range — not a calendar date, not a single fixed number." Format "N–M sprints." |
| C-08 | PASS | "Name the one or two factors that most drive this rating. 'It's complex' is not a complexity driver." |

All 3 recommended: **PASS** → 30 pts

### Aspirational (C-09–C-20)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Step 7 requires tier-up and tier-down conditions with format. |
| C-10 | PASS | Calibration field in Step 6. |
| C-11 | PASS | Step 6 Gap: "what is NOT yet known — the primary source of residual uncertainty." |
| C-12 | PASS | "A single named scenario — not a list, not a hedge" stated with failure illustration ("If requirements change is not a condition — it is a deferral"). |
| C-13 | PASS | Format: "Tier rises to [LEVEL] if:" — slot required. |
| C-14 | PASS | "Be falsifiable: name what action would settle it." "If requirements change" explicitly named as non-falsifiable. |
| C-15 | PASS | Non-overlap requirement: "If your basis is 'API contract is established,' your gap must name a different dimension — delivery behavior, error semantics, load characteristics — not 'API contract is unconfirmed.'" Concrete named WRONG pattern inline. |
| C-16 | PASS | "Land on a tier different from the currently assigned tier." |
| C-17 | PARTIAL | C-15 failure mode has a concrete named wrong pattern inline adjacent to the gap field. Sensitivity section names "'If requirements change' is not a condition" but this addresses falsifiability (C-14), not same-tier destination (C-16). C-16's documented failure mode has no WRONG/CORRECT example. Two of three required failure modes — one complete, one missing. |
| C-18 | PARTIAL | Format slots `[LEVEL]` present in sensitivity bullets; but both C-13 and C-16 constraints are in prose bullets under Step 7, not embedded in field label slots or column headers. |
| C-19 | PASS | All inline descriptions appear within their steps, not post-output. No checklist section after the output fields. |
| C-20 | FAIL | No role separation. Basis/gap are produced in the same step (Step 6) by the same "role." Non-overlap is a prose rule, not a charter prohibition. |

Aspirational: 9 PASS + 2 PARTIAL + 1 FAIL → 10.0 / 12 → **8.33 pts**

**V-04 Composite: 60 + 30 + 8.33 = 98.3** | Golden: YES

---

## V-05 — Multi-Axis Combination

### Essential (C-01–C-05)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Surface area table with WRONG/CORRECT ("several API layers" → "API endpoint (auth)... — 4 integration points") preceding the table; Total row required. |
| C-02 | PASS | WRONG/CORRECT block ("MODERATE" / "3/5" / "complex" → "HIGH") before Tier field; field label "exactly one: LOW / MEDIUM / HIGH / XL." |
| C-03 | PASS | Section 7 Inertia Check with WRONG ("named but no cost direction") / CORRECT (workaround + cost direction + reasoning); three required sub-fields. |
| C-04 | PASS | Section 5 with WRONG ("Confidence: HIGH — no basis stated") / CORRECT; Level and Basis required fields. |
| C-05 | PASS | "No task breakdowns, sprint assignments, owner names, or milestone dates" in opening. |

All 5 essential: **PASS** → 60 pts

### Recommended (C-06–C-08)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Team-size table with "name the discipline" column + WRONG/CORRECT preceding table. |
| C-07 | PASS | Sprint range field label "N–M format" + WRONG/CORRECT ("Q3 delivery" / "4 sprints" → "3–5 sprints"). |
| C-08 | PASS | Primary driver field "one or two named factors — not 'it's complex'" in field label. |

All 3 recommended: **PASS** → 30 pts

### Aspirational (C-09–C-20)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Section 8 sensitivity table with tier-up and tier-down rows; WRONG/CORRECT preceding table. |
| C-10 | PASS | Section 9: raise/lower sub-fields. |
| C-11 | PASS | Section 6 with WRONG/CORRECT (charter violation example: same-dimension gap = WRONG; different-dimension gap = CORRECT). |
| C-12 | PASS | "Single Named Condition" column header in sensitivity table. |
| C-13 | PASS | Column header "Destination Tier [fill with LOW / MEDIUM / HIGH / XL — must DIFFER from current tier]." |
| C-14 | PASS | "falsifiable — state how to confirm" in table column header. WRONG example "If requirements change" illustrates failure. |
| C-15 | PASS | Phase 2 charter: "explicitly prohibited from restating or negating what the Analyst confirmed"; charter violation test with named WRONG pattern in Section 6; structural + WRONG/CORRECT enforcement combined. |
| C-16 | PASS | Column headers "[must be HIGHER than the tier in Field 2]" / "[must be LOWER than the tier in Field 2]" encode constraint structurally; WRONG block: "Current tier is HIGH. 'Tier rises to HIGH if offline sync is required.'" |
| C-17 | PASS | All three required failure modes have named WRONG/CORRECT blocks immediately preceding their fields: C-11/C-15 — Section 6 block (charter violation = WRONG, different-dimension = CORRECT); C-16 — Section 8 block (same-tier WRONG named with current tier and XL condition as CORRECT). |
| C-18 | PASS | Sensitivity table column headers encode C-13 and C-16 as named column labels — violations visible in the skeleton. Team table, surface area table also structurally encoded. |
| C-19 | PASS | All WRONG/CORRECT blocks appear before the fields they govern. STOP gate ("STOP. Do not produce the confidence gap. Pass to Phase 2.") appears at the end of Phase 1 output fields, before Phase 2 begins. No post-output checklist. |
| C-20 | PASS | Phase 1 charter: "Producing the gap in Phase 1 is a charter violation." Phase 2 charter: "explicitly prohibited from restating or negating what the Analyst confirmed. Charter violation test: If your gap says 'X is not confirmed'... stop and name a different dimension entirely." |

Aspirational: 12 / 12 PASS → **10.0 pts**

**V-05 Composite: 60 + 30 + 10 = 100** | Golden: YES

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 5/5 (60) | 3/3 (30) | 11.0/12 (9.17) | **99.2** | YES |
| V-02 | 5/5 (60) | 3/3 (30) | 10.5/12 (8.75) | **98.8** | YES |
| V-03 | 5/5 (60) | 3/3 (30) | 10.5/12 (8.75) | **98.8** | YES |
| V-04 | 5/5 (60) | 3/3 (30) | 10.0/12 (8.33) | **98.3** | YES |
| **V-05** | 5/5 (60) | 3/3 (30) | **12/12 (10.0)** | **100** | YES |

**Ranking**: V-05 > V-01 > V-02 = V-03 > V-04

---

## Excellence Signals from V-05

**What made V-05 the top scorer:**

1. **Explicit STOP gate at phase boundary as a generation-time interrupt** — "STOP. Do not produce the confidence gap. Pass to Phase 2." placed at the exact output field where charter violation would occur. This is distinct from merely having two sections: the gate instruction appears mid-prompt at the natural temptation point, making phase boundary violation require actively overriding an imperative command.

2. **Multi-mechanism layering is additive, not redundant** — Role separation (C-20) guards relational constraints between field pairs; structural column headers (C-18) guard single-field tier value constraints; inline WRONG/CORRECT blocks (C-17/C-19) guard generation-time drift in high-failure individual fields. Each mechanism addresses a different failure vector. Combined, they produce full aspirational coverage with no mechanism competing with another — the role charter and the WRONG/CORRECT blocks both govern Section 6 from different angles simultaneously.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Explicit STOP gate at the natural temptation point — a single imperative sentence placed mid-prompt at the exact field where charter violation would occur, making phase-boundary violation require overriding a direct command rather than just ignoring structural sections", "Multi-mechanism layering is additive: role separation guards relational field pairs, structural column headers guard single-field tier values, and inline WRONG/CORRECT blocks guard generation-time drift — three mechanisms address three distinct failure vectors with no overlap, producing full aspirational coverage"]}
```
