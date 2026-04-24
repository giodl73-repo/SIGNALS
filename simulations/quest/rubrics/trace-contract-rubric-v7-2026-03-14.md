`trace-contract-rubric-v7-2026-03-14.md` written.

**What changed:**

**Formula:** `A/20 × 10` → `A/22 × 10`. Per-criterion weight ~0.5 → ~0.455. Ceiling unchanged.

**Two new aspirational criteria:**

| ID | Name | Source | Key distinction |
|----|------|---------|-----------------|
| C-29 | Challenge gate outcome is an independently queryable frontmatter key | V-03/V-05 R6 | C-27 tests the challenge log exists; C-29 tests the challenge outcome is a *separate gate key* (`gate1b_challenge_confirmed`) distinct from `gate1_isolation_confirmed`. Automation cannot distinguish "isolation confirmed, challenge pending" from "both confirmed" when subsumed in one key. |
| C-30 | Two-gate inertia exclusion spanning Phase 0 and GATE 1 | V-04 R6 | C-23 tests the GATE 1 inertia clause; C-30 tests that the same exclusion appears upstream at Phase 0 scope enumeration, before element names are committed. Inertia can enter at scope selection even when blocked at value derivation. |

**Distinction ladder gains two new rungs:**
- `C-27 → C-29`: challenge log exists → challenge outcome independently queryable as its own gate key
- `C-23 → C-30`: inertia excluded at GATE 1 → inertia also excluded at Phase 0, closing the upstream entry point
ny mismatch row does not pass. |
| C-03 | **Spec Reference column populated** | essential | coverage | Every mismatch row in the classification table has a non-blank Spec Reference (or Spec Clause) value. An artifact that includes the column but allows blank cells on any mismatch row does not pass. |
| C-04 | **Root cause hypothesis is a required sub-field** | essential | depth | Each finding includes a named root cause hypothesis as a required sub-field in the finding scaffold. A finding that states a mismatch without a root cause hypothesis does not pass. "Unknown" alone does not pass; the hypothesis must name a candidate mechanism. |
| C-05 | **CONTRACT DELTA section present** | essential | output | The artifact contains a CONTRACT DELTA section that lists spec amendments. A findings section that identifies mismatches without a separate delta consolidation does not pass. |

---

## Recommended Criteria

| ID | Criterion | Tier | Category | Pass Condition |
|----|-----------|------|----------|----------------|
| C-06 | **Expected phase is complete** | recommended | coverage | The expected phase table includes a row for every spec-defined element. An artifact that omits uncertain or low-confidence elements does not pass. The completeness check must be confirmable — not just stated as intent. Source: GATE 1 item 1 pattern. |
| C-07 | **Root cause vocabulary is domain-specific** | recommended | depth | Root cause hypotheses name specific connector-contract mechanisms — field mappings, auth handshakes, action payloads, trigger payloads, error response shapes, or metadata conventions. Generic output comparisons that ignore the contract domain do not pass. |
| C-08 | **Findings are actionable** | recommended | depth | Each finding includes a suggested resolution or next investigation step. "Investigate further" alone does not pass; it must name what to investigate. |

---

