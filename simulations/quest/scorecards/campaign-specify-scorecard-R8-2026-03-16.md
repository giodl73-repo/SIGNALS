# Quest Score — campaign-specify / Round 8 / Rubric v8

## Scoring Basis

**Inherited from R7 V-05 base**: 5/5 essential, 3/3 recommended, 24/26 aspirational (C-27, C-28, C-29, C-32 earned; C-33, C-34 unearned).

Each R8 variation is evaluated on whether its single structural change earns the targeted gap criterion/criteria, with all other positions inherited.

---

## Per-Criterion Scoring (Aspirational Gap Focus)

### C-33 — Per-Audience Verdicts in Voice Compliance Audit

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Explicitly expands the single combined audit line into three separate rows: `Exec verdict / Dev verdict / Maker verdict`. This is the minimal mechanical change required by C-33. |
| V-02 | **FAIL** | Voice Compliance Audit section unchanged from R7 V-05 — single combined line. C-33 not targeted by V-02. |
| V-03 | **PASS** | Three per-audience audit rows with Step 0c contract attribution per row (`Exec verdict: [Pass/Fail] — Step 0c exec voice contract verified`). Richer than V-01 but still earns C-33 — separate rows present. |
| V-04 | **PASS** | Inherits V-01's three bare per-audience rows. C-33 satisfied. |
| V-05 | **PASS** | Inherits V-03's richer form (three rows with contract attribution). C-33 satisfied with maximum traceability. |

---

### C-34 — Step 0c Contract Anchor in Gate Parenthetical Pass Condition

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **FAIL** | Gate Step 3 Pass parentheticals unchanged — behavioral test only, no contract name. C-34 not targeted. |
| V-02 | **PASS** | Prefixes each Pass parenthetical with `Step 0c [audience] voice contract satisfied:`. The contract name now appears inside the parenthetical — satisfies C-34's explicit requirement. |
| V-03 | **FAIL** | Gate Step 3 unchanged — behavioral criteria only, no contract attribution in parenthetical. C-34 not targeted. |
| V-04 | **PASS** | Inherits V-02's parenthetical contract anchor. C-34 satisfied. |
| V-05 | **PASS** | Inherits V-02's gate change. C-34 satisfied. |

---

## Essential Criteria — All Variations

All variations inherit R7 V-05's essential baseline. No variation removes or alters artifacts, sections, options, audience coverage, or cross-artifact consistency.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Three artifacts produced | PASS | PASS | PASS | PASS | PASS |
| C-02 | Spec has all six required sections | PASS | PASS | PASS | PASS | PASS |
| C-03 | Proposal has 3+ options incl. do-nothing | PASS | PASS | PASS | PASS | PASS |
| C-04 | Pitch covers three audience versions | PASS | PASS | PASS | PASS | PASS |
| C-05 | Cross-artifact consistency | PASS | PASS | PASS | PASS | PASS |

**Essential**: 5/5 across all variations.

---

## Recommended Criteria — All Variations

All variations inherit R7 V-05's recommended baseline.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Spec self-review flags gaps | PASS | PASS | PASS | PASS | PASS |
| C-07 | Pitch contains anti-positioning section | PASS | PASS | PASS | PASS | PASS |
| C-08 | Proposal recommendation cites trade-off rationale | PASS | PASS | PASS | PASS | PASS |

**Recommended**: 3/3 across all variations.

---

## Aspirational Criteria Summary

Inherited 24/26 from R7 V-05. Gap criteria C-33 and C-34 scored above.

| Variation | C-27 | C-28 | C-29 | C-32 | C-33 | C-34 | Other (20) | Total |
|-----------|------|------|------|------|------|------|-----------|-------|
| V-01 | PASS | PASS | PASS | PASS | PASS | FAIL | 20 PASS | **25/26** |
| V-02 | PASS | PASS | PASS | PASS | FAIL | PASS | 20 PASS | **25/26** |
| V-03 | PASS | PASS | PASS | PASS | PASS | FAIL | 20 PASS | **25/26** |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | 20 PASS | **26/26** |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | 20 PASS | **26/26** |

---

## Composite Scores

```
composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 26 * 10)
```

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60.00 | 30.00 | 9.615 | **99.6** |
| V-02 | 60.00 | 30.00 | 9.615 | **99.6** |
| V-03 | 60.00 | 30.00 | 9.615 | **99.6** |
| V-04 | 60.00 | 30.00 | 10.000 | **100.0** |
| V-05 | 60.00 | 30.00 | 10.000 | **100.0** |

---

## Ranking

| Rank | Variation | Score | Gap Earned |
|------|-----------|-------|------------|
| 1 | **V-05** | 100.0 | C-33 + C-34, with bidirectional contract attribution |
| 1 | **V-04** | 100.0 | C-33 + C-34, minimal path |
| 3 | V-01 | 99.6 | C-33 only |
| 3 | V-02 | 99.6 | C-34 only |
| 3 | V-03 | 99.6 | C-33 only (richer form) |

V-04 and V-05 tie at 100.0. V-05 is the preferred design choice: its contract attribution per audit row creates bidirectional traceability absent in V-04's bare rows, and this structural density has no scoring cost.

---

## Excellence Signals (from V-05)

**1. Bidirectional contract anchoring closes the traceability loop.**
Gate Step 3 names the Step 0c contract as Pass criterion (`Step 0c exec voice contract satisfied: ...`). The Voice Compliance Audit rows name the same contract as the verified entity (`Exec verdict: Pass — Step 0c exec voice contract verified`). The two structural locations reference each other by name — not just by function. This is what makes C-34 and C-33 mutually reinforcing rather than independent.

**2. Five-point Step 0c anchoring creates a navigable audit trail.**
The contract name appears in: pitch instructions, gate criteria, rewrite anchor, Pass parentheticals (C-34), and audit rows (C-33). A reader can trace the contract from definition through gate through verification without inference — every structural waypoint names it explicitly.

**3. Per-audience contract attribution makes C-33 and C-27 non-redundant.**
C-27 requires the formal `### Voice Compliance Audit` section to exist. C-33 requires it to contain three per-audience rows. V-05 ensures each row names its own applicable contract — so the audit section doesn't merely count results but identifies what was verified for whom. This satisfies C-33's intent (granularity) rather than just its form (row count).

**4. Isolation-then-synthesis is the correct gap-closing strategy.**
V-01 proves C-33 is mechanically separable. V-02 proves C-34 is mechanically separable. V-04 proves they combine without interference. V-05 then adds the richer form only after independence is confirmed. The variation sequence is structured discovery, not just guessing — each step is testable.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["bidirectional contract anchoring: gate criterion and audit row name the same Step 0c contract by name, closing the traceability loop without inference", "five-point structural anchoring: repeat the contract name at every structural waypoint so readers can navigate from definition through gate through verification"]}
```
