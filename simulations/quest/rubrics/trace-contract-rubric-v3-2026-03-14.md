v3 written. Here's what was extracted and why:

---

## Three new aspirational criteria from Round 2

| ID | Pattern | Source | What it tests |
|----|---------|--------|---------------|
| C-14 | Two-clause isolation as confirmable checkpoint | V-05 GATE 1 | *How* the isolation check is bound — checkbox, not prose. C-12 requires the right language; C-14 requires it be structurally confirmable |
| C-15 | Column completeness enforced at gate level | V-05 GATE 3 | Blank Severity/Spec Ref cells are a gate failure condition, not just an instruction violation. Converts C-02/C-03 from inspection compliance to structural enforcement |
| C-16 | Machine-readable gate outcome in frontmatter | V-05 frontmatter | At least one gate result is a queryable field (`gate1_isolation_confirmed: true`). Enables downstream automation to filter confirmed runs without prose parsing — new in Round 2, absent from all other variations |

**Key distinction preserved (C-12 → C-14):** V-02 passes C-12 via role-attestation prose. V-05 passes both C-12 and C-14. A weak checkbox ("actual seen after expected") could pass C-14 but fail C-12. Both dimensions are independent.

**Key distinction preserved (C-02/C-03 → C-15):** An artifact can have no blank cells (passing C-02/C-03 by inspection) while failing C-15 if no gate enforces it. Conversely, a GATE 3 checkbox can exist and still fail C-02 if the gate was never confirmed.

**Scoring formula updated:** Aspirational tier grows from 5 to 8 criteria; formula changes from `A/5 * 10` to `A/8 * 10`. Per-criterion weight softens again intentionally — C-14/C-15/C-16 are automation-layer patterns, harder to hit than output properties, so the ceiling stays 10 but each criterion contributes 1.25 points.
----|--------|----------|----------------|
| C-06 | **Three-directory structure is explicit** | recommended | format | The artifact references or mirrors the three-directory pattern: input (10+), expected (20+), actual (30+). At minimum, the expected and actual outputs are clearly separated with labels. |
| C-07 | **Automate/Connectors contract domain is engaged** | recommended | coverage | The findings reference domain-specific contract elements: connector schema, action/trigger payloads, authentication handshake, field mappings, or error response shapes. Generic output comparisons that ignore the contract domain do not pass. |
| C-08 | **Findings are actionable** | recommended | depth | Each finding includes a suggested resolution or next investigation step. "Investigate further" alone does not pass; it must name what to investigate. |

---

## Aspirational Criteria (raise the bar once essential/recommended are stable)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Severity distribution is calibrated** | aspirational | correctness | The artifact shows judgment in severity assignment: not all findings are breaking, not all are cosmetic. At least two distinct severity levels appear across findings, or a single severity is explicitly justified. |
| C-10 | **Contract delta is summarized for spec update** | aspirational | depth | The artifact ends with a consolidated delta section listing which spec clauses need amendment, suitable for direct input into a spec update workflow (finding lifecycle entry). |
| C-11 | **Classification-before-analysis gate is present** | aspirational | process | The artifact separates the diff/classification phase from the root-cause/analysis phase. No root cause hypotheses appear during the diff construction step. The gate between phases is explicit -- a section break, label, or sign-off line -- so that classification and analysis are never interleaved. Source: V-03 Round 1 PHASE 3 pattern. |
| C-12 | **Negative-constraint on expected phase** | aspirational | behavior | The expected phase includes a verification that actual output was *not* referenced -- not merely that the expected block is present. An isolation check ("no actual output consulted at this point") is distinct from an ordering check ("expected appears before actual"). Artifacts that confirm ordering but not isolation do not pass. Source: V-03 Round 1 GATE 1 pattern. |
| C-13 | **Calibration gate enforces severity distribution** | aspirational | correctness | The artifact contains an explicit checkpoint -- before findings are finalized -- that reviews whether the severity distribution is reasonable. A passing gate must name the check (e.g., "severity distribution reviewed -- not all one level unless explicitly justified"), not just produce a calibrated result. C-09 tests the output; C-13 tests whether a gate produced it. Source: V-03 Round 1 GATE 4 pattern. |
| C-14 | **Isolation check is a confirmable checkpoint, not prose** | aspirational | behavior | The negative-constraint isolation attestation (C-12) is implemented as a fillable checkbox or equivalent confirmable gate item -- not freeform prose. The two-clause form must be explicit: "not just ordered after, but not consulted at all." A prose instruction ("do not reference the actual") does not pass; a confirmable check item ("[ ] Actual output was not referenced during this phase -- not just ordered after, but not consulted at all") does. Distinct from C-12, which requires the isolation check to exist; C-14 requires it to be structurally confirmable. Source: V-05 Round 2 GATE 1 pattern. |
| C-15 | **Column completeness is enforced at gate level** | aspirational | process | The classification gate includes checkbox conditions that make blank Severity or Spec Ref cells a gate failure condition, not just an instruction violation. A gate that says "[ ] No Severity cells blank on mismatch rows" converts C-02 from instruction compliance to structural enforcement. An artifact that has C-02/C-03 column instructions but no gate-level blank-cell check does not pass. Source: V-05 Round 2 GATE 3 pattern. |
| C-16 | **Gate outcome recorded as machine-readable frontmatter** | aspirational | automation | The artifact contains at least one frontmatter field recording a gate outcome as a queryable value (e.g., `gate1_isolation_confirmed: true`). This enables downstream automation to filter confirmed runs without prose parsing. Prose attestations, even if explicit, do not pass this criterion. Source: V-05 Round 2 frontmatter pattern. |

