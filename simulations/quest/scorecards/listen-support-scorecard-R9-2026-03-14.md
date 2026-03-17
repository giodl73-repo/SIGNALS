## listen-support Round 9 — Scorecard

**Rubric**: v9 (195 pts ceiling)
**New criteria**: C-28 (Phase-Architecture Severity Inference Rule, 5 pts), C-29 (Dedicated Switching-Friction Gap Sub-Section, 5 pts)
**Base assumption**: All variations inherit R8 V-05 ceiling on C-01 through C-27 (185 pts)

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (C-01 – C-05) — all variations

All five variations build on R8 V-05 base, which held ceiling on all essential criteria. No variation removes or regresses any essential mechanism.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 All Five Fields | PASS | PASS | PASS | PASS | PASS |
| C-02 Controlled Vocabulary | PASS | PASS | PASS | PASS | PASS |
| C-03 Persona Grounding | PASS | PASS | PASS | PASS | PASS |
| C-04 Gap Analysis Structured | PASS | PASS | PASS | PASS | PASS |
| C-05 Min Count + Category Spread | PASS | PASS | PASS | PASS | PASS |

All essential pass across all variations. **Essential subtotal: 60 / 60 for all.**

---

### Recommended Criteria (C-06 – C-12, 30 pts) — all variations

No variation modifies mechanisms that bear on recommended criteria. All inherit R8 V-05 ceiling.

**Recommended subtotal: 30 / 30 for all.**

---

### Aspirational Criteria (C-13 – C-27, 95 pts) — all variations

No variation modifies mechanisms bearing on C-13 through C-27. All inherit R8 V-05 ceiling.

**Aspirational (legacy) subtotal: 95 / 95 for all.**

---

### New Aspirational Criteria (C-28 + C-29, 10 pts)

#### C-28 — Phase-Architecture Severity Inference Rule (5 pts)

The criterion requires stating *why* early-phase tickets produce lower severity (adoption friction, fallback available) and why late-phase tickets produce higher severity (parity gaps block committed users) — and making that rule directionally binding, not decorative.

| V | Mechanism | Verdict | Evidence note |
|---|-----------|---------|---------------|
| V-01 | Annotation inside Step 2 | **FAIL** | Descriptive, not operationally binding. A model reads the annotation, then applies any defensible range assignment. No structural forcing. |
| V-02 | Annotation inside Step 2 (same as V-01) | **FAIL** | Richer C-29 format doesn't help C-28. Annotation placement is identical; same failure mode as V-01. |
| V-03 | Causal prose in Step 2 + soft count in Pass 2 | **PARTIAL** | Explanation is present and directional, but no imperative constraint and no hard audit. A model can apply the reasoning selectively without triggering a flag. ~half credit. |
| V-04 | Dedicated STEP 2C (imperative) + count-and-flag in Step 4B | **PASS** | STEP 2C isolation makes the rule a named checkpoint. Step 4B's count-and-flag catches Phase 1 P0/P1 or Phase 3 P3 without requiring exception prose. Operationally binding. |
| V-05 | STEP 2C (imperative + paraphrase) + full INFERENCE AUDIT in Pass 2 Part C | **PASS** | Paraphrase-before-proceed forces internalization. Pass 2 Part C scans for directional violations and requires explicit exception acknowledgment. C-28 becomes a verified output property. |

**C-28 scores**: V-01: 0, V-02: 0, V-03: 2, V-04: 5, V-05: 5

---

#### C-29 — Dedicated Switching-Friction Gap Sub-Section (5 pts)

The criterion requires a labeled fourth sub-section in the gap analysis where every entry includes a `Migrating from: [tool]` field, making the switching-friction inventory separately enumerable.

| V | Format | Verdict | Evidence note |
|---|--------|---------|---------------|
| V-01 | 2-field, dedicated sub-section | **PASS** | Dedicated sub-section present. `Migrating from:` field present per entry. Minimum viable form satisfies the criterion. |
| V-02 | 4-field, dedicated sub-section | **PASS** | Same structural pass as V-01 with richer per-entry data (4 fields vs 2). `Migrating from:` field is grep-checkable. Exceeds minimum but same criterion verdict. |
| V-03 | 2-field, dedicated sub-section | **PASS** | Same as V-01. Sub-section dedicated and labeled; per-entry field present. |
| V-04 | 4-field, dedicated sub-section | **PASS** | Same as V-02. Richer format; criterion fully satisfied. |
| V-05 | 4-field, dedicated sub-section + verified | **PASS** | Pass 2 Part C confirms sub-section exists and fields are populated. Satisfaction is verified, not assumed. |

**C-29 scores**: V-01: 5, V-02: 5, V-03: 5, V-04: 5, V-05: 5

---

## Composite Scores

| V | Essential (60) | Recommended (30) | Aspirational legacy (95) | C-28 (5) | C-29 (5) | **Total (195)** |
|---|---------------|-----------------|--------------------------|----------|----------|----------------|
| V-01 | 60 | 30 | 95 | 0 | 5 | **190** |
| V-02 | 60 | 30 | 95 | 0 | 5 | **190** |
| V-03 | 60 | 30 | 95 | 2 | 5 | **192** |
| V-04 | 60 | 30 | 95 | 5 | 5 | **195** |
| V-05 | 60 | 30 | 95 | 5 | 5 | **195** |

---

## Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 | **V-05** | 195 | Ceiling. C-28 verified via paraphrase + inference audit. C-29 verified via Pass 2 scan. |
| 2 | **V-04** | 195 | Ceiling. C-28 operationally bound. C-29 4-field. Unverified but structurally correct. |
| 3 | **V-03** | 192 | Partial C-28 via causal prose + soft audit. C-29 passes. |
| 4 | **V-02** | 190 | C-28 fails (annotation placement). C-29 richer format but same criterion score as V-01. |
| 5 | **V-01** | 190 | C-28 fails. C-29 minimal pass. |

V-04 and V-05 tie on numeric score. V-05 ranks above because its INFERENCE AUDIT converts C-28 from a read-and-apply instruction into a verified output property — meaning future rubric tightening on C-28 won't create a regression risk.

V-02 ranks below V-03 despite a tied score: V-03 earns partial C-28 credit through directional causal prose, which is a more principled partial than V-02's zero. V-02's richer C-29 format doesn't compensate on the scoring axis.

---

## Excellence Signals (from V-05)

**Signal 1 — Paraphrase-before-proceed forces internalization.**
STEP 2C requires the model to restate the inference rule in its own words before applying it. This converts rule-reading into rule-ownership. A model that paraphrases "early-phase tickets are lower severity because workarounds are still available" cannot then assign P0 to a Phase 1 how-to ticket without a detectable contradiction. This pattern generalizes: any constraint that must be *reasoned about* rather than *looked up* benefits from forced paraphrase.

**Signal 2 — Inference audit as a verification pass converts soft constraints to hard ones.**
Pass 2 Part C scans the completed output for Phase 1 P0/P1 assignments and Phase 3 P3 assignments, then requires explicit exception acknowledgment or violation reasoning. This makes C-28 a verified output property rather than an honor-system constraint. The pattern generalizes: any rule where violations are enumerable (a specific phase+severity combination) can be made audit-checkable with a targeted scan step.

---

```json
{"top_score": 195, "all_essential_pass": true, "new_patterns": ["paraphrase-before-proceed: requiring the model to restate a rule in its own words before applying it converts rule-reading into rule-ownership and makes contradictions detectable", "inference-audit-pass: a dedicated scan step that enumerates specific violation signatures (phase+severity combinations) and requires exception acknowledgment converts a soft directional constraint into a verified output property"]}
```
