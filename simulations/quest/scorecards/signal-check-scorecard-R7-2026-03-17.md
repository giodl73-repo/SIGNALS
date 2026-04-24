## R7 Scoring Results — signal-check

**Axis:** C-50 / C-51

| V | C-50 | C-51 | Aspirational | Composite | Grade |
|---|------|------|---|---|---|
| V-01 | FAIL | PASS | 42/43 | 97.67 | A+ |
| V-02 | PASS | FAIL | 42/43 | 97.67 | A+ |
| V-03 | FAIL | FAIL | 41/43 | 95.35 | A+ |
| V-04 | PASS | PASS | 43/43 | 100.00 | A+ |
| V-05 | PASS | PASS | 43/43 | 100.00 | A+ |

**Ranking:** V-04 = V-05 > V-01 = V-02 > V-03

---

**Key findings:**

1. **C-50 requires enumeration, not abstract phrasing-agnosticism.** V-01's "any phrasing that delivers the unified-contract property passes" is a true claim but still fails — it shifts the burden of property verification to the evaluator. The meta-rule must name at least two confirmed-equivalent phrasings explicitly (e.g., V-04 R6 and V-05 R6 variants). Abstract claim ≠ confirmed label.

2. **C-51 requires labeled form classes, not abstract property reference.** V-02's "any notation satisfying the independence property passes" correctly satisfies C-49, but C-51 requires the declaration to also name Form A (bracket notation) and Form B (isolation comments) as labeled classes. Without labels, an evaluator must classify each notation by applying the full independence test — the labeling converts that inference to a lookup.

3. **C-50 and C-51 are independent — zero cascade.** V-03 (both absent) scores exactly 41/43. C-47 and C-49 remain PASS in all three failing variations because their pass conditions (unified-contract framing present; form equivalence declared) are satisfied by the abstract declarations. C-50 and C-51 are additive enumeration layers on top.

4. **Research question confirmed.** V-04 and V-05 both score 43/43. Both criteria are property-level — the specific enumeration language and form-class label words don't matter, only that at least two phrasings are named (C-50) and both form classes are labeled (C-51).

5. **Symmetry between C-50/C-47 and C-51/C-49 is complete.** Each pair has a property-declaration criterion and an enumeration criterion. The property criterion closes drift at the declaration level; the enumeration criterion closes it at the verification level by building a confirmed registry.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["C-50 enumeration requirement: abstract phrasing-agnosticism fails -- meta-rule must name at least two confirmed-equivalent phrasings explicitly, converting phrasing verification from a property test to a label lookup", "C-51 labeled-class requirement: abstract form-equivalence declaration fails -- meta-rule must name Form A and Form B by label, converting form membership from an inference task to a label match", "C-50/C-47 and C-51/C-49 symmetry: each pair has a property-declaration criterion and an enumeration criterion -- the property criterion closes drift at the declaration level; the enumeration criterion closes it at the verification level by building a confirmed registry"]}
```
ivered.

5. **Symmetry between C-50/C-47 and C-51/C-49 is complete** -- C-47 and C-49 close the drift risk at the property declaration level. C-50 and C-51 close the drift risk at the enumeration level, converting abstract claims into testable label registries. The four criteria form two symmetric pairs: C-47 (unified-contract declared) + C-50 (phrasings enumerated); C-49 (form equivalence declared) + C-51 (form classes labeled). Without the enumeration layer, correct property declarations still leave evaluators with a judgment call on every candidate -- the enumeration layer removes that call.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["C-50 enumeration requirement: abstract phrasing-agnosticism fails -- meta-rule must name at least two confirmed-equivalent phrasings explicitly, converting phrasing verification from a property test to a label lookup", "C-51 labeled-class requirement: abstract form-equivalence declaration fails -- meta-rule must name Form A and Form B by label, converting form membership from an inference task to a label match", "C-50/C-47 and C-51/C-49 symmetry: each pair has a property-declaration criterion and an enumeration criterion -- the property criterion closes drift at the declaration level; the enumeration criterion closes it at the verification level by building a confirmed registry"]}
```

---

## Full Criterion Table

