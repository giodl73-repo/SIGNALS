## scout-risk — Quest Score R1

---

### Scoring Summary

**Rubric version**: v1 | **Variations**: V-01 through V-05 | **Golden threshold**: all essential PASS + composite >= 80

---

### Criterion Definitions (quick reference)

| ID | Weight | Category |
|----|--------|----------|
| C-01 | Essential | Inertia risk listed first |
| C-02 | Essential | Multi-dimensional coverage (≥3 of 5) |
| C-03 | Essential | Risk anatomy complete (severity + likelihood + mitigation per entry) |
| C-04 | Essential | Severity uses only HIGH/MEDIUM/LOW |
| C-05 | Essential | Mitigations specific and actionable (fail if 2+ are generic) |
| C-06 | Recommended | Risks dimension-labeled (≥80%) |
| C-07 | Recommended | Likelihood qualified beyond binary |
| C-08 | Recommended | Risks ordered by priority |
| C-09 | Aspirational | Risk interdependencies noted |
| C-10 | Aspirational | AMEND behavior demonstrated |

---

### V-01 — Output Format (table-first)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | "STEP 1 — INERTIA RISK (always first, always its own row)" is explicit; row # starts at 0 for inertia before any other row. Structural enforcement is strong. |
| C-02 | **PASS** | "Cover at least 3 of the 5 non-inertia dimensions" is a stated rule in STEP 2. Compliance likely given table schema. |
| C-03 | **PASS** | Table columns force Severity, Likelihood, Mitigation on every row — cannot be omitted without breaking the table schema. |
| C-04 | **PASS** | Column header says "Severity" and rule states "HIGH / MEDIUM / LOW (no other values)" — structurally enforced. |
| C-05 | **PARTIAL** | Mitigation column label implies concreteness, and the rule says "not 'monitor closely'" — but there is only one negative example and no re-check gate. A model might produce one good mitigation and two hedges. Two generic mitigations would fail C-05. |
| C-06 | **PASS** | "Dimension" is a required column — every row gets a dimension label structurally. |
| C-07 | **PARTIAL** | Likelihood column rule says "a condition or scenario, not just 'possible' or 'unlikely'" — the prohibition is there but no enforcement mechanism or re-check. About half of rows expected to meet bar. |
| C-08 | **PASS** | "Order rows after inertia by severity descending (HIGH → MEDIUM → LOW)" is explicit. |
| C-09 | **FAIL** | No prompt for interdependencies. The table schema has no column or section for it. |
| C-10 | **PARTIAL** | STEP 3 covers AMEND with inertia-retention rule, but no base prompt to demonstrate it. Scored PARTIAL (instruction present, demonstration absent). |

**Essential**: C-01 PASS, C-02 PASS, C-03 PASS, C-04 PASS, C-05 PARTIAL → **4/5 essential pass**

> C-05 PARTIAL is a borderline case. The single "not 'monitor closely'" constraint with no re-check gate is insufficient to guarantee fewer than 2 generic mitigations in a long register. Scored PARTIAL, not PASS.

**Score calculation** (treating PARTIAL as 0.5 for sub-scoring):

- Essential: (4.5/5) × 60 = **54**
- Recommended: C-06 PASS, C-07 PARTIAL, C-08 PASS → (2.5/3) × 30 = **25**
- Aspirational: C-09 FAIL, C-10 PARTIAL → (0.5/2) × 10 = **2.5**

**Composite: ~81.5** | All essential pass: **NO** (C-05 PARTIAL blocks golden per rubric intent)

---

### V-02 — Inertia Framing (named section)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Entire `## 0. Inertia Risk — The Status Quo Competitor` section precedes the dimensional register. Structurally unavoidable. |
| C-02 | **PASS** | "Cover at least 3 of the 5" stated in STEP 1 of the dimensional register. |
| C-03 | **PASS** | Three-field anatomy (Severity / Likelihood / Mitigation) spelled out in the inertia section and again in the dimensional register template. |
| C-04 | **PASS** | "HIGH / MEDIUM / LOW" stated twice (inertia section + dimensional register). |
| C-05 | **PARTIAL** | One negative example ("not 'monitor closely'") but no re-check mechanism. Same gap as V-01. Model can produce two generic mitigations. |
| C-06 | **PASS** | `**[Dimension]: [Risk title]**` template enforces a label on every entry. |
| C-07 | **PARTIAL** | "not just 'possible'" stated — same instruction as V-01. No enforcement beyond the instruction. |
| C-08 | **PASS** | "Order: highest severity first within the dimensional register" is explicit. |
| C-09 | **PARTIAL** | `## 2. Risk Interdependencies (optional but valuable)` section exists with an example. Labeled "optional" — may be skipped. Scored PARTIAL. |
| C-10 | **PARTIAL** | AMEND section present with inertia-retention rule. Base prompt only — no demonstration. |

**Essential**: C-01 PASS, C-02 PASS, C-03 PASS, C-04 PASS, C-05 PARTIAL → **4/5 essential pass**

**Score**:

