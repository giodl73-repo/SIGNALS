Now I have everything I need. Let me score all five variations.

---

# Scout-Risk — Round 16 Scorecard (Rubric v15)

## Baseline Inheritance

All R16 variations are built on R15 V-05, which scored **166/168** on the v15 rubric. The only unmet criterion is **C-45** (0 pts). C-46 and C-47 are already PASS in R15 V-05.

Every criterion from C-01 through C-44, plus C-46 and C-47, is **PASS** in all five variations — the additions are surgical and isolated. Only C-45 varies across variations.

---

## Shared Criteria — All Variations (C-01 through C-44, C-46, C-47)

| Group | Criteria | Weight | Score (all variations) | Evidence anchor |
|-------|----------|--------|------------------------|-----------------|
| Essential | C-01–C-05 | 12 × 5 = 60 | 60 / 60 | Inherited from R15 V-05 — inertia mandatory/first, 5 dimensions, full anatomy, severity vocabulary, typed concrete mitigations |
| Recommended | C-06–C-08 | 10 × 3 = 30 | 30 / 30 | Inherited — dimension labels, IF-THEN likelihoods, HIGH-first order |
| Aspirational | C-09–C-44 | 2 × 36 = 72 | 72 / 72 | Inherited — all 36 aspirational criteria in C-09..C-44 PASS in R15 V-05 |
| Aspirational | C-46 | 2 | 2 / 2 | `"(which Phase 1b guarantees)"` present in Phase 2b scope exclusion — PASS in R15 V-05 |
| Aspirational | C-47 | 2 | 2 / 2 | `"adds columns or defines its own row anatomy"` — two mechanisms enumerated — PASS in R15 V-05 |
| **Subtotal** | | **166** | **166 / 166** | |

**C-45 starts at 0 pts (FAIL) in R15 V-05. R16 adds exactly C-45 handling. All variation scoring below focuses on C-45 delta.**

---

## C-45 Pass Condition (v15 Rubric)

> "A pre-declared violation taxonomy block — **parallel to the Phase 0 mitigation type taxonomy** — defines the permissible violation categories before any prohibition site references them. Without it, each prohibition site names its category ad hoc, leaving the violation vocabulary open."

Two functional requirements drive the assessment:
1. **Structural independence** — is the taxonomy a self-standing block or embedded inside Phase 0?
2. **Traceable drawn-from** — are prohibition sites explicitly connected to the taxonomy?

---

## Variation-by-Variation C-45 Assessment

### V-01 — Compact sub-section appended to Phase 0 (3 classes)

**What it adds**: Part B appended to the existing Phase 0 Mitigation Type Taxonomy block. Three violation classes listed compactly. No per-site citations.

**Assessment**:
- Pre-declared before generation phases: **yes** (Phase 0 precedes Phase 0b / Phase 1)
- Violation types closed: **yes** (3 named classes)
- "Parallel to" Phase 0: **no** — it is *inside* Phase 0, not a sibling block of equal structural weight. C-45 explicitly invokes "parallel to the Phase 0 mitigation type taxonomy," describing structural parity, not embedding. A sub-section of Phase 0 makes the violation taxonomy a sub-clause of the mitigation taxonomy rather than its own entity. No per-site citations to establish drawn-from evidence.

**C-45: PARTIAL (1 pt)** — taxonomy is pre-declared and closes the vocabulary, but structural independence is not satisfied; compact 3-class form lacks the parallel-weight framing that C-45 describes.

**V-01 score: 166 + 1 = 167/168** (Strong band, below golden threshold of 168 for top tier)

---

### V-02 — Standalone Phase 0c block (4 classes, parallel weight to Phase 0)

**What it adds**: A new named phase — Phase 0c — positioned after Phase 0 and Phase 0b, before Phase 1. Four violation classes with descriptions. No per-site citations.

**Assessment**:
- Pre-declared before generation phases: **yes** (Phase 0c is a pre-phase block)
- Violation types closed: **yes** (4 named classes, explicit closure)
- "Parallel to" Phase 0: **yes** — Phase 0c is a sibling block of equal structural weight to Phase 0 (both are pre-phase named reference blocks). The structural pattern directly mirrors the mitigation type taxonomy.
- Drawn-from evidence: **implicit** — no per-site citations, but the taxonomy predates all prohibition sites, so the relationship is structurally established.

