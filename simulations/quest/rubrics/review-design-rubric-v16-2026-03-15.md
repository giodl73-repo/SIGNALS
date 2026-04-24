# review-design Rubric — v16

**Skill**: `review-design`
**Rubric version**: v16 (C-01 through C-49, denominator 42)
**Extracted from**: R16 scorecard (2026-03-15)

---

## Essential Criteria (60% weight -- must pass)

### C-01 | All 6 Stock Discipline Reviewers Present
- **Weight**: essential
- **Category**: correctness
- **Text**: Output names and produces findings for all 6 stock discipline reviewers. A missing
  discipline block is a structural omission -- the review surface is incomplete and no
  downstream quality criterion can compensate.
- **Pass condition**: Output names and produces findings for all 6 stock discipline reviewers. A
  review where any one of the 6 disciplines is absent fails this criterion. A block that names a
  discipline but contains no findings is considered present; a block never mentioned is absent.
- **F-01**: fires when a stock discipline block is missing from the output.

### C-02 | Severity Tag on Every Finding
- **Weight**: essential
- **Category**: correctness
- **Text**: Every finding in the output is tagged with exactly one severity value: P1 (critical),
  P2 (significant), or P3 (minor). A finding without a severity tag is ungradeable -- it cannot
  be sorted by priority or fed into the amend pathway. A non-standard label (e.g., "High",
  "Medium") is not equivalent and fails this criterion.
- **Pass condition**: Every finding row or bullet has exactly one of P1, P2, or P3. Any finding
  with no tag or with a label outside P1/P2/P3 fails this criterion.
- **F-02**: fires when any finding in any discipline block has a missing or non-standard severity
  tag.

