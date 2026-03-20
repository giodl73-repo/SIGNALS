Scorecard written to `simulations/quest/scorecards/simulate-derivation-scorecard-R2-2026-03-20.md`.

---

## Round 2 Results Summary

**Top score: 110/115 (V-05) — Exemplary**  
**All essential pass: YES (all 5 variations)**

| Rank | Variation | Score | Band |
|------|-----------|-------|------|
| 1 | V-05 (all three axes) | 110/115 | Exemplary |
| 2 | V-04 (fault attribution + step expansion) | 103/115 | Exemplary |
| 3 | V-03 (prose-per-check) | 100/115 | Exemplary |
| 4 | V-01 (fault attribution) | 98/115 | Proficient |
| 4 | V-02 (step expansion) | 98/115 | Proficient |

**R2 progress vs R1:** Every R2 aspirational criterion is now solvable. All five that scored 0 in R1 (C-09, C-10) or were new (C-11, C-12, C-13) reach 5/5 in the variation that targets them.

**The ceiling bet held.** V-05 outperforms V-04 by 7 points — the three axes genuinely don't interfere with each other at prompt execution.

**Three new excellence signals from V-05:**

1. **own-words-gate** — `"[state explicitly]"` vs `"in the tracer's own words -- do not merely quote the paper"` is the exact phrase boundary between C-11 PARTIAL and PASS. V-01/V-02/V-04 miss it; V-03/V-05 catch it.

2. **three-axis-no-degradation** — Confirmed that stacking all three axes doesn't degrade any individual criterion. The 7-point gap between V-04 and V-05 is clean attribution to C-11 and C-13.

3. **prose-rule-synergy** — Uniform bare-YES/NO prohibition closes a behavioral inconsistency: APPROX blocks already required prose in the base, but primary checks didn't. That inconsistency was a token-budget leak. V-03/V-05 seal it.

**Residual gap for R3:** C-07 misses 2 pts across all variations — one line fixing the P1/P2 priority rule in Phase 4 would push the ceiling to **112/115**.

```json
{"top_score": 110, "all_essential_pass": true, "new_patterns": ["own-words-gate: adding in-the-tracers-own-words gate to APPROX sub-block moves C-11 from PARTIAL to PASS; [state explicitly] alone is insufficient because LLM can satisfy it by paraphrasing the source", "three-axis-no-degradation: combining Phase 1b step expansion, source acknowledgment gate, and prose-per-check in V-05 does not cause phase-dropping; all three axes hold simultaneously confirming structural independence at prompt level", "prose-rule-synergy: applying bare-YES/NO prohibition uniformly to all primary checks creates stylistic consistency that elevates APPROX block quality as side effect -- inconsistency between prose-required APPROX and bare-allowed primary checks is a token-budget leak"]}
```
prose-per-check rule; bare YES/NO permitted for algebraic, dimensional, sign checks |

**V-01 Total: 98 / 115 -- Proficient**

---

### V-02 -- Step Resolution: Compressed-Step Expansion

**Axis**: Phase 1b expansion pass with (interpolated) sub-step notation

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 Derivation map complete | PASS | 12/12 | Phase 1 table; Phase 1b expands rows without breaking completeness |
| C-02 Verification block per step | PASS | 12/12 | Phase 2 covers all steps including interpolated sub-steps; same block format |
| C-03 Every APPROX flagged | PASS | 12/12 | APPROX sub-block with (a)/(b)/(c) in verification block, same as V-01 |
| C-04 Fault register present | PASS | 12/12 | Phase 3 with P1/P2/P3; no NEW tagging (V-02 does not add source acknowledgment axis) |
| C-05 Artifact frontmatter | PASS | 12/12 | Write path and fields specified |
| C-06 Global soundness verdict | PASS | 10/10 | Phase 4 summary section |
| C-07 Amend maps to faults | PARTIAL | 8/10 | Same format as V-01; no P1/P2 priority rule |
| C-08 Step types classified | PARTIAL | 7/10 | Same as V-01 -- APPROX rich, EXACT/PHYSICAL under-specified |
| C-09 Catches fault not in paper | FAIL | 0/5 | No source acknowledgment gate; no NEW tagging in Phase 3 |
| C-10 Expands compressed steps | PASS | 5/5 | Phase 1b requires scanning for compressed steps, S-NNa/S-NNb notation, "(interpolated)" label, no-compressed-steps auto-pass note -- hits rubric pass condition precisely |
| C-11 APPROX verified independently | PARTIAL | 3/5 | "[state explicitly]" present but no "own words" gate |
| C-12 Severity labels inline in Amend | PASS | 5/5 | [F-ID] [P1/P2/P3] in Amend format |
| C-13 Verification blocks contain prose | FAIL | 0/5 | No prose-per-check rule |

