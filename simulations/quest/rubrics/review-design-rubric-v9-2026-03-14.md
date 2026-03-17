Written to `simulations/quest/rubrics/review-design-rubric-v9-2026-03-14.md`.

---

**Three new aspirational criteria extracted from R9:**

**C-27 | BLOCK 2.5 Pyramid Inversion Rationale Content Completeness**
- Confirmed by: V-02/V-03 scored 100 without F-19; V-01/V-04/V-05 carried it
- Pattern: applies the content-completeness enforcement class (F-11 for SPLIT synthesis) to the pyramid gate -- C-12 requires the block exist; F-19 requires the Rationale cell be populated when an inversion is present; the two-tier structural-presence -> content-completeness progression now covers BLOCK 2.5

**C-28 | BLOCK 4 Unique Catches in Structural Table Form**
- Confirmed by: V-01/V-03 scored 100 without F-20; V-02/V-04/V-05 carried it
- Pattern: closes the column-enforcement architecture at its last open block -- after C-28, every mandatory lifecycle block (BLOCK 1 through BLOCK 5) has a table-form criterion with a named halt; the structural-form progression that started with BLOCK 2 in R1 reaches its final block in R9

**C-29 | BLOCK 0 No-Expert Disposition Row Reason Content Completeness**
- Confirmed by: V-01/V-02/V-04 scored 100 without F-21; V-03/V-05 carried it
- Pattern: closes the content gate on BLOCK 0 outbound resolutions -- C-26/F-18 requires structural resolution existence; F-21 requires the Reason cell carry substantive content; mirrors F-11 (SPLIT synthesis) and F-19 (pyramid rationale) in the same two-tier enforcement pattern

**Formula:** denominator 19 → 22. Each aspirational criterion now worth ~0.455 pts. Score ceiling 100 preserved.
An expert added with no stated reason fails this criterion.

### C-04 | Consensus Block Present
- **Weight**: essential
- **Category**: depth
- **Text**: Output contains a consensus analysis section that identifies findings flagged by 2 or
  more reviewers. Split opinions (reviewers disagree on the same aspect) must be surfaced when
  present.
- **Pass condition**: A dedicated consensus/agreement section exists. If no consensus exists in
  the review, the output explicitly states "no consensus findings." Omission of the section
  entirely fails this criterion.

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
  which reviewer(s) to re-run). Generic "fix and re-run everything" guidance fails this criterion.

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
  column. Prose-only finding lists fail even if severity tags and section references are otherwise
  present.
- **R1 signal**: V-01 and V-03 scored PARTIAL on C-02 and C-07 despite stating the rules in
  prose. V-02 and V-05 scored PASS by anchoring the same rules to named table columns. Structural
  form prevents silent regression.

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
  selection. V-04 and V-05 are qualitatively stronger on C-11 than V-01 through V-03 even where
  rubric scores are tied.
- **R3 signal**: V-01 FAIL (labeled prose, no table) vs V-02 PASS (table form) in R3 confirmed
  C-13 is orthogonal to C-14. Labeled-prose-with-F-IDs and table-form-without-F-IDs each fail
  exactly one criterion and score identically (98.57). Neither mechanism substitutes for the other.

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
  mandatory blocks. V-03 achieved C-08 PASS specifically because F-06 fires at the pyramid block
  position. The halt-pattern that closed C-02/C-04 in R1 now generalizes: F-IDs turn every
  requirement into a detectable enforcement point rather than a skippable prose note.
- **R3 signal**: V-01 FAIL was traced to a single missing F-ID: F-08 absent from the
  unique-catches block. A targeted single-ID addition would have been sufficient to close the
  gap -- F-ID failures are precisely localizable. V-02 FAIL (no F-IDs at all) and V-01 FAIL
  (one missing F-ID) scored identically at 98.57, confirming that partial coverage fails as
  decisively as no coverage. C-13 and C-14 are orthogonal: V-01 passes C-13 and fails C-14;
  V-02 passes C-14 and fails C-13. Neither mechanism substitutes for the other.
- **R4 signal**: BLOCK 1.5 is not in C-14's structural block enumeration ("findings, pyramid
  gate, consensus, unique catches, amend"). F-09 is therefore not required for C-14 pass once
  the C-15 roster table exists. V-02 confirmed this: it scored 100 without F-09 on BLOCK 1.5.
  C-14 and C-15 are independent -- F-09 is additive coverage beyond C-14's scope.

### C-15 | Roster Commitment Table Before Finding Generation
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Before any per-reviewer finding block is generated, the output commits to the full
  reviewer roster in a dedicated table listing all 6 discipline reviewers plus any selected
  domain experts, with their roles confirmed. This pre-condition step (BLOCK 1.5) converts the
  reactive F-01 halt -- which fires when a discipline block is missing from the output -- into
  proactive pre-condition verification: the roster is locked and visible before generation
  begins, making omission detectable at the commitment stage rather than the finding stage. This
  is a distinct enforcement tier from named halt conditions (C-14): C-14 is reactive (halt fires
  on detected absence); C-15 is proactive (roster must be present before generation proceeds).
