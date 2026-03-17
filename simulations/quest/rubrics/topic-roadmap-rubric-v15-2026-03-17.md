Reading the scorecard carefully, I identify three new excellence patterns from Round 14 — one per variate axis — that exceed what C-31/C-32/C-33 already test:

- **V-01** (C-31 axis): guard names each failure mode with a formal titled label (LEVEL 1/LEVEL 2 as referenceable identifiers) plus explicit mutual necessity assertion
- **V-02** (C-32 axis): SECTION SCOPE includes an auditor navigation note confirming a C-24 auditor finds the entry enumerated without traversing phase content
- **V-03** (C-33 axis): CONTRACT is absolute document-first (before INERTIA COMPETITOR DECLARATION, not just before Phase 1), names four consequence field sites (adding Phase 5 exit criterion), and includes violation-detection language making absence detectable from the block alone

These become C-34, C-35, C-36. Denominator expands from 50 to 56.

---

# Scoring Rubric — topic-roadmap (topic-plan) v15

## What changed

| Change | Detail |
|--------|--------|
| Version bump | 14 → 15 |
| Formula denominator | `/50 * 10` → `/56 * 10` (28 aspirational × 2 = 56 max) |
| Aspirational range | C-09–C-33 → C-09–C-36 |
| **C-34 added** | PROPOSAL BIAS AUDIT failure mode label precision |
| **C-35 added** | SECTION SCOPE auditor navigation note |
| **C-36 added** | CONTRACT at absolute document-first position |

---

## Three new aspirational criteria

### C-34 — PROPOSAL BIAS AUDIT failure mode label precision
**Category:** safety

The PROPOSAL BIAS AUDIT guard names each of the two failure modes with a formal descriptive title (e.g., LEVEL 1: SYSTEMIC PHASE STRUCTURE BIAS, LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE), making each failure mode referenceable by name from other document sections. C-31 tests whether the guard distinguishes and explains the two failure modes; C-34 tests whether each failure mode carries a formal title that enables cross-referencing — turning explanatory prose into a named reference artifact that the CONTRACT or SECTION SCOPE can cite by label.

- **Full (2):** Both failure modes carry formal descriptive titles co-located in the PROPOSAL BIAS AUDIT guard text; titles are specific enough to be cited from the CONTRACT or SECTION SCOPE by name alone.
- **Partial (1):** One failure mode named with a formal title; the other described without one; or formal titles present but located outside the guard body (e.g., in a preamble annotation only).
- **Fail (0):** Neither failure mode carries a formal named title; guard text describes but does not formally label the two failure modes.

### C-35 — SECTION SCOPE auditor navigation note
**Category:** correctness

The Phase 6 SECTION SCOPE declaration includes an explicit auditor navigation note: a sentence confirming that a C-24 auditor checking Phase 6's declared scope can locate the row-level bias labeling entry from the scope declaration without traversing phase content. C-32 tests whether the scope is updated to include row-level bias labeling; C-35 tests whether that update is designed to serve auditor navigation — i.e., whether the scope declaration itself tells the auditor where to look and what to look for, rather than merely asserting the labeling's presence.

- **Full (2):** SECTION SCOPE includes an explicit navigation note stating that a C-24 auditor verifying row-level bias labeling finds it enumerated in the scope declaration; note identifies the enumeration item by number or label.
- **Partial (1):** SECTION SCOPE references C-24 or auditor navigation in passing (e.g., a parenthetical remark) but does not provide a full navigation note; or the navigation note appears in a preamble outside the SECTION SCOPE declaration itself.
- **Fail (0):** No auditor navigation note in the SECTION SCOPE declaration; or SECTION SCOPE fails C-32.

### C-36 — CONTRACT at absolute document-first position
**Category:** correctness

The OUTPUT SCHEMA CONTRACT is the absolute first section of the document — positioned before the INERTIA COMPETITOR DECLARATION — and satisfies three additional requirements: (a) a self-referential confirmation statement (e.g., "No file read instruction appears before this CONTRACT"), (b) CONTRACT A names all four consequence field sites: Phase 5 table column, Phase 6a column, Phase 6b column, and Phase 5 exit criterion, and (c) CONTRACT B names "Bias blocked by guard" with violation-detection language enabling a scorer to detect column absence from the CONTRACT block alone, without reading any phase content. C-33 tests standalone pre-Phase-1 positioning; C-36 tests whether the CONTRACT is the absolute first reader-encountered content — before all guards including INERTIA COMPETITOR DECLARATION — and whether it is fully self-sufficient for violation detection.

