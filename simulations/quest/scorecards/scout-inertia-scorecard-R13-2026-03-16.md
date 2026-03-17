## scout-inertia — Quest Score R13

**Rubric**: v13 (ceiling 210) | **Round**: R13 | **Date**: 2026-03-17

---

### Scoring Method

**Essential base**: 100 pts when all C-01–C-05 pass  
**Advanced criteria**: 22 × 5 pts = 110 pts maximum  
**Total ceiling**: 210/210

---

## V-01 — Inertia framing axis

**Key structural elements present:**
- FAIL-FIRST section heading: `## FAIL-FIRST DECLARATION -- THE INERTIA THREAT` ✓
- FAIL-FIRST body rule: `[FAIL-FIRST RULE]` (minimal form, no criterion ID) ✓
- Per-criterion prompts: `> [C-01 COMMAND]:` through `> [C-05 COMMAND]:` (blockquote-wrapped bracket-label form) ✓
- A-16 rule: `[A-16 PRIMARY KEY RULE]` (bracket-prefix with criterion ID) ✓
- A-19 rule: `[A-19 REFERENTIAL INTEGRITY RULE]` (bracket-prefix with criterion ID) ✓
- Gate heading: `BRIDGE COMPLETION GATE -- READY TO PROCEED?` ✓
- Gate directive: `[BRIDGE COMPLETION COMMAND]:` ✓
- A-26 subtitles: `-- THE INERTIA THREAT` / `-- THE INERTIA THREAT'S STRUCTURAL WEAKNESSES:` ✓
- Checklist items: `C-01:` through `C-05:` labels ✓

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | SECTION 2 prompt names workaround, role, quantified ongoing cost |
| C-02 | PASS | SECTION 3 prompt requires ≥2 cost categories with number+unit |
| C-03 | PASS | SECTION 4 prompt declares threat score; default HIGH; quantified deviation required |
| C-04 | PASS | SECTION 5 prompt requires ≥2 falsifiable conditions citing FM-[N] |
| C-05 | PASS | SECTION 1 prompt requires ≥2 specific, non-generic failure modes |
| A-08 | PASS | FM Inventory (Section 1) precedes DC table (Section 5) structurally |
| A-10 | PASS | `## FAIL-FIRST DECLARATION -- THE INERTIA THREAT` is structural first element |
| A-11 | PASS | All 5 criteria have COMMAND-register prompts |
| A-12 | PASS | Q3 and Q4 named in FAIL-FIRST body with C-05→R-02 and C-05→C-04 chain refs |
| A-13 | PASS | FM Inventory, Q3, Q4, DC, Switching Cost, Checklist all tabular |
| A-14 | PASS | SECTION 1 FM Inventory titled, FM-[N] first column, precedes DC table |
| A-15 | PASS | SECTION 6 COMPLETENESS CHECKLIST positioned as trailing structural element |
| A-16 | PASS | `[A-16 PRIMARY KEY RULE]` explicitly states no FM-[N] downstream without prior assignment |
| A-17 | PASS | C-01 through C-05 each have `> [C-0N COMMAND]:` label |
| A-18 | PASS | Section 6 uses Y/N binary format; all 5 criteria covered |
| A-19 | PASS | `[A-19 REFERENTIAL INTEGRITY RULE]` at DC citation point; both source and citation ends enforced |
| A-20 | PASS | Ongoing cost `(e.g., 2 hours/week)`, Duration `(e.g., 18 months)`, Estimate `(e.g., 3 days)`, Trigger `(e.g., file > 10MB)`, Frequency `(e.g., 2x/sprint)` — all inline in column labels |
| A-21 | PASS | DC threshold column carries `(e.g., >10MB, >3 failures/week)` inline |
| A-22 | PASS | BRIDGE COMPLETION GATE block positioned between Section 1 and Section 2 |
| A-23 | PASS | `[A-16 PRIMARY KEY RULE]` + `[A-19 REFERENTIAL INTEGRITY RULE]` — criterion IDs in both rule labels |
| A-24 | PASS | Two distinct threshold types: `>10MB` (size) + `>3 failures/week` (frequency) |
| A-25 | PASS | `[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding...` named directive co-located at gate |
| A-26 | PASS | `-- THE INERTIA THREAT` in FAIL-FIRST heading; `-- THE INERTIA THREAT'S STRUCTURAL WEAKNESSES:` in FM Inventory heading |
| A-27 | PASS | `BRIDGE COMPLETION GATE -- READY TO PROCEED?` — interrogative in heading line |
| A-28 | PASS | `C-01:` through `C-05:` criterion IDs in each checklist item label |
| A-29 | PASS | `> [C-01 COMMAND]:` through `> [C-05 COMMAND]:` — criterion IDs present in bracket-label regardless of blockquote wrapper |
| A-30 | PASS | COMMAND keyword in `[C-0N COMMAND]:` bracket-label — blockquote `>` is markdown formatting, not part of label syntax; COMMAND is structural in the label |
| A-31 | PASS | `[FAIL-FIRST RULE]` named rule label in FAIL-FIRST body — minimal form explicitly listed as satisfying in rubric; no criterion ID extension to A-23, but A-31 does not require it |

