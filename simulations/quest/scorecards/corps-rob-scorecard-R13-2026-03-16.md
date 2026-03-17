## Quest Score — corps-rob R13 (v13 Rubric)

---

### Scoring Model (v13)

| Weight | Count | Pts Each | Max |
|--------|-------|----------|-----|
| Essential (C-01–C-05) | 5 | 15 | 75 |
| Recommended (C-06–C-08) | 3 | 5 | 15 |
| Aspirational (C-09–C-42) | 34 | 5 | 170 |
| **Total** | | | **260** |

PARTIAL = half points. Composite ÷ 260 × 100 = percentage. Golden threshold: 80% (208/260).

---

### Variation Scores

---

#### V-01 — C-42 Criterion Enumeration

**Hypothesis recap:** Extends R12 V-01 glossary preamble with named-criterion enumeration for C-30 and C-34. All other elements identical.

**Essential Criteria (C-01–C-05):** All PASS. The template provides full stage labeling, role-loaded format, ROB document structure, 2+ findings per stage, and explicit Go/No-Go. 5 × 15 = **75 pts.**

**Recommended Criteria (C-06–C-08):** All PASS. Cross-stage coherence via CARRY FORWARD + BLOCKER PROTOCOL; risk register with >= 3 rows; Mission Cascade table in SPIRE. 3 × 5 = **15 pts.**

**Aspirational Criteria:**

| ID | Result | Evidence |
|----|--------|---------|
| C-09 | PASS | BLOCKER PROTOCOL declared; SYNTHESIS/Blockers subsection required |
| C-10 | PASS | CROSS-CUTTING THEMES section with 2+ stage citations required |
| C-11 | PASS | RULE CONDITIONAL-ITEM: numbered (1)/(2)/(3) items declared |
| C-12 | PASS | "severity must vary" instruction in finding table |
| C-13 | PASS | Status column (OPEN/WATCH/MITIGATED) in risk register |
| C-14 | PASS | Calibration Block with HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR |
| C-15 | PASS | Risk Register Update Protocol section with Trigger Events / Owner Role / Revisit Cadence |
| C-16 | PASS | ROLE LENS: field in Calibration Block, topic-specific requirement stated |
| C-17 | PASS | POST-STAGE AUDIT SUITE with three labeled enforcement sections |
| C-18 | PASS | Triage Note section required in every stage with all three named fields |
| C-19 | PASS | RULE ZERO-STATE: VIOLATIONS: NONE / GAPS: NONE / (a) NONE enumeration |
| C-20 | PASS | CALIBRATION AUDIT table with Stage / HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR / Honored / Deviation |
| C-21 | PASS | HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR as named fields in Triage Note |
| C-22 | PASS | ROLE CONCERN AUDIT section; RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION |
| C-23 | PASS | TRIAGE NOTE AUDIT section; RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION |
| C-24 | PASS | Three independent AUDIT SUITE sections (CALIBRATION / ROLE CONCERN / TRIAGE NOTE) |
| C-25 | PASS | TRIAGE NOTE AUDIT checks (a) absent section / (b) missing field / (c) placeholder per stage |
| C-26 | PASS | RULE AUDIT-SUITE with Anti-pattern-1 (merged) and Anti-pattern-2 (dimension repeated) |
| C-27 | PASS | RULE BOOKEND-AUDIT: "Absence is a FORMAT VIOLATION even on clean runs" |
| C-28 | PASS | TRIAGE NOTE AUDIT SCHEMA declared with labeled (a)/(b)/(c) conditions in preamble |
| C-29 | PASS | AUDIT RESULT block: (a) NONE / (b) NONE / (c) NONE per-condition enumeration |
| C-30 | PASS | Schema declared in preamble; post-stage TRIAGE NOTE AUDIT says "preamble declaration applies" |
| C-31 | PASS | Section headers carry [RULE AUDIT-SUITE, Section N] and [RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION] |
| C-32 | PASS | RULE CARRY-FORWARD: labeled block with CARRY: NONE zero-state; structurally before findings |
| C-33 | PASS | RULE SYNTHESIS: "SYNTHESIS is a cross-stage analytical artifact -- NOT an audit section" |
| C-34 | PASS | RULE CONDITIONAL-ITEM annotation: "[governs conditional verdicts -- distinct from RULE CONDITION-ENUM]" |
| C-35 | **FAIL** | RULE AUDIT-TABLE lacks additive constraint -- "Structural element: Named-column table (Stage / Pre-Commitment / Honored / Deviation)" with no "inserted ABOVE... NOT replacing it" declaration |
| C-36 | PASS | RULE SYNTHESIS enumerates 5 required subsections with VIOLATION-13 on absence |
| C-37 | PASS | IB-01 (Technical Displacement) and IB-02 (Organizational Adoption) are structurally distinct |
| C-38 | PASS | RULE CARRY-FORWARD: "Inertia ID column: tags each carried finding IB-01 / IB-02 / IB-01+IB-02 / N/A" |
| C-39 | **FAIL** | No RULE IB-URGENCY-CASCADE; no cascade constraint declared for Urgency Gradient = HIGH |
| C-40 | PASS | "This glossary is the exclusive locus for named format rule declarations... Named-rule requirements cannot be satisfied by inline rule declarations" |
| C-41 | **n/s** | Not scoreable: C-35 FAIL |
| C-42 | PASS | Exclusivity declaration enumerates "C-30 (Run-Level Preamble Schema with Named Post-Stage Reference)" and "C-34 (Conditional Item vs Condition Enum Disambiguation)" by label with functional descriptions |