- **Full (2):** CONTRACT is the first section in the document, preceding INERTIA COMPETITOR DECLARATION; self-referential confirmation statement present; CONTRACT A names all four consequence field sites; CONTRACT B includes violation-detection language.
- **Partial (1):** CONTRACT precedes INERTIA COMPETITOR DECLARATION but is missing exactly one of the three additional requirements (self-referential statement, four-site CONTRACT A, or violation-detection language in CONTRACT B).
- **Fail (0):** CONTRACT does not precede INERTIA COMPETITOR DECLARATION; or C-33 fails.

---

**Orthogonality:** C-34 tests naming precision in the guard (extends C-31). C-35 tests auditor navigation in the scope declaration (extends C-32). C-36 tests absolute document anchoring and self-sufficiency of the CONTRACT (extends C-33). All three are independent of each other: C-34 FAIL / C-35 PASS / C-36 PASS is achievable (scope and contract done, guard labels informal). A single-axis variate targeting only C-34 leaves C-35 and C-36 at 0 without any interaction penalty.

**R14 score ceiling under v15:** V-01, V-02, and V-03 (each 46/50 = 9.20 under v14) score 48/56 = 8.57 under v15, each picking up 2 points on their single new target criterion. An R15 variate targeting all three simultaneously achieves 44 (C-09–C-30) + 6 (C-31–C-33) + 6 (C-34–C-36) = 56/56 = 10.00.

---

## Criteria — Essential (all must pass)

### C-01 — INERTIA COMPETITOR DECLARATION at document open
- **Weight:** essential
- **Category:** structure
- **Text:** The skill opens with an INERTIA COMPETITOR DECLARATION naming inertia
  as the primary competitor before any phase content.
- **Pass condition:** Declaration is present at document open, before Phase 1.
  It identifies inertia by name and establishes it as the opponent the skill
  is designed to defeat.

---

### C-02 — Phase ordering enforced
- **Weight:** essential
- **Category:** structure
- **Text:** All phases are present, numbered, and gated. Each phase has an
  explicit ENTRY CONDITION that must be satisfied before the phase opens.
  Phases cannot be skipped or reordered.
- **Pass condition:** All 8 phases present in order. Each phase header includes
  an ENTRY CONDITION. No phase begins without its ENTRY CONDITION satisfied.

---

### C-03 — Phase 1 READ-BARRIER isolates FIRST-RUN from RESTART
- **Weight:** essential
- **Category:** correctness
- **Text:** Phase 1 has a READ-BARRIER that distinguishes two execution paths:
  FIRST-RUN (no existing output file) and RESTART (existing output file).
  The two paths have different instructions and cannot be conflated.
- **Pass condition:** READ-BARRIER present in Phase 1. FIRST-RUN path and
  RESTART path are both defined with distinct instructions. A run cannot
  proceed without resolving which path applies.

---

### C-04 — Phase 2 scans all 9 namespaces with null-row requirement
- **Weight:** essential
- **Category:** completeness
- **Text:** Phase 2 explicitly scans all 9 signal namespaces. For each
  namespace, it records either the signals found or a null declaration.
  No namespace may be silently omitted.
- **Pass condition:** All 9 namespaces enumerated in Phase 2. Skill includes
  explicit instruction to emit a null declaration row for any namespace with
  no signals found — a row for each namespace, even if that row is a null
  declaration.

---

### C-05 — SIGNAL READ-LOCK at Phase 2 exit
- **Weight:** essential
- **Category:** safety
- **Text:** Phase 2 ends with a SIGNAL READ-LOCK that prevents new signals from
  being read after the scan is complete. All subsequent phases operate on the
  locked signal set.
- **Pass condition:** SIGNAL READ-LOCK present at Phase 2 exit with an explicit
  statement of the lock mechanism. Subsequent phases reference the locked
  signal set; no phase reopens signal discovery after the lock.

---

## Recommended Criteria (at least 2 of 3 must pass)

### C-06 — Null path stop enforced at defeat phase
- **Weight:** recommended
- **Category:** correctness
- **Text:** When all defeat assessment verdicts are HOLDS, the skill emits a
  NULL_DELTA declaration and halts. It does not open the proposal phase for
  zero proposals.
