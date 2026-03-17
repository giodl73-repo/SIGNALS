## listen-support Round 2 — Scoring (v2 Rubric, 115 pts)

---

### Pre-Flight: C-01 Structural Finding

All five R2 variations drop the explicit `Title:` field from the ticket card template. V-01, V-02, V-04, V-05 show card formats of: Phase/Category/Persona/Volume/Severity/Body (V-01, V-04, V-05) or Category/Persona/Volume/Fallback Rationale/Severity/Body (V-02). "Ticket T-NN" is a ticket ID, not the human-readable subject line that C-01 requires. **V-03 alone restores "Title: [descriptive subject line]"** on the card, passing C-01 cleanly.

This is a design regression introduced by the v2 axis work: adding Phase/Fallback fields displaced Title rather than augmenting alongside it.

---

### Scoring Key

- **Essential (12 pts):** PASS = 12 / PARTIAL = 6 / FAIL = 0 — PARTIAL counts as essential failure for Golden gate
- **Recommended (10 pts):** PASS = 10 / PARTIAL = 5 / FAIL = 0
- **Aspirational (5 pts):** PASS = 5 / PARTIAL = 2 / FAIL = 0

---

## V-01 — Phase as First-Class Field

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PARTIAL | Card has Phase/Category/Persona/Volume/Severity/Body — no Title field; "Ticket T-NN" is ID only |
| C-02 | PASS | Controlled vocab for Phase (Phase 1/2/3), Category, Volume, Severity declared in table |
| C-03 | PASS | "Write as me — first person throughout. No role titles in body text. Just I." |
| C-04 | PASS | STEP 7: Doc Gaps + Design Gaps + Operational Gaps, each requiring >=1 named artifact |
| C-05 | PASS | TABLE CHECK: Total rows >= 7 enforced |
| C-06 | PASS | TABLE CHECK enforces Phase 1 >= 2, Phase 2 >= 1, Phase 3 >= 1; POST-BODY VERIFICATION checks phase match |
| C-07 | PASS | TABLE CHECK: Phase 1 Severity → P2/P3, Phase 3 Severity → P0/P1 |
| C-08 | PASS | TABLE CHECK: Distinct Persona values >= 3 |
| C-09 | PASS | "At least one body must name [PRIOR TOOL] by its exact name from Step 1" |
| C-10 | PASS | STEP 3 locks Phase + all metadata before bodies; bodies must match table |
| C-11 | PASS | Phase is a named card field ("Phase: [from table — Phase 1\|2\|3]"); STEP 6 checks "Phase field present on all cards" and phase distribution from field values |
| C-12 | PARTIAL | Phase-severity alignment enforced structurally (TABLE CHECK), but no per-card "I can still fall back to [PRIOR TOOL]" / "I can no longer use [PRIOR TOOL]" language; severity derived from phase rule, not from fallback availability statement |
| C-13 | PARTIAL | STEP 6 tabulates phase distribution + severity compliance, but **no role/persona diversity count with PASS/FAIL** — C-13 requires both |

**Essential:** 4.5/5 (C-01 PARTIAL) | **Recommended:** 3/3 | **Aspirational:** C-09 + C-10 + C-11 (PASS) + C-12 (PARTIAL) + C-13 (PARTIAL)

**Composite:** 6+12+12+12+12 + 10+10+10 + 5+5+5+2+2 = **103**
**all_essential_pass:** FALSE

---

## V-02 — Fallback-Grounded Severity Rationale

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PARTIAL | Card has Category/Persona/Volume/Fallback Rationale/Severity/Body — no Title, no Phase on card |
| C-02 | PASS | Controlled vocab enforced; Fallback Rationale is prose field, not vocab-constrained |
| C-03 | PASS | "Write as me — first person throughout. No role titles in body text." |
| C-04 | PASS | STEP 7: three sections required |
| C-05 | PASS | TABLE CHECK >= 7 rows |
| C-06 | PASS | Phase column in table; TABLE CHECK enforces distribution |
| C-07 | PASS | STEP 1B states inference rule explicitly; Fallback Rationale field mechanically derives severity; TABLE CHECK verifies |
| C-08 | PASS | TABLE CHECK >= 3 distinct Persona |
| C-09 | PASS | Fallback Rationale field uses "[PRIOR TOOL]" by exact name — prior tool appears on every card that has a fallback statement |
| C-10 | PASS | STEP 3 table before bodies |
| C-11 | FAIL | Phase in table only; no Phase: field on ticket card template |
| C-12 | PASS | Fallback Rationale: required field on every card; STEP 1B states the inference rule; model must write "I can still fall back to [PRIOR TOOL]" or "I can no longer use [PRIOR TOOL]" before severity value |
| C-13 | PARTIAL | STEP 6 checks Fallback Rationale consistency by phase + prior tool name count + first person; **no phase distribution count** (MATCH/MISMATCH only) and **no role diversity count** with PASS/FAIL |

