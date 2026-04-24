# scout-size — Quest Score R4 (Rubric v4)

## Criterion Reference

| ID | Weight | Category | Key requirement |
|----|--------|----------|----------------|
| C-01 | essential | format | Tier is exactly LOW/MEDIUM/HIGH/XL |
| C-02 | essential | format | Timeline is a sprint range (N–M), not point estimate |
| C-03 | essential | coverage | Surface area is named/counted (2+ distinct points or explicit 0-1) |
| C-04 | essential | coverage | Inertia check names workaround + characterizes cost |
| C-05 | essential | depth | Confidence level present with basis |
| C-06 | recommended | depth | Team-size names specializations, not just headcount |
| C-07 | recommended | depth | Complexity tier justified with at least one driver |
| C-08 | recommended | behavior | AMEND modifies output (default pass if no AMEND) |
| C-09 | aspirational | depth | At least one explicit scope exclusion named |
| C-10 | aspirational | depth | Break-even signal present (or "Cannot assess — reason") |
| C-11 | aspirational | depth | Each specialization names its implementation ownership area |
| C-12 | aspirational | depth | Named specific unknowns that would move confidence |
| C-13 | aspirational | depth | Synthesis cross-references 2+ dimensions, not juxtaposition |
| C-14 | aspirational | structure | Open unknowns in a dedicated section with Unknown/Impact/Movement typed fields |
| C-15 | aspirational | depth | Preliminary hypothesis pre-dates analysis; synthesis confirms or revises it |
| C-16 | aspirational | behavior | AMEND cascades to synthesis when amended dimension appears there (default pass) |
| C-17 | aspirational | depth | At least one aspirational section names its anti-pattern |
| C-18 | aspirational | structure | Pre-analysis structural gate precedes first analysis section with scope+break-even as preconditions |
| C-19 | aspirational | structure | Adjacent sections carry explicit prohibition rules closing them against canonical-home content |

