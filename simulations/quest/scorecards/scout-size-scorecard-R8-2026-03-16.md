# Quest Score — scout-size R8 (Rubric v8)

## Scoring Summary

All five variations meet the golden threshold. Analysis below.

---

## V-01 — Charter Completeness (Explicit Field Lists)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | PASS | Section 1.1 with WRONG/CORRECT examples; named points + count format required |
| C-02 | Complexity tier on-scale | PASS | "Assign exactly one: LOW / MEDIUM / HIGH / XL" with WRONG examples |
| C-03 | Inertia check present | PASS | Section 1.6 requires workaround + cost direction + reasoning; WRONG/CORRECT present |
| C-04 | Confidence level with basis | PASS | Section 1.5 requires level + "what IS established"; WRONG/CORRECT present |
| C-05 | Signal boundary respected | PASS | Explicit prohibition at top + signal boundary check at end |
| C-06 | Team-size names specialist types | PASS | Section 1.3 requires disciplines; WRONG "3 engineers" example |
| C-07 | Timeline as sprint range | PASS | "N–M sprints" format; WRONG calendar/point-estimate examples |
| C-08 | Primary complexity driver | PASS | Section 1.2 "one or two named factors — 'it's complex' is not a driver" |
| C-09 | Sensitivity up/down present | PASS | Sections 1.7 and 1.8 with tier-up and tier-down |
| C-10 | Confidence calibration | PASS | Section 1.9 |
| C-11 | Confidence gap named | PASS | Phase 2 section 2.1 with specific unknown + WRONG/CORRECT |
| C-12 | Sensitivity as single named conditions | PASS | "State ONE specific, named, falsifiable condition" |
| C-13 | Sensitivity names explicit tier destination | PASS | "Destination tier stated explicitly: Tier rises to [HIGH or XL]" |
| C-14 | Sensitivity conditions falsifiable | PASS | "Name what concrete investigation would settle this" with WRONG/CORRECT |
| C-15 | Basis and gap non-overlapping | PASS | Phase 2 charter violation test with WRONG/CORRECT inline |
| C-16 | Sensitivity destination differs from current | PASS | "Destination tier is different from your currently assigned tier" stated |
| C-17 | Inline failure examples for C-11/C-15/C-16 | **PARTIAL** | C-11 and C-15 have inline WRONG/CORRECT; C-16 failure mode (same-tier destination) has no dedicated WRONG example — unfalsifiable examples cover C-14 but not the vacuous-tier case |
| C-18 | Structural encoding for C-13 and C-16 | **PARTIAL** | Bracket notation in output line "Tier rises to [\_\_] if:" but not table column headers; prose-section encoding, not schema-level |
| C-19 | Inline failure examples precede output field | PASS | All WRONG/CORRECT blocks appear within each section before "Your output:" field |
| C-20 | Role-separated production for basis/gap | PASS | Phase 1 Sizing Analyst owns basis; Phase 2 Risk Assessor owns gap with explicit non-overlap charter |
| C-21 | Both WRONG and CORRECT instances | PASS | All inline examples provide both WRONG and CORRECT pairs |
| C-22 | Relational constraints co-encoded in dependent field | **PARTIAL** | Tier-destination constraint in section instruction prose (near field but not in column header label); gap non-overlap in Phase 2 prose, not in field definition |
| C-23 | Full field ownership in charters | PASS | Phase 1 charter lists all 10 fields by name; Phase 2 charter explicitly excludes all 10 Phase 1 fields by name |
| C-24 | Phase 2 names prohibited content categories | PASS | Four named categories: integration points, API contracts, complexity drivers, team/timeline signals |

**Essential**: 5/5 = 60 pts  
**Recommended**: 3/3 = 30 pts  
**Aspirational**: 13 PASS + 3 PARTIAL (C-17, C-18, C-22) = 14.5/16 = 9.1 pts  
**Composite: 99.1** | All essential pass: YES

---

