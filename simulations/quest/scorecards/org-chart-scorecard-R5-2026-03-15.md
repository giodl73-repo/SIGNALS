## org-chart — Round 5 Score Report

**Rubric:** v5 | **Variations:** V-01 through V-05 | **Baseline:** V-04/R4 = 100.0

---

### V-01 — Phrasing Register: Descriptive Throughout

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia precedes org diagram | PASS | Descriptive intro: "A skill that opens with an ASCII org box before answering the inertia question has missed the design principle." Structure enforced by ordering. |
| C-02 | Org hierarchy readable | PASS | "It shows at minimum two levels... A flat list of role names without hierarchy does not fulfill this section." |
| C-03 | Roles input honored | PASS | ROLES-LOADED / ROLES-NOTE blocks defined identically. |
| C-04 | Headcount by area | PASS | Five-column table with area rows; "A single undifferentiated total does not fulfill this section." |
| C-05 | Operating rhythm table | PASS | "At minimum three distinct rows: an ROB-equivalent, a shiproom or release gate, and a governance meeting." |
| C-06 | Committee charters complete | PASS | Four fields required; "charter section is not labeled optional." |
| C-07 | All four output sections present | PASS | Eight sections enumerated in section order. |
| C-08 | Decision rights indicated | PASS | Decides/Escalates columns in headcount table; single "Decision Scope" column explicitly excluded. |
| C-09 | Org evolution path | PASS | Evolution roadmap required; "A prose narrative about eventual evolution does not fulfill this section." |
| C-10 | Anti-patterns flagged | PASS | Anti-Pattern Watch required with named patterns and "Why It Applies Here" column. |
| C-11 | Inertia steelmans status quo | PASS | "At minimum two numbered reasons appear here." + "The numbered reasons remain in this sub-section. They are not moved to a later inventory." |
| C-12 | Decides/Escalates split | PASS | Five-column format; "The Decides and Escalates columns are distinct — a single 'Decision Scope' column does not satisfy the split." |
| C-13 | Verdict includes re-assessment trigger | PASS | Trigger required in VERDICT block; "Revisit as the team grows is not a trigger — the trigger names the observable." |
| C-14 | Steelman reasons mechanism-typed | PASS | "Each reason names something observable — a channel, an informal lead, a decision pattern, a recurring cadence. A reason asserting team cohesion or communication quality without naming a mechanism does not contribute to the count." Exclusion preserved in descriptive form. |
| C-15 | Three-part inertia labeled | PASS | Three labeled sub-sections present: Case for Staying Flat, Rebuttal, VERDICT. |
| C-16 | Escalates column names destination | PASS | "naming the destination role or forum that receives the escalation — a specific title or committee name, not 'everything else.'" |
| C-17 | Evolution trigger table has two distinct rows | PASS | Table format required; "Duplicate triggers at different wordings do not count." |
| C-18 | Anti-pattern table has domain-specific rationale column | PASS | Four-category taxonomy listed; "A 'Why It Applies Here' explanation that references team size, structural type, or generic org properties without naming a concrete element does not pass." |
| C-19 | Evolution trigger table uses cross-dimension diversity | PASS | Row 2 vocabulary (workload signal / structural symptom / milestone) provided. "A table containing two headcount thresholds — even at different numbers and different phrasings — uses one trigger dimension, not two, and does not fulfill the cross-dimension requirement." |
| C-20 | Anti-pattern rationale names specific output element by taxonomy | PASS | Four taxonomic categories named explicitly. Exclusion: "A 'Why It Applies Here' explanation that references team size, structural type, or generic org properties without naming a concrete element does not pass." |

**Essential:** 5/5 (60) | **Recommended:** 3/3 (30) | **Aspirational:** 12/12 (10.0) | **Total: 100.0**

**Finding:** Register is cosmetic when exclusion conditions are maintained in any phrasing. Descriptive "does not contribute to the count" and "does not fulfill this section" carry the same semantic load as DO NOT guards.

---