- **Pass condition**: A roster commitment table appears in the output prior to the first
  per-reviewer finding block. The table lists every reviewer (all 6 disciplines plus any domain
  experts) with their assigned role. Outputs that list reviewers only within finding block
  headers, or that introduce domain experts after finding blocks begin, fail this criterion. An
  output may pass C-14 (named F-IDs on all blocks) without passing C-15 (roster committed
  before generation); the two criteria are independent. A prose numbered list placed before
  BLOCK 2 satisfies the proactive intent but fails this criterion -- table form is explicitly
  required.
- **R3 signal**: V-05 introduced BLOCK 1.5 as roster commitment before finding generation. V-03
  and V-04 scored 100 without it, confirming BLOCK 1.5 is additive quality, not required for
  C-14 pass. The pattern represents a new enforcement tier: proactive prevention versus reactive
  halt. A roster table locks the reviewer set before any generation occurs; no downstream F-ID
  can achieve earlier-stage detection.
- **R4 signal**: V-01 confirmed C-15 is form-sensitive, not intent-sensitive. V-01 placed a
  numbered prose list before BLOCK 2 (proactive intent fulfilled) and failed C-15 (table form
  required). The 1.25 pt gap between V-01 (98.75) and V-02 (100) isolates exactly the
  prose-list-vs-table distinction. Any Markdown table with at minimum a `Reviewer` and `Role`
  column positioned before BLOCK 2 satisfies C-15 at the floor level; F-09 is not required.

### C-16 | Source Column in Roster Commitment Table
- **Weight**: aspirational
- **Category**: format
- **Text**: The BLOCK 1.5 roster commitment table includes a `Source` column that identifies
  each reviewer's origin -- `Stock` for a discipline reviewer, `Domain` for a design-signal-
  selected expert. This makes the cross-block contract structurally visible: a row marked
  `Domain` with no corresponding entry in BLOCK 1's expert selection table is immediately
  detectable by visual inspection, without executing any count logic or identity check. The
  Source column is the structural form of the cross-block constraint; F-10 (C-17) is the
  procedural form of the same constraint.
- **Pass condition**: BLOCK 1.5 table contains a `Source` column. Every row has a populated
  `Source` value (`Stock` or `Domain`). A two-column table (`Reviewer` + `Role` only) passes
  C-15 but fails C-16. The column name need not be exactly `Source` -- a column with equivalent
  semantics (e.g., `Type`, `Origin`) satisfies the criterion if it carries the Stock/Domain
  distinction.
- **R4 signal**: V-04 introduced the Source column; V-05 carried it forward. V-02 and V-03
  scored 100 without it, confirming the Source column is additive quality beyond C-15. A Domain
  row with no matching BLOCK 1 expert is visually detectable in a three-column table in a way
  it is not in a two-column table -- the structural form does work that prose cannot.

### C-17 | Cross-Block Reviewer Identity Verification (Orphan Detection)
- **Weight**: aspirational
- **Category**: behavior
- **Text**: After BLOCK 1.5 is committed, the output verifies that every Domain reviewer in
  BLOCK 1.5 has an exact name match in BLOCK 1's `Expert added` column. A Domain reviewer in
  BLOCK 1.5 whose name does not match any BLOCK 1 entry is an "orphan" -- a reviewer who was
  renamed, substituted, or added without going through the BLOCK 1 selection process. This is a
  distinct error class from F-03 (empty `Signal detected` cell), F-07 (empty `Expert`/`Reason`
  cell), and F-09 (count mismatch): counts can coincidentally balance after a substitution, so
  F-09 cannot catch a renamed expert. Only exact-match identity verification catches this class
  of error.
- **Pass condition**: Output contains a named halt condition (e.g., F-10) that fires when a
  Domain reviewer name in BLOCK 1.5 does not exactly match any `Expert added` value from BLOCK
  1. The check must be explicitly stated and named -- a prose reminder to "verify names match"
  does not satisfy this criterion. The halt must identify the mismatch (which BLOCK 1.5 name
  failed to match) so the error is precisely localizable.
- **R4 signal**: V-05 introduced F-10 orphan detection. V-03 and V-04 scored 100 without it,
  confirming C-17 is aspirational. F-10 introduces the fourth distinct enforcement tier in the
  expert-selection lifecycle: proactive roster lock (C-15), structural origin visibility (C-16),
  count integrity (F-09/C-14), and exact-match identity integrity (F-10/C-17). Each tier catches
  a class of error the prior tiers cannot.