## V-02 — Named Category Prohibition with Falsifiability Gate

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | PASS | [Phase 1 Field 1] with WRONG/CORRECT and count requirement |
| C-02 | Complexity tier on-scale | PASS | [Phase 1 Field 2] "Assign exactly one: LOW / MEDIUM / HIGH / XL" |
| C-03 | Inertia check present | PASS | [Phase 1 Field 7] with WRONG/CORRECT and cost direction |
| C-04 | Confidence level with basis | PASS | [Phase 1 Field 6] with WRONG/CORRECT; "The basis names what IS verified" |
| C-05 | Signal boundary respected | PASS | Top prohibition + signal boundary check at end |
| C-06 | Team-size names specialist types | PASS | [Phase 1 Field 4] with WRONG "2–3 engineers" example |
| C-07 | Timeline as sprint range | PASS | [Phase 1 Field 5] WRONG "6–8 weeks" and "4 sprints" examples |
| C-08 | Primary complexity driver | PASS | [Phase 1 Field 3] "Name the 1–2 factors most driving the tier" |
| C-09 | Sensitivity up/down present | PASS | [Phase 1 Field 8] and [Phase 1 Field 9] |
| C-10 | Confidence calibration | PASS | [Phase 1 Field 10] |
| C-11 | Confidence gap named | PASS | [Phase 2 Field 11] with format and WRONG/CORRECT |
| C-12 | Sensitivity as single named conditions | PASS | "One specific, named, falsifiable condition" in fields 8 and 9 |
| C-13 | Sensitivity names explicit tier destination | PASS | "[must resolve to a tier HIGHER than your assigned tier]" in field header |
| C-14 | Sensitivity conditions falsifiable | PASS | "Confirm by reviewing..." in WRONG/CORRECT examples |
| C-15 | Basis and gap non-overlapping | PASS | Falsifiability gate with WRONG/CORRECT; named category prohibition |
| C-16 | Sensitivity destination differs from current | PASS | "[must resolve to a tier HIGHER/LOWER than your assigned tier]" in field labels |
| C-17 | Inline failure examples for C-11/C-15/C-16 | **PARTIAL** | C-11 and C-15 fully covered; C-16 failure mode (same-tier destination) not shown as dedicated WRONG example in sensitivity fields |
| C-18 | Structural encoding for C-13 and C-16 | PASS | "[Phase 1 Field 8] Tier-Up Sensitivity [must resolve to a tier HIGHER than your assigned tier]" — constraint in field label |
| C-19 | Inline failure examples precede output field | PASS | All WRONG/CORRECT appear within [Phase N Field N] sections before the output marker |
| C-20 | Role-separated production for basis/gap | PASS | Phase 1 owns all fields except gap; Phase 2 owns gap only with named non-access rule |
| C-21 | Both WRONG and CORRECT instances | PASS | All WRONG/CORRECT pairs complete throughout |
| C-22 | Relational constraints co-encoded in dependent field | **PARTIAL** | Sensitivity destination co-encoded in field header labels (satisfies C-13/C-16); confidence gap non-overlap stated in Phase 2 prose rule but not embedded in gap field label in output compilation table |
| C-23 | Full field ownership in charters | **PARTIAL** | Phase 1 says "you own all sizing fields except the Confidence Gap" then enumerates 10 [Phase N Field N] entries; Phase 2 says "you own one field only: Confidence Gap. You do not produce any Phase 1 fields" — reference by category, not enumerated exclusion list |
| C-24 | Phase 2 names prohibited content categories | PASS | Four named categories + falsifiability gate ("could a reader derive this gap from Phase 1 by negation?") |

**Essential**: 5/5 = 60 pts  
**Recommended**: 3/3 = 30 pts  
**Aspirational**: 13 PASS + 3 PARTIAL (C-17, C-22, C-23) = 14.5/16 = 9.1 pts  
**Composite: 99.1** | All essential pass: YES

---

