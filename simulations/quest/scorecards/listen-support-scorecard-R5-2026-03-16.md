## listen-support Quest Scorecard — Round 5

**Rubric:** v5 (C-01–C-20, max 150 pts) | **Date:** 2026-03-16

---

### Round Summary

| Variation | Composite | all_essential_pass | Golden |
|-----------|-----------|-------------------|--------|
| V-01 (Lifecycle Emphasis) | 83/150 | FALSE | BLOCKED |
| V-02 (Phrasing Register) | 69/150 | FALSE | BLOCKED |
| V-03 (Role Sequence) | 69/150 | FALSE | BLOCKED |
| **V-04** (Lifecycle + Role Sequence) | **90/150** | FALSE | BLOCKED |
| **V-05** (Full Synthesis) | **90/150** | FALSE | BLOCKED |

**All five variations fail C-05.** The R5 design deliberately abandons the planning-table + TABLE CHECK paradigm (R3/R4) in favor of STATUS QUO + COVERAGE TRACE + phase-role sequencing. C-05 was the last unfixed Essential from R4; R5 traded it for new structural mechanisms that aren't yet in the rubric.

---

### Key criterion outcomes

- **C-05 (structural gate):** FAIL across all — phase/layer minimums are declarative soft constraints, no TABLE CHECK or halt instruction
- **C-06 (phase target):** PASS for V-01/V-04/V-05 (PHASE-ROLE MAP or phase map), FAIL for V-02/V-03 (no phase concept)
- **C-07 (role-phase matrix):** PARTIAL for V-04/V-05 (phase-row map with role priority, not ≥4 role rows), FAIL for V-01 (phase map has no role dimension), FAIL for V-02/V-03
- **C-17/C-18/C-19/C-20:** FAIL across all — "calibrate against phase character" is advisory, not a lookup key declaration; no TABLE CHECK; no gap coverage verification block

---

### Excellence Signals (candidate criteria for v6)

**C-21 — Evidence-to-gap traceability with orphan-gap check:** A 3-column COVERAGE TRACE TABLE (Ticket ID / STATUS QUO element traced / Gap traced to) links every ticket to a named prior-tool element and a specific Gap ID. Explicit orphan-gap check requires naming any gap item with no supporting ticket. Distinct from C-20 (checks gap section completeness) — this checks that each individual gap item has ticket evidence.

**C-22 — Prohibited sentinel language on consequence fields:** CROSS-TICKET PATTERN consequence fields carry `Prohibited:` lists banning disallowed value patterns ("users", "this will cause confusion", "this will slow adoption"). Forces named stock roles, specific events with ticket references, and quantified friction. Structural anti-vagueness constraint complementary to C-02 (controlled vocabulary) but applied to free-text fields rather than fixed-vocabulary fields.

---

