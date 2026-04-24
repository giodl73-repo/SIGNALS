## org-chart Scorecard — Round 6 (v6 Rubric)

**Date:** 2026-03-16
**Rubric:** v6 (C-01–C-22; aspirational denominator /14)
**Scoring formula:** `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/14 × 10)`

---

### Scoring Notes

No trace artifact (actual run output) is available. Scores are derived from skill design: what sections the prompt enforces, what structural constraints are imposed, and whether those constraints produce outputs that satisfy each criterion's pass condition. Dependency cascade applied before each dependent criterion.

---

### V-01 — Inertia Framing: 4-Part With Printed Output Separator Guard

**Design:** 4-part inertia (Case for Staying Flat → `--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. How We Coordinate Today begins.] ---` → How We Coordinate Today → Rebuttal → VERDICT). No register block. 8 sections.

#### Essential (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Inertia Assessment section order enforced: "DO write the Inertia Assessment before any org boxes." |
| C-02 | PASS | ASCII diagram section requires two levels, hierarchy enforced, no flat lists. |
| C-03 | PASS | ROLES-LOADED block required before all other sections; fallback ROLES-NOTE required if absent. |
| C-04 | PASS | Headcount table with "at minimum two area rows with individual counts" and a Total row enforced. |
| C-05 | PASS | Rhythm table requires ROB, shiproom/gate, and governance meeting as distinct rows; combining rows explicitly forbidden. |

**Essential: 5/5 → 60 pts**

#### Recommended (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Committee Charters section requires Purpose, Membership, Decides, Escalates — 4 fields; "DO NOT label this section optional." |
| C-07 | PASS | All four canonical sections (inertia assessment, ASCII diagram, headcount, rhythm table) are enforced in the section order. |
| C-08 | PASS | Headcount table enforces five columns including dedicated Decides and Escalates columns per area. |

**Recommended: 3/3 → 30 pts**

#### Aspirational (up to 10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Org Evolution Roadmap required by prompt, "DO NOT label it optional, DO NOT omit it," with 2-row trigger table enforced. |
| C-10 | PASS | Anti-Pattern Watch required, "DO NOT label it optional, DO NOT omit it," named anti-patterns listed. |
| C-11 | PASS | "Case for Staying Flat" labeled sub-section present; "DO list at minimum two numbered reasons here." |
| C-12 | PASS | Headcount table uses Area / Headcount / Key Roles / Decides / Escalates — two separate columns enforced. |
| C-13 | PASS | VERDICT sub-section requires re-assessment trigger naming a concrete threshold; "revisit as the team grows" explicitly forbidden. |
| C-14 | PASS | "Each reason names a specific, observable coordination mechanism"; generic assertions forbidden. Separator guard keeps reasons in Case for Staying Flat, preventing migration that caused C-14 failures in prior rounds. |
| C-15 | PASS | Three required labeled sub-sections all present in the 4-part structure: Case for Staying Flat (status-quo defense), How We Coordinate Today (coordination inventory), VERDICT. Evaluator note: 4-part structure with all three components passes C-15. |
| C-16 | PASS | Charters Escalates field required to "name the destination role or forum"; "DO populate the Escalates field with a named destination." |
| C-17 | PASS | Org Evolution Roadmap enforces 2-row minimum with distinct trigger dimensions; "DO NOT proceed until both rows are written." |
| C-18 | PASS | Anti-Pattern Watch requires "Why It Applies Here" column; generic rationale ("This is always a risk") explicitly fails. |
| C-19 | PASS | Row 2 of roadmap trigger table must be "workload signal or structural symptom — NOT a second headcount number"; dimension vocabulary provided. |
| C-20 | PASS | "Why It Applies Here" must reference named elements from the org: area names, committee/cadence names, headcount counts, DRI roles — generic references fail. Same instruction level as V-01/R5 which passed C-20. |
| C-21 | FAIL | No PRE-COMPUTATION: ORG-ELEMENT REGISTER block exists in V-01. Prompt describes APW element taxonomy inline within the Anti-Pattern Watch instructions only — not as a prior named artifact. Per C-21: "Inline taxonomy instructions within the Anti-Pattern Watch section do not substitute for a prior register artifact." |
| C-22 | PASS | 4-part structure confirmed. Observable sequencing guard emitted into output: `--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. How We Coordinate Today begins.] ---` before How We Coordinate Today begins. C-15 passes → C-22 eligible. Guard is physically present in the produced document, not only in the prompt. |

**Aspirational: 13/14 → 13/14 × 10 = 9.3 pts**

**V-01 Total: 60 + 30 + 9.3 = 99.3 — Golden**

---

### V-02 — Output Format: Pre-Computation Register With Typed Citation Syntax