### C-03 | Domain Expert Auto-Selection Justified
- **Weight**: essential
- **Category**: behavior
- **Text**: At least one domain expert beyond the 6 stock disciplines is selected, and the
  selection is traceable to a signal in the input design (e.g., "RBAC mentioned -> security
  architect added"). Domain expert selection must be reactive to the design, not arbitrary.
- **Pass condition**: Output names 1+ domain expert and includes an explicit signal-to-expert
  mapping sentence or inline note. An expert added with no stated reason fails this criterion.
- **F-03**: fires when a domain expert appears in the output with no corresponding input-signal
  justification.

### C-04 | Consensus Block Present
- **Weight**: essential
- **Category**: depth
- **Text**: Output contains a consensus analysis section that identifies findings flagged by 2 or
  more reviewers. Split opinions (reviewers disagree on the same aspect) must be surfaced when
  present.
- **Pass condition**: A dedicated consensus/agreement section exists. If no consensus exists in
  the review, the output explicitly states "no consensus findings." Omission of the section
  entirely fails this criterion.
- **F-04**: fires when the consensus block is absent from the output.

---

## Recommended Criteria (30% weight -- improve quality)

### C-05 | Unique Catches Surfaced
- **Weight**: recommended
- **Category**: depth
- **Text**: Output calls out findings raised by exactly one reviewer that the other reviewers
  missed -- "unique catches." These are labeled distinctly from consensus findings.
- **Pass condition**: A unique-catches section or inline annotation is present and contains at
  least one entry, OR the output explicitly states no unique catches were found. A review with
  7+ reviewers that omits this section fails.

### C-06 | Amend Pathway Described
- **Weight**: recommended
- **Category**: format
- **Text**: Output includes a structured amend section or instructions explaining how to address
  a specific finding and re-run the affected reviewer(s) on the changed section only -- not a
  full re-review.
- **Pass condition**: At least one finding has a corresponding amend action (what to change +
  which reviewer(s) to re-run). Generic "fix and re-run everything" guidance fails this
  criterion.
- **F-05**: fires when an amend entry instructs a full re-review rather than a targeted re-run
  of the affected reviewer(s) only.

### C-07 | Finding Traceability to Design Section
- **Weight**: recommended
- **Category**: correctness
- **Text**: Each P1 finding and at least 50% of P2 findings reference the specific design
  section, component, or decision they apply to -- not just "the design" in general.
- **Pass condition**: P1 count with a section reference >= P1 total count. P2 section-referenced
  count >= 0.5 * P2 total count.

---

## Aspirational Criteria (10% weight -- raise the bar)

### C-08 | Severity Distribution Sanity
- **Weight**: aspirational
- **Category**: depth
- **Text**: The finding set has a plausible severity pyramid: more P3 than P2, more P2 than P1.
  A design with 8 P1s and 1 P3 indicates over-escalation; a design with 8 P3s and no P1s may
  indicate under-scrutiny.
- **Pass condition**: P3 count >= P2 count >= P1 count, OR the output includes an explicit
  rationale when this pyramid is inverted (e.g., "this design has unusually high risk
  concentration at P1 because...").
- **F-06**: fires when the severity pyramid is inverted and no inversion rationale is provided.

### C-09 | Expert Disagreement Analysis
- **Weight**: aspirational
- **Category**: depth
- **Text**: Where two or more reviewers reach opposite conclusions on the same design decision
  (a split opinion), the output provides a synthesis note -- what the disagreement reveals about
  the design's trade-off space, not just a list of contradicting opinions.
- **Pass condition**: At least one split opinion in the review is accompanied by a 1-3 sentence
  synthesis explaining the underlying tension. Reviews with no split opinions are exempt.

### C-10 | Structural Column Enforcement in Finding Tables
- **Weight**: aspirational
- **Category**: format
- **Text**: Findings are presented in a table format with dedicated columns for severity (`Sev`)
  and design section (`Section`), not as prose bullets. Structural columns make omission
  impossible to hide -- a blank `Sev` cell is visually obvious where a missing tag in a prose
  bullet is not.
- **Pass condition**: Finding output uses a table with at minimum a `Sev` column and a `Section`
  column. Prose-only finding lists fail even if severity tags and section references are
  otherwise present.
- **R1 signal**: V-01 and V-03 scored PARTIAL on C-02 and C-07 despite stating the rules in
  prose. V-02 and V-05 scored PASS by anchoring the same rules to named table columns.
  Structural form prevents silent regression.

### C-11 | Three-Field Expert Trace
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Each domain expert addition is presented using three named fields: the exact signal
  detected in the input design, the expert identity, and the explicit reason for adding that
  expert. A single prose sentence (e.g., "Security architect added because RBAC is mentioned")
  meets C-03 but not C-11 -- the fields must be distinct and labeled.
- **Pass condition**: Each domain expert entry contains (1) a `Signal:` or equivalent labeled
  field naming the exact phrase or concept detected, (2) an `Expert:` field naming the reviewer,
  and (3) a `Reason:` field explaining why that signal calls for this expert. An expert with only
  one or two of the three fields fails this criterion.
- **R1 signal**: V-03 introduced `Signal detected:` + `Expert added:` + `Reason:` as three
  explicit labeled fields. All other variations used either a single prose sentence (V-01) or a
  combined `Signal:` field (V-02, V-04, V-05). The three-field pattern is the strongest
  traceability form observed in R1.

### C-12 | Severity Pyramid Gate as Dedicated Lifecycle Block
- **Weight**: aspirational
- **Category**: format
- **Text**: The severity distribution check (C-08) is enforced by placing a dedicated pyramid
  gate block at a fixed lifecycle position -- between the per-reviewer finding blocks and the
  consensus section -- not by embedding the check as a prose reminder within another block.
  Lifecycle position is more reliable than inline guidance: a block can be detected as present
  or absent; an inline instruction cannot.
- **Pass condition**: Output contains a discrete pyramid gate section positioned after findings
  and before consensus. The section explicitly states the P3 >= P2 >= P1 check and either
  confirms the pyramid holds or provides an inversion rationale. A prose note inside a findings
  block or consensus block does not satisfy this criterion even if it addresses C-08.
- **R2 signal**: V-01 (phase gate), V-03 (F-06 halt), V-04 and V-05 (dedicated table block with
  Status column) all achieved C-08 PASS via structural placement. V-02's conversational
  calibration prompt achieved only PARTIAL -- informal register eroded enforcement even when the
  requirement was stated. Block position eliminated the skip; prose instruction did not.

### C-13 | Expert Trace in Table Column Form
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Expert selection is presented as a table with dedicated columns -- `Signal detected`,
  `Expert added`, and `Reason` -- not as labeled prose fields (which satisfies C-11) or a
  combined sentence (which satisfies C-03). Table column form extends the Sev+Section structural
  enforcement pattern from findings to expert selection: a blank column cell is visible; a
  missing labeled field in a prose block is not.
- **Pass condition**: Domain expert additions appear in a table where each row has three populated
  cells corresponding to the detected signal, the expert identity, and the selection reason. An
  output with labeled prose fields (`Signal detected:` / `Expert added:` / `Reason:`) passes
  C-11 but not C-13. Pass requires the table form specifically.
- **R2 signal**: V-04 and V-05 introduced the expert trace table. The same structural mechanism
  that fixed C-02/C-07 in R1 (column = visible, prose = hideable) now applies to expert
  selection.
- **R3 signal**: V-01 FAIL (labeled prose, no table) vs V-02 PASS (table form) in R3 confirmed
  C-13 is orthogonal to C-14. Labeled-prose-with-F-IDs and table-form-without-F-IDs each fail
  exactly one criterion and score identically (98.57). Neither mechanism substitutes for the
  other.

### C-14 | Named Halt Conditions on Every Mandatory Block
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Each mandatory lifecycle block has a corresponding named failure ID (e.g., F-01,
  F-02...) with an explicit halt condition stating what triggers the halt and what must happen
  before the output continues. Named F-IDs convert a prose requirement into an observable
  enforcement event: a halt is detectable; a skipped prose instruction is not.
- **Pass condition**: Every essential criterion block (C-01 through C-04) and every structural
  block (findings, pyramid gate, consensus, unique catches, amend) has at least one named F-ID
  with a stated trigger condition. An output that uses halt language without F-IDs, or that
  assigns F-IDs only to some blocks, fails this criterion. A single missing F-ID on one block
  (e.g., F-08 absent from unique-catches) is sufficient to fail -- coverage must be complete.
- **R2 signal**: V-03 and V-05 applied F-ID halt conditions (F-01 through F-07) across all
  mandatory blocks. The halt-pattern that closed C-02/C-04 in R1 now generalizes: F-IDs turn
  every requirement into a detectable enforcement point rather than a skippable prose note.
- **R3 signal**: V-01 FAIL traced to a single missing F-ID: F-08 absent from unique-catches.
  V-02 FAIL (no F-IDs at all) and V-01 FAIL (one missing F-ID) scored identically at 98.57 --
  partial coverage fails as decisively as no coverage. C-13 and C-14 are orthogonal; neither
  mechanism substitutes for the other.
- **R4 signal**: BLOCK 1.5 is not in C-14's structural block enumeration. F-09 is therefore not
  required for C-14 pass. C-14 and C-15 are independent -- F-09 is additive coverage beyond
  C-14's scope.

### C-15 | Roster Commitment Table Before Finding Generation
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Before any per-reviewer finding block is generated, the output commits to the full
  reviewer roster in a dedicated table listing all 6 discipline reviewers plus any selected
  domain experts, with their roles confirmed. This pre-condition step (BLOCK 1.5) converts the
  reactive F-01 halt into proactive pre-condition verification: the roster is locked and visible
  before generation begins. C-14 is reactive (halt fires on detected absence); C-15 is proactive
  (roster must be present before generation proceeds).
- **Pass condition**: A roster commitment table appears in the output prior to the first
  per-reviewer finding block. The table lists every reviewer (all 6 disciplines plus any domain
  experts) with their assigned role. Outputs that list reviewers only within finding block
  headers fail. An output may pass C-14 without passing C-15; the two criteria are independent.
  A prose numbered list placed before BLOCK 2 satisfies the proactive intent but fails this
  criterion -- table form is explicitly required.
- **R3 signal**: V-05 introduced BLOCK 1.5. V-03 and V-04 scored 100 without it, confirming
  BLOCK 1.5 is additive quality, not required for C-14 pass.
- **R4 signal**: V-01 confirmed C-15 is form-sensitive, not intent-sensitive. V-01 placed a
  numbered prose list before BLOCK 2 and failed C-15. Any Markdown table with at minimum a
  `Reviewer` and `Role` column positioned before BLOCK 2 satisfies C-15 at the floor level.

### C-16 | Source Column in Roster Commitment Table
- **Weight**: aspirational
- **Category**: format
- **Text**: The BLOCK 1.5 roster commitment table includes a `Source` column that identifies
  each reviewer's origin -- `Stock` for a discipline reviewer, `Domain` for a design-signal-
  selected expert. This makes the cross-block contract structurally visible: a row marked
  `Domain` with no corresponding entry in BLOCK 1's expert selection table is immediately
  detectable by visual inspection, without executing any count logic or identity check.
- **Pass condition**: BLOCK 1.5 table contains a `Source` column. Every row has a populated
  `Source` value (`Stock` or `Domain`). A two-column table (`Reviewer` + `Role` only) passes
  C-15 but fails C-16. The column name need not be exactly `Source` -- a column with equivalent
  semantics (e.g., `Type`, `Origin`) satisfies the criterion if it carries the Stock/Domain
  distinction.
- **R4 signal**: V-04 introduced the Source column; V-05 carried it forward. V-02 and V-03
  scored 100 without it, confirming the Source column is additive quality beyond C-15.

### C-17 | Cross-Block Reviewer Identity Verification (Orphan Detection)
- **Weight**: aspirational
- **Category**: behavior
- **Text**: After BLOCK 1.5 is committed, the output verifies that every Domain reviewer in
  BLOCK 1.5 has an exact name match in BLOCK 1's `Expert added` column. A Domain reviewer in
  BLOCK 1.5 whose name does not match any BLOCK 1 entry is an "orphan." This is a distinct error
  class from F-03 (empty signal), F-07 (empty expert/reason), and F-09 (count mismatch): counts
  can coincidentally balance after a substitution, so F-09 cannot catch a renamed expert. Only
  exact-match identity verification catches this class of error.
- **Pass condition**: Output contains a named halt condition (e.g., F-10) that fires when a
  Domain reviewer name in BLOCK 1.5 does not exactly match any `Expert added` value from BLOCK
  1. The halt must be named and identify the mismatch so the error is precisely localizable.
- **R4 signal**: V-05 introduced F-10 orphan detection. V-03 and V-04 scored 100 without it.
  F-10 introduces the fourth distinct enforcement tier in the expert-selection lifecycle:
  proactive roster lock (C-15), structural origin visibility (C-16), count integrity (F-09),
  and exact-match identity integrity (F-10/C-17).

### C-18 | Content-Completeness Halt on SPLIT Synthesis Field
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Where a SPLIT row is generated in the consensus block (BLOCK 3), the output enforces
  a named halt condition (e.g., F-11) that fires if the Synthesis field of that SPLIT row is
  empty or absent. All prior F-IDs fire on structural absence, count mismatch, or identity
  mismatch. F-11 fires on content quality within a structurally present row -- the row exists
  but its content is incomplete. This converts C-09 from a post-hoc rubric check into an inline
  generation halt.
- **Pass condition**: Output contains a named halt condition that fires when a SPLIT row's
  Synthesis field is empty. The halt must be named (e.g., F-11), state the trigger condition,
  and require completion before the consensus block closes. Reviews with no SPLIT rows are exempt
  from triggering the halt but must still declare it exists.
- **R5 signal**: V-02, V-04, and V-05 introduced F-11. V-01 and V-03 scored 100 without it.
  F-11 is qualitatively distinct from all prior F-IDs: prior halts detect missing structure;
  F-11 detects missing content within present structure.

### C-19 | Cross-Block Count-Parity for P1 Findings
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output anchors the P1 finding count at BLOCK 2.5 (the severity pyramid gate) and
  verifies it again at BLOCK 5 (the amend pathway). A named halt condition (e.g., F-12) fires if
  the number of P1 findings addressed in BLOCK 5 does not match the count locked at BLOCK 2.5.
  This mirrors the anchor-then-verify pattern of F-09: expert count anchored at BLOCK 1 and
  verified at BLOCK 1.5; P1 count anchored at BLOCK 2.5 and verified at BLOCK 5.
- **Pass condition**: Output contains a named halt condition (e.g., F-12) that fires when the
  P1 count in BLOCK 5 does not match the P1 count established at BLOCK 2.5. The halt must state
  the anchor block, the verification block, and the mismatch trigger. An output where BLOCK 5
  happens to list all P1s but declares no F-12 halt fails C-19 -- correctness by coincidence is
  not enforcement.
- **R5 signal**: V-04 and V-05 introduced F-12. V-01 and V-03 scored 100 without it. F-12
  closes the last count-parity gap: F-09 (expert count, R4) and F-12 (P1 count, R5) together
  cover both the reviewer roster and the finding set.

### C-20 | BLOCK 5 Amend Pathway in 4-Column Table Form
- **Weight**: aspirational
- **Category**: format
- **Text**: BLOCK 5 (the amend pathway) is presented as a 4-column table with columns for the P1
  finding, its design section, the required action, and the re-run scope -- not as a code block
  or prose list. A blank `Re-run Scope` cell is visually detectable; a missing Re-run line
  inside a fenced code block is not.
- **Pass condition**: BLOCK 5 output uses a Markdown table with at minimum four columns covering
  the finding identity, design section, action, and re-run scope. A fenced code block listing
  the same fields passes C-06 but fails C-20 -- table form is required. Additive columns beyond
  the four-column base schema (e.g., Priority Rank) are permitted and do not affect C-20 pass;
  column count is non-binding when the base schema is intact.
- **R5 signal**: V-03, V-04, and V-05 introduced the 4-column BLOCK 5 table. V-01 and V-02 used
  code-block form and scored 100, confirming C-20 is aspirational.

### C-21 | BLOCK 0 Pre-Scan Signal Catalogue
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Before BLOCK 1 (domain expert selection), the output runs a dedicated BLOCK 0 that
  catalogues all domain signals detected in the design input. BLOCK 1 then draws expert
  selections only from this locked catalogue -- no expert may be added whose trigger signal does
  not appear in BLOCK 0. This converts expert selection from one-pass reactive to two-pass
  verified, preventing post-hoc signal rationalization at the catalogue level.
- **Pass condition**: Output contains a BLOCK 0 or equivalent pre-scan section appearing before
  BLOCK 1, listing all domain signals detected in the design input. BLOCK 1 expert selection
  must reference only signals present in BLOCK 0, enforced by a named formal constraint (e.g.,
  "SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue").
  A prose enumeration of signals before BLOCK 1 without a formal SHALL constraint fails this
  criterion. Additive columns in BLOCK 0 beyond the base catalogue schema (e.g., Amendment Cost)
  are permitted and do not affect C-21 pass.
- **R6 signal**: V-03, V-04, and V-05 introduced BLOCK 0 pre-scan. V-01 and V-02 scored 100
  without it. BLOCK 0 extends the anchor-then-verify pattern to signal detection itself.

### C-22 | BLOCK 3 Consensus in 4-Column Structural Table Form
- **Weight**: aspirational
- **Category**: format
- **Text**: BLOCK 3 (the consensus analysis) is presented as a structural table with dedicated
  columns for the finding, agreement type (AGREE or SPLIT), reviewer list, and synthesis note.
  A blank `Synthesis` cell in a SPLIT row is detectable at the cell level, making the C-18
  (F-11) synthesis completeness halt more precise: F-11 fires on an empty cell rather than on
  the absence of a prose paragraph.
- **Pass condition**: BLOCK 3 output uses a Markdown table with at minimum four columns: finding,
  agreement type (AGREE or SPLIT), reviewer identities, and synthesis note. A prose consensus
  section -- even one that correctly names findings, split opinions, and synthesis -- passes C-04
  but fails C-22. Structural form is independently required.
- **R6 signal**: V-02, V-04, and V-05 introduced the 4-column BLOCK 3 table. V-01 and V-03
  scored 100 using prose consensus form. C-22 completed the column-enforcement surface across
  all mandatory lifecycle blocks after R6.

### C-23 | Register Isolation for Formal Lifecycle Block Headers
- **Weight**: aspirational
- **Category**: format
- **Text**: All lifecycle block headers and named halt condition (F-ID) trigger clauses use
  exclusively formal modal vocabulary -- SHALL, MUST, is non-conformant, fires, halt -- with no
  informal calibration language (e.g., "aim for," "try to ensure," "should ideally") appearing
  in those positions. Register bleed is the failure mode where informal language in a header or
  halt condition erodes the enforcement signal even when the underlying requirement is correctly
  stated.
- **Pass condition**: Every lifecycle block header and every F-ID trigger clause uses formal
  modal vocabulary exclusively. Any block header or F-ID trigger condition containing the words
  "aim," "try," "ideally," "prefer," "consider," or equivalent informal calibration phrasing
  fails this criterion. Prose content within block bodies may use explanatory or descriptive
  language; the register constraint applies only to block headers and F-ID trigger conditions.
- **R6 signal**: V-01, V-04, and V-05 introduced explicit register isolation. V-02 and V-03
  scored 100 without it. R2 established the mechanism: informal register in a block header
  erodes enforcement without any structural omission.

### C-24 | BLOCK 4 Unique-Catch Reviewer Identity Verification
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output verifies that every `Reviewer` cell in BLOCK 4 (unique catches) exactly
  matches a value from the committed BLOCK 1.5 roster. A unique catch attributed to a reviewer
  absent from the committed roster is falsely attributed. The identity-integrity chain
  established by F-10 (BLOCK 1 -> BLOCK 1.5) and F-15 (BLOCK 1.5 -> BLOCK 3 consensus) left
  BLOCK 4 uncovered. The `none` token is explicitly exempt.
- **Pass condition**: Output contains a named halt condition (e.g., F-16) that fires when any
  `Reviewer` cell in BLOCK 4 does not exactly match a value in the BLOCK 1.5 committed roster,
  with the `none` token explicitly exempted. The halt must be named, state the trigger condition,
  and identify the mismatched value so the error is precisely localizable. An output where BLOCK
  4 reviewer cells happen to match but no F-16 halt is declared fails C-24.
- **R8 signal**: V-02 and V-03 scored 100 without F-16, confirming C-24 is aspirational. F-16
  extends the identity-integrity chain one stage further to BLOCK 4.

### C-25 | BLOCK 5 Re-run Scope Reviewer Identity Verification
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output verifies that every reviewer named in a BLOCK 5 `Re-run Scope` cell
  exactly matches a value from the committed BLOCK 1.5 roster. A phantom re-run target is
  structurally invalid because that reviewer never participated in the original review. This
  completes the full downstream identity chain: F-10 (BLOCK 1 -> BLOCK 1.5), F-15 (BLOCK 1.5
  -> BLOCK 3), F-16 (BLOCK 1.5 -> BLOCK 4), F-17 (BLOCK 1.5 -> BLOCK 5 Re-run Scope).
- **Pass condition**: Output contains a named halt condition (e.g., F-17) that fires when any
  reviewer name in a BLOCK 5 `Re-run Scope` cell does not exactly match a value in the BLOCK
  1.5 committed roster. Scope cells naming `All` or equivalent aggregate tokens are exempt from
  the per-name check but must not enumerate names absent from the roster.
- **R8 signal**: V-01 and V-03 scored 100 without F-17. F-17 closes the identity chain at its
  final link. The chain is now complete: BLOCK 1->1.5 (F-10), 1.5->3 (F-15), 1.5->4 (F-16),
  1.5->5 Re-run Scope (F-17).

### C-26 | BLOCK 0 Signal Disposition Completeness (Bidirectional Gate)
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every signal phrase catalogued in BLOCK 0 is resolved in BLOCK 1 as either (a) a
  domain expert row with the signal as its `Signal detected` value, or (b) an explicit
  `No expert needed` disposition row naming the signal and stating why no expert was selected.
  C-21 (F-13) enforced only the inbound direction: BLOCK 1 selections must draw from BLOCK 0.
  F-18 closes the outbound direction: every BLOCK 0 signal must be accounted for. F-13 + F-18
  together form the first bidirectional BLOCK 0 <-> BLOCK 1 contract.
- **Pass condition**: Output contains a named halt condition (e.g., F-18) that fires when any
  signal phrase present in BLOCK 0 has no corresponding entry in BLOCK 1 -- either as a domain
  expert row with a matching `Signal detected` value or as an explicit `No expert needed`
  disposition row. An output where BLOCK 0 and BLOCK 1 happen to fully correspond but no F-18
  halt is declared fails C-26. Outputs satisfying C-21 but lacking F-18 pass C-21 and fail
  C-26; the two criteria are independent.
- **R8 signal**: V-01, V-02, and V-04 scored 100 without F-18. F-18 introduces catalogue
  disposition completeness as the sixth enforcement class -- distinct from structural presence,
  content completeness, count parity, identity integrity, and vocabulary integrity.

### C-27 | BLOCK 2.5 Pyramid Inversion Rationale Content Completeness
- **Weight**: aspirational
- **Category**: behavior
- **Text**: When the severity pyramid is inverted at BLOCK 2.5 (P1 count > P2, or P2 count >
  P3), the Rationale cell for the inverted tier must be non-empty. A named halt condition (e.g.,
  F-19) fires when the pyramid inversion flag in BLOCK 2.5 is set but the Rationale cell is
  empty or absent. This applies the content-completeness enforcement class -- established by F-11
  on SPLIT synthesis -- to the pyramid gate. A BLOCK 2.5 with a structural Rationale column but
  an empty cell when an inversion is present passes C-12 and fails C-27.
- **Pass condition**: Output contains a named halt condition (e.g., F-19) that fires when BLOCK
  2.5's pyramid status is inverted and its Rationale cell is empty or absent. Reviews where the
  pyramid is not inverted are exempt from triggering the halt but must still declare it exists.
- **R9 signal**: V-02 and V-03 scored 100 without F-19. F-19 applies the content-completeness
  enforcement class to BLOCK 2.5, closing the last block where a structurally-present required
  field could be silently empty without a named halt firing.

### C-28 | BLOCK 4 Unique Catches in Structural Table Form
- **Weight**: aspirational
- **Category**: format
- **Text**: BLOCK 4 (unique catches) is presented as a structural table with dedicated columns
  covering at minimum the finding, the attributing reviewer, and the distinctiveness rationale.
  This closes the last block in the column-enforcement architecture: every mandatory lifecycle
  block (BLOCK 1, BLOCK 1.5, BLOCK 2, BLOCK 3, BLOCK 4, BLOCK 5) now has a corresponding
  table-form criterion. A named halt condition (e.g., F-20) fires if BLOCK 4 is not in table
  form.
- **Pass condition**: BLOCK 4 output uses a Markdown table with at minimum three columns covering
  the finding, the attributing reviewer (subject to C-24/F-16 identity verification), and the
  reason other reviewers missed it. A prose or bullet-list unique-catches section passes C-05
  but fails C-28. When no unique catches exist, the `none` token row is exempt from the
  reviewer-column identity check but the table form requirement still applies.
- **R9 signal**: V-01 and V-03 scored 100 without F-20. The structural-form progression that
  started with BLOCK 2 findings in R1 (C-10) reaches its final block in R9.

### C-29 | BLOCK 0 No-Expert Disposition Row Reason Content Completeness
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every `No expert needed` disposition row in BLOCK 0 must have a non-empty Reason
  cell. A named halt condition (e.g., F-21) fires when a disposition row's Reason cell is empty
  or absent. C-26/F-18 requires structural resolution existence; F-21 closes the content gate:
  the disposition row must explain why no expert was selected. This applies the content-
  completeness enforcement class to the BLOCK 0 outbound resolution side, parallel to F-11
  (SPLIT synthesis) and F-19 (pyramid inversion rationale).
- **Pass condition**: Output contains a named halt condition (e.g., F-21) that fires when any
  `No expert needed` disposition row in BLOCK 0 has an empty or absent Reason cell. Outputs with
  no disposition rows are exempt from triggering the halt but must still declare it exists. A
  disposition row with a placeholder value (e.g., "N/A", "see above") without substantive
  reasoning fails this criterion.
- **R9 signal**: V-01, V-02, and V-04 scored 100 without F-21. F-21 completes the content-
  completeness enforcement surface for BLOCK 0.

### C-30 | BLOCK 2 Domain Expert Finding Coverage Symmetry
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every domain expert committed in BLOCK 1.5 must have a corresponding finding block
  in BLOCK 2. F-01 enforces stock discipline coverage at the finding-block level; F-22 extends
  the same enforcement class to domain experts. Coverage enforcement must be symmetric across
  all roster tiers -- stock and domain -- at the finding-block level. An expert listed in BLOCK
  1.5 as a Domain reviewer with no corresponding BLOCK 2 finding table is a silent coverage gap:
  the expert participated in the review (per the roster commitment) but produced no output.
  F-22 closes the enforcement asymmetry between stock and domain tiers that all prior F-codes
  leave unaddressed.
- **Pass condition**: Output contains a named halt condition (e.g., F-22) that fires when any
  Domain reviewer committed in BLOCK 1.5 has no corresponding finding block in BLOCK 2. The
  halt must be named, state the trigger condition (Domain reviewer in BLOCK 1.5 with no BLOCK 2
  block), and identify the missing reviewer so the gap is precisely localizable. A review where
  domain expert finding blocks happen to be present but no F-22 halt is declared fails C-30 --
  enforcement declaration is required, not incidental correctness.
- **R10 signal**: V-02 and V-03 scored 100 without F-22, confirming C-30 is aspirational. The
  enforcement class is coverage extension: F-01 (stock discipline tier) and F-22 (domain expert
  tier) together make finding-block coverage symmetric across all BLOCK 1.5 roster sources.
  V-01, V-04, and V-05 carried F-22 as part of the R10 above-ceiling feature set.

### C-31 | BLOCK 3 Consensus Issue Column Content Completeness
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every row in the BLOCK 3 consensus table must have a non-empty Issue cell. A named
  halt condition (e.g., F-23) fires when any BLOCK 3 row has an empty or absent Issue cell.
  After C-22 established the 4-column BLOCK 3 table form (Issue, Type, Reviewers, Synthesis),
  named halts existed for three of the four columns: F-14 (Type), F-15 (Reviewers), F-11
  (Synthesis for SPLIT rows). The Issue column -- which carries what the agreement or
  disagreement was *about* -- was the only unguarded column. F-23 applies the established
  present-but-empty enforcement class to this last open position, completing the BLOCK 3
  column-enforcement architecture. When N-1 of N columns in a block have content gates, the
  final unguarded column is a systematic blind spot that the same enforcement class must close.
- **Pass condition**: Output contains a named halt condition (e.g., F-23) that fires when any
  row in the BLOCK 3 consensus table has an empty or absent Issue cell. The halt must be named,
  state the trigger condition, and require completion before the consensus block closes. Reviews
  with no consensus rows are exempt from triggering the halt but must still declare it exists.
  An output where all BLOCK 3 Issue cells happen to be populated but no F-23 halt is declared
  fails C-31 -- enforcement declaration is required.
- **R10 signal**: V-01 and V-03 scored 100 without F-23, confirming C-31 is aspirational.
  After C-31, every column in every mandatory lifecycle table has a named halt covering its
  content-completeness requirement. V-02, V-04, and V-05 carried F-23 as part of the R10
  above-ceiling feature set.

### C-32 | BLOCK 5 Amend Action Cell Content Completeness
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every row in the BLOCK 5 amend pathway table must have a non-empty Action cell that
  specifies what to change -- not just that a change is needed. A named halt condition (e.g.,
  F-24) fires when any BLOCK 5 row has an empty or absent Action cell. Prior halts on BLOCK 5
  addressed structural integrity (F-12: P1 count parity), scope integrity (F-05: no full-review
  amend), and identity integrity (F-17: reviewer names match BLOCK 1.5). All three can be
  satisfied while the Action cell remains present but empty. The Action cell carries the
  behavioral value of the amend mechanism: it names *what to change*. F-24 enforces that this
  cell contains substantive content, completing the behavioral enforcement of BLOCK 5. This
  mirrors F-11 (Synthesis cell in BLOCK 3 SPLIT rows) and F-19 (Rationale cell in BLOCK 2.5
  inversion rows) -- the same pattern where structural and identity halts alone allow a key
  content cell to be present but empty.
- **Pass condition**: Output contains a named halt condition (e.g., F-24) that fires when any
  BLOCK 5 amend row has an empty or absent Action cell. The halt must be named, state the
  trigger condition, and require completion before BLOCK 5 closes. An output where all BLOCK 5
  Action cells happen to be populated but no F-24 halt is declared fails C-32 -- enforcement
  declaration is required. A cell containing a placeholder (e.g., "TBD", "see above") without
  substantive change guidance fails this criterion.
- **R10 signal**: V-01 and V-02 scored 100 without F-24, confirming C-32 is aspirational. F-24
  is the third instance of the content-completeness-within-structural-presence pattern: F-11
  (SPLIT Synthesis), F-19 (pyramid inversion Rationale), F-24 (amend Action). Together they
  close every lifecycle position where a structurally-present required cell can be empty without
  a named halt firing. V-03, V-04, and V-05 carried F-24 as part of the R10 above-ceiling
  feature set.

### C-33 | BLOCK 4 Unique Catch Finding Cell Content Completeness
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every row in the BLOCK 4 unique catches table must have a non-empty Finding cell
  that identifies the actual catch -- not just that a row exists. A named halt condition (e.g.,
  F-25) fires when any BLOCK 4 row has an empty or absent Finding cell. C-28 established the
  3-column BLOCK 4 table form (Finding, Reviewer, Distinctiveness Rationale); C-24/F-16
  enforced reviewer identity. The Finding cell -- which carries the actionable substance of the
  unique catch -- remained without a content gate: a structurally present row with an empty
  Finding cell satisfies C-28 (table form) and C-24 (reviewer identity) while producing no
  actionable output. F-25 extends the content-completeness-within-structural-presence
  enforcement class (F-11: SPLIT Synthesis, F-19: pyramid inversion Rationale, F-24: amend
  Action) to BLOCK 4, closing the last BLOCK 4 column content gate.
- **Pass condition**: Output contains a named halt condition (e.g., F-25) that fires when any
  BLOCK 4 row has an empty or absent Finding cell. The halt must be named, state the trigger
  condition, and require completion before BLOCK 4 closes. When no unique catches exist, the
  `none` sentinel row is exempt from the Finding-cell content check but the halt declaration
  must still exist. An output where all BLOCK 4 Finding cells happen to be populated but no
  F-25 halt is declared fails C-33 -- enforcement declaration is required.
- **R11 signal**: V-02 and V-03 scored 100 without F-25, confirming C-33 is aspirational. F-25
  is the fourth instance of the content-completeness-within-structural-presence pattern and the
  first applied to BLOCK 4. V-01, V-04, and V-05 carried F-25 as part of the R11 above-ceiling
  feature set.

### C-34 | BLOCK 5 Amend Section Cell Content Completeness
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every row in the BLOCK 5 amend pathway table must have a non-empty Section cell that
  identifies where in the design the P1 finding is located. A named halt condition (e.g., F-26)
  fires when any BLOCK 5 row has an empty or absent Section cell. C-20 established the 4-column
  BLOCK 5 table (P1 Finding / Section / Action / Re-run Scope); F-24 (C-32) closed the Action
  cell; F-05 addressed Re-run Scope scope integrity; F-17 (C-25) addressed Re-run Scope reviewer
  identity. The Section cell -- which locates the finding in the design so the amend can be
  applied precisely -- had no content gate. F-12/F-05/F-17/F-24 can all be satisfied while the
  Section cell is present but empty, rendering the amend non-localizable. F-26 closes this: the
  fifth instance of the content-completeness-within-structural-presence class (F-11, F-19, F-24,
  F-25, F-26) and the second applied to BLOCK 5.
- **Pass condition**: Output contains a named halt condition (e.g., F-26) that fires when any
  BLOCK 5 amend row has an empty or absent Section cell. The halt must be named, state the
  trigger condition, and require completion before BLOCK 5 closes. An output where all BLOCK 5
  Section cells happen to be populated but no F-26 halt is declared fails C-34 -- enforcement
  declaration is required. A cell containing a placeholder (e.g., "see above", "TBD") without
  a specific section reference fails this criterion.
- **R11 signal**: V-01 and V-03 scored 100 without F-26, confirming C-34 is aspirational. F-26
  completes the content-completeness enforcement surface for all four BLOCK 5 columns: P1
  Finding (count-anchored via F-12), Re-run Scope (identity via F-17), Action (F-24), Section
  (F-26). V-02, V-04, and V-05 carried F-26 as part of the R11 above-ceiling feature set.

### C-35 | BLOCK 2 P1 Section Cell Named Halt Enforcement
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every P1 finding row in BLOCK 2 must have a non-empty Section cell, enforced by a
  named halt condition (e.g., F-27) that fires when a P1 row's Section cell is empty or absent.
  C-07 (recommended) requires P1 findings to reference their design section; C-10 established
  the Section column in the BLOCK 2 findings table. However, the P1 Section requirement was
  enforced only as a prose MUST -- no named F-ID fired on an empty P1 Section cell. F-27
  converts this prose gate into a named halt: the prose-MUST-to-named-halt conversion class
  applied to the one remaining prose-only traceability requirement. This is not a new behavioral
  requirement but a change of enforcement mechanism: the same requirement that C-07 states in
  rubric prose becomes inline generative enforcement via a named halt.
- **Pass condition**: Output contains a named halt condition (e.g., F-27) that fires when any
  P1 finding row in BLOCK 2 has an empty or absent Section cell. The halt must be named, state
  the trigger condition (P1 row + empty Section cell), and require completion before BLOCK 2
  closes. P2 and P3 rows are not required to trigger F-27 -- the halt applies to P1 rows only,
  consistent with C-07's P1-mandatory / P2-50% traceability contract. An output where all P1
  Section cells happen to be populated but no F-27 halt is declared fails C-35 -- enforcement
  declaration is required.
- **R11 signal**: V-01 and V-02 scored 100 without F-27, confirming C-35 is aspirational. F-27
  applies the prose-MUST-to-named-halt conversion class to BLOCK 2 P1 traceability -- the same
  class that converted C-08's prose inversion requirement into F-06, C-09's synthesis
  requirement into F-11, and C-06's scope requirement into F-05. V-03, V-04, and V-05 carried
  F-27 as part of the R11 above-ceiling feature set.

### C-36 | BLOCK 2 Section Column Leftmost Placement for Enforcement Salience
- **Weight**: aspirational
- **Category**: format
- **Text**: The Section column in the BLOCK 2 findings table is placed as the first (leftmost)
  column, before Sev and Finding. C-10 established that a Section column must exist; C-35/F-27
  established that an empty P1 Section cell must fire a named halt. Column position is an
  orthogonal enforcement dimension: a leftmost Section cell is inspected first on every row
  scan, making an empty cell impossible to miss visually without executing any halt logic. A
  rightmost Section column can be overlooked in a wide table where the leftmost Sev and Finding
  cells are populated; a leftmost Section column cannot be skipped. This converts C-35's
  per-row halt into a per-table structural constraint that makes the halt less likely to be
  needed in the first place.
- **Pass condition**: BLOCK 2 findings table places the Section column as the first column (i.e.,
  immediately after any row-number or index column). A table with columns ordered Sev/Section/
  Finding or Finding/Section/Sev passes C-10 and C-35 but fails C-36. Column-first placement
  must hold regardless of any additive columns appended to the right. The column name must
  remain `Section` or an equivalent (e.g., `Design Section`) -- renaming it to a non-section
  identifier defeats the intent.
- **R12 signal**: V-02 introduced Section/Sev/Finding column order. The R12 scorecard called
  out the optimization twice: at C-07 ("section-first column order makes F-27 enforcement
  maximally salient") and at C-35 ("leftmost-column position makes empty Section cell impossible
  to miss visually"). V-01 used Sev/Section/Finding order and scored 100 on C-10 and C-35
  without the leftmost optimization, confirming C-36 is aspirational and orthogonal to both.

### C-37 | Named Halt Conditions Include Inline Corrective Action Specification
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every named halt condition (F-ID) specifies not only the trigger condition but also
  the exact corrective action required to satisfy the halt and resume generation. C-14 requires
  a named F-ID and stated trigger condition and that the output states "what must happen before
  the output continues" -- but C-14's pass condition is satisfied by a halt that names the
  trigger and states "halt until resolved." C-37 requires the resolution to be specific: the
  halt must say *what specifically to do* (e.g., "populate the Section cell with a design
  section reference before continuing" rather than "halt and fix"). A specific corrective action
  converts the halt from a detection event into a repair instruction -- the generator does not
  need to infer the fix from the trigger description.
- **Pass condition**: Every named halt condition in the output includes both (a) the trigger
  condition and (b) an explicit corrective action statement specifying what to do to resolve the
  halt. Halts that state only the trigger, or that use generic resolution language ("halt until
  the issue is resolved," "correct before continuing" without specifying the correction), pass
  C-14 but fail C-37. Coverage must be complete -- a single F-ID without a corrective action
  fails the criterion even if all others carry one. The corrective action must name the target
  cell or field and the type of content required (e.g., "a specific design section reference,"
  "a synthesis note explaining the disagreement"). Anaphoric references are permitted when the
  referent is unambiguous in the trigger clause (e.g., "Populate it before continuing. Halt."
  where the trigger clause names "Rationale cell" as the subject); bare verb forms without a
  named referent ("Populate. Halt.") fail.
- **R12 signal**: V-04 applied inline corrective action to every F-ID throughout the output. The
  R12 scorecard called out the pattern across five distinct criteria: C-09 ("STOP:F-11 fires
  with corrective action specified"), C-17 ("STOP:F-10 fires with 'halt and correct the
  mismatch'"), C-34 ("STOP:F-26 with 'populate it with a specific design section reference'"),
  C-35 ("STOP:F-27 fires with 'halt and populate it before continuing'"), and C-24
  ("STOP:F-16"). V-01, V-02, V-03, and V-05 scored 100 without inline corrective actions,
  confirming C-37 is aspirational. C-37 extends the halt-completeness class from C-14 (trigger
  coverage) to C-37 (trigger + resolution coverage).
- **R13 signal**: C-37 became the first criterion to produce active differentiation at R13. V-01
  and V-04 maintained cell-level specificity throughout (e.g., "Populate the Reason cell with
  the specific content signal," "Replace the non-standard tag with P1, P2, or P3"). V-02, V-03,
  and V-05 used systematic shorthand ("Populate. Halt." / "Replace. Halt.") without naming
  target fields, each scoring exactly 99.70. C-37 is now the leading discriminator between
  perfect and near-perfect outputs.
- **R14 signal**: V-01 PASS maintained, V-02 FAIL confirmed. Anaphoric resolution precedent
  clarified: V-01 F-19 "Populate it before continuing. Halt." passes -- "it" refers to
  "Rationale cell" as named in the trigger clause, making the referent unambiguous without
  repeating the noun. V-02 F-19 "Populate. Halt." fails -- bare imperative verb with no
  referent, named or anaphoric, leaves target cell implicit. The pass/fail boundary is not
  lexical length but referential completeness: a corrective action passes C-37 if and only if
  the target cell or field is either named explicitly or unambiguously recoverable from the
  trigger clause.
- **R15 signal**: V-05 PASS confirmed -- F-14 bare "Replace the Type value" fails (doesn't name
  AGREE or SPLIT as the required replacement values). The referent-completeness boundary applies
  to value specifications as well as field references: naming the field without naming the
  required value class fails C-37 when the value class is a closed enumeration (AGREE/SPLIT,
  P1/P2/P3) that is not recoverable from context.
- **R16 signal**: V-02 and V-04 achieved C-37 PASS on F-14 by naming "AGREE or SPLIT (whichever
  correctly classifies the row)" and on F-31 by naming "ELEVATED or BASELINE (whichever
  correctly classifies this P1 finding)." V-03 FAIL confirmed: "the correct tier" without
  naming P1/P2/P3, and "the correct value" without naming AGREE or SPLIT. The referent-
  completeness boundary is now established across three closed enumerations: AGREE/SPLIT (F-14),
  P1/P2/P3 (F-02), and ELEVATED/BASELINE (F-31). V-02 and V-04 are the first variations to
  achieve full C-37 PASS while V-05 also achieves PASS on all three enumerations.

### C-38 | BLOCK 0 Amendment Cost Column
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The BLOCK 0 pre-scan signal catalogue includes an Amendment Cost column (or
  equivalent: `Complexity`, `Risk Cost`) that estimates the implementation cost of addressing
  each detected signal if a domain expert surfaces a P1 finding on it. C-21 established BLOCK 0
  as a locked signal catalogue; C-26/F-18 required each signal to have a disposition; C-29/F-21
  required disposition Reason cells to be non-empty. Amendment Cost adds a fourth column class:
  a cost dimension that converts BLOCK 0 from a pure detection inventory into a prioritized risk
  register. With cost present at the pre-scan phase, expert selection in BLOCK 1 can be informed
  by both signal relevance (what experts to add) and amendment economics (what it will cost if
  they find problems). This is not an enforcement gate -- it is an additive depth column that
  enables triage before commitment.
- **Pass condition**: BLOCK 0 table includes an Amendment Cost column with a populated value for
  each signal row. The column must carry a substantive estimate (e.g., "high -- requires schema
  migration," "low -- config change only") -- a placeholder (e.g., "TBD", "unknown") without
  reasoning fails this criterion. A BLOCK 0 with the standard signal/domain/disposition columns
  passes C-21/C-26/C-29 but fails C-38. The F-13 and F-18 gate halts must still be present
  alongside the Amendment Cost column -- adding Amendment Cost does not substitute for any prior
  BLOCK 0 enforcement.
- **R12 signal**: V-05 extended BLOCK 0 to 4 columns with Amendment Cost. The R12 scorecard
  noted at C-21: "BLOCK 0 extended to 4 columns with Amendment Cost; F-13/F-18 gates still
  present." V-01, V-02, V-03, and V-04 scored 100 without it, confirming C-38 is aspirational.
  C-38 follows the additive-column-to-locked-block pattern: the same block that already holds
  F-13/F-18 enforcement gains a cost dimension without disturbing those gates.

### C-39 | BLOCK 5 Priority Rank Column for Amendment Sequencing
- **Weight**: aspirational
- **Category**: format
- **Text**: The BLOCK 5 amend pathway table includes a Priority Rank column (or equivalent:
  `Rank`, `Order`, `Sequence`) that explicitly orders the P1 amendments by recommended
  resolution sequence. C-20 established the 4-column base schema (P1 Finding / Section / Action
  / Re-run Scope); C-19/F-12 ensures all P1s are present in BLOCK 5. When multiple P1 findings
  require amendments, order may matter: some amendments block others (e.g., a data model fix
  must precede an API fix that depends on it); some sections interact such that amending them
  out of sequence introduces new inconsistencies. A Priority Rank column makes recommended
  sequencing explicit at the generation phase rather than leaving it to the implementer to infer
  from finding severity alone.
- **Pass condition**: BLOCK 5 table includes a Priority Rank column with a populated ordering
  value for each row (e.g., 1, 2, 3 or High/Med/Low with explicit ordering semantics). The rank
  values must use a consistent, unambiguous ordering scheme -- a column with arbitrary labels
  that do not imply order fails this criterion. A 4-column BLOCK 5 (the C-20 base schema) passes
  C-20 but fails C-39. The Priority Rank column must be additive -- the four base columns (P1
  Finding, Section, Action, Re-run Scope) must remain present; the rank column supplements, not
  replaces, any of them.
- **R12 signal**: V-03 and V-05 introduced a 5-column BLOCK 5 with Priority Rank. The R12
  scorecard confirmed at C-20: "5-column table (Priority Rank added); additive extension
  satisfies structural table form; column count non-binding when base schema is intact." V-01,
  V-02, and V-04 scored 100 using the 4-column base schema, confirming C-39 is aspirational.

### C-40 | BLOCK 5 Inertia Framing as Named Design Constraint
- **Weight**: aspirational
- **Category**: behavior
- **Text**: BLOCK 5 includes an explicit inertia principle statement that names the preservation
  contract before amend rows are generated: only the sections directly identified by each
  amendment change; all other design sections, decisions, and reviewer findings are preserved.
  F-05 fires reactively when an amend entry instructs a full re-review; C-06 requires targeted
  re-run scope. C-40 requires the output to go further -- to declare the inertia principle
  proactively as a named design constraint before any amend row is written, rather than relying
  solely on F-05's defensive halt. The proactive declaration converts the scope constraint from
  "fires when violated" to "stated as governing principle at block entry." An output where BLOCK
  5 happens to produce no full-re-review instructions but carries no inertia principle statement
  passes C-06 and fails C-40 -- explicit declaration is required.
- **Pass condition**: BLOCK 5 includes an inertia principle statement positioned before or
  immediately at the amend table. The statement must (a) declare that only identified sections
  change and all others are preserved, and (b) explicitly bar instructions that would replace or
  reconstruct design sections outside the amendment scope. A BLOCK 5 that satisfies F-05 (no
  full re-review halt) and C-06 (targeted amend present) but carries no named preservation
  declaration fails C-40. The inertia principle must be declarative -- it states the governing
  rule -- not merely a restatement of what F-05 halts on.
- **R12 signal**: V-05 introduced inertia framing with an explicit named preservation constraint.
  The R12 scorecard noted at C-06: "BLOCK 5 declared primary; inertia framing explicitly bars
  replacement instructions." V-01, V-02, V-03, and V-04 scored 100 without inertia framing,
  confirming C-40 is aspirational. C-40 elevates the scope constraint class from reactive halt
  (F-05) to proactive design principle -- the same elevation pattern that C-15 applied to the
  roster commitment (C-14 reactive -> C-15 proactive).

### C-41 | BLOCK 5 Section Column Leftmost Placement for Cross-Block Traceability Salience
- **Weight**: aspirational
- **Category**: format
- **Text**: The Section column in the BLOCK 5 amend pathway table is placed as the first
  (leftmost) column, before Priority Rank (if present), P1 Finding, Action, and Re-run Scope.
  C-36 established leftmost Section placement as a traceability salience mechanism for BLOCK 2;
  C-41 applies the same structural principle to BLOCK 5. In BLOCK 5, leftmost Section placement
  has an additional cross-block function: every amend row declares its target section before
  declaring the finding, making it immediately verifiable on each row scan whether the Section
  value traces back to a P1 finding in BLOCK 2. A Section value in BLOCK 5 that cannot be
  matched to BLOCK 2 is a structural mismatch; placing Section first makes this mismatch
  detectable without traversing the table. Column-first salience and cross-block traceability
  are distinct benefits of the same positional choice, both of which are lost if Section is
  placed to the right of the finding column.
- **Pass condition**: BLOCK 5 amend table places the Section column as the first column (i.e.,
  the leftmost data column, before P1 Finding and all other content columns). A table with
  columns ordered P1 Finding/Section/Action/Re-run Scope passes C-20 and C-34 but fails C-41.
  When C-39's Priority Rank column is also present, Section must still appear as the leftmost
  data column -- column order must be Section-first regardless of additive extensions. The
  column name must remain `Section` or an equivalent (e.g., `Design Section`, `Target
  Section`).
- **R13 signal**: V-02 introduced `Section | Priority Rank | P1 Finding | Action | Re-run
  Scope` column order in BLOCK 5. The R13 scorecard identified this as a new-pattern candidate:
  "Section-first in BLOCK 5 + section-traceability cross-block rule (Section in BLOCK 5 absent
  from BLOCK 2 = structural mismatch)." V-01 scored 100 using default P1 Finding-first column
  order without the leftmost Section optimization, confirming C-41 is aspirational and
  orthogonal to C-20, C-34, and C-39.

### C-42 | BLOCK 5 Section Values Cross-Block Verified Against BLOCK 2
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every Section cell value in BLOCK 5 must match a Section value that appears in at
  least one P1 finding row in BLOCK 2. A BLOCK 5 amend row targeting a section not sourced from
  any BLOCK 2 P1 finding is a structural mismatch: the amendment claims to address a section
  that the review never flagged as containing a P1 issue. A named halt condition (e.g., F-28)
  fires when a BLOCK 5 Section value has no matching Section in BLOCK 2's P1 finding rows. This
  extends the identity-integrity chain established for reviewer names (F-10, F-15, F-16, F-17)
  to section references: the same cross-block exact-match verification that ensures reviewer
  identities are consistent now ensures that amendment targets are grounded in finding evidence.
  C-34/F-26 enforced that the Section cell is non-empty; F-28 enforces that its value is valid.
- **Pass condition**: Output contains a named halt condition (e.g., F-28) that fires when any
  Section value in BLOCK 5 does not exactly match a Section value from a P1 finding row in BLOCK
  2. The halt must be named, state the trigger condition (BLOCK 5 Section value absent from BLOCK
  2 P1 rows), and identify the mismatched value so the error is precisely localizable. An output
  where BLOCK 5 Section values happen to match BLOCK 2 but no F-28 halt is declared fails C-42
  -- enforcement declaration is required, not incidental correctness. Aggregate tokens (e.g.,
  "All P1 sections") are not valid Section values for this verification; each row must name a
  specific section traceable to a BLOCK 2 P1 source. F-28 may resolve against a dedicated BLOCK
  2.7 section registry (C-43) rather than requiring a live BLOCK 2 P1 row lookup; both placement
  strategies satisfy C-42 as long as the named halt is declared and the mismatch is localizable.
- **R13 signal**: V-02 introduced the cross-block section traceability rule "Section in BLOCK 5
  absent from BLOCK 2 = structural mismatch." The R13 scorecard surfaced this as a new-pattern
  candidate alongside C-41. C-42 is orthogonal to C-41 (column position) -- an output can
  place Section leftmost without declaring F-28, or declare F-28 without placing Section
  leftmost. V-01 scored 100 without cross-block section verification, confirming C-42 is
  aspirational. F-28 closes the final cross-block integrity gap: the amendment target column is
  now subject to the same exact-match verification discipline as the reviewer identity column
  (F-10, F-15, F-16, F-17).
- **R14 signal**: All five R14 variations pass C-42 across three distinct F-28 placement
  strategies: inline BLOCK 5 lookup (V-01), upstream dedicated BLOCK 2.7 registry (V-02/V-04/
  V-05), and inline pre-check enumeration (V-03). C-42's pass condition is placement-agnostic;
  C-43 captures the dedicated registry as the architecturally strongest form.

### C-43 | BLOCK 2.7 P1 Section Registry for Upstream Amendment Target Lock
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Before BLOCK 3 (consensus) is generated, the output commits a dedicated BLOCK 2.7
  that enumerates all BLOCK 2 P1 Section values as a locked registry. F-28 (C-42) then resolves
  against this committed set rather than performing a live cross-block P1 row scan at BLOCK 5
  generation time. BLOCK 2.7 applies the anchor-then-verify pattern -- established by BLOCK 1
  (signal count) + BLOCK 1.5 (roster commitment) and BLOCK 2.5 (P1 count anchor) -- to the
  amendment target domain: the set of valid Section values for BLOCK 5 is locked midway through
  the lifecycle before any amend row is written. A live BLOCK 2 lookup at BLOCK 5 generation
  time is functionally equivalent but architecturally weaker: it requires scanning a potentially
  large BLOCK 2 table at the time the amend row is written rather than resolving against a
  pre-committed, bounded registry. BLOCK 2.7 is not a new enforcement gate -- C-42/F-28 is the
  gate -- but a structural upgrade that makes the gate's anchor explicit and bounded before
  downstream generation begins.
- **Pass condition**: Output contains a dedicated registry block (BLOCK 2.7 or equivalent named
  block) positioned after BLOCK 2 and before BLOCK 3, enumerating all P1 Section values from
  BLOCK 2 as a committed set. F-28 must reference this block as its verification source (e.g.,
  "fires when a BLOCK 5 Section value is absent from the BLOCK 2.7 registry"). An output that
  satisfies C-42 by direct BLOCK 2 P1 row lookup at BLOCK 5 generation time passes C-42 but
  fails C-43 -- the dedicated pre-committed registry is independently required. An inline pre-
  check enumeration within BLOCK 5 itself (e.g., listing P1 sections as a preamble before the
  amend table) satisfies neither C-43 (wrong lifecycle position) nor the upstream lock intent;
  any position statement naming this placement as "non-conformant" is correct and encouraged
  (POSITION CONSTRAINT negative naming closes the enforcement gap by eliminating ambiguity about
  whether an inline pre-check might satisfy the criterion).
- **R14 signal**: V-02, V-04, and V-05 introduced BLOCK 2.7 as a dedicated P1 Section registry.
  V-01 satisfied C-42 via inline BLOCK 5 lookup (PASS C-42, FAIL C-43); V-03 satisfied C-42 via
  inline pre-check enumeration (PASS C-42, FAIL C-43). V-02/V-04/V-05 scored 100 on both C-42
  and C-43. C-43 extends the anchor-then-verify pattern one stage: BLOCK 0 locks valid signals,
  BLOCK 1.5 locks valid reviewers, BLOCK 2.5 locks P1 count, BLOCK 2.7 locks valid amendment
  sections. Each intermediate block converts a downstream lookup into a committed pre-check.
- **R15 signal**: V-02, V-04, and V-05 all included explicit POSITION CONSTRAINT negative
  naming -- "placed inside BLOCK 5 is non-conformant" -- to close the enforcement gap left by
  ambiguity about inline pre-check placement. This negative naming pattern is architecturally
  parallel to C-23 register isolation: naming what is prohibited eliminates the inference work
  of deriving the prohibition from the positive requirement alone.

### C-44 | Cross-Block Mismatch Halts Specify Both Upstream and Downstream Resolution Paths
- **Weight**: aspirational
- **Category**: behavior
- **Text**: When a named halt fires on a cross-block reference mismatch -- a value in a
  downstream block that does not match any entry in an upstream source block -- the corrective
  action specifies both possible resolution directions: (a) correct the downstream value to
  match a valid upstream entry, and (b) add the missing entry to the upstream source block. A
  cross-block mismatch is directionally ambiguous: either the downstream reference is wrong
  (amend the downstream row) or the upstream source is incomplete (add the missing entry).
  Naming only one path implicitly mandates the other as the only valid repair, which may be
  incorrect. F-28 is the canonical instance: a BLOCK 5 Section value absent from BLOCK 2 P1
  rows could mean the amendment target is wrong (fix BLOCK 5) or that a P1 finding was missed
  (add to BLOCK 2). C-44 requires both paths to be named. C-37 requires corrective action
  specificity; C-44 requires bidirectional resolution coverage for cross-block mismatch halts
  specifically. An output can satisfy C-37 with a single-path corrective action ("correct the
  Section value") and fail C-44.
- **Pass condition**: Every named halt that fires on a cross-block reference mismatch specifies
  both the downstream correction path and the upstream addition path in its corrective action
  clause. For F-28 specifically: the corrective action must name (a) correcting the BLOCK 5
  Section value to match a BLOCK 2 P1 Section, and (b) adding the missing P1 finding to BLOCK 2
  if the section is legitimately a P1 target. An F-28 corrective action that states only "correct
  the Section value" passes C-37 but fails C-44. The bidirectional requirement applies to all
  cross-block reference mismatch halts in the identity-integrity chain (F-03, F-10, F-15, F-16,
  F-17, F-28) where both resolution directions are architecturally valid. Halts on structural
  absence (F-01, F-04) or count parity (F-09, F-12) are exempt -- those failure modes have a
  single unambiguous repair path.
- **R14 signal**: V-01 introduced bifurcated F-28 corrective action: "Correct the Section value
  to match a BLOCK 2 P1 Section, or add the P1 finding to BLOCK 2 before continuing. Halt."
  The R14 scorecard identified this as a new-pattern candidate: F-28 names both paths with
  block specificity. V-02 through V-05 satisfied C-42 with single-direction corrective actions
  or no corrective action specification (failing C-37), confirming C-44 is aspirational and
  orthogonal to C-43 (registry placement). C-44 is the first criterion to encode resolution
  completeness as a distinct property from corrective action specificity (C-37): a halt is
  repair-complete when its corrective action covers every valid resolution path, not just the
  most obvious one.
- **R15 signal**: V-05 achieved full C-44 PASS -- the first variation to apply bidirectional
  resolution labeling uniformly across all 6 cross-block reference mismatch halts: F-03, F-10,
  F-15, F-16, F-17, F-28. Each carries explicit `Downstream fix:` / `Upstream fix:` labels.
  The exempt categories (structural absence F-01/F-04, count parity F-09/F-12) were correctly
  identified and remained single-path. V-01 and V-04 applied bidirectional coverage only to
  F-28, failing C-44 for the remaining mismatch halts. C-44's pass boundary is class-level
  uniformity: the bidirectional pattern must be applied to every member of the cross-block
  reference mismatch halt class, not just the most recently introduced instance.

### C-45 | BLOCK 3 Elevation Record as Typed Intermediate Artifact
- **Weight**: aspirational
- **Category**: behavior
- **Text**: BLOCK 3 (consensus) produces a typed Elevation Record that classifies each P1
  finding as ELEVATED or BASELINE based on consensus signal -- ELEVATED when two or more
  reviewers independently flagged the same P1 issue, BASELINE otherwise. BLOCK 5 then consumes
  this record via a named CONSENSUS ELEVATION RULE that deterministically orders amendments:
  ELEVATED P1s precede BASELINE P1s in the amend pathway without requiring re-computation at
  BLOCK 5 generation time. This extends the intermediate-artifact pattern established by BLOCK
  2.7 (P1 Section registry consumed by F-28) to the priority dimension: BLOCK 3 produces the
  artifact, BLOCK 5 consumes it via a named rule, and the rule's output (ordering) is
  deterministic given the artifact. A BLOCK 5 that independently re-assesses P1 priority
  without referencing a typed BLOCK 3 record re-computes what was already determined and
  introduces re-computation drift -- the same P1 may rank differently if assessed twice.
- **Pass condition**: BLOCK 3 output contains an Elevation Record (or equivalent named artifact)
  that assigns each P1 finding a typed classification (ELEVATED or BASELINE). BLOCK 5 references
  a named CONSENSUS ELEVATION RULE (or equivalent) that consumes the BLOCK 3 Elevation Record
  to determine the amendment priority ordering; the rule must name BLOCK 3 as its source. An
  output where BLOCK 5 orders amendments by priority without referencing a typed BLOCK 3 record
  passes C-39 (Priority Rank column) but fails C-45. The ELEVATED/BASELINE vocabulary need not
  be exact -- equivalent typed classification schemes (e.g., CONSENSUS-FLAGGED/SINGLE-REVIEWER)
  satisfy the criterion if the classification is produced in BLOCK 3 and consumed by name in
  BLOCK 5.
- **R15 signal**: V-05 introduced the BLOCK 3 Elevation Record pattern. The R15 scorecard
  identified this as a new-pattern candidate: "BLOCK 3 Elevation Record classifying P1 findings
  as ELEVATED or BASELINE feeding BLOCK 5 CONSENSUS ELEVATION RULE for deterministic priority
  ordering." V-01, V-02, V-03, and V-04 scored at ceiling (99.73) without it, confirming C-45
  is aspirational. C-45 is the first criterion where BLOCK 3 produces a named intermediate
  artifact consumed by a later block -- prior intermediate artifacts are all produced by
  even-numbered blocks (BLOCK 0, BLOCK 2, BLOCK 2.5, BLOCK 2.7) or by the half-blocks. The
  Elevation Record -> Elevation Rule pattern eliminates the last re-computation gap in the
  lifecycle.
- **R16 signal**: V-02 and V-04 both include F-31 (Elevation Record Consensus Status named
  halt) confirming C-45 is achievable without F-31. C-47 captures the F-31 named halt as the
  next aspirational step above C-45. V-05 adds CONSENSUS ELEVATION RULE with 3 fully enumerated
  ordered levels; C-49 captures that full-enumeration pattern as independently aspirational.

### C-46 | BLOCK N SEALED Lifecycle Gate Statements
- **Weight**: aspirational
- **Category**: behavior
- **Text**: At the close of each lifecycle block, the output contains an explicit SEALED
  statement (or equivalent named gate: VERIFIED, CLOSED, LOCKED) that attests (a) the
  verification condition that has been satisfied within the block, and (b) the next block that
  will proceed. Each SEALED statement converts an implicit block transition -- "generation
  continues" -- into a named, inspectable event: the progression is attested, not assumed. This
  extends the lifecycle-gate pattern established by the intermediate anchor blocks (BLOCK 0
  locks signals, BLOCK 1.5 locks the roster, BLOCK 2.5 locks P1 count, BLOCK 2.7 locks
  sections) to every block in the lifecycle, not just the anchor blocks. A SEALED statement is
  structurally distinct from a halt condition: halts fire when a constraint is violated; SEALED
  gates fire when a constraint is satisfied. Together they form a complete progression contract:
  halts prevent invalid advance; SEALED gates confirm valid advance.
- **Pass condition**: Each lifecycle block (BLOCK 0, BLOCK 1, BLOCK 1.5, BLOCK 2, BLOCK 2.5,
  BLOCK 2.7 if present, BLOCK 3, BLOCK 4, BLOCK 5) contains a terminal SEALED statement or
  named equivalent at its close. The statement must name (a) what was verified within the block
  and (b) which block proceeds next. A block that ends with a heading transition or a blank line
  without an explicit SEALED or equivalent attestation fails this criterion for that block. A
  single block missing its SEALED statement fails C-46, consistent with the complete-coverage
  requirement of C-14. BLOCK 5 is the terminal block; its SEALED statement must name the
  review lifecycle as complete rather than naming a next block.
- **R15 signal**: V-04 introduced BLOCK N SEALED gates -- explicit verified-progression
  statements at the close of each lifecycle block naming the verification condition and the next
  block. The R15 scorecard identified this as a new-pattern candidate: "BLOCK N SEALED gate
  statements at close of each lifecycle block naming the verification condition and next block."
  V-01, V-02, V-03, and V-05 scored at ceiling (99.73) without it, confirming C-46 is
  aspirational. C-46 is structurally parallel to C-14 (named halts on every block) but inverted
  in polarity: C-14 enforces failure-path coverage; C-46 enforces success-path attestation.
  Together they close the lifecycle contract in both directions.
- **R16 signal**: V-01, V-04, and V-05 all pass C-46. V-01 uses summary SEALED (names
  verification condition + next block); V-04 enumerates specific F-codes verified per block;
  V-05 enumerates F-codes with inline invariant descriptions per F-code. Three distinct quality
  levels of SEALED statement are now observed: (a) summary attestation (V-01, C-46 floor),
  (b) F-code enumeration (V-04, C-48 floor), (c) F-code + invariant description (V-05, above
  C-48). C-48 captures the F-code enumeration pattern as the next aspirational step above C-46.

### C-47 | Elevation Record Consensus Status Named Halt
- **Weight**: aspirational
- **Category**: behavior
- **Text**: A named halt condition (e.g., F-31) fires when any P1 row in the BLOCK 3 Elevation
  Record has a `Consensus Status` (or equivalent classification column) value that is neither
  ELEVATED nor BASELINE. C-45 requires the Elevation Record to exist and assign a typed
  classification to each P1 finding; C-47 requires a named halt to enforce that the
  classification value belongs to the correct closed enumeration. This is the content-
  completeness-within-structural-presence class applied to the Elevation Record's classification
  column: C-45 establishes the column exists and is populated; F-31 fires when the populated
  value is outside the closed enumeration {ELEVATED, BASELINE}. The pattern is structurally
  parallel to F-14 (Type column in BLOCK 3 consensus table must be AGREE or SPLIT) applied one
  block earlier on the Elevation Record artifact. Without F-31, a Consensus Status cell
  containing an arbitrary label (e.g., "HIGH", "MAYBE") satisfies C-45's structural presence
  requirement while producing a non-deterministic priority ordering in BLOCK 5.
- **Pass condition**: Output contains a named halt condition (e.g., F-31) that fires when any
  Elevation Record row's Consensus Status cell contains a value outside the closed enumeration
  {ELEVATED, BASELINE}. The halt must be named, state the trigger condition, and name both
  ELEVATED and BASELINE as the valid replacement values -- a halt that fires on an invalid value
  without naming the valid values fails C-37 and fails C-47. Reviews with no P1 findings are
  exempt from triggering the halt but must still declare it exists. The closed-enumeration
  naming requirement applies: "Replace the Consensus Status value with the correct
  classification" without naming ELEVATED or BASELINE fails C-47 per the referent-completeness
  boundary established in C-37.
- **R16 signal**: V-02, V-04, and V-05 all introduced F-31. The canonical form observed across
  all three: "Replace the Consensus Status value with ELEVATED or BASELINE (whichever correctly
  classifies this P1 finding based on BLOCK 3 AGREE rows) before continuing. Halt." V-01 and
  V-03 pass C-45 (Elevation Record present) without F-31, confirming C-47 is aspirational and
  orthogonal to C-45. F-31 is the first enforcement gate on the Elevation Record's typed
  classification column -- C-45 establishes the artifact; C-47 guards its value integrity.

### C-48 | SEALED Gate F-Code Enumeration
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Each SEALED statement (C-46) enumerates the specific named halt conditions (F-IDs)
  that were verified as satisfied within the block, rather than summarizing the verification
  condition in prose only. C-46 requires the SEALED statement to name (a) what was verified and
  (b) which block proceeds; the verification condition may be described in summary prose (e.g.,
  "all reviewers confirmed"). C-48 requires the verification description to enumerate specific
  F-IDs by name, making each SEALED gate an auditable inspection record: every F-ID that fired
  successfully (not as a halt) is named in the terminal attestation. This converts the SEALED
  gate from a summary assertion into a per-constraint checklist, enabling downstream inspection
  of exactly which invariants were verified at each block boundary without re-reading the block
  body.
- **Pass condition**: Each SEALED statement names at minimum the F-ID codes whose invariants
  were verified within the block (e.g., "F-04, F-11, F-14, F-15, F-23, and F-31 enforcement
  passed. BLOCK 4 proceeds."). A SEALED statement using only summary prose ("all constraints
  verified") passes C-46 but fails C-48 -- F-code enumeration is independently required.
  Coverage must be complete across all blocks: a single SEALED statement without F-code
  enumeration fails C-48, consistent with the complete-coverage requirement of C-14 and C-46.
  Blocks with no associated F-IDs (e.g., BLOCK 5 terminal) may describe verified conditions in
  prose when no F-IDs apply; the criterion is F-code enumeration *when F-IDs exist* for the
  block. Inline invariant descriptions per F-ID (e.g., "F-04 (block present), F-11 (SPLIT
  Synthesis populated)") are an enriched form of C-48 and are encouraged but not required for
  pass.
- **R16 signal**: V-04 introduced F-code enumeration in SEALED statements across all lifecycle
  blocks. The canonical V-04 form at BLOCK 3: "F-04, F-11, F-14, F-15, F-23, and F-31
  enforcement passed. BLOCK 4 proceeds." V-05 extended to F-code + inline invariant description:
  "F-04 (block present), F-11 (SPLIT Synthesis populated), F-14 (Type = AGREE or SPLIT), F-15
  (Reviewers from BLOCK 1.5 roster), F-23 (Issue populated), and F-31 (Consensus Status =
  ELEVATED or BASELINE) invariants verified." V-01 passes C-46 with summary prose SEALED
  without F-code enumeration, confirming C-48 is aspirational and orthogonal to C-46. C-48
  applies the same precision escalation that C-37 applied to halt corrective actions (summary ->
  named-target) to SEALED attestations (summary -> named-F-codes).

### C-49 | CONSENSUS ELEVATION RULE Three-Level Explicit Ordering with Non-Conformance Prohibition
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The BLOCK 5 CONSENSUS ELEVATION RULE (required by C-45) explicitly enumerates all
  ordering levels as a fully specified algorithm: (1) ELEVATED tier: rows ranked 1 through
  ELEVATED_count, sorted by Amendment Cost (High/Medium/Low descending) then reviewer count
  descending; (2) BASELINE tier: rows ranked ELEVATED_count+1 through P1_count, sorted by the
  same keys; (3) tie-breaking: explicitly declares no ties (or names the tiebreaker when ties
  exist). Additionally, the rule includes a named non-conformance prohibition: re-assessing
  Consensus Status at BLOCK 5 generation time is explicitly declared non-conformant. C-45
  requires the rule to exist, consume the BLOCK 3 Elevation Record, and name BLOCK 3 as its
  source; C-49 requires the rule to be a fully enumerated ordering algorithm with a named
  prohibition against deferred re-assessment. The prohibition closes the re-computation drift
  gap at the rule level: C-45 eliminates re-computation by requiring an intermediate artifact;
  C-49 makes the prohibition explicit so it cannot be silently violated by a variation that
  re-assesses elevation without labeling it as re-computation.
- **Pass condition**: BLOCK 5 CONSENSUS ELEVATION RULE contains (a) an explicit ordered tier
  enumeration naming at minimum ELEVATED and BASELINE tiers with their rank ranges and sort keys,
  and (b) an explicit non-conformance prohibition statement declaring that re-assessing Consensus
  Status at BLOCK 5 generation time is non-conformant. A rule that names the two tiers but omits
  sort keys fails C-49. A rule that names the tiers and sort keys but omits the non-conformance
  prohibition fails C-49. Both elements are required. A rule satisfying C-45 (exists, names
  BLOCK 3 as source) but not fully enumerating tiers or sort keys passes C-45 and fails C-49;
  the two criteria are independent.
- **R16 signal**: V-05 introduced the three-level explicitly enumerated CONSENSUS ELEVATION RULE
  with explicit non-conformance prohibition: "Re-assessing consensus status at BLOCK 5
  generation time is non-conformant. The Elevation Record is the sole authoritative
  classification source." The BLOCK 5 SEALED statement carried the tier count attestation:
  "[ELEVATED_count] ELEVATED-tier rows ranked 1 through [ELEVATED_count]; [BASELINE_count]
  BASELINE-tier rows ranked [ELEVATED_count + 1] through [P1_count]." V-01, V-02, V-03, and
  V-04 pass C-45 with a named rule naming BLOCK 3 as source, but none fully enumerates the
  ordered tiers or includes the non-conformance prohibition, confirming C-49 is aspirational.
  C-49 is the first criterion to combine algorithmic completeness (ordered tier enumeration with
  sort keys) with named prohibition (non-conformance statement) -- the same dual structure that
  C-43 uses for BLOCK 2.7 (committed registry as the anchor) and POSITION CONSTRAINT negative
  naming (prohibition against inline pre-check).

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 42 * 10)
```

Note: aspirational denominator changed from 39 to 42 in v16 (added C-47, C-48, C-49). Each
aspirational criterion contributes ~0.238 points at full pass.

**Golden threshold**: All 4 essential criteria pass AND composite >= 80.

| Outcome    | Condition |
|------------|-----------|
| Golden     | C-01 + C-02 + C-03 + C-04 all pass, composite >= 80 |
| Acceptable | All essential pass, composite >= 70 |
| Needs work | Any essential fails OR composite < 70 |

---

## Failure Mode Reference

| Failure | Likely Criterion | Signal |
|---------|-----------------|--------|
| Missing discipline reviewer | C-01 | Fewer than 6 named discipline sections |
| Finding with no severity | C-02 | Bullet with no P1/P2/P3 tag |
| Domain expert with no stated reason | C-03 | Expert listed without input-signal mapping |
| No consensus section | C-04 | Review ends after per-reviewer blocks |
| All findings are P1 | C-08 | Over-escalation, reviewer calibration issue |
| Split opinions listed but not analyzed | C-09 | "Reviewer A says X; Reviewer B says Y" with no synthesis |
| Finding list is prose bullets, no table | C-10 | No Sev or Section column present |
| Expert trace is a single sentence | C-11 | No labeled Signal/Expert/Reason fields |
| Pyramid gate not a dedicated block | C-12 | Pyramid check embedded in findings prose |
| Expert trace is labeled prose, not table | C-13 | Three fields present but not in column form |
| Block has no named F-ID | C-14 | Halt language without an F-ID code |
| No roster table before findings | C-15 | No BLOCK 1.5 committed roster |
| Roster table has no Source column | C-16 | Stock/Domain origin not structurally visible |
| No orphan detection halt | C-17 | F-10 missing from output |
| SPLIT row has empty Synthesis | C-18 | F-11 missing or not firing |
| BLOCK 5 P1 count doesn't match BLOCK 2.5 | C-19 | F-12 missing from output |
| BLOCK 5 is a code block, not a table | C-20 | No 4-column amend table |
| No BLOCK 0 pre-scan catalogue | C-21 | Expert selection not anchored to a signal list |
| BLOCK 3 is prose, not a table | C-22 | No 4-column consensus table |
| Informal language in block headers | C-23 | "aim for" / "try to" in F-ID trigger clauses |
| BLOCK 4 reviewer not in roster | C-24 | F-16 missing from output |
| BLOCK 5 re-run names phantom reviewer | C-25 | F-17 missing from output |
| BLOCK 0 signal has no BLOCK 1 disposition | C-26 | F-18 missing from output |
| BLOCK 2.5 inversion has empty Rationale | C-27 | F-19 missing from output |
| BLOCK 4 is prose, not a table | C-28 | No 3-column unique-catch table |
| Disposition row has empty Reason | C-29 | F-21 missing from output |
| Domain expert has no BLOCK 2 finding block | C-30 | F-22 missing from output |
| BLOCK 3 row has empty Issue cell | C-31 | F-23 missing from output |
| BLOCK 5 row has empty Action cell | C-32 | F-24 missing from output |
| BLOCK 4 row has empty Finding cell | C-33 | F-25 missing from output |
| BLOCK 5 row has empty Section cell | C-34 | F-26 missing from output |
| P1 finding row has empty Section cell | C-35 | F-27 missing from output |
| Section column not leftmost in BLOCK 2 | C-36 | Sev or Finding precedes Section |
| Halt states trigger but not corrective action | C-37 | F-ID names the problem but not the fix |
| BLOCK 0 has no Amendment Cost column | C-38 | Signal catalogue missing cost dimension |
| BLOCK 5 has no Priority Rank column | C-39 | Amend table lacks sequencing guidance |
| BLOCK 5 has no inertia principle statement | C-40 | Preservation contract not declared |
| Section column not leftmost in BLOCK 5 | C-41 | P1 Finding precedes Section in BLOCK 5 |
| BLOCK 5 Section not verified against BLOCK 2 | C-42 | F-28 missing from output |
| No BLOCK 2.7 dedicated section registry | C-43 | F-28 resolves at BLOCK 5 generation time |
| Mismatch halt names only one repair path | C-44 | Downstream fix named, upstream fix omitted |
| No BLOCK 3 Elevation Record artifact | C-45 | BLOCK 5 priority order re-computed at generation |
| Block closes without SEALED attestation | C-46 | Implicit transition, no verified-progression gate |
| Elevation Record has no F-31 value halt | C-47 | Consensus Status cell not guarded by named halt |
| SEALED gate names verification in prose only | C-48 | F-codes not enumerated in SEALED statement |
| CONSENSUS ELEVATION RULE not fully enumerated | C-49 | Tier sort keys or non-conformance prohibition absent |