```json
{"top_score": 90, "all_essential_pass": false, "new_patterns": ["Evidence-to-gap traceability with orphan-gap check -- a 3-column COVERAGE TRACE TABLE links each ticket to a named STATUS QUO element and a specific Gap ID; an explicit no-orphan-gap check requires naming any gap item with no supporting ticket evidence; distinct from C-20 (gap section completeness) and C-16 (prior-tool tracing); closes the ticket-evidence-to-gap-claim loop that neither C-04 nor C-20 addresses", "Prohibited sentinel language on consequence fields -- CROSS-TICKET PATTERN consequence fields carry Prohibited: lists naming disallowed value patterns (e.g., Prohibited: 'this will cause confusion', 'users', 'this will slow adoption'); forces named stock roles, specific events with ticket references, and quantified friction statements; structural anti-vagueness constraint complementary to controlled vocabulary (C-02) but applied to free-text consequence fields rather than fixed-vocabulary fields"]}
```
on resolution path table. |
| C-11 Phase as card field | PARTIAL (2) | Card template has `**Phase**: [P1 / P2 / P3]` as a named field. Phase label present; day range absent. C-11 requires "Phase N (day X-Y)" with day range on the field. |
| C-12 Fallback-grounded severity | PARTIAL (2) | Severity calibration present: "P0/P1: feature broken or inaccessible; no viable workaround exists / P2/P3: workaround available; cosmetic or enhancement." Norm-based, not a fallback rule for ambiguous-phase cases. No "if phase unclear, assign PX" clause. |
| C-13 Mid-output verification block | FAIL (0) | No verification block after ticket generation. No named post-generation step checking phase distribution, severity compliance, or role diversity with PASS/FAIL gates. |
| C-14 Phase+Title coexistence | PARTIAL (2) | Both Phase and Title present as discrete named fields in the card template. No verification check confirming coexistence -- C-13 absent means no coexistence gate. |
| C-15 Temporal adoption window severity model | FAIL (0) | STEP 2 phase map has day windows and character descriptions but NO severity ranges per window. Severity in STEP 3 is assigned by workaround availability (P0/P1 = no workaround, P2/P3 = workaround), independent of phase. No day-window severity lookup table, no override prohibition. |
| C-16 Prior-tool coverage as 4th verification check | PARTIAL (2) | STATUS QUO section names prior tool. STEP 7 COVERAGE TRACE TABLE has "STATUS QUO element traced" column linking each ticket to a named prior-tool element. No vocabulary column with Prior-tool ref? marker. No verification block, so no 4th gate on citation count. |
| **C-17 Phase-as-severity-key declaration** | FAIL (0) | No statement "Phase is the lookup key for severity assignment." Severity assignment is workaround-based, not phase-derived. No "No override path exists" constraint anywhere. |
| **C-18 Gate minimum correct at >=7** | FAIL (0) | No structural gate. Phase minimums sum to >=4, not >=7. |
| **C-19 TABLE CHECK halt instruction** | FAIL (0) | No TABLE CHECK block. No halt instruction. |
| **C-20 Gap analysis coverage verification block** | FAIL (0) | STEP 7 Coverage trace table checks ticket-to-gap evidence traceability (orphan-gap check) but does NOT verify that each gap section (Doc/Design/Operational) contains >=1 named artifact with PASS/FAIL per type. Different mechanism from C-20. |

**V-01 Composite:** 12+12+12+12+0 + 10+0+10 + 5+2+2+2+0+2+0+2+0+0+0+0 = **83/150**
**all_essential_pass:** FALSE (C-05 FAIL)
**Golden:** BLOCKED

---

### V-02: Phrasing Register -- Conversational Imperative

**Axis:** Direct imperative phrasing throughout; STATUS QUO section; no phase concept --
role vocabulary and consequence prohibition via imperative instructions.

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-01 Title field on card** | PASS (12) | Card format has `Title: [specific title -- not a category label]` as a discrete named field |
| **C-02 Controlled vocabulary declared and enforced** | PASS (12) | "Step 2 -- Fix your vocabulary. Use only these values. No variants, no capitalisation changes." Explicit prohibition on synonyms. |
| **C-03 First-person voice throughout** | PASS (12) | "You ARE [persona name]. Do not write 'the user', 'they', or any third-person word that refers to yourself." Constraint stated. |
| **C-04 Gap analysis with three named sections** | PASS (12) | Step 6 has Doc gaps (D-01...), Design gaps (Ds-01...), Operational gaps (O-01...) with IDs and Priority Close Order |
| **C-05 Minimum ticket count enforced** | **FAIL (0)** | "Step 3 -- Know your minimum: Generate at least 5 tickets." Soft instruction, no TABLE CHECK block, no structural gate. Threshold is 5 (below 7) and enforcement is advisory. |
| C-06 Phase target declared before ticket generation | **FAIL (0)** | No phase concept. V-02 uses no phase labeling; tickets have no phase dimension. No phase targets declared. |
| C-07 Role-phase matrix | **FAIL (0)** | No phase concept, no role-phase matrix of any kind. |
| C-08 Migration framing present | PASS (10) | Step 1 STATUS QUO names specific tool, friction point, and first new-feature action. STATUS QUO connection field on each card. |
| C-09 Cross-ticket pattern table | PASS (5) | Step 5 CROSS-TICKET PATTERN with named structured fields and three Consequence fields with Prohibited lists |
| C-10 Resolution paths for high-severity tickets | PARTIAL (2) | Priority Close Order ranks top 3 gaps with ticket IDs. Gap-level, not per-ticket resolution paths. |
| C-11 Phase as card field | **FAIL (0)** | No Phase field on cards. V-02 has no phase concept. |
| C-12 Fallback-grounded severity | PARTIAL (2) | "Severity rule: P0 or P1 means the feature is broken or inaccessible with no viable workaround. P2 or P3 means a workaround exists." Norm-based; no fallback for ambiguous cases. |
| C-13 Mid-output verification block | FAIL (0) | No verification block after ticket generation. |
| C-14 Phase+Title coexistence | **FAIL (0)** | Phase absent from cards; coexistence impossible. |
| C-15 Temporal adoption window severity model | **FAIL (0)** | No phase or day-window concept. |
| C-16 Prior-tool coverage as 4th verification check | PARTIAL (2) | STATUS QUO names prior tool. Step 7 coverage trace table has STATUS QUO element column. No vocabulary column or 4th verification gate. |
| **C-17 Phase-as-severity-key declaration** | FAIL (0) | No phase concept; no lookup key declaration. |
| **C-18 Gate minimum correct at >=7** | FAIL (0) | Minimum is 5, no gate. |
| **C-19 TABLE CHECK halt instruction** | FAIL (0) | No TABLE CHECK block. |
| **C-20 Gap analysis coverage verification block** | FAIL (0) | Coverage trace table checks ticket-to-gap evidence; does not verify gap section completeness with PASS/FAIL per type. |

