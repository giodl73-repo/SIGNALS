## crew-review Variate R5 — Scorecard

**Rubric**: crew-review-rubric-v5-2026-03-16.md | **Max**: 145 | **Golden threshold**: 80 (all essential passing)

---

### Scoring Reference

| Tier | Count | Per criterion | Max |
|------|-------|--------------|-----|
| Essential | 5 | 12 | 60 |
| Recommended | 6 | 10 | 60 |
| Aspirational | 10 | 2.5 | 25 |
| **Total** | | | **145** |

PARTIAL = half points. All five essential criteria must pass for golden to be possible.

---

## V-01 — Inertia framing (C-20 + C-21 co-located)

**Design repair**: Keeps R4 V-01's OPEN/CLOSED state machine gate (C-20) and adds the C-21 prohibited-form statement directly inside the escalation rule text at step 3.

### Essential

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | **PASS** | Step 1 reads every file in `.craft/roles/`; "Zero roles may be fabricated." |
| C-02 | **PASS** | Output section declares 4-column table: Role, Findings, Severity, Recommendation. |
| C-03 | **PASS** | Severity enum: "exactly HIGH, MEDIUM, or LOW — no other labels." Challenger severities are semantically grounded. |
| C-04 | **PASS** | Challengers apply null hypothesis frame; domain roles apply "only that role's `lens.verify` perspective." |
| C-05 | **PASS** | "one concrete action naming what to do and where in the artifact" — generic directives are excluded by instruction. |

**Essential: 60/60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | **PASS** | Standard: 2–3 roles (excluding challengers); `--depth deep`: every non-challenger role. |
| C-07 | **PASS** | Cross-role synthesis required (2–3 sentences), names at least one convergence or conflict; slot-gap rows count. |
| C-08 | **PASS** | AMEND block with 4 specific options including `--amend rerun:challengers`. |
| C-09 | **PASS** | CHALLENGER PHASE appears before DOMAIN PHASE; runs all `archetype: challenger` roles first with null hypothesis form. |
| C-10 | **PASS** | Domain finding instruction: "Name a specific artifact surface in each finding (section title, field name, diagram element, named assumption)." |
| C-14 | **PASS** | Step 1 ERROR halts: absent directory, empty directory, missing `lens.verify`/`expertise.relevance` — all unconditional, no soft fallback. |

**Recommended: 60/60**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-11 | **PASS** | 4-slot form (SLOT-A through D) with named fill-in blanks. |
| C-12 | **FAIL** | No Lens column; no per-role lens-lock declaration before findings. Domain phase says "apply only that role's `lens.verify`" but no declared sentence in output. |
| C-13 | **FAIL** | 4-column plain matrix; no typed column contracts with visible enforcement. |
| C-15 | **PASS** | "CHALLENGER PHASE" and "DOMAIN PHASE" are named as discrete sections with clear boundary. |
| C-16 | **PASS** | Slot-to-row escalation rule mandates a dedicated HIGH-severity matrix row for each unfilled slot. |
| C-17 | **PASS** | G1 gate: OPEN state declared; 5-condition closure predicate; "Domain review does not begin until G1 transitions to CLOSED." |
| C-18 | **PASS** | Step 2: "Produce a **separate, dedicated matrix row**." Step 3: "This row is a full matrix row. It is NOT a sentence embedded within the challenger row's Findings cell. It is NOT a note or comment appended below the challenger row. It is NOT a parenthetical or footnote." |
| C-19 | **FAIL** | No typed column definitions; no anti-pattern exclusion inside any column constraint. |
| C-20 | **PASS** | G1 named states OPEN/CLOSED; 5-condition closure predicate requiring all conditions simultaneously true. |
| C-21 | **PASS** | Step 3 of escalation rule states prohibited forms inside the rule itself: "NOT a sentence embedded within the challenger row's Findings cell... NOT a note or comment appended below... NOT a parenthetical or footnote." |

**Aspirational: C-11, C-15, C-16, C-17, C-18, C-20, C-21 pass → 7 × 2.5 = 17.5/25**

### V-01 Composite: 60 + 60 + 17.5 = **137.5** ✅ Golden

---

## V-02 — Output format (C-21 primary + C-20 added)

**Design**: Takes R4 V-02's C-21 escalation rule as anchor; wraps it in a proper OPEN/CLOSED state machine gate with a 3-condition closure predicate.