### C-18 | Content-Completeness Halt on SPLIT Synthesis Field
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Where a SPLIT row is generated in the consensus block (BLOCK 3), the output enforces
  a named halt condition (e.g., F-11) that fires if the Synthesis field of that SPLIT row is
  empty or absent. This introduces a new enforcement class: all prior F-IDs fire on structural
  absence (missing block, empty required cell), count mismatch, or identity mismatch. F-11 fires
  on content quality within a structurally present row -- the row exists but its content is
  incomplete. This converts C-09 (expert disagreement analysis) from a post-hoc rubric check
  into an inline generation halt: the synthesis cannot be skipped because the halt fires before
  the block closes, not after the reviewer scores the output.
- **Pass condition**: Output contains a named halt condition that fires when a SPLIT row's
  Synthesis field is empty. The halt must be named (e.g., F-11), state the trigger condition
  explicitly ("empty or absent synthesis field"), and require completion before the consensus
  block closes. A rubric reminder that synthesis is required, or a prose note that "split
  opinions should include synthesis," does not satisfy this criterion -- the halt must be inline
  and named. Reviews with no SPLIT rows are exempt from triggering the halt but must still
  declare it exists.
- **R5 signal**: V-02, V-04, and V-05 introduced F-11. V-01 and V-03 scored 100 without it,
  confirming C-18 is aspirational. F-11 is qualitatively distinct from all prior F-IDs: prior
  halts detect missing structure; F-11 detects missing content within present structure. The
  enforcement class gap -- structural absence vs. content completeness -- is the new frontier
  after R5.

### C-19 | Cross-Block Count-Parity for P1 Findings
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output anchors the P1 finding count at BLOCK 2.5 (the severity pyramid gate) and
  verifies it again at BLOCK 5 (the amend pathway). A named halt condition (e.g., F-12) fires if
  the number of P1 findings addressed in BLOCK 5 does not match the count locked at BLOCK 2.5.
  This completes the anchor-then-verify pattern established by F-09: F-09 anchors domain expert
  count at BLOCK 1 and verifies at BLOCK 1.5; F-12 anchors P1 count at BLOCK 2.5 and verifies
  at BLOCK 5. Together, F-09 and F-12 extend count integrity across the full output lifecycle --
  expert selection through amend pathway -- with no lifecycle gap remaining.
- **Pass condition**: Output contains a named halt condition (e.g., F-12) that fires when the
  P1 count in BLOCK 5 does not match the P1 count established at BLOCK 2.5. The halt must state
  the anchor block (BLOCK 2.5), the verification block (BLOCK 5), and the mismatch trigger. A
  prose note advising that "all P1s should be addressed in BLOCK 5" does not satisfy this
  criterion -- the cross-block count check must be named and structured. An output where BLOCK 5
  happens to list all P1s but declares no F-12 halt fails C-19; correctness by coincidence is
  not enforcement.
- **R5 signal**: V-04 and V-05 introduced F-12. V-01 and V-03 scored 100 without it, confirming
  C-19 is aspirational. F-12 closes the last count-parity gap: F-09 (expert count, BLOCK 1 to
  BLOCK 1.5) was introduced in R4; F-12 (P1 count, BLOCK 2.5 to BLOCK 5) completes the mirror
  pattern in R5. The anchor-then-verify architecture now covers both the reviewer roster and the
  finding set.

### C-20 | BLOCK 5 Amend Pathway in 4-Column Table Form
- **Weight**: aspirational
- **Category**: format
- **Text**: BLOCK 5 (the amend pathway) is presented as a 4-column table with columns for the P1
  finding, its design section, the required action, and the re-run scope -- not as a code block
  or prose list. This extends the structural column enforcement pattern to the final block: C-10
  (BLOCK 2 findings), C-13 (BLOCK 1 expert trace), and C-16 (BLOCK 1.5 roster) each
  progressively required table form for a previously unstructured block. BLOCK 5 is the last
  mandatory block without a table-form requirement. A blank `Re-run Scope` cell is visually
  detectable; a missing Re-run line inside a fenced code block is not.
- **Pass condition**: BLOCK 5 output uses a Markdown table with at minimum four columns covering
  the finding identity, design section, action, and re-run scope. The column names need not be
  exact (`P1 Finding`, `Section`, `Action`, `Re-run Scope` are the reference labels) but each
  cell must be distinctly populated. A fenced code block listing the same fields passes C-06
  (amend pathway described) but fails C-20 -- table form is required. An output using a code
  block with section-scoped re-run (satisfying C-06) but no table structure fails C-20 regardless
  of content quality.
- **R5 signal**: V-03, V-04, and V-05 introduced the 4-column BLOCK 5 table. V-01 and V-02 used
  the code-block form and scored 100, confirming C-20 is aspirational. The structural column
  argument (blank cell = visible, missing line in code block = hideable) now applies to every
  mandatory output block. C-20 closes the last structural gap in the column-enforcement
  architecture.