**V-02 Composite:** 12+12+12+12+0 + 0+0+10 + 5+2+0+2+0+0+0+2+0+0+0+0 = **69/150**
**all_essential_pass:** FALSE (C-05 FAIL)
**Golden:** BLOCKED

---

### V-03: Role Sequence -- Operational-First

**Axis:** Layer 1 (SRE/Support) before Layer 2 (C-01 through C-12) before Layer 3 (PM/UX);
Layer field on cards replaces Phase; STATUS QUO + coverage trace.

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-01 Title field on card** | PASS (12) | Card template has `**Title**: [specific, action-oriented title]` as discrete named field |
| **C-02 Controlled vocabulary declared and enforced** | PASS (12) | CONTROLLED VOCABULARY block with "Apply exactly. No synonyms or variants." Category/Volume/Severity values declared. |
| **C-03 First-person voice throughout** | PASS (12) | "You ARE [persona name]. Do not write 'the user', 'they', or any third-person reference to yourself." |
| **C-04 Gap analysis with three named sections** | PASS (12) | GAP ANALYSIS has Doc gaps (D-01...), Design gaps (Ds-01...), Operational gaps (O-01...) with IDs and Priority Close Order tying gaps to layer data |
| **C-05 Minimum ticket count enforced** | **FAIL (0)** | "Minimum ticket count: 5 or more." Declarative in vocabulary block. Layer minimums (>=2 Layer 1, >=2 Layer 2, >=1 Layer 3) total >=5. No TABLE CHECK block, no structural gate. |
| C-06 Phase target declared before ticket generation | **FAIL (0)** | No phase concept. V-03 uses Layer 1/2/3 ordering, not phase buckets. No phase target declaration. |
| C-07 Role-phase matrix | **FAIL (0)** | ROLE SEQUENCE section defines three layers with role groupings and quantity minimums. No phase dimension; no cross-matrix format; no per-phase constraints. Layer ordering is a sequence rule, not a matrix. |
| C-08 Migration framing present | PASS (10) | STATUS QUO section names prior tool, friction point, and first new-feature action. STATUS QUO connection field on each card traces body to named element. |
| C-09 Cross-ticket pattern table | PASS (5) | CROSS-TICKET PATTERN section with Pattern name, Pattern tickets, Pattern root cause, and three Consequence fields (Prohibited labels on each) |
| C-10 Resolution paths for high-severity tickets | PARTIAL (2) | Priority Close Order in GAP ANALYSIS ranks top 3 gaps with ticket IDs, layer references, and volume/severity. Gap-level, not per-ticket. |
| C-11 Phase as card field | **FAIL (0)** | Card has `**Layer**: [1 -- Operational | 2 -- Customer | 3 -- Strategic]`, not a Phase field. Layer is an ordering dimension, not a temporal adoption window. |
| C-12 Fallback-grounded severity | PARTIAL (2) | Severity calibration: P0/P1 = no workaround, P2/P3 = workaround. Norm without explicit fallback rule for ambiguous cases. |
| C-13 Mid-output verification block | FAIL (0) | No verification block. |
| C-14 Phase+Title coexistence | **FAIL (0)** | Phase absent; Layer field is not Phase. Coexistence requirement unmet. |
| C-15 Temporal adoption window severity model | **FAIL (0)** | No phase or day-window concept. Layer ordering has no temporal character tied to severity ranges. |
| C-16 Prior-tool coverage as 4th verification check | PARTIAL (2) | STATUS QUO names prior tool. COVERAGE TRACE TABLE has STATUS QUO element column per ticket. No vocabulary column or 4th gate. |
| **C-17 Phase-as-severity-key declaration** | FAIL (0) | No phase concept; no lookup key declaration. |
| **C-18 Gate minimum correct at >=7** | FAIL (0) | Minimum >=5, no structural gate. |
| **C-19 TABLE CHECK halt instruction** | FAIL (0) | No TABLE CHECK block. |
| **C-20 Gap analysis coverage verification block** | FAIL (0) | Coverage trace orphan-gap check verifies ticket-to-gap evidence, not gap section completeness with PASS/FAIL per type. |

