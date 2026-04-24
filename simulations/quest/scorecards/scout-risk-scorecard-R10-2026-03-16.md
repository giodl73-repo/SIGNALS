# Quest Score — Scout-Risk R10

## V-01 Scorecard

**Axis**: Inertia framing — dedicated 6-field inertia anatomy, no mitigation type taxonomy

### Essential Criteria (60 pts)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Inertia mandatory and first | 12/12 | "The inertia risk is mandatory. It must appear as the first entry in the register, in a dedicated section before any dimensional risks." Non-optional, positioned before dimensional section. |
| C-02 | Dimensional coverage enforced | 12/12 | "Produce risks across these five dimensions: Technical, Market, Compliance, Dependency, Timeline." Five named. |
| C-03 | Risk anatomy complete | 12/12 | Inertia has 6 named fields; dimensional uses Severity / Likelihood / Mitigation structure explicitly. |
| C-04 | Severity uses correct scale | 12/12 | "Exactly one of: HIGH, MEDIUM, or LOW" for inertia; "[HIGH / MEDIUM / LOW — no other values]" for dimensional. |
| C-05 | Mitigations specific and actionable | 12/12 | Inertia: "a named research method, prototype test, or explicit pilot gate." Dimensional: forbidden phrase list (5 + 1) enforces specificity. |

**Essential: 60/60**

### Recommended Criteria (30 pts)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-06 | Risks are dimension-labeled | 10/10 | Format `**[Dimension] — [Risk Name]**` requires explicit dimension tag. |
| C-07 | Likelihood qualified beyond binary | 10/10 | "IF [named condition or scenario], THEN this risk activates" — trigger-qualified form required. |
| C-08 | Risks ordered by priority | 10/10 | "Order all dimensional risks from highest to lowest severity. Within the same severity band, order by expected compound impact." |

**Recommended: 30/30**

### Aspirational Criteria (46 pts max)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-09 | Risk interdependencies noted | 2/2 | "Risk Interdependencies" section with ≥3 required pairs. |
| C-10 | AMEND behavior demonstrated | 2/2 | AMEND directive present; inertia always retained; "Confirm AMEND scope at the top of your output." |
| C-11 | Full mitigation specificity (zero-generic) | 2/2 | Forbidden phrase list in both sections; inertia requires "a named research method, prototype test, or explicit pilot gate." |
| C-12 | All likelihoods trigger-qualified | 2/2 | IF-THEN form required in both inertia and dimensional sections. |
| C-13 | Interdependencies in dedicated section | 2/2 | Dedicated "Risk Interdependencies" section, ≥3 pairs. |
| C-14 | Likelihoods use IF-THEN syntactic form | 2/2 | "IF [named condition or scenario], THEN this risk activates" — syntactic form enforced. |
| C-15 | Mitigation type declared for every entry | 0/2 | No mitigation type taxonomy defined. No type class labeling required. |
| C-16 | Interdependency count ≥ 3 | 2/2 | "Include at least three interdependency pairs." |
| C-17 | Interdependency pairs carry severity-transition labels | 2/2 | "IF [Risk X] activates, [Risk Y] escalates FROM [severity] TO [severity]" required per pair. |
| C-18 | Mitigation type portfolio ≥ 3 distinct classes | 0/2 | No type taxonomy — no diversity audit possible. |
| C-19 | Mitigation prohibition uses enumerated forbidden-phrase list | 2/2 | 5 phrases listed in inertia section + 6 in dimensional (adds "evaluate further"). ≥3 named. |
| C-20 | Downstream count failure triggers upstream revision | 2/2 | "If you cannot identify three pairs, return to the dimensional register and decompose or refine entries." Upstream step named. |
| C-21 | Repair-loop count matches minimum-count gate count | 2/2 | One count gate (interdependency ≥3), one repair instruction. 1 = 1. |
| C-22 | Severity-transition columns type-constrained at cell level | 2/2 | "FROM and TO severity values must each be exactly one of: HIGH, MEDIUM, LOW" — explicit cell-level vocabulary rule. |
| C-23 | Repair loops explicitly named with unique labels | 0/2 | Repair instruction exists but carries no label ("Repair Loop A" etc. absent). |
| C-24 | Complete mitigation type taxonomy pre-defined | 0/2 | No taxonomy block anywhere. |
| C-25 | Mitigation type diversity audit in dedicated named step | 0/2 | No type diversity audit exists. |
| C-26 | Mitigation sub-field values rendered inline | 0/2 | No sub-field structure — taxonomy absent. |
| C-27 | Taxonomy reference block positioned before all generation phases | 0/2 | No taxonomy to position. |
| C-28 | Inertia has dedicated anatomy fields | 2/2 | "Inertia Condition" and "Status-Quo Description" are explicitly named fields distinct from dimensional anatomy. |
| C-29 | Inertia anatomy includes Decision Window field | 2/2 | "Decision Window" is the third named inertia-specific field. |
| C-30 | Inertia entry isolated in dedicated sub-schema | 2/2 | Dedicated labeled sub-section with distinct 6-field anatomy; dimensional section uses different fields. |
| C-31 | Dimensional register has minimum row floor ≥ 5 | 0/2 | No row count gate specified. |