**C-45: PASS (2 pts)** — standalone block, parallel structural weight, 4 closed classes.

**V-02 score: 166 + 2 = 168/168** (Golden — maximum)

---

### V-03 — Phase 0 sub-section + explicit per-site citations

**What it adds**: Same sub-section placement as V-01 (Part B of Phase 0, 3 classes), but every violation site adds `(Phase 0c taxonomy)` or equivalent citation.

**Assessment**:
- Pre-declared before generation phases: **yes**
- Violation types closed: **yes** (3 named classes)
- "Parallel to" Phase 0: **no** — same structural issue as V-01; the block is nested inside Phase 0
- Drawn-from evidence: **yes, explicitly** — per-site citations establish the `drawn-from` relationship at every use site, satisfying C-45's behavioral requirement even if the structural placement is weaker than a standalone phase

C-45's pass condition requires that violation types be "drawn from" the taxonomy rather than named ad hoc. V-03's per-site citations directly demonstrate this at each prohibition site — "format violation (Phase 0 taxonomy)" at Phase 2 converts the ad hoc naming into an explicit reference. The taxonomy is pre-declared; the citations make the drawing traceable. The "parallel to" language describes the structural analogy, but the functional requirement (closed vocabulary, pre-declared, sites draw from it) is satisfied.

**C-45: PASS (2 pts)** — per-site citations compensate for sub-section placement by making the drawn-from relationship explicit and verifiable at each site.

**V-03 score: 166 + 2 = 168/168** (Golden — maximum)

---

### V-04 — Standalone Phase 0c (4 classes + explicit closure declaration; no per-site citations)

**What it adds**: Phase 0c as a standalone block (like V-02) with 4 classes, plus an explicit closure declaration sentence (e.g., "This taxonomy is closed. No violation category outside this list may be named at any prohibition site."). No per-site citations.

**Assessment**:
- Pre-declared before generation phases: **yes**
- Violation types closed: **yes, doubly** — 4 classes + explicit closed declaration
- "Parallel to" Phase 0: **yes** — standalone phase block, parallel structural weight
- Drawn-from evidence: **implicit** — no per-site citations; the structural pre-declaration + closure language establishes the connection

The explicit closure declaration goes beyond V-02 by making the closed-set guarantee a named assertion rather than an implied one. This is the strongest form of vocabulary closure without per-site citation overhead.

**C-45: PASS (2 pts)** — standalone block + closure declaration — most structurally robust form for C-45 compliance.

**V-04 score: 166 + 2 = 168/168** (Golden — maximum)

---

### V-05 — Standalone Phase 0c (V-02) + per-site citations referencing Phase 0c by name (V-03)

**What it adds**: Phase 0c standalone block (4 classes, parallel weight) + explicit `(Phase 0c taxonomy)` citation at every violation site.

**Assessment**:
- Pre-declared before generation phases: **yes**
- Violation types closed: **yes** (4 classes, standalone)
- "Parallel to" Phase 0: **yes** — fully independent structural block
- Drawn-from evidence: **yes, explicit by name** — every prohibition site cites "Phase 0c taxonomy," making the vocabulary closure verifiable at the annotation level as well as the structural level

V-05 satisfies every facet of C-45: structural independence (Phase 0c), parallel weight to Phase 0, pre-declared taxonomy, closed vocabulary, and explicit drawn-from citations at each use site. This is the maximum expression of C-45.

**C-45: PASS (2 pts)**

**V-05 score: 166 + 2 = 168/168** (Golden — maximum)

---

## Composite Score Summary

| Variation | C-45 | Delta | Score | Band | Rank |
|-----------|------|-------|-------|------|------|
| V-01 | PARTIAL (1) | +1 | **167/168** | Strong | 5th |
| V-02 | PASS (2) | +2 | **168/168** | Golden | T-1st |
| V-03 | PASS (2) | +2 | **168/168** | Golden | T-1st |
| V-04 | PASS (2) | +2 | **168/168** | Golden | T-1st |
| V-05 | PASS (2) | +2 | **168/168** | Golden | T-1st |

