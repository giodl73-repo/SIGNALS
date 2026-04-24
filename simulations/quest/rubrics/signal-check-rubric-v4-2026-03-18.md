Reading the R3 scorecard excellence signals to extract new criteria.

From the scorecard, three distinct new patterns emerge that aren't yet captured as criteria:

1. **Verbatim phrases at point of use** — C-15 requires verbatim phrases exist; V-02 satisfies it via a reference table, V-05 embeds them inline. The excellence signal names this as a stronger compliance form (removes table-lookup dependency).
2. **Advisory register carried structurally** — V-05's preflight/pilot framing embeds the advisory register in vocabulary and section labels, not just a top-of-file disclaimer. Goes beyond C-05 (which only requires advisory register be present).
3. **Triple enforcement stack declared as a unit** — C-14 + C-15 + C-16 address three independent failure modes and none substitutes for another. An output that names this interdependency explicitly is more robust than one that happens to pass all three independently.

That yields C-17, C-18, C-19. Aspirational tier grows from 8 to 11; denominator in formula updates accordingly.

---

# signal-check Rubric — v4 (2026-03-18)

Evaluates the output of `/signal:check` against quality criteria derived from iterative design experiments. Three tiers: Essential (gate), Recommended (depth), Aspirational (excellence). Gold requires all essential passing and composite >= 80.

---

## Criterion Summary

**5 Essential** — all must pass for the output to be a usable health report:

| ID | Criterion |
|----|-----------|
| C-01 | All four dimensions present (SEQUENCE, COHERENCE, STALENESS, CAUSAL GAP) |
| C-02 | SEQUENCE grounded in artifact dates, not assumed ordering |
| C-03 | COHERENCE names specific signal pairs — not generic "seems aligned" |
| C-04 | CAUSAL GAP states mechanism evidence or explicitly names the absence |
| C-05 | Advisory/coaching register throughout — no blocking verdicts |

**3 Recommended** — meaningfully better with all three:

| ID | Criterion |
|----|-----------|
| C-06 | STALENESS applies a named, concrete age threshold |
| C-07 | Every flagged issue includes a next action |
| C-08 | Report opens with a readiness summary before dimension analysis |

**11 Aspirational** — raise the bar once essentials are stable. C-09 and C-10 retained from v1; C-11 through C-13 added from R1; C-14 through C-16 added from R2; C-17 through C-19 added from R3:

| ID | Criterion | Source |
|----|-----------|--------|
| C-09 | Cross-dimension patterns named when a shared root cause exists | v1 |
| C-10 | Missing signals identified by namespace + specific skill | v1 |
| C-11 | All skill references use `/namespace:skill` format consistently | EX-01 |
| C-12 | A terminal MISSING SIGNAL GUIDE section collates all gaps | EX-02 |
| C-13 | Absent evidence is declared explicitly — no dimension silently omits | EX-03 |
| C-14 | A named STANDING RULES block precedes all inventory and analysis | EX-04 |
| C-15 | Each dimension specifies required verbatim absence phrases | EX-05 |
| C-16 | Every constraint explicitly enumerates all output locations it governs | EX-06 |
| C-17 | Verbatim absence phrases are embedded at point of use within each dimension | R3-EX-01 |
| C-18 | Advisory register is carried structurally through framing vocabulary, not only declared | R3-EX-02 |
| C-19 | The triple enforcement stack (C-14 + C-15 + C-16) is declared as a unit with interdependency named | R3-EX-03 |

**Golden threshold**: all 5 essential pass + composite >= 80.

---

## Criterion Detail

### Essential (C-01 to C-05)

*(unchanged from v3)*

### Recommended (C-06 to C-08)

*(unchanged from v3)*

### Aspirational (C-09 to C-19)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09–C-16 | *(unchanged from v3)* | | |
| C-17 | Verbatim absence phrases embedded at point of use | correctness | The verbatim absence phrases required by C-15 appear inline within each dimension's instruction block — not solely in a pre-analysis reference table. Embedding phrases at point of use removes the table-lookup dependency; an output that satisfies C-15 via a standalone reference table does not satisfy C-17. An output satisfying C-17 automatically satisfies C-15; the converse is not true. Derived from R3: verbatim-phrase-at-point-of-use outperforms reference-table for C-15 compliance. |
| C-18 | Advisory register carried structurally through framing vocabulary | register | The advisory/coaching register required by C-05 is expressed through the structural vocabulary of the output — section headings, dimension labels, and status fields use framing language (e.g., preflight/pilot/clearance, coaching check, advisory) rather than relying solely on a top-of-file disclaimer. A disclaimer alone satisfies C-05 but not C-18; structural framing prevents register drift across the output more reliably than declaration alone. Derived from R3: preflight/pilot framing in V-05 carries the advisory register structurally, not just declaratively. |
| C-19 | Triple enforcement stack declared as a unit with interdependency named | coherence | The output or skill instruction explicitly names C-14, C-15, and C-16 (or their functional equivalents — named preamble block, verbatim phrases per dimension, full location enumeration) as a coordinated enforcement stack, and states that the three mechanisms address independent failure modes such that no layer substitutes for another. Passing all three independently without naming their interdependency does not satisfy C-19. Derived from R3: the triple enforcement stack addresses three distinct failure modes; no two layers substitute for the third. |

---

## Composite Score Formula

```
composite = (essential_pass / 5  * 60)
          + (recommended_pass / 3  * 30)
          + (aspirational_pass / 11 * 10)
```

| Tier | Criteria | Weight | Points each |
|------|----------|--------|-------------|
| Essential | 5 | 60 pts | 12.00 pts |
| Recommended | 3 | 30 pts | 10.00 pts |
| Aspirational | 11 | 10 pts | ~0.91 pts |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-17 | Initial — 5E / 3R / 2A |
| v2 | 2026-03-17 | +C-11 to C-13 from R1 excellence signals |
| v3 | 2026-03-18 | +C-14 to C-16 from R2 excellence signals |
| v4 | 2026-03-18 | +C-17 to C-19 from R3 excellence signals; aspirational denominator 8 → 11 |