- **Pass condition:** Defeat assessment phase contains an explicit conditional:
  "If all verdicts are HOLDS: Emit NULL_DELTA. Stop. Do not open Phase 6."
  A run that generates an empty proposal table after all-HOLDS verdicts fails.

---

### C-07 — Confidence tiers defined
- **Weight:** recommended
- **Category:** depth
- **Text:** Proposals carry a confidence level defined with specific evidential
  criteria. The tiers are HIGH, MEDIUM, and LOW; each is tied to the count
  or type of independent NEW artifacts supporting the defeat.
- **Pass condition:** At least three confidence tiers are defined with their
  evidential backing (e.g., HIGH = two+ independent NEW artifacts; MEDIUM =
  one; LOW = inference). Tiers without evidential criteria do not pass.

---

### C-08 — Exit criterion references consequence field by name
- **Weight:** recommended
- **Category:** correctness
- **Text:** The skill's exit criterion — the condition under which the run is
  considered complete — references the consequence field by its exact name
  as defined in the output schema. The exit criterion is not satisfied by
  presence of proposals alone; it requires consequence field population.
- **Pass condition:** Exit criterion names the consequence field exactly as
  it appears in the output schema. Exit is gated on consequence field
  completion, not merely proposal table presence.

---

## Aspirational Criteria (C-09 through C-36, each worth 2 points)

### C-09 — Defeat signal minimum threshold
**Category:** correctness

The skill defines a minimum number of independent NEW signals required to declare a defeat. "NEW" is defined operationally: signals not present in the prior roadmap version. The threshold is stated before Phase 5 opens.

- **Full (2):** Minimum threshold stated with explicit definition of "NEW" tied to prior-version comparison; threshold is enforced as a Phase 5 entry condition.
- **Partial (1):** Threshold stated but "NEW" not defined operationally; or threshold present but not enforced as a gate.
- **Fail (0):** No minimum threshold; any signal count proceeds to defeat assessment.

---

### C-10 — Signal provenance chain
**Category:** depth

Each signal in the Phase 2 scan carries a provenance declaration: which namespace, which artifact file, and which specific finding within that artifact. Provenance is not inferred; it is stated per signal.

- **Full (2):** Every signal entry includes namespace, artifact path, and finding reference; provenance is machine-checkable (paths are real, not illustrative).
- **Partial (1):** Provenance declared for most signals but missing for some; or provenance format is inconsistent across namespaces.
- **Fail (0):** Signals listed without provenance; or provenance is illustrative only.

---

### C-11 — Prior roadmap version pinned at Phase 1
**Category:** correctness

Phase 1 pins the exact prior roadmap version being compared against. The pin is an artifact reference (file path or version identifier), not a description. All defeat assessments in Phase 5 compare against this pinned version.

- **Full (2):** Prior version pinned by artifact reference in Phase 1; Phase 5 explicitly references the pinned version in each defeat assessment.
- **Partial (1):** Prior version described but not pinned by reference; or pinned in Phase 1 but not carried forward to Phase 5.
- **Fail (0):** No prior version identification; defeat assessments have no explicit comparison baseline.

---

### C-12 — Defeat vocabulary locked
**Category:** correctness

The skill defines a closed vocabulary of defeat verdicts (e.g., DEFEATED, PARTIAL, HOLDS) before Phase 5 opens. No verdict outside the vocabulary may be used. The vocabulary lock is stated explicitly.

- **Full (2):** Closed vocabulary defined before Phase 5; lock statement present; all Phase 5 verdicts use only vocabulary terms.
- **Partial (1):** Vocabulary defined but lock statement absent; or vocabulary defined but one or more Phase 5 verdicts deviate.
- **Fail (0):** No defined vocabulary; verdicts are free-form.

---

### C-13 — PARTIAL defeat handling defined
**Category:** correctness

The skill defines what happens when a defeat verdict is PARTIAL: which proposals are eligible, whether partial defeats count toward the null-path threshold, and how partial defeats are represented in the output table.

- **Full (2):** PARTIAL verdict handling defined with all three elements: proposal eligibility, null-path threshold treatment, and output representation.
- **Partial (1):** PARTIAL handling mentioned but one element missing; or PARTIAL treated identically to DEFEATED without explanation.
- **Fail (0):** No PARTIAL handling; verdicts are binary DEFEATED/HOLDS only.

---

### C-14 — Proposal generation scoped to defeated dimensions only
**Category:** correctness

