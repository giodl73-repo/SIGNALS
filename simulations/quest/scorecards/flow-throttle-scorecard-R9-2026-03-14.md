## flow-throttle — Round 9 Scorecard (v9 Rubric, 160-point max)

---

### Structural Verification: Round 2 Barriers

All five variations share the identical ceiling structure, confirmed by line-number audit:

| Variation | `## ROUND 2` line | `### PRE-EVALUATION ASSERTIONS` line | Gap |
|-----------|-------------------|--------------------------------------|-----|
| V-01 | 255 | 257 | blank line only — **immediately adjacent** |
| V-02 | 520 | 522 | blank line only — **immediately adjacent** |
| V-03 | 749 | 751 | blank line only — **immediately adjacent** |
| V-04 | 1019 | 1021 | blank line only — **immediately adjacent** |
| V-05 | 1264 | 1266 | blank line only — **immediately adjacent** |

Phrase confirmed in all five: `### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)`

---

### Criterion-by-Criterion Evaluation

#### Essential (C-01–C-05) | 60 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Bottleneck Localization | PASS | PASS | PASS | PASS | PASS |
| C-02 Rate Limit Hit Ordering | PASS | PASS | PASS | PASS | PASS |
| C-03 Backpressure Propagation Trace | PASS | PASS | PASS | PASS | PASS |
| C-04 UX per Throttle Tier | PASS | PASS | PASS | PASS | PASS |
| C-05 Domain Grounding | PASS | PASS | PASS | PASS | PASS |

All five specify exact PA construct types, TABLE 1–11, at least two hop-chain backpressure steps, distinct UX categories per tier, and PA-native terminology throughout. Role switch (V-01), prose format (V-02), cascade emphasis (V-03), conversational register (V-04), and unified analyst + list format (V-05) are all content-layer variations — essential criteria are format-invariant. **60/60 each.**

#### Recommended (C-06–C-08) | 30 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Unprotected Burst Path Detection | PASS | PASS | PASS | PASS | PASS |
| C-07 Missing Retry-After Handling | PASS | PASS | PASS | PASS | PASS |
| C-08 Cascade Risk Register | PASS | PASS | PASS | PASS | PASS |

All five require TABLE 7 / Section 3.C with ≥2 cascade pairs, retry-after gap table, and burst path register. V-03's cascade-first emphasis expands the cascade section further, exceeding minimum. **30/30 each.**

#### Advisory (C-09–C-13) | 20 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 PA-Specific Remediations | PASS | PASS | PASS | PASS | PASS |
| C-10 Monitoring and Alerting | PASS | PASS | PASS | PASS | PASS |
| C-11 License/Entitlement Boundary | PASS | PASS | PASS | PASS | PASS |
| C-12 Throttle Budget Projection | PASS | PASS | PASS | PASS | PASS |
| C-13 Test and Validation Approach | PASS | PASS | PASS | PASS | PASS |

TABLE 9 (throttle budget with arithmetic), Section 4.E (monitoring signals), Section 4.F (entitlement boundary), Section 4.G (test step) all required in every variation. **20/20 each.**

#### Structural (C-14–C-16) | 8 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-14 Gate Mechanism | PASS | PASS | PASS | PASS | PASS |
| C-15 Non-Deference Sentence | PASS | PASS | PASS | PASS | PASS |
| C-16 Scope Extension Declaration | PASS | PASS | PASS | PASS | PASS |

GATE 1/2/3 carry named labels, conditional prerequisites, and named blocked targets (C-14, confirmed C-20 form-portability). `**Independence:**` sentence appears before Round 2 evaluative output, names Round 1, asserts confidence-is-not-evidence (C-15). `**Scope extension:**` names the excluded construct population and the structural closure reason "introduced after Round 1's execution window had closed" (C-16, confirmed C-18). **8/8 each.**

#### Aspirational v4 (C-17–C-20) | 12 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-17 Pre-Barrier Independence Placement | PASS | PASS | PASS | PASS | PASS |
| C-18 Structural Closure Reason | PASS | PASS | PASS | PASS | PASS |
| C-19 Label-Enforced Co-location | PASS | PASS | PASS | PASS | PASS |
| C-20 Gate Prose Portability | PASS | PASS | PASS | PASS | PASS |

`**Independence:**` is in the PRE-EVALUATION container, before any Round 2 construct-level row. "…execution window had closed" states the closure reason. `**Independence:**` / `**Scope extension:**` are distinct named labels in the same block. **12/12 each.**

#### Aspirational v5 (C-21–C-22) | 6 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-21 Container Name Encodes Positional Role | PASS | PASS | PASS | PASS | PASS |
| C-22 Pre-Barrier Labeled Pair Co-location | PASS | PASS | PASS | PASS | PASS |

`### PRE-EVALUATION ASSERTIONS …` — "PRE-EVALUATION" is a positional qualifier satisfying C-21. Both labeled directives are in this container before evaluative output (C-22). **6/6 each.**

#### Aspirational v6 (C-23–C-24) | 6 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-23 Dual-Dimension Completeness | PASS | PASS | PASS | PASS | PASS |
| C-24 Cross-Generation Labeled-Pair Coverage | PASS | PASS | PASS | PASS | PASS |