Scoring model: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/11 × 10)`

---

## V-01 — Axis: Pre-write gate only

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | "exactly one of: LOW / MEDIUM / HIGH / XL — no other values" |
| C-02 | PASS | "sprint range — 'N–M sprints' — not a point estimate, not a calendar date" |
| C-03 | PASS | Table with Total row required; "A general description without named points fails" |
| C-04 | PASS | Workaround / Maintenance cost / Cost direction all required; "one word" verdict enforced |
| C-05 | PASS | Confidence + Basis required in CONFIDENCE section |
| C-06 | PASS | "specialist disciplines + FTE fractions + implementation ownership per role" |
| C-07 | PASS | "Primary driver: [the one or two factors most responsible for this tier]" |
| C-08 | PASS | No AMEND present — default pass |
| C-09 | PASS | PRE-FLIGHT GATE forces "Out-of-scope boundary" with "Do not say 'TBD'" stop guard |
| C-10 | PASS | PRE-FLIGHT GATE forces "Break-even signal" with explicit "Cannot assess — [reason]" fallback |
| C-11 | PASS | "implementation ownership per role" explicitly required in TEAM AND TIMELINE |
| C-12 | PASS | OPEN UNKNOWNS requires concrete specifics; "A generic placeholder like 'dependencies may exist' fails" |
| C-13 | PASS | SYNTHESIS requires cross-referencing two dimensions; "conclusion must not be derivable from any single dimension alone" |
| C-14 | PASS | OPEN UNKNOWNS is a separate section with Unknown: / Impact: / Movement: typed fields |
| C-15 | FAIL | No MANDATORY OPENING: PRELIMINARY HYPOTHESIS section; no pre-analysis commitment to revise |
| C-16 | PASS | No AMEND — default pass |
| C-17 | PASS | SYNTHESIS names anti-pattern: "Restating each section in sequence... is juxtaposition, not synthesis" with example |
| C-18 | PASS | PRE-FLIGHT GATE fires before INERTIA CHECK; has both scope boundary + break-even fields; explicit "STOP: Do not proceed" instruction |
| C-19 | PARTIAL | CONFIDENCE has "Do not list unknowns here. Unknowns go in the OPEN UNKNOWNS section below." — unknowns canonical home is closed. But no section adjacent to the scope exclusion canonical home (PRE-FLIGHT GATE) carries an explicit prohibition; SURFACE AREA and COMPLEXITY have no "do not include scope exclusions here" guard. One of two canonical homes is closed; the other is not. Fails C-19 minimum-pass requirement. |

**Aspirational pass: 9/11** (C-15 FAIL, C-19 PARTIAL→FAIL)

**Composite: 60 + 30 + (9/11 × 10) = 98.2**

---

## V-02 — Axis: Prohibition guards only

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | "LOW / MEDIUM / HIGH / XL — exactly this vocabulary" |
| C-02 | PASS | "'N–M sprints' form required" |
| C-03 | PASS | Table + Total row; "Total row required" |
| C-04 | PASS | Workaround / Maintenance cost / Cost direction fields; one-word verdict |
| C-05 | PASS | Confidence + Basis in CONFIDENCE section |
| C-06 | PASS | "specialist disciplines + FTE fractions + implementation ownership area per role" |
| C-07 | PASS | "Primary driver: [one or two factors most responsible]" |
| C-08 | PASS | No AMEND — default pass |
| C-09 | PASS | SCOPE EXCLUSIONS canonical section at end is required: "State at least one explicit exclusion... If full scope: 'No exclusions — full scope assumed.'" |
| C-10 | FAIL | No break-even field anywhere. INERTIA CHECK has workaround / maintenance cost / cost direction but no break-even estimate. No PRE-FLIGHT GATE. |
| C-11 | PASS | "implementation ownership area per role" required |
| C-12 | PASS | OPEN UNKNOWNS with concrete typed fields; anti-placeholder guard |
| C-13 | PASS | SYNTHESIS requires cross-reference; anti-pattern noted |
| C-14 | PASS | OPEN UNKNOWNS is canonical section; CONFIDENCE and SYNTHESIS both explicitly closed against unknowns |
| C-15 | FAIL | No preliminary hypothesis section |
| C-16 | PASS | No AMEND — default pass |
| C-17 | PASS | SYNTHESIS: "Restating sections in sequence is juxtaposition, not synthesis." OPEN UNKNOWNS: "A generic placeholder like 'dependencies may exist' fails." Both aspirational sections name anti-patterns. |
| C-18 | FAIL | No PRE-FLIGHT GATE; first analysis section is INERTIA CHECK with no precondition gate |
| C-19 | PASS | SURFACE AREA: "Do not include scope exclusions here. Scope exclusions belong in SCOPE EXCLUSIONS below." COMPLEXITY: "Do not list what is out of scope here." CONFIDENCE: "Do not list unknowns here... listing an unknown creates a second, structurally invisible record." SYNTHESIS: closed against both unknowns and scope exclusions. OPEN UNKNOWNS: "Do not list unknowns in CONFIDENCE above or in SYNTHESIS below." Comprehensive bilateral closure. |

**Aspirational pass: 8/11** (C-10 FAIL, C-15 FAIL, C-18 FAIL)

**Composite: 60 + 30 + (8/11 × 10) = 97.3**

---

## V-03 — Axes: Pre-write gate + Prohibition guards (minimal)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | "exactly: LOW / MEDIUM / HIGH / XL" |
| C-02 | PASS | "N–M sprints" |
| C-03 | PASS | Table + Total row required |
| C-04 | PASS | Workaround / Maintenance cost / Cost direction required |
| C-05 | PASS | Confidence + Basis |
| C-06 | PASS | "specialist disciplines + FTE fractions + implementation ownership per role" |
| C-07 | PASS | "Primary driver" required |
| C-08 | PASS | No AMEND — default pass |
| C-09 | PASS | PRE-FLIGHT GATE forces "Out-of-scope boundary" before all analysis |
| C-10 | PASS | PRE-FLIGHT GATE forces "Break-even signal" before all analysis |
| C-11 | PASS | Implementation ownership per role required |
| C-12 | PASS | OPEN UNKNOWNS with concrete typed fields required |
| C-13 | PASS | SYNTHESIS requires cross-reference; blockquote anti-pattern: "is juxtaposition — it fails this section" |
| C-14 | PASS | OPEN UNKNOWNS is a separate section with Unknown:/Impact:/Movement: typed fields; both CONFIDENCE and SYNTHESIS explicitly closed |
| C-15 | FAIL | No MANDATORY OPENING: PRELIMINARY HYPOTHESIS; no pre-analysis estimate to revise in synthesis |
| C-16 | PASS | No AMEND — default pass |
| C-17 | PASS | SYNTHESIS blockquote: "**Anti-pattern**: Restating sections in sequence... is juxtaposition — it fails this section." Explicit failure mode label. |
| C-18 | PASS | PRE-FLIGHT GATE: "Resolve both fields before proceeding to any analysis section. This gate fires before all other sections." Contains scope boundary + break-even fields with specific response required; "Do not proceed to INERTIA CHECK until both fields contain specific responses." |
| C-19 | PASS | CONFIDENCE: "Do not list unknowns here. Unknowns belong in OPEN UNKNOWNS below." SURFACE AREA: "Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE above." COMPLEXITY: "Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE." OPEN UNKNOWNS: "Do not list unknowns in CONFIDENCE above or in SYNTHESIS below — those sections are closed against unknowns." Both canonical homes have adjacent sections explicitly closed. |

**Aspirational pass: 10/11** (C-15 FAIL only)

**Composite: 60 + 30 + (10/11 × 10) = 99.1**

---

## V-04 — Axes: Pre-write gate + Prohibition guards + R3 V-05 (17-criterion self-check)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Tier vocabulary enforced; self-check C-01 |
| C-02 | PASS | Sprint range enforced; self-check C-02 |
| C-03 | PASS | Table + Total row; self-check C-03 |
| C-04 | PASS | Inertia fields enforced; self-check C-04 |
| C-05 | PASS | Confidence + Basis; self-check C-05 |
| C-06 | PASS | Specializations + ownership; self-check C-06 |
| C-07 | PASS | Complexity driver; self-check C-07 |
| C-08 | PASS | No AMEND — default pass; self-check C-08 |
| C-09 | PASS | PRE-FLIGHT GATE forces scope boundary; self-check C-09 includes canonical location note |
| C-10 | PASS | PRE-FLIGHT GATE forces break-even; self-check C-10 |
| C-11 | PASS | Ownership per role; self-check C-11 |
| C-12 | PASS | Named unknowns required; self-check C-12 |
| C-13 | PASS | Cross-signal synthesis required; self-check C-13; failure mode blockquote in STEP 7 |
| C-14 | PASS | STEP 6 is a dedicated unknowns section with typed fields; STEP 5 explicitly closed; self-check C-14 |
| C-15 | PASS | MANDATORY OPENING: PRELIMINARY HYPOTHESIS commits a tier and sprint range before STEP 1. STEP 7 requires explicit confirm/revise statement with three template forms. Self-check C-15. |
| C-16 | PASS | AMEND INSTRUCTION in STEP 7: "If AMEND directive is present... re-read this synthesis. If the amended dimension appears in the synthesis conclusion, update or explicitly reaffirm." Self-check C-16. No AMEND present → default pass. |
| C-17 | PASS | STEP 6: "FAILURE MODE FOR THIS SECTION" blockquote. STEP 7: "FAILURE MODE FOR THIS SECTION" blockquote naming juxtaposition by example. Self-check C-17. |
| C-18 | PASS | PRE-FLIGHT GATE fires before MANDATORY OPENING (which is itself analysis commitment). "STOP: Do not proceed to MANDATORY OPENING until both fields above contain specific responses." Scope boundary + break-even fields. Self-check C-09, C-10 confirm canonical location. |
| C-19 | PASS | STEP 2: "Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE." STEP 3: same prohibition. STEP 5: "this section is explicitly closed against unknowns." STEP 6: "Do not include scope exclusions here... Do not include break-even observations here." Full bilateral closure; 17-criterion self-check includes C-09 and C-10 verification. |

**Aspirational pass: 11/11**

**Composite: 60 + 30 + 10 = 100**

---

## V-05 — Full integration + 19-criterion self-check

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Same as V-04 + self-check C-01 |
| C-02 | PASS | Same as V-04 + self-check C-02 |
| C-03 | PASS | Same as V-04 + self-check C-03 |
| C-04 | PASS | Same as V-04 + self-check C-04 |
| C-05 | PASS | Same as V-04 + self-check C-05 |
| C-06 | PASS | Same as V-04 + self-check C-06 |
| C-07 | PASS | Same as V-04 + self-check C-07 |
| C-08 | PASS | No AMEND — default pass |
| C-09 | PASS | PRE-FLIGHT GATE + self-check C-09: "must appear in PRE-FLIGHT GATE (canonical location); also acceptable anywhere else in the output" |
| C-10 | PASS | PRE-FLIGHT GATE + self-check C-10 |
| C-11 | PASS | Ownership per role + self-check C-11 |
| C-12 | PASS | Named unknowns + self-check C-12 |
| C-13 | PASS | Cross-signal synthesis + failure mode blockquote + self-check C-13 |
| C-14 | PASS | STEP 6 dedicated section + STEP 5 closed + self-check C-14 |
| C-15 | PASS | MANDATORY OPENING: PRELIMINARY HYPOTHESIS + STEP 7 revision template + self-check C-15 |
| C-16 | PASS | AMEND INSTRUCTION in STEP 7 + self-check C-16 |
| C-17 | PASS | Failure mode blockquotes in STEP 6 + STEP 7; STEP 6: "fails exactly as silently as an absent section" + self-check C-17 |
| C-18 | PASS | PRE-FLIGHT GATE before MANDATORY OPENING + STOP instruction. Self-check C-18 defines exact pass: "PRE-FLIGHT GATE appears before MANDATORY OPENING and before all STEPs; contains both scope boundary and break-even fields with specific responses; includes a stop instruction; **inline reminders inside sections do not count**." Dual enforcement: structural + checklist-defined. |
| C-19 | PASS | STEP 2 + STEP 3 closed against scope exclusions; STEP 5 closed against unknowns; STEP 6 closed against scope exclusions + break-even. Self-check C-19 defines exact pass: "at least one section adjacent to OPEN UNKNOWNS (specifically STEP 5 CONFIDENCE) and at least one section adjacent to the scope exclusion canonical location (STEP 2 SURFACE AREA or STEP 3 COMPLEXITY) carry an explicit prohibition rule." Names which adjacent sections are required by name — not just that a canonical section exists. |

**Aspirational pass: 11/11**

**Composite: 60 + 30 + 10 = 100**

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|-------------|-----------|------|
| V-01 | 5/5 | 3/3 | 9/11 | 98.2 | Gold |
| V-02 | 5/5 | 3/3 | 8/11 | 97.3 | Gold |
| V-03 | 5/5 | 3/3 | 10/11 | 99.1 | Gold |
| V-04 | 5/5 | 3/3 | 11/11 | **100** | Gold |
| V-05 | 5/5 | 3/3 | 11/11 | **100** | Gold |

**Ranking**: V-04 = V-05 > V-03 > V-01 > V-02

---

## Excellence Signals

**From V-04 and V-05 (the only variations to reach 100/100):**

**1. The pre-analysis gate fires before the hypothesis commitment, not merely before analysis sections.**
All R4 gate-bearing variations (V-01, V-03, V-04, V-05) place the PRE-FLIGHT GATE before INERTIA CHECK. But V-04 and V-05 place it before MANDATORY OPENING: PRELIMINARY HYPOTHESIS. This is a qualitatively different ordering: the scope boundary and break-even are resolved before any estimate is committed — not just before analysis is populated. The hypothesis becomes a function of already-resolved scope, not a commitment made before exclusions are known. This is how C-18 enables the hypothesis-revision lifecycle (C-15): the hypothesis cannot contradict the gate because the gate precedes it.

**2. The 19-criterion self-check (V-05) converts structural pass conditions from rubric language into self-auditable definitions.**
V-04's 17-criterion self-check verifies C-01–C-17. V-05 adds C-18 and C-19 with exact structural definitions: C-18 specifies "inline reminders inside sections do not count"; C-19 names which specific adjacent sections must be closed ("specifically STEP 5 CONFIDENCE" and "STEP 2 SURFACE AREA or STEP 3 COMPLEXITY"). The model can now verify its own structural compliance against named location requirements rather than a general principle. This closes the dual-enforcement loop that R3 V-05 achieved for C-09 and C-10 — structural mechanism prevents violations during generation, checklist with explicit structural definitions catches residuals before writing.

**Differentiating V-05 from V-04 (same rubric score, higher execution reliability):**
V-05 provides insurance against a model that satisfies the structural mechanisms but fails to execute them correctly. By naming the exact sections and exact conditions in the checklist, V-05 makes C-18 and C-19 self-correcting: even if the gate is placed incorrectly or a prohibition guard is omitted, the checklist will surface the specific location of the failure before the artifact is written.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Pre-analysis gate placed before hypothesis commitment — resolving scope boundary and break-even before any estimate is committed makes them foundational inputs that anchor analysis, not confirmatory additions verified afterward", "Self-check items that define structural pass conditions by location and exception — C-18 and C-19 checklist entries name exactly which sections must carry which mechanism and what does not qualify (e.g., inline reminders do not count for C-18), converting structural criteria into self-auditable items before writing"]}
```