### V-02 — Output Format: Explicit Self-Reference Block

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia precedes org diagram | PASS | Standard imperative guards preserved. |
| C-02 | Org hierarchy readable | PASS | Same as V-01. |
| C-03 | Roles input honored | PASS | |
| C-04 | Headcount by area | PASS | |
| C-05 | Operating rhythm table | PASS | |
| C-06 | Committee charters complete | PASS | "DO NOT label this section optional." |
| C-07 | All four output sections present | PASS | Nine sections enumerated (adds ORG-ELEMENT REGISTER). All four canonical sections (inertia, diagram, headcount, rhythm) present. |
| C-08 | Decision rights indicated | PASS | |
| C-09 | Org evolution path | PASS | |
| C-10 | Anti-patterns flagged | PASS | |
| C-11 | Inertia steelmans status quo | PASS | "DO include at minimum two numbered reasons. DO NOT proceed until at least two are written." |
| C-12 | Decides/Escalates split | PASS | "DO NOT use a single 'Decision Scope' column — the Decides and Escalates columns are separate and both required." |
| C-13 | Verdict includes re-assessment trigger | PASS | |
| C-14 | Steelman reasons mechanism-typed | PASS | "DO NOT write generic statements like 'the team communicates well.'" |
| C-15 | Three-part inertia labeled | PASS | Three labeled sub-sections: Case for Staying Flat, Rebuttal, VERDICT. |
| C-16 | Escalates column names destination | PASS | "DO populate the Escalates field with a named destination. DO NOT write 'everything not listed under Decides.'" |
| C-17 | Evolution trigger table has two distinct rows | PASS | "Two headcount thresholds at different values count as one dimension — they do not pass as two distinct rows." |
| C-18 | Anti-pattern table has domain-specific rationale column | PASS | ORG-ELEMENT REGISTER block filled before Anti-Pattern Watch; "DO cite an element from the register by name — copy the exact name." |
| C-19 | Evolution trigger table uses cross-dimension diversity | PASS | Row 2 dimension vocabulary; "DO NOT proceed until both rows are written with distinct trigger dimensions." |
| C-20 | Anti-pattern rationale names specific output element by taxonomy | PASS | **Strongest guard in R5.** ORG-ELEMENT REGISTER physically written first; Anti-Pattern Watch must cite from it by exact name. "DO NOT write a 'Why It Applies Here' cell that does not name any element from the register." The lookup is structurally non-optional — the register artifact must exist before rationale is written. |

**Essential:** 5/5 (60) | **Recommended:** 3/3 (30) | **Aspirational:** 12/12 (10.0) | **Total: 100.0**

**Finding:** Physical intermediate output (register block before dependent section) is a stronger C-20 guard than inline taxonomy instruction. The model must produce the register as a named artifact, making omission visible rather than silent.

---

### V-03 — 4-Part Inertia With Trap Guard

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia precedes org diagram | PASS | |
| C-02 | Org hierarchy readable | PASS | |
| C-03 | Roles input honored | PASS | |
| C-04 | Headcount by area | PASS | |
| C-05 | Operating rhythm table | PASS | |
| C-06 | Committee charters complete | PASS | |
| C-07 | All four output sections present | PASS | |
| C-08 | Decision rights indicated | PASS | |
| C-09 | Org evolution path | PASS | |
| C-10 | Anti-patterns flagged | PASS | |
| C-11 | Inertia steelmans status quo | PASS | Trap guard: "DO NOT move mechanism-typed content to the How We Coordinate Today sub-section. The numbered reasons live here, in this sub-section, before the inventory is written." Case for Staying Flat structurally precedes How We Coordinate Today; migration is explicitly forbidden. |
| C-12 | Decides/Escalates split | PASS | |
| C-13 | Verdict includes re-assessment trigger | PASS | |
| C-14 | Steelman reasons mechanism-typed | PASS | "Each reason names a specific, observable coordination mechanism — a communication channel, an informal lead role, a decision pattern, or a recurring cadence. Generic assertions about team cohesion or communication quality do not count as reasons." C-11 guard keeps reasons in Case for Staying Flat, so mechanism typing applies to the right sub-section. |
| C-15 | Three-part inertia labeled | PASS | 4-part structure contains all three required labeled components: Case for Staying Flat (status-quo defense), How We Coordinate Today (coordination mechanisms inventory), VERDICT (verdict with trigger). Pass condition tests presence of three, not exclusivity of three. |
| C-16 | Escalates column names destination | PASS | |
| C-17 | Evolution trigger table has two distinct rows | PASS | "DO NOT write two headcount thresholds — this counts as one dimension, not two." |
| C-18 | Anti-pattern table has domain-specific rationale column | PASS | "Named elements are: area names from the Headcount table, committee or cadence names from the Rhythm Table or Charters, the headcount total or an individual area count, a DRI role from the rhythm table." |
| C-19 | Evolution trigger table uses cross-dimension diversity | PASS | Row 2 vocabulary: workload signal / structural symptom / milestone. Template row label: "Row 2 — workload signal or structural symptom — NOT a second headcount number." |
| C-20 | Anti-pattern rationale names specific output element by taxonomy | PASS | Four-category taxonomy present. Exclusion: "A 'Why It Applies Here' cell that names none of these elements and could apply to any org of similar type does not pass." |

