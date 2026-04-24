anti-patterns on RULE INERTIA-BASELINE, RULE IB-URGENCY-CASCADE, or RULE CARRY-FORWARD. The R18 additions are valid structural improvements that will generate new rubric criteria (C-52/C-53/C-54) but do not close the existing gap. Gap persists at -5.

---

### Variation-Specific Notes

**V-01 only**: RULE INERTIA-BASELINE adds Anti-pattern-2 (indistinguishable baseline pair naming the technical-locus vs behavioral-locus distinction requirement). No existing criterion in C-01–C-51 maps to this addition. C-39 unaffected (cascade constraint unchanged).

**V-02 only**: RULE IB-URGENCY-CASCADE adds Anti-pattern-2 (partial cascade compliance — satisfying 1-of-3 positions named as disqualifying form). C-39 already passes on the cascade constraint declaration; Anti-pattern-2 strengthens the rule but does not enable a new C-39 pass (C-39 was already PASS).

**V-03 only**: RULE CARRY-FORWARD adds Propagation scope declaration ("ALL open FINDING LEDGER rows entering this stage — not only findings from the immediately prior stage") and Anti-pattern-2 (prior-stage-only carry block). C-32 and C-38 unaffected; both already pass on the existing schema.

**V-04**: Inherits V-01 + V-02 changes. RULE CARRY-FORWARD remains at 1 anti-pattern (R17 V-05 form). No additional criterion impact beyond the two single-variation notes above.

**V-05**: Inherits all three. RULE CARRY-FORWARD Anti-pattern-1 relabeled from "Anti-pattern" to "Anti-pattern-1" and Anti-pattern-2 added. RULE INERTIA-BASELINE and RULE IB-URGENCY-CASCADE both at dual anti-pattern parity.

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Composite | Max |
|-----------|-----------|-------------|--------------|-----------|-----|
| V-01 | PASS | PASS | 42/43 PASS, 1 FAIL (unidentified gap) | **300** | 305 |
| V-02 | PASS | PASS | 42/43 PASS, 1 FAIL (unidentified gap) | **300** | 305 |
| V-03 | PASS | PASS | 42/43 PASS, 1 FAIL (unidentified gap) | **300** | 305 |
| V-04 | PASS | PASS | 42/43 PASS, 1 FAIL (unidentified gap) | **300** | 305 |
| V-05 | PASS | PASS | 42/43 PASS, 1 FAIL (unidentified gap) | **300** | 305 |

Golden threshold: 80% of 305 = 244. All variations clear golden.

---

## Ranking

All five variations tie at 300/305 under v17. Structural ranking (tiebreaker by completeness):

| Rank | Variation | Structural delta from R17 V-05 |
|------|-----------|-------------------------------|
| 1 | **V-05** | All three inertia-governing rules at dual AP parity; propagation scope declaration added to RULE CARRY-FORWARD |
| 2 | **V-04** | Two of three rules at dual AP parity (RULE INERTIA-BASELINE + RULE IB-URGENCY-CASCADE) |
| 3 | **V-01** | RULE INERTIA-BASELINE at dual AP parity; locus distinction named |
| 3 | **V-02** | RULE IB-URGENCY-CASCADE at dual AP parity; all-or-nothing cascade completeness named |
| 3 | **V-03** | RULE CARRY-FORWARD at dual AP parity; full-ledger propagation scope declared |

V-05 is the reference variation for this round.

---

## Excellence Signals from V-05

**Signal 1 — RULE INERTIA-BASELINE Anti-pattern-2: structural locus distinction**
V-05 names the indistinguishable-pair form as the disqualifying anti-pattern for RULE INERTIA-BASELINE. The anti-pattern declares that IB-01 must anchor to a technical locus (system/artifact/API contract being displaced) and IB-02 must anchor to a behavioral locus (workflow/habit/convention being disrupted). A pair sharing the same Status-Quo anchor under two column headers does not provide the structural contrast required for dual-baseline attribution at carry-forward and risk-register level. This closes the gap between C-19's positive zero-state mandate (RULE ZERO-STATE satisfies presence) and the content quality of the dual baselines (Anti-pattern-2 guards against coincident-structure pairs).

