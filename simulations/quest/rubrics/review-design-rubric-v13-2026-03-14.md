Written to `simulations/quest/rubrics/review-design-rubric-v13-2026-03-14.md`.

---

**Two new criteria extracted from R13:**

**C-41 | BLOCK 5 Section Column Leftmost Placement for Cross-Block Traceability Salience**
- Pattern class: format (parallel to C-36 for BLOCK 2)
- V-02 introduced `Section | Priority Rank | P1 Finding | Action | Re-run Scope`; Section-first makes each amend row's target section immediately verifiable against BLOCK 2 without traversing the table
- Pass condition: Section must be the leftmost data column in BLOCK 5 regardless of additive extensions; `P1 Finding/Section/...` order fails

**C-42 | BLOCK 5 Section Values Cross-Block Verified Against BLOCK 2**
- Pattern class: behavior / cross-block content integrity (extends the F-10/F-15/F-16/F-17 identity chain to section references)
- F-28 fires when a BLOCK 5 Section value has no matching Section in BLOCK 2 P1 rows — an amendment targeting a section the review never flagged is a structural mismatch
- Pass condition: named F-28 halt declared; C-34 (non-empty) + C-42 (valid) together close the Section column

**Formula:** denominator 33 → 35. Each aspirational criterion ~0.286 pts. Ceiling 100 preserved.

**C-37 note added:** R13 made C-37 the first active differentiator — V-01/V-04 at 100.00 vs V-02/V-03/V-05 at 99.70, split solely on cell-level corrective action specificity vs. "Populate. Halt." shorthand.
issing discipline block is a structural omission -- the review surface is incomplete and no
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
  "a synthesis note explaining the disagreement").
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
  specific section traceable to a BLOCK 2 P1 source.
