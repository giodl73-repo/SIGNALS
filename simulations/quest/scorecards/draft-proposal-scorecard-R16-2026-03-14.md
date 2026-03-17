# draft-proposal Scoring — Round 16 (Rubric v16)

**Formula**: `(E/4 × 60) + (R/3 × 30) + (A/34 × 10)`
**Tier anchors**: E = 4 Essential gates · R = 3 Risk gates · A = 34 compliance rows (C-01..C-41 minus C-21, C-22, C-24, C-25, C-26, C-27 which are structural sub-criteria — wait, let me apply the denominator as stated: /34, meaning 34 of the 41 C-tier rows carry scoring weight in the A-tier)

> **Denominator note**: v16 states A-denominator = /34. The 34 scoreable A-tier rows are C-01..C-41 minus the 7 gate-phase rows that are captured by E-tier and R-tier gates. The only differentiating rows across variations are C-38, C-39, C-40, C-41.

---

## Criterion Reference (v16 differentiating rows)

| ID | What it requires | Cascade |
|----|-----------------|---------|
| C-37 | T-37 TRIGGER is operationally specific (not a category label) | none |
| C-38 | T-37 CONDITION carries **Part 1**: inline exemplar of a failing T-37 CONDITION | C-38 FAIL → C-39 FAIL |
| C-39 | T-37 CONDITION additionally carries **Part 2**: correct-format prescription of a passing T-37 CONDITION | independent if C-38 PASS |
| C-40 | T-38 CONDITION carries **Part 1**: inline exemplar of a failing T-38 CONDITION (what abstract-only T-37 CONDITION looks like) | C-40 FAIL → C-41 FAIL |
| C-41 | T-38 CONDITION additionally carries **Part 2**: correct-format prescription of a passing T-38 CONDITION | independent if C-40 PASS |
| C-24 | Amendment table row count = 41 (one per C-01..C-41) | none |

---

## V-01 — Role Sequence (Architect-First) | Designed fail: C-39 only

### Criterion-by-Criterion

**E-tier** *(4/4)*

| Gate | Evidence | Result |
|------|----------|--------|
| E-01 | Role sequence header declared: `Architect → PM (Phase 9 exception: PM issues recommendation first)`. PHASE 0 present with [GATE: E-01]. | **PASS** |
| E-02 | PHASE 1 (Problem Statement) and PHASE 2 (Option Composition) both present with [GATE: E-02] citations. | **PASS** |
| E-03 | PHASE 4 (Comparison Matrix) present with [GATE: E-03]. Column headers use verbatim Phase 2 labels: Option-A / Option-B / do-nothing. | **PASS** |
| E-04 | PHASE 9 (Recommendation) present with [GATE: E-04]. PM names recommended option, cites ≥2 matrix dimensions, addresses inertia competitor, includes qualifying conditions. | **PASS** |

**R-tier** *(3/3)*

| Gate | Evidence | Result |
|------|----------|--------|
| R-01 | PHASE 3 risk register present with columns R-NN / RISK / P / I / P×I / MITIGATION. At least one do-nothing-only risk present. | **PASS** |
| R-02 | PHASE 6 prerequisites check enumerates option count, do-nothing, risk register count, Phase 4b R-NN citations, phase sequence. | **PASS** |
| R-03 | PHASE 10 finalization executes explicitly numbered four-step list with Finding entries for open triggers. | **PASS** |

**A-tier key rows** *(33/34)*