**V-03 Composite:** 12+12+12+12+0 + 0+0+10 + 5+2+0+2+0+0+0+2+0+0+0+0 = **69/150**
**all_essential_pass:** FALSE (C-05 FAIL)
**Golden:** BLOCKED

---

### V-04: Combined -- Lifecycle Emphasis + Role Sequence

**Axes:** PHASE-ROLE MAP (phase rows with role priority per phase) + STATUS QUO +
coverage trace table.

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-01 Title field on card** | PASS (12) | Card template has `**Title**: [specific, action-oriented title]` as discrete named field |
| **C-02 Controlled vocabulary declared and enforced** | PASS (12) | CONTROLLED VOCABULARY block with Category/Volume/Severity values; "P0/P1: feature broken or inaccessible with no viable workaround / P2/P3: workaround available or issue is cosmetic" |
| **C-03 First-person voice throughout** | PASS (12) | "You ARE [persona name]. Do not write 'the user', 'they', or any third-person reference to yourself." |
| **C-04 Gap analysis with three named sections** | PASS (12) | GAP ANALYSIS has Doc gaps (D-01...), Design gaps (Ds-01...), Operational gaps (O-01...) with IDs; Priority Close Order ties each gap to ticket IDs and phases |
| **C-05 Minimum ticket count enforced** | **FAIL (0)** | "Minimums: at least 2 P1 tickets, at least 2 P2 tickets, at least 1 P3 ticket." = >=5 total. Declarative constraints in PHASE-ROLE MAP. No TABLE CHECK block, no halt instruction, no structural gate. |
| C-06 Phase target declared before ticket generation | PASS (10) | PHASE-ROLE MAP (Phase / Window / Role priority / Character) declared as a named planning artifact before ticket generation. Per-phase role priority establishes distribution target. |
| C-07 Role-phase matrix | PARTIAL (5) | PHASE-ROLE MAP table has 3 phase rows with Role priority column (SRE+Support for P1, C-01 through C-12 for P2, PM+UX for P3) and Character column with expected volume/severity ranges. Per-phase constraints present. Does not have >=4 named role rows (rows are phase-keyed, not role-keyed). |
| C-08 Migration framing present | PASS (10) | STATUS QUO section names prior tool, friction point, and first new-feature action. STATUS QUO connection field on every card traces body to named element. |
| C-09 Cross-ticket pattern table | PASS (5) | CROSS-TICKET PATTERN with Pattern name, Pattern tickets (with phase labels), Pattern root cause, and three Consequence fields with Prohibited lists |
| C-10 Resolution paths for high-severity tickets | PARTIAL (2) | Priority Close Order: "Rank the top 3 gaps to close before launch. Tie each gap to specific ticket IDs, their phases, and their volume/severity." Gap-level resolution, not per-ticket owner/action table. |
| C-11 Phase as card field | PARTIAL (2) | Card has `**Phase**: [P1 / P2 / P3]` as a named field. Phase label present; day range absent. C-11 requires "Phase N (day X-Y)" with day range. |
| C-12 Fallback-grounded severity | PARTIAL (2) | Severity calibration: P0/P1 = no workaround, P2/P3 = workaround. No explicit fallback for ambiguous-phase cases. Card says "calibrate against phase character" which introduces judgment. |
| C-13 Mid-output verification block | FAIL (0) | No verification block after ticket generation. |
| C-14 Phase+Title coexistence | PARTIAL (2) | Both Phase and Title present as discrete named fields on every card. No verification step confirming coexistence; C-13 absent. |
| C-15 Temporal adoption window severity model | PARTIAL (2) | PHASE-ROLE MAP Character column includes severity ranges per phase: "High volume. P0/P1 severity." (P1), "Medium volume. P1/P2." (P2), "Low volume. P2/P3." (P3). Ranges present but not a mechanical hard lookup table; no "No override path exists" constraint; card says "calibrate against phase character" (advisory, not locked). No verification check on mechanical compliance. |
| C-16 Prior-tool coverage as 4th verification check | PARTIAL (2) | STATUS QUO names prior tool. COVERAGE TRACE TABLE has "STATUS QUO element traced" column per ticket (with phase label). No vocabulary column with Prior-tool ref? marker. No 4th verification gate on citation count. |
| **C-17 Phase-as-severity-key declaration** | FAIL (0) | Card template: `**Severity**: [controlled vocabulary; calibrate against phase character]`. "Calibrate against phase character" is advisory guidance, not a lookup key declaration. No "Phase is the lookup key for severity assignment" or "No override path exists" statement anywhere. Phase-severity ranges in the PHASE-ROLE MAP are descriptive, not declared as a binding structural rule. |
| **C-18 Gate minimum correct at >=7** | FAIL (0) | No structural gate; no TABLE CHECK. Phase minimums total >=5. |
| **C-19 TABLE CHECK halt instruction** | FAIL (0) | No TABLE CHECK block. No halt instruction. |
| **C-20 Gap analysis coverage verification block** | FAIL (0) | COVERAGE TRACE TABLE no-orphan-gap check verifies ticket evidence per gap item. Does not append a coverage verification block to the gap analysis confirming >=1 named artifact per Doc/Design/Operational section with PASS/FAIL. |