**V-02 Total: 98 / 115 -- Proficient**

---

### V-03 -- Prose-per-Check Verification

**Axis**: YES -- [sentence] required for every check token; bare YES/NO prohibited

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 Derivation map complete | PASS | 12/12 | Phase 1 table; standard |
| C-02 Verification block per step | PASS | 12/12 | Per-step block with mandatory prose rule applied to all checks |
| C-03 Every APPROX flagged | PASS | 12/12 | APPROX sub-block with (a)/(b)/(c); prose format extends into APPROX block |
| C-04 Fault register present | PASS | 12/12 | Phase 3 with P1/P2/P3; no NEW tagging (V-03 does not add source acknowledgment axis) |
| C-05 Artifact frontmatter | PASS | 12/12 | Write path and fields specified |
| C-06 Global soundness verdict | PASS | 10/10 | Phase 4 summary section |
| C-07 Amend maps to faults | PARTIAL | 8/10 | [F-ID] [P1/P2/P3]: [fix] format; no explicit P1/P2 priority rule |
| C-08 Step types classified | PARTIAL | 7/10 | Same as V-01/V-02 -- APPROX rich, EXACT/PHYSICAL under-specified |
| C-09 Catches fault not in paper | FAIL | 0/5 | No source acknowledgment gate; no NEW tagging |
| C-10 Expands compressed steps | FAIL | 0/5 | No Phase 1b |
| C-11 APPROX verified independently | PASS | 5/5 | APPROX sub-block says "in the tracer's own words -- do not merely quote the paper" for both (a) and (b) -- only single-axis variation with this gate; satisfies C-11 pass condition fully |
| C-12 Severity labels inline in Amend | PASS | 5/5 | [F-ID] [P1/P2/P3] in Amend |
| C-13 Verification blocks contain prose | PASS | 5/5 | "Reasoning rule -- applies to all checks: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning." Explicit, universal, non-optional |

**V-03 Total: 100 / 115 -- Exemplary**

---

### V-04 -- Combined: Fault Attribution + Step Expansion

**Axes**: V-01 (source acknowledgment gate + NEW tag) + V-02 (Phase 1b expansion pass)

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 Derivation map complete | PASS | 12/12 | Phase 1 table; Phase 1b adds sub-steps without displacing rows |
| C-02 Verification block per step | PASS | 12/12 | Per-step block including interpolated sub-steps; "do not abbreviate" inherited |
| C-03 Every APPROX flagged | PASS | 12/12 | APPROX sub-block with (a)/(b)/(c) |
| C-04 Fault register present | PASS | 12/12 | Phase 3 with P1/P2/P3 and NEW tagging |
| C-05 Artifact frontmatter | PASS | 12/12 | Write path and fields specified |
| C-06 Global soundness verdict | PASS | 10/10 | Phase 4 summary section |
| C-07 Amend maps to faults | PARTIAL | 8/10 | [F-ID] [P1/P2/P3] format; no P1/P2 priority rule |
| C-08 Step types classified | PARTIAL | 7/10 | Same as V-01/V-02 |
| C-09 Catches fault not in paper | PASS | 5/5 | Source acknowledgment gate for WEAK/BROKEN + Phase 3 NEW tagging both present |
| C-10 Expands compressed steps | PASS | 5/5 | Phase 1b with S-NNa/S-NNb and "(interpolated)" label |
| C-11 APPROX verified independently | PARTIAL | 3/5 | Has "[state explicitly]" prose guidance but no "in your own words" gate |
| C-12 Severity labels inline in Amend | PASS | 5/5 | [F-ID] [P1/P2/P3] in Amend |
| C-13 Verification blocks contain prose | FAIL | 0/5 | No prose-per-check rule -- V-03 axis not included |

**V-04 Total: 103 / 115 -- Exemplary**

---

### V-05 -- Combined: All Three Axes