### Essential

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | **PASS** | Step 1 reads every file; "Zero roles may be invented." |
| C-02 | **PASS** | Step 4 declares 4-column table. |
| C-03 | **PASS** | "exactly HIGH, MEDIUM, or LOW — no other values." |
| C-04 | **PASS** | Domain roles: "Apply only that role's `lens.verify` perspective." |
| C-05 | **PASS** | "one concrete action naming what to do and where." |

**Essential: 60/60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | **PASS** | Standard: 2–3 roles; deep: all non-challenger. |
| C-07 | **PASS** | Step 5: cross-role synthesis required; convergence/conflict named; slot-gap rows count. |
| C-08 | **PASS** | Step 6: AMEND with 4 specific options. |
| C-09 | **PASS** | Step 2 (Challenger bracket) precedes Step 3 (Domain review). |
| C-10 | **PASS** | Step 3: "Name a specific artifact surface in each finding." |
| C-14 | **PASS** | Step 1: ERROR halts unconditional — absent directory, empty directory, missing fields. |

**Recommended: 60/60**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-11 | **PASS** | 4-slot form (SLOT-A through D). |
| C-12 | **FAIL** | 4-column schema only; no Lens column; no per-role lens declaration in output. |
| C-13 | **FAIL** | No typed column contracts. |
| C-15 | **PASS** | "Step 2 — Challenger bracket" named before "Step 3 — Domain review"; gate G1 enforces boundary. |
| C-16 | **PASS** | Escalation rule mandates dedicated HIGH-severity row per unfilled slot. |
| C-17 | **PASS** | G1 OPEN/CLOSED states; "Domain review does not begin until G1 closes." |
| C-18 | **PASS** | Items 4–5 inside escalation rule: "Do not embed the gap finding as a sentence within the challenger row's Findings cell." "Do not append the gap as a note or comment below the challenger row." |
| C-19 | **FAIL** | No typed column schema; no column-level anti-pattern exclusions. |
| C-20 | **PASS** | G1 named states OPEN/CLOSED; 3-condition closure predicate. ≥2 enumerated conditions all required. |
| C-21 | **PASS** | Items 4–5 of escalation rule state prohibited forms inside the rule definition: "Do not embed... A finding embedded inside another row's cell is not a dedicated row." "Do not append... An appended note is not a matrix row." |

**Aspirational: C-11, C-15, C-16, C-17, C-18, C-20, C-21 pass → 7 × 2.5 = 17.5/25**

### V-02 Composite: 60 + 60 + 17.5 = **137.5** ✅ Golden

---

## V-03 — Output format (C-19 column anti-patterns + C-20 gate)

**Design**: Schema-first with 5-column output contract (columns carry anti-pattern exclusions); Phase 2 challenger bracket runs under a 4-condition OPEN/CLOSED gate.

### Essential

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | **PASS** | Phase 1: reads every file; "Zero roles may be invented or substituted." |
| C-02 | **PASS** | Phase 4: 5-column table — required 4 columns present plus Lens (superset schema passes). |
| C-03 | **PASS** | Severity column definition: "enum — exactly HIGH, MEDIUM, or LOW." Anti-pattern listed in schema. |
| C-04 | **PASS** | Phase 3 per-row validation gate checks Lens cell against this role's `lens.verify`; findings against named surface. |
| C-05 | **PASS** | Recommendation column: "names (1) what to do and (2) where in the artifact." Anti-pattern: generic directives excluded. |

**Essential: 60/60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | **PASS** | Standard: 2–4 non-challenger roles; deep: all non-challenger. |
| C-07 | **PASS** | Phase 4: cross-role synthesis required; convergence/conflict named. |
| C-08 | **PASS** | AMEND block with 4 specific options. |
| C-09 | **PASS** | Phase 2 (CHALLENGER BRACKET) executes before Phase 3 (DOMAIN REVIEW). |
| C-10 | **PASS** | Findings column definition: "names a specific artifact surface: a section title, field name, diagram element, or named assumption." Anti-pattern excluded by column schema. |
| C-14 | **PASS** | Phase 1 ERROR halts: absent directory, empty, missing fields — unconditional, no soft fallback. |