**V-04 Composite:** 12+12+12+12+0 + 10+5+10 + 5+2+2+2+0+2+2+2+0+0+0+0 = **90/150**
**all_essential_pass:** FALSE (C-05 FAIL)
**Golden:** BLOCKED

---

### V-05: Full Synthesis -- All Three Axes + Summary Table Vocabulary Lock

**Axes:** Phase-role ordering (V-04) + summary table before card generation + STATUS QUO +
coverage trace with frontmatter verify.

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-01 Title field on card** | PASS (12) | STEP 5 card template: `**Title**: [matches summary table]` as discrete named field. Summary table also carries Title as a column. |
| **C-02 Controlled vocabulary declared and enforced** | PASS (12) | STEP 3 CONTROLLED VOCABULARY: "Apply exactly. No synonyms, no variants, no capitalisation changes." STEP 4 summary table locks all controlled-vocabulary values before prose generation. STEP 8 frontmatter verify: "Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category, Persona, Volume, and Severity value in the full card bodies." Triple-layer enforcement. |
| **C-03 First-person voice throughout** | PASS (12) | "You ARE [persona name]. Do not write 'the user', 'they', 'the SRE', 'the PM', or any third-person reference to yourself." Extended prohibited-reference list. |
| **C-04 Gap analysis with three named sections** | PASS (12) | STEP 7 GAP ANALYSIS has Doc gaps (D-xx), Design gaps (Ds-xx), Operational gaps (O-xx) with IDs; Priority Close Order names ticket IDs, phases, and volume/severity per gap |
| **C-05 Minimum ticket count enforced** | **FAIL (0)** | STEP 2 minimums: "at least 2 P1 tickets, 2 P2 tickets, 1 P3 ticket" = >=5. STEP 4 SUMMARY TABLE is a vocabulary lock step, not a minimum count gate. No TABLE CHECK block, no halt instruction enforcing >=7. |
| C-06 Phase target declared before ticket generation | PASS (10) | STEP 2 PHASE-ROLE MAP (Phase / Window / Role priority / Expected character) declared before STEP 5 card generation |
| C-07 Role-phase matrix | PARTIAL (5) | PHASE-ROLE MAP: P1 (SRE then Support), P2 (C-01 through C-12), P3 (PM, UX, advanced C-xx). Per-phase role priority present; 3 phase rows with character and severity ranges. Does not have >=4 named role rows -- rows are phase-keyed. |
| C-08 Migration framing present | PASS (10) | STEP 1 STATUS QUO section names prior tool, friction point, first new action. STATUS QUO connection field per card. STEP 8 trace table verifies STATUS QUO tracing. |
| C-09 Cross-ticket pattern table | PASS (5) | STEP 6 CROSS-TICKET PATTERN with named structured fields and three Consequence fields with Prohibited lists including specific forbidden phrases |
| C-10 Resolution paths for high-severity tickets | PARTIAL (2) | STEP 7 Priority Close Order format: "1. [Gap ID]: prevents T-01 (P1, high/P1), T-03 (P1, high/P1). Closes before P2 adoption begins." Gap-level with ticket/phase evidence. Not a per-ticket owner/action table. |
| C-11 Phase as card field | PARTIAL (2) | STEP 5 card: `**Phase**: [P1 / P2 / P3] (must match summary table)`. Summary table also has Phase column. Phase label present; day range absent on both card and table. |
| C-12 Fallback-grounded severity | PARTIAL (2) | Severity calibration: P0/P1 = no workaround, P2/P3 = workaround. Card: `**Severity**: [controlled vocabulary; calibrate against phase character]`. No fallback rule for ambiguous-phase cases. |
| C-13 Mid-output verification block | FAIL (0) | STEP 8 "Frontmatter verify" is a single consistency check (summary table vs cards), not a verification block with >=3 named PASS/FAIL checks on phase distribution, severity compliance, and role diversity. |
| C-14 Phase+Title coexistence | PARTIAL (2) | Both Phase and Title present on every card and in the summary table. STEP 8 frontmatter verify checks that both fields match summary table values, providing indirect coexistence verification. Not a named coexistence check. |
| C-15 Temporal adoption window severity model | PARTIAL (2) | PHASE-ROLE MAP Character column includes severity ranges: "High volume. P0/P1 severity." (P1), "Medium volume." (P2), "Low volume." (P3). Phase-to-severity ranges present in named planning artifact. No "No override path exists" constraint; card uses "calibrate against phase character" (advisory). No mechanical compliance check. |
| C-16 Prior-tool coverage as 4th verification check | PARTIAL (2) | STATUS QUO names prior tool. STEP 8 COVERAGE TRACE TABLE has "STATUS QUO element traced" column requiring exact phrase or tool name from Step 1. Frontmatter verify cross-checks card vocabulary. No vocabulary column with Prior-tool ref? marker. No 4th gate on citation count. |
| **C-17 Phase-as-severity-key declaration** | FAIL (0) | Card: `**Severity**: [controlled vocabulary; calibrate against phase character]`. "Calibrate against phase character" is advisory, not a key declaration. PHASE-ROLE MAP has severity ranges but no explicit "Phase is the lookup key for severity assignment. No override path exists." Neither the planning table nor the card template declares Phase as the structural key for severity. |
| **C-18 Gate minimum correct at >=7** | FAIL (0) | No structural gate. Phase minimums = >=5. |
| **C-19 TABLE CHECK halt instruction** | FAIL (0) | STEP 4 SUMMARY TABLE generates vocabulary lock before cards but has no TABLE CHECK format, no halt instruction, no named target step to block on. |
| **C-20 Gap analysis coverage verification block** | FAIL (0) | STEP 8 no-orphan-gap check verifies ticket evidence per gap item; does not append a PASS/FAIL coverage block to the STEP 7 gap analysis confirming >=1 named artifact per Doc/Design/Operational section. |