| ID | Evidence | Result |
|----|----------|--------|
| C-01..C-23 | All structural phases present in declared sequence; phase headers carry [GATE] citations; inertia competitor labeled and populated; option label register fixed (Option-A / Option-B / do-nothing); Phase 4b present with canonical R-NN bracket form; risk register ≥3 entries; Phase 9b risk propagation domain enumeration present; coverage table present. | **PASS** |
| C-24 | Amendment table initialized with T-01..T-41 (41 rows). Row count = 41. | **PASS** |
| C-25 | Amendment table columns: ID / TRIGGER / CONDITION / STATUS / PHASE. | **PASS** |
| C-26..C-36 | Gate audit, coverage table structure, qualification conditions, Architect feasibility confirmation, P×I formula confirmed at Domain 1 citation sites. | **PASS** |
| C-37 | T-37 TRIGGER is operationally specific — fires on a named structural property, not a category label. | **PASS** |
| C-38 | T-37 CONDITION carries **Part 1**: inline exemplar quoting a deficient T-37 CONDITION form ("abstract-only" example). | **PASS** |
| C-39 | T-37 CONDITION does **not** carry Part 2: the correct-format prescription (what a passing T-37 CONDITION looks like) is absent. C-38 PASS confirms this is an independent C-39 failure, not a cascade. | **FAIL** |
| C-40 | T-38 CONDITION carries **Part 1** (inline exemplar of abstract-only T-37 CONDITION form). | **PASS** |
| C-41 | T-38 CONDITION carries **Part 2** (correct-format prescription of passing T-37 CONDITION). | **PASS** |

### Scores

| Tier | Pass | Possible | Points |
|------|------|----------|--------|
| E | 4 | 4 | 60.00 |
| R | 3 | 3 | 30.00 |
| A | 33 | 34 | 9.71 |

**Composite: 99.71**

---

## V-02 — Inertia Framing (Maximum Prominence) | Designed fail: C-40 → C-41 cascade

### Criterion-by-Criterion

**E-tier** *(4/4)*

| Gate | Evidence | Result |
|------|----------|--------|
| E-01 | Role sequence declared. Inertia framing convention prominently stated. PHASE 0 present. | **PASS** |
| E-02 | PHASE 1 and PHASE 2 present. Inertia competitor framed with maximum explicitness. | **PASS** |
| E-03 | PHASE 4 present; inertia column receives dedicated prominence over active options (dominant column ordering). | **PASS** |
| E-04 | PHASE 9 present; recommendation explicitly states whether it beats the inertia competitor and on what quantified basis. | **PASS** |

**R-tier** *(3/3)*

| Gate | Evidence | Result |
|------|----------|--------|
| R-01 | Risk register present; inertia-specific risks given elevated P×I emphasis. | **PASS** |
| R-02 | Prerequisites check present. | **PASS** |
| R-03 | Finalization four-step list present. | **PASS** |

**A-tier key rows** *(32/34)*

| ID | Evidence | Result |
|----|----------|--------|
| C-01..C-36 | All structural criteria satisfied; inertia register formatting meets canonical R-NN bracket requirement; maximum inertia emphasis does not conflict with any criterion. | **PASS** |
| C-37 | T-37 TRIGGER operationally specific. | **PASS** |
| C-38 | T-37 CONDITION carries Part 1 (inline exemplar of failing form). | **PASS** |
| C-39 | T-37 CONDITION carries Part 2 (correct-format prescription). | **PASS** |
| C-40 | T-38 CONDITION is abstract-only — names condition category ("abstract CONDITION form") without quoting a deficient T-37 CONDITION instance. **Part 1 absent.** | **FAIL** |
| C-41 | C-40 FAIL cascades: abstract T-38 CONDITION contains neither Part 1 nor Part 2. | **FAIL** |

### Scores

| Tier | Pass | Possible | Points |
|------|------|----------|--------|
| E | 4 | 4 | 60.00 |
| R | 3 | 3 | 30.00 |
| A | 32 | 34 | 9.41 |

**Composite: 99.41**

---

## V-03 — Phrasing Register (Conversational) | Designed fail: none

### Criterion-by-Criterion

**E-tier** *(4/4)*

| Gate | Evidence | Result |
|------|----------|--------|
| E-01 | Role sequence declared. Phrasing uses "the PM should" / "the Architect should" rather than imperative "PM:" / "Architect:" directives — but the declared sequence and Phase 9 exception are unambiguous. | **PASS** |
| E-02 | PHASE 1 and PHASE 2 present; problem statement and option composition complete. | **PASS** |
| E-03 | PHASE 4 present; comparison matrix columns use verbatim Phase 2 labels. | **PASS** |
| E-04 | PHASE 9 present; recommendation with qualifying conditions. | **PASS** |

**R-tier** *(3/3)*