### Essential (C-01--C-05) -- all variations: 5/5 PASS

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | All four dimensions present (CAUSAL GAP, SEQUENCE, COHERENCE, STALENESS) | PASS | PASS | PASS | PASS | PASS |
| C-02 | SEQUENCE finding grounded in artifact dates or ordering | PASS | PASS | PASS | PASS | PASS |
| C-03 | COHERENCE identifies specific agreements or contradictions | PASS | PASS | PASS | PASS | PASS |
| C-04 | CAUSAL GAP verdict states mechanism evidence presence | PASS | PASS | PASS | PASS | PASS |
| C-05 | Output is coaching, not verdictive | PASS | PASS | PASS | PASS | PASS |

### Recommended (C-06--C-08) -- all variations: 3/3 PASS

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Concrete staleness threshold (14/30 days from inventory count) | PASS | PASS | PASS | PASS | PASS |
| C-07 | Each flagged issue includes suggested next action | PASS | PASS | PASS | PASS | PASS |
| C-08 | Report opens with readiness summary | PASS | PASS | PASS | PASS | PASS |

### Aspirational (C-09--C-51) -- axis highlighted; carry-forward at PASS for unchanged criteria

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|----|-----------|------|------|------|------|------|---------------|
| C-09 | Cross-dimension pattern named when present | PASS | PASS | PASS | PASS | PASS | Root pattern: [label] at STEP 3 all vars |
| C-10 | Missing signal types identified by namespace | PASS | PASS | PASS | PASS | PASS | Step 1 empty-namespace enumeration all vars |
| C-11 | Readiness drafted before analysis, confirmed or revised after | PASS | PASS | PASS | PASS | PASS | STEP B DRAFT label; STEP D CONFIRMED; finalized STEP E |
| C-12 | Staleness threshold calibrated from inventory contents | PASS | PASS | PASS | PASS | PASS | Inertia-relevant count -> 14 days if 1+, 30 days if 0 |
| C-13 | Analysis phases isolated via separators and scope budgets | PASS | PASS | PASS | PASS | PASS | `==== STEP N: TITLE (~X words) ====` markers |
| C-14 | Severity embedded in analysis, protected from coaching register | PASS | PASS | PASS | PASS | PASS | `(internal: green/yellow/red)` in PART 1 only |
| C-15 | Status-quo alternative anchored at Step 0 before inventory runs | PASS | PASS | PASS | PASS | PASS | STEP 0: INERTIA ANCHOR before Step 1 |
| C-16 | Two-register separation by document shape | PASS | PASS | PASS | PASS | PASS | PART 1 / PART 2 named structural sections |
| C-17 | SEQUENCE as mechanism-evidence audit, not temporal ordering only | PASS | PASS | PASS | PASS | PASS | Mechanism verdict quoted; pool-artifact lens required |
| C-18 | PART 2 opens with inertia case-strength question at summary level | PASS | PASS | PASS | PASS | PASS | STEP A: INERTIA CASE STRENGTH first in PART 2 |
| C-19 | Mechanism verdict as required literal input to SEQUENCE | PASS | PASS | PASS | PASS | PASS | Verbatim-quote prohibition at SEQUENCE |
| C-20 | Inertia-relevance as named column in inventory, CAUSAL GAP consumes | PASS | PASS | PASS | PASS | PASS | "Inertia Relevant?" column + pool filter in CAUSAL GAP |
| C-21 | Inertia case-strength in dedicated named section at PART 2 | PASS | PASS | PASS | PASS | PASS | `==== STEP A: INERTIA CASE STRENGTH ====` |
| C-22 | PART 2 inertia section opens with mechanism verdict quoted verbatim | PASS | PASS | PASS | PASS | PASS | `Quoting mechanism verdict: "..."` opens STEP A |
| C-23 | Named binary outputs consumed by label downstream | PASS | PASS | PASS | PASS | PASS | All binaries consumed by label with prohibitions |
| C-24 | STEP 3 emits named root-pattern label consumed by PART 2 by name | PASS | PASS | PASS | PASS | PASS | `Root pattern: [label] -> PART 2 STEP B/C/D` |
| C-25 | ARCHITECTURE block declares all named outputs before analysis | PASS | PASS | PASS | PASS | PASS | 12-row named-output table before STEP 0 |
| C-26 | Consuming steps carry per-input "Required input -- do not re-derive" | PASS | PASS | PASS | PASS | PASS | Prohibition annotation at every consuming step |
| C-27 | ARCHITECTURE block uses three-column table form | PASS | PASS | PASS | PASS | PASS | Named Output / Produced by / Consumed by |
| C-28 | C-26 prohibition per-input, not grouped | PASS | PASS | PASS | PASS | PASS | Separate annotation line per named input |
| C-29 | STEP C drift binaries emitted per dimension, consumed by STEP D | PASS | PASS | PASS | PASS | PASS | STEP C drift: CLOSED/OPEN at each dimension |
| C-30 | Production steps annotate output with forward-declaration arrow | PASS | PASS | PASS | PASS | PASS | `-> STEP 3:` / `-> STEP E:` at all production sites |
| C-31 | ARCHITECTURE opens with per-input prohibition meta-rule | PASS | PASS | PASS | PASS | PASS | Meta-rule pre-declares per-input form before table |
| C-32 | STEP D emits named confirmed-readiness verdict consumed by STEP E | PASS | PASS | PASS | PASS | PASS | `Confirmed readiness: [...] -> STEP E` |
| C-33 | STEP A emits named inertia-case verdict consumed by STEP E | PASS | PASS | PASS | PASS | PASS | `Inertia case: [...] -> STEP E` |
| C-34 | PART 2 readiness summary opens with two per-input prohibitions | PASS | PASS | PASS | PASS | PASS | Confirmed readiness + Inertia case prohibitions at STEP E |
| C-35 | ARCHITECTURE includes PART 2 internal named outputs | PASS | PASS | PASS | PASS | PASS | Inertia case, Confirmed readiness rows in table |
| C-36 | Per-input prohibitions independently self-standing at convergence | PASS | PASS | PASS | PASS | PASS | Each annotation complete without proximity dependency |
| C-37 | ARCHITECTURE Consumed-by entries at step-level granularity | PASS | PASS | PASS | PASS | PASS | "PART 2 STEP E (by label)" not "PART 2" |
| C-38 | STEP E emits named terminal verdict | PASS | PASS | PASS | PASS | PASS | `Terminal readiness: [PROCEED/LOOP/INVESTIGATE + reason]` |
| C-39 | STEP E carries `Required output -- emit exactly:` annotation | PASS | PASS | PASS | PASS | PASS | Production-site obligation marker present at STEP E |
| C-40 | Terminal verdict includes one-phrase reason | PASS | PASS | PASS | PASS | PASS | `[verdict + one-phrase reason]` declared in template |
| C-41 | ARCHITECTURE terminal row names external consumer by system identity | PASS | PASS | PASS | PASS | PASS | `topic namespace (by label)` as Consumed-by |
| C-42 | Multi-consumer ARCHITECTURE entries list all consuming steps | PASS | PASS | PASS | PASS | PASS | Root pattern: PART 2 STEP B; STEP C per-dim; STEP D |
| C-43 | C-36 independence at every multi-input consuming step pipeline-wide | PASS | PASS | PASS | PASS | PASS | Bracket notes (V-01--04) / isolation comments (V-05) at all steps |
| C-44 | Terminal producer annotates verdict with inline forward-declaration arrow | PASS | PASS | PASS | PASS | PASS | Arrow inline on verdict line: `-> topic namespace` |
| C-45 | ARCHITECTURE meta-rule names independence as governing standard | PASS | PASS | PASS | PASS | PASS | `[C-45 PASS: ...]` explicitly marked; positive standard stated |
| C-46 | Each multi-input consuming step carries inline convergence compliance note | PASS | PASS | PASS | PASS | PASS | 7/7 steps carry compliance notes (V-01--04 Form A; V-05 Form B) |
| C-47 | ARCHITECTURE meta-rule names all three enforcement nodes as unified local-verifiability contract | PASS | PASS | PASS | PASS | PASS | All vars: "co-equal self-declaration peers" / "complete local-verifiability contract" framing present |
| C-48 | Output carries pipeline-completeness certification (C-46 coverage: complete -- N/N) | PASS | PASS | PASS | PASS | PASS | Count commitment pre-declared + post-analysis assertion all vars |
| C-49 | ARCHITECTURE meta-rule declares form equivalence for convergence compliance notes | PASS | PASS | PASS | PASS | PASS | V-01/03: abstract property declaration. V-02: abstract. V-04/05: full with labeled classes. All satisfy C-49 (property declaration present); C-51 separates labeled vs. abstract. |
| **C-50** | **ARCHITECTURE meta-rule carries explicit phrasing-agnosticism for C-47, naming at least two confirmed-equivalent phrasings** | **FAIL** | PASS | **FAIL** | PASS | PASS | V-01/03: "any phrasing that delivers the unified-contract property passes" -- abstract claim, no phrasings named. V-02/04/05: two phrasings explicitly listed (R6 V-04 and V-05 variants). |
| **C-51** | **Form-equivalence declaration (C-49) names confirmed-equivalent form classes by label (Form A / Form B)** | PASS | **FAIL** | **FAIL** | PASS | PASS | V-02/03: form equivalence declared by property reference only; no "Form A (bracket notation)" or "Form B (isolation comments)" labeled. V-01/04/05: both class labels named explicitly. |

