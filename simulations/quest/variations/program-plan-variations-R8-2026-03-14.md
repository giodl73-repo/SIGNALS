Written to `simulations/quest/rubrics/program-plan-rubric-v8-R8-variate-2026-03-15.md`.

---

## program-plan — R8 Variate Prompt Bodies (V-01 through V-05)

All five variations inherit R7 V-05's full structural payload (205/205 under v8). New axes isolate three single-axis extensions of the C-31 lineage-and-justification family, then combine.

---

### Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Artifact Consumer Map | Single-hop lineage (producer→immediate gate) hides multi-stage dependencies. A Consumer Map tracing every artifact to ALL downstream consumers makes the dependency graph a lattice. Discriminating signal: at least one non-adjacent consumer traced. |
| **V-02** | Stage Arc-Uniqueness Register | C-28 asks "why can't it run earlier?"; C-29 asks "why these skills together?" Neither asks "why can't this stage be absent?" Arc-Uniqueness forces each stage to declare its irreplaceable evidence contribution + permanent arc gap on removal. |
| **V-03** | Gate Threshold Calibration | C-10 verifies N exists; C-13 verifies syntax. Neither requires reasoning for why this N. Threshold Calibration forces per-gate N-selection with minimum-floor + topic-specific choice rationale — making N a deliberate design decision. |
| **V-04** | V-01 + V-02 | Consumer Map and Arc-Uniqueness are orthogonal: graph-level dependency vs. arc-level contribution. Combined without interference. |
| **V-05** | V-01 + V-02 + V-03 + Gate Semantic Claim | All three + a fourth axis: each gate includes an `asserting:` clause — the evidence state asserted when the threshold passes, not just the count. Extended gate format: `"[producing skill]; [actor] hands off when >=N... -- asserting: [evidence claim] -- removing this gate: [cascade] -- and gate N+1 loses: [adjacent]"` |

---

### New structural elements per variation

**V-01 new step:** Step 7 — Artifact Consumer Map (pre-YAML). Table: `Artifact Type | Producing Skill | Producing Stage | All Downstream Consumers`. Requires at least one non-adjacent consumer. Gate format unchanged (R7 V-05 lineage prefix retained).

**V-02 new step:** Step 6 — Stage Arc-Uniqueness Register (pre-YAML, after Cohesion Audit Table). Table: `Stage Name | Unique Arc Contribution | Arc Evidence Gap if Stage Removed (2+ hop)`. "Contribution" must be an evidence assertion, not a skill list. "Gap" requires -> notation, 2+ hops, arc-layer crossing. Gate format unchanged.

**V-03 new step:** Step 8 — Gate Threshold Calibration (pre-gate-format, after Gate Cascade Audit). Table: `Gate | Minimum N for Valid Signal | Chosen N | Calibration Rationale`. Minimum N states the floor with topic-specific reason. Rationale must reference topic characteristics — generic rationales fail. Calibrated N flows into gate string. Gate format unchanged.

**V-05 additional step:** Step 10 — Semantic Gate Claims (pre-gate-format). Table: `Gate | Semantic Evidence Claim`. Claim states what is now true about the evidence state when the threshold passes. Count restatements fail. Extended gate format adds `-- asserting: [claim] --` between threshold and cascade clause.

---

### R8 design principles

| Signal | Pattern | Extends |
|--------|---------|---------|
| R8-01 Artifact Consumer Map | Full consumer graph per artifact, non-adjacent trace required | C-31 (producer per gate) → all consumers per artifact |
| R8-02 Stage Arc-Uniqueness Register | Irreplaceability justification per stage: evidence contribution + arc gap | C-28 (displacement: why can't it run earlier?) → uniqueness (why can't it be absent?) |
| R8-03 Gate Threshold Calibration | N-selection reasoning per gate with minimum floor + topic rationale | C-10 (N exists) + C-13 (syntax instructed) → N is deliberate design choice |
| R8-04 Gate Semantic Claim | Evidence state assertion embedded in gate string as `asserting:` clause | C-16/C-22/C-24 (gate template structure) → gate as semantic assertion over evidence state |

**Orthogonality:** Consumer Map (dependency graph), Arc-Uniqueness (stage contribution), Threshold Calibration (threshold reasoning), Semantic Claim (gate meaning) are structurally independent axes with no expected interference.

**V-05 retroactive under current v8:** 205/205 (inherits full R7 V-05 payload + four new axes). V-04 would introduce two new axes; V-01/V-02/V-03 each one. C-31 (the R8 anchor) is already passing at baseline for all five variations — the new axes extend beyond it, setting up v9 discriminators.