**All essentials (C-01–C-05): PASS in all variations.**
**All recommended (C-06–C-08): PASS in all variations.**

---

## Leaderboard Differentiation (Tiebreak Within 168/168)

V-02, V-03, V-04, V-05 all score 168/168. Structural quality distinguishes them within the tie:

| Rank | Variation | Why It's Stronger |
|------|-----------|-------------------|
| 1st | **V-05** | Standalone Phase 0c (structural independence) + per-site citations (explicit drawn-from traceability) — satisfies both axes of C-45 |
| 2nd | **V-04** | Standalone Phase 0c + explicit closure declaration — strongest structural form; closure language makes the closed-set assertion explicit rather than implied |
| 3rd | **V-02** | Standalone Phase 0c — full structural independence, 4 classes, clean and minimal |
| 4th | **V-03** | Sub-section placement (structural weakness) compensated by per-site citations; achieves PASS but with a weaker structural foundation than V-02 |
| 5th | **V-01** | Sub-section, no citations, compact 3 classes — PARTIAL on C-45; falls to 167/168 |

**Recommended golden artifact**: V-05 — it represents the complete pattern: pre-declared standalone violation taxonomy + explicit per-site citation, paralleling the mitigation taxonomy pattern at Phase 0 while adding the drawn-from evidence chain missing from V-02.

---

## Excellence Signals

Patterns from V-05 (top-scoring variation) that made the difference:

**Pattern 1: Violation taxonomy isolated as a named pre-phase block parallel to the mitigation taxonomy**
V-05's Phase 0c stands as a sibling to Phase 0 — both are named pre-phase reference blocks, both define closed vocabularies, both govern behavior across all subsequent phases. The structural parallelism is the mechanism: it gives the violation taxonomy the same enforcement posture as the mitigation taxonomy, converting "format violation" from a label invented at one site into a category drawn from a closed, pre-declared set.

**Pattern 2: Per-site citations link each prohibition to its named taxonomy source**
`"...is a format violation (Phase 0c taxonomy)"` at every prohibition site. This converts the drawn-from relationship from a structural implication into an explicit annotation. Any prohibition site that names a violation type now carries a verifiable pointer to the taxonomy that authorizes that category — the same traceability mechanism that per-site mitigation type annotations provide for the mitigation taxonomy.

**Pattern 3: Vocabulary closure is doubly grounded** (from V-04, present in V-05 as well when combined with the explicit closure declaration)
When a taxonomy block carries an explicit "this list is closed" declaration AND each use site cites the taxonomy by name, the closed-set guarantee is both structurally declared (in the taxonomy block) and behaviorally enforced (at each site). Neither alone is as strong as both together.

---

## Failure Pattern Analysis

**V-01 failure mechanism**: Taxonomy embedded inside Phase 0 lacks structural independence. "Parallel to the Phase 0 mitigation type taxonomy" implies a separate block of equal weight, not a sub-section within Phase 0. Compact 3-class form with no per-site citations provides no drawn-from evidence to compensate. The violation vocabulary is pre-declared but the C-45 structural criterion is only partially met.

**What V-01 would need to reach 168**: Either (a) extract the violation taxonomy into its own Phase 0c block, or (b) add per-site citations establishing drawn-from evidence. Either axis alone would lift C-45 from PARTIAL to PASS.

---

## Regression Check

No regressions detected in any variation. All five variations are additions-only to R15 V-05 — no existing phase text was modified in ways that could destabilize C-01 through C-44, C-46, or C-47. The isolated surgical nature of the changes preserves all prior PASS results.

---

```json
{"top_score": 168, "all_essential_pass": true, "new_patterns": ["violation taxonomy isolated as a named pre-phase block parallel to the mitigation taxonomy — each violation type drawn from a pre-declared closed set rather than named ad hoc at the prohibition site", "per-site citations linking each prohibition to its named taxonomy source — converts implied drawn-from relationship into explicit verifiable annotation at every violation use site"]}
```