### C-21 | BLOCK 0 Pre-Scan Signal Catalogue
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Before BLOCK 1 (domain expert selection), the output runs a dedicated BLOCK 0 that
  catalogues all domain signals detected in the design input. BLOCK 1 then draws expert
  selections only from this locked catalogue -- no expert may be added whose trigger signal does
  not appear in BLOCK 0. This converts expert selection from one-pass reactive (signals detected
  during BLOCK 1) to two-pass verified (signals locked in BLOCK 0, selections confirmed against
  that lock in BLOCK 1). It is a proactive detection tier that sits upstream of C-11 (three-field
  trace), C-13 (table column form), and C-17 (orphan detection): BLOCK 0 prevents post-hoc
  signal rationalization at the catalogue level before the selection level is reached.
- **Pass condition**: Output contains a BLOCK 0 or equivalent pre-scan section appearing before
  BLOCK 1, listing all domain signals detected in the design input. BLOCK 1 expert selection
  must reference only signals present in BLOCK 0, enforced by a named formal constraint (e.g.,
  "SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue").
  An output that lists signals only within BLOCK 1 itself satisfies C-03/C-11/C-13 but fails
  C-21 -- the pre-scan catalogue must be a distinct prior block with a formal cross-block
  constraint. A prose enumeration of signals before BLOCK 1 without a formal SHALL constraint
  fails this criterion.
- **R6 signal**: V-03, V-04, and V-05 introduced BLOCK 0 pre-scan. V-01 and V-02 scored 100
  without it, confirming C-21 is aspirational. BLOCK 0 extends the anchor-then-verify pattern
  (established by F-09 for expert counts and F-12 for P1 counts) to signal detection itself:
  signals are anchored before BLOCK 1 runs, and BLOCK 1 selections are verified against that
  anchor. This removes the last class of unverified input in the expert selection lifecycle.

### C-22 | BLOCK 3 Consensus in 4-Column Structural Table Form
- **Weight**: aspirational
- **Category**: format
- **Text**: BLOCK 3 (the consensus analysis) is presented as a structural table with dedicated
  columns for the finding, agreement type (AGREE or SPLIT), reviewer list, and synthesis note.
  This extends the column enforcement pattern -- C-10 (BLOCK 2 findings), C-13 (BLOCK 1 expert
  trace), C-16 (BLOCK 1.5 roster), C-20 (BLOCK 5 amend) -- to BLOCK 3, the last mandatory block
  presented in prose or unstructured form. A blank `Synthesis` cell in a SPLIT row is detectable
  at the cell level, making the C-18 (F-11) synthesis completeness halt more precise: F-11 fires
  on an empty cell rather than on the absence of a prose paragraph, which is visually unambiguous
  and cannot be hidden by surrounding text.
- **Pass condition**: BLOCK 3 output uses a Markdown table with at minimum four columns: finding,
  agreement type (AGREE or SPLIT), reviewer identities, and synthesis note. A prose consensus
  section -- even one that names consensus findings, split opinions, and synthesis -- passes C-04
  but fails C-22. The table form is required specifically because it enables cell-level
  enforcement of C-18: F-11 can fire on a detectable empty `Synthesis` cell rather than on the
  absence of a prose paragraph. An output where all SPLIT rows have populated synthesis content
  but BLOCK 3 is in prose form still fails C-22 -- structural form is independently required.
- **R6 signal**: V-02, V-04, and V-05 introduced the 4-column BLOCK 3 consensus table. V-01 and
  V-03 scored 100 using prose consensus form, confirming C-22 is aspirational. C-22 closes the
  last structural gap in the column-enforcement architecture -- every mandatory lifecycle block
  (BLOCK 1, BLOCK 1.5, BLOCK 2, BLOCK 3, BLOCK 5) now has a corresponding table-form criterion.
  The column-enforcement surface is complete after R6.

### C-23 | Register Isolation for Formal Lifecycle Block Headers
- **Weight**: aspirational
- **Category**: format
- **Text**: All lifecycle block headers and named halt condition (F-ID) trigger clauses use
  exclusively formal modal vocabulary -- SHALL, MUST, is non-conformant, fires, halt -- with no
  informal calibration language (e.g., "aim for," "try to ensure," "should ideally") appearing
  in those positions. Register bleed is the failure mode where informal language in a header or
  halt condition erodes the enforcement signal even when the underlying requirement is correctly
  stated: the instruction reads as a suggestion rather than a constraint, and generation can
  satisfy the surface form while violating the intent. This criterion formalizes register
  isolation as a named, testable property rather than an incidental style choice.