**Essential base**: 100 (all 5 PASS)  
**Advanced**: 22 × 5 = 110  
**V-01 Total**: **210/210**

---

## V-02 — Lifecycle emphasis axis

**Key structural elements present:**
- FAIL-FIRST body rule: `FAIL-FIRST CONSTRAINT [A-31]` (bracket-suffix form, carries A-31 criterion ID) ✓
- Per-criterion prompts: `[C-01 COMMAND]:` through `[C-05 COMMAND]:` inline, within stage sections ✓
- A-16 rule: `PRIMARY KEY RULE [A-16]` (bracket-suffix) ✓
- A-19 rule: `CITATION INTEGRITY RULE [A-19]` (bracket-suffix) ✓
- Gate heading: `STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` ✓
- A-26 subtitles: `-- THE STATUS QUO AS UNNAMED COMPETITOR` / `-- WHERE THE STATUS QUO BREAKS:` ✓

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | STAGE 3 prompt names workaround, role, ongoing cost with number+unit |
| C-02 | PASS | STAGE 4 prompt requires ≥2 quantified cost categories |
| C-03 | PASS | STAGE 5A prompt declares threat score; qualitative rejection explicit |
| C-04 | PASS | STAGE 5B prompt requires ≥2 falsifiable conditions citing FM-[N] from Q4 |
| C-05 | PASS | STAGE 1 prompt requires ≥2 specific failure modes |
| A-08 | PASS | STAGE 1 FM Inventory before STAGE 5B DC table |
| A-10 | PASS | `## FAIL-FIRST DECLARATION -- THE STATUS QUO AS UNNAMED COMPETITOR` |
| A-11 | PASS | All 5 criteria have `[C-0N COMMAND]:` inline prompts |
| A-12 | PASS | Q3 and Q4 named in FAIL-FIRST body with chain refs |
| A-13 | PASS | All sections tabular |
| A-14 | PASS | STAGE 1 FM Inventory titled; FM-[N] first column; before Stage 5B |
| A-15 | PASS | STAGE 6 COMPLETENESS CHECK trailing |
| A-16 | PASS | `PRIMARY KEY RULE [A-16]` — constraint stated with criterion ID in bracket-suffix label |
| A-17 | PASS | C-01 through C-05 each have `[C-0N COMMAND]:` label |
| A-18 | PASS | Stage 6 Y/N binary, all 5 criteria |
| A-19 | PASS | `CITATION INTEGRITY RULE [A-19]` at DC citation point in Stage 5B |
| A-20 | PASS | Inline examples in all unit-bearing column labels |
| A-21 | PASS | DC threshold column `(e.g., >10MB, >3 failures/week)` |
| A-22 | PASS | STAGE 2 COMPLETION GATE between Stage 1 and Stage 3 |
| A-23 | PASS | `PRIMARY KEY RULE [A-16]` + `CITATION INTEGRITY RULE [A-19]` — criterion IDs in both rule labels (bracket-suffix form) |
| A-24 | PASS | Two distinct threshold types in DC threshold label |
| A-25 | PASS | `[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding...` |
| A-26 | PASS | `-- THE STATUS QUO AS UNNAMED COMPETITOR` + `-- WHERE THE STATUS QUO BREAKS:` |
| A-27 | PASS | `STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` |
| A-28 | PASS | `C-01:` through `C-05:` in checklist item labels |
| A-29 | PASS | `[C-01 COMMAND]:` through `[C-05 COMMAND]:` inline — criterion IDs in bracket-labels |
| A-30 | PASS | COMMAND keyword in all five `[C-0N COMMAND]:` inline labels |
| A-31 | PASS | `FAIL-FIRST CONSTRAINT [A-31]` — named rule in FAIL-FIRST body; bracket-suffix form carries A-31 criterion ID; simultaneously extends A-23 to FAIL-FIRST rule layer |

