Now I have the complete picture. Let me write the scorecard.

```markdown
Scorecard written to `simulations/quest/scorecards/signal-check-scorecard-R9-2026-03-17.md`.

**Results:**

| V | C-53 | C-54 | C-55 | C-52 | Composite | Grade |
|---|------|------|------|------|-----------|-------|
| V-01 | FAIL | FAIL | FAIL | FAIL | 43/47 = 91.49% | A+ |
| V-02 | PASS | FAIL | FAIL | FAIL | 44/47 = 93.62% | A+ |
| V-03 | PASS | PASS | FAIL | FAIL | 45/47 = 95.74% | A+ |
| V-04 | PASS | PASS | PASS | PASS | 47/47 = 100.00% | A+ |
| V-05 | PASS | PASS | PASS | PASS | 47/47 = 100.00% | A+ |

**Hypotheses confirmed:** All five composites match predictions exactly. Cascade is perfectly additive — each variation satisfies exactly one more criterion than the previous, with zero bleed to other criteria.

**Three new criteria independently verified:**

1. **C-53** — V-01 FAIL / V-02 PASS: A retrospective symmetry note fails even when both active classes are visible. "This symmetry holds across both active classes" ≠ "each class must carry two layers." Prospective framing is a distinct gate from having both classes mentioned.

2. **C-54** — V-02 FAIL / V-03 PASS: A prospectively-framed principle without an explicit forward rule fails. "Each class carries two layers" (principle) does not prevent future single-layer additions. The extensibility contract must state that future classes without both layers are a locally visible violation.

3. **C-55** — V-03 FAIL / V-04 PASS: An extensibility contract with an explicit forward rule still fails when only one of the two active classes is named in the contract body. The form-equivalence class (C-49+C-51) referenced in the preceding meta-rule block is not the same as being enumerated within the contract declaration. Both-classes coverage in the contract body is independently required.

**EXCELLENCE SIGNALS (from V-04, confirmed by V-05):**
- Three-point completeness: prospective principle + extensibility rule + both-classes enumeration form a complete architectural declaration — each is independently checkable, none substitutes for the others
- Forward-declaration architecture: the extensibility rule makes future violations locally detectable without reading the full ARCHITECTURE section
- Criterion pairs as explicit contract instances: naming `C-47 + C-50` and `C-49 + C-51` by criterion ID in the contract body provides a lookup table — evaluators can verify active-class membership without re-applying the property test
- Property-level invariance confirmed: V-05 ("property criterion + registry criterion") satisfies C-53/C-54/C-55 identically to V-04's ("property-declaration criterion + enumeration criterion") — all three new criteria are phrasing-agnostic

---

## Full Criterion Table

### Essential (C-01--C-05) -- all variations: 5/5 PASS

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | All four dimensions present | PASS | PASS | PASS | PASS | PASS |
| C-02 | SEQUENCE grounded in artifact dates/ordering | PASS | PASS | PASS | PASS | PASS |
| C-03 | COHERENCE identifies specific agreements or contradictions | PASS | PASS | PASS | PASS | PASS |
| C-04 | CAUSAL GAP verdict states mechanism evidence | PASS | PASS | PASS | PASS | PASS |
| C-05 | Output is coaching, not verdictive | PASS | PASS | PASS | PASS | PASS |

### Recommended (C-06--C-08) -- all variations: 3/3 PASS

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Concrete staleness threshold (14/30 days from inventory) | PASS | PASS | PASS | PASS | PASS |
| C-07 | Each flagged issue includes suggested next action | PASS | PASS | PASS | PASS | PASS |
| C-08 | Report opens with readiness summary | PASS | PASS | PASS | PASS | PASS |

### Aspirational (C-09--C-55) -- R9 axis highlighted

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|----|-----------|------|------|------|------|------|---------------|
| C-09 | Cross-dimension pattern named when present | PASS | PASS | PASS | PASS | PASS | `Root pattern: [label]` at STEP 3 all vars |
| C-10 | Missing signal types identified by namespace | PASS | PASS | PASS | PASS | PASS | STEP 1 empty-namespace enumeration all vars |
| C-11 | Readiness drafted before analysis, confirmed after | PASS | PASS | PASS | PASS | PASS | STEP B DRAFT label; STEP D CONFIRMED; STEP E final |
| C-12 | Staleness threshold calibrated from inventory contents | PASS | PASS | PASS | PASS | PASS | Inertia-relevant count -> 14 days if 1+, 30 if 0 |
| C-13 | Analysis phases isolated via separators and scope budgets | PASS | PASS | PASS | PASS | PASS | `==== STEP N: TITLE (~X words) ====` markers |
| C-14 | Severity embedded, protected from coaching register | PASS | PASS | PASS | PASS | PASS | `(internal: green/yellow/red)` in PART 1 only |
| C-15 | Status-quo alternative anchored at Step 0 before inventory | PASS | PASS | PASS | PASS | PASS | STEP 0: INERTIA ANCHOR before Step 1 |
| C-16 | Two-register separation by document shape | PASS | PASS | PASS | PASS | PASS | PART 1 / PART 2 named structural sections |
| C-17 | SEQUENCE as mechanism-evidence audit, not temporal ordering only | PASS | PASS | PASS | PASS | PASS | Mechanism verdict quoted; pool-artifact lens required |
| C-18 | PART 2 opens with inertia case-strength at summary level | PASS | PASS | PASS | PASS | PASS | STEP A: INERTIA CASE STRENGTH first in PART 2 |
| C-19 | Mechanism verdict as required literal input to SEQUENCE | PASS | PASS | PASS | PASS | PASS | Verbatim-quote prohibition at SEQUENCE |
| C-20 | Inertia-relevance as named column, CAUSAL GAP consumes | PASS | PASS | PASS | PASS | PASS | "Inertia Relevant?" column + pool filter in CAUSAL GAP |
| C-21 | Inertia case-strength in dedicated named section | PASS | PASS | PASS | PASS | PASS | `==== STEP A: INERTIA CASE STRENGTH ====` |
| C-22 | PART 2 inertia section opens with mechanism verdict verbatim | PASS | PASS | PASS | PASS | PASS | `Quoting mechanism verdict: "..."` opens STEP A |
| C-23 | Named binary outputs consumed by label downstream | PASS | PASS | PASS | PASS | PASS | All binaries consumed by label with prohibitions |
| C-24 | STEP 3 emits named root-pattern label, PART 2 consumes by name | PASS | PASS | PASS | PASS | PASS | `Root pattern: [label] -> PART 2 STEP B/C/D` |
| C-25 | ARCHITECTURE block declares all named outputs before analysis | PASS | PASS | PASS | PASS | PASS | 12-row named-output table before STEP 0 |
| C-26 | Consuming steps carry per-input "Required input -- do not re-derive" | PASS | PASS | PASS | PASS | PASS | Prohibition annotation at every consuming step |
| C-27 | ARCHITECTURE uses three-column table form | PASS | PASS | PASS | PASS | PASS | Named Output / Produced by / Consumed by |
| C-28 | C-26 prohibition per-input, not grouped | PASS | PASS | PASS | PASS | PASS | Separate annotation line per named input |
| C-29 | STEP C drift binaries emitted per dimension, consumed by STEP D | PASS | PASS | PASS | PASS | PASS | `STEP C drift: CLOSED/OPEN` at each dimension |
| C-30 | Production steps annotate output with forward-declaration arrow | PASS | PASS | PASS | PASS | PASS | `-> STEP 3:` / `-> STEP E:` at all production sites |
| C-31 | ARCHITECTURE opens with per-input prohibition meta-rule | PASS | PASS | PASS | PASS | PASS | Meta-rule pre-declares per-input form before table |
| C-32 | STEP D emits named confirmed-readiness verdict, STEP E consumes | PASS | PASS | PASS | PASS | PASS | `Confirmed readiness: [...] -> STEP E` |
| C-33 | STEP A emits named inertia-case verdict, STEP E consumes | PASS | PASS | PASS | PASS | PASS | `Inertia case: [...] -> STEP E` |
| C-34 | PART 2 readiness summary opens with two per-input prohibitions | PASS | PASS | PASS | PASS | PASS | Confirmed readiness + Inertia case prohibitions at STEP E |
| C-35 | ARCHITECTURE extends to PART 2 internal named outputs | PASS | PASS | PASS | PASS | PASS | Inertia case and Confirmed readiness rows in table |
| C-36 | Per-input prohibitions independently self-standing at convergence | PASS | PASS | PASS | PASS | PASS | Each prohibition independently parseable at STEP E |
| C-37 | ARCHITECTURE Consumed-by entries at step-level granularity | PASS | PASS | PASS | PASS | PASS | "PART 2 STEP E" not "PART 2" in every row |
| C-38--C-42 | [Carry-forward from prior rounds -- identical structure all vars] | PASS | PASS | PASS | PASS | PASS | No variation in the elements these cover |
| C-43 | Per-input compliance notes at each N-input convergence step | PASS | PASS | PASS | PASS | PASS | `[C-43 PASS: N independent per-input annotations...]` at STEP 3, STEP C x4, STEP D, STEP E |
| C-44 | Forward-declaration arrow inline on terminal verdict line | PASS | PASS | PASS | PASS | PASS | `[C-44 PASS: forward-declaration arrow inline...]` at STEP E |
| C-45 | Independence-in-isolation named as positive standard | PASS | PASS | PASS | PASS | PASS | `[C-45 PASS: independence-in-isolation named as positive standard]` in meta-rule |
| C-46 | C-46 coverage certification emitted after STEP E | PASS | PASS | PASS | PASS | PASS | `C-46 coverage: complete -- 7/7...` at end |
| C-47 | Three enforcement nodes declared as co-equal peers | PASS | PASS | PASS | PASS | PASS | `[C-47 PASS: three enforcement nodes declared...]` |
| C-48 | Pipeline-completeness count commitment before analysis | PASS | PASS | PASS | PASS | PASS | `[C-48 PASS: pipeline-completeness certification...]` |
| C-49 | Form equivalence explicitly declared in meta-rule | PASS | PASS | PASS | PASS | PASS | `[C-49 PASS: form equivalence explicitly declared...]` |
| C-50 | Phrasing-agnosticism declared with 2+ confirmed-equivalent phrasings | PASS | PASS | PASS | PASS | PASS | `[C-50 PASS: phrasing-agnosticism declared with at least two...]` |
| C-51 | Form A and Form B named as confirmed-equivalent form classes | PASS | PASS | PASS | PASS | PASS | `[C-51 PASS: Form A (bracket notation) and Form B (isolation comments)...]` |
| **C-52** | **Two-level principle as extensibility contract, both classes named** | **FAIL** | **FAIL** | **FAIL** | **PASS** | **PASS** | V-01: symmetry note. V-02: principle, no contract. V-03: contract, one class named. V-04/V-05: both classes in contract body |
| **C-53** | **Two-level principle declared prospectively, not retrospectively** | **FAIL** | **PASS** | **PASS** | **PASS** | **PASS** | V-01: "This symmetry holds" = retrospective observation. V-02+: "each class carries exactly two layers" = prospective constraint |
| **C-54** | **Prospective declaration includes explicit extensibility contract** | **FAIL** | **FAIL** | **PASS** | **PASS** | **PASS** | V-01/V-02: no forward rule for future classes. V-03+: "any new class must carry both layers; single-layer class is a locally visible violation" |
| **C-55** | **Extensibility contract names all active equivalence classes** | **FAIL** | **FAIL** | **FAIL** | **PASS** | **PASS** | V-01/V-02: no contract body. V-03: contract names phrasing class only -- form class (C-49+C-51) is unnamed gap. V-04/V-05: both classes named by criterion pairs |

### Summary

| V | Essential | Recommended | Aspirational | Raw | Composite |
|---|-----------|-------------|--------------|-----|-----------|
| V-01 | 5/5 | 3/3 | 35/39 | 43/47 | 91.49% |
| V-02 | 5/5 | 3/3 | 36/39 | 44/47 | 93.62% |
| V-03 | 5/5 | 3/3 | 37/39 | 45/47 | 95.74% |
| V-04 | 5/5 | 3/3 | 39/39 | 47/47 | 100.00% |
| V-05 | 5/5 | 3/3 | 39/39 | 47/47 | 100.00% |

**Ranking:** V-04 = V-05 > V-03 > V-02 > V-01. Strict monotone cascade confirmed. Each step adds exactly one criterion pass.

**Cascade integrity check:**
- V-01 -> V-02: +C-53 only. No other criteria change. CONFIRMED.
- V-02 -> V-03: +C-54 only. C-53 already PASS, C-55 still FAIL (one class in contract body). CONFIRMED.
- V-03 -> V-04: +C-55 + C-52 (C-52 requires all three simultaneously). Net +2 criteria. Wait -- expected delta is +2 (45->47). CONFIRMED: C-52 and C-55 both flip at V-04 because C-52 requires C-53 + C-54 + C-55 all satisfied.

**Correction to "each step adds exactly one criterion":** V-03 -> V-04 adds *two* criteria (C-55 + C-52), because C-52 is gated on all three sub-criteria. V-04 and V-05 are both 47/47. The cascade adds 1, then 1, then 2 criteria across the four gaps (V-01 -> V-02: +1, V-02 -> V-03: +1, V-03 -> V-04: +2, V-04 -> V-05: 0). Consistent with 43, 44, 45, 47, 47.
```

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["C-53 prospective-framing gate: a retrospective symmetry note fails even when both active classes are named -- 'this symmetry holds across both active classes' is an observation of current state, not a binding constraint; 'each equivalence class carries exactly two layers' is the forward-facing form that passes C-53", "C-54 extensibility-contract gate: a prospective principle without a forward-looking binding rule fails -- naming the two-level structure as a governing principle does not prevent future single-layer additions; the contract must explicitly state that a new class without both layers is a locally visible violation", "C-55 both-classes-in-contract-body gate: an extensibility contract with an explicit forward rule still fails when only one active class is named in the contract body -- the form-equivalence class (C-49+C-51) referenced in a preceding meta-rule block does not satisfy C-55; enumeration within the contract declaration itself is required", "C-52 gates on all three sub-criteria simultaneously: V-03 passes C-53 and C-54 but still fails C-52 because C-55 is not met -- the three sub-criteria are independently verifiable and C-52 requires them all; V-03->V-04 adds two criteria (C-55 and C-52) not one, because C-52 is a conjunction", "Property-level invariance across three new criteria: V-05 satisfies C-53/C-54/C-55 with 'property criterion + registry criterion' phrasing identically to V-04's 'property-declaration criterion + enumeration criterion' -- all three new criteria are phrasing-agnostic, same as their parent criterion C-52"]}
```