**Recommended: 60/60**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-11 | **PASS** | Phase 2: 4-slot form (SLOT-A through D). |
| C-12 | **PASS** | Lens column in 5-column schema: "one sentence: 'As a [role], I care about [specific concern from `lens.verify`]'." Anti-pattern: "NOT: generic role restatements." Challenger Lens cell explicitly templated. |
| C-13 | **PASS** | Output schema table declares type contracts per column. "Per-row validation gate: before writing any row, verify all five cells against their column constraints including anti-pattern exclusions." |
| C-15 | **PASS** | "PHASE 2 — CHALLENGER BRACKET" declared before "PHASE 3 — DOMAIN REVIEW"; G1 gate enforces boundary. |
| C-16 | **PASS** | Escalation rule: unfilled slot → "log a HIGH finding in the matrix." Severity HIGH, per-slot. |
| C-17 | **PASS** | G1 OPEN state declared; "Domain review does not begin until G1 transitions to CLOSED"; 4-condition closure predicate. |
| C-18 | **PARTIAL** | Escalation rule says "log a HIGH finding in the matrix" — directs to a matrix entry, but does not use "separate, dedicated row" language, does not show the full row schema template, and does not name the prohibited forms (embedding/appending) inside the rule. Evidence is sufficient to imply a matrix row but lacks the explicit structural specification C-18 requires. |
| C-19 | **PASS** | Output schema table lists anti-pattern exclusions inside each column definition: Severity — "NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe)"; Findings — "NOT: abstract observations without a named surface"; Lens — "NOT: generic role restatements"; Recommendation — "NOT: generic directives." |
| C-20 | **PASS** | Gate G1: OPEN/CLOSED states named; "G1 transitions OPEN → CLOSED when all hold:" with 4 enumerated conditions. |
| C-21 | **FAIL** | Escalation rule says "log a HIGH finding in the matrix" but contains no statement of the prohibited form inside the rule definition. "Do not collapse two slots into one sentence" is a cardinality constraint, not an exclusion naming the anti-form. |

**Aspirational: C-11, C-12, C-13, C-15, C-16, C-17, C-19, C-20 pass (8 × 2.5 = 20.0) + C-18 partial (1.25) = 21.25/25**

### V-03 Composite: 60 + 60 + 21.25 = **141.25** ✅ Golden

---

## V-04 — Inertia + output format (C-20 + C-21 as structural unit)

**Design**: Gate G1 closure conditions are expressed in terms of row production; the escalation rule names both required form and prohibited forms; the prohibited forms cross-reference the gate conditions they violate.

### Essential

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | **PASS** | Step 1: reads every file; "Pool is locked. Zero roles may be invented." |
| C-02 | **PASS** | Phase 2 review matrix: 4-column table. |
| C-03 | **PASS** | "exactly HIGH, MEDIUM, or LOW — no other values." |
| C-04 | **PASS** | Domain roles: "Apply only that role's `lens.verify` perspective." |
| C-05 | **PASS** | "one action naming what to do and where." |

**Essential: 60/60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | **PASS** | Standard: 2–3 non-challenger; deep: all non-challenger. |
| C-07 | **PASS** | Cross-role synthesis required; convergence/conflict named; slot-gap rows count. |
| C-08 | **PASS** | AMEND with 4 specific options including "Reopen G1." |
| C-09 | **PASS** | PHASE 1 — CHALLENGER BRACKET precedes PHASE 2 — DOMAIN REVIEW AND OUTPUT. |
| C-10 | **PASS** | "Name a specific artifact surface in each finding." |
| C-14 | **PASS** | Step 1: ERROR halts — "unconditional, no soft fallback, no partial execution." Strongest language in R5. |

**Recommended: 60/60**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-11 | **PASS** | 4-slot form (SLOT-A through D). |
| C-12 | **FAIL** | 4-column output matrix; no Lens column; no per-role lens declaration. |
| C-13 | **FAIL** | No typed column contracts. |
| C-15 | **PASS** | "PHASE 1 — CHALLENGER BRACKET" and "PHASE 2 — DOMAIN REVIEW" as named phases. |
| C-16 | **PASS** | Escalation rule mandates dedicated HIGH-severity row per slot. |
| C-17 | **PASS** | G1 OPEN state; 5-condition closure; "Domain review does not begin until G1 transitions to CLOSED." |
| C-18 | **PASS** | Step 2: "Produce a **separate, dedicated matrix row**." Steps 3–4: "Do not embed... produces an inline annotation, not a matrix row, and **does not satisfy G1 closure condition 3**." "Do not append... produces an appended comment, not a matrix row, and **does not satisfy G1 closure condition 3**." |
| C-19 | **FAIL** | No typed column schema; no column-level anti-pattern exclusions. |
| C-20 | **PASS** | G1 named states OPEN/CLOSED; 5-condition closure; conditions 3–4 define what does NOT satisfy the gate (anti-forms at the gate level). |
| C-21 | **PASS** | Steps 3–4 of escalation rule state prohibited forms inside the rule definition, and additionally back-reference the gate condition they violate ("does not satisfy G1 closure condition 3"). Strongest C-21 evidence in R5 for the gate-escalation entanglement. |

