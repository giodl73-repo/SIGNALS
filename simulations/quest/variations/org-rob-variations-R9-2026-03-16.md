`simulations/quest/golden/corps-rob-variate-R9-2026-03-16.md` written.

---

# Variate R9 -- org-rob

5 complete prompt body variations targeting structural robustness of the 122/122 score from R8.

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Risk-lead stage sequence: tpm -> arch-board -> teams -> pm -> leadership -> spire | V-01 | C-06, C-09, C-10, C-12 |
| Phrasing register: descriptive/declarative rather than imperative/template-heavy | V-02 | C-02, C-11, C-18, C-23 |
| Dual inertia baselines: IB-01 (technical) + IB-02 (organizational) before Stage 1 | V-03 | C-21, C-24 |
| Risk-lead + extended C-24: VIOLATION-10 enforcing Via: column position (C-19) | V-04 | C-19, C-21, C-24 |
| Full R9 stack: dual baselines + risk-lead + VIOLATION-09/10/11 triple C-24 loops | V-05 | C-09..C-24 all ++ |

---

## Design rationale per variation

**V-01 (Risk-Lead Sequence)**: Inverts stage order so TPM defines the risk landscape before teams self-review. Escalation graph has no backward edges — every downstream stage inherits known risks rather than discovering them. All R8 structural elements preserved; tests whether C-06/C-09/C-10/C-12 scores change with clean forward-flow escalation.

**V-02 (Phrasing Register)**: Replaces imperative templates ("Print a block that looks like this:") with declarative prose explaining what each section accomplishes and why. Tests whether structural criteria are information-grounded (survive register changes) or format-prescription-dependent (drop when the template is removed). Full VIOLATION-01..09 taxonomy with consequence rationale satisfies C-23.

**V-03 (Dual Inertia Baselines)**: Splits the single INERTIA BASELINE into IB-01 (technical coupling and migration cost) and IB-02 (organizational behavior change and adoption resistance). Each has its own VIOLATION-NN entry — VIOLATION-09 for IB-01, VIOLATION-10 for IB-02 — creating two C-24 enforcement loops targeting distinct C-21 sub-types.

**V-04 (Risk-Lead + Extended C-24)**: Combines V-01 stage ordering with a second C-24 enforcement loop: VIOLATION-10 assigned to Via: column position (C-19). Two named structural elements — INERTIA BASELINE (C-21) and Via: second column (C-19) — are each self-policing through the taxonomy. Tests whether dual C-24 loops are structurally compatible with the risk-lead stage sequence.

**V-05 (Full R9 Stack)**: Triple C-24 enforcement network — VIOLATION-09 (IB-01/C-21), VIOLATION-10 (IB-02/C-21), VIOLATION-11 (FINDING LEDGER/C-17) — combined with dual inertia baselines, risk-lead stage order, and consequence rationale on 5 violations (C-23). Tests 122/122 via a structurally diverse path from R8 V-05: triple enforcement loops, dual baselines, forward-flow escalation, five rationale paragraphs.

---

## Expected R9 scores under v8 rubric

| Variation | C-21 | C-22 | C-23 | C-24 | Expected |
|-----------|------|------|------|------|----------|
| V-01 | ++ (IB-01) | ++ (VIOLATION-09+) | ++ (5 rationale paragraphs) | ++ (VIOLATION-09 → IB-01) | 122/122 |
| V-02 | ++ | ++ | ++ | ++ | 122/122 |
| V-03 | ++ (IB-01+IB-02) | ++ | ++ | ++ (VIOLATION-09 → IB-01, VIOLATION-10 → IB-02) | 122/122 |
| V-04 | ++ | ++ | ++ | ++ (VIOLATION-09 → IB-01, VIOLATION-10 → Via:) | 122/122 |
| V-05 | ++ (IB-01+IB-02) | ++ | ++ (5 violations) | ++ (triple loop) | 122/122 |

**R9's structural question**: does the 122/122 score survive (a) reversed stage ordering, (b) a descriptive register that removes template scaffolding, and (c) dual-baseline inertia framing with two independently enforced C-21 elements? If any variation drops, the failing criterion reveals what was template-dependent rather than structurally grounded.