| Gate | Evidence | Result |
|------|----------|--------|
| R-01 | Risk register present; columns and row counts met. | **PASS** |
| R-02 | Prerequisites check present. | **PASS** |
| R-03 | Finalization four-step list present. | **PASS** |

**A-tier key rows** *(34/34)*

| ID | Evidence | Result |
|----|----------|--------|
| C-01..C-36 | All structural criteria satisfied. Conversational phrasing register does not affect any criterion: rubric criteria are structural and content-based, not syntactic. Phase gate citations still present. Inertia framing meets requirements. Risk propagation domains enumerated. | **PASS** |
| C-37 | T-37 TRIGGER operationally specific. | **PASS** |
| C-38 | T-37 CONDITION carries Part 1 inline failure exemplar. | **PASS** |
| C-39 | T-37 CONDITION carries Part 2 correct-format prescription. | **PASS** |
| C-40 | T-38 CONDITION carries Part 1 inline exemplar of abstract-only T-37 CONDITION form. | **PASS** |
| C-41 | T-38 CONDITION carries Part 2 correct-format prescription of passing T-37 CONDITION. | **PASS** |

### Scores

| Tier | Pass | Possible | Points |
|------|------|----------|--------|
| E | 4 | 4 | 60.00 |
| R | 3 | 3 | 30.00 |
| A | 34 | 34 | 10.00 |

**Composite: 100.00**

---

## V-04 — Role Sequence + Table-Heavy Option Anatomy | Designed fail: C-41 only

### Criterion-by-Criterion

**E-tier** *(4/4)*

| Gate | Evidence | Result |
|------|----------|--------|
| E-01 | Role sequence declared (Architect-first); Phase 9 PM-first exception confirmed. Table-heavy option anatomy does not affect PHASE 0 gate. | **PASS** |
| E-02 | PHASE 1 and PHASE 2 present; options rendered as structured tables (label / problem / risk / rationale rows) rather than prose blocks — still fully evaluable. | **PASS** |
| E-03 | PHASE 4 comparison matrix present; option labels verbatim from Phase 2 register. Table-heavy anatomy naturally aligns with matrix structure. | **PASS** |
| E-04 | PHASE 9 recommendation present; qualifying conditions present. | **PASS** |

**R-tier** *(3/3)*

| Gate | Evidence | Result |
|------|----------|--------|
| R-01 | Risk register present; table columns correct. | **PASS** |
| R-02 | Prerequisites check present. | **PASS** |
| R-03 | Finalization four-step list present. | **PASS** |

**A-tier key rows** *(33/34)*

| ID | Evidence | Result |
|----|----------|--------|
| C-01..C-36 | Structural criteria met. Table-heavy anatomy satisfies all content criteria — option labels, risk citations, R-NN back-fill, Phase 4b canonical bracket form all present in tabular format. | **PASS** |
| C-37 | T-37 TRIGGER operationally specific. | **PASS** |
| C-38 | T-37 CONDITION carries Part 1 inline failure exemplar. | **PASS** |
| C-39 | T-37 CONDITION carries Part 2 correct-format prescription. | **PASS** |
| C-40 | T-38 CONDITION carries **Part 1** (inline exemplar of abstract-only T-37 CONDITION form). C-40 PASS confirmed. | **PASS** |
| C-41 | T-38 CONDITION does **not** carry Part 2: the correct-format prescription of a passing T-38 CONDITION is absent. C-40 PASS does not guarantee C-41 PASS — Part 1 present, Part 2 independently omitted. | **FAIL** |

### Scores

| Tier | Pass | Possible | Points |
|------|------|----------|--------|
| E | 4 | 4 | 60.00 |
| R | 3 | 3 | 30.00 |
| A | 33 | 34 | 9.71 |

**Composite: 99.71**

---

## V-05 — Lifecycle Emphasis + Inertia Framing | Designed fail: C-38→C-39 + C-40→C-41 cascade

### Criterion-by-Criterion

**E-tier** *(4/4)*

