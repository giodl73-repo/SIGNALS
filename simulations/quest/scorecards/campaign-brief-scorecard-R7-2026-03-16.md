---

## campaign-brief / Round 7 — Scoring Complete

**Result: All five variations — 230/230**

### Summary

| Var | Score | Key change | C-22 | C-23 |
|-----|-------|-----------|------|------|
| V-01 | 230 | Baseline (R6 V-05 verbatim) | PASS | PASS |
| V-02 | 230 | Timestamp isolation stated twice | PASS | PASS |
| V-03 | 230 | Zero-signal mandate as named rule | PASS | PASS |
| V-04 | 230 | Action-posture sub-labels | PASS | PASS |
| V-05 | 230 | All three axes | PASS | PASS |

### Critical experiment outcomes

- **V-01 = 230/230** — confirmed. R6 V-05's pre-existing zero-signal clause in the STORY execution note satisfies C-22; bounded/unbounded syntax + execution note satisfies C-23. No gap existed entering R7.
- **V-03 = V-01** — C-22 PASS does not require a *named rule*. Embedded execution-note clause is sufficient. V-03's promotion to a standalone mandate is robustness hardening, not a gap fix.
- **V-04 = V-01** — C-23 PASS does not require explicit action-posture labels. The bounded/unbounded syntax alone carries the derivability signal.
- **V-05 = V-01** — all three axes are pure robustness additions with zero rubric cost.

### R8 base: V-05

Maximum structural coverage (three hardening axes) at zero rubric cost. V-05 is the preferred R8 base.

### R8 investigation: COMPRESSED x `found` timestamp survival

The open risk is live: at >4 blocking entries the COMPRESSED branch activates, and the model may abbreviate the entire STATUS block including `found` timestamps. V-05 states the isolation rule at two locations, but both are prose instructions. R8 must run live output at >4 blocking gaps to falsify. If timestamps drop, C-24 adds a structural separation (separate `[FOUND]` block).

```json
{"top_score": 230, "all_essential_pass": true, "new_patterns": ["named isolation rule at two structural locations for timestamp survival under COMPRESSED", "zero-signal mandate promoted to standalone named execution rule with two operational clauses", "action-posture sub-labels on bounded/unbounded inertia field enabling direct action derivation"]}
```
prohibition list | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-18 | STORY three-question sequential structure | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-19 | Gap reclassification rule | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-20 | Density ceiling on entry count | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-21 | Sparse-coverage synthesis protection | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-22 | Zero-signal synthesis mandate | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-23 | Bounded/unbounded inertia at verdict | Aspirational | PASS | PASS | PASS | PASS | PASS |
| | **TOTAL** | | **230** | **230** | **230** | **230** | **230** |

---

## Evidence Notes

### C-22 — Zero-signal synthesis mandate

**V-01/V-02/V-04:** Zero-signal clause present in two locations within STORY: (1) question 1
body text — "Zero-signal rule: when `found` is empty... do not write 'no signals found —
synthesis not possible.' The gap pattern is the evidence set. State what the uniform absence
of signals implies..." (2) STORY execution note — "When `found` is empty, the gap pattern is
the evidence set; question 1 must characterize what uniform absence implies rather than
vacating synthesis." The execution note contains an explicit non-vacating mandate. PASS gate
satisfied: explicit clause in STORY execution note is present.

**V-03/V-05:** Zero-signal mandate promoted from embedded question text to a standalone
named execution rule after the execution note, with two explicit operational sub-clauses:
(1) "Empty `found` is not grounds for omitting synthesis — the gap pattern is the evidence
set." (2) "Question 1 must characterize what uniform absence implies: what surface of the
problem has not been probed at all, and what that means for the decision." Named-rule form
is structurally stronger than inline advisory. Same rubric outcome: PASS.

### C-23 — Bounded/unbounded inertia classification at verdict level

**V-01/V-02/V-03:** VERDICT template declares:
  `inertia_cost: bounded: <residual risk and why recoverable post-commit>`
  `              OR`
  `              unbounded: <failure class and why irreversible once committed>`
Execution note: "classify recoverability: use `bounded:` when... use `unbounded:` when..."
The team can derive action posture from the verdict block alone — bounded implies
commit-with-monitoring, unbounded implies do-not-commit. PASS gate satisfied.

**V-04/V-05:** Action-posture sub-labels added to the `inertia_cost` field:
  `bounded: <...>  action: commit with monitoring`
  `unbounded: <...>  action: do not commit until resolved`