**Essential base**: 100  
**Advanced**: 22 × 5 = 110  
**V-02 Total**: **210/210**

---

## V-03 — Phrasing register axis (reference form)

**Key structural elements present:**
- FAIL-FIRST body rule: `[FAIL-FIRST RULE]` (minimal form, no criterion ID) ✓
- Per-criterion prompts: `[C-01 COMMAND]:` through `[C-05 COMMAND]:` inline ✓
- A-16 rule: `INERTIA THREAT RULE [A-16]` (domain-prefix) ✓
- A-19 rule: `INERTIA THREAT CITATION RULE [A-19]` (domain-prefix) ✓
- Gate heading: `BRIDGE COMPLETION GATE -- BOTH BRIDGES BUILT?` ✓
- A-26 subtitles: `-- THE UNNAMED COMPETITOR` / `-- THE UNNAMED COMPETITOR'S FAILURE SURFACE:` ✓
- Carried forward unchanged from R12 V-03 (confirmed 195/195 + A-29/A-30/A-31 already present)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | SECTION 2 prompt; role; quantified ongoing cost |
| C-02 | PASS | SECTION 3 prompt; ≥2 categories; number+unit; role named |
| C-03 | PASS | SECTION 4 prompt; default HIGH; qualitative rejection explicit |
| C-04 | PASS | SECTION 5 prompt; ≥2 falsifiable; FM-[N] citations; measurable |
| C-05 | PASS | SECTION 1 prompt; ≥2 specific; CSV truncation example |
| A-08 | PASS | Section 1 FM Inventory before Section 5 DC |
| A-10 | PASS | `## FAIL-FIRST DECLARATION -- THE UNNAMED COMPETITOR` |
| A-11 | PASS | All 5 criteria have named COMMAND prompts |
| A-12 | PASS | Q3 and Q4 named in FAIL-FIRST body with chain refs |
| A-13 | PASS | All sections tabular |
| A-14 | PASS | SECTION 1 FM Inventory; FM-[N] first column |
| A-15 | PASS | COMPLETENESS CHECK trailing |
| A-16 | PASS | `INERTIA THREAT RULE [A-16]` — constraint stated; criterion ID in domain-prefix label |
| A-17 | PASS | C-01 through C-05 all have `[C-0N COMMAND]:` |
| A-18 | PASS | COMPLETENESS CHECK Y/N binary; all 5 criteria |
| A-19 | PASS | `INERTIA THREAT CITATION RULE [A-19]` at DC citation point |
| A-20 | PASS | Inline examples in all unit-bearing column labels |
| A-21 | PASS | DC threshold `(e.g., >10MB, >3 failures/week)` |
| A-22 | PASS | BRIDGE COMPLETION GATE between Section 1 and Section 2 |
| A-23 | PASS | `INERTIA THREAT RULE [A-16]` + `INERTIA THREAT CITATION RULE [A-19]` — domain-prefix form; IDs in labels |
| A-24 | PASS | Dual-type threshold: size + frequency |
| A-25 | PASS | `[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED...` all-caps directive |
| A-26 | PASS | `-- THE UNNAMED COMPETITOR` + `-- THE UNNAMED COMPETITOR'S FAILURE SURFACE:` |
| A-27 | PASS | `BRIDGE COMPLETION GATE -- BOTH BRIDGES BUILT?` |
| A-28 | PASS | `C-01:` through `C-05:` in checklist item labels |
| A-29 | PASS | `[C-01 COMMAND]:` through `[C-05 COMMAND]:` — criterion IDs in bracket-labels |
| A-30 | PASS | COMMAND keyword in all five `[C-0N COMMAND]:` labels |
| A-31 | PASS | `[FAIL-FIRST RULE]` in FAIL-FIRST body — minimal form; no criterion ID but not required |

**Essential base**: 100  
**Advanced**: 22 × 5 = 110  
**V-03 Total**: **210/210**