---

## Design Notes

**v1 rationale (unchanged):** C-01 enforces contract-first thinking; C-03 and C-04 together prevent "diff dumps" with no analysis; C-07 keeps the Connectors domain concrete rather than generic.

**v2 additions -- why C-11/C-12/C-13 earned aspirational status:**

- **C-11 (classification gate):** The most common trace-contract failure is writing findings while constructing the diff -- analysis contaminates classification. Separating phases structurally improves both the diff quality (classification is exhaustive before any hypothesis is formed) and finding quality (hypotheses are not anchored to the first plausible explanation). No Round 1 variation except V-03 used this separation.

- **C-12 (negative-constraint gate):** Ordering checks (expected before actual) allow contamination if the model looks ahead. An isolation check -- verifying actual was *not referenced* during the expected phase -- is a strictly stronger mechanism. The distinction matters in automated or partially-automated runs where the model has access to both blocks. V-03 is the only variation to implement this as a gate rather than a step label.

- **C-13 (calibration gate):** C-09 tests whether the severity distribution happens to be calibrated. C-13 tests whether there is an explicit mechanism that produced calibration -- a gate that fires before findings are finalized. In Round 1, C-09 passed only for V-03, and only because GATE 4 converted the nudge to an enforcement check.

**v3 additions -- why C-14/C-15/C-16 earned aspirational status:**

- **C-14 (isolation checkpoint confirmability):** V-02 in Round 2 passed C-12 via role-attestation prose; V-05 passed C-12 via a structural gate checkbox. Both satisfy C-12. But V-05's form is strictly stronger: the two-clause phrasing ("not just ordered after, but not consulted at all") is bound to a confirmable gate item, not inferred from section position or role prose. In automated runs, a checkbox can be enforced mechanically; prose cannot. C-14 captures this structural distinction that C-12 does not require.

- **C-15 (column completeness at gate level):** C-02 and C-03 test that the Severity and Spec Ref columns exist and are populated. But "populated" in v1/v2 is verified by inspection -- there is no mechanism that prevents a blank cell from slipping through. V-05 GATE 3 converts blank cells into a gate failure condition ("[ ] No Severity cells blank on mismatch rows"). This is a structural guarantee, not instruction compliance. The criterion captures an entire class of silent failures that pass the essential tier by coincidence.

- **C-16 (machine-readable frontmatter):** All prior patterns require reading prose or section structure to determine whether a gate passed. V-05 introduces `gate1_isolation_confirmed: true` in frontmatter -- a queryable key. This is new in Round 2 and not present in any other variation. The value is primarily for pipeline automation: a downstream scorer, aggregator, or CI check can filter isolation-confirmed runs without NLP. As signal tooling matures, this pattern becomes load-bearing.

**Key distinction ladder (C-12 -> C-14):** C-12 tests *what* the isolation check says (negative-constraint language, not just ordering). C-14 tests *how* it is bound (confirmable checkpoint, not freeform prose). A variation can pass C-12 via prose and fail C-14 (V-02). A variation that has a gate checkbox with weak language ("actual seen after expected") would pass C-14 structurally but fail C-12 semantically. Both dimensions matter.

**Key distinction (C-02/C-03 -> C-15):** C-02 and C-03 require the columns to be present and populated. C-15 requires the gate to enforce completeness. The same output can satisfy C-02/C-03 by having no blank cells (passing inspection) while failing C-15 if no gate checks for blank cells. Conversely, a variation can have a GATE 3 checkbox for blanks and still fail C-02 if the column is present but the gate was never confirmed.

---

## Scoring Worksheet

| Tier | Criteria | Pass Count | Max | Weight | Points |
|------|----------|------------|-----|--------|--------|
| Essential | C-01 to C-05 | _/5 | 5 | 60 | _ |
| Recommended | C-06 to C-08 | _/3 | 3 | 30 | _ |
| Aspirational | C-09 to C-16 | _/8 | 8 | 10 | _ |
| **Composite** | | | | | **(E/5 * 60) + (R/3 * 30) + (A/8 * 10)** |

**Golden**: all essential pass (5/5) AND composite >= 80.

---

## Changelog

| Version | Change |
|---------|--------|
| v1 | Initial rubric -- 10 criteria (5 essential, 3 recommended, 2 aspirational) |
| v2 | Add C-11 (classification gate), C-12 (negative-constraint gate), C-13 (calibration gate) from V-03 Round 1 excellence signals. Aspirational tier grows from 2 to 5; scoring formula updated to A/5 * 10. |
| v3 | Add C-14 (isolation checkpoint confirmability), C-15 (column completeness at gate level), C-16 (machine-readable gate frontmatter) from V-05 Round 2 excellence signals. Aspirational tier grows from 5 to 8; scoring formula updated to A/8 * 10. |
