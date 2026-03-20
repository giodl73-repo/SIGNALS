# /quest:score — specify-abstract R2

## Scoring Method

No trace artifact available. Scoring from skill description and variation text.

**Baseline assumption**: Standard Phase 5 amendment exists but is not hardened. V-01 adds Before/After + non-triviality guard to Phase 5 only. V-02 adds dual-pass structure (Pass A completeness, Pass B precision). V-03 adds gap-first ordering + constraint reasoning. V-04 extends Phase 1 to quote-level extraction. V-05 reduces draft strictness, extends Phase 5 to 4 hardened amendments with Before/After.

---

## Per-Criterion Scorecard

| Criterion | Max | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| C-01 Six-part structure | 10 | 10 | 10 | 10 | 10 | 10 |
| C-02 Word count within target | 10 | 10 | 10 | 10 | 10 | 10 |
| C-03 Artifact written to correct path | 10 | 10 | 10 | 10 | 10 | 10 |
| C-04 Gap framed as gap, not goal | 10 | 10 | 10 | 10 | 10 | 10 |
| C-05 Signal acquisition executed | 10 | 10 | 10 | 10 | 10 | 10 |
| C-06 Result section is quantified | 10 | 10 | 10 | 5 | 10 | 10 |
| C-07 Amendment pass: 3 distinct changes | 10 | 10 | 5 | 5 | 5 | 10 |
| C-08 Journal variant applied correctly | 10 | 10 | 10 | 10 | 10 | 10 |
| C-09 Claim uses correct tense | 4 | 2 | 4 | 2 | 2 | 2 |
| C-10 Abstract reads as coherent prose | 4 | 2 | 2 | 2 | 2 | 4 |
| C-11 Constraint reasoning stated | 4 | 0 | 0 | 4 | 0 | 0 |
| C-12 Connective bridges pre-merge | 4 | 0 | 0 | 0 | 0 | 0 |
| C-13 Amendment non-triviality guard | 2 | 2 | 0 | 0 | 0 | 2 |
| C-14 Gap drafted first | 2 | 0 | 0 | 2 | 0 | 0 |
| **TOTAL** | **100** | **86** | **81** | **80** | **79** | **88** |

---

## Evidence Notes

**C-06**:
- V-01/V-05: Amendment 2 explicitly targets "add a number if missing" → PASS.
- V-02: Pass B precision check requires "number, percentage, effect size, or explicit qualitative strength word" → PASS.
- V-04: Numbers surface in Phase 1 quote extraction and flow forward → PASS.
- V-03: Baseline Phase 2 instructs quantification but no enforcement mechanism added by variation → PARTIAL.

**C-07**:
- V-01: Explicit Before/After + non-triviality guard for all 3 slots → PASS.
- V-05: 4 amendments all with Before/After → exceeds requirement, PASS.
- V-02/V-03/V-04: Standard amendment phase retained but not hardened → PARTIAL.

**C-09**:
- V-02 exclusively: Pass B includes explicit check — "Does it use past tense for empirical ('we found') or present tense for theoretical ('we show')?" with paper-type identification. Only variation to enforce this → PASS.
- All others: Baseline claim instruction exists but no explicit tense enforcement → PARTIAL.

**C-10**:
- V-05 exclusively: 4th amendment explicitly targets prose coherence → PASS.
- V-02: Dual-pass risks mechanical output (noted in variation hypothesis) → PARTIAL.
- All others: No explicit prose coherence mechanism → PARTIAL.

**C-11**: V-03 only. Adds one-sentence *why* for each section constraint. All others → FAIL.

**C-12**: No variation adds connective bridge composition step before merge. Universal FAIL. Persistent gap from R1.

**C-13**: V-01 and V-05 only. Both add non-triviality guard ("if N, rewrite After"). V-02/V-03/V-04 → FAIL.

**C-14**: V-03 only. Gap-first ordering grounds Background. All others write in Background-first order → FAIL.

---

## Golden Threshold Check

All essential pass = C-01 through C-05 all PASS for a given variation.

| Variation | All Essential? | Composite | Golden? |
|-----------|---------------|-----------|---------|
| V-01 | YES | 86 | GOLDEN |
| V-02 | YES | 81 | GOLDEN |
| V-03 | YES | 80 | GOLDEN (exact) |
| V-04 | YES | 79 | NOT GOLDEN — 1 point short |
| V-05 | YES | 88 | GOLDEN |

V-04 misses by 1 point. C-07 PARTIAL is the deciding gap — V-04 extends Phase 1 but leaves Phase 5 standard. If V-04 had inherited V-01's hardened Phase 5, it would score 84.

---

## Ranking

1. **V-05** — 88. Quality load shifted to amendment phase. 4th amendment directly targets prose coherence. Before/After on all amendments.
2. **V-01** — 86. Hardened amendment phase. Amendment 2 catches C-06. Minimal change, high payoff.
3. **V-02** — 81. Strongest C-09 (explicit tense check). C-10 risk from mechanical dual-pass reduces prose score.
4. **V-03** — 80. Uniquely covers C-11 and C-14. Weak on amendment criteria.
5. **V-04** — 79. Strongest C-05. Phase 1 rigor doesn't compensate for missing amendment hardening.

---

## Excellence Signals from V-05

**Signal 1 — Amendment-over-draft-discipline**: Permissive fast draft + hardened amendment phase outperforms constrained draft + standard amendment. Each phase has one job: Phase 2 gets coverage, Phase 5 gets correctness. Removing self-correction overhead from Phase 2 lets the model write faster without conflating completeness and precision.

**Signal 2 — Prose-coherence-as-amendment-target**: V-05 is the only variation to treat prose coherence as an explicit amendment (not a side effect of merge). The 4th amendment slot makes it a named target rather than hoped-for emergent quality. This is the mechanism that earns C-10 PASS.

**R3 candidate**: V-03 + V-01 combination (gap-first + constraint reasoning during draft, hardened Before/After amendment phase). Covers C-11 + C-14 from V-03, C-07 + C-13 from V-01, and would score approximately 90 if C-06 is also handled by Amendment 2. C-12 (connective bridges) remains the persistent unaddressed criterion across all R2 variations — it needs an explicit Phase step, not a criterion retrofit.

---

```json
{"top_score": 88, "all_essential_pass": true, "new_patterns": ["amendment-over-draft-discipline", "fourth-amendment-prose-coherence"]}
```