- **R13 signal**: V-02 introduced the cross-block section traceability rule "Section in BLOCK 5
  absent from BLOCK 2 = structural mismatch." The R13 scorecard surfaced this as a new-pattern
  candidate alongside C-41. C-42 is orthogonal to C-41 (column position) -- an output can
  place Section leftmost without declaring F-28, or declare F-28 without placing Section
  leftmost. V-01 scored 100 without cross-block section verification, confirming C-42 is
  aspirational. F-28 closes the final cross-block integrity gap: the amendment target column is
  now subject to the same exact-match verification discipline as the reviewer identity column
  (F-10, F-15, F-16, F-17).

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 35 * 10)
```

Note: aspirational denominator changed from 33 to 35 in v13 (added C-41, C-42). Each
aspirational criterion contributes ~0.286 points at full pass.

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
| Pyramid check is inline prose, not a block | C-12 | No discrete pyramid gate section between findings and consensus |
| Expert trace is labeled prose, not a table | C-13 | Three-field prose passes C-11; only table form passes C-13 |
| Halt conditions use prose, not named F-IDs | C-14 | Requirements stated without failure identifier tags |
| F-IDs present but missing from any one block | C-14 | Partial coverage fails as decisively as no coverage |
| No roster table before first finding block | C-15 | Reviewers appear only as finding block headers, not pre-committed in BLOCK 1.5 |
| Roster committed as prose list, not table | C-15 | Numbered list before BLOCK 2 satisfies proactive intent; table form is required |
| BLOCK 1.5 table has no Source column | C-16 | Two-column table (Reviewer + Role) passes C-15; Source column required for C-16 |
| Domain reviewer in BLOCK 1.5 has no BLOCK 1 match | C-17 | No F-10 or equivalent named orphan-detection halt present |
| SPLIT row has empty Synthesis field, no halt fires | C-18 | F-11 absent; content completeness not enforced inline |
| BLOCK 5 P1 count not verified against BLOCK 2.5 anchor | C-19 | No F-12 or equivalent cross-block count-parity halt present |
| BLOCK 5 uses code-block form, not 4-column table | C-20 | Amend pathway described passes C-06; table form required for C-20 |
| No pre-scan block before BLOCK 1 expert selection | C-21 | Signals listed only within BLOCK 1; no locked catalogue with formal SHALL constraint |
| BLOCK 3 consensus is prose, not 4-column table | C-22 | Prose consensus passes C-04; table form with Synthesis column required for C-22 |
| Block header or F-ID trigger uses informal language | C-23 | "Aim for," "try to ensure," or similar calibration phrasing in a header or halt condition |
| BLOCK 4 Reviewer cell has no BLOCK 1.5 match | C-24 | No F-16 or equivalent named halt; none token exempt from check |
| BLOCK 5 Re-run Scope names reviewer absent from BLOCK 1.5 | C-25 | No F-17 or equivalent named halt; identity chain incomplete at BLOCK 5 |
| BLOCK 0 signal has no BLOCK 1 resolution or disposition row | C-26 | No F-18 or equivalent named halt; inbound gate (C-21) present but outbound resolution absent |
| BLOCK 2.5 inversion present but Rationale cell empty | C-27 | No F-19 halt; pyramid gate block exists (C-12) but inversion rationale not enforced at cell level |
| BLOCK 4 unique catches in prose or bullets, not a table | C-28 | No F-20 halt; C-05 passes on presence; 3-column table form required for C-28 |
| BLOCK 0 no-expert disposition row has empty Reason cell | C-29 | No F-21 halt; disposition row exists (C-26) but reason content not enforced at cell level |
| Domain expert in BLOCK 1.5 has no BLOCK 2 finding block | C-30 | No F-22 halt; F-01 covers stock disciplines but domain tier was previously unguarded |
| BLOCK 3 row has empty Issue cell, no halt fires | C-31 | No F-23 halt; three of four BLOCK 3 columns had halts; Issue column was the last unguarded |
| BLOCK 5 amend row has empty or placeholder Action cell | C-32 | No F-24 halt; structural and identity halts on BLOCK 5 allow empty Action cell to pass |
| BLOCK 4 row has empty or absent Finding cell | C-33 | No F-25 halt; table form (C-28) and reviewer identity (C-24) satisfied but no catch content enforced |
| BLOCK 5 amend row has empty or placeholder Section cell | C-34 | No F-26 halt; Action cell (C-32) closed but Section cell left without content gate; amend non-localizable |
| P1 finding row in BLOCK 2 has empty Section cell, no halt fires | C-35 | No F-27 halt; C-07 prose-MUST not converted to named halt; inline enforcement absent |
| BLOCK 2 Section column is not leftmost | C-36 | Section column present (C-10) and F-27 halt declared (C-35) but column order places Section after Sev or Finding; visual salience absent |
| Named halt states trigger but not corrective action | C-37 | F-ID fires on trigger condition; generic "halt until resolved" without specifying what to do; C-14 passes, C-37 fails |
| BLOCK 0 has no Amendment Cost column | C-38 | Signal catalogue present (C-21), disposition complete (C-26), reason populated (C-29) but no cost estimate per signal; triage dimension absent |
| BLOCK 5 has no Priority Rank column | C-39 | 4-column base schema present (C-20), all P1s covered (C-19) but no amendment sequencing; multi-P1 ordering left implicit |
| BLOCK 5 has no inertia principle declaration | C-40 | F-05 halt present (no full re-review), targeted re-run declared (C-06) but no named preservation constraint before amend rows; proactive inertia framing absent |
| BLOCK 5 Section column is not leftmost | C-41 | Section column present (C-34) but placed after P1 Finding or Priority Rank; cross-block traceability salience absent; C-36 pattern not mirrored in BLOCK 5 |
| BLOCK 5 Section value absent from BLOCK 2 P1 rows | C-42 | No F-28 halt; Section cell non-empty (C-34) but value not verified against BLOCK 2 P1 source sections; amendment targets a section the review never flagged as containing a P1 |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric -- 9 criteria, 4E/3R/2A |
| v2 | 2026-03-14 | Added C-10 (structural columns) and C-11 (three-field expert trace) from R1 scorecard excellence signals; updated aspirational denominator from 2 to 4 |
| v3 | 2026-03-14 | Added C-12 (pyramid gate as lifecycle block), C-13 (expert trace table columns), and C-14 (named F-ID halt conditions) from R2 scorecard new_patterns; updated aspirational denominator from 4 to 7 |
| v4 | 2026-03-14 | Added C-15 (roster commitment table before finding generation) from R3 new_patterns; refined C-13 and C-14 with R3 orthogonality and localizability signals; updated aspirational denominator from 7 to 8 |
| v5 | 2026-03-14 | Added C-16 (Source column in roster commitment table) and C-17 (cross-block reviewer identity verification / orphan detection) from R4 excellence signals; refined C-14 and C-15 with R4 form-sensitivity signals; updated aspirational denominator from 8 to 10 |
| v6 | 2026-03-14 | Added C-18 (content-completeness halt on SPLIT synthesis field / F-11), C-19 (cross-block count-parity for P1 findings / F-12), and C-20 (BLOCK 5 amend pathway in 4-column table form) from R5 scorecard new_patterns; updated aspirational denominator from 10 to 13 |
| v7 | 2026-03-14 | Added C-21 (BLOCK 0 pre-scan signal catalogue), C-22 (BLOCK 3 consensus in 4-column structural table form), and C-23 (register isolation for formal lifecycle block headers) from R6 scorecard new_patterns; updated aspirational denominator from 13 to 16 |
| v8 | 2026-03-14 | Added C-24 (BLOCK 4 unique-catch reviewer identity verification / F-16), C-25 (BLOCK 5 Re-run Scope reviewer identity verification / F-17), and C-26 (BLOCK 0 signal disposition completeness / F-18 bidirectional gate) from R8 scorecard excellence signals; updated aspirational denominator from 16 to 19 |
| v9 | 2026-03-14 | Added C-27 (BLOCK 2.5 pyramid inversion rationale content completeness / F-19), C-28 (BLOCK 4 unique catches in structural table form / F-20), and C-29 (BLOCK 0 no-expert disposition row reason content completeness / F-21) from R9 scorecard excellence signals; updated aspirational denominator from 19 to 22 |
| v10 | 2026-03-14 | Added C-30 (BLOCK 2 domain expert finding coverage symmetry / F-22), C-31 (BLOCK 3 consensus Issue column content completeness / F-23), and C-32 (BLOCK 5 amend Action cell content completeness / F-24) from R10 scorecard excellence signals; updated aspirational denominator from 22 to 25 |
| v11 | 2026-03-14 | Added C-33 (BLOCK 4 unique catch Finding cell content completeness / F-25), C-34 (BLOCK 5 amend Section cell content completeness / F-26), and C-35 (BLOCK 2 P1 Section cell named halt enforcement / F-27) from R11 scorecard excellence signals; updated aspirational denominator from 25 to 28 |
| v12 | 2026-03-14 | Added C-36 (BLOCK 2 Section column leftmost placement for enforcement salience), C-37 (named halt conditions include inline corrective action specification), C-38 (BLOCK 0 Amendment Cost column), C-39 (BLOCK 5 Priority Rank column for amendment sequencing), and C-40 (BLOCK 5 inertia framing as named design constraint) from R12 scorecard excellence signals; updated aspirational denominator from 28 to 33; updated C-20 pass condition to note column count non-binding when base schema intact; updated C-21 pass condition to note additive BLOCK 0 columns permitted |
| v13 | 2026-03-14 | Added C-41 (BLOCK 5 Section column leftmost placement for cross-block traceability salience) and C-42 (BLOCK 5 Section values cross-block verified against BLOCK 2 / F-28) from R13 scorecard excellence signals; updated aspirational denominator from 33 to 35; added R13 signal note to C-37 documenting its emergence as the leading differentiator between perfect and near-perfect outputs |