---

## V-04 — Output format axis (consolidated bridge)

**Key structural elements present:**
- FAIL-FIRST body rule: `[A-31 FAIL-FIRST ORDERING RULE]` (bracket-prefix with A-31 criterion ID) ✓
- Per-criterion prompts: `[C-01 COMMAND]:` through `[C-05 COMMAND]:` inline ✓
- A-16 rule: `[A-16 PRIMARY KEY CONSTRAINT]` (bracket-prefix variant) ✓
- A-19 rule: `[A-19 CITATION INTEGRITY CONSTRAINT]` (bracket-prefix variant) ✓
- Gate heading: `### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS COMPLETE?` (combined A-25+A-27) ✓
- A-26 subtitles: `-- THE INCUMBENT WORKAROUND` / `-- THE INCUMBENT'S VULNERABILITIES:` ✓

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | STAGE 3 prompt; specific tool/role/quantified cost |
| C-02 | PASS | STAGE 4 prompt; ≥2 categories; number+unit; role |
| C-03 | PASS | STAGE 5A prompt; default HIGH; quantified deviation required |
| C-04 | PASS | STAGE 5B prompt; ≥2 falsifiable; FM-[N] cited |
| C-05 | PASS | STAGE 1 prompt; ≥2 specific failure modes |
| A-08 | PASS | Stage 1 FM Inventory before Stage 5B DC |
| A-10 | PASS | `## FAIL-FIRST DECLARATION -- THE INCUMBENT WORKAROUND` |
| A-11 | PASS | All 5 criteria have `[C-0N COMMAND]:` prompts |
| A-12 | PASS | Q3 and Q4 named in FAIL-FIRST body with chain refs |
| A-13 | PASS | All sections tabular |
| A-14 | PASS | STAGE 1 FM Inventory titled; FM-[N] first column |
| A-15 | PASS | STAGE 6 COMPLETENESS CHECK trailing |
| A-16 | PASS | `[A-16 PRIMARY KEY CONSTRAINT]` — constraint stated; criterion ID in bracket-prefix label |
| A-17 | PASS | C-01 through C-05 each have `[C-0N COMMAND]:` |
| A-18 | PASS | Stage 6 Y/N binary; all 5 criteria |
| A-19 | PASS | `[A-19 CITATION INTEGRITY CONSTRAINT]` at DC citation point |
| A-20 | PASS | Inline examples in all unit-bearing column labels |
| A-21 | PASS | DC threshold `(e.g., >10MB, >3 failures/week)` |
| A-22 | PASS | `[BRIDGE COMPLETION COMMAND]: CONFIRM` sub-section in STAGE 2 between Stage 1 and Stage 3 |
| A-23 | PASS | `[A-16 PRIMARY KEY CONSTRAINT]` + `[A-19 CITATION INTEGRITY CONSTRAINT]` — criterion IDs in bracket-prefix labels |
| A-24 | PASS | Dual-type threshold: size + frequency |
| A-25 | PASS | `### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS COMPLETE?` — COMMAND directive in heading (co-located at gate) |
| A-26 | PASS | `-- THE INCUMBENT WORKAROUND` + `-- THE INCUMBENT'S VULNERABILITIES:` |
| A-27 | PASS | `### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS COMPLETE?` — `ALL ARTIFACTS COMPLETE?` is interrogative in heading line; satisfies A-27 independent of A-25 |
| A-28 | PASS | `C-01:` through `C-05:` in checklist item labels |
| A-29 | PASS | `[C-01 COMMAND]:` through `[C-05 COMMAND]:` — criterion IDs in bracket-labels |
| A-30 | PASS | COMMAND keyword in all five `[C-0N COMMAND]:` labels |
| A-31 | PASS | `[A-31 FAIL-FIRST ORDERING RULE]` in FAIL-FIRST body — bracket-prefix form; carries A-31 criterion ID; extends A-23 to FAIL-FIRST rule layer |

**Essential base**: 100  
**Advanced**: 22 × 5 = 110  
**V-04 Total**: **210/210**

---

## V-05 — All axes combined