| Gate | Evidence | Result |
|------|----------|--------|
| E-01 | Role sequence declared; Phase 4b elevated to dedicated lifecycle position with boundary markers. PHASE 0 structure intact. | **PASS** |
| E-02 | PHASE 1 and PHASE 2 present. | **PASS** |
| E-03 | PHASE 4 present; lifecycle emphasis adds Phase 4b prominence but does not displace matrix. | **PASS** |
| E-04 | PHASE 9 recommendation present with qualifying conditions and inertia beat statement. | **PASS** |

**R-tier** *(3/3)*

| Gate | Evidence | Result |
|------|----------|--------|
| R-01 | Risk register present; inertia risks elevated with maximum P×I explicitness. | **PASS** |
| R-02 | Prerequisites check present; Phase 4b boundary markers verified. | **PASS** |
| R-03 | Finalization four-step list present. | **PASS** |

**A-tier key rows** *(30/34)*

| ID | Evidence | Result |
|----|----------|--------|
| C-01..C-36 | Structural criteria met. Lifecycle explicitness and inertia framing satisfy Phase 4b requirements; R-NN canonical bracket form present; Phase 4b boundary markers do not conflict with any criterion. | **PASS** |
| C-37 | T-37 TRIGGER operationally specific. | **PASS** |
| C-38 | T-37 CONDITION is abstract-only — names the deficiency category ("T-37 CONDITION lacks operational specificity") without quoting an inline deficient example. **Part 1 absent.** | **FAIL** |
| C-39 | C-38 FAIL cascades: abstract T-37 CONDITION contains neither Part 1 nor Part 2. | **FAIL** |
| C-40 | T-38 CONDITION is abstract-only — names condition category without quoting a deficient T-37 CONDITION instance. **Part 1 absent.** | **FAIL** |
| C-41 | C-40 FAIL cascades: abstract T-38 CONDITION contains neither Part 1 nor Part 2. | **FAIL** |

### Scores

| Tier | Pass | Possible | Points |
|------|------|----------|--------|
| E | 4 | 4 | 60.00 |
| R | 3 | 3 | 30.00 |
| A | 30 | 34 | 8.82 |

**Composite: 98.82**

---

## Summary Table

| Rank | Variation | Designed Fails | E | R | A | Composite |
|------|-----------|---------------|---|---|---|-----------|
| 1 | V-03 (Register) | none | 4/4 | 3/3 | 34/34 | **100.00** |
| 2 | V-01 (Role Sequence) | C-39 | 4/4 | 3/3 | 33/34 | **99.71** |
| 2 | V-04 (Role Seq + Table) | C-41 | 4/4 | 3/3 | 33/34 | **99.71** |
| 4 | V-02 (Inertia Max) | C-40, C-41 | 4/4 | 3/3 | 32/34 | **99.41** |
| 5 | V-05 (Lifecycle+Inertia) | C-38, C-39, C-40, C-41 | 4/4 | 3/3 | 30/34 | **98.82** |

---

## Excellence Signals from V-03

**V-03** scores 100.00 by holding complete T-37 and T-38 CONDITION coverage while varying only phrasing register. The patterns that made it the top scorer:

**1. Structural satisfaction is register-invariant.** Conversational phrasing ("the PM should", "the Architect should") passes all criteria identically to imperative phrasing ("PM:", "Architect:"). Rubric criteria bind on structural presence and content completeness — not on syntactic register. Variation axes that do not touch amendment table CONDITION authoring are orthogonal to score.

**2. Two-part CONDITION completeness is the only A-tier differentiator at this rubric epoch.** Once all structural phases are present and all phase gates are cited, the only way to lose A-tier points in v16 is to leave either T-37 or T-38 CONDITION incomplete. V-03 demonstrates that holding both parts on both trigger rows achieves the ceiling regardless of every other axis.

**3. Independent C-41 failure is a real mode, not just a cascade artifact.** V-04 confirms: C-40 PASS (Part 1 present) does not protect C-41. An author who writes the inline exemplar but omits the correct-format prescription loses C-41 without triggering the cascade. The two-part requirement must be treated as two independent authoring obligations, not a single check.

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["Phrasing register (conversational vs imperative) is orthogonal to all rubric criteria — criterion satisfaction is structural and content-based, not syntactic", "C-40 PASS does not protect C-41: Part 1 present with Part 2 absent is a real independent failure mode, not solely a cascade artifact"]}
```
