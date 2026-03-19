## roles-create R14 Scorecard

### Scoring Framework

**Formula:** `(essential_passed × 12) + (recommended_passed × 15) + (aspirational_passed / 23 × 10)`
**Denominator:** 23 aspirational criteria | **Per-criterion weight:** 0.4348pt

---

### Essential Criteria (C-01 – C-05)

All five variations pass all essential criteria. These are structural — all five variations have:
- Phase 6 writes to `.craft/roles/{area}/{subrole}.md` (C-01)
- FIELD-REGISTER governs all 12 frontmatter fields (C-02)
- Phase 0/1 routes name-only / description / interactive correctly (C-03)
- FIELD-REGISTER requires domain-specific orientation and lens content (C-04)
- Phase 2 checks for inertia-advocate; generates if absent (C-05)

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| **Essential** | **5/5** | **5/5** | **5/5** | **5/5** | **5/5** |

---

### Recommended Criteria (C-06 – C-07)

All five variations pass. FIELD-REGISTER enforces boolean lens.verify items (C-06); Phase 4 generates a domain specializations table (C-07).

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| **Recommended** | **2/2** | **2/2** | **2/2** | **2/2** | **2/2** |

---

### Aspirational Criteria (C-08 – C-30)

C-08 through C-24: uniform PASS across all five variations. Evidence column covers the shared pass reasons then focuses on the discriminating criteria.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-08 | PASS | PASS | PASS | PASS | PASS | FIELD-REGISTER directs archetype check against existing area roles |
| C-09 | PASS | PASS | PASS | PASS | PASS | FIELD-REGISTER governs frame (first-person) and serves (third-person) registers |
| C-10 | PASS | PASS | PASS | PASS | PASS | COLUMN-HEADER contract enforced at Gate 4b in all variations |
| C-11 | PASS | PASS | PASS | PASS | PASS | Phase 2 generates full companion file when absent |
| C-12 | PASS | PASS | PASS | PASS | PASS | INTERACTIVE-HOLD contract prohibits partial generation before all three answers |
| C-13 | PASS | PASS | PASS | PASS | PASS | Phase 5 pre-write confirmation with explicit YES/NO checklist |
| C-14 | PASS | PASS | PASS | PASS | PASS | Phase 0 INPUT-ROUTING-RULES classifies all malformed inputs before mode detection |
| C-15 | PASS | PASS | PASS | PASS | PASS | In-phase gates at Phases 0, 1, 2, 3, 4; Phase 5 is final confirmation |
| C-16 | PASS | PASS | PASS | PASS | PASS | CONTRACT: AUDIT-CHECKLIST defined before any phase |
| C-17 | PASS | PASS | PASS | PASS | PASS | Six named CONTRACT blocks at top level |
| C-18 | PASS | PASS | PASS | PASS | PASS | Checklist rows have "Gated At" column; phase gates carry `[G]`, `[H]`, `[B]`–`[F]` backward citations |
| C-19 | PASS | PASS | PASS | PASS | PASS | Phase bodies cite CONTRACT by name; no rule restatement. V-04 retry prose is correction workflow, not rule content |
| C-20 | PASS | PASS | PASS | PASS | PASS | Checklist items name CONTRACT block + scope only; no rule enumeration |
| C-21 | PASS | PASS | PASS | PASS | PASS | All cited CONTRACTs covered: G (INPUT-ROUTING-RULES), H (INERTIA-ADVOCATE-TEMPLATE), B–E (FIELD-REGISTER), F (COLUMN-HEADER); Phase 1/INTERACTIVE-HOLD is routing, not content-producing |
| C-22 | PASS | PASS | PASS | PASS | PASS | AUDIT-CHECKLIST header: "Items name the CONTRACT block and validation scope only -- no rule enumeration." |
| C-23 | PASS | PASS | PASS | PASS | PASS | Rule content confined to CONTRACT blocks, thin phase citations, thin checklist items. V-04 retry prose is procedural correction, not rule content |
| C-24 | PASS | PASS | PASS | PASS | PASS | All gates use inline annotation form `-> Gate N [ID]: ... PASS / FAIL` throughout |

