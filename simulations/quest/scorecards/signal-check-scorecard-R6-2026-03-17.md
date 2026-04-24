## R6 Scoring Results — signal-check

**Axis**: C-47 / C-48 / C-49

| V | C-47 | C-48 | C-49 | Aspirational | Composite | Grade |
|---|------|------|------|---|---|---|
| V-01 | FAIL (enumerated, not unified) | PASS | PASS | 40/41 | 97.56 | A+ |
| V-02 | PASS | FAIL (no certification) | PASS | 40/41 | 97.56 | A+ |
| V-03 | PASS | PASS | FAIL (form mandated) | 40/41 | 97.56 | A+ |
| V-04 | PASS | PASS | PASS | 41/41 | 100.00 | A+ |
| V-05 | PASS | PASS | PASS | 41/41 | 100.00 | A+ |

**Ranking:** V-04 = V-05 > V-01 = V-02 = V-03

---

**Key findings:**

1. **C-47 requires unified-contract framing, not enumeration** — V-01 names all three nodes as a bullet list ("Enforcement mechanisms present: -...") but never declares them as co-equal peers forming a system. The "together they make every obligation locally visible" framing in V-04/V-05 is what closes this. Naming ≠ declaring a unified system.

2. **C-48 is independent of C-46** — V-02 has all 7 compliance notes present and still fails. Individual step compliance does not substitute for a pipeline-level count assertion. The R5 all-or-nothing finding generalizes: partial coverage is undetectable without a count certification.

3. **C-49 is forward-looking protection** — V-03 uses bracket form correctly everywhere (C-46 PASS) but mandates it as "exactly this form." Future valid alternatives would face false-fail. C-49 closes this by pre-declaring form as interchangeable at the property level.

4. **Research question confirmed** — V-04 and V-05 both score 41/41. C-47 and C-49 are property-level: alternative phrasings that deliver the unified-contract property or the independence-as-criterion property both pass.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["C-47 unified-contract framing: naming three nodes as co-equal peers in a single system statement is required -- enumeration alone fails", "C-48 independence from C-46: all convergence notes present does not satisfy count assertion requirement -- certification is a separate pipeline-level obligation", "C-49 pre-declared form equivalence prevents notation lock-in: without it, valid alternative forms face false-fail at the meta-rule level"]}
```
-- V-04 and V-05 both score 41/41. C-47 is satisfied by "co-equal self-declaration peers in a local-verifiability contract" (V-04) and "three-node self-declaration system... co-equal... locally visible" (V-05). C-49 is satisfied by "bracketed group note, per-annotation isolation comment, or equivalent form are interchangeable. The criterion is the property, not the specific notation." (V-04) and "independence property is the criterion; the specific form is not." (V-05). Both phrasings are distinct; both pass.

5. **Form B (isolation comments) passes C-46 equivalently to Form A (bracket notation)** -- V-05's per-annotation isolation comments ("(annotation stands alone: readable in isolation without the X annotation)" plus trailing "[N annotations above; each stands alone -- independence property satisfied at this N-input step]") satisfy C-46 as documented in the rubric: the independence property is the criterion. Since C-49 declares form equivalence in V-05's meta-rule, no false-fail risk exists.

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

### Aspirational (C-09--C-49) -- axis highlighted; carry-forward at PASS for unchanged criteria

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
| **C-47** | **ARCHITECTURE meta-rule names all three enforcement nodes as unified local-verifiability contract** | **FAIL** | PASS | PASS | PASS | PASS | V-01: bullet list "Enforcement mechanisms present: -..." without co-equal peer declaration. V-02--05: explicit unified contract statement with "co-equal" framing. |
| **C-48** | **Output carries pipeline-completeness certification (C-46 coverage: complete -- N/N)** | PASS | **FAIL** | PASS | PASS | PASS | V-02: 7 C-46 notes present, zero count certification anywhere. V-01/03/04/05: count commitment pre-declared + post-analysis assertion present. |
| **C-49** | **ARCHITECTURE meta-rule declares form equivalence for convergence compliance notes** | PASS | PASS | **FAIL** | PASS | PASS | V-03: bracket form mandated as "exactly this form" -- no equivalence declared; alternative forms face false-fail. V-01/02/04/05: equivalence declared at property level. |

---

## Score Summary

| V | Essential | Recommended | Aspirational | Composite | Grade |
|---|---|---|---|---|---|
| V-01 | 5/5 | 3/3 | 40/41 | 97.56 | A+ |
| V-02 | 5/5 | 3/3 | 40/41 | 97.56 | A+ |
| V-03 | 5/5 | 3/3 | 40/41 | 97.56 | A+ |
| V-04 | 5/5 | 3/3 | 41/41 | 100.00 | A+ |
| V-05 | 5/5 | 3/3 | 41/41 | 100.00 | A+ |

**Ranking:** V-04 = V-05 > V-01 = V-02 = V-03

**Research question answered:** V-04 and V-05 both score 41/41, confirming C-47 and C-49 are property-level criteria -- any phrasing that delivers the unified-contract framing (C-47) or the independence-as-criterion framing (C-49) passes. Specific phrases are not required.

---

## Excellence Signals

**From V-04 and V-05 (top-scoring, 41/41):**

1. **Unified contract statement closes the enumeration gap** -- The three enforcement nodes must be declared as co-equal peers forming a complete system (C-47), not merely listed. The signal phrase: "Together these ensure / together they make every pipeline obligation locally self-declared / locally visible without cross-referencing." The "together" framing is what elevates a list into a contract.

2. **Pre-declared count commitment makes C-48 enforceable before analysis** -- V-04's `C-46 coverage commitment: 7 multi-input consuming steps` before the table, paired with a post-analysis `C-46 coverage: complete -- 7/7`, creates a two-point certification anchor. The count is declared up-front so partial compliance is auditable by inspection rather than step enumeration.

3. **Property-level form equivalence removes form as a scoring axis** -- V-04's "The criterion is the property (independence / parseable completeness), not the specific notation" and V-05's "The independence property is the criterion; the specific form is not" both satisfy C-49. The criterion is declared interchangeable-form at the meta-rule level, preventing future variations from failing C-46 on notation grounds when the independence property is satisfied.

4. **Form B (V-05) is a valid alternative to Form A** -- Per-annotation isolation comments ("annotation stands alone: readable in isolation without the X annotation") plus a trailing summary note ("[N annotations above; each stands alone -- independence property satisfied at this N-input step]") fully satisfy C-46 and C-43. Form B is more verbose but makes independence locally visible per annotation rather than in a group note. When C-49 is satisfied, both forms are scoring-equivalent.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["C-47 unified-contract framing: naming three nodes as co-equal peers in a single system statement is required -- enumeration alone fails", "C-48 independence from C-46: all convergence notes present does not satisfy count assertion requirement -- certification is a separate pipeline-level obligation", "C-49 pre-declared form equivalence prevents notation lock-in: without it, valid alternative forms face false-fail at the meta-rule level"]}
```
