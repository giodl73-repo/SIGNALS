I have all the data needed. Now I'll score all five variations.

---

## flow-throttle — Round 7 Scorecard (v7 Rubric, 148-point max)

### Criterion Trace — Evidence per Variation

All five variations share identical Round 1 structure (PHASES 1–4, TABLES 1–10, GATES 1–3). The only axis of variation is the Round 2 pre-barrier container header and its placement relative to the `## ROUND 2` heading.

---

#### Essential Criteria (C-01 to C-05, max 60)

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 Bottleneck Localization | 12 | PASS | PASS | PASS | PASS | PASS |
| C-02 Rate Limit Hit Ordering | 12 | PASS | PASS | PASS | PASS | PASS |
| C-03 Backpressure Propagation Trace | 12 | PASS | PASS | PASS | PASS | PASS |
| C-04 UX per Throttle Tier | 12 | PASS | PASS | PASS | PASS | PASS |
| C-05 Domain Grounding in PA/Connectors | 12 | PASS | PASS | PASS | PASS | PASS |

Evidence: TABLE 1 domain rule names exact PA construct types; TABLE 2 provides ordered bottleneck analysis with arithmetic; TABLE 3 traces propagation hops; TABLE 4 maps distinct UX categories per tier. Identical across all five variations. **All pass: 60 pts.**

---

#### Recommended Criteria (C-06 to C-08, max 30)

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-06 Unprotected Burst Path Detection | 10 | PASS | PASS | PASS | PASS | PASS |
| C-07 Missing Retry-After Handling | 10 | PASS | PASS | PASS | PASS | PASS |
| C-08 Cascade Risk Register | 10 | PASS | PASS | PASS | PASS | PASS |

Evidence: TABLE 5 (burst path register with PA construct type + why it bypasses tier-1 guard), TABLE 6 (Retry-After gaps with failure modes), TABLE 7 (cascade register, minimum 2 pairs with mechanism + severity). All identical. **All pass: 30 pts.**

---

#### Advisory Criteria (C-09 to C-13, max 20)

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-09 PA-Specific Remediations | 6 | PASS | PASS | PASS | PASS | PASS |
| C-10 Monitoring and Alerting | 5 | PASS | PASS | PASS | PASS | PASS |
| C-11 License/Entitlement Boundary | 4 | PASS | PASS | PASS | PASS | PASS |
| C-12 Throttle Budget Projection | 3 | PASS | PASS | PASS | PASS | PASS |
| C-13 Test and Validation Approach | 2 | PASS | PASS | PASS | PASS | PASS |

Evidence: TABLE 10 (>=2 PA-native remediations, each mapped to a finding); Section 4.E names PA-observable signals; Section 4.F names entitlement boundary with scenario impact; TABLE 9 requires arithmetic for >=1 row; Section 4.G requires concrete PA test method. All identical. **All pass: 20 pts.**

---

#### Structural Criteria (C-14 to C-16, max 8)

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-14 Gate Mechanism | 4 | PASS | PASS | PASS | PASS | PASS |
| C-15 Non-Deference Sentence | 2 | PASS | PASS | PASS | PASS | PASS |
| C-16 Scope Extension Declaration | 2 | PASS | PASS | PASS | PASS | PASS |

Evidence for C-14: GATE 1/2/3 each carry (a) label, (b) conditional prerequisite, (c) named blocked target ("PHASE N is blocked until..."). C-20 confirmed prose gates satisfy C-14 — tabular format not required. Evidence for C-15: `**Independence:**` sentence in every pre-barrier block names Round 1 and asserts confidence-is-not-evidence. Evidence for C-16: `**Scope extension:**` names the closed-window exclusion and structural reason in every variation. **All pass: 8 pts.**

---

#### Aspirational v4 Criteria (C-17 to C-20, max 12)

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-17 Pre-Barrier Independence Placement | 3 | PASS | PASS | PASS | PASS | PASS |
| C-18 Structural Closure Reason | 3 | PASS | PASS | PASS | PASS | PASS |
| C-19 Label-Enforced Co-location | 3 | PASS | PASS | PASS | PASS | PASS |
| C-20 Gate Mechanism Prose Portability | 3 | PASS | PASS | PASS | PASS | PASS |

Evidence: C-17 — Independence sentence precedes TABLE 11 in all variations. C-18 — "excluded from Round 1's execution window because Round 1 closed before TABLE 8 corrections were finalized" is the structural closure reason. C-19 — `**Independence:**` and `**Scope extension:**` are distinct labeled entries in all pre-barrier blocks. C-20 — GATE prose carries all three elements. **All pass: 12 pts.**

---

#### Aspirational v5 Criteria (C-21 to C-22, max 6)

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-21 Pre-Barrier Container Name Encodes Positional Role | 3 | PASS | PASS | PASS | PASS | PASS |
| C-22 Pre-Barrier Labeled Pair Co-location | 3 | PASS | PASS | PASS | PASS | PASS |

Evidence for C-21: "PRE-EVALUATION" prefix satisfies the positional qualifier requirement in all variations. V-04 uses "PRE-EVALUATION DIRECTIVES" — still encodes positional role. C-22: labeled `**Independence:**` + `**Scope extension:**` co-located in the pre-barrier section, before TABLE 11. **All pass: 6 pts.**

