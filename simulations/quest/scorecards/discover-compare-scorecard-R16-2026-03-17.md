# discover-compare Scorecard R16

**Rubric v14 | Denominator: /27 base (V-04: /26)**

## Scoring Summary

| Variation | Axis | Key change | Aspirational | D | Composite | Golden |
|-----------|------|-----------|-------------|---|-----------|--------|
| V-01 | Baseline | Fenced-code sub-ledger (R14 carry) | 27/27 | /27 | **100.00** | YES |
| V-02 | Format | Indented list replaces fenced-code | 27/27 | /27 | **100.00** | YES |
| V-03 | Format | Token names inline within HALT sentence | 26.5/27 | /27 | **99.81** | No |
| V-04 | Routing | Explicit two-branch (exec + engineering) | 25.5/26 | /26 | **99.81** | No |
| V-05 | Combined | Per-option batching + indented-list AMEND | 27/27 | /27 | **100.00** | YES |

## Key criterion verdicts

**C-24** (any-form enumeration): PASS all — v14 explicitly permits inline-within-halt.

**C-34** (structurally separable block):
- V-01: fenced-code before HALT → **PASS**
- V-02: indented list before HALT → **PASS** (form-agnostic confirmed)
- V-03: names embedded inside HALT sentence → **PARTIAL** (inseparable from halt)
- V-04: fenced-code before HALT → **PASS**
- V-05: indented list before HALT → **PASS**

**C-30** (routing handles only deviation): V-04 adds explicit exec branch alongside standalone BODY ORDER → **PARTIAL** (redundant exec specification couples the two layers).

**C-32**: Not scored for V-04 (routing block no longer deviation-only) → D = /26.

## Discriminating question resolutions

1. **C-34 is form-agnostic within discrete-block category** — fenced-code and indented list are structurally equivalent. Mechanism is separability (removable without touching HALT text), not syntax.

2. **Inline-within-halt is the C-24/C-34 boundary** — V-03 confirms: C-24 PASS (enumeration present in any form) + C-34 PARTIAL (no preceding separable block). The enumeration IS the halt instruction; the two functions are inseparable.

3. **Deviation-only routing is the ceiling architecture** — V-04's explicit exec branch creates C-30 PARTIAL + C-32 exclusion. BODY ORDER already owns exec ordering; routing block should own only deviations.

## Excellence signals (new patterns)