Field value maps directly to team action at the template level. Stronger compliance signal,
same rubric outcome: PASS.

---

## Critical Experiment Results

| Experiment | Result | Interpretation |
|-----------|--------|---------------|
| V-01 = 230/230? | YES — confirmed | C-22 and C-23 fully satisfied by R6 V-05. R7 adds no new gap. |
| V-03 > V-01? | NO — tied 230 | C-22 PASS does not require a named rule. Embedded execution-note clause is sufficient. V-03 is robustness hardening, not gap-closing. |
| V-04 > V-01? | NO — tied 230 | C-23 PASS does not require explicit action-posture labels. bounded/unbounded syntax + execution note carries the derivability signal. |
| V-02 > V-01? | NO — tied 230 | C-16 isolation stated once is sufficient. Double-location restatement adds no rubric signal. |
| V-05 = V-01? | YES — tied 230 | All three axes are pure robustness additions. Zero rubric cost confirmed. |

---

## Ranking

| Rank | Variation | Score | Basis |
|------|-----------|-------|-------|
| 1 | **V-05** | 230/230 | Preferred R8 base — all three hardening axes, maximum failure-mode coverage |
| 1 | V-01 | 230/230 | Rubric-equivalent baseline (R6 V-05 verbatim) |
| 1 | V-02 | 230/230 | Timestamp isolation stated twice — robustness only |
| 1 | V-03 | 230/230 | Zero-signal mandate as named rule — robustness only |
| 1 | V-04 | 230/230 | Action-posture sub-labels — robustness only |

V-05 is the R8 base by structural preference, not score differential.

---

## Excellence Signals (from V-05 as preferred R8 base)

**Pattern 1 — Named isolation rule at two structural locations for timestamp survival**
The `found:` timestamp isolation rule appears in both the density contract preamble
("Found-signal timestamp isolation rule" named paragraph) and as a template comment
in the STATUS block template (`<- timestamps required; not subject to density contract`).
Two-location restatement reduces the risk of model attention drift when the COMPRESSED
branch activates at high gap count, where the model is most likely to abbreviate the
entire STATUS block.

**Pattern 2 — Zero-signal mandate as standalone named execution rule with two operational clauses**
V-03/V-05 promote the zero-signal clause from embedded question-body advisory text to a
named execution mandate with two numbered operational sub-clauses: (1) empty `found` is
not grounds for omitting synthesis, (2) question 1 must characterize uniform absence.
The named-rule form is more resistant to being treated as soft guidance than inline
question text, even when the inline text contains identical content.

**Pattern 3 — Action-posture sub-labels on bounded/unbounded inertia fields**
V-04/V-05 add `action: commit with monitoring` / `action: do not commit until resolved`
as explicit sub-labels under each `inertia_cost` form. This maps the field value directly
to a team action at the template level, eliminating any inference gap between the
bounded/unbounded classification and what the team should do next. The C-23 intent
(actionable from verdict block alone) is realized without requiring the reader to derive
the posture from the prose description.

---

## R8 Investigation Candidate (carried forward)

**COMPRESSED format x `found` timestamp survival — live falsification needed.**

V-02 and V-05 state the found-signal isolation rule at two locations. The failure mode is:
when COMPRESSED triggers at >4 blocking entries, the model may abbreviate the entire STATUS
block including `found` timestamps. Two-location restatement reduces this risk but does not
eliminate it at the template level — the isolation rule is still a prose instruction, and
the model may not treat the `found:` section as structurally exempt when executing the
COMPRESSED branch under attention compression.

R8 must produce live output at >4 blocking gaps to confirm `found` timestamps survive the
COMPRESSED branch in practice. If timestamps drop, the isolation rule requires a structural
mechanism (e.g., a separate `[FOUND]` block that precedes the density-governed `[MISSING]`
block) rather than a prose instruction at any number of locations.

---

## R8 Base Recommendation

**V-05** is the R8 base. No rubric gaps remain in v7. R8 scope:
- Execute V-05 live at >4 blocking entries to test COMPRESSED x timestamp survival
- If timestamps survive: R8 closes the investigation candidate, no v8 criterion needed
- If timestamps drop: R8 adds C-24 (structural separation of `found` from density contract)

```json
{"top_score": 230, "all_essential_pass": true, "new_patterns": ["named isolation rule at two structural locations for timestamp survival under COMPRESSED", "zero-signal mandate promoted to standalone named execution rule with two operational clauses", "action-posture sub-labels on bounded/unbounded inertia field enabling direct action derivation"]}
```