- **Pass condition**: Every lifecycle block header and every F-ID trigger clause uses formal
  modal vocabulary exclusively. Any block header or F-ID trigger condition containing the words
  "aim," "try," "ideally," "prefer," "consider," or equivalent informal calibration phrasing
  fails this criterion. Prose content within block bodies may use explanatory or descriptive
  language; the register constraint applies only to block headers and F-ID trigger conditions.
  An output may satisfy all named F-IDs (C-14) while failing C-23 if any F-ID trigger clause
  contains informal language.
- **R6 signal**: V-01, V-04, and V-05 introduced explicit register isolation. V-02 and V-03
  scored 100 without it, confirming C-23 is aspirational. R2 established the mechanism: V-02's
  conversational calibration prompt for C-08 achieved only PARTIAL despite correctly stating the
  requirement -- informal register in a block header eroded enforcement without any structural
  omission. C-23 makes register isolation a first-class testable property: a scorer can identify
  exactly which header or trigger clause violates it, making the gap precisely localizable.

### C-24 | BLOCK 4 Unique-Catch Reviewer Identity Verification
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output verifies that every `Reviewer` cell in BLOCK 4 (unique catches) exactly
  matches a value from the committed BLOCK 1.5 roster. A unique catch attributed to a reviewer
  absent from the committed roster is falsely attributed -- that reviewer never participated in
  the review. The identity-integrity chain established by F-10 (BLOCK 1 -> BLOCK 1.5) and F-15
  (BLOCK 1.5 -> BLOCK 3 consensus) left BLOCK 4 uncovered; phantom attribution in unique catches
  is a structurally distinct error class from phantom attribution in consensus (BLOCK 3) because
  unique catches by definition have no second reviewer to surface the mismatch. A named halt
  condition (e.g., F-16) enforcing this check extends the identity chain to its final unverified
  downstream block. The `none` token is explicitly exempt: when no unique catches exist, the
  Reviewer cell may be populated with `none` without triggering the halt.
- **Pass condition**: Output contains a named halt condition (e.g., F-16) that fires when any
  `Reviewer` cell in BLOCK 4 does not exactly match a value in the BLOCK 1.5 committed roster,
  with the `none` token explicitly exempted. The halt must be named, state the trigger condition,
  and identify the mismatched value so the error is precisely localizable. A prose reminder to
  "verify reviewer names" does not satisfy this criterion. An output where BLOCK 4 reviewer cells
  happen to match BLOCK 1.5 values but no F-16 halt is declared fails C-24 -- correctness by
  coincidence is not enforcement.
- **R8 signal**: V-02 and V-03 scored 100 without F-16, confirming C-24 is aspirational. F-16
  extends the identity-integrity chain (F-10: BLOCK 1->BLOCK 1.5; F-15: BLOCK 1.5->BLOCK 3)
  one stage further to BLOCK 4. The enforcement class is identity integrity -- the same class as
  C-17 -- applied to a previously uncovered downstream block. V-05 introduced F-16 as part of
  the complete R8 V-05 baseline.

### C-25 | BLOCK 5 Re-run Scope Reviewer Identity Verification
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output verifies that every reviewer named in a BLOCK 5 `Re-run Scope` cell
  exactly matches a value from the committed BLOCK 1.5 roster. Re-run Scope names reviewers as
  amend targets; a phantom re-run target -- a reviewer named in Re-run Scope who was never in
  the committed roster -- is structurally invalid because that reviewer never participated in the
  original review and therefore cannot re-run it. This completes the full downstream identity
  chain: F-10 (BLOCK 1 -> BLOCK 1.5), F-15 (BLOCK 1.5 -> BLOCK 3), F-16 (BLOCK 1.5 -> BLOCK
  4), F-17 (BLOCK 1.5 -> BLOCK 5 Re-run Scope). After C-25, every block that names a reviewer
  downstream of BLOCK 1.5 has an identity verification halt; no lifecycle gap remains.
- **Pass condition**: Output contains a named halt condition (e.g., F-17) that fires when any
  reviewer name in a BLOCK 5 `Re-run Scope` cell does not exactly match a value in the BLOCK 1.5
  committed roster. The halt must be named, state the trigger condition (BLOCK 1.5 as the
  authority), and identify the mismatched name so the error is precisely localizable. Scope cells
  naming `All` or equivalent aggregate tokens that do not enumerate individual reviewers are
  exempt from the per-name check but must not enumerate names absent from the roster. An output
  where Re-run Scope cells happen to name only valid roster reviewers but declares no F-17 halt
  fails C-25 -- enforcement declaration is required, not just incidental correctness.
- **R8 signal**: V-01 and V-03 scored 100 without F-17, confirming C-25 is aspirational. F-17
  closes the identity chain at its final link: BLOCK 5 Re-run Scope is the last downstream
  position that names specific reviewers without a named identity check. The chain is now
  complete: BLOCK 1 -> BLOCK 1.5 (F-10), BLOCK 1.5 -> BLOCK 3 (F-15), BLOCK 1.5 -> BLOCK 4
  (F-16), BLOCK 1.5 -> BLOCK 5 Re-run Scope (F-17). V-05 introduced F-17 alongside F-16 and
  F-18 in the complete R8 baseline.