## Aspirational Criteria (raise the bar once essential/recommended are stable)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Severity distribution is calibrated** | aspirational | correctness | The artifact shows judgment in severity assignment: not all findings are breaking, not all are cosmetic. At least two distinct severity levels appear across findings, or a single severity is explicitly justified. |
| C-10 | **Contract delta is summarized for spec update** | aspirational | depth | The artifact ends with a consolidated delta section listing which spec clauses need amendment, suitable for direct input into a spec update workflow (finding lifecycle entry). |
| C-11 | **Classification-before-analysis gate is present** | aspirational | process | The artifact separates the diff/classification phase from the root-cause/analysis phase. No root cause hypotheses appear during the diff construction step. The gate between phases is explicit — a section break, label, or sign-off line — so that classification and analysis are never interleaved. Source: V-03 Round 1 PHASE 3 pattern. |
| C-12 | **Negative-constraint on expected phase** | aspirational | behavior | The expected phase includes a verification that actual output was *not* referenced — not merely that the expected block is present. An isolation check ("no actual output consulted at this point") is distinct from an ordering check ("expected appears before actual"). Artifacts that confirm ordering but not isolation do not pass. Source: V-03 Round 1 GATE 1 pattern. |
| C-13 | **Calibration gate enforces severity distribution** | aspirational | correctness | The artifact contains an explicit checkpoint — before findings are finalized — that reviews whether the severity distribution is reasonable. A passing gate must name the check (e.g., "severity distribution reviewed — not all one level unless explicitly justified"), not just produce a calibrated result. C-09 tests the output; C-13 tests whether a gate produced it. Source: V-03 Round 1 GATE 4 pattern. |
| C-14 | **Isolation check is a confirmable checkpoint, not prose** | aspirational | behavior | The negative-constraint isolation attestation (C-12) is implemented as a fillable checkbox or equivalent confirmable gate item — not freeform prose. The two-clause form must be explicit: "not just ordered after, but not consulted at all." A prose instruction ("do not reference the actual") does not pass; a confirmable check item ("[ ] Actual output was not referenced during this phase — not just ordered after, but not consulted at all") does. Distinct from C-12, which requires the isolation check to exist; C-14 requires it to be structurally confirmable. Source: V-05 Round 2 GATE 1 pattern. |
| C-15 | **Column completeness is enforced at gate level** | aspirational | process | The classification gate includes checkbox conditions that make blank Severity or Spec Ref cells a gate failure condition, not just an instruction violation. A gate that says "[ ] No Severity cells blank on mismatch rows" converts C-02 from instruction compliance to structural enforcement. An artifact that has C-02/C-03 column instructions but no gate-level blank-cell check does not pass. Source: V-05 Round 2 GATE 3 pattern. |
| C-16 | **Gate outcome recorded as machine-readable frontmatter** | aspirational | automation | The artifact contains at least one frontmatter field recording a gate outcome as a queryable value (e.g., `gate1_isolation_confirmed: true`). This enables downstream automation to filter confirmed runs without prose parsing. Prose attestations, even if explicit, do not pass this criterion. Source: V-05 Round 2 frontmatter pattern. |
| C-17 | **Domain element-type taxonomy enforced as structural column** | aspirational | coverage | The classification table includes a pre-printed domain element-type column with a fixed vocabulary (e.g., schema-field, auth-handshake, action-payload, trigger-payload, error-shape, metadata) required on every field row. Blank element-type cells are a gate failure condition, not a vocabulary suggestion. C-07 tests that domain vocabulary appears in findings prose or role names; C-17 tests that a domain taxonomy column is structurally required across all phases with gate-level blank-cell enforcement identical to Severity and Spec Ref. An artifact that names domain elements in findings text but lacks the pre-printed column does not pass. Source: V-03/V-05 Round 3 excellence signal. |
| C-18 | **Calibration is a standalone first-class phase with severity tally table** | aspirational | process | Severity calibration is implemented as a dedicated, named phase (e.g., Phase 4B) separate from the findings phase — not a gate item appended to findings. The phase must include a severity tally table that counts findings by level before the assessment is written. The CONTRACT DELTA section is gated behind this calibration phase and cannot proceed until the phase gate passes. C-13 tests that a calibration gate fires before findings are finalized; C-18 tests that calibration is structurally isolated as its own phase, making it impossible to merge calibration with findings or skip it to reach the delta. A combined Phase 4 that handles both findings completeness and calibration does not pass. Source: V-04/V-05 Round 3 excellence signal, Phase 4B pattern. |
| C-19 | **All gate outcomes recorded as independent queryable frontmatter keys** | aspirational | automation | The artifact records every gate outcome as a separate queryable frontmatter key (e.g., gate1_isolation_confirmed, gate2_actual_complete, gate3_diff_complete, gate4b_calibration_confirmed). C-16 requires at least one queryable key; C-19 requires complete coverage — every gate has its own key — enabling downstream automation to independently verify any individual gate without treating the artifact as a single pass/fail. An artifact with four or more gates and only one frontmatter key passes C-16 but fails C-19. Source: V-02/V-05 Round 3 excellence signal, multi-gate manifest pattern. |
| C-20 | **Gate-level blank-cell enforcement covers all required classification columns** | aspirational | process | Every column designated as required in the template has its own gate-level blank-cell check, not only Severity and Spec Ref. If the artifact defines a domain element-type column, a connector-surface column, or any other required field, each must appear as an explicit gate item that makes blank cells a gate failure condition. C-15 requires gate enforcement for Severity and Spec Ref; C-20 requires that the same enforcement extends to all required columns the template defines. An artifact that gates Severity and Spec Ref but not an element-type column it designates as required passes C-15 but fails C-20. Source: V-03/V-05 Round 3 excellence signal, three-column GATE 3 pattern. |
| C-21 | **Calibration gate requires per-element severity justification** | aspirational | correctness | Within the calibration phase gate, each finding's severity is individually justified — not assessed as a group. A gate item of the form "[ ] Each element individually justified at that level" is required; a group-level justification ("all breaking because inertia implies full replacement") is a gate failure condition. C-09 tests that the distribution is calibrated; C-13 tests that a gate fires; C-18 tests that calibration is a standalone phase; C-21 tests that the gate enforces individual justification within that phase. An artifact where the calibration gate fires and the distribution is calibrated but a single rationale covers all findings passes C-09, C-13, and C-18 but fails C-21. Source: V-05 Round 4 GATE 4B item 2. |
| C-22 | **CONTRACT DELTA entries carry priority annotations derived from Phase 4B severity** | aspirational | depth | Each entry in the CONTRACT DELTA section includes a priority annotation derived from the calibrated Phase 4B severity (e.g., `breaking → P1`, `degraded → P2`, `cosmetic → P3`). This creates a structural dependency: the delta cannot be written without first completing Phase 4B, because the priority of each amendment is traceable to a named calibrated severity level. C-10 tests that a consolidated delta exists; C-18 tests that calibration is a standalone phase; C-22 tests that calibration output flows into the delta as a required per-entry annotation. An artifact with a standalone Phase 4B and a CONTRACT DELTA that lists amendments without priority annotations passes C-10 and C-18 but fails C-22. Source: V-05 Round 4 CONTRACT DELTA pattern. |
| C-23 | **Inertia-specific expert-knowledge anti-contamination clause in GATE 1** | aspirational | behavior | GATE 1 includes an explicit clause prohibiting the use of expert runtime knowledge about the connector to constrain expected table construction: "Do not reference what you know the connector currently does." This closes a contamination path distinct from actual output consultation — expert knowledge of current connector behavior can anchor the expected table to known inertia rather than pure spec derivation. C-12 tests that actual output is not referenced; C-14 tests that the isolation check is confirmable; C-23 tests that a second, independent contamination path is explicitly closed at GATE 1. An artifact whose GATE 1 passes C-12 and C-14 for the actual-output path but says nothing about expert knowledge does not pass. Scoped to inertia-framing variations where "what the connector currently does" is a semantically meaningful contamination path; N/A for non-inertia-framing contexts. Source: V-05 Round 4 GATE 1 inertia-specific clause. |
| C-24 | **Spec Clause enforcement present at Phase 1 gate** | aspirational | process | GATE 1 includes an explicit item enforcing Spec Clause column completeness in the expected phase table — not deferred to GATE 3. A 4-item GATE 1 that includes "[ ] No Spec Clause cells blank in expected table rows" prevents blank cells from entering Phase 2 before diff construction begins. C-03 tests that the Spec Clause column is populated; C-20 tests that gate-level enforcement covers all required columns at the classification gate; C-24 tests that Spec Clause enforcement is also applied upstream, at Phase 1 output. An artifact that enforces Spec Clause at GATE 3 only passes C-20 but fails C-24. V-03's 3-item GATE 1 — missing this item, relying on a table note for Phase 1 Spec Clause instruction compliance — is the canonical fail case. Source: V-01/V-02/V-04/V-05 Round 4 4-item GATE 1 pattern; V-03 Round 4 structural gap. |
| C-25 | **Phase 0 scope enumeration creates verifiable prior commitment** | aspirational | process | The artifact includes a Phase 0 step that enumerates all in-scope elements as a named, committed list before Phase 1 begins. GATE 0 fires after Phase 0 and before Phase 1 starts, with at least one explicit gate item confirming the scope list is complete. Phase 1 completeness is then checkable against the Phase 0 list by a reader independent of Phase 1 construction — not self-assessed within the same phase. An artifact that starts Phase 1 without a prior committed scope list, or that verifies completeness only within Phase 1 itself, does not pass. C-06 tests that the expected phase is complete; C-25 tests that completeness is verifiable against a named prior artifact rather than self-declared. When C-25 passes, C-19 coverage must extend to gate0_scope_confirmed — a Phase 0 gate key is required in the frontmatter manifest. Source: V-01/V-04/V-05 Round 5 Phase 0 pattern. |
| C-26 | **Pre-populated skeleton separates coverage commitment from value derivation** | aspirational | process | Phase 1 begins from a pre-committed spec index (skeleton) that separates the element enumeration step from the value derivation step: Step 1 builds the index (element names, types, Spec Clause keys — no expected values); Step 2 fills in expected values for each pre-committed row. Element omission is structurally detectable — a missing element is a blank Expected Value cell in a pre-committed row, not an absent row that slips past a completeness declaration. Coverage is enforced by skeleton shape, not by a completeness assertion written after Phase 1 completes. An artifact that enumerates and derives expected values in a single combined step does not pass. C-06 tests that the expected phase is complete; C-25 tests that completeness is verifiable against a prior committed artifact; C-26 tests that the skeleton structure itself makes omission structurally visible rather than a prose claim. An artifact can satisfy C-26 without C-25 (no Phase 0; skeleton built at Phase 1 start) and C-25 without C-26 (Phase 0 list exists but Phase 1 has no pre-populated skeleton). Source: V-02/V-04/V-05 Round 5 pre-populated skeleton pattern. |
| C-27 | **Challenge log converts GATE 1 isolation attestation to two-reader record** | aspirational | behavior | GATE 1 isolation is backed by a challenge log in which a second reader (e.g., Automate) reviews each Phase 1 row for contamination signals before the gate fires. The gate attestation item references the challenge log as evidence: "[ ] Challenge log reviewed — no contamination signals carried into final table." The attestation is not solely self-certified by the Phase 1 author. C-12 tests that actual output is not referenced; C-14 tests that the isolation check is a confirmable checkpoint; C-27 tests that a second reader's review record backs the attestation — contamination claims are externally validated, not inferred solely from the author's assertion. An artifact with a confirmable two-clause GATE 1 isolation check (passing C-14) that has no challenge log does not pass. Source: V-03/V-05 Round 5 challenge log pattern. |
| C-28 | **CONTRACT DELTA includes required amendment type taxonomy column** | aspirational | depth | The CONTRACT DELTA section includes a required amendment type column with a fixed vocabulary (e.g., add-field, remove-field, change-type, change-enum, change-error-shape, change-auth-flow). The column is orthogonal to the priority column (C-22) and enables amendment grouping by change kind. Blank amendment-type cells are a gate failure condition, not a vocabulary suggestion — the same gate-level blank-cell enforcement applied to Severity and Spec Ref in C-15 extends to the amendment-type column in the delta. An artifact with a CONTRACT DELTA that carries priority annotations (passing C-22) but no amendment-type taxonomy column does not pass. C-10 tests that a consolidated delta exists; C-22 tests that calibration output flows into the delta as priority annotations; C-28 tests that a second, orthogonal classification axis is structurally required alongside priority, enabling amendment batching by change kind independently of urgency. Source: V-05 Round 5 amendment type taxonomy pattern. |
| C-29 | **Challenge gate outcome is an independently queryable frontmatter key** | aspirational | automation | The challenge log outcome is recorded as a separate, independently queryable frontmatter key (e.g., `gate1b_challenge_confirmed`) distinct from the isolation attestation key (`gate1_isolation_confirmed`). Phase 1B (or equivalent challenge gate) is a standalone named gate with its own frontmatter key, enabling automation to verify isolation and challenge completion independently. C-27 tests that a challenge log exists and backs the GATE 1 attestation; C-29 tests that the challenge outcome is a separate gate key — not subsumed within the isolation gate's key. An artifact where a single key (e.g., `gate1_isolation_confirmed`) records the outcome of both isolation attestation and challenge log review passes C-27 but fails C-29. C-19 requires that every gate has its own key; C-29 requires specifically that the challenge gate is treated as its own named gate rather than an item within the isolation gate. Source: V-03/V-05 Round 6 Phase 1B standalone gate pattern. |
| C-30 | **Two-gate inertia exclusion spanning Phase 0 and GATE 1** | aspirational | behavior | Phase 0 scope enumeration includes an explicit instruction prohibiting inertia-anchored scope construction ("do not anchor scope to current connector behavior"), closing the inertia contamination path before element names are committed. Both GATE 0 and GATE 1 carry inertia exclusion instructions — GATE 0 for scope enumeration, GATE 1 for expected value derivation — making it impossible to introduce expert-knowledge inertia at either entry point. C-23 tests the GATE 1 inertia anti-contamination clause only; C-30 tests that the same exclusion is applied upstream at Phase 0, before any element names are written. An inertia-framing artifact whose GATE 1 passes C-23 but whose Phase 0 instruction carries no inertia exclusion has a structural gap: inertia can enter at scope enumeration even though it is blocked at value derivation. Scoped to inertia-framing variations identical to C-23; N/A for non-inertia-framing contexts. Source: V-04 Round 6 dual-gate inertia exclusion pattern. |