**Essential:** 4.5/5 (C-01 PARTIAL) | **Recommended:** 3/3 | **Aspirational:** C-09 + C-10 + C-12 (PASS) + C-11 (FAIL) + C-13 (PARTIAL)

**Composite:** 6+12+12+12+12 + 10+10+10 + 5+5+0+5+2 = **101**
**all_essential_pass:** FALSE

---

## V-03 — Mid-Output Verification Block

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Card has Title/Category/Persona/Volume/Severity/Body — all 6 required fields present |
| C-02 | PASS | Controlled vocab in table; TABLE CHECK enforces |
| C-03 | PASS | "Write as me — first person throughout." |
| C-04 | PASS | STEP 6 (gap analysis) has three sections |
| C-05 | PASS | TABLE CHECK >= 7 |
| C-06 | PASS | TABLE CHECK + STEP 5B phase distribution with counts and PASS/FAIL |
| C-07 | PASS | Transition curve states severity floor/ceiling (Day 0-30 → P2/P3, Day 61-90 → P0/P1); TABLE CHECK verifies; STEP 5B phase-severity compliance scan |
| C-08 | PASS | TABLE CHECK + STEP 5B role diversity count with PASS/FAIL |
| C-09 | PASS | "At least one body must name [PRIOR TOOL]"; STEP 5B checks prior tool coverage |
| C-10 | PASS | STEP 3 table before bodies |
| C-11 | FAIL | Phase in table but **not on ticket card template** (Title replaces Phase position); STEP 5B "count from card bodies above" implies inference from body, not field read |
| C-12 | PARTIAL | STEP 1 transition curve implies fallback → P2/P3; no fallback → P0/P1, but this is phase-rule framing, not a per-card Fallback Rationale: field; severity-fallback connection is asserted structurally, not derived per-ticket |
| C-13 | PASS | STEP 5B: phase distribution counts per phase (PASS/FAIL), phase-severity compliance scan (PASS/FAIL), role diversity count (PASS/FAIL), prior tool coverage check; fires between STEP 5 (bodies) and STEP 6 (gap analysis); full tabulation per C-13 spec |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** C-09 + C-10 + C-13 (PASS) + C-11 (FAIL) + C-12 (PARTIAL)

**Composite:** 12+12+12+12+12 + 10+10+10 + 5+5+0+2+5 = **107**
**all_essential_pass:** TRUE — **GOLDEN**

---

## V-04 — Phase Field + Fallback Severity Combined

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PARTIAL | Card has Phase/Category/Persona/Volume/Fallback Rationale/Severity/Body — no Title field |
| C-02 | PASS | Controlled vocab; Fallback Rationale is prose |
| C-03 | PASS | "Write as me — first person throughout." |
| C-04 | PASS | STEP 7: three sections |
| C-05 | PASS | TABLE CHECK >= 7 |
| C-06 | PASS | Phase column in table; TABLE CHECK enforces Phase 1 >= 2, Phase 2 >= 1, Phase 3 >= 1 |
| C-07 | PASS | STEP 1B inference rule + TABLE CHECK + Fallback Rationale mechanical derivation creates double enforcement |
| C-08 | PASS | TABLE CHECK >= 3 distinct Persona |
| C-09 | PASS | "Fallback Rationale: field must use the exact product name declared in Step 1" |
| C-10 | PASS | STEP 3 table before bodies; Phase as required column |
| C-11 | PASS | Phase is a named card field; STEP 6 checks "Phase field present on all cards" and phase distribution from Phase fields (not body text) |
| C-12 | PASS | Fallback Rationale: required per card; STEP 1B inference rule copied; STEP 6 checks Phase 1/3 Fallback Rationale consistency |
| C-13 | PARTIAL | STEP 6 has phase distribution (MATCH/MISMATCH vs table), Fallback Rationale consistency by phase, prior tool name, first person, field values — **no standalone role/persona diversity count with PASS/FAIL** |

**Essential:** 4.5/5 (C-01 PARTIAL) | **Recommended:** 3/3 | **Aspirational:** C-09 + C-10 + C-11 + C-12 (PASS) + C-13 (PARTIAL)

**Composite:** 6+12+12+12+12 + 10+10+10 + 5+5+5+5+2 = **106**
**all_essential_pass:** FALSE

---