### C-26 | BLOCK 0 Signal Disposition Completeness (Bidirectional Gate)
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every signal phrase catalogued in BLOCK 0 is resolved in BLOCK 1 as either (a) a
  domain expert row with the signal as its `Signal detected` value, or (b) an explicit
  `No expert needed` disposition row naming the signal and stating why no expert was selected.
  C-21 (F-13) enforced only the inbound direction: BLOCK 1 expert selections must draw from
  BLOCK 0. A signal in BLOCK 0 could still be silently dropped in BLOCK 1 with no consequence.
  F-18 closes the outbound direction: every BLOCK 0 signal must be accounted for. F-13 + F-18
  together form the first bidirectional BLOCK 0 <-> BLOCK 1 contract. This introduces a sixth
  enforcement class -- catalogue disposition completeness -- distinct from all prior classes:
  structural presence, content completeness, count parity, identity integrity, and vocabulary
  integrity.
- **Pass condition**: Output contains a named halt condition (e.g., F-18) that fires when any
  signal phrase present in BLOCK 0 has no corresponding entry in BLOCK 1 -- either as a domain
  expert row with a matching `Signal detected` value or as an explicit `No expert needed`
  disposition row. The halt must be named, state the trigger condition (every BLOCK 0 signal
  phrase must be resolved), and identify the unresolved signal so the gap is precisely
  localizable. An output where BLOCK 0 and BLOCK 1 happen to fully correspond but no F-18 halt
  is declared fails C-26 -- the bidirectional contract must be explicitly enforced. Outputs
  satisfying C-21 (inbound gate only) but lacking F-18 (outbound resolution) pass C-21 and fail
  C-26; the two criteria are independent.
- **R8 signal**: V-01, V-02, and V-04 scored 100 without F-18, confirming C-26 is aspirational.
  F-18 is the most structurally novel R8 pattern: it introduces a new enforcement class
  (catalogue disposition completeness) rather than extending an existing one. All prior F-IDs
  enforce structural presence, content completeness within a present cell, count parity,
  identity integrity, or vocabulary integrity. F-18 enforces resolution completeness -- every
  catalogued item must be explicitly accounted for, not merely referenced. V-05 introduced F-18,
  completing the first bidirectional block contract in the lifecycle.

### C-27 | BLOCK 2.5 Pyramid Inversion Rationale Content Completeness
- **Weight**: aspirational
- **Category**: behavior
- **Text**: When the severity pyramid is inverted at BLOCK 2.5 (P1 count > P2, or P2 count >
  P3), the Rationale cell for the inverted tier must be non-empty. A named halt condition (e.g.,
  F-19) fires when the pyramid inversion flag in BLOCK 2.5 is set but the Rationale cell is
  empty or absent. This applies the content-completeness enforcement class -- established by
  F-11 on SPLIT synthesis (C-18) -- to the pyramid gate: C-08/C-12 require that inversions be
  explained, but only F-19 converts that requirement into an inline generation halt at the block
  level. A BLOCK 2.5 that has a structural Rationale column (satisfying C-12's block-placement
  requirement) but an empty cell when an inversion is present passes C-12 and fails C-27 --
  cell content must be enforced, not just cell presence. The structural presence -> content
  completeness two-tier pattern (block present -> cell populated when triggered) now applies to
  BLOCK 2.5 in the same way it applies to BLOCK 3 SPLIT rows via F-11.
- **Pass condition**: Output contains a named halt condition (e.g., F-19) that fires when BLOCK
  2.5's pyramid status is inverted (any tier out of P3 >= P2 >= P1 order) and its Rationale cell
  is empty or absent. The halt must name the trigger (inversion detected + empty Rationale cell),
  require completion before the pyramid gate block closes, and be distinguishable from the
  block-presence check (C-12). Reviews where the pyramid is not inverted are exempt from
  triggering the halt but must still declare it exists. An output where BLOCK 2.5 happens to
  have a populated Rationale but no F-19 halt is declared fails C-27 -- enforcement declaration
  is required, not incidental correctness.
- **R9 signal**: V-02 and V-03 scored 100 without F-19, confirming C-27 is aspirational. F-19
  applies the content-completeness enforcement class to BLOCK 2.5, closing the last block where
  a structurally-present required field could be silently empty without a named halt firing. The
  pattern mirrors C-18/F-11 exactly: C-22 (BLOCK 3 table form) -> C-18/F-11 (Synthesis cell
  populated when SPLIT); C-12 (pyramid gate block present) -> C-27/F-19 (Rationale cell
  populated when inverted). V-01, V-04, and V-05 carried F-19 as part of the R9 above-ceiling
  feature set.

