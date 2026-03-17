Written to `simulations/quest/golden/org-chart-variate-R11-v11-2026-03-16.md`.

---

## org-chart Variate — Round 11 (Rubric v11)

**Baseline:** R10-V-05 scores 220/230 on v11 — two new criteria unaddressed.

### Variation Map

| V | Axis | C-35 | C-36 | Key change |
|---|------|------|------|------------|
| **V-01** | Phrasing register (formal/imperative) | PASS (control) | absent | Inherits R10-V-05 CHARTER-FORMAT-AUDIT loop unchanged; ROLE-CONTINUITY stays post-loop in CHECKPOINT-3 |
| **V-02** | Loop structure: role continuity inside loop + aggregate backup | PASS | **TARGET** | Adds third per-charter check to loop: Membership role names cross-referenced against GATE 0 before loop advances; CHECKPOINT-3 retains aggregate ROLE-CONTINUITY as backup |
| **V-03** | Loop structure: role continuity inside loop only | PASS | **TARGET (alt)** | Same loop as V-02; CHECKPOINT-3 replaces separate ROLE-CONTINUITY item with reference to completed loop — probes whether C-34 requires independent aggregate declaration or is satisfied via C-36 subsumption |
| **V-04** | Inertia framing emphasis + V-02 loop | PASS | **TARGET** | Enriches GATE 1 with STRUCTURING-COST FRAME, NET-COST-COMPARISON, SUB-SECTION-4-ANCHOR-SEQUENCE; V-02 loop for C-36 — tests composition without interference |
| **V-05** | Full integration: V-02 loop + V-04 inertia + explicit gate chain | PASS | **TARGET** | GATE CHAIN: block with named artifact handoffs; per-charter loop with role continuity; enriched inertia; strongest composite predicted |

### Key structural change (C-36 target — V-02/V-03/V-04/V-05)

The CHARTER-FORMAT-AUDIT loop template gains a third check item:

```
[ ] Membership role continuity: for each role name in this charter's Membership field,
    verify the name is present in the GATE 0 ROLES-LOADED or ROLES-NOTE typed role list
    REJECT: role name [X] not found in GATE 0 typed role list -- halt loop at this charter;
    remediation: add [X] to GATE 0 ROLES-LOADED and re-emit GATE 0 STATUS; DO NOT advance
    to the next charter until this charter passes all three checks
```

This integrates C-34's lookup into C-35's per-charter iteration, satisfying C-36 at the earliest detection point rather than post-hoc in CHECKPOINT-3.

### V-03 probing question

Does C-34 require an independent aggregate declaration in CHECKPOINT-3, or is it satisfied through C-36's subsumption? V-03 removes the separate aggregate ROLE-CONTINUITY item from CHECKPOINT-3 and replaces it with a reference to the completed loop. The rubric hierarchy says "a variation satisfying C-36 necessarily satisfies both C-35 and C-34" — V-03 tests this claim empirically.