**Aspirational: 31 PASS × 5 = 155 pts** (C-35 FAIL, C-39 FAIL, C-41 not scoreable = 3 out of 34)

**Composite: 75 + 15 + 155 = 245 / 260 (94.2%)**
**Golden: YES (exceeds 80% threshold; all essentials pass)**

---

#### V-02 — C-35 + C-41 Clean Reproduction

**Hypothesis recap:** Reproduces R12 V-02's RULE AUDIT-TABLE additive constraint and named anti-pattern in isolation. No glossary exclusivity declaration (C-40 intentionally absent).

**Essential (C-01–C-05):** All PASS. 5 × 15 = **75 pts.**
**Recommended (C-06–C-08):** All PASS. 3 × 5 = **15 pts.**

**Aspirational divergence from V-01:**

| ID | Result | Evidence |
|----|--------|---------|
| C-35 | PASS | RULE AUDIT-TABLE: "inserted ABOVE the AUDIT RESULT block -- NOT replacing it. Additive constraint: The table is a new layer... The AUDIT RESULT block with per-condition (a)/(b)/(c) enumeration is preserved BENEATH the table and is mandatory regardless of table presence." |
| C-39 | FAIL | No urgency cascade rule |
| C-40 | **FAIL** | Glossary preamble is generic: "All named format rules for this run are declared here before any stage output. Post-stage sections reference rules by glossary name rather than redeclaring conditions inline." No exclusivity self-declaration |
| C-41 | PASS | RULE AUDIT-TABLE: "Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29's per-condition enumeration" -- names failure mode and cites C-29; C-35 PASS satisfies dependency |
| C-42 | **n/s** | Not scoreable: C-40 FAIL |

All other aspirational criteria: same PASS as V-01.

**Aspirational: 31 PASS × 5 = 155 pts** (C-39 FAIL, C-40 FAIL, C-42 not scoreable = 3 out of 34)

**Composite: 75 + 15 + 155 = 245 / 260 (94.2%)**
**Golden: YES**

---

#### V-03 — Imperative-Register + GLOSSARY-GOVERNED CRITERIA Block

**Hypothesis recap:** Replaces inline criterion enumeration with a dedicated GLOSSARY-GOVERNED CRITERIA block using SHALL NOT / MUST language. C-40 present; C-42 via block structure. No RULE AUDIT-TABLE additive constraint (same as R12 V-01).

**Essential (C-01–C-05):** All PASS. 5 × 15 = **75 pts.**
**Recommended (C-06–C-08):** All PASS. 3 × 5 = **15 pts.**

**Aspirational divergence from V-01:**

| ID | Result | Evidence |
|----|--------|---------|
| C-35 | **FAIL** | RULE AUDIT-TABLE unchanged from V-01: "Anti-pattern: Table without per-condition AUDIT RESULT block beneath it" -- no "inserted ABOVE... NOT replacing it" additive-constraint language |
| C-39 | FAIL | No urgency cascade rule |
| C-40 | PASS | "This glossary is the exclusive locus for named format rule declarations in this run. Named-rule requirements SHALL NOT be satisfied by inline rule declarations..." -- stronger register but same criterion signal |
| C-41 | **n/s** | Not scoreable: C-35 FAIL |
| C-42 | PASS | GLOSSARY-GOVERNED CRITERIA block explicitly enumerates C-30 and C-34 with MUST / SHALL NOT constraints -- dedicated labeled block vs inline sentences |

