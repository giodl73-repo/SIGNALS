Written to `simulations/quest/rubrics/review-design-rubric-v10-2026-03-14.md`.

---

**Three new aspirational criteria extracted from R10:**

**C-30 | BLOCK 2 Domain Expert Finding Coverage Symmetry (F-22)**
- Confirmed by: V-02 and V-03 scored 100 without it; V-01/V-04/V-05 carried it
- Pattern: coverage enforcement must be symmetric across all roster tiers. F-01 guards stock disciplines; F-22 extends the same class to domain experts. An expert committed in BLOCK 1.5 with no BLOCK 2 finding block is a silent gap that all prior F-codes miss.

**C-31 | BLOCK 3 Consensus Issue Column Content Completeness (F-23)**
- Confirmed by: V-01 and V-03 scored 100 without it; V-02/V-04/V-05 carried it
- Pattern: BLOCK 3 had halts on Type (F-14), Reviewers (F-15), and Synthesis/SPLIT (F-11) -- three of four columns. The Issue column was the last unguarded. F-23 closes the final gap: when N-1 of N columns have content gates, the remaining column is a systematic blind spot.

**C-32 | BLOCK 5 Amend Action Cell Content Completeness (F-24)**
- Confirmed by: V-01 and V-02 scored 100 without it; V-03/V-04/V-05 carried it
- Pattern: F-12/F-05/F-17 on BLOCK 5 are all satisfiable with a present but empty Action cell. F-24 enforces that the cell carries prescriptive content -- the third instance of the content-completeness-within-structural-presence pattern (F-11, F-19, F-24).

**Formula:** denominator 22 -> 25. Each aspirational criterion now worth ~0.4 pts. Score ceiling 100 preserved.
sent but empty Action cell. F-24 enforces that the
  Action cell carries prescriptive content (what to change), not just that it exists. Behavioral
  enforcement completes the amend mechanism only when it targets the prescriptive-content cell.

**Formula:** denominator 22 -> 25. Each aspirational criterion now worth ~0.4 pts. Score ceiling
100 preserved.

---

## Essential Criteria (60% weight -- pass or fail)

### C-01 | All 6 Stock Disciplines Present
- **Weight**: essential
- **Category**: format
- **Text**: Output contains finding blocks from all 6 stock discipline reviewers: Security,
  Performance, Scalability, Maintainability, UX, and Data/API (or equivalent canonical names).
  A missing discipline block is a structural omission -- the review surface is incomplete and no
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
  the same fields passes C-06 but fails C-20 -- table form is required.
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
  criterion.
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

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 25 * 10)
```

Note: aspirational denominator changed from 22 to 25 in v10 (added C-30, C-31, C-32).
Each aspirational criterion contributes ~0.4 points at full pass.

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
