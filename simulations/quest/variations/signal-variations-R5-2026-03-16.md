Written to `simulations/quest/golden/signal-variate-R5-2026-03-16.md`.

---

## Round 5 Variates -- /signal

**Context**: R4 champion V-05 (pre-print + 7 RULES with C-NN IDs + COMPLIANCE AUDIT) anticipated C-18 and C-19. But it has one structural gap: RULE 6 (C-14) merges C-14 (bidir) and C-16 (`->` enforcement) in a single rule. Under v5 C-18, a scorer looking for "RULE N (C-16)" can't find it without inferring it's inside RULE 6 (C-14). That's O(N) inference, not O(1) inspection.

---

### Variations

| Var | Axis | Hypothesis | C-16 label | C-17 rule | Completeness seal |
|-----|------|-----------|-----------|-----------|-----------------|
| **V-01** | C-16 standalone RULE 8 (C-16) | Giving C-16 its own labeled rule makes C-18 unambiguous for all 9 aspirational criteria | RULE 8 (C-16) | structural (no dedicated rule) | no |
| **V-02** | Phrasing register: invitation-style routing hints | Register change is orthogonal to rubric; tests whether "When you need to X..." format creates any discrimination | RULE 6 (C-14) embedded | 7-rule base (R4 V-05) | no |
| **V-03** | V-01 + RULE 9 (C-17) self-referential completeness | Making C-17 explicitly self-referential (a rule that asserts the list is complete) gives C-17 its own labeled RULE 9 | RULE 8 (C-16) | RULE 9 (C-17) explicit | in audit checkbox |
| **V-04** | V-01 + COMPLETENESS SEAL inside the gate | Completeness claim in the gate (active) is stronger than completeness claim in the rules (passive) | RULE 8 (C-16) | structural | COMPLETENESS SEAL in COMPLIANCE AUDIT |
| **V-05** | Full integration: RULE 9 (C-17) + 9-checkbox audit + COMPLETENESS SEAL | Max structural guarantee: rule declares completeness, gate verifies it, "do not proceed" enforces it | RULE 8 (C-16) | RULE 9 (C-17) | both rule and audit |

### Predicted Scores (v5 rubric)

```
V-01:  100/100  -- RULE 8 (C-16) solves the C-18 gap; C-18 PASS for all criteria
V-02:  ~99.1    -- C-18 PARTIAL (C-16 uninferrable from RULE 6 label); otherwise clean
V-03:  100/100  -- 9 labeled rules, every aspirational criterion has its own RULE N (C-NN)
V-04:  100/100  -- RULE 8 (C-16) + COMPLETENESS SEAL; strongest C-19 gate form
V-05:  100/100  -- Max structural: 9 rules + 9 checkboxes + COMPLETENESS SEAL + "do not proceed"
```

**Key discriminator**: V-02 is the only predicted non-100 (C-18 PARTIAL for C-16). V-01/V-03/V-04/V-05 all predicted at 100/100 but differ on structural guarantee strength for C-17/C-19. **V-05 is the predicted structural champion** — RULE 9 (C-17) labeled in the rule list, checkpoint for RULE 9 in the audit, COMPLETENESS SEAL affirmed before any output.