---

## Design Notes

**v1 rationale (unchanged):** C-01 enforces contract-first thinking; C-03 and C-04 together prevent
"diff dumps" with no analysis; C-07 keeps the Connectors domain concrete rather than generic.

**v2 additions — why C-11/C-12/C-13 earned aspirational status:**

- **C-11 (classification gate):** The most common trace-contract failure is writing findings while
  constructing the diff — analysis contaminates classification. Separating phases structurally
  improves both the diff quality (classification is exhaustive before any hypothesis is formed) and
  finding quality (hypotheses are not anchored to the first plausible explanation). No Round 1
  variation except V-03 used this separation.

- **C-12 (negative-constraint gate):** Ordering checks (expected before actual) allow contamination
  if the model looks ahead. An isolation check — verifying actual was *not referenced* during the
  expected phase — is a strictly stronger mechanism. The distinction matters in automated or
  partially-automated runs where the model has access to both blocks. V-03 is the only variation to
  implement this as a gate rather than a step label.

- **C-13 (calibration gate):** C-09 tests whether the severity distribution happens to be
  calibrated. C-13 tests whether there is an explicit mechanism that produced calibration — a gate
  that fires before findings are finalized. In Round 1, C-09 passed only for V-03, and only because
  GATE 4 converted the nudge to an enforcement check.