### C-28 | BLOCK 4 Unique Catches in Structural Table Form
- **Weight**: aspirational
- **Category**: format
- **Text**: BLOCK 4 (unique catches) is presented as a structural table with dedicated columns
  covering at minimum the finding, the attributing reviewer, and the distinctiveness rationale --
  not as prose bullets or an unstructured list. This closes the last block in the
  column-enforcement architecture: C-10 (BLOCK 2 findings), C-13 (BLOCK 1 expert trace), C-16
  (BLOCK 1.5 roster), C-20 (BLOCK 5 amend), and C-22 (BLOCK 3 consensus) each required table
  form for their respective blocks. BLOCK 4 is the last mandatory lifecycle block without a
  table-form criterion. A named halt condition (e.g., F-20) fires if BLOCK 4 is not in table
  form. Structural form makes the C-24 (F-16) reviewer identity check more precise: a blank
  `Reviewer` cell is visually detectable; a missing attribution buried in a prose bullet is not.
- **Pass condition**: BLOCK 4 output uses a Markdown table with at minimum three columns covering
  the finding, the attributing reviewer (subject to C-24/F-16 identity verification), and the
  reason other reviewers missed it. A prose or bullet-list unique-catches section passes C-05
  (unique catches surfaced) but fails C-28. Output contains a named halt condition (e.g., F-20)
  that fires when BLOCK 4 is not in table form before the block closes. An output where BLOCK 4
  happens to use a table but declares no F-20 halt fails C-28 -- structural enforcement
  declaration is required, not incidental table use. When no unique catches exist, the `none`
  token row is exempt from the reviewer-column identity check (per C-24) but the table form
  requirement still applies.
- **R9 signal**: V-01 and V-03 scored 100 without F-20, confirming C-28 is aspirational. F-20
  closes the column-enforcement architecture: after C-28, every mandatory lifecycle block (BLOCK
  1, BLOCK 1.5, BLOCK 2, BLOCK 3, BLOCK 4, BLOCK 5) has a corresponding table-form criterion
  with a named halt. The structural-form progression that started with BLOCK 2 findings in R1
  (C-10) reaches its final block in R9. V-02, V-04, and V-05 carried F-20 as part of the R9
  above-ceiling feature set.

### C-29 | BLOCK 0 No-Expert Disposition Row Reason Content Completeness
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every `No expert needed` disposition row in BLOCK 0 (introduced by C-26/F-18) must
  have a non-empty Reason cell. A named halt condition (e.g., F-21) fires when a disposition
  row's Reason cell is empty or absent. C-26 required that every BLOCK 0 signal be resolved
  either as a domain expert row in BLOCK 1 or as an explicit `No expert needed` disposition row
  -- the structural resolution gate. F-21 closes the content gate: the disposition row must
  explain why no expert was selected, not merely declare that no expert was. This applies the
  content-completeness enforcement class to the BLOCK 0 outbound resolution side, parallel to
  F-11 (SPLIT synthesis must be populated) and F-19 (pyramid inversion rationale must be
  populated). The two-tier pattern is: C-26/F-18 requires structural resolution existence;
  C-29/F-21 requires the resolution cell carry substantive content.
