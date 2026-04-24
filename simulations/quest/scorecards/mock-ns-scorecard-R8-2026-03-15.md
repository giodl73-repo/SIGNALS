## mock-ns Round 8 -- Scorecard

### Pre-scoring: Constant criteria across all variants

All five variations share the same setup (S-1), category (S-2), header assembly (A-1), fidelity warning (A-2), body (A-3), write (A-4), and next-step (A-5) structure. The only differentiating axis is the **consequence sentence in S-3**, after the C-21 affirmative closure. I verify the common criteria first, then isolate the variable criteria.

---

### Common criteria (all five variants)

| # | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Note |
|---|-----------|------|------|------|------|------|------|
| C-01 | MOCK ARTIFACT header block | PASS | PASS | PASS | PASS | PASS | All six fields present, ordered, before body |
| C-02 | Category assignment | PASS | PASS | PASS | PASS | PASS | Category table complete, correct |
| C-03 | Skill-specific structure | PASS | PASS | PASS | PASS | PASS | Steps A-3 through A-5 enforce golden-rubric structure requirement |
| C-04 | Automatic flag present and matched | PASS | PASS | PASS | PASS | PASS | Flag computed at S-3, copied verbatim at A-1 |
| C-05 | Artifact path convention | PASS | PASS | PASS | PASS | PASS | `simulations/mock/{topic}-{namespace}-mock-{date}.md` |
| C-06 | Representative skill selection | PASS | PASS | PASS | PASS | PASS | Default table present, correct defaults |
| C-07 | Fidelity warning | PASS | PASS | PASS | PASS | PASS | All three category variants fully specified including Tier 2+ qualifier |
| C-08 | Next-step invocation | PASS | PASS | PASS | PASS | PASS | A-5 present in all variants |
| C-09 | Tier-conditional flag refinement | PASS | PASS | PASS | PASS | PASS | Case 1 names critical namespaces + Tier 2+ explicitly |
| C-10 | TOPICS.md emit line | PASS | PASS | PASS | PASS | PASS | Dedicated `> TOPICS.md: ...` line in S-1 |
| C-11 | Flag computed as named step before header | PASS | PASS | PASS | PASS | PASS | S-3 precedes A-1 in all variants |
| C-12 | topic-status exclusion documented | PASS | PASS | PASS | PASS | PASS | Exclusion constraint column in default table |
| C-13 | Fidelity warning as lead section | PASS | PASS | PASS | PASS | PASS | A-2 precedes A-3, delimited by `---` |
| C-14 | FLAG immutability at both sites | PASS | PASS | PASS | PASS | PASS | S-3: "MUST NOT be recomputed"; A-1: "copy verbatim, do not rederive" |
| C-15 | Structural exclusion column | PASS | PASS | PASS | PASS | PASS | Three-column table with dedicated Exclusion constraint column |
| C-16 | Run-scoped prohibition at compute site | PASS | PASS | PASS | PASS | PASS | "not in any step, any conditional branch, any fallback path, any regeneration sequence, or any other execution context, including paths that do not pass through prior steps in normal order" |
| C-17 | Prohibition first rule at consumption site | PASS | PASS | PASS | PASS | PASS | "The first rule of this step is: copy FLAG from S-3 verbatim" |
| C-18 | Named path classes at compute site | PASS | PASS | PASS | PASS | PASS | Enumerates step, conditional branch, fallback path, regeneration sequence, plus catch-all |
| C-19 | Anti-displacement closure at consumption site | PASS | PASS | PASS | PASS | PASS | Names field-listing, category lookup, formatting instruction; "No instruction in A-1 precedes this rule" |
| C-20 | Failure-consequence at consumption site | PASS | PASS | PASS | PASS | PASS | "Inertia risk: re-deriving FLAG here produces a category mismatch invisible to downstream tooling..." |
| C-21 | No-exemption affirmative closure at compute site | PASS | PASS | PASS | PASS | PASS | "Every execution path that reaches A-1 carries the FLAG value emitted here. No path is exempt." |
| C-22 | Catch-all instruction clause | PASS | PASS | PASS | PASS | PASS | "or any other instruction in this step" in A-1 |
| C-23 | Failure-consequence at compute site | PASS | PASS | PASS | PASS | PASS | "If any path modifies FLAG after this point, ... A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one" |
| C-24 | No-instruction-exempt affirmative | PASS | PASS | PASS | PASS | PASS | "Every instruction in this step -- named or unnamed -- is governed by this rule. No instruction in this step is exempt." |

---

### Variable criteria -- the S-3 consequence sentence

The exact consequence sentence form in each variant:

| Variant | S-3 consequence sentence |
|---------|-------------------------|
| V-01 | "...the guarantee stated above is broken: A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one." |
| V-02 | "...A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one, producing the same silent category mismatch described at the consumption site." |
| V-03 | "...A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one." |
| V-04 | "...the guarantee stated above is broken: A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one, producing the same silent category mismatch described at the consumption site." |
| V-05 | Identical to V-04 |

#### C-25 -- Guarantee-break framing at compute site
Pass condition: consequence statement frames violation as explicitly breaking the C-21 guarantee. Required: "the guarantee stated above is broken" (or equivalent backward-pointing causal bridge to C-21).

| Variant | Result | Evidence |
|---------|--------|----------|
| V-01 | **PASS** | "the guarantee stated above is broken:" present as causal bridge |
| V-02 | **FAIL** | Consequence names mechanism and cross-site reference but no guarantee-break framing; reads as independent consequence |
| V-03 | **FAIL** | Minimal form; no guarantee-break framing |
| V-04 | **PASS** | "the guarantee stated above is broken:" present |
| V-05 | **PASS** | "the guarantee stated above is broken:" present |

