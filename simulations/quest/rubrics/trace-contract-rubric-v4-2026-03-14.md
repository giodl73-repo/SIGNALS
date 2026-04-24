v4 written. Here's what was extracted and why:

---

## Four new aspirational criteria from Round 3

| ID | Pattern | Source | What it tests |
|----|---------|--------|---------------|
| C-17 | Domain element-type taxonomy as structural column | V-03/V-05 R3, GATE 3 | *Whether* domain engagement is structural (pre-printed column + gate enforcement) vs. incidental (vocabulary in prose). C-07 tests presence; C-17 tests structural enforcement |
| C-18 | Standalone calibration phase with severity tally table | V-04/V-05 R3, Phase 4B | *Whether* calibration is an isolated first-class phase or a gate item within findings. C-13 tests that a calibration gate exists; C-18 tests that it cannot be merged with or buried in findings |
| C-19 | All gate outcomes as independent queryable frontmatter keys | V-02/V-05 R3, multi-gate manifest | *Completeness* of machine-readable gate recording. C-16 requires at least one key; C-19 requires every gate independently filterable |
| C-20 | Gate-level blank-cell enforcement for all required columns | V-03/V-05 R3, three-column GATE 3 | *Universality* of the C-15 pattern. C-15 names Severity + Spec Ref; C-20 requires every required column the template defines to have the same gate-level prohibition |

**Key distinction ladder preserved (C-15 -> C-20):** An artifact can pass C-15 by gating Severity and Spec Ref while accepting blank cells in an element-type column it designates required. C-20 generalizes: the gate-level blank-cell pattern applies universally to all columns the template defines as required.

**Key distinction preserved (C-13 -> C-18):** A combined GATE 4 that handles both findings completeness and calibration passes C-13. A standalone Phase 4B where calibration work is the *only* permitted activity, with a severity tally table and CONTRACT DELTA gated behind it, is the strictly stronger form that C-18 requires.

**Scoring formula updated:** Aspirational tier grows from 8 to 12 criteria; formula changes from `A/8 * 10` to `A/12 * 10`. Per-criterion weight softens to ~0.83 points. C-17 through C-20 are template-design decisions that require explicit structural choices, so per-criterion weight softening is appropriate -- the ceiling stays 10 but each criterion is proportionally weighted.
eld mappings, or error response shapes. Generic output comparisons that ignore the contract domain do not pass. |
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
| C-17 | **Domain element-type taxonomy enforced as structural column** | aspirational | coverage | The classification table includes a pre-printed domain element-type column with a fixed vocabulary (e.g., schema-field, auth-handshake, action-payload, trigger-payload, error-shape, metadata) required on every field row. Blank element-type cells are a gate failure condition, not a vocabulary suggestion. C-07 tests that domain vocabulary appears in findings prose or role names; C-17 tests that a domain taxonomy column is structurally required across all phases with gate-level blank-cell enforcement identical to Severity and Spec Ref. An artifact that names domain elements in findings text but lacks the pre-printed column does not pass. Source: V-03/V-05 Round 3 excellence signal. |
| C-18 | **Calibration is a standalone first-class phase with severity tally table** | aspirational | process | Severity calibration is implemented as a dedicated, named phase (e.g., Phase 4B) separate from the findings phase -- not a gate item appended to findings. The phase must include a severity tally table that counts findings by level before the assessment is written. The CONTRACT DELTA section is gated behind this calibration phase and cannot proceed until the phase gate passes. C-13 tests that a calibration gate fires before findings are finalized; C-18 tests that calibration is structurally isolated as its own phase, making it impossible to merge calibration with findings or skip it to reach the delta. A combined Phase 4 that handles both findings completeness and calibration does not pass. Source: V-04/V-05 Round 3 excellence signal, Phase 4B pattern. |
| C-19 | **All gate outcomes recorded as independent queryable frontmatter keys** | aspirational | automation | The artifact records every gate outcome as a separate queryable frontmatter key (e.g., gate1_isolation_confirmed, gate2_actual_complete, gate3_diff_complete, gate4b_calibration_confirmed). C-16 requires at least one queryable key; C-19 requires complete coverage -- every gate has its own key -- enabling downstream automation to independently verify any individual gate without treating the artifact as a single pass/fail. An artifact with four or more gates and only one frontmatter key passes C-16 but fails C-19. Source: V-02/V-05 Round 3 excellence signal, multi-gate manifest pattern. |
| C-20 | **Gate-level blank-cell enforcement covers all required classification columns** | aspirational | process | Every column designated as required in the template has its own gate-level blank-cell check, not only Severity and Spec Ref. If the artifact defines a domain element-type column, a connector-surface column, or any other required field, each must appear as an explicit gate item that makes blank cells a gate failure condition. C-15 requires gate enforcement for Severity and Spec Ref; C-20 requires that the same enforcement extends to all required columns the template defines. An artifact that gates Severity and Spec Ref but not an element-type column it designates as required passes C-15 but fails C-20. Source: V-03/V-05 Round 3 excellence signal, three-column GATE 3 pattern. |

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

