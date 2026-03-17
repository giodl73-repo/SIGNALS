**Scout-Requirements R2 Scorecard** written to `simulations/quest/scorecards/scout-requirements-scorecard-R2-2026-03-14.md`.

---

## Results Summary

| Rank | Variation | Score | Band |
|------|-----------|-------|------|
| 1 | **V-05 Full Synthesis** | **122/122** | Golden |
| 2 | V-02 Structural Closure Phrasing | 120/122 | Golden |
| 3 | V-03 Per-Law Independent Chains | 119/122 | Golden |
| 3 | V-04 C-21 + C-22 Combination | 119/122 | Golden |
| 5 | V-01 Charter Self-Naming | 118/122 | Golden |

**V-05 is the first perfect score (122/122) in this series.**

---

**Key findings vs predictions:**

Predictions ran 1–2 pts high for V-01..V-04. The calibration error was **C-22**: all predictions credited PASS when the Prevention-Detection Complementarity paragraph was present (the sentence matches the C-22 example verbatim). Actual scoring requires the charter to *perform* ownership ("This charter names X as a structural obligation before execution begins"), not just *describe* the relationship. V-01/V-02/V-03 describe; V-04/V-05 own.

**Three new patterns from R2:**

1. **Named design contract** — `"chartered here as a design contract, not inferred from structural proximity"` enacts C-22; the Prevention-Detection paragraph only describes it (C-20 level)
2. **Independence inside closure** — C-23 (per-law splits) and C-24 (unified closure) resolve by nesting independence as the *structure* of the closure, not its alternative
3. **Logical necessity vs prohibition** — `"simultaneously instantiates as necessary consequences"` is self-enforcing through structural incompleteness; `"contradicts this charter's structure"` requires an external enforcer

```json
{"top_score": 122, "all_essential_pass": true, "new_patterns": ["named design contract over structural description -- the charter must *perform* ownership ('chartered here as a named obligation') not just *describe* the relationship; sentence presence achieves C-20, performative ownership achieves C-22", "independence inside closure -- per-law independent enforcement chains (C-23) and unified structural closure (C-24) resolve by treating independence as the internal structure of the meta-declaration, not its alternative; independence operates at the law level, closure at the meta level", "logical necessity vs external prohibition -- 'simultaneously instantiates as necessary consequences' makes Loop 2 structurally required by Loop 1's declaration; 'contradicts this charter's structure' is external enforcement; necessity is self-enforcing through logical incompleteness"]}
```
ediction vs actual**: Off by 1. Prediction likely credited C-22 as PASS due to verbatim sentence match. Rubric distinction: C-22's pass condition requires charter ownership ("named obligation before execution begins"), not just sentence presence. The Prevention-Detection paragraph describes the relationship; V-04/V-05's dedicated Design Contract section owns it.

---

### V-02 -- Structural Closure Phrasing
**Score: 120/122 -- Golden** (predicted: 121, delta -1)

| C | Rating | Evidence |
|---|--------|----------|
| C-01..C-20 | PASS (114) | Inherited. |
| C-21 | PASS (2) | Header: "This charter is C-17 (Loop 1 / declare)." Bullets: "C-17 (Loop 1 / declare)", "C-18 (Loop 2 / apply)", "C-19 (Loop 3 / verify)". Criterion IDs assigned; recursive naming satisfies C-21. |
| C-22 | PARTIAL (1) | Prevention-Detection paragraph unchanged from V-01. Sentence present; charter ownership not performed. |
| C-23 | PARTIAL (1) | Single unified meta-requirement. No per-law chains. |
| C-24 | PASS (2) | Structural Closure paragraph delivers the required language: "Asserting C-17 simultaneously instantiates C-18 as its necessary application consequence: the act of declaring laws (C-17) constitutes the obligation to apply them (C-18)... Asserting C-17 simultaneously brings C-18 and C-19 into existence as logical consequences." The three-loop system is described as "a single self-closing declaration where Loop 1 is the only incomplete loop." Full C-24 pass. |

**Decisive strength**: C-24 language is the cleanest structural closure in R2 -- "simultaneously instantiates... as necessary consequences" directly satisfies the rubric's pass condition. Missing only C-22 (named contract) and C-23 (per-law independence).

---

### V-03 -- Per-Law Independent Chains
**Score: 119/122 -- Golden** (predicted: 121, delta -2)