- Essential: (4.5/5) × 60 = **54**
- Recommended: C-06 PASS, C-07 PARTIAL, C-08 PASS → (2.5/3) × 30 = **25**
- Aspirational: C-09 PARTIAL, C-10 PARTIAL → (1/2) × 10 = **5**

**Composite: ~84** | All essential pass: **NO** (C-05 PARTIAL)

---

### V-03 — Phrasing Register (imperative/conversational)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | "**First: write the inertia risk.**" — bold, imperative, explicit prohibition: "Do not skip this. Do not move it. Do not bury it after technical risks." Strongest C-01 enforcement of all single-axis variations. |
| C-02 | **PASS** | "List at least one risk each from 3 or more of these dimensions" — explicit minimum. |
| C-03 | **PASS** | "Second" step lists all five fields per risk entry (Name / Dimension / Severity / Likelihood / Mitigation). Every field named and required. |
| C-04 | **PASS** | "Severity: HIGH, MEDIUM, or LOW — nothing else" stated twice (inertia + dimensional). |
| C-05 | **PASS** | **Third step is an explicit self-check**: "Read back every mitigation you wrote. If two or more say something like 'monitor closely', 'keep an eye on', 'revisit later', or 'consider alternatives' — replace them." This directly targets the C-05 fail condition and gives the model multiple negative examples. |
| C-06 | **PASS** | "Dimension: which of the five it belongs to" is a required field in the dimensional risk template. |
| C-07 | **PASS** | "what specific condition or scenario triggers this risk" for Likelihood — specific qualifier. Plus the imperative tone reduces drift. Likely > half of entries meet this bar. |
| C-08 | **PASS** | "Sort the dimensional risks from highest to lowest severity." |
| C-09 | **FAIL** | No interdependency prompt exists. Third step only checks mitigations. |
| C-10 | **PARTIAL** | Fourth step covers AMEND with inertia-retention. Base prompt only. |

**Essential**: C-01 PASS, C-02 PASS, C-03 PASS, C-04 PASS, C-05 **PASS** → **5/5 essential pass**

**Score**:

- Essential: (5/5) × 60 = **60**
- Recommended: C-06 PASS, C-07 PASS, C-08 PASS → (3/3) × 30 = **30**
- Aspirational: C-09 FAIL, C-10 PARTIAL → (0.5/2) × 10 = **2.5**

**Composite: ~92.5** | All essential pass: **YES** → **GOLDEN**

---

### V-04 — Role Sequence + Lifecycle

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Role A (The Skeptic) explicitly owns inertia as its first required output. PHASE 3 SYNTHESIS rule: "Inertia (from Role A) is always position #1." Dual enforcement. |
| C-02 | **PASS** | Role A (Market/Compliance), Role B (Technical/Dependency), Role C (Timeline) — three roles guarantee five dimensions attempted; cover ≥3 is structurally near-certain. |
| C-03 | **PASS** | Each role is instructed "(with severity/likelihood/mitigation)" — anatomy stated per role, then confirmed in PHASE 3 SYNTHESIS. |
| C-04 | **PASS** | "Severity scale: HIGH / MEDIUM / LOW only" in PHASE 3 SYNTHESIS. |
| C-05 | **PASS** | PHASE 3: "Mitigations must be specific actions — not 'monitor', not 'revisit'." Each role individually names actions as the expected output. Role-specific vocabulary (Skeptic/Realist/Scheduler) drives richer, role-appropriate mitigations. |
| C-06 | **PASS** | "Each entry carries: Dimension, Risk title, Severity, Likelihood, Mitigation" in PHASE 3 SYNTHESIS. |
| C-07 | **PASS** | Likelihood phrasing not explicitly pushed beyond binary in a single instruction, but role lenses (Realist, Scheduler) imply conditional framing. PHASE 3 doesn't repeat the "condition or scenario" constraint — scored PARTIAL. |
| C-08 | **PASS** | "all other entries sorted by severity descending (HIGH → MEDIUM → LOW)" in PHASE 3. |
| C-09 | **PASS** | "If Role B and Role C flagged the same Dependency risk independently, note the interdependency explicitly." Cross-role interdependency mechanism is unique to this variation. |
| C-10 | **PARTIAL** | PHASE 4 covers AMEND with inertia-retention. Base prompt only. |

**Essential**: C-01 PASS, C-02 PASS, C-03 PASS, C-04 PASS, C-05 PASS → **5/5 essential pass**

**Score**:

- Essential: (5/5) × 60 = **60**
- Recommended: C-06 PASS, C-07 PARTIAL, C-08 PASS → (2.5/3) × 30 = **25**
- Aspirational: C-09 PASS, C-10 PARTIAL → (1.5/2) × 10 = **7.5**

**Composite: ~92.5** | All essential pass: **YES** → **GOLDEN**

---