---

## Score Summary

| V | Essential | Recommended | Aspirational | Composite | Grade |
|---|---|---|---|---|---|
| V-01 | 5/5 | 3/3 | 42/43 | 97.67 | A+ |
| V-02 | 5/5 | 3/3 | 42/43 | 97.67 | A+ |
| V-03 | 5/5 | 3/3 | 41/43 | 95.35 | A+ |
| V-04 | 5/5 | 3/3 | 43/43 | 100.00 | A+ |
| V-05 | 5/5 | 3/3 | 43/43 | 100.00 | A+ |

**Ranking:** V-04 = V-05 > V-01 = V-02 > V-03

**Research question answered:** V-04 and V-05 both score 43/43, confirming C-50 and C-51 are property-level criteria -- any enumeration naming at least two confirmed-equivalent phrasings (C-50) and any labeling naming the two confirmed-equivalent form classes by label (C-51) both pass. The specific phrasings cited and the specific form-class label words are not required; the properties (enumeration present, labeling present) are.

---

## Excellence Signals

**From V-04 and V-05 (top-scoring, 43/43):**

1. **Enumeration converts phrasing verification from property test to label lookup** -- V-04 names both R6 confirmed-equivalent phrasings explicitly: `"co-equal self-declaration peers in a local-verifiability contract" (V-04 R6)` and `"three-node self-declaration system... co-equal... locally visible" (V-05 R6)`. V-05 uses equivalent enumeration language: `"Both the following phrasings deliver the unified-contract property: ..."`. In both cases, an evaluator encountering either phrasing in the wild can match by label rather than re-applying the full property test. The confirmed-label registry is the structural gain.