Phase 6 generates proposals only for dimensions with DEFEATED or PARTIAL verdicts. Proposals for HOLDS dimensions are explicitly prohibited. The prohibition is stated at Phase 6 entry.

- **Full (2):** Prohibition stated at Phase 6 entry; proposals are indexed to defeated dimensions; no proposal may reference a HOLDS dimension.
- **Partial (1):** Prohibition implied but not stated; or proposals indexed to defeated dimensions but HOLDS prohibition not explicit.
- **Fail (0):** No scope restriction; proposals may be generated for any dimension.

---

### C-15 — Proposal table schema complete
**Category:** structure

The output proposal table has a defined schema with at least: proposal text, target dimension, confidence tier, signal count, and consequence field. Schema is stated before Phase 6 populates the table.

- **Full (2):** All five fields present in schema; schema stated before Phase 6; every row in the output table conforms to the schema.
- **Partial (1):** Four of five fields present; or schema stated mid-phase rather than before Phase 6 opens.
- **Fail (0):** No defined schema; table structure is ad hoc.

---

### C-16 — Consequence field populated per proposal
**Category:** correctness

Every proposal row includes a populated consequence field — a specific, falsifiable statement of what remains unchanged if the proposal is not adopted. "No change" or empty entries are not permitted.

- **Full (2):** Every proposal row has a populated, specific consequence statement; no row is empty or uses a generic placeholder.
- **Partial (1):** Most rows populated; one or two rows use generic language or are empty.
- **Fail (0):** Consequence field consistently empty or generic across the table.

---

### C-17 — Signal count per proposal is auditable
**Category:** depth

Each proposal's signal count is auditable: the signals supporting it are listed by reference, not just counted. A reviewer can verify the count without re-scanning Phase 2 output.

- **Full (2):** Signal references listed per proposal; count is derivable from the reference list; no proposal claims a count without enumerable references.
- **Partial (1):** Signal count present but references not listed; or references listed for some proposals but not others.
- **Fail (0):** Signal counts absent or not tied to verifiable references.

---

### C-18 — Phase 7 output is a diff, not a replacement
**Category:** correctness

Phase 7 produces a diff of the roadmap — additions, modifications, and removals — not a full replacement document. Each diff entry is keyed to a specific prior roadmap section.

- **Full (2):** Phase 7 output is structured as a diff; each entry identifies the prior section, the change type (add/modify/remove), and the proposed new content.
- **Partial (1):** Diff structure present but some entries lack prior section keys; or change type not always specified.
- **Fail (0):** Phase 7 produces a full replacement document without diff structure.

---

### C-19 — Phase 8 summarizes defeat coverage
**Category:** depth

Phase 8 includes a defeat coverage summary: how many dimensions were assessed, how many were defeated (fully or partially), and what percentage of the total roadmap surface the proposals address.

- **Full (2):** Defeat coverage summary present with all three elements; percentages are computed from Phase 5 verdicts, not estimated.
- **Partial (1):** Summary present but missing one element; or percentages estimated rather than computed.
- **Fail (0):** No defeat coverage summary in Phase 8.

---

### C-20 — INERTIA-GATE enforced at Phase 5 entry
**Category:** safety

Phase 5 has a named INERTIA-GATE at its entry point. The gate tests whether sufficient new signal mass exists to proceed to defeat assessment. A run that reaches Phase 5 with insufficient signal mass halts at the gate.

- **Full (2):** Named INERTIA-GATE at Phase 5 entry; gate condition stated with explicit signal mass threshold; halt instruction present for gate failure.
- **Partial (1):** Gate present but unnamed; or gate condition stated without a halt instruction.
- **Fail (0):** No gate at Phase 5 entry; defeat assessment opens regardless of signal mass.

---

### C-21 — INERTIA-GATE enforced at Phase 6 entry
**Category:** safety

Phase 6 has a named INERTIA-GATE at its entry point, separate from the Phase 5 gate. The Phase 6 gate confirms that at least one DEFEATED or PARTIAL verdict exists before proposals are generated.

- **Full (2):** Named INERTIA-GATE at Phase 6 entry; gate tests for at least one non-HOLDS verdict; halt instruction present for gate failure.
- **Partial (1):** Gate present but unnamed; or gate condition does not test verdict content (tests only proposal count or similar proxy).
- **Fail (0):** No gate at Phase 6 entry.

---

### C-22 — Phase annotations distinguish bias type per phase
**Category:** safety