**v3 additions — why C-14/C-15/C-16 earned aspirational status:**

- **C-14 (isolation checkpoint confirmability):** V-02 in Round 2 passed C-12 via role-attestation
  prose; V-05 passed C-12 via a structural gate checkbox. Both satisfy C-12. But V-05's form is
  strictly stronger: the two-clause phrasing ("not just ordered after, but not consulted at all") is
  bound to a confirmable gate item, not inferred from section position or role prose. In automated
  runs, a checkbox can be enforced mechanically; prose cannot. C-14 captures this structural
  distinction that C-12 does not require.

- **C-15 (column completeness at gate level):** C-02 and C-03 test that the Severity and Spec Ref
  columns exist and are populated. But "populated" in v1/v2 is verified by inspection — there is no
  mechanism that prevents a blank cell from slipping through. V-05 GATE 3 converts blank cells into
  a gate failure condition ("[ ] No Severity cells blank on mismatch rows"). This is a structural
  guarantee, not instruction compliance. The criterion captures an entire class of silent failures
  that pass the essential tier by coincidence.

- **C-16 (machine-readable frontmatter):** All prior patterns require reading prose or section
  structure to determine whether a gate passed. V-05 introduces `gate1_isolation_confirmed: true` in
  frontmatter — a queryable key. This is new in Round 2 and not present in any other variation. The
  value is primarily for pipeline automation: a downstream scorer, aggregator, or CI check can
  filter isolation-confirmed runs without NLP. As signal tooling matures, this pattern becomes
  load-bearing.

