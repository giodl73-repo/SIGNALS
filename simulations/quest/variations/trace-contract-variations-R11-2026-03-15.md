Here are the five variations:

---

## Round 11 Variation Map

| | Axis | Primary Targets | Hypothesis |
|--|------|-----------------|------------|
| **V-01** | role-sequence | C-31, C-32, C-29, C-30 | Expert resumes ownership of S5.5 census — engaging spec-reading context at the synthesis step |
| **V-02** | output-format | C-28, C-31, C-32 | Tabular findings with mechanism-type as a column — enumeration constraint becomes structural, Sub-task A becomes a column tally |
| **V-03** | lifecycle-emphasis | C-31, C-32 | S5.5 as hard STOP gate with BLOCKED signal — converts C-31 from advisory to enforced |
| **V-04** | role-sequence + lifecycle-emphasis | C-31, C-32, C-29, C-30 | Expert owns S5.5 + STOP gate — quality (ownership) and emission guarantee (gate) address orthogonal failure modes |
| **V-05** | output-format + phrasing-register | C-28, C-29, C-31, C-32 | Tabular findings + staging lines as decision documentation (rationale clause) — Sub-task A mechanical, Sub-task B deliberate |

---

**Single-axis variations (V-01, V-02, V-03):**

**V-01 — Role Sequence**: The Connectors Contract Expert explicitly resumes at S5.5 with the framing "the findings are Automate's work; the synthesis is yours." Sub-task A is cast as a verification pass (Expert may reclassify tokens). Sub-task B is cast as a contract-level determination about systemic vs. coincident failures. The `[TAXONOMY-CENSUS-COMPLETE]` token carries `census-author:Connectors-Contract-Expert`.

**V-02 — Output Format**: Findings become a table with `Mechanism-Type` as a dedicated column. The enumeration constraint becomes a cell constraint — blank = visible gap. S5.5 Sub-task A is a column scan (mechanical tally) rather than prose-block parse. The key bet: column isolation reduces token drift and re-derivation errors in Summary.

**V-03 — Lifecycle Emphasis**: S5.5 gets a hard `STOP` header with explicit `BLOCKED` language. The gate explicitly calls out the zero-finding case (most common skip path) — "zero findings → both sub-tasks produce one-line outputs — still required." The `STOP gate is lifted` phrasing makes lifting the gate the model's next visible action after emitting `[TAXONOMY-CENSUS-COMPLETE]`.

---

**Combination variations (V-04, V-05):**

**V-04 — Expert + STOP**: Role ownership (quality) and gate enforcement (emission) are non-overlapping. The test: does role ownership independently improve Sub-task B group-candidate accuracy beyond what the gate alone ensures? If not, the gate is load-bearing and ownership is decorative.

**V-05 — Tabular + Rationale Staging**: The tabular column solves Sub-task A (mechanical tally). The remaining weakness is Sub-task B — staging lines can be written as format-compliant fill-in without genuine grouping decisions. Adding a `rationale:` clause to each `group-candidate-N:` line forces the model to document *why* findings are grouped or isolated. Test signal: do rationale-bearing lines produce fewer spurious `mixed` declarations and fewer false single-type groupings?

---

Written to `simulations/quest/golden/trace-contract-variate-R11-census-2026-03-15.md` (new file — the existing R11 files use rubric tracks v11-C-01-C-39 and v16-C-01-C-10; this is the census-rubric track targeting C-26–C-32).