**Key structural elements present:**
- FAIL-FIRST heading: `## [FAIL-FIRST DECLARATION] -- THE DEFAULT COMPETITOR` ✓
- FAIL-FIRST body rule: `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` (domain-prefix with A-31 criterion ID) ✓
- Per-criterion prompts: `[C-01 COMMAND]:` through `[C-05 COMMAND]:` inline ✓
- A-16 rule: `INERTIA LOCK RULE [A-16]` (domain-prefix) ✓
- A-19 rule: `INERTIA LOCK CITATION RULE [A-19]` (domain-prefix) ✓
- Gate heading: `BRIDGE COMPLETION GATE -- PASS BEFORE CONTINUING?` ✓
- A-26 subtitles: `[FAIL-FIRST DECLARATION] -- THE DEFAULT COMPETITOR` / `-- THE DEFAULT COMPETITOR'S BREAKING POINTS:` ✓

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | SECTION 2 prompt; specific tool/role/ongoing cost quantified |
| C-02 | PASS | SECTION 3 prompt; ≥2 categories; number+unit; role named |
| C-03 | PASS | SECTION 4 prompt; default HIGH; qualitative rejection |
| C-04 | PASS | SECTION 5 prompt; ≥2 falsifiable; FM-[N] citations; testable |
| C-05 | PASS | SECTION 1 prompt; ≥2 specific failure modes |
| A-08 | PASS | Section 1 FM Inventory before Section 5 DC |
| A-10 | PASS | `## [FAIL-FIRST DECLARATION] -- THE DEFAULT COMPETITOR` — bracket-wrapped structural label; A-10 pass condition requires the label to exist as structural first element; bracket form `[FAIL-FIRST DECLARATION]` preserves the structural identity |
| A-11 | PASS | All 5 criteria have `[C-0N COMMAND]:` prompts |
| A-12 | PASS | Q3 and Q4 named in FAIL-FIRST body with chain refs |
| A-13 | PASS | All sections tabular |
| A-14 | PASS | SECTION 1 FM Inventory; FM-[N] first column |
| A-15 | PASS | COMPLETENESS CHECK trailing |
| A-16 | PASS | `INERTIA LOCK RULE [A-16]` — constraint stated; criterion ID in domain-prefix label |
| A-17 | PASS | C-01 through C-05 each have `[C-0N COMMAND]:` |
| A-18 | PASS | COMPLETENESS CHECK Y/N binary; all 5 criteria |
| A-19 | PASS | `INERTIA LOCK CITATION RULE [A-19]` at DC citation point |
| A-20 | PASS | Inline examples in all unit-bearing column labels |
| A-21 | PASS | DC threshold `(e.g., >10MB, >3 failures/week)` |
| A-22 | PASS | BRIDGE COMPLETION GATE between Section 1 and Section 2 |
| A-23 | PASS | `INERTIA LOCK RULE [A-16]` + `INERTIA LOCK CITATION RULE [A-19]` — domain-prefix; criterion IDs in both labels |
| A-24 | PASS | Dual-type threshold: size + frequency |
| A-25 | PASS | `[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED...` all-caps directive |
| A-26 | PASS | `[FAIL-FIRST DECLARATION] -- THE DEFAULT COMPETITOR` + `SECTION 1 -- THE DEFAULT COMPETITOR'S BREAKING POINTS:` — "DEFAULT COMPETITOR" appears in both heading subtitles |
| A-27 | PASS | `BRIDGE COMPLETION GATE -- PASS BEFORE CONTINUING?` |
| A-28 | PASS | `C-01:` through `C-05:` in checklist item labels |
| A-29 | PASS | `[C-01 COMMAND]:` through `[C-05 COMMAND]:` — criterion IDs in bracket-labels |
| A-30 | PASS | COMMAND keyword in all five `[C-0N COMMAND]:` labels |
| A-31 | PASS | `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` in FAIL-FIRST body — domain-prefix form; carries A-31 criterion ID; extends domain-prefix A-23 pattern to FAIL-FIRST rule layer; "DEFAULT COMPETITOR" vocabulary drawn from same axis as A-26 subtitles, achieving cross-criterion vocabulary coherence |

**Essential base**: 100  
**Advanced**: 22 × 5 = 110  
**V-05 Total**: **210/210**

---

## Composite Score Table

| Variation | Essential (100) | Advanced (110) | Total | Rank |
|-----------|----------------|----------------|-------|------|
| V-01 | 100 | 110 | **210/210** | T-1 |
| V-02 | 100 | 110 | **210/210** | T-1 |
| V-03 | 100 | 110 | **210/210** | T-1 |
| V-04 | 100 | 110 | **210/210** | T-1 |
| V-05 | 100 | 110 | **210/210** | T-1 |