**Discriminating criteria:**

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-25 | PASS | PASS | PASS | **FAIL** | PASS | V-04 bodies carry retry prose after artifact reference ("If classification fails, re-run…"; "If any field fails gate inspection, correct the field and re-run the gate before advancing.") — exceeds minimum surface |
| C-26 | PASS | PASS | **FAIL** | PASS | PASS | V-03: COLUMN-HEADER defined 3rd, FIELD-REGISTER defined 4th — inverts Phase 3/Phase 4 first-citation order. All others: canonical order (INPUT-ROUTING-RULES → INTERACTIVE-HOLD → FIELD-REGISTER → COLUMN-HEADER → INERTIA-ADVOCATE-TEMPLATE → AUDIT-CHECKLIST) |
| C-27 | PASS | PASS | PASS | PASS | PASS | V-04 phase bodies open with CONTRACT citation; retry prose follows the artifact reference, not before the citation |
| C-28 | PASS | PASS | PASS | **FAIL** | PASS | V-04: "If any field fails gate inspection, correct the field and re-run the gate before advancing." appears in Phase 3 body, after the artifact reference — correction logic in body narrative, not gate fail branch |
| C-29 | PASS | **FAIL** | PASS | PASS | PASS | V-02: Gate FAIL branches carry correction directives ("FAIL: Add missing fields before advancing.", "FAIL: Rewrite orientation.frame to first-person observational register before advancing." etc.). V-01/V-03/V-04: FAIL branches are bare verdict tokens. V-05: all bare |
| C-30 | **FAIL** | **FAIL** | **FAIL** | **FAIL** | PASS | V-01/V-02/V-03/V-04: PASS branches carry affirmation summaries ("PASS: All 12 frontmatter fields confirmed present.", "PASS: orientation.frame in first-person observational register.", etc.). V-05: all gates are bare `PASS / FAIL` — no annotation text in either branch. C-30 implies C-29: V-02's C-29 failure independently triggers C-30 failure; V-01/V-03/V-04 fail C-30 while passing C-29, confirming PASS-branch annotation is an independent inspection axis |

---

### Composite Scores

| | Essential (max 60) | Recommended (max 30) | Aspirational (max 10) | **Total** |
|--|---|---|---|---|
| **V-01** | 5/5 → 60 | 2/2 → 30 | 22/23 → 9.565 | **99.57** |
| **V-02** | 5/5 → 60 | 2/2 → 30 | 21/23 → 9.130 | **99.13** |
| **V-03** | 5/5 → 60 | 2/2 → 30 | 21/23 → 9.130 | **99.13** |
| **V-04** | 5/5 → 60 | 2/2 → 30 | 20/23 → 8.696 | **98.70** |
| **V-05** | 5/5 → 60 | 2/2 → 30 | 23/23 → 10.000 | **100.00** |

---

### Ranking

| Rank | Variation | Score | Failing Criteria |
|------|-----------|-------|-----------------|
| 1 | V-05 | 100.00 | — |
| 2 | V-01 | 99.57 | C-30 only |
| 3 (tie) | V-02 | 99.13 | C-29 + C-30 |
| 3 (tie) | V-03 | 99.13 | C-26 + C-30 |
| 5 | V-04 | 98.70 | C-25 + C-28 + C-30 |

---

### Discrimination Results

**V-01 vs V-02 symmetry probe:** Confirmed. V-01 scores exactly 1 point higher than V-02 (0.4348pt = 1 criterion). PASS-branch affirmation and FAIL-branch correction are independent annotation axes — failing one does not cascade to the other.

**V-01 (C-30 isolation):** C-30 fires on PASS-branch affirmation regardless of FAIL branch state. Gate PASS annotation is an independent inspection surface. 1 deduction only.

**V-02 (C-29 + C-30):** Two independent deductions. No cascade to C-25, C-27, or C-28 — phase bodies remain citation-only. Orthogonality confirmed.

**V-03 (C-30 + C-26):** Two independent deductions across different structural surfaces (gate annotation vs. CONTRACT ordering). No cascade. Orthogonality confirmed.

**V-04 (C-30 + C-28):** Three deductions: C-25 (implied by C-28) + C-28 + C-30. C-27 passes (citation opens body). C-29 passes (FAIL branches bare). All three surfaces — body prose, FAIL branch, PASS branch — are independently governed.

---

### Excellence Signals (V-05)

1. **Bare verdict tokens eliminate annotation surface entirely** — `PASS / FAIL` with no text on either side means gates are pure signal; the rubric has no annotation surface to inspect in either direction
2. **PASS/FAIL symmetry is the canonical form** — once FAIL-branch annotation is eliminated (C-29), applying the same discipline to PASS branches (C-30) is not additive complexity but completion of the same principle: gates communicate outcome, Phase 5 communicates state interpretation
3. **Correction prose quarantine is total** — no fix-and-retry guidance anywhere in the phase structure; Phase 5's checklist loop is the one and only repair path

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["gate PASS annotation is an independent inspection axis from gate FAIL annotation -- a skill can pass C-29 (bare FAIL) while failing C-30 (annotated PASS)", "bare PASS / FAIL in both branches eliminates all annotation surface simultaneously -- gates become pure signal in both directions with no asymmetry between verdict sides"]}
```