**V-05 Composite:** 12+12+12+12+0 + 10+5+10 + 5+2+2+2+0+2+2+2+0+0+0+0 = **90/150**
**all_essential_pass:** FALSE (C-05 FAIL)
**Golden:** BLOCKED

---

### Round Summary

| Variation | Composite | all_essential_pass | Golden | C-05 | C-06 | C-07 | C-15 | C-17 | C-18 | C-19 | C-20 |
|-----------|-----------|-------------------|--------|------|------|------|------|------|------|------|------|
| V-01 | 83/150 | FALSE | BLOCKED | FAIL | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |
| V-02 | 69/150 | FALSE | BLOCKED | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |
| V-03 | 69/150 | FALSE | BLOCKED | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |
| **V-04** | **90/150** | FALSE | BLOCKED | FAIL | PASS | PARTIAL | PARTIAL | FAIL | FAIL | FAIL | FAIL |
| **V-05** | **90/150** | FALSE | BLOCKED | FAIL | PASS | PARTIAL | PARTIAL | FAIL | FAIL | FAIL | FAIL |

**Paradigm note:** All R5 variations abandon the planning-table + TABLE CHECK paradigm used in R3/R4.
C-05 (structural gate) is the Essential blocker for every variation -- all FAIL because none implement
TABLE CHECK or an equivalent structural count gate. C-05 was the last unfixed Essential in R4;
R5 variations deliberately traded it for new structural mechanisms in the coverage trace + phase-role paradigm.