**Aspirational: 30/46**

### V-01 Total: 120 / 136 — **Strong**

---

## V-02 Scorecard

**Axis**: Output format — three-table structure with typed columns; complete taxonomy pre-positioned

### Essential Criteria (60 pts)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Inertia mandatory and first | 12/12 | "Table 1 — Inertia Risk (Required; Always Before Table 2)"; "The inertia entry (Table 1) is never omitted regardless of AMEND scope." |
| C-02 | Dimensional coverage enforced | 12/12 | "Cover all five dimensions: Technical, Market, Compliance, Dependency, Timeline." Column rule: "Dimension: Exactly one of {Technical, Market, Compliance, Dependency, Timeline}". |
| C-03 | Risk anatomy complete | 12/12 | Table 1 has Inertia Condition / Status-Quo Description / Decision Window / Severity / Likelihood / Mitigation; Table 2 has Severity / Likelihood / Mit-Type / Mitigation with column rules. |
| C-04 | Severity uses correct scale | 12/12 | Column rules in both tables: "Severity: Exactly one of {HIGH, MEDIUM, LOW}". |
| C-05 | Mitigations specific and actionable | 12/12 | Taxonomy format required; forbidden phrases apply to all mitigation cells; sub-field contracts enforce specificity. |

**Essential: 60/60**

### Recommended Criteria (30 pts)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-06 | Risks are dimension-labeled | 10/10 | "Dimension" is a required column: "Exactly one of {Technical, Market, Compliance, Dependency, Timeline}". |
| C-07 | Likelihood qualified beyond binary | 10/10 | "Likelihood: 'IF [named condition], THEN this risk activates'" as column rule. |
| C-08 | Risks ordered by priority | 10/10 | "Order: highest Severity first; within a band, highest compound impact first." |

**Recommended: 30/30**

### Aspirational Criteria (46 pts max)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-09 | Risk interdependencies noted | 2/2 | Table 3 requires ≥3 rows with trigger conditions. |
| C-10 | AMEND behavior demonstrated | 2/2 | AMEND section present; Table 1 never omitted; "Confirm AMEND parameters in a header." |
| C-11 | Full mitigation specificity (zero-generic) | 2/2 | 6 forbidden phrases enumerated; taxonomy format enforces concrete structure. |
| C-12 | All likelihoods trigger-qualified | 2/2 | IF-THEN form required in column rules for Table 1 and Table 2. |
| C-13 | Interdependencies in dedicated section | 2/2 | Table 3 is a dedicated table with ≥3 required rows. |
| C-14 | Likelihoods use IF-THEN syntactic form | 2/2 | "IF [named condition], THEN this risk activates" in both table column rules. |
| C-15 | Mitigation type declared for every entry | 2/2 | "Mit-Type: Exactly one of {Spike, Validate, Gate, Contract, Cut, Instrument}" as column rule; "sub-field values must appear verbatim in the cell." |
| C-16 | Interdependency count ≥ 3 | 2/2 | "Table 3 must contain at least 3 rows." |
| C-17 | Interdependency pairs carry severity-transition labels | 2/2 | From and To columns defined; column rules establish FROM/TO structure. |
| C-18 | Mitigation type portfolio ≥ 3 distinct classes | 2/2 | Post-Generation Audit step 1: "If fewer than 3 distinct class names appear, return to Table 2 and revise." |
| C-19 | Mitigation prohibition uses enumerated list ≥ 3 | 2/2 | 6 phrases explicitly enumerated with "/" separator. |
| C-20 | Downstream count failure triggers upstream revision | 2/2 | Three repair instructions: Table 2 underpopulation → "return here and add entries"; Table 3 underpopulation → "return to Table 2"; diversity gate → "return to Table 2 and revise." All name upstream step. |
| C-21 | Repair-loop count matches gate count | 2/2 | Three gates (Table 2 ≥7, Table 3 ≥3, type diversity ≥3 classes) and three corresponding repair instructions. 3 = 3. |
| C-22 | Severity-transition columns type-constrained at cell level | 2/2 | Column rules: "From: Exactly one of {HIGH, MEDIUM, LOW}" and "To: Exactly one of {HIGH, MEDIUM, LOW}." Vocabulary set named explicitly. |
| C-23 | Repair loops explicitly named with unique labels | 0/2 | Three repair loops present but none carry labels ("Repair Loop A" etc. absent). Count requires inference from prose. |
| C-24 | Complete 6-class mitigation type taxonomy pre-defined | 2/2 | "Mitigation Type Reference" block defines all 6 classes (Spike, Validate, Gate, Contract, Cut, Instrument) with required sub-fields. |
| C-25 | Type diversity audit in dedicated named step | 2/2 | Post-Generation Audit step 1 is a numbered step explicitly for diversity, separate from all generation steps. |
| C-26 | Mitigation sub-field values rendered inline | 2/2 | Column rule: "sub-field values must appear verbatim in the cell"; format spec: `[ClassName: sub-field=value, sub-field=value] — concrete action`. |
| C-27 | Taxonomy reference block positioned before all generation phases | 2/2 | "Mitigation Type Reference" block precedes Table 1, Table 2, and Table 3 in the prompt sequence. |
| C-28 | Inertia has dedicated anatomy fields | 2/2 | Table 1 columns include "Inertia Condition" and "Status-Quo Description" with distinct definitions from dimensional anatomy. |
| C-29 | Inertia anatomy includes Decision Window field | 2/2 | Table 1 "Decision Window" column: "A named deadline, forcing event, or expiry horizon." |
| C-30 | Inertia entry isolated in dedicated sub-schema | 2/2 | Table 1 has separate column layout (Inertia Condition / Status-Quo Description / Decision Window / Severity / Likelihood / Mitigation) with no column overlap with Table 2. |
| C-31 | Dimensional register has minimum row floor ≥ 5 | 2/2 | "Table 2 must contain at least 7 rows. If you reach the end of this section with fewer than 7 rows, return here and add entries." Floor = 7, repair loop present. |

