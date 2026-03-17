Written to `simulations/quest/golden/org-chart-variate-R10-v10-2026-03-16.md`.

---

## Round 10 -- org-chart (Rubric v10)

**Baseline:** R9-V-05 = 210/210 on v9. On v10: 210/220 (95.5%). Two gaps.

### Variation Map

| V | Axis | Hypothesis | C-33 | C-34 |
|---|------|-----------|------|------|
| **V-01** | Lifecycle: FORMAT-VERIFY items in CHECKPOINT-3 | Naming prohibited Quorum alternatives and the TYPE closed set in the checkpoint items converts generic presence checks into field-format compliance | TARGET | open |
| **V-02** | Lifecycle: ROLE-CONTINUITY lookup item in CHECKPOINT-3 | Naming GATE 0 as the lookup authority with an explicit FAIL+remediation directive converts declaration-scope constraint into checkpoint-execution lookup | open | TARGET |
| **V-03** | Output format: dedicated CHARTER-FORMAT-AUDIT loop | Per-charter iteration with labeled REJECT conditions and a DO NOT advance guard tests whether the loop structure satisfies C-33's "every produced charter" requirement more directly than inline items | TARGET (alt) | open |
| **V-04** | Combined: V-01 FORMAT-VERIFY + V-02 ROLE-CONTINUITY | C-33 and C-34 are orthogonal checks (format within charter vs. name against GATE 0); inline combination in CHECKPOINT-3 | TARGET | TARGET |
| **V-05** | Full integration: V-03 CHARTER-FORMAT-AUDIT + V-02 ROLE-CONTINUITY | Strongest C-33 (dedicated loop with REJECT labels and re-run directive) + strongest C-34 (named lookup authority + named remediation) on R9-V-05 base | TARGET | TARGET |

### What changed from R9-V-05

The only structural differences across all five variations are within GATE 3. Everything from GATE 0 through GATE 2 and Steps 3.1--3.5 is identical to R9-V-05.

**C-33 gap in R9-V-05:** CHECKPOINT-3 items 4-5 read:
```
- [ ] Quorum in `N of M member roles` form for all charters
- [ ] Membership >= 2 roles with `(TYPE)` annotation for all charters
```
These confirm format presence but do not name the closed set for TYPE or the prohibited Quorum patterns. A model can satisfy these with `(OWNER)` or `"majority of 5"`.

**V-01 fix:** Replace with FORMAT-VERIFY items that name every rejection condition:
- `FORMAT-VERIFY QUORUM`: fractional ("3/5"), percentage ("60%"), prose quorum, bare number explicitly NOT acceptable
- `FORMAT-VERIFY MEMBERSHIP TYPE`: closed set `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}` named; unannotated entries or out-of-set values explicitly rejected

**V-03 fix (alternate):** A pre-CHECKPOINT `CHARTER-FORMAT-AUDIT` loop runs `REJECT:` conditions per charter with an explicit "re-run from first charter" guard. CHECKPOINT-3 item 4 becomes a single reference to the completed audit.

**C-34 gap in R9-V-05:** CHECKPOINT-3 has no cross-gate lookup. C-02 and C-25 address the constraint at declaration and handoff scope, not at checkpoint execution.

**V-02/V-04/V-05 fix:** A `ROLE-CONTINUITY` item in CHECKPOINT-3 names GATE 0 as the lookup authority and states: "If any Membership role name is absent from GATE 0: CHECKPOINT-3 FAILS. Remediation: add the undeclared role to GATE 0 and re-emit GATE 0 STATUS before GATE 3 STATUS can emit."

### Predicted scores on v10 rubric

| V | C-33 | C-34 | Aspirational | Total | % |
|---|------|------|-------------|-------|---|
| V-01 | PASS | FAIL | 33/34 (C-33 closed; C-34 open) | 215/220 | 97.7% |
| V-02 | FAIL | PASS | 33/34 (C-34 closed; C-33 open) | 215/220 | 97.7% |
| V-03 | PASS | FAIL | 33/34 (C-33 closed via loop; C-34 open) | 215/220 | 97.7% |
| V-04 | PASS | PASS | 34/34 | 220/220 | 100.0% |
| V-05 | PASS | PASS | 34/34 | 220/220 | 100.0% |

V-04 and V-05 differ only in C-33 implementation method. Both predicted 220/220. V-05 is the preferred base for R11 if a rubric signal indicates the dedicated-loop format has stronger downstream properties than inline items.