## V-03 — Role-Tagged Column Headers (C-23 via Structural Encoding)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | PASS | Surface Area table with "[name each individually — no general descriptions]" in column header; Total row required |
| C-02 | Complexity tier on-scale | PASS | Complexity table "[exactly one: LOW / MEDIUM / HIGH / XL — no other vocabulary]" |
| C-03 | Inertia check present | PASS | Confidence table row "Inertia Check [name the workaround — state: cheaper / comparable / more expensive]" |
| C-04 | Confidence level with basis | PASS | "Confidence Basis [what IS established — name the specific dimension]" in column header |
| C-05 | Signal boundary respected | PASS | Prohibition at top + signal boundary check after both tables |
| C-06 | Team-size names specialist types | PASS | Team-Size table "[name the role — not just 'engineer']" |
| C-07 | Timeline as sprint range | PASS | Timeline table "[N–M format — not a calendar date, not a single number]" |
| C-08 | Primary complexity driver | PASS | Complexity table "Primary Driver [1–2 named factors — 'it's complex' fails]" |
| C-09 | Sensitivity up/down present | PASS | Tier-Up and Tier-Down Sensitivity rows in Confidence table |
| C-10 | Confidence calibration | PASS | Confidence Calibration row |
| C-11 | Confidence gap named | PASS | Risk Assessor Table with WRONG/CORRECT; gap column defined with format |
| C-12 | Sensitivity as single named conditions | PASS | "single named falsifiable condition — name what action would confirm it" in column header |
| C-13 | Sensitivity names explicit tier destination | PASS | "[Tier rises to \_\_ — must be HIGHER than your assigned tier: fill with HIGH or XL]" in column header |
| C-14 | Sensitivity conditions falsifiable | PASS | "name what action would confirm it" in column header |
| C-15 | Basis and gap non-overlapping | PASS | Risk Assessor WRONG/CORRECT block before table cell; "same dimension with opposite polarity" named |
| C-16 | Sensitivity destination differs from current | PASS | "[must be HIGHER/LOWER than your assigned tier]" in column headers |
| C-17 | Inline failure examples for C-11/C-15/C-16 | **PARTIAL** | C-11 and C-15 have full WRONG/CORRECT; C-16 failure mode in sensitivity notes is WRONG-only ("Destination tier must differ... a tier that maps to itself is vacuous") — no C-16 WRONG example with both WRONG+CORRECT |
| C-18 | Structural encoding for C-13 and C-16 | PASS | Tier destination and relational constraints fully encoded in column headers |
| C-19 | Inline failure examples precede output field | **PARTIAL** | Risk Assessor WRONG/CORRECT precedes the gap cell (PASS); sensitivity notes appear after Confidence table cells — model fills sensitivity cells before encountering sensitivity WRONG examples (FAIL for sensitivity scope) |
| C-20 | Role-separated production for basis/gap | PASS | Two-table design; "Risk Assessor owns exactly one field: Confidence Gap" |
| C-21 | Both WRONG and CORRECT instances | **PARTIAL** | Risk Assessor WRONG/CORRECT block is complete; sensitivity notes in Sizing Analyst section are WRONG-only ("'Tier rises to HIGH if scope grows' fails..."; "'Tier drops to MEDIUM if the integration is simpler than expected' fails...") — no CORRECT counterpart in sensitivity notes |
| C-22 | Relational constraints co-encoded in dependent field | PASS | Sensitivity column headers encode destination constraints; Risk Assessor column header encodes all 4 prohibited categories at the gap cell definition point |
| C-23 | Full field ownership in charters | PASS | Every table and every column header carries "[Sizing Analyst]" or "[Risk Assessor]" role tag; "Risk Assessor owns exactly one field" stated explicitly |
| C-24 | Phase 2 names prohibited content categories | PASS | Gap column header names 4 prohibited categories inline at point of production |

**Essential**: 5/5 = 60 pts  
**Recommended**: 3/3 = 30 pts  
**Aspirational**: 13 PASS + 3 PARTIAL (C-17, C-19, C-21) = 14.5/16 = 9.1 pts  
**Composite: 99.1** | All essential pass: YES

---

