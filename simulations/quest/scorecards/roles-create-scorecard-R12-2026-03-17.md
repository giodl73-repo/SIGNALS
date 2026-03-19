## roles-create R12 — Scorecard

### Summary Table

| Variation | C-24 | C-25 | C-26 | C-27 | C-28 | Aspirational | Score | Rank |
|-----------|------|------|------|------|------|--------------|-------|------|
| V-05 | PASS | PASS | PASS | PASS | PASS | 21/21 | **100** | 1 |
| V-01 | PASS | FAIL | PASS | FAIL | PASS | 19/21 | **99.05** | 2= |
| V-02 | PASS | FAIL | PASS | PASS | FAIL | 19/21 | **99.05** | 2= |
| V-03 | PASS | FAIL | PASS | FAIL | FAIL | 18/21 | **98.57** | 4= |
| V-04 | PASS | FAIL | FAIL | PASS | FAIL | 18/21 | **98.57** | 4= |

All essential (5/5) and recommended (2/2) pass for all variations.

### Key Discrimination Answers

**Q1 (V-01):** C-27 fires on process-narrative openers while C-19/C-23 pass — **CONFIRMED.** C-27 is positional (citation must be first); C-19 is content-based (no rule restatement). "INPUT GUARD -- this phase runs before any routing decision." fails C-27 (wrong position) while passing C-19 (no rule content). Exactly 2 deductions: C-25 + C-27.

**Q2 (V-02):** C-28 fires when retry text follows the artifact even though citation is first — **CONFIRMED.** "If any gate fails, correct... and re-run the failed gate before advancing" in the body fails C-28 regardless of where it sits relative to the citation. Gate FAIL conditions are the canonical location. Exactly 2 deductions: C-25 + C-28.

**Q3 (V-03):** C-27 + C-28 produces exactly 3 deductions — **CONFIRMED.** C-25 + C-27 + C-28, no cascade. Both violations are process narrative, not rule restatement — C-19/C-23 unaffected.

**Q4 (V-04):** C-26 and C-28 are orthogonal — **CONFIRMED.** Exactly 3 deductions: C-25 + C-26 + C-28. CONTRACT ordering and phase body surface area are fully independent failure axes, extending the R11 C-24/C-26 orthogonality result to a third pair.

### Excellence Signals from V-05

1. **Position rule vs. content rule:** C-27 and C-19 govern orthogonal properties of the same text — position and content respectively. A connector opener fails C-27 (not first) while passing C-19 (not a rule restatement). Minimum-surface bodies satisfy both simultaneously.

2. **Correction logic is a structural invariant:** V-05 achieves C-28 compliance by carrying nothing in the body beyond citation + artifact — no FAIL branches even in gate annotations, no correction prose anywhere. Phase 5 and the AUDIT-CHECKLIST pre-declaration handle the correction path implicitly.