**Essential:** 5/5 (60) | **Recommended:** 3/3 (30) | **Aspirational:** 12/12 (10.0) | **Total: 100.0**

**Finding:** The R3/V-03 failure was a structural sequencing bug, not an inherent property of 4-part inertia. With an explicit trap guard and structural separation (Case for Staying Flat completes before How We Coordinate Today begins), C-11 and C-14 pass. C-15 is an inclusive check, not an exclusive count.

---

### V-04 — Descriptive Register + Explicit Self-Reference Block

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-08 | All essential + recommended | PASS | Descriptive framing with exclusion conditions maintained throughout; ORG-ELEMENT REGISTER step present. |
| C-09 | Org evolution path | PASS | |
| C-10 | Anti-patterns flagged | PASS | |
| C-11 | Inertia steelmans status quo | PASS | "The numbered reasons remain in this sub-section." Descriptive but constraint is clear. |
| C-12 | Decides/Escalates split | PASS | "The Decides and Escalates columns are distinct." |
| C-13 | Verdict includes re-assessment trigger | PASS | |
| C-14 | Steelman reasons mechanism-typed | PASS | Mechanism constraint present in descriptive form; exclusion condition maintained. |
| C-15 | Three-part inertia labeled | PASS | Three labeled sub-sections: Case for Staying Flat, Rebuttal, VERDICT. |
| C-16 | Escalates column names destination | PASS | "naming the specific destination role or forum that receives the escalation." |
| C-17 | Evolution trigger table has two distinct rows | PASS | "A table with two headcount numbers — even at different values — uses one dimension." |
| C-18 | Anti-pattern table has domain-specific rationale column | PASS | ORG-ELEMENT REGISTER (descriptive form) + "The rationale cites the element by the exact name it appears in the register." |
| C-19 | Evolution trigger table uses cross-dimension diversity | PASS | "The two rows address categorically different trigger dimensions. Row 1 names a headcount threshold. Row 2 names a trigger from a different category." Vocabulary list provided. |
| C-20 | Anti-pattern rationale names specific output element by taxonomy | PASS | Register block (descriptive) + "A 'Why It Applies Here' explanation that references team size, org type, or structural pattern without naming a specific element from the register does not pass." |

**Note on interaction effect:** V-04's ORG-ELEMENT REGISTER instruction reads "the output contains a named-element register" rather than "DO produce this block — DO NOT skip it." This is the weakest expression of the register-step guard across V-02 and V-04, which is the predicted interaction risk. The constraint is still present, but a model under token pressure has slightly less enforcement than V-02's gate instruction. C-20 rated PASS on design quality; flagged as the axis most likely to show degradation in live runs.

**Essential:** 5/5 (60) | **Recommended:** 3/3 (30) | **Aspirational:** 12/12 (10.0) | **Total: 100.0**

---

### V-05 — 4-Part Inertia + Full V-04/R4 Guards

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-08 | All essential + recommended | PASS | Imperative framing throughout; standard guards. |
| C-09 | Org evolution path | PASS | |
| C-10 | Anti-patterns flagged | PASS | |
| C-11 | Inertia steelmans status quo | PASS | "CRITICAL: The numbered reasons stay here. DO NOT move mechanism content to Sub-section 2. Sub-section 1 must contain at minimum two numbered mechanism reasons before Sub-section 2 begins." Strongest C-11 guard in R5. |
| C-12 | Decides/Escalates split | PASS | |
| C-13 | Verdict includes re-assessment trigger | PASS | |
| C-14 | Steelman reasons mechanism-typed | PASS | CRITICAL guard ensures mechanism-typed reasons remain in Case for Staying Flat where C-14 evaluates them. |
| C-15 | Three-part inertia labeled | PASS | 4-part structure: Case for Staying Flat (status-quo defense) + How We Coordinate Today (coordination mechanisms inventory) + Rebuttal + VERDICT (verdict block with trigger). All three required labeled sub-sections present. Pass condition is inclusive. |
| C-16 | Escalates column names destination | PASS | |
| C-17 | Evolution trigger table has two distinct rows | PASS | "DO NOT write two headcount thresholds — this counts as one dimension, not two." |
| C-18 | Anti-pattern table has domain-specific rationale column | PASS | Four-category taxonomy present; exclusion condition stated. |
| C-19 | Evolution trigger table uses cross-dimension diversity | PASS | Dimension vocabulary: workload / structural symptom / milestone. Template label: "NOT a second headcount number." |
| C-20 | Anti-pattern rationale names specific output element by taxonomy | PASS | "DO name an element from one of these four categories in each 'Why It Applies Here' cell. DO NOT write a cell that references team size, org type, or structural pattern without citing a specific named element from the artifact above." |

