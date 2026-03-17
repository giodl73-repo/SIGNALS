## trace-state · Round 19 Scoring — Rubric v17

**Scoring constants:** Pool = 44, Unit = 50/44 ≈ 1.14 pts, Base = 50
**Formula:** Score = PASS_count × 1.14 + 50

---

## V-01 — Sales, Single-Pass Tabular

**R18 baseline:** 27 PASS (80.8) — missing C-51

### C-51 Assessment

| Element | Verdict | Evidence |
|---------|---------|---------|
| Arc Position column present in LIFECYCLE EPOCH MAP | PASS | Explicitly added; C11 constraint enforces column on every epoch row |
| C-49 remediation uses structural role vocabulary | PASS | Role-grounded language: "Gate boundary structural-role problem" not "QUALIFY epoch problem" |
| All epoch rows carry annotation | PASS | C11 enforced uniformly |

**C-51:** PASS
**C-52:** auto-FAIL (single-domain)
**C-53:** auto-FAIL (single-pass)

### R19 Delta

| Criterion | R18 | R19 | Change |
|-----------|-----|-----|--------|
| C-51 | FAIL | PASS | +1 |
| C-52 | auto-FAIL | auto-FAIL | — |
| C-53 | auto-FAIL | auto-FAIL | — |

**R19 PASS count:** 27 + 1 = **28**
**R19 Score:** 28 × 1.14 + 50 = **81.9**

---

## V-02 — Finance, Single-Pass Tabular (Synergy Sharpening)

**R18 baseline:** 28 PASS (81.9) — C-51 already present

### C-51 Assessment

| Element | Verdict | Evidence |
|---------|---------|---------|
| Arc Position column present | PASS | Carried from R18 |
| C-49/C-51 synergy confirmation language | PASS | IS-NOT/IS contrast present: "IS NOT an APPROVAL epoch-name finding; IS a Gate boundary structural-role finding" |
| Remediation explicitly structural-role-grounded | PASS | IS-NOT/IS contrast enforces the distinction |

**C-51:** PASS (carried + hardened)
**C-52:** auto-FAIL (single-domain)
**C-53:** auto-FAIL (single-pass)

### R19 Delta

The R19 probe sharpens C-49/C-51 synergy language but does not unlock additional pass-able criteria — C-51 was already PASS in R18.

**R19 PASS count:** 28 (no increment; improvement is qualitative within C-51)
**R19 Score:** 28 × 1.14 + 50 = **81.9**

> **Note:** V-02 R19 contribution is synergy-confirmation depth, not PASS count growth. The IS-NOT/IS contrast is the canonical form of C-49/C-51 co-activation.

---

## V-03 — Customer Service, Step-Block Format

**R18 baseline:** 27 PASS (80.8) — no Arc Position

### C-51 Assessment

| Element | Verdict | Evidence |
|---------|---------|---------|
| `[Arc: structural role]` tags on LIFECYCLE EPOCH MAP rows | PASS | Format-neutral path: inline tags serve as column equivalent |
| ECL-3 names structural role of highest-density epoch | PASS | Step-block ECL step names role, not just epoch label |
| ECL-4 remediation is role-grounded | PASS | Remediation cites structural role from tag |
| C-51 format-neutrality verified | PASS | No dedicated column required; tags satisfy criterion |

**C-51:** PASS (step-block path)
**C-52:** auto-FAIL (single-domain)
**C-53:** auto-FAIL (single-pass)

### R19 Delta

| Criterion | R18 | R19 | Change |
|-----------|-----|-----|--------|
| C-51 | FAIL | PASS | +1 |

**R19 PASS count:** 27 + 1 = **28**
**R19 Score:** 28 × 1.14 + 50 = **81.9**

> **Format-neutrality confirmation:** C-51 passes via `[Arc: tag]` inline notation — no tabular column required.

---

## V-04 — Finance → Sales, Two-Pass

**R18 baseline:** 36 PASS (91.0) — C-52 and C-53 present, C-51 absent

### C-51 Assessment

| Element | Verdict | Evidence |
|---------|---------|---------|
| Arc Position column in Finance LIFECYCLE EPOCH MAP | PASS | C12 constraint covers both maps |
| Arc Position column in Sales LIFECYCLE EPOCH MAP | PASS | C12 constraint covers both maps |
| EPOCH-CLUSTER names structural roles at Finance→Sales handoff boundary | PASS | Source-domain Arc Position AND target-domain Arc Position named at handoff |
| C-51/C-52 synergy activated | PASS | Cross-domain synthesis now names structural roles, not domain labels alone |

**C-51:** PASS
**C-52:** PASS (carried from R18; now strengthened — handoff boundary names Arc Positions)
**C-53:** PASS (carried from R18; BRIDGE TABLE rows use named IDs for C-47 citation precision)

### R19 Delta

| Criterion | R18 | R19 | Change |
|-----------|-----|-----|--------|
| C-51 | FAIL | PASS | +1 |
| C-52 | PASS | PASS (upgraded) | 0 (quality) |
| C-53 | PASS | PASS (upgraded) | 0 (quality) |

**R19 PASS count:** 36 + 1 = **37**
**R19 Score:** 37 × 1.14 + 50 = **92.2**