## V-04 — Reversed Role Sequence + Complete Charter Enumeration

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | PASS | Phase 2 section 2.1 with WRONG/CORRECT; count is mandatory |
| C-02 | Complexity tier on-scale | PASS | Section 2.2 "Exactly one: LOW / MEDIUM / HIGH / XL" |
| C-03 | Inertia check present | PASS | Section 2.6 with WRONG/CORRECT and cost direction |
| C-04 | Confidence level with basis | PASS | Section 2.5 with WRONG/CORRECT; "name what IS established" |
| C-05 | Signal boundary respected | PASS | Top prohibition + signal boundary check |
| C-06 | Team-size names specialist types | PASS | Section 2.3 with WRONG "2–3 engineers" |
| C-07 | Timeline as sprint range | PASS | Section 2.4 "sprint range, not a calendar date, not a single number" |
| C-08 | Primary complexity driver | PASS | Section 2.2 "[1–2 named factors — not 'it's complex']" |
| C-09 | Sensitivity up/down present | PASS | Sections 2.7 and 2.8 |
| C-10 | Confidence calibration | PASS | Section 2.9 |
| C-11 | Confidence gap named | PASS | Phase 1 Risk Assessor with WRONG/CORRECT; specific unknown + sizing impact |
| C-12 | Sensitivity as single named conditions | PASS | "One named falsifiable condition" in 2.7 and 2.8 |
| C-13 | Sensitivity names explicit tier destination | PASS | Section headers "[destination must be HIGHER/LOWER than your assigned tier]" |
| C-14 | Sensitivity conditions falsifiable | PASS | WRONG/CORRECT examples show falsifiability requirement; "confirm by..." |
| C-15 | Basis and gap non-overlapping | PASS | Phase 2 non-access rule with reversed-scenario WRONG/CORRECT; "the basis colonizes the gap" failure named |
| C-16 | Sensitivity destination differs from current | PASS | Section headers "[destination must be HIGHER/LOWER than your assigned tier]" |
| C-17 | Inline failure examples for C-11/C-15/C-16 | **PARTIAL** | C-11 and C-15 fully covered with WRONG/CORRECT; sections 2.7 and 2.8 show C-14 failures (unfalsifiable conditions) but no dedicated C-16 failure example (same-tier destination) |
| C-18 | Structural encoding for C-13 and C-16 | **PARTIAL** | Section headings "### 2.7 Tier-Up Sensitivity [destination must be HIGHER than your assigned tier]" — constraint is in section heading (field label), not table column header; better than prose-only but not schema-level |
| C-19 | Inline failure examples precede output field | PASS | All WRONG/CORRECT appear within each section before "Your output" marker; Phase 1 gap examples precede "Your Confidence Gap:" |
| C-20 | Role-separated production for basis/gap | PASS | Reversed sequence: Phase 1 Risk Assessor produces gap; Phase 2 Sizing Analyst produces basis with non-access rule |
| C-21 | Both WRONG and CORRECT instances | PASS | All WRONG/CORRECT pairs are complete throughout |
| C-22 | Relational constraints co-encoded in dependent field | **PARTIAL** | Sensitivity destination co-encoded in section header labels; confidence gap non-overlap in Phase 2 prose (2.5 instruction), not embedded in the Phase 1 gap field definition |
| C-23 | Full field ownership in charters | PASS | Phase 1 charter: 1 owned + 10 explicitly excluded by name; Phase 2 charter: 10 owned by name + 1 excluded by name |
| C-24 | Phase 2 names prohibited content categories | PASS | Phase 2 non-access rule dynamically names the gap dimension Phase 1 identified as the prohibited category: "if Phase 1 identified X as the gap, your Confidence Basis must name a different dimension" |

**Essential**: 5/5 = 60 pts  
**Recommended**: 3/3 = 30 pts  
**Aspirational**: 13 PASS + 3 PARTIAL (C-17, C-18, C-22) = 14.5/16 = 9.1 pts  
**Composite: 99.1** | All essential pass: YES

---

## V-05 — Three-Phase + Inertia-First + Full Charter + Named Prohibition + Table Encoding

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | PASS | Surface Area Table "[name individually — no general descriptions]" with Total row required |
| C-02 | Complexity tier on-scale | PASS | Complexity Table "[exactly one: LOW / MEDIUM / HIGH / XL]" in column header |
| C-03 | Inertia check present | PASS | Phase 0 gate with WRONG/CORRECT; column header "[name the workaround AND state: cheaper / comparable / more expensive]" |
| C-04 | Confidence level with basis | PASS | "Confidence Basis [what IS established — name the specific dimension; do NOT address the gap dimension Phase 2 will identify]" |
| C-05 | Signal boundary respected | PASS | Prohibition at top + signal boundary check across all three phases |
| C-06 | Team-size names specialist types | PASS | Team-Size Table "[name the role]" |
| C-07 | Timeline as sprint range | PASS | Timeline Table "[N–M format — not calendar date, not single number]" |
| C-08 | Primary complexity driver | PASS | Complexity Table "[1–2 named factors — 'it's complex' fails]" |
| C-09 | Sensitivity up/down present | PASS | Tier-Up and Tier-Down rows in Confidence + Sensitivity Table |
| C-10 | Confidence calibration | PASS | Confidence Calibration row in Phase 1 table |
| C-11 | Confidence gap named | PASS | Phase 2 Risk Assessor table with WRONG/CORRECT; specific unknown + sizing impact format |
| C-12 | Sensitivity as single named conditions | PASS | "[single named falsifiable condition — name what action confirms it]" in column headers |
| C-13 | Sensitivity names explicit tier destination | PASS | "[Tier rises to \_\_ — must be HIGHER than assigned tier: HIGH or XL]" in column header |
| C-14 | Sensitivity conditions falsifiable | PASS | "[name what action confirms it]" in column header; CORRECT examples show investigation action |
| C-15 | Basis and gap non-overlapping | PASS | Phase 2 non-access rule + falsifiability gate + WRONG/CORRECT both present |
| C-16 | Sensitivity destination differs from current | PASS | "[must be HIGHER/LOWER than assigned tier]" in column headers |
| C-17 | Inline failure examples for C-11/C-15/C-16 | **PARTIAL** | C-11 and C-15 fully covered; C-16 acknowledged parenthetically in sensitivity WRONG example ("destination already assigned above if current = HIGH") but not as a standalone C-16 failure with a dedicated WRONG/CORRECT pair |
| C-18 | Structural encoding for C-13 and C-16 | PASS | Tier destination fully encoded in column headers with fill instructions "[HIGH or XL]" / "[LOW or MEDIUM]"; column headers are schema-level features |
| C-19 | Inline failure examples precede output field | **PARTIAL** | Phase 0 and Phase 2 WRONG/CORRECT precede their output cells (PASS); Phase 1 sensitivity WRONG/CORRECT are in post-table notes after the sensitivity cells — model fills cells before encountering notes (FAIL for sensitivity scope) |
| C-20 | Role-separated production for basis/gap | PASS | Three-phase design; Phase 0 owns inertia, Phase 1 owns 9 fields, Phase 2 owns gap — each with explicit charter |
| C-21 | Both WRONG and CORRECT instances | PASS | All examples have complete WRONG+CORRECT pairs: Phase 0 table, Phase 1 sensitivity notes (WRONG tier-up + CORRECT tier-up; WRONG tier-down + CORRECT tier-down), Phase 2 table |
| C-22 | Relational constraints co-encoded in dependent field | PASS | Sensitivity destination constraints in column headers; gap column header encodes all 4 prohibited categories + falsifiability gate; basis column header forward-references gap constraint ("do NOT address the gap dimension Phase 2 will identify") — bi-directional co-encoding |
| C-23 | Full field ownership in charters | PASS | Phase 0: 1 owned + 10 excluded by name. Phase 1: 9 owned by name + 2 excluded by name. Phase 2: 1 owned + 10 excluded by name (all three phases fully enumerated) |
| C-24 | Phase 2 names prohibited content categories | PASS | 4 named categories in Phase 2 prose non-access rule + same 4 categories in gap column header — two enforcement layers; falsifiability gate active at both points |