**v4 additions — why C-17/C-18/C-19/C-20 earned aspirational status:**

- **C-17 (domain taxonomy as structural column):** C-07 tests that domain vocabulary appears
  somewhere in the artifact — in role names, in finding prose, in root cause scaffolds. V-03/V-05
  Round 3 show a strictly stronger form: a pre-printed 6-way element-type column applied at every
  phase boundary, with gate-level blank-cell prohibition. Domain coverage becomes a structural
  guarantee rather than a vocabulary nudge. An artifact can pass C-07 by mentioning "connector
  schema" in a root cause hypothesis while accepting blank element-type cells in 40% of diff rows.
  C-17 closes that gap. The distinction: C-07 tests presence; C-17 tests structural enforcement.

- **C-18 (standalone calibration phase):** C-13 tests that a calibration gate fires before findings
  are finalized. V-04 Round 3 shows that calibration can be elevated further: a dedicated Phase 4B
  with its own opening instruction ("do not merge Phase 4 and Phase 4B"), a severity tally table
  that forces a count before assessment, and a CONTRACT DELTA gate behind the phase rather than
  appended to it. In a combined gate (V-02/V-05 R2), findings completeness and calibration share a
  GATE 4 — calibration items can be deprioritized when completeness items dominate. Phase 4B makes
  that impossible. Both forms pass C-13; only the standalone phase passes C-18.