### V-05 — Full Integration

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | STEP 1 is named "INERTIA RISK (mandatory, always first)" with a dedicated format block. Self-check gate at STEP 4 explicitly verifies "Inertia is row 0 (before any Technical/Market/Compliance/Dependency/Timeline risk)". Double enforcement. |
| C-02 | **PASS** | "Cover at least 3 of the 5 dimensions" stated in STEP 2 and verified in STEP 4 checklist. |
| C-03 | **PASS** | Table schema (# / Dimension / Risk / Severity / Likelihood / Mitigation) enforces all fields. STEP 4 checklist item confirms. |
| C-04 | **PASS** | "only HIGH, MEDIUM, or LOW. No numbers, percentages, or invented labels" + STEP 4 checklist "Severity values are only HIGH, MEDIUM, or LOW". |
| C-05 | **PASS** | Explicit negative examples: "Not 'monitor closely', not 'keep an eye on', not 'be careful'. If you write a generic hedge, replace it." + STEP 4 checklist: "Fewer than 2 mitigations are generic non-actions". Strongest C-05 enforcement. |
| C-06 | **PASS** | Dimension column in table. Every row gets a label. |
| C-07 | **PASS** | "a specific condition or scenario. Not 'possible', not 'may occur'." in STEP 2 rules. Role lenses additionally drive conditional framing. |
| C-08 | **PASS** | "sorted by severity descending after inertia" in STEP 2, confirmed in STEP 4 checklist. |
| C-09 | **PASS** | STEP 3 "INTERDEPENDENCIES" is mandatory, not optional. "At least one interdependency is expected for most topics." Explicit format: "If [Risk A] materializes, [Risk B] escalates to [severity]." |
| C-10 | **PARTIAL** | STEP 5 handles AMEND with inertia-retention. Base prompt only. |

**Essential**: C-01 PASS, C-02 PASS, C-03 PASS, C-04 PASS, C-05 PASS → **5/5 essential pass**

**Score**:

- Essential: (5/5) × 60 = **60**
- Recommended: C-06 PASS, C-07 PASS, C-08 PASS → (3/3) × 30 = **30**
- Aspirational: C-09 PASS, C-10 PARTIAL → (1.5/2) × 10 = **7.5**

**Composite: ~97.5** | All essential pass: **YES** → **GOLDEN**

---

### Variation Scorecard

| ID | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Score | Golden |
|----|------|------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 | PASS | PASS | PASS | PASS | PARTIAL | PASS | PARTIAL | PASS | FAIL | PARTIAL | ~81.5 | NO |
| V-02 | PASS | PASS | PASS | PASS | PARTIAL | PASS | PARTIAL | PASS | PARTIAL | PARTIAL | ~84 | NO |
| V-03 | PASS | PASS | PASS | PASS | **PASS** | PASS | PASS | PASS | FAIL | PARTIAL | ~92.5 | YES |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PASS | **PASS** | PARTIAL | ~92.5 | YES |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** | PARTIAL | **~97.5** | YES |

---

### Rankings

1. **V-05** — 97.5 — Full integration; only C-10 is PARTIAL (AMEND cannot be demonstrated on a base prompt)
2. **V-03** — 92.5 — Imperative + self-check solves C-05; loses C-09 (no interdependency prompt)
3. **V-04** — 92.5 — Role sequence solves C-09 organically; C-07 slightly weaker (no "condition or scenario" restatement in synthesis)
4. **V-02** — 84 — Named inertia section is excellent for C-01 depth; C-05 and C-07 lack enforcement
5. **V-01** — 81.5 — Table schema is strong for C-03/C-06; no C-09, weak C-05

---

### Excellence Signals (from V-05)

**1. Self-check gate as a structural backstop.** The STEP 4 checklist reprints every essential criterion in imperative checkbox form. This is the single highest-leverage addition across all variations — it gives the model a final verification pass where it can catch and fix violations before committing the artifact. V-03 had a partial version of this (mitigation re-check only); V-05 generalizes it to all criteria.

**2. Negative examples with a replace instruction.** "Not 'monitor closely', not 'keep an eye on', not 'be careful'. If you write a generic hedge, replace it." Three named anti-patterns plus an explicit repair verb ("replace") is more actionable than a single "not 'monitor closely'" constraint.

**3. Mandatory interdependency section with expected output framing.** "At least one interdependency is expected for most topics" shifts the model from optional to obligatory. Pairing this with a concrete format ("If [Risk A] materializes, [Risk B] escalates to [severity]") removes ambiguity about what a valid response looks like.

**4. Role lenses as a coverage forcing function.** The Skeptic/Realist/Scheduler roles are more than flavor — each role is assigned exclusive dimensional ownership, guaranteeing that all five dimensions are attempted before synthesis. No single-axis variation achieves coverage this mechanically.

**5. Double enforcement on inertia.** STEP 1 names it mandatory; STEP 4 checklist verifies it was done. A model that drifts inertia to row 3 will catch the violation at STEP 4 before writing the artifact. Single-statement enforcement (V-01, V-02) relies on one instruction holding; double enforcement catches compliance failures.

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["self-check gate reprints all essential criteria as imperative checkboxes before artifact write", "replace instruction with multiple named anti-patterns forces model to repair rather than just avoid", "mandatory interdependency section with 'expected for most topics' framing shifts optional to obligatory", "role-owned dimensional coverage assigns each dimension to a named analyst to guarantee multi-dimensional reach"]}
```
