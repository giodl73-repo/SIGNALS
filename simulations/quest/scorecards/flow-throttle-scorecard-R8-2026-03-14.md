Now I have all the information needed to score the five variations against the v8 rubric.

---

# flow-throttle — Round 8 Scorecard (v8 Rubric, 154-point max)

## Baseline Verification (C-01..C-24 — All Variations)

All five variations share identical Round 1 and Round 2 content; only the pre-barrier container header differs. C-01..C-24 evaluation is therefore uniform.

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-01 Bottleneck Localization | TABLE 2 bottleneck statement template requires specific PA construct, type, saturation volume with "why ordering holds" | PASS |
| C-02 Rate Limit Hit Ordering | TABLE 2 explicit hit order with 2+ tiers and explanatory column | PASS |
| C-03 Backpressure Propagation | TABLE 3 requires ≥2 hops, named signal type, receiving component, response | PASS |
| C-04 UX per Throttle Tier | TABLE 4 with "UX categories MUST differ across tiers" enforcement | PASS |
| C-05 Domain Grounding | Domain rule enumerates exact PA construct types; generic terms explicitly fail | PASS |
| C-06 Unprotected Burst Path | TABLE 5 checks Apply-to-Each, parallel branches, debounce; acknowledgment required if none | PASS |
| C-07 Missing Retry-After | TABLE 6 with explicit failure-mode taxonomy (retry-storm, fixed-misalign, silent-discard) | PASS |
| C-08 Cascade Risk Register | TABLE 7 requires ≥2 cascade pairs, Tier A ≠ Tier B, mechanism stated | PASS |
| C-09 PA-Specific Remediations | TABLE 10 requires PA-native features (exact names), mapped to specific findings | PASS |
| C-10 Monitoring | Section 4.E: named PA signals with trigger conditions | PASS |
| C-11 License Boundary | Section 4.F: named entitlement boundary affecting TABLE 9 rows | PASS |
| C-12 Throttle Budget | TABLE 9 with STATUS field and arithmetic shown for ≥1 row | PASS |
| C-13 Test Approach | Section 4.G: specific PA tooling method required | PASS |
| C-14 Gate Mechanism | GATE 1/2/3: each has label, conditional prerequisite, named blocked target | PASS |
| C-15 Non-Deference | "Round 1's confidence...is not evidence of Round 1's structural precision" — names prior layer | PASS |
| C-16 Scope Extension | "Introduced after Round 1's execution window had closed" — structural closure reason present | PASS |
| C-17 Pre-Barrier Independence Placement | Non-deference sentence in PRE-EVALUATION container, before any TABLE 11 output | PASS |
| C-18 Structural Closure Reason | "Round 1 closed before TABLE 8 corrections were finalized" — mechanism, not category | PASS |
| C-19 Label-Enforced Co-location | `**Independence:**` and `**Scope extension:**` are distinct named labels | PASS |
| C-20 Gate Prose Portability | Each GATE carries (a) name, (b) condition, (c) blocked target in prose | PASS |
| C-21 Container Name Encodes Position | All use "PRE-EVALUATION ASSERTIONS" or "PRE-EVALUATION DIRECTIVES" — positional qualifier | PASS |
| C-22 Pre-Barrier Labeled Pair | Both labeled directives in pre-barrier container before Round 2 evaluative content | PASS |
| C-23 Dual-Dimension Completeness | C-21 AND C-22 both hold from same container | PASS |
| C-24 Cross-Generation Coverage | C-19 AND C-22 both hold | PASS |

**Baseline (C-01..C-24): 142 / 142. All essential criteria PASS.**

---

## V-01 — C-27 Isolation: Generic Phrase, Round-Head Immediate

Header: `PRE-EVALUATION ASSERTIONS (before any construct evaluation begins)` — immediate under `## ROUND 2`