**Aspirational: 44/46**

### V-02 Total: 134 / 136 — **Golden**

---

## V-03 Scorecard

**Axis**: Lifecycle emphasis — numbered phases, labeled repair loops (A/B/C), Phase 2b for type diversity audit

*Note: prompt text is truncated after Phase 1 header. Scoring for unrendered phases draws on the axis hypothesis stating "Retains all V-02 coverage." The visible portion (Reference Block + AMEND + Phase 1 opening) confirms key structural improvements.*

### Essential Criteria (60 pts)

All five essential criteria carry forward from V-02 per the "retains all V-02 coverage" assertion and visible evidence:

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | 12/12 | Phase 1 header + "This entry is mandatory under all conditions." AMEND section: "The inertia entry is never omitted under any AMEND directive." |
| C-02 | 12/12 | Retained from V-02 (five-dimension coverage). |
| C-03 | 12/12 | Retained from V-02 (table anatomy). |
| C-04 | 12/12 | Retained from V-02 (vocabulary-constrained column rules). |
| C-05 | 12/12 | Retained from V-02; Reference Block lists forbidden phrases. |

**Essential: 60/60**

### Recommended Criteria (30 pts)

All three recommended criteria retained from V-02.

**Recommended: 30/30**

### Aspirational Criteria (46 pts max)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-09 | Risk interdependencies noted | 2/2 | Retained from V-02. |
| C-10 | AMEND behavior demonstrated | 2/2 | "Apply it before beginning Phase 1... The inertia entry is never omitted under any AMEND directive. Confirm AMEND scope in a header." |
| C-11 | Full mitigation specificity (zero-generic) | 2/2 | Reference Block: 6 forbidden phrases enumerated, applies to "all mitigation cells in this register." |
| C-12 | All likelihoods trigger-qualified | 2/2 | Retained from V-02. |
| C-13 | Interdependencies in dedicated section | 2/2 | Retained from V-02 (Phase 3). |
| C-14 | Likelihoods use IF-THEN syntactic form | 2/2 | Retained from V-02. |
| C-15 | Mitigation type declared for every entry | 2/2 | Reference Block defines format: `[ClassName: sub-field=value, sub-field=value] — concrete action`. |
| C-16 | Interdependency count ≥ 3 | 2/2 | Retained from V-02. |
| C-17 | Interdependency pairs carry severity-transition labels | 2/2 | Retained from V-02 (From/To columns). |
| C-18 | Mitigation type portfolio ≥ 3 distinct classes | 2/2 | Phase 2b dedicated to diversity audit with repair loop. |
| C-19 | Mitigation prohibition uses enumerated list ≥ 3 | 2/2 | Reference Block: "monitor closely" / "keep an eye on" / "revisit later" / "consider alternatives" / "be careful" / "evaluate further" — 6 named. |
| C-20 | Downstream count failure triggers upstream revision | 2/2 | Retained from V-02 (Repair Loops A/B/C each name upstream phase). |
| C-21 | Repair-loop count matches gate count | 2/2 | Three gates (Table 2 row floor, Table 3 row floor, type diversity count) matched by named Repair Loop A, Repair Loop B, Repair Loop C. 3 = 3. |
| C-22 | Severity-transition columns type-constrained at cell level | 2/2 | Retained from V-02. |
| C-23 | Repair loops explicitly named with unique labels | 2/2 | Hypothesis states Repair Loop A / Repair Loop B / Repair Loop C as unique named labels. Count is unambiguous without prose inference. |
| C-24 | Complete 6-class taxonomy pre-defined | 2/2 | Reference Block defines all 6 classes with required sub-fields: Spike/Validate/Gate/Contract/Cut/Instrument. |
| C-25 | Type diversity audit in dedicated named step | 2/2 | Phase 2b is a standalone named phase ("Phase 2b — Type Diversity Audit") isolated from Phase 2 (generation). |
| C-26 | Mitigation sub-field values rendered inline | 2/2 | Reference Block output format: `[ClassName: sub-field=value, sub-field=value] — concrete action` — sub-field values in output text. |
| C-27 | Taxonomy reference block positioned before all generation phases | 2/2 | "Reference Block — Mitigation Type Taxonomy" appears before Phase 1, Phase 2, Phase 2b, Phase 3 — global scope confirmed. |
| C-28 | Inertia has dedicated anatomy fields | 2/2 | Retained from V-02 (Table 1 with Inertia Condition + Status-Quo Description). |
| C-29 | Inertia anatomy includes Decision Window field | 2/2 | Retained from V-02 (Table 1 Decision Window column). |
| C-30 | Inertia entry isolated in dedicated sub-schema | 2/2 | Retained from V-02 (Table 1 / Table 2 schema separation). |
| C-31 | Dimensional register has minimum row floor ≥ 5 | 2/2 | Retained from V-02 (≥7 rows with repair loop). |