#### C-26 -- Cross-site reference at compute site
Pass condition: consequence statement names the shared failure mechanism at the consumption site by explicit reference to C-20. Required: "producing the same silent category mismatch described at the consumption site" (or equivalent). Requires C-20 to be present (it is, in all variants). Requires C-23 pass (all pass).

| Variant | Result | Evidence |
|---------|--------|----------|
| V-01 | **FAIL** | Guarantee-break framing only; no cross-site reference |
| V-02 | **PASS** | "producing the same silent category mismatch described at the consumption site" present |
| V-03 | **FAIL** | Minimal form; no cross-site reference |
| V-04 | **PASS** | "producing the same silent category mismatch described at the consumption site" present |
| V-05 | **PASS** | "producing the same silent category mismatch described at the consumption site" present |

---

### Per-variant criterion summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (E) | P | P | P | P | P |
| C-02 (E) | P | P | P | P | P |
| C-03 (E) | P | P | P | P | P |
| C-04 (E) | P | P | P | P | P |
| C-05 (E) | P | P | P | P | P |
| C-06 (R) | P | P | P | P | P |
| C-07 (R) | P | P | P | P | P |
| C-08 (R) | P | P | P | P | P |
| C-09 (A) | P | P | P | P | P |
| C-10 (A) | P | P | P | P | P |
| C-11 (A) | P | P | P | P | P |
| C-12 (A) | P | P | P | P | P |
| C-13 (A) | P | P | P | P | P |
| C-14 (A) | P | P | P | P | P |
| C-15 (A) | P | P | P | P | P |
| C-16 (A) | P | P | P | P | P |
| C-17 (A) | P | P | P | P | P |
| C-18 (A) | P | P | P | P | P |
| C-19 (A) | P | P | P | P | P |
| C-20 (A) | P | P | P | P | P |
| C-21 (A) | P | P | P | P | P |
| C-22 (A) | P | P | P | P | P |
| C-23 (A) | P | P | P | P | P |
| C-24 (A) | P | P | P | P | P |
| C-25 (A) | **P** | **F** | **F** | **P** | **P** |
| C-26 (A) | **F** | **P** | **F** | **P** | **P** |

Legend: E=essential, R=recommended, A=aspirational, P=PASS, F=FAIL

---

### Score computation

Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/18 × 10)`

| Variant | Essential (5/5) | Recommended (3/3) | Aspirational (/18) | Composite |
|---------|----------------|------------------|--------------------|-----------|
| V-01 | 60.00 | 30.00 | 17/18 × 10 = 9.44 | **99.44** |
| V-02 | 60.00 | 30.00 | 17/18 × 10 = 9.44 | **99.44** |
| V-03 | 60.00 | 30.00 | 16/18 × 10 = 8.89 | **98.89** |
| V-04 | 60.00 | 30.00 | 18/18 × 10 = 10.00 | **100.00** |
| V-05 | 60.00 | 30.00 | 18/18 × 10 = 10.00 | **100.00** |

---

### Rankings

| Rank | Variant | Score | Band | Delta from next |
|------|---------|-------|------|-----------------|
| 1 (tie) | V-04 | 100.00 | Gold | -- |
| 1 (tie) | V-05 | 100.00 | Gold | -- |
| 3 (tie) | V-01 | 99.44 | Gold | −0.56 |
| 3 (tie) | V-02 | 99.44 | Gold | −0.56 |
| 5 | V-03 | 98.89 | Gold | −0.56 |

All variants reach Gold band (all essential pass + composite ≥ 80). The spread is 1.11 points across all five variants — the rubric is in its convergence zone.

---

### Key observations

**C-25 vs C-26 head-to-head:** V-01 (C-25 only) and V-02 (C-26 only) score identically at 99.44. Neither criterion is stronger than the other in isolation under this rubric weighting. Both are single-point aspirational additions at equal weight. R7 finding (C-23 stronger single addition than C-24) does not repeat here — R8's two additions are structurally different mechanisms (logical bridge vs. cross-reference) but symmetrically weighted.

**Minimal-form completeness:** V-04 achieves 100 via minimal additions — both C-25 and C-26 were satisfied by inserting two phrases into the existing C-23 consequence sentence without adding a new sentence. This confirms that the rubric's pass conditions for C-25/C-26 are precision-oriented, not verbosity-oriented.

**Table-structured S-3 (V-04):** The table format for FLAG computation cases in V-04 reduces cognitive load at the branching decision without compressing the prohibition block. It does not affect any rubric criterion but is the only structural difference between V-04 and V-05.

**No new excellence signals beyond C-25 + C-26:** Both top-scoring variants (V-04 and V-05) differ only in S-3 case formatting (table vs. prose). This is a presentation axis, not a semantic one. No new rubric criterion is implied.

---

### Excellence signals from top-scoring variations (V-04 / V-05)

The co-presence of C-25 and C-26 in a single consequence sentence produces the only distinguishing feature:

> "...the guarantee stated above is broken: A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one, producing the same silent category mismatch described at the consumption site."

This form: (1) provides a backward-pointing causal bridge to the C-21 commitment (C-25), and (2) provides a forward-pointing navigational cross-reference to the C-20 consumption-site consequence (C-26), within a single sentence. Neither requires elaboration. The combination completes the six-level compute-site escalation chain.

No patterns emerged from V-04/V-05 that point toward a new rubric criterion. The aspirational space at the compute site appears closed with C-26.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