- **Pass condition**: Output contains a named halt condition (e.g., F-21) that fires when any
  `No expert needed` disposition row in BLOCK 0 has an empty or absent Reason cell. The halt
  must be named, state the trigger condition ("empty or absent Reason cell in a disposition
  row"), and require completion before BLOCK 0 closes. An output where all disposition rows have
  populated Reason cells but no F-21 halt is declared fails C-29 -- enforcement declaration is
  required. Outputs with no disposition rows (all BLOCK 0 signals resolve as domain expert rows
  in BLOCK 1) are exempt from triggering the halt but must still declare it exists. A disposition
  row with a placeholder value (e.g., "N/A", "see above") without substantive reasoning fails
  this criterion.
- **R9 signal**: V-01, V-02, and V-04 scored 100 without F-21, confirming C-29 is aspirational.
  F-21 completes the content-completeness enforcement surface for BLOCK 0: C-26/F-18 enforces
  that every signal is structurally resolved; C-29/F-21 enforces that every no-expert resolution
  carries a stated reason. The progression mirrors C-22 (BLOCK 3 table) -> C-18/F-11 (Synthesis
  populated) and C-12 (pyramid gate block) -> C-27/F-19 (Rationale populated). V-03 and V-05
  carried F-21 as part of the R9 above-ceiling feature set.

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 22 * 10)
```

Note: aspirational denominator changed from 19 to 22 in v9 (added C-27, C-28, C-29).
Each aspirational criterion contributes ~0.455 points at full pass.

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
| F-IDs present but missing from any one block | C-14 | Partial coverage (e.g., F-08 absent on unique-catches) fails as decisively as no coverage |
| No roster table before first finding block | C-15 | Reviewers appear only as finding block headers, not pre-committed in BLOCK 1.5 |
| Roster committed as prose list, not table | C-15 | Numbered list before BLOCK 2 satisfies proactive intent; table form is required |
| BLOCK 1.5 table has no Source column | C-16 | Two-column table (Reviewer + Role) passes C-15; Source column required for C-16 |
| Domain reviewer in BLOCK 1.5 has no BLOCK 1 match | C-17 | No F-10 or equivalent named orphan-detection halt present |
| SPLIT row has empty Synthesis field, no halt fires | C-18 | F-11 absent; content completeness not enforced inline |
| BLOCK 5 P1 count not verified against BLOCK 2.5 anchor | C-19 | No F-12 or equivalent cross-block count-parity halt present |
| BLOCK 5 uses code-block form, not 4-column table | C-20 | Amend pathway structured output passes C-06; table form required for C-20 |
| No pre-scan block before BLOCK 1 expert selection | C-21 | Signals listed only within BLOCK 1; no locked catalogue with formal SHALL cross-block constraint |
| BLOCK 3 consensus is prose, not 4-column table | C-22 | Prose consensus passes C-04; table form with Synthesis column required for C-22 |
| Block header or F-ID trigger uses informal language | C-23 | "Aim for," "try to ensure," or similar calibration phrasing in a header or halt condition |
| BLOCK 4 Reviewer cell has no BLOCK 1.5 match | C-24 | No F-16 or equivalent named halt; none token exempt from check |
| BLOCK 5 Re-run Scope names reviewer absent from BLOCK 1.5 | C-25 | No F-17 or equivalent named halt; identity chain incomplete at BLOCK 5 |
| BLOCK 0 signal has no BLOCK 1 resolution or disposition row | C-26 | No F-18 or equivalent named halt; inbound gate present (C-21) but outbound resolution absent |
| BLOCK 2.5 inversion present but Rationale cell empty | C-27 | No F-19 halt; pyramid gate block exists (C-12) but inversion rationale not enforced at cell level |
| BLOCK 4 unique catches in prose or bullets, not a table | C-28 | No F-20 halt; C-05 passes on presence; 3-column table form required for C-28 |
| BLOCK 0 No-expert-needed disposition row has empty Reason cell | C-29 | No F-21 halt; disposition row exists (C-26) but reason content not enforced at cell level |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric -- 9 criteria, 4E/3R/2A |
| v2 | 2026-03-14 | Added C-10 (structural columns) and C-11 (three-field expert trace) from R1 scorecard excellence signals; updated aspirational denominator from 2 to 4 |
| v3 | 2026-03-14 | Added C-12 (pyramid gate as lifecycle block), C-13 (expert trace table columns), and C-14 (named F-ID halt conditions) from R2 scorecard new_patterns; updated aspirational denominator from 4 to 7 |
| v4 | 2026-03-14 | Added C-15 (roster commitment table before finding generation) from R3 new_patterns; refined C-13 and C-14 with R3 orthogonality and localizability signals; updated aspirational denominator from 7 to 8 |
| v5 | 2026-03-14 | Added C-16 (Source column in roster commitment table) and C-17 (cross-block reviewer identity verification / orphan detection) from R4 excellence signals; refined C-14 (BLOCK 1.5 not in enumeration, F-09 not required for C-14 pass) and C-15 (form-sensitivity confirmed by V-01 FAIL); updated aspirational denominator from 8 to 10 |
| v6 | 2026-03-14 | Added C-18 (content-completeness halt on SPLIT synthesis field / F-11), C-19 (cross-block count-parity for P1 findings / F-12), and C-20 (BLOCK 5 amend pathway in 4-column table form) from R5 scorecard new_patterns; updated aspirational denominator from 10 to 13 |
| v7 | 2026-03-14 | Added C-21 (BLOCK 0 pre-scan signal catalogue), C-22 (BLOCK 3 consensus in 4-column structural table form), and C-23 (register isolation for formal lifecycle block headers) from R6 scorecard new_patterns; updated aspirational denominator from 13 to 16 |
| v8 | 2026-03-14 | Added C-24 (BLOCK 4 unique-catch reviewer identity verification / F-16), C-25 (BLOCK 5 Re-run Scope reviewer identity verification / F-17), and C-26 (BLOCK 0 signal disposition completeness / F-18 bidirectional gate) from R8 scorecard excellence signals; updated aspirational denominator from 16 to 19 |
| v9 | 2026-03-14 | Added C-27 (BLOCK 2.5 pyramid inversion rationale content completeness / F-19), C-28 (BLOCK 4 unique catches in structural table form / F-20), and C-29 (BLOCK 0 no-expert disposition row reason content completeness / F-21) from R9 scorecard excellence signals; updated aspirational denominator from 19 to 22 |