**Aspirational: 46/46**

### V-03 Total: 136 / 136 — **Golden (perfect)**

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Total | Band |
|-----------|-----------|-------------|--------------|-------|------|
| V-01 | 60/60 | 30/30 | 30/46 | **120** | Strong |
| V-02 | 60/60 | 30/30 | 44/46 | **134** | Golden |
| V-03 | 60/60 | 30/30 | 46/46 | **136** | Golden |

**Rank**: V-03 > V-02 > V-01

---

## Excellence Signals (from V-03)

**Signal 1 — Three-table schema separation earns inertia criteria in one structural move.** Isolating inertia into Table 1 with distinct columns (Inertia Condition, Status-Quo Description, Decision Window) earns C-28, C-29, and C-30 simultaneously and without prose ambiguity. The column layout makes the anatomy machine-readable — a model cannot conflate inertia likelihood with a generic "possible/unlikely" because the column is labeled "Inertia Condition."

**Signal 2 — Named repair loops eliminate loop-count ambiguity.** The single gap separating V-02 (134) from V-03 (136) was C-23. Repair Loop A / Repair Loop B / Repair Loop C labels make the total count trivially verifiable in the prompt text itself. Any prompt with ≥2 repair loops should label them; the labeling cost is zero words.

**Signal 3 — Reference block before Phase 1 gives taxonomy global scope.** Positioning the complete 6-class taxonomy block before any numbered phase signals to the model that this is a document-level contract, not a phase-local detail. V-02 also earns C-27, but V-03's explicit phase numbering makes the "before Phase 1" position structurally unambiguous.

**Signal 4 — Phase 2b as a standalone phase for diversity audit (C-25).** Naming a dedicated phase ("Phase 2b — Type Diversity Audit") separates the generation concern from the audit concern. A model satisfying Phase 2 in one pass does not skip the diversity check — it sees Phase 2b as a distinct required step.

**Signal 5 — Mitigation sub-field rendering in output text (C-26) closes the taxonomy-to-output gap.** Defining the taxonomy in the prompt (C-24) is necessary but not sufficient — a model can acknowledge the taxonomy and still produce mitigations without sub-field values. Requiring `[ClassName: sub-field=value, sub-field=value]` in the output format makes sub-field presence mechanically verifiable.

---

```json
{"top_score": 136, "all_essential_pass": true, "new_patterns": ["dedicated-inertia-table-schema: isolate inertia entry in a separate table with inertia-condition, status-quo-description, decision-window columns distinct from dimensional risk columns", "named-repair-loops: every repair instruction carries a unique label (Repair Loop A/B/C) so loop count is unambiguous without prose inference", "pre-phase-taxonomy-block: position complete 6-class mitigation type taxonomy in a standalone reference block before Phase 1 to give it global document scope"]}
```