3. **Structural axes are independently addressable:** Gate form (C-24), CONTRACT ordering (C-26), phase body entry point (C-27), and correction placement (C-28) are each independently fixable — confirmed across R11 and R12.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-27 is a positional criterion independent of C-19: a connector opener before the CONTRACT citation fails C-27 (wrong position) while passing C-19 (no rule restatement) -- the two criteria govern orthogonal properties of the same text, enabling precise decomposition of phase body violations into content-type (C-19/C-23) vs entry-point (C-27)", "C-26 and C-28 are orthogonal independent failure axes -- CONTRACT definition ordering and phase body surface area can each be violated without affecting the other, combining to exactly 3 deductions (C-25 + C-26 + C-28) with no cascade, extending the R11 C-24/C-26 orthogonality result to a third independent pair"]}
```
) |
| C-11 | PASS | Companion file generated from INERTIA-ADVOCATE-TEMPLATE |
| C-12 | PASS | Interactive hold gates all three answers (INTERACTIVE-HOLD) |
| C-13 | PASS | Phase 5 pre-write confirmation executes against all checklist items |
| C-14 | PASS | Malformed input guard in Phase 0 (INPUT-ROUTING-RULES) |
| C-15 | PASS | In-phase gates at each phase with [ID] back-references |
| C-16 | PASS | AUDIT-CHECKLIST pre-declared in CONTRACTS section before phases |
| C-17 | PASS | All six CONTRACT blocks named and defined |
| C-18 | PASS | Forward (Gated At column) and backward ([ID] citations) both present |
| C-19 | PASS | Connector openers are process narrative -- they do not reproduce or paraphrase CONTRACT rule content; no rule restatement in phase steps |
| C-20 | PASS | AUDIT-CHECKLIST items thin: name block + scope only |
| C-21 | PASS | All cited CONTRACT blocks have AUDIT-CHECKLIST coverage |
| C-22 | PASS | AUDIT-CHECKLIST header declares "no rule enumeration" format constraint |
| C-23 | PASS | Connector openers are process narrative; no rule content appears outside the three canonical locations |
| C-24 | PASS | All gates inline throughout Phases 0-4; no TABLE gates present |
| **C-25** | **FAIL** | Connector openers ("INPUT GUARD -- this phase runs before any routing decision.") precede the CONTRACT citation in every phase body, exceeding the minimum citation + artifact surface |
| C-26 | PASS | CONTRACTS order: INPUT-ROUTING-RULES -> INTERACTIVE-HOLD -> FIELD-REGISTER -> COLUMN-HEADER; unconditional main-flow pair FIELD-REGISTER (Phase 3) < COLUMN-HEADER (Phase 4) in correct sequence |
| **C-27** | **FAIL** | Each content-producing phase body opens with a connector phrase before the CONTRACT citation -- "FRONTMATTER GENERATION -- all 12 frontmatter fields are generated here." precedes "CONTRACT: FIELD-REGISTER applied." Position violation, not content violation (C-19/C-23 unaffected) |
| C-28 | PASS | Correction instructions appear only in gate FAIL branches ("FAIL: Add missing fields before advancing."), not in phase body prose |

**Cascade check:** C-27 fires -> C-25 implied (already deducted, no additional cascade). C-25 does not imply C-19 -- connector openers are process narrative, not rule restatement (confirmed R11). C-23 passes for the same reason.

**Aspirational passed:** 19 / 21
**Score:** 60 + 30 + (19 x 10/21) = 60 + 30 + 9.048 = **99.05**

---

### V-02: C-28 in Isolation

**Structure:** Each phase body opens correctly with the CONTRACT citation (no connector openers). After the artifact reference, the body appends fix-and-retry instructions ("If Gate 0 fails, apply the correction action from the classification table and return to gate evaluation before continuing.", "If any gate fails, correct the specific field using the FIELD-REGISTER register table and re-run the failed gate before advancing to Phase 4."). Gate annotations carry no explicit FAIL branches -- correction logic lives in body prose, not the gate. CONTRACT order is canonical.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | File written to `.craft/roles/{area}/{subrole}.md` |
| C-02 | PASS | All 12 frontmatter fields present |
| C-03 | PASS | Phase 0 -> Phase 1 routing intact |
| C-04 | PASS | Domain-specific field values via FIELD-REGISTER |
| C-05 | PASS | Inertia companion surfaced / generated in Phase 2 |
| C-06 | PASS | Lens.verify items are boolean checks >= 4 |
| C-07 | PASS | Domain specializations table in body |
| C-08 | PASS | Archetype checked against area pattern |
| C-09 | PASS | frame first-person; serves names beneficiary |
| C-10 | PASS | Domain-named column headers |
| C-11 | PASS | Companion file generated from template |
| C-12 | PASS | Interactive hold gates all three answers |
| C-13 | PASS | Phase 5 pre-write confirmation present |
| C-14 | PASS | Malformed input guard in Phase 0 |
| C-15 | PASS | In-phase gates at each phase with [ID] back-references |
| C-16 | PASS | AUDIT-CHECKLIST pre-declared before phases |
| C-17 | PASS | All six CONTRACT blocks defined |
| C-18 | PASS | Bidirectional traceability present |
| C-19 | PASS | Retry text in body prose is operational instruction, not CONTRACT rule restatement |
| C-20 | PASS | AUDIT-CHECKLIST items are thin CONTRACT references |
| C-21 | PASS | All cited CONTRACT blocks covered in checklist |
| C-22 | PASS | Checklist format constraint declared in header |
| C-23 | PASS | Retry text is process instruction, not rule content from a CONTRACT block; three-location quarantine not violated |
| C-24 | PASS | All gates inline throughout; homogeneous form |
| **C-25** | **FAIL** | Each phase body appends "If any gate fails... re-run the failed gate before advancing" after the artifact reference, exceeding the minimum citation + artifact surface |
| C-26 | PASS | FIELD-REGISTER defined before COLUMN-HEADER in CONTRACTS; canonical unconditional main-flow pair order |
| C-27 | PASS | Phase bodies open directly with "CONTRACT: X applied." -- no connector opener precedes the citation |
| **C-28** | **FAIL** | Fix-and-retry instructions appear in phase body prose after the artifact reference ("If any gate fails, correct the specific field... and re-run the failed gate before advancing to Phase 4."), not in gate FAIL conditions; gate annotations carry only "PASS / FAIL" with no FAIL branch |

**Cascade check:** C-28 fires -> C-25 implied (already deducted, no additional cascade). Retry text is process instruction -- does not restate CONTRACT rule content -- so C-19 and C-23 pass. C-27 passes because body entry point is correct.

**Aspirational passed:** 19 / 21
**Score:** 60 + 30 + (19 x 10/21) = 60 + 30 + 9.048 = **99.05**

---

### V-03: C-27 + C-28 Combined

**Structure:** Both violations simultaneously. Connector openers appear before CONTRACT citations in all phase bodies (C-27 pattern from V-01), AND fix-and-retry instructions appear in body prose after the artifact reference (C-28 pattern from V-02). Gate annotations carry no explicit FAIL branches. CONTRACT order is canonical. Inline gates throughout (C-24 passes).

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | Same as V-01 and V-02 |
| C-08–C-23 | PASS | Structural skeleton identical; thin checklist; CONTRACT blocks present; connector openers and retry text are process narrative, not rule restatement (C-19, C-23 unaffected) |
| C-24 | PASS | All gates inline throughout Phases 0-4; homogeneous form |
| **C-25** | **FAIL** | Both connector openers before citation AND retry text after artifact; phase body surface area exceeds citation + artifact minimum |
| C-26 | PASS | FIELD-REGISTER before COLUMN-HEADER in CONTRACTS; canonical order |
| **C-27** | **FAIL** | Connector openers ("FRONTMATTER GENERATION -- all 12 frontmatter fields are generated here.") precede CONTRACT citations in all content-producing phases |
| **C-28** | **FAIL** | Fix-and-retry instructions ("If any gate fails, correct the specific field... and re-run the failed gate before advancing to Phase 4.") appear in phase body prose; gate annotations carry no FAIL branches |

**Cascade check:** C-27 + C-28 both fire -> C-25 implied once (one deduction regardless of how many sub-types fire). C-25 does not cascade to C-19 -- process narrative openers and retry text are not rule restatements. C-19, C-23 unaffected. C-26 passes. Exactly 3 deductions: C-25, C-27, C-28.

**Orthogonality confirmed:** V-01 shows C-27 can fire without C-28; V-02 shows C-28 can fire without C-27; V-03 shows both fire together with exactly 3 deductions -- the violations do not interact or compound.

**Aspirational passed:** 18 / 21
**Score:** 60 + 30 + (18 x 10/21) = 60 + 30 + 8.571 = **98.57**

---

### V-04: C-26 + C-28 Combination

**Structure:** COLUMN-HEADER is defined third in the CONTRACTS block, before FIELD-REGISTER which is defined fourth -- inverting the unconditional main-flow pair (Phase 3 cites FIELD-REGISTER first, Phase 4 cites COLUMN-HEADER second, so FIELD-REGISTER must be defined first). Phase bodies open correctly with CONTRACT citations (no connector openers, C-27 passes). Fix-and-retry instructions appear in body prose after the artifact reference (C-28 pattern). Inline gates throughout (C-24 passes).

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | Same as other variations |
| C-08–C-23 | PASS | Named CONTRACT blocks present; thin phases and checklist; bidirectional traceability; no rule restatement in body prose or checklist items |
| C-24 | PASS | All gates inline throughout; homogeneous form |
| **C-25** | **FAIL** | Retry text ("If any gate fails, correct the specific field... and re-run the failed gate before advancing to Phase 4.") in body prose exceeds minimum citation + artifact surface |
| **C-26** | **FAIL** | CONTRACTS block order: INPUT-ROUTING-RULES -> INTERACTIVE-HOLD -> COLUMN-HEADER -> FIELD-REGISTER -- COLUMN-HEADER (Phase 4, second cited in main flow) defined before FIELD-REGISTER (Phase 3, first cited in main flow); inverts first-citation sequence for the unconditional main-flow pair |
| C-27 | PASS | Phase bodies open directly with CONTRACT citations -- "CONTRACT: FIELD-REGISTER applied." is first substantive text in Phase 3; no connector openers |
| **C-28** | **FAIL** | Fix-and-retry instructions in body prose ("If any gate fails, correct the specific field using the FIELD-REGISTER register table and re-run the failed gate before advancing to Phase 4."); gate annotations carry no FAIL branches |

**Cascade check:** C-26 fires -- does not cascade to C-17 (CONTRACT blocks are defined, just out of order; C-17 requires presence, not ordering). C-28 fires -> C-25 implied. Retry text is not rule restatement -> C-19, C-23 unaffected. C-27 passes. Exactly 3 deductions: C-25, C-26, C-28.

**C-26/C-28 orthogonality confirmed:** CONTRACT definition ordering and phase body surface area are independent failure modes. Combining them produces exactly 3 deductions with no interaction, mirroring the C-24/C-26 orthogonality confirmed in R11.

**Aspirational passed:** 18 / 21
**Score:** 60 + 30 + (18 x 10/21) = 60 + 30 + 8.571 = **98.57**

---

### V-05: Full Ceiling (Canonical Form)

**Structure:** R11 V-05 reproduced verbatim. Homogeneous inline gates throughout. Minimum-surface phase bodies: CONTRACT citation + artifact/action reference only. No connector openers before citations (C-27 passes). No retry text in body prose (C-28 passes). CONTRACTS block in first-citation order with unconditional main-flow pair FIELD-REGISTER < COLUMN-HEADER (C-26 passes). No preamble (C-23 passes).

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | All essential and recommended satisfied |
| C-08–C-22 | PASS | Named CONTRACTs; bidirectional traceability; thin phases and checklist; all cited blocks covered; self-documenting header |
| C-23 | PASS | No preamble; rule content confined to CONTRACTS block definitions, phase citations, and checklist items only |
| C-24 | PASS | All phases use inline `-> **Gate N [ID]:**` -- no TABLE gates |
| C-25 | PASS | Every phase body: one CONTRACT citation + one artifact/action reference; no bridging prose, no connector opener, no retry text |
| C-26 | PASS | CONTRACTS order: INPUT-ROUTING-RULES -> INTERACTIVE-HOLD -> FIELD-REGISTER -> COLUMN-HEADER; unconditional main-flow pair in Phase 3 < Phase 4 citation order; conditional contracts and AUDIT-CHECKLIST placed after |
| C-27 | PASS | Phase 0: "CONTRACT: INPUT-ROUTING-RULES applied." is first text; Phase 3: "CONTRACT: FIELD-REGISTER applied." is first text; Phase 4: "CONTRACT: COLUMN-HEADER applied." is first text; no connector opener precedes any citation |
| C-28 | PASS | Phase bodies carry no retry instructions; gate annotations read "PASS / FAIL" with no FAIL branches; no correction prose anywhere in body |

**Aspirational passed:** 21 / 21
**Score:** 60 + 30 + 10 = **100**

---

### Summary Table

| Variation | C-24 | C-25 | C-26 | C-27 | C-28 | Essential | Recommended | Aspirational | Score | Rank |
|-----------|------|------|------|------|------|-----------|-------------|--------------|-------|------|
| V-05 | PASS | PASS | PASS | PASS | PASS | 5/5 | 2/2 | 21/21 | **100** | 1 |
| V-01 | PASS | FAIL | PASS | FAIL | PASS | 5/5 | 2/2 | 19/21 | **99.05** | 2= |
| V-02 | PASS | FAIL | PASS | PASS | FAIL | 5/5 | 2/2 | 19/21 | **99.05** | 2= |
| V-03 | PASS | FAIL | PASS | FAIL | FAIL | 5/5 | 2/2 | 18/21 | **98.57** | 4= |
| V-04 | PASS | FAIL | FAIL | PASS | FAIL | 5/5 | 2/2 | 18/21 | **98.57** | 4= |

---

### Key Discrimination Answers

**Q1 -- V-01: Does C-27 fire on process-narrative openers while C-19/C-23 pass?**
YES. C-27 is a positional criterion: the phase body must open with the CONTRACT citation. "INPUT GUARD -- this phase runs before any routing decision." is process description -- it contains no rule content from the CONTRACT block -- so C-19 (no rule restatement) and C-23 (rule quarantine) are unaffected. C-27 fires purely because the citation is not first. The distinction between C-27 and C-19 is position vs. content.

**Q2 -- V-02: Does C-28 fire when the CONTRACT citation is correctly first but retry text follows the artifact?**
YES. C-28 fires on the presence of fix-and-retry text in the phase body regardless of placement relative to the citation. "If any gate fails, correct the specific field... and re-run the failed gate before advancing to Phase 4." is in the body, not in the gate's FAIL condition -- C-28 fires. The gate is the canonical location for correction logic; the body is canonical for citation + artifact only.

**Q3 -- V-03: Does C-27 + C-28 produce exactly 3 deductions with no cascade?**
YES. C-25 + C-27 + C-28 = 3 deductions. No cascade: connector openers (C-27 violation) and retry text (C-28 violation) are both process narrative, not rule restatement -- C-19 and C-23 are unaffected. C-26 passes (canonical CONTRACT order). C-24 passes (homogeneous inline gates). The violations are orthogonal and independent.

**Q4 -- V-04: Are C-26 and C-28 orthogonal, combining to exactly 3 deductions?**
YES. C-25 + C-26 + C-28 = 3 deductions. C-26 (inverted CONTRACT ordering) does not interact with C-28 (retry text in body). C-26 does not cascade to C-17 (CONTRACT blocks are still defined; C-17 requires presence, not ordering). C-28 implies C-25 but does not cascade to C-19 or C-23. C-27 passes (bodies open with citations). The combination follows the same orthogonality pattern as C-24/C-26 confirmed in R11.

---

### Excellence Signals -- V-05

**Signal 1 -- Position rule is independent of content rule:** C-27 and C-19 govern different properties of the same text. C-19 asks "does this text restate CONTRACT rules?" -- C-27 asks "is this text before the CONTRACT citation?" A process-description opener ("FRONTMATTER GENERATION -- ...") fails C-27 (wrong position) while passing C-19 (no rule content). A minimum-surface body passes both. This distinction enables precise diagnosis: a phase body can violate position without violating content, or violate content without violating position.

**Signal 2 -- Correction logic placement is a structural invariant:** C-28 is structural, not semantic. "If any gate fails, correct... and re-run" in the body always fails C-28, regardless of how useful the guidance is. The canonical form (V-05) achieves C-28 compliance by putting nothing in the body beyond citation + artifact -- no FAIL branches in gate annotations, no correction prose anywhere. The gate's "PASS / FAIL" annotation is sufficient structure; the AUDIT-CHECKLIST pre-declaration and Phase 5 confirmation handle the correction path implicitly.

**Signal 3 -- C-26/C-28 orthogonality extends the R11 independence result:** R11 confirmed C-24 and C-26 are orthogonal (gate structural form and CONTRACT ordering are independent). R12 V-04 confirms C-26 and C-28 are also orthogonal (CONTRACT ordering and phase body surface area are independent). The structural axes -- gate form (C-24), CONTRACT ordering (C-26), phase body entry point (C-27), correction placement (C-28) -- are each independently addressable.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-27 is a positional criterion independent of C-19: a connector opener before the CONTRACT citation fails C-27 (wrong position) while passing C-19 (no rule restatement) -- the two criteria govern orthogonal properties of the same text, enabling precise decomposition of phase body violations into content-type (C-19/C-23) vs entry-point (C-27)", "C-26 and C-28 are orthogonal independent failure axes -- CONTRACT definition ordering and phase body surface area can each be violated without affecting the other, combining to exactly 3 deductions (C-25 + C-26 + C-28) with no cascade, extending the R11 C-24/C-26 orthogonality result to a third independent pair"]}
```