**Aspirational: C-11, C-15, C-16, C-17, C-18, C-20, C-21 pass → 7 × 2.5 = 17.5/25**

### V-04 Composite: 60 + 60 + 17.5 = **137.5** ✅ Golden

---

## V-05 — Maximal (C-19 + C-20 + C-21 + full prior stack)

**Design**: Four-phase lifecycle (LOAD → CHALLENGER → DOMAIN → RENDER); 5-column typed schema with anti-pattern exclusions per column (C-13 + C-19); named state machine gate with 4-condition closure (C-15 + C-17 + C-20); escalation rule naming prohibited forms cross-referenced to G1 closure conditions (C-16 + C-18 + C-21); Lens column (C-12); structured null hypothesis (C-11).

### Essential

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | **PASS** | PHASE 1 L1–L4: reads every file; "Pool locked. Zero roles may be invented." |
| C-02 | **PASS** | PHASE 4 R2: 5-column table — Role, Lens, Findings, Severity, Recommendation. All four required columns present. |
| C-03 | **PASS** | Severity column: "enum — exactly HIGH, MEDIUM, or LOW." Anti-pattern: "NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations." |
| C-04 | **PASS** | D3 per-role instructions enforce distinct perspectives; per-row validation gate checks lens traces to `lens.verify`. |
| C-05 | **PASS** | Recommendation column: "names (1) what to do and (2) where in the artifact." Anti-pattern: "NOT: generic directives; NOT: recommendations without a named artifact location." |

**Essential: 60/60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | **PASS** | Standard: 2–4 non-challenger roles; deep: all non-challenger. |
| C-07 | **PASS** | R3: cross-role synthesis required; convergence/conflict named; slot-gap rows count. |
| C-08 | **PASS** | R4 AMEND: 5 specific options (add reviewer, full registry, scope to group, reopen G1, re-run single role). Richest AMEND block in R5. |
| C-09 | **PASS** | PHASE 2 — CHALLENGER BRACKET executes before PHASE 3 — DOMAIN REVIEW. G1 gate enforces the boundary. |
| C-10 | **PASS** | Findings column: "names a specific artifact surface." Anti-pattern: "NOT: abstract observations without a named surface." Per-row validation gate checks this before writing. |
| C-14 | **PASS** | L3 ERROR halts: absent directory, empty, missing fields — unconditional, no soft fallback. |

**Recommended: 60/60**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-11 | **PASS** | C2: 4-slot form (SLOT-A through D) with named blanks. |
| C-12 | **PASS** | Lens column declared in output schema: "one sentence: 'As a [role], I care about [specific concern from `lens.verify`]'." Anti-pattern: "NOT: generic role restatements." C5 and D3 enforce lens declaration per role. |
| C-13 | **PASS** | Output schema is a 5-column typed table with column contracts and anti-pattern exclusions. "Per-row validation gate: before writing any row, verify all five cells against their constraints including anti-pattern exclusions." |
| C-15 | **PASS** | PHASE 2 — CHALLENGER BRACKET and PHASE 3 — DOMAIN REVIEW are named phases with explicit entry conditions. |
| C-16 | **PASS** | C4 escalation rule: unfilled slot → "Produce a separate, dedicated matrix row... Severity: HIGH." |
| C-17 | **PASS** | G1 OPEN/CLOSED states; "Domain review does not begin until G1 transitions to CLOSED." 4-condition closure predicate. |
| C-18 | **PASS** | C4 steps 3–4: "Do not embed this finding as a sentence within the challenger row's Findings cell. A sentence inside another row's Findings cell is not a dedicated row and **does not satisfy G1 closure condition 3**." "Do not append this as a note below the challenger row. An appended note is not a matrix row and **does not satisfy G1 closure condition 3**." |
| C-19 | **PASS** | Output schema table lists anti-pattern exclusions inside each column definition: Role — "NOT: invented names"; Lens — "NOT: generic role restatements"; Findings — "NOT: abstract observations without a named surface"; Severity — "NOT: freestyle labels..."; Recommendation — "NOT: generic directives; NOT: recommendations without a named artifact location." |
| C-20 | **PASS** | G1 named states OPEN/CLOSED; 4-condition closure predicate requiring all conditions simultaneously true. "G1 transitions from OPEN to CLOSED when ALL hold." |
| C-21 | **PASS** | C4 steps 3–4 state prohibited forms inside the escalation rule definition. Each prohibition cross-references the gate condition it violates: "is not a dedicated row and **does not satisfy G1 closure condition 3**." The prohibition is mechanically entangled with the state machine gate — C-20 and C-21 share structural site. |