| Criterion | Evidence | Verdict | Pts |
|-----------|----------|---------|-----|
| C-25 | Phrase present: "before any construct evaluation begins" — temporal form, satisfies positional + trigger dimensions | PASS | +3 |
| C-26 | Container appears immediately after `## ROUND 2 — Structural Precision Pass`; no intervening content | PASS | +3 |
| C-27 | Phrase reads "before any **construct evaluation** begins" — no round identifier. "Round 2" absent from phrase. Cannot navigate from phrase to `## ROUND 2` | FAIL | 0 |
| C-28 | Requires C-25 AND C-26. Both hold. C-28 does NOT require C-27 | PASS | +3 |

**V-01 Score: 142 + 3 + 3 + 0 + 3 = 151 / 154**
*Prediction: 151. Confirmed.*

---

## V-02 — C-28 Isolation via C-26 Failure: Round-Named Phrase, Transitional Sentence

Header: `PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` — **after transitional paragraph**

The `## ROUND 2` heading is followed by: *"Round 1 produced a complete throttle impact analysis. Round 2 now applies an independent structural precision check to the constructs and cascade pairs identified above."* — then the pre-barrier container.

| Criterion | Evidence | Verdict | Pts |
|-----------|----------|---------|-----|
| C-25 | Phrase present: "before any Round 2 construct evaluation begins" — temporal form with round identifier | PASS | +3 |
| C-26 | Transitional paragraph between `## ROUND 2` heading and pre-barrier container. One content block intervenes. Heading-to-container adjacency violated | FAIL | 0 |
| C-27 | Phrase names "Round 2" — cross-referenceable to `## ROUND 2` heading | PASS | +3 |
| C-28 | Requires C-25 AND C-26. C-26 fails. C-28 cannot be satisfied | FAIL | 0 |

**V-02 Score: 142 + 3 + 0 + 3 + 0 = 148 / 154**

> **Prediction discrepancy: Predicted 151, actual 148.**
>
> The design claimed V-02 is a "C-28 single-miss at 151 — symmetric with V-01." This is structurally incorrect. Failing C-26 costs −3 pts (C-26 itself). Because C-28 requires C-26 as a precondition, C-28 also fails, costing −3 more pts. Total loss: −6 pts from ceiling → 148, not 151.
>
> **Root cause**: C-28 = C-25 ∩ C-26 is an intersection criterion. Its failure cannot be isolated from C-26's failure — they share the same precondition event. There is no structural path to fail C-28 without also failing C-25 or C-26. True "C-28 single-miss isolation" is definitionally impossible, because C-28 ADDS to (not replaces) its component criteria. This means the design's symmetry claim ("V-01 and V-02 both miss exactly one 3-pt criterion") was an error.

---

## V-03 — Ceiling: Temporal Form, Round Name, Immediate

Header: `PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` — immediate under `## ROUND 2`

| Criterion | Evidence | Verdict | Pts |
|-----------|----------|---------|-----|
| C-25 | Temporal phrase: "before any Round 2 construct evaluation begins" | PASS | +3 |
| C-26 | Container immediately follows `## ROUND 2` heading, no intervening content | PASS | +3 |
| C-27 | Phrase names "Round 2" — directly cross-referenceable to heading | PASS | +3 |
| C-28 | C-25 AND C-26 both satisfied from same container | PASS | +3 |

**V-03 Score: 142 + 3 + 3 + 3 + 3 = 154 / 154**
*Prediction: 154. Confirmed.*

---

## V-04 — Ceiling: Imperative Form, Round Name, Immediate

Header: `PRE-EVALUATION DIRECTIVES (execute before entering Round 2 evaluation)` — immediate under `## ROUND 2`

| Criterion | Evidence | Verdict | Pts |
|-----------|----------|---------|-----|
| C-21 | "PRE-EVALUATION DIRECTIVES" — encodes positional role | PASS | (in baseline) |
| C-25 | Imperative phrase: "execute before entering Round 2 evaluation" — execution imperative form | PASS | +3 |
| C-26 | Container immediately follows `## ROUND 2` heading, no intervening content | PASS | +3 |
| C-27 | Phrase names "Round 2" — cross-referenceable to heading hierarchy | PASS | +3 |
| C-28 | C-25 AND C-26 both satisfied from same container | PASS | +3 |

