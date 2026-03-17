# topic-echo — Round 14 Scoring (v13 Rubric)

## Rubric Context

v13 scoring model: **25 Proven criteria = 100 pts.** C-31 (Cross-layer synthesis claim coherence, 1 pt) is new and Unproven — R14 is the first opportunity for confirmation across all five variations simultaneously.

---

## Per-Variation Scoring

### V-01 — Full-Stack R14 Baseline

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-26 (archetype constraint vocabulary) | PASS | Vocabulary-class explicitly specified per archetype |
| C-27 (synthesis claim separation) | PASS | Live-inspection layer discrete and named |
| C-28 (manifest pre-populated baseline) | PASS | Baseline populated in template |
| C-29 (canonical illustration synthesis claim) | PASS | Template-complete canonical example with synthesis claim |
| C-30 (baseline entry template completeness) | PASS | Four-field structure confirmed complete |
| C-31 (cross-layer coherence audit) | PASS | Discrete post-inspection section; three layers named verbatim; COHERENT/INCOHERENT verdict gate explicit; blocking instruction on incoherence present |
| C-01–C-25 (remaining proven) | PASS | All structural baseline held constant from R13 |

**Score: 100/100 + C-31 PASS**

Canonical reference implementation — most explicit instantiation of C-31. Verbatim-restate instruction at full documentary depth.

---

### V-02 — Single-axis: Role Sequence (Check B → CAT → NGT)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-26 through C-30 | PASS | Structure held constant; axis is per-gate reorder only |
| C-31 | PASS | Audit is post-inspection and gate-order-independent; runs in fixed pre-write window regardless of gate sequence |
| NGT position effect | No degradation | NGT criterion met at later gate; accessibility window shifts but is not suppressed |

**Score: 100/100 + C-31 PASS**

Gate-order independence of C-31 confirmed: the coherence audit does not interleave with per-surprise gates, so sequence change cannot suppress it.

---

### V-03 — Single-axis: Inertia Framing

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-26 through C-30 | PASS | Inertia block is preamble-level; template structure unchanged |
| C-31 | PASS | Audit section is template-level, independent of preamble content |
| C-21 (mechanism identification precision) | PASS + Enhanced | Pre-manifest block names two failure modes (silent antagonism, archetype drift) — increases classification precision before pair inspection begins |
| C-17 (archetype taxonomy) | PASS + Amplified | Inertia framing increases classification rigor without competing with vocabulary check |

**Score: 100/100 + C-31 PASS** *(enhanced on C-21/C-17 dimensions)*

Highest analytical depth in single-axis field. Preamble-level enhancement is additive and PARALLEL to all structural criteria — no tradeoff.

---

### V-04 — Combination: Role Sequence + Inertia Framing

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-26 through C-30 | PASS | Both axes are structural-independent; combination preserves baseline |
| C-31 | PASS | Audit unchanged by either axis; gate reorder and preamble addition do not reach the post-inspection section |
| C-21 / C-17 | PASS + Enhanced | Inertia block benefit preserved in combination |
| Compound degradation | None | Axes confirmed PARALLEL; no interaction effects |

**Score: 100/100 + C-31 PASS**

Cumulative benefit of V-02 + V-03 with no degradation. Combination independence confirmed.

---

### V-05 — Combination: Role Sequence + Inertia Framing + Phrasing Register

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-26 through C-30 | PASS | Structural integrity maintained across register change |
| C-31 | PASS | Coherence audit retains: three named layers, verbatim-restate instruction (compressed to directive form), COHERENT/INCOHERENT verdict gate |
| C-21 / C-17 | PASS + Enhanced | Inertia framing preserved in conversational register |
| Register compression risk | No suppression | Directive form ("If live claim uses PARALLEL vocabulary and baseline uses PREREQUISITE vocabulary: rewrite now") encodes required check without full documentary elaboration |

**Score: 100/100 + C-31 PASS**

Minor note: C-31 verbatim-restate instruction is compressed relative to V-01's documentary form. All required structural components present; explicitness slightly lower. PASS at slightly reduced depth.

---

## Composite Rankings

| Rank | Variation | Score | C-31 | Differentiator |
|------|-----------|-------|------|----------------|
| 1 | V-03 | 100 | PASS | Highest analytical richness — C-21/C-17 amplified, single clean axis |
| 2 | V-04 | 100 | PASS | Cumulative V-02+V-03 gains, no degradation — confirms PARALLEL independence |
| 3 | V-01 | 100 | PASS | Canonical reference; most explicit C-31 audit depth |
| 4 | V-02 | 100 | PASS | Clean structural purity; confirms gate-order independence of C-31 |
| 5 | V-05 | 100 | PASS | All criteria met; C-31 slightly compressed in directive form |

All five variations achieve **100/100 + C-31 PASS**. Differentiation is at the excellence signal level. Top rank to V-03 on analytical depth enhancement; V-04 second on confirmed combination safety.

---

## Excellence Signals (from V-03 / top field)

### Signal 1 — C-31 Universally Confirmed Across All Axes
R14 is the first round all five variations simultaneously pass C-31. The cross-layer coherence audit survives gate reorder (V-02), inertia framing (V-03), combination (V-04), and register change (V-05) without suppression. C-31 is now a confirmed baseline expectation rather than a candidate, paralleling what R13 did for C-30.

### Signal 2 — C-31 Register-Independence Established
V-05 confirms that the conversational imperative register compresses the verbatim-restate instruction to directive form without losing the structural enforcement requirement. The audit retains all three named layers and the verdict gate. C-31 is format-independent — the coherence check survives reformatting.

### Signal 3 — Inertia Framing as Preamble-Level Amplifier
V-03 and V-04 confirm that naming specific failure modes before pair inspection (silent mechanism antagonism, archetype drift) improves C-21 analytical depth and C-17 archetype taxonomy without competing with any template-level criterion. The pattern is: a well-specified failure-mode preamble is fully PARALLEL to structural criteria and has no tradeoff cost.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-31 cross-layer coherence audit confirmed universal across all axis variations — gate order, inertia framing, and register change do not suppress audit structure; C-31 is format-independent and gate-order-independent", "Inertia framing (pre-manifest failure-mode block naming silent antagonism and archetype drift) amplifies analytical depth criteria (C-21, C-17) without structural competition — confirmed PARALLEL property across single-axis and combination variations"]}
```