Each phase carries an annotation identifying the type of bias that phase's structure prevents. Annotations are phase-specific (not generic); they name the bias type and explain which structural element of the phase addresses it.

- **Full (2):** Every phase has a bias annotation; each annotation names a specific bias type and the structural element that addresses it; annotations are not copied from phase to phase.
- **Partial (1):** Most phases annotated; a few phases share identical annotation text; or annotations name bias type without identifying the structural element.
- **Fail (0):** No per-phase bias annotations; or a single generic annotation applied to all phases.

---

### C-23 — Verdict Vocabulary carries evidential criteria per tier
**Category:** depth

The Verdict Vocabulary (C-12) includes evidential criteria for each confidence tier (C-07). Each tier definition states the specific evidence type or count required — not merely a descriptive label.

- **Full (2):** All confidence tiers defined with evidential criteria in the Verdict Vocabulary block; criteria are specific (counts, artifact types) not descriptive (e.g., "strong" or "weak").
- **Partial (1):** Tiers defined in Verdict Vocabulary but evidential criteria are descriptive rather than specific; or one tier lacks evidential criteria.
- **Fail (0):** Confidence tiers and Verdict Vocabulary defined in separate sections with no cross-reference; or evidential criteria absent from all tiers.

---

### C-24 — SECTION SCOPE spatial separation
**Category:** correctness

Each major phase section carries a SECTION SCOPE declaration that lists all content types produced within that section. No content type produced within a section is absent from that section's declared scope. A C-24 auditor can verify scope completeness without reading phase content.

- **Full (2):** SECTION SCOPE present in all phases producing structured output; each scope declaration enumerates all content types produced; no content type is produced without appearing in the scope.
- **Partial (1):** SECTION SCOPE present in most phases; one phase produces content not named in its scope; or scope declarations are present but not co-located with phase headers.
- **Fail (0):** SECTION SCOPE absent from two or more phases; or content types consistently produced outside their declared scope.

---

### C-25 — Restart path preserves locked signal set
**Category:** correctness

The RESTART path (C-03) explicitly preserves the SIGNAL READ-LOCK (C-05) from the prior run. A restart does not re-scan signals; it resumes from the locked signal set recorded in the existing output file.

- **Full (2):** RESTART path states that signal scanning is skipped; locked signal set is read from the existing output file; Phase 2 is bypassed on restart.
- **Partial (1):** RESTART path present but does not explicitly state whether Phase 2 is re-run; or locked signal set is re-read but lock mechanism is not referenced.
- **Fail (0):** RESTART path re-runs Phase 2; or RESTART path does not address signal set handling.

---

### C-26 — Proposal independence assertion
**Category:** depth

Each proposal in Phase 6 carries an independence assertion: a statement that the proposal addresses a defeat dimension not covered by any other proposal in the current table. Duplicate coverage is explicitly prohibited.

- **Full (2):** Independence assertion required per proposal; prohibition on duplicate coverage stated at Phase 6 entry; a run that generates two proposals targeting the same defeat dimension fails.
- **Partial (1):** Independence assertion present but not enforced as a gate; or prohibition stated only for full duplicates, not for partial overlap.
- **Fail (0):** No independence assertion; multiple proposals may address the same dimension without restriction.

---

### C-27 — WRITE GUARD at Phase 7 and Phase 8
**Category:** safety

Phase 7 and Phase 8 each carry a WRITE GUARD: an explicit statement that file writes occur only within that phase and only for the artifact type declared in the phase header. Writes outside the declared artifact type are prohibited.

- **Full (2):** Named WRITE GUARD present in both Phase 7 and Phase 8; each guard specifies the permitted artifact type; prohibition on writes outside the artifact type is stated.
- **Partial (1):** WRITE GUARD present in one phase but not the other; or guard present in both but artifact type not specified.
- **Fail (0):** No WRITE GUARD in either phase; or writes are permitted in phases outside Phase 7 and Phase 8.

---

### C-28 — Defeat assessment independence at two sites
**Category:** correctness

Defeat assessments in Phase 5 are produced independently at two sites: once during the assessment pass (verdicts assigned without consulting proposals) and once at Phase 6 entry (verdicts confirmed before proposals open). The two-site pattern prevents assessment from being influenced by anticipated proposals.