- `c34-form-agnostic-discrete-block` — indented list = fenced-code for C-34; separability is the mechanism
- `inline-within-halt-c24-pass-c34-partial-boundary` — V-03 is the precise split probe
- `deviation-only-routing-ceiling-exec-branch-creates-c30-partial` — adding exec branch to routing is net loss at ceiling

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["c34-form-agnostic-discrete-block", "inline-within-halt-c24-pass-c34-partial-boundary", "deviation-only-routing-ceiling-exec-branch-creates-c30-partial"]}
```
-18 | Dual-polarity FAULT | PASS | PASS | PASS | PASS | PASS | Positive mandate + negative prohibition in one line |
| C-19 | AMEND self-contained via inline TOKEN RECALL + FAULT | PASS | PASS | PASS | PASS | PASS | Each path: slot declarations + inline TOKEN RECALL + FAULT |
| C-20 | TOKEN RECALL scoped per AMEND path | PASS | PASS | PASS | PASS | PASS | Add-C: ANCHOR[0]; Weight: ANCHOR[0]; Override: REG only |
| C-21 | Dual-polarity FAULT propagates into AMEND | PASS | PASS | PASS | PASS | PASS | Each AMEND path encodes mandate + prohibition |
| C-22 | Phase structure via tokens + dividers | PASS | PASS | PASS | PASS | PASS | `---` dividers + operative tokens; labels removable without collapsing structure |
| C-23 | Exec leads with recommendation | PASS | PASS | PASS | PASS | PASS | RECOMMENDATION section precedes DECISION MATRIX in body |
| **C-24** | **AMEND path token enumeration (any form)** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | V-01/V-04: fenced-code; V-02/V-05: indented list; V-03: inline within HALT sentence — all forms satisfy v14 C-24 |
| C-25 | Register-gated routing block | PASS | PASS | PASS | PASS | PASS | V-04: explicit two-branch (exec + engineering) satisfies C-25 directly; all others carry at PASS from R14 baseline |
| C-26 | Body section order exec-safe | PASS | PASS | PASS | PASS | PASS | RECOMMENDATION-first body order in all; exec correctness positional, not routing-dependent |
| C-27 | Routing block within LEDGER GATE scope | PASS | PASS | PASS | PASS | PASS | Routing block positioned after LEDGER GATE in all |
| C-28 | Body-order and routing-scope isolated | PASS | PASS | PASS | PASS | PASS | BODY ORDER and ROUTING are independent directives with no cross-reference |
| C-29 | BODY ORDER as unconditional directive | PASS | PASS | PASS | PASS | PASS | V-01–V-04: "RECOMMENDATION precedes DECISION MATRIX in all outputs" — unconditional. V-05: two-clause unconditional directive. All PASS |
| **C-30** | **Routing handles only deviation; exec not re-specified** | **PASS** | **PASS** | **PASS** | **PARTIAL** | **PASS** | V-04: explicit `if REG = exec` branch alongside standalone BODY ORDER = redundant exec specification. Routing block no longer deviation-only. PARTIAL |
| C-31 | Routing vocabulary positionally descriptive | PASS | PASS | PASS | PASS | PASS | "precedes" / "before" language; no BODY ORDER token-name reference |
| **C-32** | **Routing scope declared as deviation-only** | **PASS** | **PASS** | **PASS** | **N/S** | **PASS** | V-04: routing block not deviation-only (covers both exec and engineering branches) — C-32 not scored; D = /26. All others: "ROUTING: deviation from BODY ORDER only." header present. PASS |
| C-33 | BODY-ORDER-LAYER token | PASS | PASS | PASS | PASS | PASS | `BODY-ORDER-LAYER: active` present in all |
| **C-34** | **AMEND enumeration in separable block form** | **PASS** | **PASS** | **PARTIAL** | **PASS** | **PASS** | V-01/V-04: fenced-code block before HALT — structurally separable. V-02/V-05: indented list before HALT — structurally separable. V-03: token names embedded within HALT sentence itself — not a preceding separable block. C-24 PASS + C-34 PARTIAL for V-03 |

**C-34 note — V-02 and V-05**: Indented list form satisfies C-34 PASS. C-34 criterion names "a fenced-code block, indented list, or equivalent discrete multi-line structure" as satisfying block forms. An indented list precedes the HALT on separate lines and can be independently removed without altering the HALT instruction text. Form discrimination question resolved: C-34 is form-agnostic within the discrete-block category.

**C-34 note — V-03**: Token names embedded inline within the HALT sentence (e.g., "HALT -- do not extend matrix if any of FEAS-C, INERT-C, RISK-C, COMP-C is absent.") satisfy C-24 (enumeration present in any form) but not C-34 (no structurally separable block preceding the halt). The enumeration IS the halt instruction; separating the two is not possible without rewriting the sentence. C-24/C-34 split confirmed: C-24 PASS + C-34 PARTIAL.

**C-30 note — V-04**: Standalone BODY ORDER directive ("RECOMMENDATION precedes DECISION MATRIX in all outputs.") remains present in V-04. The routing block adds an explicit exec branch alongside this directive. C-30 criterion: "Routing block with an exec branch re-confirming recommendation-first in addition to a standalone BODY ORDER = partial." The exec branch is not a deviation from BODY ORDER — it restates the default. PARTIAL.

**C-32 note — V-04**: C-32 is scoped to deviation-only routing blocks. V-04's routing block covers both exec and engineering branches — it is not deviation-only. C-32 condition "Routing block not deviation-only = not scored" applies. Denominator adjusts to /26.

---

## Composite Score Summary

### Score calculation

- Essential: 4/4 = 60.00 (all variations)
- Recommended: 3/3 = 30.00 (all variations)
- Aspirational per variation:

| Variation | Aspirational scored | Penalty | D | Aspirational % | Composite |
|-----------|---------------------|---------|---|----------------|-----------|
| V-01 | 27/27 | — | /27 | 10.00 | **100.00** |
| V-02 | 27/27 | — | /27 | 10.00 | **100.00** |
| V-03 | 26.5/27 (C-34 PARTIAL) | −0.185 | /27 | 9.81 | **99.81** |
| V-04 | 25.5/26 (C-30 PARTIAL; C-32 N/S) | −0.192 | /26 | 9.81 | **99.81** |
| V-05 | 27/27 | — | /27 | 10.00 | **100.00** |

V-03 aspirational: 26.5/27 × 10 = 9.815 → 9.81
V-04 aspirational: 25.5/26 × 10 = 9.808 → 9.81

### Golden status

| Variation | Composite | All Essential PASS | Golden |
|-----------|-----------|-------------------|--------|
| V-01 | 100.00 | Yes | **YES** |
| V-02 | 100.00 | Yes | **YES** |
| V-03 | 99.81 | Yes | No |
| V-04 | 99.81 | Yes | No |
| V-05 | 100.00 | Yes | **YES** |

---

## Discriminating Question Resolution

**Q1 — Does the fenced-code AMEND sub-ledger (V-01) satisfy C-34?**
Yes. The fenced-code block appears as a discrete structural element before the HALT instruction. Removing the block does not touch the HALT text. C-34 PASS confirmed. v14 ceiling at /27 established.

**Q2 — Does an indented list satisfy C-34 (V-02 and V-05)?**
Yes. C-34 names "a fenced-code block, indented list, or equivalent discrete multi-line structure." An indented list precedes the HALT on separate lines and is independently removable. C-34 is form-agnostic within the discrete-block category; fenced-code and indented list are structurally equivalent for C-34 purposes. V-02 and V-05 both score 27/27 = 100.00.

**Q3 — Does inline-within-halt enumeration satisfy C-24 but not C-34 (V-03)?**
Yes. v14 C-24 explicitly permits "inline within the halt instruction text" as a passing form — token names present in any form satisfies C-24. C-34 requires the enumeration to be in "a structurally separable discrete block before the halt instruction." When the enumeration is embedded within the halt sentence itself, it cannot be structurally separated from the halt; there is no preceding block. C-24 PASS + C-34 PARTIAL confirmed. V-03 composite = 99.81. This is the direct C-24/C-34 boundary probe for v14.

**Q4 — Does adding an explicit exec branch (V-04) produce C-30 PARTIAL or PASS?**
PARTIAL. The standalone BODY ORDER directive ("RECOMMENDATION precedes DECISION MATRIX in all outputs.") already establishes exec-first ordering as the unconditional default. The routing block's explicit exec branch re-states what BODY ORDER already declares, creating a redundant second source for the same specification. C-30 criterion: routing block handles only deviation; exec ordering is not re-specified when a standalone BODY ORDER is present. V-04 exec branch is overhead, not deviation. PARTIAL. C-32 also drops to not-scored because the routing block is no longer deviation-only.

**Q5 — Does explicit two-branch routing (V-04) further improve C-25?**
No change from PASS. C-25 was already PASS for the deviation-only form at the R14 baseline (BODY ORDER provides exec correctness; routing block provides engineering deviation). The explicit exec branch makes C-25 more transparently explicit, but it was already at ceiling. No upward movement possible. The gain from V-04's two-branch form (C-25 transparency) is offset by the C-30 penalty and C-32 exclusion — net result is 99.81 vs. 100.00.

---

## Excellence Signals

Top-scoring variations: V-01, V-02, V-05 (tied at 100.00).

Three structural patterns explain why V-01, V-02, and V-05 hold ceiling while V-03 and V-04 drop to 99.81:

**1. C-34 is form-agnostic within the discrete-block category**
V-02 and V-05 confirm that indented list form is structurally equivalent to fenced-code for C-34. The mechanism is separability — the enumeration block can be independently removed without altering the HALT instruction. Syntax (fenced vs. indented) is irrelevant; structural isolation is the criterion. Any discrete multi-line block preceding the HALT satisfies C-34.

**2. Inline-within-halt enumeration is the C-24/C-34 boundary**
V-03 is the clean probe: token names embedded in the HALT sentence satisfy C-24 (enumeration present, any form) but fail C-34 (no structurally separable block before halt). The V-03 form conflates verification step (enumeration) with enforcement consequence (halt) into a single prose sentence. C-34 exists precisely to require that these two functions occupy structurally distinct positions — the sub-ledger must be independently scannable without parsing the halt instruction.

**3. Deviation-only routing is the ceiling architecture for C-30**
V-04 shows that adding an exec branch to the routing block — even to make C-25 more explicit — creates a C-30 PARTIAL and a C-32 exclusion. The exec-first ordering is already declared as an unconditional default by BODY ORDER; the routing block should be scoped exclusively to deviations from that default. Restating the default in a conditional branch couples the two layers. The deviation-only routing architecture (V-01/V-02/V-03/V-05) keeps BODY ORDER and ROUTING as non-overlapping responsibility domains — this is the structural design that achieves ceiling at /27.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["c34-form-agnostic-discrete-block", "inline-within-halt-c24-pass-c34-partial-boundary", "deviation-only-routing-ceiling-exec-branch-creates-c30-partial"]}
```