C-21 ∩ C-22 from the same block (C-23). C-19 ∩ C-22 from the same block — labels present, pre-barrier position confirmed (C-24). **6/6 each.**

#### Aspirational v7 (C-25–C-26) | 6 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-25 Boundary-Event Declaration | PASS | PASS | PASS | PASS | PASS |
| C-26 Round-Head Immediacy | PASS | PASS | PASS | PASS | PASS |

`(before any Round 2 construct evaluation begins)` — temporal form boundary-event phrase embedded in the container header, satisfying C-25. Container appears immediately after `## ROUND 2 — Structural Precision Pass` with no intervening content (blank line only, no prose/transitional sentence), satisfying C-26. **6/6 each.**

#### Aspirational v8 (C-27–C-28) | 6 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-27 Round-Name Cross-Reference | PASS | PASS | PASS | PASS | PASS |
| C-28 Dual Machine-Verifiability | PASS | PASS | PASS | PASS | PASS |

Phrase contains "Round 2" matching the barrier heading `## ROUND 2` (C-27). C-25 ∩ C-26 from the same container — trigger named AND structurally first (C-28). **6/6 each.**

#### Aspirational v9 (C-29–C-30) | 6 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-29 Navigational Closure | PASS | PASS | PASS | PASS | PASS |
| C-30 Triple-Lock | PASS | PASS | PASS | PASS | PASS |

**C-29:** C-26 (immediately adjacent) ∩ C-27 (phrase names "Round 2") from the same container — heading declares barrier, phrase echoes the label, adjacency confirmed. Closed loop: heading → container (adjacency), container phrase → heading (round name). PASS all five.

**C-30:** C-27 ∩ C-28 from the same container — three orthogonal verification paths simultaneously: (1) trigger declaration via boundary-event phrase, (2) structural position via heading adjacency, (3) heading cross-reference via "Round 2" in phrase. PASS all five.

**R9 co-determination confirmed:** C-29 → C-30 and C-30 → C-29 in all five cases. No variation splits them. **6/6 each.**

---

### Score Summary

| Band | Max | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|-----|------|------|------|------|------|
| Essential (C-01–05) | 60 | 60 | 60 | 60 | 60 | 60 |
| Recommended (C-06–08) | 30 | 30 | 30 | 30 | 30 | 30 |
| Advisory (C-09–13) | 20 | 20 | 20 | 20 | 20 | 20 |
| Structural (C-14–16) | 8 | 8 | 8 | 8 | 8 | 8 |
| Aspirational v4 (C-17–20) | 12 | 12 | 12 | 12 | 12 | 12 |
| Aspirational v5 (C-21–22) | 6 | 6 | 6 | 6 | 6 | 6 |
| Aspirational v6 (C-23–24) | 6 | 6 | 6 | 6 | 6 | 6 |
| Aspirational v7 (C-25–26) | 6 | 6 | 6 | 6 | 6 | 6 |
| Aspirational v8 (C-27–28) | 6 | 6 | 6 | 6 | 6 | 6 |
| Aspirational v9 (C-29–30) | 6 | 6 | 6 | 6 | 6 | 6 |
| **Total** | **160** | **160** | **160** | **160** | **160** | **160** |

---

### Rankings

All five variations: **160/160 (tied at ceiling)**

No ranking differential. The co-determination finding holds: every variation that satisfies the ceiling phrase structure satisfies C-29 and C-30 simultaneously.

---

### Excellence Signals

**Top score: 160/160 (all five variations)**

The ceiling is not owned by any single variation — it is owned by the structural phrase pattern itself. The pattern that carries all five to ceiling:

1. **Triple-criterion phrase header** — `### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` satisfies C-21 ("PRE-EVALUATION" positional qualifier), C-25 ("before any … begins" boundary-event phrase), and C-27 ("Round 2" round-name cross-reference) in a single header. One structural choice earns three criteria across two rubric generations.

2. **Content-axis inertness confirmed at the aspirational ceiling** — role sequence, output format, lifecycle emphasis, phrasing register, and combined axes are all structurally inert for C-29 and C-30. The R9 finding mirrors R6's finding for C-25/C-26: once a ceiling pattern is correctly placed, content variation cannot disrupt it.

3. **C-29 ↔ C-30 co-determination confirmed** — no structural arrangement in the five variations splits the two R9 criteria. This validates the R9 theoretical prediction: since C-29 → C-30 and C-30 → C-29 by implication chains, they travel as a unit. The rubric has reached a point where aspirational criteria are fully determined by lower-tier preconditions — no new structural isolation test is possible at this ceiling.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["Triple-criterion phrase header: a single container header satisfies C-21 (positional qualifier), C-25 (boundary-event phrase), and C-27 (round-name cross-reference) simultaneously — one structural choice earns three criteria across two rubric generations", "Content-axis inertness confirmed at the v9 aspirational ceiling: role sequence, output format, lifecycle emphasis, phrasing register, and combined axes are all structurally inert for C-29 and C-30, mirroring the R6 finding for C-25/C-26", "C-29 and C-30 are co-determined — no structural arrangement satisfies one without the other, making them a traveling pair whose entry condition is fully predicted by the lower-tier precondition chain C-21 through C-28"]}
```