**Essential**: 5/5 = 60 pts  
**Recommended**: 3/3 = 30 pts  
**Aspirational**: 14 PASS + 2 PARTIAL (C-17, C-19) = 15/16 = 9.4 pts  
**Composite: 99.4** | All essential pass: YES

---

## Rankings

| Rank | Variation | Score | Delta from next | Discriminating criteria |
|------|-----------|-------|-----------------|------------------------|
| 1 | **V-05** | **99.4** | +0.3 | C-22 PASS (bi-directional co-encoding); C-21 PASS (complete sensitivity WRONG/CORRECT) |
| 2 | V-01 | 99.1 | — | C-19 PASS; C-21 PASS; but C-18 PARTIAL, C-22 PARTIAL |
| 2 | V-02 | 99.1 | — | C-18 PASS; C-19 PASS; but C-22 PARTIAL, C-23 PARTIAL |
| 2 | V-03 | 99.1 | — | C-18 PASS; C-22 PASS; but C-19 PARTIAL, C-21 PARTIAL |
| 2 | V-04 | 99.1 | — | C-19 PASS; C-21 PASS; but C-18 PARTIAL, C-22 PARTIAL |

---

## Excellence Signals from V-05

**1. Phase 0 as structural inertia gate**
Three-phase design elevates inertia check from a supplementary field to a gating prerequisite. The feature must be compared against its alternative before any sizing begins. This prevents the most common skip pattern (naming the workaround in passing without a cost direction) by making it Phase 0's entire charter.

**2. Bi-directional relational co-encoding (C-22 full pass)**
Both fields in the basis/gap pair are annotated with the relational constraint — the basis column header says "do NOT address the gap dimension Phase 2 will identify" (forward reference) and the gap column header lists all 4 prohibited categories (backward reference). This is the first variation to encode the constraint at both ends simultaneously, making the relational rule observable from either field without cross-referencing a rules section.

**3. Post-table sensitivity examples with both WRONG and CORRECT (C-21 full pass)**
V-03's post-table sensitivity notes were WRONG-only. V-05's post-table sensitivity notes supply complete WRONG+CORRECT pairs for both tier-up and tier-down, and the WRONG example for tier-up includes the C-16 parenthetical ("destination already assigned above if current = HIGH"). This makes the notes useful for self-correction even as post-fill gates.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["phase-0-inertia-gate: three-phase design elevates inertia check to a structural prerequisite before sizing begins, preventing skip by making it a role-owned gate phase rather than a section", "bi-directional-relational-co-encoding: embed the relational constraint in both fields of a constrained pair — forward reference in the basis field header (do not address gap dimension) and backward reference in the gap field header (prohibited categories) — so the rule is observable from either end without consulting a separate rules section"]}
```