---

#### Aspirational v6 Criteria (C-23 to C-24, max 6)

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-23 Pre-Barrier Block Dual-Dimension Completeness | 3 | PASS | PASS | PASS | PASS | PASS |
| C-24 Cross-Generation Labeled-Pair Coverage | 3 | PASS | PASS | PASS | PASS | PASS |

Evidence: C-23 requires C-21 AND C-22 from the same block — all pass both. C-24 requires C-19 AND C-22 — all have labeled pairs in pre-barrier position satisfying both generations. **All pass: 6 pts.**

---

#### Aspirational v7 Criteria (C-25 to C-26, max 6)

This is the discriminating band. Evidence from the Round 2 section in each variation:

**V-01** — `### PRE-EVALUATION ASSERTIONS` (no phrase). Immediately follows `## ROUND 2` heading.
- C-25: FAIL — positional qualifier "PRE-EVALUATION" present (C-21 satisfied), but no boundary-event phrase ("before X begins" or "execute before entering X") in the name.
- C-26: PASS — container is the first element under the Round 2 heading. Zero intervening content.

**V-02** — `### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` but preceded by: *"Round 1 produced a complete throttle impact analysis. Round 2 now applies an independent structural precision check to the constructs and cascade pairs identified above."*
- C-25: PASS — temporal form "before any Round 2 construct evaluation begins" present.
- C-26: FAIL — one transitional sentence intervenes between the `## ROUND 2` heading and the pre-barrier container. Adjacency violated.

**V-03** — `### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` immediately after `## ROUND 2` heading.
- C-25: PASS — temporal form explicitly present.
- C-26: PASS — zero intervening content; heading-to-container adjacency intact.

**V-04** — `### PRE-EVALUATION DIRECTIVES (execute before entering Round 2 evaluation)` immediately after `## ROUND 2` heading.
- C-25: PASS — imperative form "execute before entering Round 2 evaluation" present.
- C-26: PASS — zero intervening content; heading-to-container adjacency intact.

**V-05** — `### PRE-EVALUATION ASSERTIONS` (no phrase), preceded by: *"Round 1 produced a complete throttle impact analysis. Round 2 applies an independent structural precision check to the constructs and cascade pairs identified above."*
- C-25: FAIL — positional qualifier only, no boundary-event phrase.
- C-26: FAIL — transitional sentence intervenes before the pre-barrier container.

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-25 Pre-Barrier Container Boundary-Event Declaration | 3 | FAIL | PASS | PASS | PASS | FAIL |
| C-26 Pre-Barrier Block Round-Head Immediacy | 3 | PASS | FAIL | PASS | PASS | FAIL |

---

### Composite Scores

| Variation | C-01..C-24 (142) | C-25 (3) | C-26 (3) | **Total / 148** |
|-----------|-----------------|----------|----------|----------------|
| V-01 | 142 | 0 | 3 | **145** |
| V-02 | 142 | 3 | 0 | **145** |
| V-03 | 142 | 3 | 3 | **148** |
| V-04 | 142 | 3 | 3 | **148** |
| V-05 | 142 | 0 | 0 | **142** |

Predicted scores confirmed exactly: 148 / 145 / 142 three-level spread.

---

### Ranking

1. **V-03 and V-04 — 148/148** (tied ceiling)
2. **V-01 and V-02 — 145/148** (tied, single-criterion miss)
3. **V-05 — 142/148** (double miss, prior-generation ceiling)

---

### Excellence Signals from V-03 and V-04

**What made the top-scoring variations better:**

1. **Dual-layer container name** — The header encodes both the *positional role* (C-21: "PRE-EVALUATION...") and the *execution trigger* (C-25: "before X begins" / "execute before entering X") in a single name. The two dimensions are orthogonal: position says *where*, boundary-event phrase says *when*. V-03 uses temporal form ("before any Round 2 construct evaluation begins"); V-04 uses imperative form ("execute before entering Round 2 evaluation"). Both satisfy C-25, confirming no form-specificity.

2. **Round-head immediacy** (C-26) — The pre-barrier container is structurally adjacent to the Round 2 heading with zero intervening content. No transitional sentence, no preamble, no meta-commentary. This makes structural priority machine-verifiable from heading position alone — an analyst or automated checker can confirm pre-barrier placement without reading the block's content.

3. **Form equivalence confirmed** — V-03 temporal and V-04 imperative both reach 148. C-25 has no hidden preference for one phrasing form. This closes the form-disambiguation question raised in the R7 design notes.

4. **Independence arithmetic holds** — V-05 scores exactly 142, not lower. C-25 and C-26 each carry independent 3-pt weight with no hidden cascade into earlier criteria. V-01 (-3 for C-25 only) and V-02 (-3 for C-26 only) confirm the split is clean.

---

```json
{"top_score": 148, "all_essential_pass": true, "new_patterns": ["dual-layer container name: positional qualifier plus boundary-event phrase in same header encodes both position and execution trigger", "round-head immediacy: pre-barrier container immediately after Round 2 heading with zero intervening content makes structural priority machine-verifiable", "temporal and imperative boundary-event forms are equivalent: both satisfy C-25 with no form-specificity"]}
```