- **C-19 (full gate manifest):** C-16 tests for the presence of at least one queryable frontmatter
  key. V-02 Round 3 shows that recording every gate independently (6 keys across 4 phases) enables
  qualitatively different automation: a CI pipeline can separately verify isolation (gate1), diff
  cleanliness (gate3_diff_complete), and calibration (gate4b_calibration_confirmed) without parsing
  prose or treating the artifact as a single pass/fail unit. An artifact with a single
  `gate1_isolation_confirmed: true` key passes C-16 but leaves all downstream gates opaque. C-19
  requires complete coverage.

- **C-20 (universal column completeness at gate level):** C-15 names exactly two columns: Severity
  and Spec Ref. V-03/V-05 Round 3 show the same gate-enforcement pattern applies to any column the
  template designates as required — including domain-specific columns like element type. An artifact
  that gates Severity and Spec Ref but accepts blank cells in an element-type column it labels
  required has applied the C-15 pattern selectively. C-20 generalizes it: the gate-level blank-cell
  check must cover every required column the template defines, without exception. C-15 and C-20 are
  additive — C-15 establishes the pattern for the two essential columns; C-20 requires it to extend
  to all.

**v5 additions — why C-21/C-22/C-23/C-24 earned aspirational status:**

- **C-21 (per-element calibration justification):** C-09 tests whether the distribution is
  calibrated. C-13 tests whether a gate fired. C-18 tests whether calibration is a standalone phase.
  V-05 Round 4 introduces a fourth dimension: within the calibration gate, each finding must be
  individually justified at its assigned level — group-level reasoning ("all breaking because inertia
  implies full replacement") is explicitly prohibited as a gate failure condition. This matters
  because group justification can produce a calibrated distribution by coincidence — two breaking,
  one degraded, one cosmetic — without any element-level reasoning. An artifact can pass C-09
  (distribution looks right), C-13 (gate fires), and C-18 (standalone phase) while providing one
  group justification that covers all findings. C-21 closes that gap.

- **C-22 (delta priority annotation from Phase 4B):** C-10 tests that a consolidated delta exists.
  C-18 tests that calibration is a standalone phase. V-05 Round 4 shows that calibration output can
  be made structurally consequential in the delta: each amendment carries a priority
  (`breaking → P1`, `degraded → P2`, `cosmetic → P3`) directly derived from Phase 4B severity.
  This creates a load-bearing structural dependency — the delta cannot be written without first
  completing Phase 4B, because the priority annotation requires a named calibrated severity for each
  entry. No prior variation made calibration structurally upstream of individual delta entries; in
  prior forms, calibration informed but did not gate delta content. C-22 captures this downstream
  dependency that C-10 and C-18 do not require.

- **C-23 (expert-knowledge anti-contamination):** C-12 tests that actual output is not referenced
  during the expected phase. C-14 tests that the isolation check is a confirmable checkpoint. V-05
  Round 4 shows that actual output consultation and expert runtime knowledge are two distinct
  contamination paths. The standard two-clause isolation form ("not just ordered after, but not
  consulted at all") closes the actual-output path; it says nothing about whether the model
  constrains expected table construction using what it knows the connector currently does. In
  inertia-framing contexts, this matters: an agent who knows the connector returns a specific error
  code may anchor the expected table to that knowledge rather than deriving it purely from spec.
  C-23 requires GATE 1 to explicitly close this second path with a named clause. The criterion is
  scoped to inertia-framing variations; for non-inertia-framing contexts, it is N/A.

- **C-24 (Phase 1 Spec Clause gate):** C-03 tests that the Spec Clause column is populated. C-20
  tests that gate-level enforcement covers all required columns at the classification gate (GATE 3).
  Both are satisfied by GATE 3 enforcement — which fires after the expected table has already been
  committed and diff construction has already run. V-01/V-02/V-04/V-05 Round 4 all include a
  4-item GATE 1 adding "[ ] No Spec Clause cells blank in the expected table" — enforcing
  completeness before the expected table enters Phase 2. V-03's 3-item GATE 1 is the canonical fail
  case: V-03 passes C-20 because GATE 3 items 1/2/3 cover all three required columns, but Phase 1
  enforcement is instruction-level only. C-24 tests that Spec Clause enforcement is present at both
  gates — upstream at Phase 1 output and downstream at classification — not only downstream.

**v6 additions — why C-25/C-26/C-27/C-28 earned aspirational status:**

- **C-25 (Phase 0 prior commitment):** C-06 tests that the expected phase table covers all
  spec-defined elements — but "complete" is verified within Phase 1 by the same author who built it.
  V-01/V-04/V-05 Round 5 show a strictly stronger mechanism: Phase 0 enumerates in-scope elements
  as a committed, named artifact before Phase 1 begins, and GATE 0 fires before Phase 1 starts.
  Phase 1 completeness is then checkable against the Phase 0 list by a reader independent of Phase 1
  construction — self-assessment is replaced by external verifiability. The distinction is whether
  the completeness claim is checkable against a prior artifact or declared within the same phase
  that produced it. When C-25 passes, the frontmatter manifest (C-19) must extend to
  gate0_scope_confirmed.

- **C-26 (pre-populated skeleton):** C-06 tests completeness by assertion; C-25 tests completeness
  by prior artifact. V-02/V-04/V-05 Round 5 show a third approach: Phase 1 begins from a skeleton
  that pre-commits the element rows (names, types, Spec Clause keys) before expected values are
  derived. The separation of enumeration from derivation makes omission structurally visible — a
  missing element appears as a blank Expected Value cell in a committed row, not as an absent row
  that slips past a completeness check. An artifact can hold C-26 without C-25 (no Phase 0; skeleton
  built at Phase 1 start) and C-25 without C-26 (Phase 0 list exists but Phase 1 derives without a
  skeleton). V-04 and V-05 hold both. The distinction C-26 draws: coverage is enforced by skeleton
  shape, not by a completeness assertion written after the phase is complete.

- **C-27 (challenge log two-reader record):** C-14 tests that the GATE 1 isolation attestation is a
  confirmable checkpoint. V-03/V-05 Round 5 show that a confirmable checkpoint can still be solely
  self-certified — the Phase 1 author checks their own work. A challenge log converts this to a
  two-reader record: a second reader (Automate) reviews each Phase 1 row for contamination signals
  before the gate fires, and the gate item references the log as evidence rather than the author's
  assertion. The improvement is epistemological: contamination claims backed by external review are
  qualitatively stronger than confirmable self-certification. An artifact can have a structurally
  perfect GATE 1 (passing C-12, C-14, C-23, C-24) with no challenge log and pass all four; C-27
  tests the additional property that the isolation claim is externally validated.

- **C-28 (amendment type taxonomy):** C-22 tests that each CONTRACT DELTA entry carries a priority
  annotation derived from Phase 4B severity — a severity-axis classification. V-05 Round 5
  introduces a second, orthogonal axis: an amendment type column with a fixed vocabulary
  (add-field, remove-field, change-type, change-enum, change-error-shape, change-auth-flow).
  Priority answers "how urgent is this amendment?" Amendment type answers "what kind of change is
  this?" The two axes are independent: a breaking add-field and a breaking change-enum both carry P1
  but differ in kind, enabling amendment batching by change kind for spec authoring. Blank
  amendment-type cells are a gate failure condition — the same structural enforcement applied to
  classification columns extends to the delta. An artifact with a delta carrying priority annotations
  but no type taxonomy passes C-22 but fails C-28.

**v7 additions — why C-29/C-30 earned aspirational status:**

- **C-29 (challenge gate queryable key):** C-27 tests that a challenge log exists and backs the
  GATE 1 isolation attestation. V-03/V-05 Round 6 show a strictly stronger form: Phase 1B is a
  standalone gate (GATE 1B) with its own frontmatter key (`gate1b_challenge_confirmed`), independent
  of the isolation key (`gate1_isolation_confirmed`). In V-01/V-02/V-04, the challenge log review
  and isolation attestation share a single GATE 1 key — automation cannot distinguish "isolation
  confirmed but challenge not yet reviewed" from "both confirmed." V-03/V-05 make the challenge
  outcome independently queryable: a pipeline can separately verify that isolation passed
  (gate1_isolation_confirmed) and that the challenge review passed (gate1b_challenge_confirmed)
  without parsing the challenge log prose. C-19 requires that every gate has its own key; C-29
  extends this to require specifically that the challenge gate is a named standalone gate rather than
  an item subsumed within the isolation gate.

- **C-30 (upstream inertia exclusion at Phase 0):** C-23 tests that GATE 1 carries an explicit
  inertia anti-contamination clause — "Do not reference what you know the connector currently does"
  — closing the expert-knowledge contamination path during expected value derivation. V-04 Round 6
  shows that inertia can contaminate even earlier: at Phase 0 scope enumeration, an agent who
  anchors element selection to known connector behavior will commit a biased scope list before Phase 1
  begins. V-04 adds an inertia exclusion instruction to Phase 0 ("do not anchor scope to current
  connector behavior"), closing this upstream contamination path. Two-gate inertia exclusion spans
  both Phase 0 (scope commitment) and GATE 1 (value derivation), making it impossible to introduce
  inertia at either entry point. An artifact whose GATE 1 passes C-23 but whose Phase 0 carries no
  inertia instruction has a structural gap: inertia can enter at scope enumeration even though it is
  blocked at value derivation. C-30 closes this gap. Like C-23, scoped to inertia-framing
  variations; N/A for non-inertia-framing contexts.

**Key distinction ladder (cumulative across versions):**

- **C-12 → C-14:** C-12 tests *what* the isolation check says (negative-constraint language).
  C-14 tests *how* it is bound (confirmable checkpoint, not freeform prose).

- **C-12/C-14 → C-23:** Actual output not referenced (confirmable) → expert runtime knowledge also
  not referenced (inertia-framing only; second contamination path explicitly named and gated).

- **C-12/C-14/C-23 → C-27:** Isolation attestation confirmable and both contamination paths closed
  → attestation backed by second-reader challenge log (external validation, not solely
  self-certified).

- **C-27 → C-29:** Challenge log exists and backs attestation → challenge gate outcome is
  independently queryable as a separate frontmatter key; isolation and challenge independently
  verifiable by automation.

- **C-23 → C-30:** Inertia exclusion at GATE 1 (value derivation) → inertia exclusion also at
  Phase 0 (scope enumeration); both contamination entry points explicitly closed.

- **C-02/C-03 → C-15 → C-20:** Column presence and population (inspection) → gate-level
  enforcement on Severity and Spec Ref → gate-level enforcement on all required columns.

- **C-13 → C-18:** Calibration gate fires → calibration is a structurally isolated phase that
  cannot be merged with findings or skipped.

- **C-07 → C-17:** Domain vocabulary present in prose → domain taxonomy structurally enforced as
  a required column with gate-level blank-cell prohibition.

- **C-09 → C-13 → C-21:** Calibrated distribution exists → gate produced it → gate requires
  per-element justification (group rationale is a gate failure condition).

- **C-10 → C-18 → C-22 → C-28:** Delta section exists → calibration is upstream as standalone
  phase → calibration output is a required per-entry priority annotation → amendment type is a
  second required per-entry annotation orthogonal to priority.

- **C-06 → C-25 → C-26:** Expected phase complete (declared within Phase 1) → completeness
  verifiable against named prior artifact (Phase 0 commitment) → completeness structurally enforced
  by skeleton (omission = visible blank cell, not absent row).

- **C-20 → C-24:** All required columns gated at GATE 3 (classification) → Spec Clause also gated
  at GATE 1 (Phase 1 output), before diff construction begins.
