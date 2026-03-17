Written to `simulations/quest/golden/corps-rob-variate-R19-2026-03-17.md`.

---

## R19 Variate Summary

**Base**: R18 V-05 (315/320 under v18). All three new axes probe the persistent gap (-5 pts, unidentified since R14).

### Variation table

| V | Axis | Hypothesis | Gap probe |
|---|------|------------|-----------|
| V-01 | Phrasing register | H-A | RULE CONDITION-ENUM Anti-pattern-2 |
| V-02 | Output format | H-B | RULE FINDING-LEDGER Anti-pattern-2 |
| V-03 | Lifecycle emphasis | H-C | CARRY FORWARD AUDIT propagation completeness |
| V-04 | Phrasing + Format | H-A + H-B | CONDITION-ENUM + FINDING-LEDGER |
| V-05 | All three | H-A + H-B + H-C | Full target -- 320/320 |

---

### Three new structural elements

**H-A -- RULE CONDITION-ENUM Anti-pattern-2** (schema-source requirement): The preamble schema is the exclusive condition-label authority for AUDIT RESULT blocks. Per-condition labels defined or rephrased inline -- even if topically matching -- are disqualifying. Closes the structural asymmetry vs RULE CONDITIONAL-ITEM and RULE AUDIT-SUITE (both 2 AP).

**H-B -- RULE FINDING-LEDGER Anti-pattern-2** (lifecycle-static ledger): A FINDING LEDGER whose lifecycle-tracking columns (Escalated To / Acknowledged By / Resolved By / Resolution) remain uniformly blank through all downstream stages is structurally initialized but lifecycle-non-functional. Closes the asymmetry vs RULE CARRY-FORWARD, RULE STAGE-HANDOFF, RULE BLOCKER-PROTOCOL (all 2 AP).

**H-C -- CARRY FORWARD AUDIT propagation completeness**: Extends the audit section from reference-validity checking ("LIDs match ledger") to propagation-completeness checking ("all open LIDs enter each carry block"). Adds an AUDIT RESULT block with three named conditions: absent carry block / prior-stage-only carry block / CARRY: NONE when open LIDs exist. V-05 also adds a **FINDING LEDGER LIFECYCLE AUDIT** section enforcing H-B compliance at the artifact level.

### Scoring prediction under v18

All five variations carry C-52 + C-53 + C-54 PASS (R18 V-05 base). If the persistent gap is any of H-A/H-B/H-C: V-05 scores 320/320.