2. **Form-class labeling converts form membership from inference to lookup** -- V-04 names Form A (bracket notation) and Form B (isolation comments) as explicit labeled classes under the form-equivalence declaration. V-05 uses "bracket-group form" and "isolation-comment form" as equivalent labels. Either naming passes C-51 because the criterion is label presence, not specific label text. An evaluator encountering an isolation-comment compliance note can match it to Form B by label rather than applying the full independence-property test to classify it.

3. **C-50 and C-51 close the final verification-burden gap in the meta-rule** -- After R6, the ARCHITECTURE block was fully declared (C-25, C-27, C-31, C-35) with form equivalence (C-49) and unified-contract framing (C-47). The remaining gap: all three abstraction-level declarations still required evaluators to apply property tests to candidate phrasings and forms. C-50 and C-51 close that by pre-populating the confirmed-equivalent sets, reducing evaluator work at every future assessment from O(property-test) to O(label-match).

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["C-50 enumeration requirement: abstract phrasing-agnosticism fails -- meta-rule must name at least two confirmed-equivalent phrasings explicitly, converting phrasing verification from a property test to a label lookup", "C-51 labeled-class requirement: abstract form-equivalence declaration fails -- meta-rule must name Form A and Form B by label, converting form membership from an inference task to a label match", "C-50/C-47 and C-51/C-49 symmetry: each pair has a property-declaration criterion and an enumeration criterion -- the property criterion closes drift at the declaration level; the enumeration criterion closes it at the verification level by building a confirmed registry"]}
```