**v4 additions -- why C-17/C-18/C-19/C-20 earned aspirational status:**

- **C-17 (domain taxonomy as structural column):** C-07 tests that domain vocabulary appears somewhere in the artifact -- in role names, in finding prose, in root cause scaffolds. V-03/V-05 Round 3 show a strictly stronger form: a pre-printed 6-way element-type column applied at every phase boundary, with gate-level blank-cell prohibition. Domain coverage becomes a structural guarantee rather than a vocabulary nudge. An artifact can pass C-07 by mentioning "connector schema" in a root cause hypothesis while accepting blank element-type cells in 40% of diff rows. C-17 closes that gap. The distinction: C-07 tests presence; C-17 tests structural enforcement.

- **C-18 (standalone calibration phase):** C-13 tests that a calibration gate fires before findings are finalized. V-04 Round 3 shows that calibration can be elevated further: a dedicated Phase 4B with its own opening instruction ("do not merge Phase 4 and Phase 4B"), a severity tally table that forces a count before assessment, and a CONTRACT DELTA gate behind the phase rather than appended to it. In a combined gate (V-02/V-05 R2), findings completeness and calibration share a GATE 4 -- calibration items can be deprioritized when completeness items dominate. Phase 4B makes that impossible. Both forms pass C-13; only the standalone phase passes C-18.

- **C-19 (full gate manifest):** C-16 tests for the presence of at least one queryable frontmatter key. V-02 Round 3 shows that recording every gate independently (6 keys across 4 phases) enables qualitatively different automation: a CI pipeline can separately verify isolation (gate1), diff cleanliness (gate3_diff_complete), and calibration (gate4b_calibration_confirmed) without parsing prose or treating the artifact as a single pass/fail unit. An artifact with a single `gate1_isolation_confirmed: true` key passes C-16 but leaves all downstream gates opaque. C-19 requires complete coverage.

- **C-20 (universal column completeness at gate level):** C-15 names exactly two columns: Severity and Spec Ref. V-03/V-05 Round 3 show the same gate-enforcement pattern applies to any column the template designates as required -- including domain-specific columns like element type. An artifact that gates Severity and Spec Ref but accepts blank cells in an element-type column it labels required has applied the C-15 pattern selectively. C-20 generalizes it: the gate-level blank-cell check must cover every required column the template defines, without exception. C-15 and C-20 are additive -- C-15 establishes the pattern for the two essential columns; C-20 requires it to extend to all.

**Key distinction ladder (C-12 -> C-14):** C-12 tests *what* the isolation check says (negative-constraint language, not just ordering). C-14 tests *how* it is bound (confirmable checkpoint, not freeform prose). A variation can pass C-12 via prose and fail C-14 (V-02 Round 2). A variation that has a gate checkbox with weak language ("actual seen after expected") would pass C-14 structurally but fail C-12 semantically. Both dimensions matter.

