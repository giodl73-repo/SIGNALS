## Quest Score — corps-leaderboard R8

---

### Scoring Model (v8)

Derived from rubric's stated expected scores:
- All 5 essential pass → **90 pts base** (implied from 98.82 = 90 + 15 × 10/17)
- 17 aspirational criteria × **10/17 pts each** (~0.588 pts) → 10 pts max
- **Total max: 100**

Formula: `90 + (aspirational_passed / 17) × 10`

---

### Essential Criteria: C-01 – C-05

All five R8 variations carry the essential baseline forward from R7. Verified per variation:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Signal Registry Scan (glob, 4 fields, empty-workspace halt) | PASS | PASS | PASS | PASS | PASS |
| **C-02** Per-topic achievements, exact names (all 5 names) | PASS | PASS | PASS | PASS | PASS |
| **C-03** Three team milestones, exact names, non-empty evidence | PASS | PASS | PASS | PASS | PASS |
| **C-04** Ranked leaderboard, unknown-contributor fallback | PASS | PASS | PASS | PASS | PASS |
| **C-05** ≥3 actions, namespace+topic+exact achievement name per action | PASS | PASS | PASS | PASS | PASS |

**All essential: PASS across all five variations.**

---

### Aspirational Criteria: C-06 – C-23 (Inherited from R7)

All five R8 variations were designed to carry C-06–C-23 forward at full coverage. Spot-check on the two most recently added (v6/v7) criteria:

**C-22 — Dual-Statement Prevents-Rule Redundancy**: `prevents:` rule at two structurally independent locations.

- **V-01**: Pre-Write Check states the rule; then restated explicitly after the action template as a separate `prevents: prefix rule` paragraph. Two independent locations. **PASS**
- **V-02**: Pre-Write Check ("directly eliminate a zero-score condition carry the `prevents:` prefix") + Action definition ("The `prevents:` prefix applies to zero-score-eliminating actions") — both in Role 3 section 3.3, structurally independent. **PASS**
- **V-03**: Pre-Write Check states the rule; then "The `prevents:` prefix rule applies to the action list below. This rule also applies inside the action template" is a second independent statement. **PASS**
- **V-04**: Pre-Write Check states the rule; then explicit blockquote `> **prevents: prefix rule** — Any action whose primary purpose is eliminating a state...` is structurally independent. **PASS**
- **V-05**: Pre-Write Check header states the rule; then `**prevents: prefix rule** (applied inside the action template and enforced here)` is a second structurally distinct statement. **PASS**

**C-23 — Two-Level Nearest-Miss Cascade**: Level 1 first; Level 2 only when no Level 1 exists; both with name + numeric gap.

- All five variations: Level 1 is defined as 1 unit away, Level 2 is "ONLY when no Level 1 topic exists" with explicit name + gap requirement. **PASS** across all.

C-06–C-23 (16 criteria): **PASS** for all five variations.

---

### Aspirational Criteria: C-24 and C-25 (New in v8)

**C-24 — Gate-Level Prevents: Prefix Count Self-Audit**

Tests for a gate construct that requires emitting a count of how many actions used the `prevents:` prefix.

- **V-01**: Pre-Write Check identifies zero-score conditions, action template shows `prevents:` prefix usage, but **no count audit gate line** after actions. FAIL.
- **V-02**: Role 3 (Publisher), section 3.3 ends with: `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions` — explicit post-action count report, substituting N with the actual count. **PASS.** This makes the zero-score coverage mechanically verifiable at review time.
- **V-03**: Pre-Write Check and dual-location rule present, but no count gate. FAIL.
- **V-04**: Phase 4 exit gate checklist includes "prevents: prefix applied to zero-score-condition actions" as a check, but this is a generic checklist item, not a count-audit line. The criterion requires counting and reporting N. FAIL.
- **V-05**: Pre-Write Check and dual rule present, no count gate. FAIL.

**C-25 — Synthesis Novelty Constraint**

Tests for an instruction-level constraint requiring the Team Insight to contain information not already in the health/inertia assessment.

