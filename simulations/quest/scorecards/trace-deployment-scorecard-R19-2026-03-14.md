(all 4 phases present but one domain per phase, no domain × phase pairing); **V-03 PASS**: 4×4 grid — 16 sub-questions, every phase × domain combination; **V-04 PASS**: 2-part sub-questions per domain, all 4 phases covered; **V-05 PASS**: "(Domain / Phase)" labeled sub-questions, all 4 phases with multi-domain coverage |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | Path |
|-----------|:---------:|:-----------:|:------------:|:-----:|------|
| V-03 | 60 | 30 | 60 (12 criteria) | **150/250** | Two-stage + basic aspirational |
| V-04 | 60 | 30 | 60 (12 criteria) | **150/250** | Two-stage + basic aspirational |
| V-05 | 60 | 30 | 60 (12 criteria) | **150/250** | Two-stage + basic aspirational |
| V-01 | 60 | 30 | 55 (11 criteria) | **145/250** | Two-stage, C-40 miss |
| V-02 | 60 | 30 | 37.5 (7+1 partial) | **127.5/250** | Two-stage, no disqualifier path |

**Criteria passing per variation:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-09 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-10 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-11 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-13 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-19 | ✓ | ✗ | ✓ | ✓ | ✓ |
| C-20 | ✓ | ✗ | ✓ | ✓ | ✓ |
| C-25 | ✓ | ✗ | ✓ | ✓ | ✓ |
| C-29 | ✓ | ✗ | ✓ | ✓ | ✓ |
| C-37 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-38 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-39 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-40 | ✗ | ~ | ✓ | ✓ | ✓ |
| **Total** | **11** | **7+~** | **12** | **12** | **12** |

---

## Ranking

1. **V-03, V-04, V-05 — tied at 150/250**
   - Rank tiebreaker by C-40 implementation strength: V-03 (4×4 = 16 sub-questions) > V-05 (8 labeled by phase+domain) > V-04 (8 with 2 sub-parts)
2. **V-01 — 145/250**: C-40 miss is the sole differentiator; sub-questions cover 3 of 4 phases (post-validate absent)
3. **V-02 — 127.5/250**: Missing the entire disqualifier block (C-19/C-20/C-25/C-29); table-anchoring format does not automatically activate the "'Add monitoring' does not qualify" pattern

---

## Why V-02 Scored Lowest

V-02's table-anchoring design enforced structural coverage well (C-37–C-40 all activate) but stripped the disqualifier vocabulary out of the automation hooks fill rule. Every other variation carried `"Add monitoring" does not qualify` or equivalent — that single phrase fires C-19, C-20, C-25, and C-29 simultaneously (20 pts). V-02 replaced it with a specification: `"Each hook references a specific tool, pipeline stage, or named check."` A specification tells the model what to write; a disqualifier names what fails. Only the latter activates the rubric block.

---

## Why V-01 Scored Below the V-03/V-04/V-05 Cluster

V-01's four domain sub-questions mapped one domain per phase (Commerce → pre-deploy, Infrastructure → sequence, Data → sequence, Security → rollback). Post-validate phase received no sub-question. C-40's pass condition explicitly requires `"domain-specific post-deploy layer checks"` — a missed phase fails outright, not partially. The fix is sub-question labeling: once you write `"(Commerce / PRE-DEPLOY)"` you are forced to choose a phase, and the choice reveals phase gaps in the set.

---

## Why 200/250 Was Not Reached

All five variations implement the two-stage block (C-37–C-40) cleanly, worth +20 pts on any base path. The 200/250 ceiling requires those +20 to stack on the **prose structural-adoption base** (180 pts), which requires:
- C-12: status-quo baseline in role block
- C-14: front-loaded empty gap skeleton before Phase 1
- C-21: colloquial interrogative phase headers
- C-26: interrogative headers as structural anchors
- C-15: prose-instruction saturation (depends on C-12)
- C-33/C-34: joint prose-path adoption ceiling

None of the R19 variations implemented these. All five used formal phase headers (`PHASE 1 — PRE-DEPLOY CHECKS TABLE`, `DIRECTIVE 1`, etc.) and placed the FINDINGS TABLE after Stage 2 sub-questions rather than as an upfront empty skeleton. The two-stage architecture and the prose structural-adoption architecture are orthogonal and additive — R19 confirmed the two-stage block works; R20 target is to combine it with interrogative headers + front-loaded skeleton + C-12 baseline.

---

## Excellence Signals (from V-03/V-04/V-05)

1. **`"Add monitoring" does not qualify`** in the AUTOMATION HOOKS fill rule fires four aspirational criteria (C-19, C-20, C-25, C-29) at zero structural cost — one sentence, 20 pts.
2. **Phase × domain labeled sub-questions** (`"Sub-question 1a (Commerce / PRE-DEPLOY)"`) guarantee C-40 passes all four phases; any sub-question that omits phase labeling creates a systematic gap (V-01's post-validate miss).
3. **Dual fill mandate in FINDINGS**: `"≥1 row per domain AND ≥1 row per phase"` (V-05) is the strongest C-38 expression — it forces a 4×4 coverage expectation and the explanatory note `"if all gaps land in one domain or one phase, sub-questions were not fully answered"` directly satisfies the cross-domain comparison mandate.
4. **Stage 2 vocabulary in Stage 2's role block** (not distributed per-phase) keeps C-11 cleanly activated regardless of Stage 1's vocabulary architecture.

---

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["phase-domain-pair-sub-question-notation: Stage 2 sub-questions labeled by explicit (Domain / Phase) pairs guarantee C-40 coverage across all four phases; domain-only sub-questions without phase labels create systematic post-validate gaps", "two-stage-only-path-ceiling: two-stage role block without prose structural-adoption infrastructure (C-12 status-quo baseline, C-14 front-loaded skeleton, C-21 interrogative headers) achieves ~150/250 regardless of sub-question density; the +20 from C-37–C-40 stacks only on prose structural-adoption base — R20 target is interrogative headers plus front-loaded skeleton plus two-stage combined"]}
```