- **Full (2):** Two-site INERTIA-GATE enforcement pattern present; first site in Phase 5 assessment pass; second site at Phase 6 entry; both sites reference the same locked verdict set.
- **Partial (1):** Two-site pattern present but sites reference different verdict sets; or second site is a summary rather than an independent confirmation.
- **Fail (0):** Single-site defeat assessment; no confirmation at Phase 6 entry.

---

### C-29 — Consequence field naming identity across all sites
**Category:** correctness

The consequence field name is identical at every site where it appears: Phase 5 table column header, Phase 6a column header, Phase 6b column header, and Phase 5 exit criterion. Naming drift across sites (e.g., "Consequence" vs "Consequence if unchanged") is a failure condition.

- **Full (2):** Consequence field name identical at all four sites; no variation in capitalization, spacing, or phrasing across the four appearances.
- **Partial (1):** Name consistent at three of four sites; one site uses a variant phrasing.
- **Fail (0):** Name varies across two or more sites; or fewer than four sites present.

---

### C-30 — Bias column present in Phase 6 schema
**Category:** correctness

The Phase 6 proposal table schema includes a "Bias blocked by guard" column. The column is named in the schema declaration before Phase 6a populates the table. Column absence is a schema violation, not a data gap.

- **Full (2):** "Bias blocked by guard" column present in Phase 6a and Phase 6b schema declarations; column appears in every proposal row; absence is treated as a schema violation.
- **Partial (1):** Column present in Phase 6a but not Phase 6b; or column named in schema but absent from one or more proposal rows.
- **Fail (0):** "Bias blocked by guard" column absent from Phase 6 schema; or column present only as a comment rather than a schema field.

---

### C-31 — PROPOSAL BIAS AUDIT guard at Phase 6 entry
**Category:** safety

A named enforcement point at Phase 6 entry. The guard text distinguishes per-row bias labeling (prevents motivated reasoning at the individual proposal decision surface) from phase-level annotations (prevents systemic phase structure bias) and explains why both are required — not merely asserts presence. C-30 tests whether the column is in the table schema; C-31 tests whether Phase 6 entry carries a named guard with the structural rationale.

- **Full (2):** Named guard at Phase 6 entry, co-located with INERTIA-GATE label; guard text distinguishes the two labeling levels and explains the distinct failure mode each addresses.
- **Partial (1):** Guard present but lacks the explanatory distinction; or guard is in a preamble section rather than at phase entry.
- **Fail (0):** No named guard at Phase 6 entry.

---

### C-32 — Phase 6 SECTION SCOPE includes row-level bias labeling
**Category:** correctness

The Phase 6 SECTION SCOPE declaration explicitly adds "row-level bias labeling" to its scope text. Without this update, a C-24 auditor checking Phase 6's declared scope would find the C-31 guard operating on content not named in that scope — a spatial separation violation introduced by adding C-31. C-24 tests the three pre-existing mechanisms; C-32 tests whether Phase 6's scope declaration is updated to preserve C-24 after C-31 is added.

- **Full (2):** SECTION SCOPE text reads (e.g.) "gate-exclusion text, proposal generation, and row-level bias labeling"; co-located with Phase 6 INERTIA-GATE.
- **Partial (1):** SECTION SCOPE present but not updated; or row-level bias labeling mentioned in Phase 6 preamble but not in the scope declaration.
- **Fail (0):** No SECTION SCOPE declaration, or SECTION SCOPE unchanged from pre-C-31 form.

---

### C-33 — Output Schema CONTRACT pre-commits consequence field name and bias column
**Category:** correctness

An OUTPUT SCHEMA CONTRACT block before any file read pre-commits both (a) the exact consequence field name at all three C-29 table-column sites and (b) "Bias blocked by guard" as a required Phase 6 column. Makes C-29 naming drift and C-30 column absence detectable from the schema block alone. V-05's CONTRACT A + CONTRACT B is the reference. C-29 tests naming identity at runtime; C-33 tests pre-execution commitment. C-30 tests column presence in the table; C-33 tests contractual declaration before any file is read.

- **Full (2):** CONTRACT block before any file read; pre-commits both consequence field name (naming all three table-column sites) and "Bias blocked by guard" column; both failures detectable from the block alone.
- **Partial (1):** Contract block present but pre-commits only one of the two elements; or block is positioned after a file read instruction.
- **Fail (0):** No schema CONTRACT block; or CONTRACT appears after Phase 1 begins.

---

### C-34 — PROPOSAL BIAS AUDIT failure mode label precision
**Category:** safety