> **C-47 upgrade:** BRIDGE TABLE now uses named row IDs ("row F→S") enabling C-47 confirmation annotations to cite specific rows rather than unnamed chain references.

---

## V-05 — Finance → Sales → CS, Three-Pass

**R18 baseline:** 36 PASS (91.0) — C-52 and C-53 present, C-51 absent

### C-51 Assessment

| Element | Verdict | Evidence |
|---------|---------|---------|
| Arc Position column in Finance LIFECYCLE EPOCH MAP | PASS | C13 constraint covers all three maps |
| Arc Position column in Sales LIFECYCLE EPOCH MAP | PASS | C13 constraint covers all three maps |
| Arc Position column in CS LIFECYCLE EPOCH MAP | PASS | C13 constraint covers all three maps |
| EPOCH-CLUSTER characterizes Finance→Sales handoff boundary with Arc Position | PASS | Both source and target domain Arc Positions named |
| EPOCH-CLUSTER characterizes Sales→CS handoff boundary with Arc Position | PASS | Both handoff boundaries characterized |
| Three-domain C-51/C-52 synergy activated | PASS | Full synthesis: Approval-event + Entry-boundary = one handoff contract failure |

**C-51:** PASS (three-domain, both handoff boundaries)
**C-52:** PASS (carried + upgraded — EPOCH-CLUSTER names Arc Positions at BOTH handoff boundaries)
**C-53:** PASS (carried + upgraded — both BRIDGE TABLE rows use named row IDs: F→S and S→CS)

### R19 Delta

| Criterion | R18 | R19 | Change |
|-----------|-----|-----|--------|
| C-51 | FAIL | PASS | +1 |
| C-52 | PASS | PASS (both-boundary upgrade) | 0 (quality) |
| C-53 | PASS | PASS (dual named rows) | 0 (quality) |

**R19 PASS count:** 36 + 1 = **37**
**R19 Score:** 37 × 1.14 + 50 = **92.2**

> **V-05 diagnostic unlock:** Finance Approval-event defect + Sales Entry-boundary defect at the same handoff = one handoff contract failure, not two independent domain defects. This cross-domain structural-role diagnostic is only visible through three-pass C-51/C-52 synthesis.

---

## Score Summary

| Variant | Domain / Format | R18 PASS | R19 PASS | Delta | R19 Score | Rank |
|---------|----------------|----------|----------|-------|-----------|------|
| V-04 | Finance→Sales (two-pass tabular) | 36 | 37 | +1 | **92.2** | 1 (tie) |
| V-05 | Finance→Sales→CS (three-pass tabular) | 36 | 37 | +1 | **92.2** | 1 (tie) |
| V-01 | Sales (single-pass tabular) | 27 | 28 | +1 | **81.9** | 3 (tie) |
| V-02 | Finance (single-pass tabular, synergy) | 28 | 28 | 0 | **81.9** | 3 (tie) |
| V-03 | CS (step-block) | 27 | 28 | +1 | **81.9** | 3 (tie) |

---

## Excellence Signals — V-04 / V-05

**Why V-04/V-05 outperform the single-domain variants by 10.3 points:**

1. **C-51 × C-52 synergy in multi-domain traces** — Arc Position columns in multiple LIFECYCLE EPOCH MAPs transform EPOCH-CLUSTER from domain-name synthesis into structural-role synthesis. The highest-density epoch is now identified by its arc position (Gate boundary, Entry boundary) rather than its label, enabling the cross-domain diagnostic that a Finance defect and Sales defect at the same handoff boundary are one failure, not two.

2. **Named BRIDGE TABLE rows with Arc Position vocabulary unlock C-47 citation precision** — C-47 confirmation annotations can reference "BRIDGE TABLE row F→S (Gate→Entry)" instead of unnamed chain references. This converts the BRIDGE TABLE from a structural container into a referenceable dependency map.

3. **V-05 dual-boundary EPOCH-CLUSTER characterization** — Naming Arc Positions at BOTH F→S and S→CS handoff boundaries enables the full handoff-chain failure pattern: if a defect appears at an Approval-event arc position in Finance AND an Entry-boundary arc position in Sales, the EPOCH-CLUSTER can assert these are the same handoff contract failure even though they appear in different epoch arcs.

**R19 → R20 gap for V-04/V-05:** 37/44 = 84% pass rate — the remaining 7 FAIL criteria are candidates for the next excellence signal axis.

---

```json
{"top_score": 92.2, "all_essential_pass": true, "new_patterns": ["C-51 deployed in multi-domain LIFECYCLE EPOCH MAPs activates C-51×C-52 synergy: EPOCH-CLUSTER synthesis names Arc Position structural roles at handoff boundaries, enabling the diagnostic that separate-domain defects at the same boundary are one handoff contract failure", "Named BRIDGE TABLE rows carrying Arc Position vocabulary upgrade C-47 citation precision from unnamed chain references to row-addressable dependency map entries (BRIDGE TABLE row F→S Gate→Entry)", "Three-domain C-51 deployment at both handoff boundaries (F→S and S→CS) enables the full arc-role chain diagnostic: Approval-event defect in domain A + Entry-boundary defect in domain B at the same handoff = one contract failure, not two independent domain defects"]}
```