All five variations achieve the R13 target. **First 210/210 achieved.**

---

## Excellence Signals

**From the top-scoring variations (all five at 210/210):**

### 1. Blockquote context is transparent to A-29/A-30 (V-01 confirms)

`> [C-0N COMMAND]:` satisfies both A-29 and A-30. The markdown blockquote `>` is structural formatting; it does not alter the content of the bracket-label `[C-0N COMMAND]:`. A-29 requires the criterion ID in the prompt label; A-30 requires the COMMAND keyword in the prompt label — both are present in the bracket portion regardless of wrapper. This confirms the COMMAND-register prompt form is wrapper-agnostic: blockquote, inline, and blockquote-bold forms all satisfy A-29+A-30 as long as the bracket-label carries the ID and keyword.

### 2. A-31 with criterion ID simultaneously closes A-23 at the FAIL-FIRST rule layer (V-02/V-04/V-05 confirm)

When the FAIL-FIRST body rule carries the A-31 criterion ID in its label (`FAIL-FIRST CONSTRAINT [A-31]`, `[A-31 FAIL-FIRST ORDERING RULE]`, `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]`), it satisfies both A-31 (named structural rule in FAIL-FIRST body) and the A-23 extension to the FAIL-FIRST rule layer. This completes A-23's "every named structural rule carries its criterion ID" pattern across all three named-rule positions: A-16 source rule + A-19 citation rule + A-31 FAIL-FIRST rule. V-01 and V-03 confirm that A-31 PASS does not require the criterion ID — the minimal `[FAIL-FIRST RULE]` form is sufficient for A-31 alone.

### 3. Three-layer criterion-ID traceability chain complete (all variations confirm)

R13 closes the traceability chain at all three structural layers where criteria are enforced:
- **Integrity rule layer** (A-23): criterion IDs in A-16 and A-19 rule labels
- **Verification layer** (A-28): criterion IDs in trailing checklist item labels (C-01 through C-05)
- **Authoring-prompt layer** (A-29+A-30): criterion IDs in per-criterion COMMAND-register prompt labels

An author encounters the criterion ID at every enforcement point — when assigning FM identifiers, when citing them downstream, when completing each criterion's authoring prompt, and when verifying the output. No structural layer requires referencing an external legend.

### 4. Domain-prefix A-31 form achieves cross-criterion vocabulary coherence (V-05 distinguishes)

`DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` draws the domain prefix ("DEFAULT COMPETITOR") from the same axis vocabulary that A-26 requires in heading subtitles. The FAIL-FIRST body rule and the section headings speak the same vocabulary, making the template internally coherent at the domain level. This is a structural bonus not required by A-31 or A-26 independently, but achievable when the two criteria are designed together. V-05 is the only variation that achieves this cross-criterion coherence pattern between A-26 and A-31.

---

## Round Summary

| Metric | R12 | R13 |
|--------|-----|-----|
| Ceiling | 195 | 210 |
| Top score achieved | 195/195 | 210/210 |
| New criteria | A-26, A-27, A-28 | A-29, A-30, A-31 |
| All variations at ceiling | Yes (5/5) | Yes (5/5) |
| Key confirmation | A-26 vocabulary-agnostic; A-27 interrogative-form-agnostic; A-28 extends A-23 to checklist layer | A-29/A-30 wrapper-agnostic; A-31 minimal form sufficient; A-31+criterion-ID extends A-23 to FAIL-FIRST rule layer |

---

```json
{"top_score": 210, "all_essential_pass": true, "new_patterns": ["blockquote-wrapped bracket-label satisfies A-29 and A-30 -- markdown wrapper context is transparent to criterion-ID and COMMAND keyword presence in the bracket-label", "A-31 body rule carrying criterion ID simultaneously closes A-23 at the FAIL-FIRST rule layer -- completing every-named-rule-carries-criterion-ID coverage across A-16 source, A-19 citation, and A-31 FAIL-FIRST positions", "domain-prefix A-31 form achieves cross-criterion vocabulary coherence between A-26 heading subtitles and A-31 body rule when both draw from the same axis vocabulary"]}
```