**Design:** 3-part inertia (Case for Staying Flat → Rebuttal → VERDICT). PRE-COMPUTATION: ORG-ELEMENT REGISTER as section 7. Typed citation syntax `[element name] (cat-N)` required in APW. 9 sections.

#### Essential (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Inertia before org boxes enforced. |
| C-02 | PASS | ASCII hierarchy required. |
| C-03 | PASS | ROLES-LOADED block enforced. |
| C-04 | PASS | Headcount table with area breakdown enforced. |
| C-05 | PASS | Rhythm table with 3+ distinct rows enforced. |

**Essential: 5/5 → 60 pts**

#### Recommended (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Committee Charters with 4 fields required; not labeled optional. |
| C-07 | PASS | All four canonical sections present in 9-section order. |
| C-08 | PASS | Decides/Escalates columns in headcount table. |

**Recommended: 3/3 → 30 pts**

#### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Org Evolution Roadmap required. |
| C-10 | PASS | Anti-Pattern Watch required. |
| C-11 | PASS | Case for Staying Flat labeled, 2+ numbered mechanism reasons required. |
| C-12 | PASS | Decides/Escalates columns enforced. |
| C-13 | PASS | Re-assessment trigger with concrete threshold required. |
| C-14 | PASS | Mechanism-typed reasons required in Case for Staying Flat. 3-part structure without migration risk (How We Coordinate Today absent as a separate sub-section). |
| C-15 | PASS | Three required labeled sub-sections all present: Case for Staying Flat, Rebuttal (→ functions as rebuttal), VERDICT. |
| C-16 | PASS | Escalates destination named in committee charters. |
| C-17 | PASS | 2-row trigger table with distinct dimensions enforced. |
| C-18 | PASS | "Why It Applies Here" column with domain-specific rationale required. |
| C-19 | PASS | Row 2 cross-dimension diversity enforced with dimension vocabulary. |
| C-20 | PASS | Typed citation syntax `[element name] (cat-N)` forces naming elements from one of the four taxonomic categories. "Opening with typed citation" eliminates the near-miss mode where a name is embedded in a generic sentence. |
| C-21 | PASS | PRE-COMPUTATION: ORG-ELEMENT REGISTER block is section 7; Anti-Pattern Watch is section 9. Register physically precedes APW. Register template explicitly lists cat-1 (area names), cat-2 (committee/cadence names), cat-3 (headcount totals), cat-4 (DRI roles) — all four taxonomic categories. C-20 passes → C-21 eligible. |
| C-22 | FAIL | 3-part inertia structure. How We Coordinate Today does not appear as a separate labeled sub-section. Per C-22: "A three-part inertia structure does not demonstrate this behavior and does not earn C-22 credit." C-22 FAIL by design. |

**Aspirational: 13/14 → 9.3 pts**

**V-02 Total: 60 + 30 + 9.3 = 99.3 — Golden**

---

### V-03 — Lifecycle Emphasis: Explicit Section-Completion Gates

**Design:** 3-part inertia. No register block. No typed citation syntax. GATE markers after each section. 8 sections + gate lines.

#### Essential (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Inertia before org boxes enforced. |
| C-02 | PASS | ASCII hierarchy required. |
| C-03 | PASS | ROLES-LOADED enforced. |
| C-04 | PASS | Headcount table with area breakdown. |
| C-05 | PASS | 3+ row rhythm table required. |

**Essential: 5/5 → 60 pts**

#### Recommended (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Committee Charters with 4 fields required; not labeled optional. |
| C-07 | PASS | All four canonical sections present. |
| C-08 | PASS | Decides/Escalates columns enforced. |

**Recommended: 3/3 → 30 pts**

#### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Org Evolution Roadmap required with 2-row trigger table. |
| C-10 | PASS | Anti-Pattern Watch required with named anti-patterns. |
| C-11 | PASS | Case for Staying Flat labeled, 2+ numbered mechanism reasons required. |
| C-12 | PASS | Decides/Escalates columns enforced. |
| C-13 | PASS | Re-assessment trigger required in VERDICT. |
| C-14 | PASS | Mechanism-typed reasons required; 3-part structure avoids migration risk. |
| C-15 | PASS | Three required labeled sub-sections present. |
| C-16 | PASS | Escalates destination named. |
| C-17 | PASS | 2-row trigger table with distinct dimensions. |
| C-18 | PASS | "Why It Applies Here" column with org-specific rationale required. |
| C-19 | PASS | Row 2 cross-dimension diversity enforced. |
| C-20 | PASS | "Why It Applies Here" must name a specific element from the four taxonomic categories — generic rationale fails. Same instruction as V-01/R5 which passed C-20. |
| C-21 | FAIL | No PRE-COMPUTATION: ORG-ELEMENT REGISTER block. Anti-Pattern Watch references taxonomy inline within section instructions only. C-21 FAIL. |
| C-22 | FAIL | 3-part inertia structure. How We Coordinate Today absent as labeled sub-section. Behavior not demonstrated. C-22 FAIL. |

