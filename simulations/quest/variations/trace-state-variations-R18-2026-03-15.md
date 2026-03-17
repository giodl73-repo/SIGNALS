R18 variations written. Here's the summary:

---

## R18 Variations — trace-state (Rubric v16)

**Gap Analysis:** R17 ceiling under v16 was ~82.2 (V-01 achieves C-48, but no variant had C-49 or C-50). R18 closes that gap.

---

### Variation Axis Map

| V | Axis | Domain | New Structure | C-48 | C-49 | C-50 |
|---|------|--------|---------------|------|------|------|
| V-01 | Phrasing register | Sales | EPOCH-CLUSTER ANALYSIS (tabular) | Saturation verified in every section | PASS | — |
| V-02 | Lifecycle emphasis | Finance | EPOCH-CLUSTER ANALYSIS + Arc Position column in LIFECYCLE EPOCH MAP | PASS | PASS (richer remediation specificity) | — |
| V-03 | Output format | Customer Service | EPOCH-CLUSTER ANALYSIS as step-block labeled analysis block; C-38/C-39 active | PASS | PASS (format-neutral test) | — |
| V-04 | Role sequence × phrasing | Finance → Sales | DOMAIN DEPENDENCY DECLARATION (top-scope) + BRIDGE TABLE + EPOCH-CLUSTER spanning two domains | PASS | PASS (cross-domain) | PASS (two-hop) |
| V-05 | Full synthesis | Finance → Sales → CS | Three-pass + BRIDGE F→S + BRIDGE S→CS + EPOCH-CLUSTER across three epoch vocabularies | PASS | PASS (three-domain cascade) | PASS (full two-hop chain declared) |

---

### Key Structural Additions vs R17

**All variants:** `EPOCH-CLUSTER ANALYSIS [T]` section added after FINDINGS — maps each F-NN to an epoch, counts per epoch, names highest-density epoch, states a targeted remediation implication with named operation boundary (not generic). GATE D updated to block on EPOCH-CLUSTER ANALYSIS completion. IS-negation register (`IS NOT ... ; it IS ...`) deployed in GATE definitions, FINDINGS preamble, and EPOCH-CLUSTER ANALYSIS preamble for C-48 saturation.

**V-02 probe:** Arc Position column in LIFECYCLE EPOCH MAP (Entry boundary / Gate boundary / Approval event / Terminal settlement) grounds the C-49 remediation implication in the defect class implied by the epoch's structural role — tests whether this raises C-49 from PARTIAL to a clearly specific PASS.

**V-03 probe:** C-49 in step-block format (labeled analysis steps ECL-1 through ECL-4) — tests the rubric's format-neutral claim explicitly.

**V-04/V-05 probe:** C-50 DOMAIN DEPENDENCY DECLARATION at top scope, written in IS-negation register (`Finance IS NOT a sequential pre-step; Finance IS the state authority...`), simultaneously contributing to C-48 saturation. V-05 specifically tests the C-50 PARTIAL boundary: the rubric flags "fewer than all downstream domains named in a 3+ domain trace" as PARTIAL — V-05 explicitly names all three domains and both dependency hops.
