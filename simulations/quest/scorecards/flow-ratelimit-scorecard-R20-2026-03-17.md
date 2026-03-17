Now I have everything I need to score all variations. Let me write the scorecard.

## flow-ratelimit — Round 20 Scorecard

### Score Summary

| Variation | Axes | Ess | Rec | Asp (40) | Composite |
|-----------|------|-----|-----|----------|-----------|
| **V-05** | C-46+C-47+C-48 | 5/5 | 3/3 | 40/40 | **120.00** |
| **V-04** | C-46+C-47 | 5/5 | 3/3 | 38/40 | **118.50** |
| V-01 | C-46 | 5/5 | 3/3 | 36/40 | 117.00 |
| V-02 | C-47 | 5/5 | 3/3 | 36/40 | 117.00 |
| V-03 | C-48 | 5/5 | 3/3 | 36/40 | 117.00 |

Scoring: Essential 60 pts (5 × 12), Recommended 30 pts (3 × 10), Aspirational 30 pts (pass/40 × 30, 0.75 each).

---

### Criterion-by-Criterion Breakdown

#### Essential — all 5 variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-01 | PASS | PASS | PASS | PASS | PASS | Role 4 scope-distinct tier requirement; 3+ tiers with distinct scope levels enforced at gate. |
| C-02 | PASS | PASS | PASS | PASS | PASS | Role 4 scope-distinction check explicitly rejects same-scope variants as non-distinct tiers. |
| C-03 | PASS | PASS | PASS | PASS | PASS | Role 5 SCHEMA-B block per tier; six-item gate enforced per block; tier count = B. |
| C-04 | PASS | PASS | PASS | PASS | PASS | Role 3 STRUCTURAL/INCIDENTAL classification with justification; gate requires at least one STRUCTURAL path. |
| C-05 | PASS | PASS | PASS | PASS | PASS | RH-xx Finding IDs (retry-handling gaps) produced in Role 5 and consumed in SCHEMA-M Role 8c. |

#### Recommended — all 5 variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-06 | PASS | PASS | PASS | PASS | PASS | Role 8a SCHEMA-A cascade table with required prose causal chain statement. |
| C-07 | PASS | PASS | PASS | PASS | PASS | Role 1 binding constraint requires numeric threshold; Role 4 confirms it; cited in SCHEMA-A. |
| C-08 | PASS | PASS | PASS | PASS | PASS | Role 6 SCHEMA-V with BASELINE BEHAVIOR and PROTECTED BEHAVIOR columns; 5x spike derived. |

#### Aspirational — new criteria (C-43 through C-48)

All variations inherit C-09–C-42 (34 prior-round criteria) as PASS. The six most recent criteria discriminate:

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-43 | PASS | FAIL | FAIL | PASS | PASS | V-01/V-04/V-05: SCHEMA-A CELL ANCHOR with two explicitly distinguished violation classes. V-02: no cell anchor. V-03: BURST PATH TABLE routing only, no general cell anchor. |
| C-44 | FAIL | PASS | FAIL | PASS | PASS | V-02/V-04/V-05: Schema Production Registry as dedicated aggregate table before body entries. V-01/V-03: no registry. |
| C-45 | FAIL | FAIL | PASS | FAIL | PASS | V-03/V-05: BURST PATH TABLE in Role 3 with SCHEMA-A BASELINE SOURCE column; bidirectional traceability declared. V-01/V-02/V-04: no BURST PATH TABLE. |
| C-46 | PASS | FAIL | FAIL | PASS | PASS | V-01: e.3 explicitly names "missing or invalid prefix" as prohibited merged form. V-04: Plane 2 e.6 names it. V-05: Plane 3 e.5–e.6 names it. V-02/V-03: no cell anchor audit plane, prohibition not applicable. Requires C-43. |
| C-47 | FAIL | PASS | FAIL | PASS | PASS | V-02: CHECK (e) e.3 names ORPHANED SCHEMA as logically independent symmetric class with independent audit direction. V-04: Plane 1 e.3 names both classes. V-05: Plane 1 e.3 names both. V-01/V-03: no registry plane. Requires C-44. |
| C-48 | FAIL | FAIL | PASS | FAIL | PASS | V-03: SCHEMA-A BASELINE SOURCE VIOLATION as named rejection clause in Format Contract body. V-05: same, plus three-plane CHECK (e) enforces it at Plane 2. V-01/V-02/V-04: no BURST PATH TABLE, clause cannot appear. Requires C-45. |

#### Aspirational passing count