**Axes**: V-01 (fault attribution) + V-02 (step expansion) + V-03 (prose-per-check)

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 Derivation map complete | PASS | 12/12 | Phase 1 table; Phase 1b adds without breaking completeness |
| C-02 Verification block per step | PASS | 12/12 | Per-step block including interpolated sub-steps; prose rule adds depth |
| C-03 Every APPROX flagged | PASS | 12/12 | APPROX sub-block with (a)/(b)/(c); prose-per-check rule extends consistently |
| C-04 Fault register present | PASS | 12/12 | Phase 3 with P1/P2/P3 and NEW tagging |
| C-05 Artifact frontmatter | PASS | 12/12 | Write path and fields specified |
| C-06 Global soundness verdict | PASS | 10/10 | Phase 4 summary section |
| C-07 Amend maps to faults | PARTIAL | 8/10 | [F-ID] [P1/P2/P3] format; no explicit P1/P2 priority rule -- single remaining gap across all R2 variations |
| C-08 Step types classified | PARTIAL | 7/10 | APPROX type rich with "own words" gate; EXACT/PHYSICAL still under-specified |
| C-09 Catches fault not in paper | PASS | 5/5 | Source acknowledgment gate for WEAK/BROKEN + Phase 3 NEW tagging |
| C-10 Expands compressed steps | PASS | 5/5 | Phase 1b with S-NNa/S-NNb and "(interpolated)" |
| C-11 APPROX verified independently | PASS | 5/5 | APPROX sub-block says "in the tracer's own words -- do not merely quote the paper"; prose-per-check rule reinforces this -- strongest possible C-11 signal |
| C-12 Severity labels inline in Amend | PASS | 5/5 | [F-ID] [P1/P2/P3] in Amend |
| C-13 Verification blocks contain prose | PASS | 5/5 | "Reasoning rule -- applies to all checks: Do not write a bare YES or NO." Explicit, universal |

**V-05 Total: 110 / 115 -- Exemplary**

---

## Ranking

| Rank | Variation | Score | All Essential Pass? | Band | Notes |
|------|-----------|-------|---------------------|------|-------|
| 1 | **V-05** | **110/115** | YES | Exemplary | Ceiling test held; all three axes stack without degradation |
| 2 | **V-04** | **103/115** | YES | Exemplary | C-09 + C-10 recovered; C-13 absent costs 5 pts |
| 3 | **V-03** | **100/115** | YES | Exemplary | C-11 + C-13 recovered; C-09 + C-10 absent costs 10 pts |
| 4 | **V-01** | **98/115** | YES | Proficient | C-09 recovered; C-10, C-13 absent; C-11 partial |
| 4 | **V-02** | **98/115** | YES | Proficient | C-10 recovered; C-09, C-13 absent; C-11 partial |

---

## Per-criterion R1 vs R2 progression

| Criterion | R1 best | R2 best variation | R2 score |
|-----------|---------|-------------------|---------|
| C-09 | 0/5 (none) | V-01, V-04, V-05 | 5/5 SOLVED |
| C-10 | 0/5 (none) | V-02, V-04, V-05 | 5/5 SOLVED |
| C-11 | n/a (new) | V-03, V-05 | 5/5 SOLVED |
| C-12 | n/a (new) | All variations | 5/5 SOLVED |
| C-13 | n/a (new) | V-03, V-05 | 5/5 SOLVED |

All five R2 aspirational criteria are solvable. V-05 earns 4 of 5 individually.

---

## Residual Gap: C-07 (2 pts left on table across all variations)

No R2 variation adds the explicit P1/P2 priority rule to the Amend instruction. Fix: add one line to Phase 4:
"If P1 faults exist, the first fix must cite a P1. If P2 faults exist, at least one fix must cite a P2."
Combined with V-05 base, this pushes the ceiling to 112/115.

---

## Excellence Signals from V-05

1. **own-words-gate** -- Adding "in the tracer's own words -- do not merely quote the paper" to the APPROX sub-block instruction moves C-11 from PARTIAL to PASS. The distinction between "[state explicitly]" (V-01/V-02/V-04) and "in your own words -- do not merely quote" (V-03/V-05) is the precise gate that unlocks independent validity reasoning. Without it, the LLM can satisfy the letter of the instruction by paraphrasing the source.

2. **three-axis-no-degradation** -- The V-05 ceiling test confirms that Phase 1b (step expansion), source acknowledgment gate, and prose-per-check do not compete for execution bandwidth. All three hold simultaneously; V-05 outperforms V-04 by 7 points, confirming structural independence at the prompt level.

3. **prose-rule-synergy** -- The reasoning rule applied uniformly to all primary checks also elevates APPROX sub-block quality (C-11) because the block is now stylistically consistent. In V-01/V-02/V-04, the APPROX block requires prose but primary checks do not -- a behavioral inconsistency that gives the LLM implicit license to reduce reasoning elsewhere. V-03/V-05 close this leak.

---

```json
{"top_score": 110, "all_essential_pass": true, "new_patterns": ["own-words-gate: adding in-the-tracers-own-words gate to APPROX sub-block moves C-11 from PARTIAL to PASS; [state explicitly] alone is insufficient because LLM can satisfy it by paraphrasing the source", "three-axis-no-degradation: combining Phase 1b step expansion, source acknowledgment gate, and prose-per-check in V-05 does not cause phase-dropping; all three axes hold simultaneously confirming structural independence at prompt level", "prose-rule-synergy: applying bare-YES/NO prohibition uniformly to all primary checks creates stylistic consistency that elevates APPROX block quality as side effect -- inconsistency between prose-required APPROX and bare-allowed primary checks is a token-budget leak"]}
```