The PROPOSAL BIAS AUDIT guard names each of the two failure modes with a formal descriptive title (e.g., LEVEL 1: SYSTEMIC PHASE STRUCTURE BIAS, LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE), making each failure mode referenceable by name from other document sections. C-31 tests whether the guard distinguishes and explains the two failure modes; C-34 tests whether each failure mode carries a formal title that enables cross-referencing — turning explanatory prose into a named reference artifact that the CONTRACT or SECTION SCOPE can cite by label.

- **Full (2):** Both failure modes carry formal descriptive titles co-located in the PROPOSAL BIAS AUDIT guard text; titles are specific enough to be cited from the CONTRACT or SECTION SCOPE by name alone.
- **Partial (1):** One failure mode named with a formal title; the other described without one; or formal titles present but located outside the guard body (e.g., in a preamble annotation only).
- **Fail (0):** Neither failure mode carries a formal named title; guard text describes but does not formally label the two failure modes.

---

### C-35 — SECTION SCOPE auditor navigation note
**Category:** correctness

The Phase 6 SECTION SCOPE declaration includes an explicit auditor navigation note: a sentence confirming that a C-24 auditor checking Phase 6's declared scope can locate the row-level bias labeling entry from the scope declaration without traversing phase content. C-32 tests whether the scope is updated to include row-level bias labeling; C-35 tests whether that update is designed to serve auditor navigation — i.e., whether the scope declaration itself tells the auditor where to look and what to look for, rather than merely asserting the labeling's presence.

- **Full (2):** SECTION SCOPE includes an explicit navigation note stating that a C-24 auditor verifying row-level bias labeling finds it enumerated in the scope declaration; note identifies the enumeration item by number or label.
- **Partial (1):** SECTION SCOPE references C-24 or auditor navigation in passing (e.g., a parenthetical) but does not provide a full navigation note; or the navigation note appears in a preamble outside the SECTION SCOPE declaration itself.
- **Fail (0):** No auditor navigation note in the SECTION SCOPE declaration; or SECTION SCOPE fails C-32.

---

### C-36 — CONTRACT at absolute document-first position
**Category:** correctness

The OUTPUT SCHEMA CONTRACT is the absolute first section of the document — positioned before the INERTIA COMPETITOR DECLARATION — and satisfies three additional requirements beyond C-33: (a) a self-referential confirmation statement (e.g., "No file read instruction appears before this CONTRACT"), (b) CONTRACT A names all four consequence field sites: the Phase 5 table column, Phase 6a column, Phase 6b column, and Phase 5 exit criterion, and (c) CONTRACT B names "Bias blocked by guard" with violation-detection language enabling a scorer to detect column absence from the CONTRACT block alone without reading any phase content. C-33 tests standalone pre-Phase-1 positioning; C-36 tests whether the CONTRACT is the absolute first reader-encountered content — before all guards including INERTIA COMPETITOR DECLARATION — and whether it is fully self-sufficient for violation detection.

- **Full (2):** CONTRACT is the first section in the document, preceding INERTIA COMPETITOR DECLARATION; self-referential confirmation statement present; CONTRACT A names all four consequence field sites; CONTRACT B includes violation-detection language.
- **Partial (1):** CONTRACT precedes INERTIA COMPETITOR DECLARATION but is missing exactly one of the three additional requirements (self-referential statement, four-site CONTRACT A, or violation-detection language in CONTRACT B).
- **Fail (0):** CONTRACT does not precede INERTIA COMPETITOR DECLARATION; or C-33 fails.

---

**Orthogonality:** C-34 tests naming precision in the guard (extends C-31). C-35 tests auditor navigation in the scope declaration (extends C-32). C-36 tests absolute document anchoring and self-sufficiency of the CONTRACT (extends C-33). All three are independent of each other: C-34 FAIL / C-35 PASS / C-36 PASS is achievable (scope and contract correctly positioned; guard labels remain informal). C-31 FAIL implies C-34 FAIL; C-32 FAIL implies C-35 FAIL; C-33 FAIL implies C-36 FAIL — but the converse does not hold.

**R14 score ceiling under v15:** V-01, V-02, and V-03 (each 46/50 = 9.20 under v14) score 48/56 = 8.57 under v15, each picking up 2 points on their single new target criterion (C-34, C-35, and C-36 respectively). An R15 variate targeting all six new criteria (C-31 through C-36) achieves 44 (C-09–C-30) + 12 (C-31–C-36) = 56/56 = 10.00.