| Variation | C-09..C-42 | C-43 | C-44 | C-45 | C-46 | C-47 | C-48 | Total |
|-----------|-----------|------|------|------|------|------|------|-------|
| V-01 | 34/34 | PASS | FAIL | FAIL | PASS | FAIL | FAIL | 36/40 |
| V-02 | 34/34 | FAIL | PASS | FAIL | FAIL | PASS | FAIL | 36/40 |
| V-03 | 34/34 | FAIL | FAIL | PASS | FAIL | FAIL | PASS | 36/40 |
| V-04 | 34/34 | PASS | PASS | FAIL | PASS | PASS | FAIL | 38/40 |
| V-05 | 34/34 | PASS | PASS | PASS | PASS | PASS | PASS | 40/40 |

---

### Independence Confirmation

| V | C-46 | C-47 | C-48 | Delta vs. baseline (35 prior) |
|---|------|------|------|-------------------------------|
| V-01 (C-46 seed) | PASS | FAIL | FAIL | +0.75 |
| V-02 (C-47 seed) | FAIL | PASS | FAIL | +0.75 |
| V-03 (C-48 seed) | FAIL | FAIL | PASS | +0.75 |
| V-04 (C-46+C-47) | PASS | PASS | FAIL | +1.50 |
| V-05 (all three) | PASS | PASS | PASS | +2.25 |

**C-46, C-47, C-48 confirmed independent.** Each criterion adds exactly 0.75 pts when present. V-04 (2 criteria) = V-01 + V-02 delta. V-05 (3 criteria) = V-01 + V-02 + V-03 delta. No interaction effects.

---

### Key Findings

**C-46 enforcement boundary** (V-01): The minimum viable addition is one sentence in e.3 of CHECK (e). The sentence does two things: names the prohibited form by its exact label ("missing or invalid prefix") and declares that a report using that label for both classes does not satisfy the requirement. The constraint is localized entirely to the CHECK instruction — no other role changes. This makes it the minimum viable patch for the C-43 gap: C-43 required the two classes to be "explicitly distinguished" but did not name the merged form that re-conflates them at summary level.

**ORPHANED SCHEMA as symmetric counterpart** (V-02): C-44's REGISTRY GAP detects undercounting (row count comparison). V-02's C-47 closes the reverse direction: ORPHANED SCHEMA detects misalignment by scanning body entries against registry rows. The two detection methods are different (count comparison vs. entry scan), the two failure modes are different (missing row vs. stale body entry), and both can coexist. The symmetric framing — "REGISTRY GAP = registry smaller than it should be; ORPHANED SCHEMA = registry has what it shouldn't" — makes both directions auditable in a single pass without requiring separate queries.

**Named rejection clause enables scan-time flagging without context** (V-03): Without SCHEMA-A BASELINE SOURCE VIOLATION in the Format Contract, an auditor reading a BASELINE cell that writes "BP-01: 600 req/min" must consult the routing requirement in a different section to determine whether it violates C-45. With the named clause, the Format Contract is self-authoritative: the cell is testable against the clause directly. V-03 explicitly notes the C-41 vs. C-45 distinction inline — a cell satisfies C-41 (cross-role ID anchoring) but violates C-45 (BURST PATH TABLE routing) — making the violation class distinguishable from a different kind of format compliance.

**Three-plane architecture** (V-05): Separating CHECK (e) into three independent planes means partial failure is attributable by traceability level: Plane 1 = document-structure completeness (registry), Plane 2 = baseline-definition traceability (BURST PATH TABLE routing), Plane 3 = per-cell semantic validity (anchor + resolved reference). A document that fails Plane 2 but passes Planes 1 and 3 has a baseline-definition problem, not a registry or cell problem. This is a diagnostic upgrade over a flat audit that would aggregate all three planes into a single findings block.

---

### Excellence Signals from V-05

1. **Named prohibited form converts structural requirement to output obligation** — C-43 requiring "explicit distinction" is satisfied by enumerating both classes; C-46's named prohibition forecloses the summary-level re-conflation. Pattern: whenever a criterion requires two things to be "distinguished," escalate by naming the merged form as a labeled violation.

2. **Symmetric violation class closes reverse direction of completeness contract** — C-44's REGISTRY GAP audits one direction (what's missing from the registry); C-47's ORPHANED SCHEMA audits the other (what's in the body but not the registry). Pattern: any single-direction completeness check should be paired with its symmetric counterpart.

3. **Format Contract rejection clause as scan-time authority** — placing the named violation class directly in the Format Contract's rejection clause list makes it independently citable without external context lookup. Pattern: whenever a routing or structural requirement exists, add a named rejection clause at declaration site, not only in the CHECK instruction.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["named prohibited merged form converts structural distinctness into output obligation: 'missing or invalid prefix' must be labeled non-compliant in the CHECK instruction, not merely absent from the enumeration", "symmetric violation class closes reverse direction of completeness contract: REGISTRY GAP catches undercounting; ORPHANED SCHEMA catches misalignment -- both detection methods and failure modes are independent", "Format Contract rejection clause as scan-time authority: named violation class in the Format Contract body makes the constraint independently citable without consulting the routing requirement elsewhere"]}
```