| C | Rating | Evidence |
|---|--------|----------|
| C-01..C-20 | PASS (114) | Inherited. |
| C-21 | PASS (2) | Meta-Requirement section assigns "C-17 (Loop 1 / declare) = this charter", "C-18 (Loop 2 / apply) = step-level cross-references (per-law)", "C-19 (Loop 3 / verify) = pre-output verification protocol." Criterion IDs present in the unified meta-requirement. |
| C-22 | PARTIAL (1) | Prevention-Detection paragraph: "C-18 (Loop 2 across both chains) creates the execution artifacts -- inline [AMBIG:] notations (Law A) and closure sentences (Law B) -- that C-19 (Loop 3) requires as evidence." Same factual-description pattern as V-01/V-02. Not chartered as named obligation. |
| C-23 | PASS (2) | Explicit "Law A Independent Enforcement Chain" (C-17-A, C-18-A, C-19-A) and "Law B Independent Enforcement Chain" (C-17-B, C-18-B, C-19-B). Non-cascade statements: "a failure in C-18-A cannot cascade to Law B's enforcement." Each law has its own declare/apply/verify triplet; chains are structurally isolated. |
| C-24 | FAIL (0) | Non-skippability phrased as prohibition: "Satisfying C-17 while skipping C-18-A contradicts Law A's chain." Per-law framing is closer (the contradiction is localized to each chain) but "contradicts" is still prohibition, not logical necessity. C-24 requires "simultaneously instantiates as necessary consequences." |