## V-05 — Full Synthesis (Phase + Fallback + Verification)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PARTIAL | Card has Phase/Category/Persona/Volume/Fallback Rationale/Severity/Body — no Title field (same gap as V-04) |
| C-02 | PASS | Controlled vocab enforced |
| C-03 | PASS | "Write as me — first person throughout." |
| C-04 | PASS | STEP 6 (gap analysis): three sections |
| C-05 | PASS | TABLE CHECK >= 7 |
| C-06 | PASS | TABLE CHECK + STEP 5B phase distribution from Phase field values |
| C-07 | PASS | STEP 1B inference rule + TABLE CHECK + STEP 5B severity-phase compliance from Phase+Severity field pairs |
| C-08 | PASS | TABLE CHECK + STEP 5B role diversity from Persona field values |
| C-09 | PASS | Fallback Rationale uses exact name; STEP 5B checks both Fallback Rationale fields AND body naming |
| C-10 | PASS | STEP 3 table before bodies; Phase required column |
| C-11 | PASS | Phase is a named card field; STEP 5B explicitly reads "from Phase field values" — not body inference; C-11 enables C-13 tabulation |
| C-12 | PASS | Fallback Rationale: required per card using exact prior tool name; STEP 1B inference rule; STEP 5B checks "Phase 1 Fallback Rationale fields state fallback available" and "Phase 3 Fallback Rationale fields state no fallback" |
| C-13 | PASS | STEP 5B: phase distribution (from Phase fields, counts + PASS/FAIL), severity-phase compliance (from Phase+Severity pairs), Fallback Rationale alignment (Phase 1/3 check), role diversity (from Persona fields, count + PASS/FAIL), prior tool in Fallback Rationale + body; fires between STEP 5 and STEP 6; all checks from field values |

**Essential:** 4.5/5 (C-01 PARTIAL) | **Recommended:** 3/3 | **Aspirational:** all 5 PASS

**Composite:** 6+12+12+12+12 + 10+10+10 + 5+5+5+5+5 = **109**
**all_essential_pass:** FALSE

---

## Rankings

| Rank | Variation | Composite | all_essential_pass | Golden |
|------|-----------|-----------|---------------------|--------|
| 1 | V-05 | 109 | NO (C-01 missing Title) | NO |
| 2 | V-03 | 107 | YES | **YES** |
| 3 | V-04 | 106 | NO | NO |
| 4 | V-01 | 103 | NO | NO |
| 5 | V-02 | 101 | NO | NO |

**Only V-03 achieves Golden.** V-05 has the highest composite but cannot reach Golden without fixing C-01.

---

## Excellence Signals

**From V-05 (highest composite, 109):**

1. **Verification block reads field values, not body text.** STEP 5B explicitly declares: "This block reads from field values declared above — not from body text." This is the structural mechanism that prevents Phase inference regression — when Phase is a declared field, the audit reads the field; when it's absent, the block would have to scan bodies. C-11 enables C-13 tabulation; C-12 enables C-13 compliance check.

2. **STEP 1B: inference rule as copy-this-rule.** Pre-stating the severity inference rule as a required verbatim copy + paraphrase ("State the rule in your own words") forces comprehension at the start of the prompt — not at severity-assignment time. The model arrives at each ticket having already internalized the rule, not pattern-matching to phase labels.

3. **Fallback Rationale alignment as a third verification axis.** STEP 5B adds a check category absent from V-01/V-02/V-03/V-04: "Phase 1 Fallback Rationale: fields state fallback available" and "Phase 3 Fallback Rationale: fields state no fallback." This closes the loop between C-11 (Phase field), C-12 (fallback language), and C-13 (verification), making the three v2 criteria mutually load-bearing rather than independent.

**From V-03 (Golden, all essential pass):**

4. **Preserving Title while adding Phase to the table.** V-03 is the only variation that retains the essential "Title: [descriptive subject line]" card field. The design lesson: when adding new structural fields (Phase), place them in the pre-commitment table and not as a replacement of existing card fields.

---

## Critical Design Gap (Round 3 Recommendation)

The synthesis prompt (V-05) needs one fix to become both the highest composite AND Golden: **add `Title: [descriptive subject line]` to the card template.** The card format should be: Title / Phase / Category / Persona / Volume / Fallback Rationale / Severity / Body. This gives 7 structured fields + body and satisfies both C-01 (Title) and C-11 (Phase as first-class field).

```json
{"top_score": 109, "all_essential_pass": false, "new_patterns": ["verification block declares its data source (field values not body text) — prevents inference regression when Phase/Severity are structural fields", "inference rule pre-stated as copy-this-rule at STEP 1B — model internalizes severity derivation before ticket generation, not at assignment time", "fallback rationale alignment as a third verification axis in STEP 5B — cross-audits Phase field against Fallback Rationale field, closing the C-11/C-12/C-13 loop"]}
```