**C-42 distinction from V-01:** V-01 uses inline prose sentences weaving C-30 and C-34 into the exclusivity declaration. V-03 lifts them into a separately labeled `GLOSSARY-GOVERNED CRITERIA` block with imperative-register entries. Both satisfy C-42's pass condition (at minimum, C-30 and C-34 named by label with functional description).

**V-01 vs V-03 C-42 comparison verdict:** Both PASS. Block structure does not produce a distinguishable advantage for rubric purposes -- criterion is satisfied by naming, not format of the naming. Both are equivalent signals for C-42.

**Aspirational: 31 PASS × 5 = 155 pts** (same failure pattern as V-01)

**Composite: 75 + 15 + 155 = 245 / 260 (94.2%)**
**Golden: YES**

---

#### V-04 — C-42 + C-35 + C-41 Combined

**Hypothesis recap:** Combines V-01's glossary preamble (C-40 + C-42) with V-02's RULE AUDIT-TABLE (C-35 + C-41). Structurally independent additions; no interaction effects predicted.

**Essential (C-01–C-05):** All PASS. 5 × 15 = **75 pts.**
**Recommended (C-06–C-08):** All PASS. 3 × 5 = **15 pts.**

**Aspirational:**

| ID | Result | Evidence |
|----|--------|---------|
| C-35 | PASS | From V-02: "inserted ABOVE the AUDIT RESULT block -- NOT replacing it" + full additive constraint declaration |
| C-39 | **FAIL** | No RULE IB-URGENCY-CASCADE; Urgency Gradient field absent from IB-02 |
| C-40 | PASS | From V-01: explicit exclusivity self-declaration with criterion enumeration |
| C-41 | PASS | From V-02: "Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29's per-condition enumeration"; C-35 dependency satisfied |
| C-42 | PASS | From V-01: C-30 and C-34 named by label in exclusivity declaration; C-40 dependency satisfied |

All other aspirational criteria: PASS (same base as V-01/V-02, both adding to each other without conflict).

**Interaction check:** C-34 is present in V-04's RULE CONDITIONAL-ITEM annotation (same as V-01). C-35 additive constraint is present (same as V-02). C-42 names C-34 as requiring glossary scope -- and C-34 is indeed declared in the glossary. No contradiction. Full structural coherence. ✓

**Aspirational: 33 PASS × 5 = 165 pts** (only C-39 FAIL = 1 out of 34)

**Composite: 75 + 15 + 165 = 255 / 260 (98.1%)**
**Golden: YES**

---

#### V-05 — Full Convergence + IB-URGENCY-CASCADE Named Rule

**Hypothesis recap:** V-04 base extended with RULE IB-URGENCY-CASCADE in the glossary, Urgency Gradient field on IB-02, and conditional SYNTHESIS subsection 5 branching.

**Essential (C-01–C-05):** All PASS. 5 × 15 = **75 pts.**
**Recommended (C-06–C-08):** All PASS. 3 × 5 = **15 pts.**

**Aspirational — key additions over V-04:**

| ID | Result | Evidence |
|----|--------|---------|
| C-39 | **PASS** | RULE IB-URGENCY-CASCADE declared in glossary with: Trigger (IB-02 Urgency Gradient = HIGH), Cascade constraint 1 (Go/No-Go MUST cite IB-02), Cascade constraint 2 (Risk Register MUST include delay-compounding entry attributed to IB-02), Cascade constraint 3 (Inertia Pressure Summary MUST name compounding path). Three named downstream sections with explicit citation requirements. C-37 dependency: IB-01 and IB-02 both present as structurally distinct baselines. ✓ |
| C-35 | PASS | Carried from V-04 |
| C-40 | PASS | Carried from V-04 |
| C-41 | PASS | Carried from V-04 |
| C-42 | PASS | Carried from V-04 |

**C-39 pass condition verification:** "The format specification includes an explicit declared cascade rule: when IB-02 Urgency Gradient = HIGH, at least two named downstream sections are explicitly required to cite or incorporate IB-02." V-05 names three (Go/No-Go, Risk Register, Inertia Pressure Summary) -- exceeds minimum. PASS. ✓

**IB-02 Urgency Gradient field:** Structurally present in RULE INERTIA-BASELINE as a new field element with vocabulary (LOW / MED / HIGH) and definition -- the trigger value is explicit, not implicit. This is what activates the cascade.

