Rubric written to `simulations/quest/rubrics/trace-contract-rubric-2026-03-14.md`.

**10 criteria across 3 tiers:**

**Essential (5) — must all pass:**
- C-01: Expected output written before actual (behavior)
- C-02: Every mismatch has a severity label — breaking/degraded/cosmetic (correctness)
- C-03: Every mismatch has a spec reference (correctness)
- C-04: Root cause hypothesis per finding (depth)
- C-05: Breaking vs. non-breaking is unambiguous (coverage)

**Recommended (3):**
- C-06: Three-directory structure explicit (format)
- C-07: Automate/Connectors domain engaged — schema, payloads, field mappings (coverage)
- C-08: Findings are actionable with named next steps (depth)

**Aspirational (2):**
- C-09: Severity distribution is calibrated — not all one level (correctness)
- C-10: Consolidated contract delta for spec update workflow (depth)

The key design choices: C-01 enforces the discipline of writing expected-first (contract-first thinking); C-03 and C-04 together prevent "diff dumps" with no analysis; C-07 keeps the Connectors domain concrete rather than generic.
 placeholder. |
| C-02 | **Every mismatch has a severity label** | essential | correctness | Each deviation between expected and actual is tagged with exactly one of: `breaking`, `degraded`, or `cosmetic`. No unlabeled diffs present. |
| C-03 | **Every mismatch has a spec reference** | essential | correctness | Each finding cites the specific spec section, field name, or contract clause it violates. Generic references like "see spec" do not qualify. |
| C-04 | **Root cause hypothesis present for each finding** | essential | depth | Each finding includes at least one stated hypothesis for why the deviation occurred (e.g., missing field mapping, schema version mismatch, null handling). Observations without hypotheses do not pass. |
| C-05 | **Breaking findings are distinguished from non-breaking** | essential | coverage | The output makes it unambiguous which findings block the feature (breaking) vs. degrade it (degraded) vs. are cosmetic. A summary count or section separation is sufficient. |

---

## Recommended Criteria (output is better with these)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **Three-directory structure is explicit** | recommended | format | The artifact references or mirrors the three-directory pattern: input (10+), expected (20+), actual (30+). At minimum, the expected and actual outputs are clearly separated with labels. |
| C-07 | **Automate/Connectors contract domain is engaged** | recommended | coverage | The findings reference domain-specific contract elements: connector schema, action/trigger payloads, authentication handshake, field mappings, or error response shapes. Generic output comparisons that ignore the contract domain do not pass. |
| C-08 | **Findings are actionable** | recommended | depth | Each finding includes a suggested resolution or next investigation step. "Investigate further" alone does not pass; it must name what to investigate. |

---

## Aspirational Criteria (raise the bar once essential/recommended are stable)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Severity distribution is calibrated** | aspirational | correctness | The artifact shows judgment in severity assignment: not all findings are breaking, not all are cosmetic. At least two distinct severity levels appear across findings, or a single severity is explicitly justified. |
| C-10 | **Contract delta is summarized for spec update** | aspirational | depth | The artifact ends with a consolidated delta section listing which spec clauses need amendment, suitable for direct input into a spec update workflow (finding lifecycle entry). |

---

## Scoring Worksheet

| Tier | Criteria | Pass Count | Max | Weight | Points |
|------|----------|------------|-----|--------|--------|
| Essential | C-01 to C-05 | _/5 | 5 | 60 | _ |
| Recommended | C-06 to C-08 | _/3 | 3 | 30 | _ |
| Aspirational | C-09 to C-10 | _/2 | 2 | 10 | _ |
| **Composite** | | | | | **(E/5 * 60) + (R/3 * 30) + (A/2 * 10)** |

**Golden**: all essential pass (5/5) AND composite >= 80.