**Essential:** 5/5 (60) | **Recommended:** 3/3 (30) | **Aspirational:** 12/12 (10.0) | **Total: 100.0**

**Finding:** Prompt complexity does not erode quality when structural guards are layered rather than nested. The 4-part inertia trap guard (CRITICAL label) is compatible with the full V-04/R4 guard set. C-15 passes with 4-part inertia because its pass condition checks for the presence of three labeled sub-sections, not their exclusive count.

---

### Summary Table

| Variation | Essential | Recommended | Aspirational | Total | Band |
|-----------|-----------|-------------|--------------|-------|------|
| V-01 | 5/5 (60) | 3/3 (30) | 12/12 (10.0) | **100.0** | Golden |
| V-02 | 5/5 (60) | 3/3 (30) | 12/12 (10.0) | **100.0** | Golden |
| V-03 | 5/5 (60) | 3/3 (30) | 12/12 (10.0) | **100.0** | Golden |
| V-04 | 5/5 (60) | 3/3 (30) | 12/12 (10.0) | **100.0** | Golden |
| V-05 | 5/5 (60) | 3/3 (30) | 12/12 (10.0) | **100.0** | Golden |

**Ceiling confirmation:** All five variation axes reach 100.0. The V-04/R4 ceiling is axis-robust.

---

### Excellence Signals (R5)

**1. Descriptive register preserves constraint semantics.** V-01 confirms the V-05/R4 hypothesis (never scored): imperative DO/DO NOT framing and descriptive "this section produces..." framing are semantically equivalent when exclusion conditions are maintained. "Does not contribute to the count," "does not fulfill this section," and "does not pass" carry the same load as DO NOT guards. Register is a stylistic choice, not a correctness variable.

**2. Physical intermediate output enforces C-20 more reliably than inline taxonomy.** V-02's ORG-ELEMENT REGISTER forces the model to produce a named artifact before writing Anti-Pattern rationale. The register becomes a lookup target the model has already written — citing from it by exact name is structurally non-optional. Inline taxonomy instruction (V-01, V-03, V-05) is also sufficient, but the physical register eliminates the failure mode of rationale that references structure type without naming a specific output element.

**3. 4-part inertia passes C-11/C-14 when Case for Staying Flat is structurally guarded.** V-03 and V-05 confirm the R3/V-03 failure was a sequencing bug. The CRITICAL guard ("Sub-section 1 must contain at minimum two numbered mechanism reasons before Sub-section 2 begins") fixes it by making mechanism migration structurally impossible — Case for Staying Flat must complete before How We Coordinate Today can begin.

**4. C-15 is an inclusive criterion, not exclusive.** The pass condition checks that three specific labeled sub-sections exist (status-quo defense, coordination mechanisms inventory, VERDICT block), not that exactly three sub-sections exist. A 4-part structure that includes a Rebuttal sub-section passes C-15 because all three required components are present and labeled.

---

### R5 Interpretation

R5 answers all three design questions conclusively:
- **Does phrasing register matter?** No — V-01 = 100.0.
- **Does the explicit self-reference step improve C-20?** Yes structurally (strongest guard), though V-04's descriptive variant introduces a token-pressure risk in live runs.
- **Can 4-part inertia pass C-11/C-14?** Yes, with the CRITICAL trap guard and structural separation — V-03 = 100.0.

The rubric has reached its current ceiling. No new aspirational criteria are implied by R5 variation behavior; the ceiling holds under all five axes.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Descriptive and imperative register are semantically equivalent when exclusion conditions are maintained — 'does not contribute to the count' carries the same load as DO NOT", "Physical intermediate output (ORG-ELEMENT REGISTER block before Anti-Pattern Watch) enforces C-20 by making the lookup non-optional — the model cites from an artifact it has already produced", "4-part inertia resolves the C-11/C-14 trap when Case for Staying Flat is guarded to complete before the coordination inventory sub-section begins", "C-15 is inclusive (three required labeled sub-sections must be present) not exclusive (exactly three) — 4-part structures pass when all three required components are labeled"]}
```