**SYNTHESIS subsection 5 update:** Conditional branch added: "if IB-02 Urgency Gradient = HIGH, name the compounding path per RULE IB-URGENCY-CASCADE." The subsection requirement is now condition-sensitive.

All other aspirational criteria: same PASS as V-04.

**Aspirational: 34 PASS × 5 = 170 pts** (zero failures)

**Composite: 75 + 15 + 170 = 260 / 260 (100%)**
**Golden: YES**

---

### Variation Ranking

| Rank | Variation | Score | Composite % | Key Differentiators |
|------|-----------|-------|-------------|---------------------|
| 1 | **V-05** | **260/260** | **100.0%** | C-39 (named cascade rule) + all V-04 criteria |
| 2 | **V-04** | **255/260** | **98.1%** | C-35 + C-41 + C-40 + C-42 combined; C-39 gap |
| 3 (tie) | **V-01** | **245/260** | **94.2%** | C-40 + C-42 inline enumeration; C-35/C-41 absent |
| 3 (tie) | **V-02** | **245/260** | **94.2%** | C-35 + C-41 clean; C-40/C-42 absent |
| 3 (tie) | **V-03** | **245/260** | **94.2%** | C-40 + C-42 block structure; C-35/C-41 absent |

V-01 and V-03 are equivalent scores with equivalent failure patterns. The block vs inline distinction for C-42 does not produce a scoring difference -- both satisfy the criterion at the same level.

---

### Excellence Signals from V-05

**Signal 1: Cascade rule trigger anti-pattern guards implicit activation**

V-05's RULE IB-URGENCY-CASCADE includes: *"Anti-pattern: Citing IB-02 in downstream sections without a declared Urgency Gradient value (gradient must be explicit before cascade applies; implicit urgency does not trigger)."*

The anti-pattern targets the trigger condition, not the cascade output. A rule that declares cascade constraints but does not guard its trigger leaves an adjacent-but-wrong implementation: a run that cites IB-02 in downstream sections without declaring the Urgency Gradient can appear to satisfy the cascade while the trigger was never activated. The anti-pattern closes that gap the same way C-41 closed the gap in RULE AUDIT-TABLE (additive constraint declared, table still used as replacement). Pattern: every cascade rule with a threshold trigger needs an anti-pattern naming the un-triggered citation as a failure mode.

**Signal 2: SYNTHESIS subsection conditional content branching**

V-05's RULE SYNTHESIS subsection 5 gains a conditional branch: *"if IB-02 Urgency Gradient = HIGH, name the compounding path per RULE IB-URGENCY-CASCADE."* This is the first SYNTHESIS subsection with condition-sensitive content requirements. Prior SYNTHESIS criteria (C-09, C-10, C-33, C-36) treat subsection requirements as unconditional. The conditional branch pattern means: the subsection must exist regardless (C-36), but its content requirements are gated by a field value declared elsewhere in the run. This extends the SYNTHESIS schema from a static checklist to a conditional artifact -- a different structural class.

---

### Score Summary Table

| | C-35 | C-39 | C-40 | C-41 | C-42 | Aspirational | Total |
|--|------|------|------|------|------|-------------|-------|
| **V-01** | FAIL | FAIL | PASS | n/s | PASS | 31/34 (155) | **245** |
| **V-02** | PASS | FAIL | FAIL | PASS | n/s | 31/34 (155) | **245** |
| **V-03** | FAIL | FAIL | PASS | n/s | PASS | 31/34 (155) | **245** |
| **V-04** | PASS | FAIL | PASS | PASS | PASS | 33/34 (165) | **255** |
| **V-05** | PASS | PASS | PASS | PASS | PASS | 34/34 (170) | **260** |

---

```json
{"top_score": 260, "all_essential_pass": true, "new_patterns": ["Cascade rule trigger anti-pattern: RULE IB-URGENCY-CASCADE names implicit-activation as failure mode -- citing downstream sections without declared Urgency Gradient field does not satisfy cascade, closing the un-triggered-citation gap analogous to C-41 for audit-table", "SYNTHESIS subsection conditional branching: subsection 5 gains condition-sensitive content requirement (if IB-02 Urgency Gradient = HIGH, name compounding path) -- first instance of a SYNTHESIS subsection whose content requirements are gated by a field value declared elsewhere in the run, extending SYNTHESIS schema from static to conditional"]}
```