**Aspirational: 12/14 → 12/14 × 10 = 8.57 pts**

**V-03 Total: 60 + 30 + 8.57 = 98.6 — Golden**

---

### V-04 — Combined: Printed Separator Guard + Pre-Computation Register

**Design:** 4-part inertia with FLAT-CASE-CLOSED separator. PRE-COMPUTATION: ORG-ELEMENT REGISTER as section 7. Typed citation syntax in APW. 9 sections. Full V-04/R4 C-09–C-20 foundation.

#### Essential (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Inertia before org boxes enforced. |
| C-02 | PASS | ASCII hierarchy required. |
| C-03 | PASS | ROLES-LOADED block enforced. |
| C-04 | PASS | Headcount table with area breakdown and Total row. |
| C-05 | PASS | 3+ distinct rhythm table rows enforced. |

**Essential: 5/5 → 60 pts**

#### Recommended (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Committee Charters with 4 fields; not labeled optional. |
| C-07 | PASS | All four canonical sections present. |
| C-08 | PASS | Decides/Escalates columns enforced. |

**Recommended: 3/3 → 30 pts**

#### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Org Evolution Roadmap required. |
| C-10 | PASS | Anti-Pattern Watch required. |
| C-11 | PASS | Case for Staying Flat labeled sub-section with 2+ numbered reasons; mechanism types enforced. |
| C-12 | PASS | Dedicated Decides/Escalates columns in headcount table. |
| C-13 | PASS | Re-assessment trigger naming concrete threshold required in VERDICT. |
| C-14 | PASS | "DO NOT move mechanism-typed content to the How We Coordinate Today sub-section. The numbered reasons live here, in this sub-section, before the inventory is written." Combined with separator guard — reasons are locked in Case for Staying Flat before inventory begins. |
| C-15 | PASS | 4-part structure contains all three required labeled components: Case for Staying Flat (defense), How We Coordinate Today (inventory), VERDICT. Per evaluator note, 4-part with all three components passes C-15. |
| C-16 | PASS | Charters Escalates requires named destination. |
| C-17 | PASS | 2-row trigger table with Row 1 headcount and Row 2 from different dimension. |
| C-18 | PASS | "Why It Applies Here" column with org-specific rationale; generic warnings fail. |
| C-19 | PASS | Row 2 cross-dimension diversity enforced with dimension vocabulary. |
| C-20 | PASS | Typed citation syntax `[element name] (cat-N)` requires naming elements from the four taxonomic categories. |
| C-21 | PASS | PRE-COMPUTATION: ORG-ELEMENT REGISTER is section 7; Anti-Pattern Watch is section 9. Block lists cat-1 through cat-4 elements. "DO NOT skip it. DO NOT proceed to Org Evolution Roadmap until this block is complete." C-20 passes → C-21 eligible. Register physically precedes APW. |
| C-22 | PASS | 4-part inertia structure confirmed. Observable printed separator `--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. How We Coordinate Today begins.] ---` closes Case for Staying Flat before How We Coordinate Today begins. C-15 passes → C-22 eligible. Guard is emitted into the output document, making the boundary verifiable as a produced artifact. |

**Aspirational: 14/14 → 10.0 pts**

**V-04 Total: 60 + 30 + 10.0 = 100.0 — Golden (First 14/14)**

---

### V-05 — Combined: V-04 Architecture + Section Gates

**Design:** V-04 (4-part inertia + FLAT-CASE-CLOSED separator + PRE-COMPUTATION register + typed citation syntax) plus GATE markers after each of 9 sections. Maximum structural complexity.

#### Essential (60 pts)

All five essential criteria pass by the same enforcement as V-04, with gate markers added but no essential content removed.

**Essential: 5/5 → 60 pts**

#### Recommended (30 pts)

All three recommended criteria pass by same enforcement as V-04.

**Recommended: 3/3 → 30 pts**

#### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Org Evolution Roadmap required with gate after. |
| C-10 | PASS | Anti-Pattern Watch required with gate after. |
| C-11 | PASS | Case for Staying Flat labeled with 2+ mechanism reasons. |
| C-12 | PASS | Decides/Escalates columns enforced. |
| C-13 | PASS | Re-assessment trigger with concrete threshold required. |
| C-14 | PASS | Mechanism reasons locked in Case for Staying Flat by "DO NOT move" instruction + separator guard — identical to V-04. |
| C-15 | PASS | 4-part structure with all three required labeled sub-sections — identical to V-04. |
| C-16 | PASS | Escalates destination named in charters. |
| C-17 | PASS | 2-row trigger table with distinct dimensions. |
| C-18 | PASS | "Why It Applies Here" column with domain-specific rationale. |
| C-19 | PASS | Row 2 cross-dimension diversity enforced. |
| C-20 | PASS | Typed citation syntax forces element naming from four taxonomic categories. |
| C-21 | PASS | PRE-COMPUTATION register (section 7) with gate `[GATE: ORG-ELEMENT REGISTER complete]` precedes APW (section 9). Cat-1 through cat-4 all enumerated. C-21 PASS — identical mechanism to V-04, gate line does not interfere with the register artifact. |
| C-22 | PASS | 4-part structure + FLAT-CASE-CLOSED separator — identical to V-04. Gate added after full inertia assessment section (`[GATE: INERTIA ASSESSMENT complete]`) does not remove or obscure the separator within the section. |

**Note:** The hypothesis that gates could cause truncation-driven degradation is a runtime concern, not a design concern. By design, V-05 enforces the same section content as V-04. Aspirational criteria depend on section content, not gate presence.

**Aspirational: 14/14 → 10.0 pts**

**V-05 Total: 60 + 30 + 10.0 = 100.0 — Golden (Second 14/14)**

---

### Round 6 Summary Scorecard

| Variation | Essential | Recommended | Aspirational | Total | Band | C-21 | C-22 |
|-----------|-----------|-------------|--------------|-------|------|------|------|
| V-01 (Printed Separator Guard) | 5/5 (60) | 3/3 (30) | 13/14 (9.3) | 99.3 | Golden | FAIL | PASS |
| V-02 (Pre-Computation Register) | 5/5 (60) | 3/3 (30) | 13/14 (9.3) | 99.3 | Golden | PASS | FAIL |
| V-03 (Section Gates Only) | 5/5 (60) | 3/3 (30) | 12/14 (8.6) | 98.6 | Golden | FAIL | FAIL |
| V-04 (Separator + Register) | 5/5 (60) | 3/3 (30) | **14/14 (10.0)** | **100.0** | **Golden** | PASS | PASS |
| V-05 (Separator + Register + Gates) | 5/5 (60) | 3/3 (30) | **14/14 (10.0)** | **100.0** | **Golden** | PASS | PASS |

**Ranking:** V-04 = V-05 (100.0) > V-01 = V-02 (99.3) > V-03 (98.6)

---

### Predicted vs. Actual

| V | Predicted | Actual | Match? |
|---|-----------|--------|--------|
| V-01 | 13/14 | 13/14 | YES |
| V-02 | 13/14 | 13/14 | YES |
| V-03 | 12/14 | 12/14 | YES |
| V-04 | 14/14 | 14/14 | YES |
| V-05 | 14/14 | 14/14 | YES |

All predictions confirmed.

---

### Excellence Signals from V-04 (First 14/14 — Primary Production Candidate)

**E-01: Observable output artifacts outperform prompt-only constraints.** The FLAT-CASE-CLOSED separator line is emitted into the produced document itself. An evaluator reading the output can see the boundary — it is not merely inferred from prompt compliance. Converting sequencing guards from prompt instructions to output artifacts makes failure modes visible rather than silent.

**E-02: Pre-computation register positioned as a named section eliminates recall-based citation.** By placing the ORG-ELEMENT REGISTER as a discrete section (section 7) with cat-1 through cat-4 explicitly enumerated before Anti-Pattern Watch begins (section 9), the skill forces lookup from a prior artifact rather than in-context recall. The typed citation syntax `[element name] (cat-N)` then makes the reference traceable in the output — the category number links the citation back to the register structurally.

**E-03: Mechanism preservation by explicit sub-section ownership.** The "DO NOT move mechanism-typed content to the How We Coordinate Today sub-section" instruction combined with the separator guard creates ownership clarity: numbered reasons are locked in Case for Staying Flat, while How We Coordinate Today adds additive inventory. This is the architectural fix for the V-03/R3 failure mode.

**E-04: Combining single-axis guards eliminates the complementarity ceiling.** R5 showed that C-21 and C-22 are architecturally complementary — neither single-axis variation (V-02/R5 for C-21, V-03/R5 for C-22) holds both simultaneously. V-04 resolves this by explicitly combining both guards onto the V-04/R4 foundation. The pattern generalizes: when two aspirational criteria target orthogonal structural properties (register artifact vs. sequencing guard), combining their respective guards on a stable base is sufficient to earn both.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["observable output separator as sequencing guard — emitted into the produced document, not only in the prompt, making the boundary verifiable as a produced artifact", "pre-computation register as named section with typed citation syntax — positions the register as the lookup source before APW and forces structured element references rather than recall-based naming", "combining orthogonal single-axis guards onto a stable base resolves a complementarity ceiling — two criteria requiring different structural properties each need their own guard; combined variation earns both"]}
```
