Written to `simulations/quest/rubrics/review-design-rubric-v4-2026-03-14.md`.

---

**Changes from v3 to v4:**

**New criterion — C-15 | Roster Commitment Table Before Finding Generation**
The R3 scorecard named BLOCK 1.5 as a C-15 candidate. V-05 proved it: roster pre-commitment is a distinct enforcement tier from named halt conditions. C-14 is reactive (halt fires on detected absence). C-15 is proactive (roster locked before generation begins — omission is caught earlier, at the commitment stage). V-03 and V-04 scored 100 without it, so it is genuinely aspirational and not a gap in C-14.

**Refinements to existing criteria:**

- **C-13**: Added R3 signal line — V-01/V-02 result confirms C-13 and C-14 are orthogonal; neither mechanism substitutes for the other.
- **C-14**: Pass condition tightened ("a single missing F-ID on one block is sufficient to fail"); added R3 signal noting F-08 localizability and the identical 98.57 score for partial-coverage vs. no-coverage failures.

**Formula update:**
```
aspirational denominator: 7 -> 8
each criterion: ~1.43 pts -> 1.25 pts
```

The score ceiling of 100 is preserved — R4 needs all 8 aspirational criteria to reach it, meaning C-15 is now the new distinguishing gate between 98.75 and 100.
is traceable to a signal in the input design (e.g., "RBAC mentioned -> security
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
  before generation); the two criteria are independent.
- **R3 signal**: V-05 introduced BLOCK 1.5 as roster commitment before finding generation. V-03
  and V-04 scored 100 without it, confirming BLOCK 1.5 is additive quality, not required for
  C-14 pass. The pattern represents a new enforcement tier: proactive prevention versus reactive
  halt. A roster table locks the reviewer set before any generation occurs; no downstream F-ID
  can achieve earlier-stage detection.

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

Note: aspirational denominator changed from 7 to 8 in v4 (added C-15).
Each aspirational criterion contributes 1.25 points at full pass.

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

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric -- 9 criteria, 4E/3R/2A |
| v2 | 2026-03-14 | Added C-10 (structural columns) and C-11 (three-field expert trace) from R1 scorecard excellence signals; updated aspirational denominator from 2 to 4 |
| v3 | 2026-03-14 | Added C-12 (pyramid gate as lifecycle block), C-13 (expert trace table columns), and C-14 (named F-ID halt conditions) from R2 scorecard new_patterns; updated aspirational denominator from 4 to 7 |
| v4 | 2026-03-14 | Added C-15 (roster commitment table before finding generation) from R3 new_patterns; refined C-13 and C-14 with R3 orthogonality and localizability signals; updated aspirational denominator from 7 to 8 |