**Signal 2 — RULE IB-URGENCY-CASCADE Anti-pattern-2: all-or-nothing cascade completeness**
V-05 names the partial-cascade-compliance form as the disqualifying anti-pattern: a run where Go/No-Go cites IB-02 but the Risk Register carries no delay-compounding entry attributed to IB-02, or the Inertia Pressure Summary names IB-02 without the compounding path. The anti-pattern declares the cascade is position-level all-or-nothing — satisfying 1-of-3 or 2-of-3 is explicitly disqualifying. Without this anti-pattern, a generator that satisfies the Go/No-Go cascade position can consider RULE IB-URGENCY-CASCADE honored. With it, each position is independently auditable.

**Signal 3 — RULE CARRY-FORWARD Anti-pattern-2 + propagation scope: full-ledger carry**
V-05 introduces a Propagation scope declaration in RULE CARRY-FORWARD and names the prior-stage-only carry block as the disqualifying form. The scope declaration states the carry block must include ALL open FINDING LEDGER rows entering the stage — not only findings from the immediately prior stage. A carry block that is structurally complete (correct schema, Inertia ID column present, CARRY: NONE absent) but scans only stage N-1 output breaks the propagation chain for earlier-stage LIDs. The anti-pattern closes the structural gap between schema compliance (C-32 passes) and propagation completeness (only the explicit scope + anti-pattern enforces the latter).

---

## Persistent Gap Diagnostic

R18 exhausted the hypothesis that the gap lies in the first-anti-pattern parity space (R17 did that: C-49, C-50, C-51). R18 probes the dual-anti-pattern parity space for inertia-adjacent rules. Since none of H-A, H-B, H-C map to an identifiable criterion in C-01–C-51, the gap remains open.

**Implication for R19**: The gap lies in a fourth dimension not yet probed. Candidate directions:
- Rules with only 1 anti-pattern not in the inertia-adjacent group: RULE CONDITION-ENUM (1 AP), RULE FINDING-LEDGER (1 AP), RULE BOOKEND-AUDIT (1 AP), RULE SYNTHESIS (1 AP), RULE VIA-POSITION (1 AP)
- A meta-criterion about the violation taxonomy itself (e.g., violation taxonomy entries having all three fields actually populated in the Violation section, not just declared in RULE VIOLATION-TAXONOMY)
- A criterion about the CARRY FORWARD AUDIT section's structural completeness (the format includes a Carry Forward Audit block but its rubric criterion may not yet be fully satisfied)

---

## R18 Rubric Update (v18 signal pool)

| Proposed criterion | Signal source | Dependency |
|-------------------|---------------|------------|
| C-52: RULE INERTIA-BASELINE Dual Anti-Pattern Completeness | V-01 / H-A: locus-distinction anti-pattern | C-19 or inertia baseline criterion |
| C-53: RULE IB-URGENCY-CASCADE Cascade Completeness Anti-Pattern | V-02 / H-B: all-or-nothing position-level declaration | C-39 |
| C-54: RULE CARRY-FORWARD Propagation Scope Anti-Pattern | V-03 / H-C: full-ledger propagation + prior-stage-only anti-pattern | C-32 |

Max composite rises from 305 → 320 under v18. Retroactive R18 V-05 under v18 = 315/320 (C-52 + C-53 + C-54 all PASS; persistent gap still -5).

---

```json
{"top_score": 300, "all_essential_pass": true, "new_patterns": ["RULE INERTIA-BASELINE dual anti-pattern: Anti-pattern-2 names the structurally indistinguishable baseline pair (shared Status-Quo anchor or Incumbent Forces under two surface labels) as the disqualifying form, declaring that IB-01 must have a technical locus and IB-02 a behavioral locus", "RULE IB-URGENCY-CASCADE cascade completeness Anti-pattern-2: names partial cascade compliance (satisfying 1-of-3 or 2-of-3 downstream positions) as the disqualifying form; the cascade is all-or-nothing at the position level when Urgency Gradient = HIGH", "RULE CARRY-FORWARD propagation scope + Anti-pattern-2: adds an explicit full-ledger scope declaration (ALL open FINDING LEDGER rows, not only prior-stage findings) and names the prior-stage-only carry block as the disqualifying form, closing the gap between schema-correct carry blocks and propagation-complete carry blocks"]}
```