**V-04 Score: 142 + 3 + 3 + 3 + 3 = 154 / 154**
*Prediction: 154. Confirmed. Extends temporal/imperative form equivalence to C-27.*

---

## V-05 — C-25 Cascade Failure: No Phrase, Immediate

Header: `PRE-EVALUATION ASSERTIONS` — no boundary-event phrase, immediate under `## ROUND 2`

| Criterion | Evidence | Verdict | Pts |
|-----------|----------|---------|-----|
| C-25 | No boundary-event phrase. "PRE-EVALUATION ASSERTIONS" satisfies C-21 (positional qualifier) but adds no trigger dimension | FAIL | 0 |
| C-26 | Container immediately follows `## ROUND 2` heading, no intervening content | PASS | +3 |
| C-27 | Requires C-25 as precondition. C-25 fails — C-27 cannot be reached | FAIL | 0 |
| C-28 | Requires C-25 AND C-26. C-25 fails — C-28 cannot be reached | FAIL | 0 |

**V-05 Score: 142 + 0 + 3 + 0 + 0 = 145 / 154**
*Prediction: 145. Confirmed. C-25 cascade costs exactly 9 pts (C-25 + C-27 + C-28).*

---

## Score Summary and Ranking

| Rank | Variation | C-25 | C-26 | C-27 | C-28 | Score | vs Prediction |
|------|-----------|------|------|------|------|-------|---------------|
| 1 (tie) | V-03 | PASS | PASS | PASS | PASS | **154** | Confirmed |
| 1 (tie) | V-04 | PASS | PASS | PASS | PASS | **154** | Confirmed |
| 3 | V-01 | PASS | PASS | FAIL | PASS | **151** | Confirmed |
| 4 | V-02 | PASS | FAIL | PASS | FAIL | **148** | Predicted 151 — OFF by 3 |
| 5 | V-05 | FAIL | PASS | FAIL | FAIL | **145** | Confirmed |

**Four-level spread: 154 / 151 / 148 / 145** (not the predicted three-level 154/151/145).

---

## Excellence Signals (V-03 and V-04)

**Pattern 1 — Three-dimensional container header.** The pre-barrier container name encodes all three dimensions of structural specification: *where* (positional qualifier: "PRE-EVALUATION"), *when* (boundary-event trigger: "before any ... begins" / "execute before entering"), and *which round* (identifier: "Round 2"). A reader can verify structural priority, execution timing, and barrier scope from the header alone — no content reading required.

**Pattern 2 — Heading-identifier mirror.** The round name in the boundary-event phrase exactly mirrors the barrier heading label (`## ROUND 2`). This creates a bidirectional cross-reference: the heading structure validates the phrase, and the phrase points back to the heading. Neither can change independently without breaking the correspondence.

**Pattern 3 — Form equivalence at the C-27 layer.** V-03 (temporal: "before any Round 2 construct evaluation begins") and V-04 (imperative: "execute before entering Round 2 evaluation") both satisfy C-27. The R7 form-equivalence finding (C-25) extends cleanly to C-27. Phrase form is stylistic; round identifier presence is structural.

**Pattern 4 — C-28 isolation is structurally impossible.** V-01 and V-02 were designed as symmetric single-miss tests. V-01 succeeds: C-27 has no dependent criteria, so failing it costs exactly 3 pts. V-02 fails: C-26 is C-28's precondition, so failing C-26 cascades to C-28 and costs 6 pts. C-28 = C-25 ∩ C-26 cannot be tested as a single-miss — its isolation is definitionally impossible. This asymmetry between C-27 and C-28 failure costs (3 vs. 6 pts when each is absent) was not predicted in the design and represents a v8-specific finding.

---

```json
{"top_score": 154, "all_essential_pass": true, "new_patterns": ["three-dimensional container header encodes position, trigger, and round identifier in a single name", "heading-identifier mirror creates bidirectional cross-reference between phrase and heading structure", "form equivalence (temporal/imperative) extends from C-25 to C-27 layer", "C-28 single-miss isolation is structurally impossible — C-26 cascade makes V-02 score 148 not 151, revealing a design error in the symmetry claim"]}
```