**Aspirational: ALL 10 pass → 10 × 2.5 = 25/25**

### V-05 Composite: 60 + 60 + 25 = **145** ✅ Golden — MAX SCORE

---

## Summary Table

| Variation | E | R | A | Composite | All Essential | Golden? |
|-----------|---|---|---|-----------|--------------|---------|
| V-01 | 60 | 60 | 17.5 | **137.5** | YES | ✅ |
| V-02 | 60 | 60 | 17.5 | **137.5** | YES | ✅ |
| V-03 | 60 | 60 | 21.25 | **141.25** | YES | ✅ |
| V-04 | 60 | 60 | 17.5 | **137.5** | YES | ✅ |
| V-05 | 60 | 60 | 25.0 | **145.0** | YES | ✅ |

**Rank**: V-05 (145) > V-03 (141.25) > V-01 = V-02 = V-04 (137.5)

---

## Aspirational Criteria Pass Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-12 | ❌ | ❌ | ✅ | ❌ | ✅ |
| C-13 | ❌ | ❌ | ✅ | ❌ | ✅ |
| C-15 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-16 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-17 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-18 | ✅ | ✅ | ~½ | ✅ | ✅ |
| C-19 | ❌ | ❌ | ✅ | ❌ | ✅ |
| C-20 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-21 | ✅ | ✅ | ❌ | ✅ | ✅ |

The **V-03 vs V-05 gap** (141.25 vs 145) is exactly the C-21 failure (−2.5) and C-18 partial (−1.25) in V-03. V-03 achieved C-19 and C-20 together but the escalation rule's "log a HIGH finding in the matrix" language did not name the prohibited forms inside the rule.

The **V-01/V-02/V-04 cluster** (all 137.5) all pass C-20 and C-21 but lack C-12, C-13, C-19 — all three schema-quality criteria that require the typed 5-column output contract.

---

## Excellence Signals — V-05

V-05 is the first variation in the crew-review series to achieve maximum score. Three structural properties made it uniquely the top scorer:

**1. Escalation rule anti-patterns cross-referenced to gate closure conditions**
The C-21 prohibition ("Do not embed this finding as a sentence within the challenger row's Findings cell") is not just inside the escalation rule — it is linked back to the gate by number: "does not satisfy G1 closure condition 3." This makes C-20 and C-21 causally entangled: violating C-21 is not merely a formatting error, it is a gate failure. The model cannot satisfy G1 closure without satisfying C-21. V-04 introduced this pattern for C-18 and C-20; V-05 extends it to C-21 as well.

**2. Four-phase lifecycle separating schema declaration, challenger execution, domain review, and output rendering**
By making PHASE 4 — RENDER a distinct phase (separate from DOMAIN REVIEW), V-05 creates a structural moment where all rows already exist before output is composed. The schema is declared before PHASE 1 — LOAD begins, so every phase that follows operates under a known output contract. This is what allows C-13 and C-19 to be simultaneously stable: the contract is declared once, enforced by per-row validation in every phase, and rendered last.

**3. Archetype-group ordering within domain review**
D2 assigns domain roles to execution groups (product → technical → quality → other) before selecting alphabetically within groups. This extends the phase discipline (C-15) one level deeper into the domain review phase itself — not just challenger-before-domain, but a sub-ordering within domain execution. This does not yet have its own criterion but is a candidate for C-22 in a future rubric round.

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["Escalation rule anti-pattern prohibitions cross-reference gate closure conditions by number, making C-21 and C-20 causally entangled: violating the prohibited form is a gate failure, not merely a formatting error", "Four-phase lifecycle (LOAD, CHALLENGER, DOMAIN, RENDER) declares the typed output schema before execution begins, so every phase operates under the same contract and per-row validation fires in each phase independently", "Archetype-group ordering within domain review (product -> technical -> quality -> other) extends phase discipline one structural level below the challenger/domain boundary"]}
```
