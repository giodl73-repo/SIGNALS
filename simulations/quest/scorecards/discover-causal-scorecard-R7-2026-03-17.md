## Discover-Causal — Round 7 Scorecard

**Rubric**: v7 (16 aspirational criteria, denominator 16)
**Golden threshold**: all 5 essential pass AND composite ≥ 80

---

### Essential Criteria

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Mechanism pathway named | PASS | PASS | PASS | PASS | PASS |
| C-02 | Falsification condition present | PASS | PASS | PASS | PASS | PASS |
| C-03 | Inertia check performed | PASS | PASS | PASS | PASS | PASS |
| C-04 | Causal claim is scoped/testable | PASS | PASS | PASS | PASS | PASS |
| C-05 | AMEND directive produced | PASS | PASS | PASS | PASS | PASS |

All 5 essential: **PASS** across all variations.

---

### Recommended Criteria

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| R-01 | Context-specific mechanism evidence | PASS | PASS | PASS | PASS | PASS |
| R-02 | Alternative causes or confounders named | PASS | PASS | PASS | PASS | PASS |
| R-03 | Mechanism chain ≥ 2 hops | PASS | PASS | PASS | PASS | PASS |

All 3 recommended: **PASS** across all variations.

---

### Aspirational Criteria

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| A-01 | Mechanism strength qualified | PASS | PASS | PASS | PASS | PASS |
| A-02 | Inertia baseline quantified or bounded | PASS | PASS | PASS | PASS | PASS |
| A-03 | Adversarial section structurally separated | PASS | PASS | PASS | PASS | PASS |
| A-04 | All classifications use discrete labels | PASS | PASS | PASS | PASS | PASS |
| A-05 | Evidence precedes mechanism mapping | PASS | PASS | PASS | PASS | PASS |
| A-06 | Dual mechanism strength (pre/post adversarial) | PASS | PASS | PASS | PASS | PASS |
| A-07 | Falsification confidence per row | PASS | PASS | PASS | PASS | PASS |
| A-08 | Hops cross-reference falsification conditions | PASS | PASS | PASS | PASS | PASS |
| A-09 | Structural gate checklists | PASS | PASS | PASS | PASS | PASS |
| A-10 | Mechanism hop observability labeled | PASS | PASS | PASS | PASS | PASS |
| A-11 | Falsification testability per condition | PASS | PASS | PASS | PASS | PASS |
| A-12 | Chain observability aggregate + AMEND routing | PASS | PASS | PASS | PASS | PASS |
| A-13 | Testability refinement yield tracked | PASS | PASS | PASS | PASS | PASS |
| **A-14** | **I-NN structured sub-pool** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| **A-15** | **Inertia pathway observability labeled** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| **A-16** | **Post-processing role + routing table** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |

#### A-14 Evidence per variation
- **V-01**: FRAMER Step 3 generates I-NN table with same column structure as F-NN (ID | Condition | Testability | Rationale), ≥2 rows, testability Unknown at genesis. SKEPTIC final falsification table carries I-NN rows alongside F-NN with per-row Confidence.
- **V-02**: Section 2 produces a parallel I-NN table with identical 5-column structure to F-NN (ID | Condition | Testability | Confidence | Rationale), Confidence=Pending, testability=Unknown at genesis. Visually identical to F-NN pool.
- **V-03**: Step 2 generates I-NN pool before claim extraction exists, ≥2 rows; claim-context-free derivation. Step 7 assigns Confidence per row in final falsification table.
- **V-04**: Phase 3 I-NN table (ID | Pathway | Testability | Rationale), ≥2 rows, matching F-NN Phase 2 structure. Phase 6 final table merges both pools with Confidence per row.
- **V-05**: Section B B4 generates I-NN from CH-Hop challenges with a Source hop column (ID | Condition | Source hop | Testability | Rationale), structurally anchoring each I-NN to its counter-hypothesis step.

#### A-15 Evidence per variation
- **V-01**: Step 3 has dedicated `Inertia pathway observability` field (Observable/Partial/Opaque) with rationale and structural independence note distinguishing it from hop observability.
- **V-02**: Section 2 inertia pool header places observability label as first field before I-NN rows, with rationale and explicit note that it answers a different question than Section 4 hop observability.
- **V-03**: Step 1 declares inertia pathway observability before any F-NN or claim work — the earliest lifecycle placement across all variations.
- **V-04**: Q3.3 explicit question ("Can we detect whether Y occurs without X?") elicits Observable/Partial/Opaque label with rationale; structured field follows at Phase 3 close.
- **V-05**: Section B B3 derives inertia pathway observability as an aggregate of CH-Hop observability labels — emergent from chain analysis rather than a standalone declaration. Includes aggregate counts (CH-Observable/CH-Partial/CH-Opaque).

