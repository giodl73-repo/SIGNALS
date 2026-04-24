Rubric v2 written to `simulations/quest/rubrics/trace-contract-rubric-v2-2026-03-14.md`.

---

**What changed:**

Three new aspirational criteria extracted from V-03's structural patterns:

| ID | Pattern | What it tests |
|----|---------|---------------|
| C-11 | Classification-before-analysis gate | Phase separation is explicit — no hypotheses during diff construction |
| C-12 | Negative-constraint gate | Expected phase verifies actual was *not referenced* (isolation, not just ordering) |
| C-13 | Calibration gate | An explicit pre-finalization checkpoint exists that reviews severity distribution |

**Key distinction preserved:** C-09 tests the *output* (distribution is calibrated). C-13 tests the *mechanism* (a gate produced it). These are independent — a model can rubber-stamp C-13 and still fail C-09, or produce a calibrated output by accident and pass C-09 without ever having a gate. Both matter.

**Scoring formula updated:** Aspirational tier grows from 2 to 5 criteria; formula changes from `A/2 * 10` to `A/5 * 10`. This softens the per-criterion aspirational weight intentionally — the new criteria are harder to hit (process gates, not output properties), so each point is worth less in absolute terms but the ceiling stays 10.
 for why the deviation occurred (e.g., missing field mapping, schema version mismatch, null handling). Observations without hypotheses do not pass. |
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
| C-11 | **Classification-before-analysis gate is present** | aspirational | process | The artifact separates the diff/classification phase from the root-cause/analysis phase. No root cause hypotheses appear during the diff construction step. The gate between phases is explicit -- a section break, label, or sign-off line -- so that classification and analysis are never interleaved. Source: V-03 PHASE 3 pattern. |
| C-12 | **Negative-constraint on expected phase** | aspirational | behavior | The expected phase includes a verification that actual output was *not* referenced -- not merely that the expected block is present. An isolation check ("no actual output consulted at this point") is distinct from an ordering check ("expected appears before actual"). Artifacts that confirm ordering but not isolation do not pass. Source: V-03 GATE 1 pattern. |
| C-13 | **Calibration gate enforces severity distribution** | aspirational | correctness | The artifact contains an explicit checkpoint -- before findings are finalized -- that reviews whether the severity distribution is reasonable. A passing gate must name the check (e.g., "severity distribution reviewed -- not all one level unless explicitly justified"), not just produce a calibrated result. C-09 tests the output; C-13 tests whether a gate produced it. Source: V-03 GATE 4 pattern. |

---

## Design Notes

**v1 rationale (unchanged):** C-01 enforces contract-first thinking; C-03 and C-04 together prevent "diff dumps" with no analysis; C-07 keeps the Connectors domain concrete rather than generic.

**v2 additions -- why these three patterns earned aspirational status:**

- **C-11 (classification gate):** The most common trace-contract failure is writing findings while constructing the diff -- analysis contaminates classification. Separating phases structurally improves both the diff quality (classification is exhaustive before any hypothesis is formed) and finding quality (hypotheses are not anchored to the first plausible explanation). No Round 1 variation except V-03 used this separation.

- **C-12 (negative-constraint gate):** Ordering checks (expected before actual) allow contamination if the model looks ahead. An isolation check -- verifying actual was *not referenced* during the expected phase -- is a strictly stronger mechanism. The distinction matters in automated or partially-automated runs where the model has access to both blocks. V-03 is the only variation to implement this as a gate rather than a step label.

- **C-13 (calibration gate):** C-09 tests whether the severity distribution happens to be calibrated. C-13 tests whether there is an explicit mechanism that produced calibration -- a gate that fires before findings are finalized. In Round 1, C-09 passed only for V-03, and only because GATE 4 converted the nudge to an enforcement check. The 2.5-point margin between V-03 (100) and the next tier (97.5) came entirely from this mechanism.

---

## Scoring Worksheet

| Tier | Criteria | Pass Count | Max | Weight | Points |
|------|----------|------------|-----|--------|--------|
| Essential | C-01 to C-05 | _/5 | 5 | 60 | _ |
| Recommended | C-06 to C-08 | _/3 | 3 | 30 | _ |
| Aspirational | C-09 to C-13 | _/5 | 5 | 10 | _ |
| **Composite** | | | | | **(E/5 * 60) + (R/3 * 30) + (A/5 * 10)** |

**Golden**: all essential pass (5/5) AND composite >= 80.

---

## Changelog

| Version | Change |
|---------|--------|
| v1 | Initial rubric -- 10 criteria (5 essential, 3 recommended, 2 aspirational) |
| v2 | Add C-11 (classification gate), C-12 (negative-constraint gate), C-13 (calibration gate) from V-03 Round 1 excellence signals. Aspirational tier grows from 2 to 5; scoring formula updated to A/5 * 10. |
