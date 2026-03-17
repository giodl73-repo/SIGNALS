---

## prove-prototype R17 Scorecard

**Rubric**: v16 (329 pts) | **Variations scored**: V-01 through V-05

### Scores

| Variation | C-01–C-42 | C-43 | C-44 | C-45 | **Total** |
|-----------|-----------|------|------|------|-----------|
| V-01 (full combination) | 304 | PASS (6) | PASS (7) | PASS (12) | **329** |
| V-02 (lifecycle emphasis) | 304 | PASS (6) | PASS (7) | PASS (12) | **329** |
| V-03 (role sequence) | 304 | PARTIAL (3) | PASS (7) | PASS (12) | **326** |
| V-04 (output format) | 304 | PARTIAL (3) | PASS (7) | PASS (12) | **326** |
| V-05 (lifecycle + role combined) | 304 | PASS (6) | PASS (7) | PASS (12) | **329** |

**Ranking**: V-01 = V-02 = V-05 (329) > V-03 = V-04 (326)

### C-43 Gap — Why V-03 and V-04 are PARTIAL

The framing paragraph in V-03 and V-04 states **constraints** ("Identification FORBIDDEN in DESIGN") but not **rationale** ("naming the incumbent before the metric is frozen would allow baseline measurement concerns to contaminate scope decisions"). C-43's pass condition requires the framing paragraph to explain *why* each container boundary gates that lifecycle transition. The fail conditions (framing paragraph absent / annotation absent / CALIBRATE sub-transitions absent) are not triggered — both are PARTIAL, not FAIL.

### Excellence Signals

1. **WHY-not-WHAT** is the C-43 differentiator: the framing paragraph needs the reason for each boundary, not just the constraint.
2. **V-05's co-equal thread elevation** makes C-45 convergence architecturally inevitable — parallel structural spines of equal weight create mutual enforcement.
3. **Phase body compression is safe** (V-02): all three new criteria fire on structural marker presence, not instruction verbosity.

```json
{"top_score": 329, "all_essential_pass": true, "new_patterns": ["WHY-not-WHAT in C-43 framing paragraph: C-43 requires the framing paragraph to state rationale for why each container boundary gates that lifecycle transition — naming the contamination risk and isolation purpose — not just constraint language (FORBIDDEN in DESIGN); V-03 and V-04 provide state-to-container enumeration with prohibitions but no rationale, earning PARTIAL", "Co-equal thread elevation as structural enforcement: V-05 gives Thread 1 and Thread 2 equal preamble weight as parallel structural spines, making C-45 multi-criterion terminal discharge architecturally inevitable — both threads are equally declared, so omitting either at CLOSE COMPLETE would be inconsistent with the document opening commitment", "Phase body compression is C-43/C-44/C-45 safe: V-02 demonstrates that compressing phase instructions to minimum expression does not degrade new-criteria scoring; framing paragraph, per-container annotations, Phase 9 prerequisite gate, and thread labels on COMPLETE lines all fire on structural marker presence independent of instruction verbosity"]}
```
