Written to `simulations/quest/rubrics/review-design-rubric-v6-2026-03-14.md`.

---

**v6 summary:**

Three new aspirational criteria from R5 `new_patterns`:

**C-18 | Content-Completeness Halt on SPLIT Synthesis Field** (F-11)
New enforcement class: prior F-IDs detect structural absence or count/identity mismatch; F-11 detects content quality within a present row. Converts C-09 from post-hoc rubric check to inline generation halt. V-01/V-03 scored 100 without it — aspirational confirmed.

**C-19 | Cross-Block Count-Parity for P1 Findings** (F-12)
Completes the anchor-then-verify pattern: F-09 covers expert count (BLOCK 1 -> BLOCK 1.5); F-12 covers P1 count (BLOCK 2.5 -> BLOCK 5). No lifecycle gap remains. V-01/V-03 scored 100 without it — aspirational confirmed.

**C-20 | BLOCK 5 Amend Pathway in 4-Column Table Form**
Extends structural column enforcement to the last uncovered block. C-10 (BLOCK 2), C-13 (BLOCK 1), C-16 (BLOCK 1.5), now C-20 (BLOCK 5). Blank `Re-run Scope` cell is detectable; missing line in code block is not. V-01/V-02 scored 100 in code-block form — aspirational confirmed.

**Formula:** denominator 10 -> 13. Each aspirational criterion now worth ~0.769 pts. Score ceiling 100 preserved.
rational

**C-20 | BLOCK 5 Amend Pathway in 4-Column Table Form** (from V-03/V-04/V-05)
- BLOCK 5 presented as a 4-column table: `P1 Finding | Section | Action | Re-run Scope`
- Extends the structural column enforcement pattern to the amend pathway: C-10 (BLOCK 2),
  C-13 (BLOCK 1 expert trace), C-16 (BLOCK 1.5 roster) — BLOCK 5 is the final uncovered block
- A blank `Re-run Scope` cell is visually detectable; a missing Re-run line in a code block is not
- V-01/V-02 scored 100 in code-block form — confirmed aspirational; table form is the next gate

**Formula:** aspirational denominator 10 -> 13, each criterion 1.0 -> ~0.769 pts. Score ceiling
100 preserved.

---

## Essential Criteria (60% weight -- must all pass)

### C-01 | All 6 Stock Disciplines Present
- **Weight**: essential
- **Category**: completeness
- **Text**: Output contains a per-reviewer block for each of the 6 stock disciplines: Architect,
  Code-Quality, Security, UX, Performance, and Reliability. Disciplines may be presented in any
  order but must each have a named finding block.
- **Pass condition**: All 6 discipline names appear as reviewer block headers. Fewer than 6 fails
  this criterion.

### C-02 | Severity Tag on Every Finding
- **Weight**: essential
- **Category**: format
- **Text**: Every finding in the output carries exactly one severity tag: P1, P2, or P3. No
  finding may be untagged or carry a freeform label.
- **Pass condition**: Every finding line or table row has a P1, P2, or P3 tag. A finding with no
  tag or a label outside P1/P2/P3 fails this criterion.

### C-03 | Domain Expert Auto-Selection Justified
- **Weight**: essential
- **Category**: behavior
- **Text**: At least one domain expert beyond the 6 stock disciplines is selected, and the
  selection is traceable to a signal in the input design (e.g., "RBAC mentioned -> security
  architect added").
- **Pass condition**: Output names 1+ domain expert and includes an explicit signal-to-expert
  mapping sentence or inline note. An expert added with no stated reason fails this criterion.

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

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 13 * 10)
```

Note: aspirational denominator changed from 10 to 13 in v6 (added C-18, C-19, C-20).
Each aspirational criterion contributes ~0.769 points at full pass.

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