**Prediction vs actual**: Off by 2. Prediction likely credited both C-22 (PASS, +1) and possibly partial C-24 (+1). Under strict reading, C-22 requires charter ownership (V-03 describes but doesn't own), and C-24 requires simultaneous instantiation (V-03 says "contradicts").

---

### V-04 -- C-21 + C-22 Combination
**Score: 119/122 -- Golden** (predicted: 121, delta -2)

| C | Rating | Evidence |
|---|--------|----------|
| C-01..C-20 | PASS (114) | Inherited. |
| C-21 | PASS (2) | Bullets: "C-17 (Loop 1 / declare)", "C-18 (Loop 2 / apply)", "C-19 (Loop 3 / verify)". Non-skippability names C-17 as declaring C-18 as apply layer. Criterion IDs present. |
| C-22 | PASS (2) | Dedicated "### Loop 2 -> Loop 3 Design Contract" section with: "This charter names the following as a structural obligation before execution begins: C-18 (Loop 2) creates the execution artifacts that C-19 (Loop 3) requires as evidence." Charter explicitly owns the dependency as a named obligation -- this is the C-22 pass form. |
| C-23 | PARTIAL (1) | The Design Contract differentiates Law A and Law B artifacts ("Law A's C-18 (Loop 2) creates inline [AMBIG:] notations... Law B's C-18 (Loop 2) creates closure sentences"), but the enforcement structure remains a unified Three-Loop Meta-Requirement. No independent C-17-A/B declare triplets. One chain's failure can still cascade. |
| C-24 | FAIL (0) | Non-skippability: "A model that satisfies C-17 while skipping C-18 contradicts this charter's structure." Prohibition language, not structural closure. |

**Decisive strength**: The "Loop 2 -> Loop 3 Design Contract" subsection with "This charter names... as a structural obligation before execution begins" is the exact C-22 pass form -- the first variation to explicitly perform charter ownership rather than describe the relationship. V-04 closes C-21 and C-22 but leaves C-23 and C-24.

**Prediction vs actual**: Off by 2. Prediction credited C-23 as having gained more from per-law differentiation inside the Design Contract. Under strict C-23 reading, differentiating artifact types inside a unified chain is not the same as independent declare/apply/verify triplets (C-23 requires isolated chains where one's failure cannot cascade).

---

### V-05 -- Full Synthesis
**Score: 122/122 -- Golden** (predicted: 122, delta 0) CORRECT

| C | Rating | Evidence |
|---|--------|----------|
| C-01..C-20 | PASS (114) | Inherited. |
| C-21 | PASS (2) | Per-law sub-IDs (C-17-A, C-18-A, C-19-A, C-17-B, C-18-B, C-19-B) plus unified meta-requirement "C-17 (Loop 1 / declare)", "C-18 (Loop 2 / apply)", "C-19 (Loop 3 / verify)". Criterion IDs at both per-law and unified levels. |
| C-22 | PASS (2) | Dedicated "### Loop 2 -> Loop 3 Design Contract" section: "This dependency is chartered here as a design contract, not inferred from structural proximity." Verbatim charter ownership. Specifies per-law artifact creation: Law A's C-18-A creates [AMBIG:] notations; Law B's C-18-B creates closure sentences. C-19 audits these specific artifacts. |
| C-23 | PASS (2) | "Law A Independent Enforcement Chain" (C-17-A, C-18-A, C-19-A) and "Law B Independent Enforcement Chain" (C-17-B, C-18-B, C-19-B) with non-cascade statements: "a failure in C-18-A cannot cascade to Law B's enforcement." Independent triplets for each law; each chain's failure is isolated. |
| C-24 | PASS (2) | Structural Closure section: "C-17 is structurally incomplete without C-18. Declaring format laws without an application layer is not enforcement -- it is an incomplete declaration. Asserting C-17 simultaneously instantiates C-18 (both Law A's C-18-A and Law B's C-18-B) as necessary consequences... Asserting C-17 simultaneously brings C-18 and C-19 into existence as logical consequences." The per-law split is resolved inside the unified closure: independence is the structure of the meta-declaration, not its alternative. |

**Decisive strength**: V-05 resolves the apparent tension between C-23 (per-law independence requires splitting) and C-24 (unified closure requires unity) by nesting independence inside closure: the unified meta-requirement is the self-closing declaration; the per-law chains are its named independent components. Independence lives inside the closure.

---

## Ranking

| Rank | Variation | Score | Band | Criteria Closed |
|------|-----------|-------|------|-----------------|
| 1 | V-05 Full Synthesis | **122/122** | Golden | C-21, C-22, C-23, C-24 |
| 2 | V-02 Structural Closure Phrasing | **120/122** | Golden | C-21, C-24 |
| 3 | V-03 Per-Law Independent Chains | **119/122** | Golden | C-21, C-23 |
| 3 | V-04 C-21 + C-22 Combination | **119/122** | Golden | C-21, C-22 |
| 5 | V-01 Charter Self-Naming | **118/122** | Golden | C-21 |

---

## Key Findings

**C-21 closes universally.** Every R2 variation adds rubric criterion IDs to the meta-requirement bullet points. All five score PASS on C-21. The base gap (PARTIAL, 1 pt) is fully closed in R2 for all variations.

**C-22 requires charter ownership, not sentence presence.** V-01/V-02/V-03 all have the required sentence matching the C-22 example verbatim but score PARTIAL. The pass condition distinguishes *existing in the design* (C-20 level) from *the charter owning it as a named obligation* (C-22 level). The magic phrase is "This charter names the following as a structural obligation before execution begins" (V-04) or "chartered here as a design contract, not inferred from structural proximity" (V-05). Mere sentence presence at the description level achieves C-20; the performative act of naming it an obligation achieves C-22.

**C-23 and C-24 are axis-specific.** No single-axis variation closes both. V-03 gets C-23 by splitting into per-law chains; V-02 gets C-24 by the structural closure paragraph. Both require distinct changes that neither subsumes the other. V-05 synthesizes both by placing the per-law independent chains *inside* the unified self-closing meta-declaration.

**The C-23/C-24 resolution is the R2 architectural insight.** Per-law independence (C-23) appears to conflict with unified structural closure (C-24): splitting creates independence; unity creates closure. V-05 resolves this by treating the meta-requirement as the closure unit (C-24 passes at the meta level) while the per-law chains are its named independent components (C-23 passes at the law level). Independence is the *structure* of the unified closure, not its antithesis.

**Prediction calibration**: All four single/dual-axis predictions were over by 1-2 pts because they credited C-22 as PASS when the Prevention-Detection paragraph is present. Under rubric, C-22 requires the charter to perform ownership, not describe the relationship. V-05 prediction was exact.

---

## Excellence Signals

Patterns from V-05 not present in prior rounds:

1. **Named design contract over structural description** -- The "Loop 2 -> Loop 3 Design Contract" section performs charter ownership explicitly: "This dependency is chartered here as a design contract, not inferred from structural proximity." Prior variations described the relationship (C-20 level); V-04/V-05 own it as an obligation (C-22 level). The key phrase enacts the contract; it doesn't describe it.

2. **Independence inside closure** -- Per-law independent enforcement chains (C-23) nested inside a single self-closing meta-declaration (C-24). The tension between splitting (independence) and unity (closure) resolves when independence is treated as the internal structure of the unified declaration. Closure operates at the meta level; independence operates at the law level.

3. **Logical necessity vs external prohibition for non-skippability** -- "Asserting C-17 simultaneously instantiates Loops 2 and 3 as necessary consequences" (C-24 pass form) vs "satisfying C-17 while skipping C-18 contradicts this charter's structure" (prohibition form). Prohibition requires an external enforcer to check for the contradiction; logical necessity makes the declaration structurally incomplete without its consequences. A model cannot satisfy a logically incomplete declaration without instantiating its necessary consequences.

---

```json
{"top_score": 122, "all_essential_pass": true, "new_patterns": ["named design contract over structural description -- the charter must *perform* ownership ('chartered here as a named obligation') not just *describe* the relationship; sentence presence achieves C-20, performative ownership achieves C-22", "independence inside closure -- per-law independent enforcement chains (C-23) and unified structural closure (C-24) resolve by treating independence as the internal structure of the meta-declaration, not its alternative; independence operates at the law level, closure at the meta level", "logical necessity vs external prohibition -- 'simultaneously instantiates as necessary consequences' makes Loop 2 structurally required by Loop 1's declaration; 'contradicts this charter's structure' is external enforcement; necessity is self-enforcing through logical incompleteness"]}
```
