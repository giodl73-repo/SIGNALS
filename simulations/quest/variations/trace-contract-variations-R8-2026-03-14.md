Written to `simulations/quest/rubrics/trace-contract-variate-R8-2026-03-15.md`.

---

## trace-contract — Round 8 Variations Summary

Five complete, runnable variations for the v8 rubric (A/24×10).

---

### V-01 — Role Sequence
**Axis:** Explicit named-role ownership of every phase and gate.
**C-31 coverage:** GATE 1 carries both isolation clauses in two-clause confirmable form — actual-output isolation and inertia exclusion get identical structural treatment: `— [CONFIRMED / NOT CONFIRMED]` on both.
**C-32 coverage:** Primary target. `phase1a_author: Expert` / `gate1b_owner: Automate` in frontmatter. Explicit `> HANDOFF TO AUTOMATE` boundary between GATE 1 and Phase 1B. "Expert cannot certify GATE 1B" as a structural rule. Role table at prompt header.

---

### V-02 — Output Format
**Axis:** Pre-specified table schemas, frontmatter key names, and standardized `— [CONFIRMED / NOT CONFIRMED]` form applied uniformly.
**C-31 coverage:** The inertia exclusion item in GATE 1 gets the same checkbox format as the actual-output isolation item — format axis makes both clauses first-class gate entries by default.
**C-32 coverage:** `gate1b_owner: Automate` in the required frontmatter schema; machine-readable. The format makes role separation queryable.

---

### V-03 — Lifecycle Emphasis
**Axis:** STOP markers at every phase boundary; phase dependency table at header; "cannot begin until" language.
**C-31 coverage:** The inertia exclusion clause in GATE 1 is a lifecycle checkpoint on the same GATE 1 node as the actual-output isolation check — it blocks Phase 1B just as the actual-output check does.
**C-32 coverage:** The phase dependency table lists "**Automate**" in bold for Phase 1B. The STOP after GATE 1 reads: "Phase 1B owner is Automate — not Expert. The same role that built Phase 1A cannot certify GATE 1B." Lifecycle handoff language makes role separation a sequencing rule.

---

### V-04 — Inertia Framing
**Axis:** Opening paragraph names inertia as the semantic threat; every contamination barrier is explained in terms of the risk it closes.
**C-31 coverage:** Primary target. The GATE 1 inertia exclusion item reads "not just deprioritized after consideration, but excluded entirely from expected value derivation — [CONFIRMED / NOT CONFIRMED]" — two-clause confirmable form, placed after an explicit inertia risk explanation that gives it maximum explanatory force.
**C-32 coverage:** Present as structural baseline. Phase 1B framing: "Automate reviews each row with the contamination question front of mind." Role separation is explained via the epistemological argument (author cannot detect their own contamination).

---

### V-05 — Combined Full Integration
**Axes:** All four combined.
**C-31 + C-32 coverage:** Both first-class. Role table + phase dependency table + inertia framing + two-clause confirmable form on both contamination paths in GATE 1. `phase1a_author` and `gate1b_owner` in frontmatter. Blocking STOP at Phase 1A → 1B boundary with explicit role-separation rule. All 24 aspirational criteria addressed by gate item or template structure.

---

### Predicted R8 scores (indicative)

| Var | Primary axis | C-31 | C-32 | Projected A/24 | Projected score |
|-----|-------------|------|------|----------------|-----------------|
| V-01 | Role Sequence | PASS | PASS | ~19.5 | ~8.1 |
| V-02 | Output Format | PASS | PASS | ~18.5 | ~7.7 |
| V-03 | Lifecycle Emphasis | PASS | PASS | ~21.0 | ~8.8 |
| V-04 | Inertia Framing | PASS | PASS | ~21.5 | ~9.0 |
| V-05 | Combined | PASS | PASS | ~24.0 | ~10.0 |

V-01 retains its delta blind spot risk (C-22 was FAIL in R7); V-02 retains its depth-item risk (C-21, C-22). V-03 and V-04 carry different weak spots (V-03: delta annotation depth; V-04: challenge log depth). V-05 closes all.