---

### Excellence Signals

V-04 and V-05 achieve the ceiling for this paradigm (90/150). Both fail the Essential gate (C-05)
and therefore cannot clear Golden, but they implement structural mechanisms not captured by any
current rubric criterion.

**Signal 1 -- Evidence-to-gap traceability with orphan-gap check (all variations, strongest in V-05)**

All five variations include a COVERAGE TRACE TABLE with three columns:
Ticket ID (with phase label in V-04/V-05) | STATUS QUO element traced (exact phrase or tool name)
| Gap traced to (Gap ID + short name).

After completing the table, each variation requires: "Every gap ID named in the Gap Analysis
appears in at least one row of the Gap traced to column. No orphan gaps." If any gap ID is absent,
the model must explicitly name it: "Orphan gap: [Gap ID] -- no ticket evidence generated for this gap."

This mechanism creates bidirectional evidence traceability: STATUS QUO -> tickets (via STATUS QUO
connection field) and tickets -> gaps (via Gap traced to column). The orphan-gap check is a structural
closure requirement that surfaces unsubstantiated gap claims.

Distinct from C-20 (gap analysis coverage verification block, which checks that each gap SECTION
has >=1 named artifact) and from C-16 (prior-tool coverage, which checks STATUS QUO -> ticket
tracing). The coverage trace checks that each individual GAP ITEM has at least one ticket providing
evidence for it. A gap section can have named artifacts (passing C-20) but those artifacts can be
unsubstantiated by any ticket (failing the orphan-gap check). No current criterion captures this.

**Signal 2 -- Prohibited sentinel language on consequence fields (all variations)**

The CROSS-TICKET PATTERN section carries explicit "Prohibited:" lists on three named fields:

- Consequence -- Affected segment: Prohibited: "users", "customers", "teams", "adopters", any
  unnamed group. Forces named stock role or customer cohort (C-01 through C-12).

- Consequence -- Day-90 scenario: Prohibited: "this will cause confusion", any outcome without
  a named event and a ticket reference. Forces a specific event with a ticket ID.

- Consequence -- Adoption cost: Prohibited: "this will slow adoption", any statement without a
  number or named cost mechanism. Forces a quantity (hours, percentage, churn risk, path length).

These are structural anti-vagueness constraints: the "Prohibited:" list is the complement of the
controlled vocabulary pattern (C-02). Where C-02 restricts to allowed values, prohibited sentinels
ban specific disallowed value patterns. The effect is strongest on free-text consequence fields where
vague platitudes ("this will cause confusion") are the modal failure mode. No current criterion
captures prohibited-sentinel enforcement on consequence fields.

---

```json
{"top_score": 90, "all_essential_pass": false, "new_patterns": ["Evidence-to-gap traceability with orphan-gap check -- a 3-column COVERAGE TRACE TABLE links each ticket to a named STATUS QUO element and a specific Gap ID; an explicit no-orphan-gap check requires naming any gap item with no supporting ticket evidence; distinct from C-20 (gap section completeness) and C-16 (prior-tool tracing); closes the ticket-evidence-to-gap-claim loop that neither C-04 nor C-20 addresses", "Prohibited sentinel language on consequence fields -- CROSS-TICKET PATTERN consequence fields carry Prohibited: lists naming disallowed value patterns (e.g., Prohibited: 'this will cause confusion', 'users', 'this will slow adoption'); forces named stock roles, specific events with ticket references, and quantified friction statements; structural anti-vagueness constraint complementary to controlled vocabulary (C-02) but applied to free-text consequence fields rather than fixed-vocabulary fields"]}
```