#### A-16 Evidence per variation
- **V-01**: SYNTHESIZER role owns all four diagnostics and produces a 5-row routing table including I-NN pool coverage (row 5 triggers Mechanism slot if Minimal). Role name reflects expanded scope vs. R6 AUDITOR.
- **V-02**: AUDITOR role, 4-row routing table (chain-obs, testability, evidence, inertia). No I-NN coverage row.
- **V-03**: EVALUATOR role, 5-row routing table — row 5 adds inertia-observability as a distinct routing condition (Opaque triggers Inertia-visibility slot).
- **V-04**: EXAMINER role, 4-row routing table. Interrogative framing carries into EXAMINER (Q_E1 through Q_E5).
- **V-05**: AUDITOR role, 5-row routing table — row 5 adds triple-gap count (count > 0 triggers Triple-gap slot), a joint diagnostic not present in any prior variation.

---

### Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (16/16 × 10) | **Composite** | Golden? |
|-----------|---------------|-----------------|--------------------------|---------------|---------|
| V-01 | 60 | 30 | 10.0 | **100.0** | YES |
| V-02 | 60 | 30 | 10.0 | **100.0** | YES |
| V-03 | 60 | 30 | 10.0 | **100.0** | YES |
| V-04 | 60 | 30 | 10.0 | **100.0** | YES |
| V-05 | 60 | 30 | 10.0 | **100.0** | YES |

All five variations achieve **100.0 / 100** composite and all are golden.

**R7 baseline under v7: 100.0 (all 5 variations, 16/16 aspirational)**

---

### Excellence Signals

**R7 achieved the design target**: every variation implements all three new criteria (A-14, A-15, A-16). The round's analytical value is in the structural differences between implementations, which seed new criteria candidates for v8.

#### Pattern 1 — Triple-gap joint diagnostic (V-05)
A fifth AUDITOR diagnostic row that tests co-occurrence of three independent failure signals: Opaque forward mechanism hop + Unknown testability after evidence + I-NN condition with overlapping scope. The triple-gap produces a separate AMEND slot ("Triple-gap") distinct from Observability, Testability, and Inertia slots. Neither A-12, A-13, nor A-14 alone surfaces this co-occurrence. The triple-gap count is a joint severity signal unavailable from individual diagnostics.

#### Pattern 2 — Source hop column in I-NN pool (V-05)
The I-NN table in V-05 adds a Source hop column that structurally anchors each I-NN condition to the CH-Hop that generated it. This creates bidirectional traceability: I-NN → CH-Hop (structural origin) and forward mechanism hop → I-NN (falsification cross-reference via A-08). No other variation has explicit derivation provenance in the I-NN table structure.

#### Pattern 3 — Cross-pool refinement detection (V-03)
Step 5 adds a `Cross-pool note` field tracking whether claim-focused evidence refines I-NN conditions (which were generated before the claim). This creates an evidence transfer signal: did learning about the claim mechanism also bound the inertia pathways? V-03's `cross_pool_refinement_detected` frontmatter field makes this observable across runs.

#### Pattern 4 — Inertia-first independence dividend field (V-03)
EVALUATOR Diagnostic 3 includes an `Inertia-first dividend` field explicitly asking whether the inertia-first ordering produced I-NN conditions that are mechanistically distinct from F-NN conditions. This is the first variation to surface the ordering effect as a labeled diagnostic finding rather than leaving it implicit.

---

### R8 Candidates

Three candidate criteria emerge from R7 excellence signals:

- **A-17 — Triple-gap joint diagnostic declared** (V-05 triple-gap pattern): The AUDITOR/post-processing role tests for triple-gap conditions and declares a count and severity level.
- **A-18 — I-NN derivation provenance recorded** (V-05 Source hop column): Each I-NN condition carries a structural origin field (source hop, source question, or source step) making derivation traceable.
- **A-19 — Cross-pool refinement tracked** (V-03 cross-pool note): Evidence refinement is tracked separately for whether claim evidence improved testability of I-NN conditions (cross-pool transfer).

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["triple-gap joint diagnostic: fifth AUDITOR row testing co-occurrence of Opaque hop + Unknown testability + I-NN scope match, producing a Triple-gap AMEND slot not derivable from A-12/A-13/A-14 individually", "I-NN source hop column: each I-NN condition carries a derivation provenance field linking it to the counter-hypothesis chain hop that generated it", "cross-pool refinement detection: explicit field tracking whether claim-focused evidence refines I-NN conditions generated independently of the claim", "inertia-first independence dividend: labeled diagnostic field asking whether inertia-first ordering produced I-NN conditions mechanistically distinct from F-NN conditions"]}
```