**Key distinction (C-02/C-03 -> C-15 -> C-20):** C-02 and C-03 require the columns to be present and populated. C-15 requires the gate to enforce completeness on Severity and Spec Ref. C-20 requires gate enforcement on every required column. An artifact can pass C-02/C-03 by having no blank cells (inspection) while failing C-15 if no gate checks for blanks. It can pass C-15 while failing C-20 if a domain column is required but not gated. The ladder from inspection compliance to structural enforcement now applies universally.

**Key distinction (C-13 -> C-18):** C-13 tests whether a named calibration checkpoint fires before findings are finalized. C-18 tests whether calibration is a structurally isolated phase that cannot be merged, skipped, or dominated by findings-completeness work. Both dimensions are independent: a combined GATE 4 passes C-13; only a standalone Phase 4B passes C-18.

**Key distinction (C-07 -> C-17):** C-07 tests domain vocabulary presence in findings (role names, root cause prose, next-step specificity). C-17 tests that domain taxonomy is a structural column enforced at gate level. An artifact passes C-07 by naming "connector schema" in two root cause hypotheses while leaving element-type cells blank in the diff. It passes C-17 only when every required field row carries a pre-printed vocabulary value and gate-level enforcement prohibits blank cells.

**Key distinction (C-16 -> C-19):** C-16 requires at least one queryable frontmatter key. C-19 requires complete coverage -- every gate independently queryable. An artifact with six gates and one frontmatter key passes C-16 and fails C-19. The distinction enables per-phase pipeline filtering vs per-artifact pass/fail filtering.

**Declaration form equivalency (confirmed in Round 3):** CONFIRMED/NOT CONFIRMED numbered declarations satisfy C-14 and C-15 as "equivalent confirmable gate items." The criterion tests active token production and two-clause language preservation, not checkbox syntax specifically. V-01 Round 3 passes both criteria via declarations.

---

## Scoring Worksheet

| Tier | Criteria | Pass Count | Max | Weight | Points |
|------|----------|------------|-----|--------|--------|
| Essential | C-01 to C-05 | _/5 | 5 | 60 | _ |
| Recommended | C-06 to C-08 | _/3 | 3 | 30 | _ |
| Aspirational | C-09 to C-20 | _/12 | 12 | 10 | _ |
| **Composite** | | | | | **(E/5 * 60) + (R/3 * 30) + (A/12 * 10)** |

**Golden**: all essential pass (5/5) AND composite >= 80.

**Scoring note:** Aspirational tier grows from 8 to 12 criteria; formula changes from `A/8 * 10` to `A/12 * 10`. Per-criterion weight softens to ~0.83 points intentionally -- C-17 through C-20 are structural-enforcement patterns requiring explicit template design decisions, harder to hit than output properties, so the ceiling stays 10 but each criterion contributes equally.

---

## Changelog

| Version | Change |
|---------|--------|
| v1 | Initial rubric -- 10 criteria (5 essential, 3 recommended, 2 aspirational) |
| v2 | Add C-11 (classification gate), C-12 (negative-constraint gate), C-13 (calibration gate) from V-03 Round 1 excellence signals. Aspirational tier grows from 2 to 5; scoring formula updated to A/5 * 10. |
| v3 | Add C-14 (isolation checkpoint confirmability), C-15 (column completeness at gate level), C-16 (machine-readable gate frontmatter) from V-05 Round 2 excellence signals. Aspirational tier grows from 5 to 8; scoring formula updated to A/8 * 10. |
| v4 | Add C-17 (domain element-type taxonomy as structural column), C-18 (standalone calibration phase with severity tally table), C-19 (all gate outcomes as independent queryable frontmatter keys), C-20 (gate-level blank-cell enforcement for all required columns) from Round 3 excellence signals. Aspirational tier grows from 8 to 12; scoring formula updated to A/12 * 10. |