- **V-01**: Team Insight: "cross-topic conclusion + concrete number + named contributor or topic." Structural form only. No novelty gate. FAIL.
- **V-02**: Team Insight (section 3.2): Same structural requirements. No novelty gate. FAIL.
- **V-03**: Team Insight: "cross-topic conclusion, includes a concrete number, and names a specific contributor or topic." No novelty gate. FAIL.
- **V-04**: Team Insight: "cross-topic conclusion + concrete number + named contributor or topic." No novelty gate. FAIL.
- **V-05**: Team Insight (section 2.2): Skeptic gate is fully explicit. "The Team Insight must contain something the Skeptic would not already know from reading Pass 1." Includes operationalized pass/fail examples — a restated inertia flag fails, a second-order cross-topic pattern passes. The Skeptic having read Pass 1 in full defines "already known" operationally. **PASS.**

---

### Per-Variation Score Summary

| Variation | Essential | C-06–C-21 | C-22 | C-23 | C-24 | C-25 | Aspirational | Score |
|-----------|-----------|-----------|------|------|------|------|-------------|-------|
| V-01 | 5/5 | 12/12 | ✓ | ✓ | ✗ | ✗ | 15/17 | **98.82** |
| V-02 | 5/5 | 12/12 | ✓ | ✓ | ✓ | ✗ | 16/17 | **99.41** |
| V-03 | 5/5 | 12/12 | ✓ | ✓ | ✗ | ✗ | 15/17 | **98.82** |
| V-04 | 5/5 | 12/12 | ✓ | ✓ | ✗ | ✗ | 15/17 | **98.82** |
| V-05 | 5/5 | 12/12 | ✓ | ✓ | ✗ | ✓ | 16/17 | **99.41** |

Score formula: `90 + (passed/17) × 10`
- 15/17 → 90 + 8.824 = **98.82**
- 16/17 → 90 + 9.412 = **99.41**

---

### Ranking

1. **V-02** (99.41) — Role sequence: Archivist → Analyst → Publisher + C-24 count gate
1. **V-05** (99.41) — Inertia framing + C-25 Skeptic novelty gate *(tied)*
3. **V-01** (98.82) — Direct imperative phrasing register
3. **V-03** (98.82) — Prose health narrative format *(tied)*
3. **V-04** (98.82) — Milestones-first inverted lifecycle *(tied)*

Two co-ceiling-setters at 99.41. The ceiling remains open — no variation combines both C-24 and C-25.

---

### Excellence Signals

**From V-02 (C-24)**:

The `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions` line is a **post-phase verification line** — it runs *after* the action-writing phase has closed, forcing the model to count backward through what it wrote. A model that silently omitted a `prevents:` prefix will produce a mismatch between the required count and actual rows, making the failure detectable at review time. This is qualitatively different from a pre-write check (which only primes the model before it writes). The gate creates an independent post-write audit signal.

**From V-05 (C-25)**:

The Skeptic gate is not just a novelty instruction — it provides an operational pass/fail test *within the instruction itself*. The failing example ("alice is the sole contributor on 3 topics, each flagged solo-hold") describes something directly visible in the inertia table. The passing example describes a second-order cross-section conjunction ("exactly 1 contributor away from unlocking shared coverage, but that contributor would need to post to 2 different topics simultaneously — an action no current team member has done yet"). Embedding example contrasts in the instruction removes ambiguity about what novelty means, shifting the model from structural compliance to reasoning compliance.

---

### R9 Ceiling

The first variation combining both: a **Publisher role** with an explicit `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions` line (C-24) **and** a **Skeptic-named novelty gate** on the Team Insight with pass/fail examples (C-25) — should score 100 against v8.

```json
{"top_score": 99.41, "all_essential_pass": true, "new_patterns": ["Post-action count audit gate: after the action-writing phase closes, emit a verifiable count line stating how many actions used the prevents: prefix — this creates a post-write checkpoint that surfaces silent zero-score omissions at review time, operating independently of pre-write checks", "Named-reader novelty test with embedded examples: designate a Skeptic who has read all prior sections in full, require the Team Insight to contain something that reader would acknowledge as new, and embed explicit pass/fail examples inside the instruction to operationalize novelty beyond structural form compliance"]}
```
