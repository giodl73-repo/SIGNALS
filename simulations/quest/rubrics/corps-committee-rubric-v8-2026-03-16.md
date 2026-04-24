```markdown
# corps-committee-rubric-v8-2026-03-16.md

## What changed from v7

**Three new aspirational criteria** sourced from R7 excellence signals. C-24 arrives from
V-01 (action-attribution traceability at the action-item level), C-25 from V-02 (explicit
inertia resolution accounting in Phase 5), and C-26 from V-03 (committee-type-aware outcome
vocabulary declared at Phase 0 and enforced through Phase 4). R7 V-05 integrates all three
simultaneously, becoming the first variation to earn all 19 aspirational criteria under v8.

### C-24 — Phase 5 Action-Attribution Linkage
ACTION ITEMS entries in Phase 5 carry a fourth `Origin:` field naming the participant token
or stance from the STANCE MANIFEST whose position generated the action (e.g., `Origin:
LEAD-ENG — opposed on grounds of timeline`). An ACTION ATTRIBUTION gate validates every
`Origin:` value against STANCE MANIFEST entries before PHASE-5-COMMIT. The commit line
includes `ACTION ATTRIBUTION validated` as an explicit terminal marker. R7 V-01 introduces
this pattern. It extends C-21's completeness-gate mechanism to the output layer — every
action item must trace to a named governance source, making untraceable action assignments
a structural defect rather than an attribution gap.

### C-25 — Phase 5 Inertia Resolution Summary Block
A `## INERTIA RESOLUTION SUMMARY` block appears in Phase 5 before PHASE-5-COMMIT. Each
inertia item token from Phase 1 must appear with either `Addressed by:` (citing the action
item or decision that resolves it) or `No action needed:` (with stated reason). A
`RESOLUTION RESULT:` field at the end of the block declares `COMPLETE` when all entries are
filled; only `COMPLETE` permits proceeding to PHASE-5-COMMIT. A seventh MINUTES INTEGRITY
CHECK checkbox confirms `RESOLUTION RESULT: COMPLETE`. R7 V-02 introduces this pattern. It
closes the structural loop opened by the INERTIA RECORD in Phase 1 — every inertia finding
must exit Phase 5 with an explicit disposition.

### C-26 — Phase 0 Committee-Type-Aware Outcome Vocabulary
Phase 0 header includes an `Outcome Vocabulary:` field declaring the set of valid verdict
terms for the declared Committee Type (e.g., `APPROVED / REJECTED / DEFERRED` for Budget
Approval; `PROCEED / HOLD / ESCALATE` for ROB). A third COMMITTEE TYPE GATE checkbox
confirms `Outcome Vocabulary:` is declared and non-empty before Phase 0 closes. A
`VOCABULARY CHECK` step in the Phase 4 TALLY LEDGER PROTOCOL validates that the tally
verdict uses exactly one term from the declared vocabulary set; a term outside the declared
set halts the tally. The Phase 5 `Verdict:` field must match the declared vocabulary. The
PHASE-4-COMMIT line includes `OUTCOME declared using Phase 0 vocabulary` as an explicit
marker. R7 V-03 introduces this pattern. It anchors verdict semantics to committee function
at declaration time — vocabulary drift between Phase 0 intent and Phase 5 output becomes a
structural defect.

---

## Scoring impact

Aspirational pool expands from 16-way to **19-way split** (≈0.526 pts each vs 0.625 pts in
v7). Only R7 V-05, which integrates all three new criteria, pays no redistribution penalty.

| Variation | Criteria earned | v7 score | v8 score | Δ |
|---|---|---|---|---|
| R6 V-01 / V-02 (C-23 absent) | 15/19 | 97.21 | **95.72** | −1.49 |
| R6 V-03 / V-04 / V-05 (all v7 criteria) | 16/19 | 97.83 | **96.25** | −1.58 |
| R7 V-01 (adds C-24; 17 of 19) | 17/19 | 97.83 | **96.78** | −1.05 |
| R7 V-02 (adds C-25; 17 of 19) | 17/19 | 97.83 | **96.78** | −1.05 |
| R7 V-03 (adds C-26; 17 of 19) | 17/19 | 97.83 | **96.78** | −1.05 |
| R7 V-04 (adds C-24 + C-25; 18 of 19) | 18/19 | 97.83 | **97.30** | −0.53 |
| R7 V-05 (adds C-24 + C-25 + C-26; all 19) | 19/19 | 97.83 | **97.83** | 0.00 |

R7 V-05 is the first variation to earn all 19 aspirational criteria. Under v8 it holds 97.83
uncontested; R7 V-04 follows at 97.30 (one criterion gap).

---

## Essential Criteria
> Output fails without these. A missing or broken essential criterion disqualifies the
> variation.

### C-01 — Typed Agenda Item Declaration
- **Weight**: essential
- **Category**: format
- **Text**: The output opens with an `Agenda Type:` line declaring the meeting category
  (e.g., `ROB`, `Quarterly Business Review`, `Budget Approval`) AND an `Agenda Item:`
  line naming the specific subject under review. Both lines appear before any phase
  content.
- **Pass condition**: Both `Agenda Type:` and `Agenda Item:` labels present at output
  open, in that order, before Phase 0 begins. `Agenda Type:` uses a recognized
  meeting-category term. `Agenda Item:` names a specific subject. Fails if either label
  is absent, unlabeled, or uses non-standard phrasing (e.g., `product review` instead
  of `ROB`).

### C-02 — Five-Phase Structure with Terminal Commits
- **Weight**: essential
- **Category**: structure
- **Text**: The output contains exactly six phase blocks labeled Phase 0 through Phase 5
  in ascending order. Each phase block closes with a `PHASE-N-COMMIT: [locked]` line as
  its terminal element. No content appears after a commit line within its own phase
  block.
- **Pass condition**: Phases 0–5 present in sequence. Each phase's final line matches
  `PHASE-N-COMMIT: [locked]`. No phase content follows its commit line. Fails if any
  phase is missing, out of order, or its commit line is not terminal.

### C-03 — Phase 1 Investigation Attempt Labeling
- **Weight**: essential
- **Category**: structure
- **Text**: Each investigation attempt in Phase 1 is introduced by a heading of the form
  `### INVESTIGATION-ATTEMPT-N` (N = 1, 2, …) before any findings content for that
  attempt. The label appears as a standalone heading line; finding entries follow below
  it.
- **Pass condition**: At least one `### INVESTIGATION-ATTEMPT-1` heading present in
  Phase 1 before any finding lines. Subsequent attempts labeled sequentially. Fails if
  findings appear without a preceding attempt heading or if the heading format deviates
  from the required pattern.

### C-04 — Phase 0 Committee Type Gate
- **Weight**: essential
- **Category**: structure
- **Text**: Phase 0 contains a `Committee Type:` field declaring the committee category
  (e.g., `Budget Approval`, `ROB`, `Design Review`). A `## COMMITTEE TYPE GATE` block
  follows with at least two checkboxes: (1) committee type is a recognized category,
  (2) agenda item is in-scope for that committee type. All boxes must be ticked before
  Phase 0 content is complete. The gate's halt declaration prevents Phase 1 from
  beginning if any checkbox is unticked.
- **Pass condition**: `Committee Type:` field present in Phase 0. `## COMMITTEE TYPE
  GATE` block present with checkbox list and halt declaration. All initial checkboxes
  ticked before PHASE-0-COMMIT. Fails if `Committee Type:` is absent, gate block is
  missing, halt declaration is omitted, or any checkbox is unticked at commit time.

### C-05 — Phase 2 Participant Position Block Labeling
- **Weight**: essential
- **Category**: structure
- **Text**: Each participant's position entry in Phase 2 is introduced by a labeled
  heading of the form `### POSITION-[PARTICIPANT-TOKEN]` before the stance and rationale
  content for that participant. Participant tokens must match tokens declared or
  discoverable from Phase 1 context.
- **Pass condition**: At least two `### POSITION-[TOKEN]` headings present in Phase 2,
  one per participant covered. Fails if participant positions appear unlabeled or if
  token format deviates from the required pattern.

### C-06 — Phase 3 Tally Block Presence
- **Weight**: essential
- **Category**: structure
- **Text**: Phase 3 contains a `## TALLY` block that enumerates all participant positions
  by stance category (support, oppose, abstain, conditional) with a running count. The
  tally concludes with a `TALLY RESULT:` line declaring the aggregate outcome (e.g.,
  `MAJORITY-SUPPORT`, `NO-CONSENSUS`).
- **Pass condition**: `## TALLY` block present in Phase 3. Participant positions
  enumerated by stance. `TALLY RESULT:` line present and non-empty. Fails if tally block
  is absent, participant positions are not enumerated, or `TALLY RESULT:` is missing.

### C-07 — Phase 5 Minutes Block Presence
- **Weight**: essential
- **Category**: structure
- **Text**: Phase 5 contains a `## MINUTES` block that includes at minimum: a `Verdict:`
  field, an `Attendees:` list, a `Key Discussion Points:` section, and an `Action
  Items:` section. The block must be present before PHASE-5-COMMIT.
- **Pass condition**: `## MINUTES` block with `Verdict:`, `Attendees:`, `Key Discussion
  Points:`, and `Action Items:` all present in Phase 5 before PHASE-5-COMMIT. Fails if
  the block or any required field is absent.

---

## Aspirational Criteria
> Graded on a 19-way split (≈0.526 pts each). Full score = 87.83 + 10.00 = 97.83.

### C-08 — INERTIA RECORD with One-Phrase Anchors
- **Weight**: aspirational
- **Category**: traceability
- **Text**: Phase 1 contains an `## INERTIA RECORD` block listing each blocking or
  impeding factor discovered during investigation. Each entry carries a unique token of
  the form `INERTIA-FINDING-[TOKEN]` and a one-phrase anchor summarizing the inertia
  in a single noun phrase (e.g., `INERTIA-FINDING-A: budget-ceiling constraint`). The
  record appears after all INVESTIGATION-ATTEMPT blocks and before PHASE-1-COMMIT.
- **Pass condition**: `## INERTIA RECORD` block present in Phase 1 after
  INVESTIGATION-ATTEMPT content. Each entry has a unique `INERTIA-FINDING-*` token and
  a one-phrase anchor. Fails if the block is absent, entries lack tokens, or anchors
  span multiple sentences.

### C-09 — INERTIA INVARIANT Declaration
- **Weight**: aspirational
- **Category**: traceability
- **Text**: The `## INERTIA RECORD` block closes with an `INERTIA INVARIANT:` line
  stating the total count of inertia findings and asserting that the count will not
  change after Phase 1 locks (e.g., `INERTIA INVARIANT: 4 findings locked at Phase 1.
  Count is immutable.`). The invariant must appear as the final line of the INERTIA
  RECORD block.
- **Pass condition**: `INERTIA INVARIANT:` line present as the final line of the INERTIA
  RECORD block. States a count and an immutability assertion. Fails if line is absent,
  count is missing, or line appears outside the INERTIA RECORD block.

### C-10 — PHASE-1-COMMIT Coupling Pair A
- **Weight**: aspirational
- **Category**: traceability
- **Text**: The PHASE-1-COMMIT carries a `COUPLING PAIR A:` annotation declaring both
  coupling directions: (A→) Phase 1 inertia findings will be cited in Phase 3 positions;
  (→A) Phase 3 positions must reference Phase 1 findings. Both directions are named
  explicitly on the commit line or in a `COUPLING PAIR A` block immediately following it.
- **Pass condition**: `COUPLING PAIR A` annotation or block present at or immediately
  after PHASE-1-COMMIT. Both (A→) forward and (→A) backward directions declared. Fails
  if either direction is absent or COUPLING PAIR A is not co-located with
  PHASE-1-COMMIT.

### C-11 — Phase 1 Symmetry Declaration
- **Weight**: aspirational
- **Category**: integrity
- **Text**: Phase 1 contains a `SYMMETRY DECLARATION:` statement asserting the structural
  relationship between inertia findings and participant positions — that each inertia
  finding has a corresponding position response and each position response cites at least
  one inertia finding. The declaration appears after the INERTIA RECORD and before
  PHASE-1-COMMIT.
- **Pass condition**: `SYMMETRY DECLARATION:` present in Phase 1 after the INERTIA
  RECORD. Names the symmetry property to be enforced. Fails if absent or if the
  declaration appears in a phase other than Phase 1.

### C-12 — STANCE MANIFEST with Per-Participant Entries
- **Weight**: aspirational
- **Category**: completeness
- **Text**: Phase 2 contains a `## STANCE MANIFEST` block enumerating every participant's
  stance in structured form: `[PARTICIPANT-TOKEN]: [STANCE] — [one-phrase rationale]`.
  The manifest covers all participants who delivered positions in Phase 2 and appears
  after all POSITION blocks, before PHASE-2-COMMIT.
- **Pass condition**: `## STANCE MANIFEST` block present in Phase 2 after POSITION
  blocks. Every Phase 2 participant has an entry in `TOKEN: STANCE — rationale` format.
  Fails if block is absent, any participant is omitted, or entry format deviates.

### C-13 — STANCE INVARIANT Declaration
- **Weight**: aspirational
- **Category**: integrity
- **Text**: The `## STANCE MANIFEST` block closes with a `STANCE INVARIANT:` line
  asserting the count of participants and that stance assignments are locked at Phase 2
  (e.g., `STANCE INVARIANT: 6 participants locked. Stances immutable after Phase 2.`).
  The invariant is the final line of the STANCE MANIFEST block.
- **Pass condition**: `STANCE INVARIANT:` line present as the final line of the STANCE
  MANIFEST block. States participant count and immutability assertion. Fails if absent,
  count is missing, or line appears outside STANCE MANIFEST.

### C-14 — VOICE COMPLETENESS CHECK with Per-Tier Checkboxes
- **Weight**: aspirational
- **Category**: completeness
- **Text**: Phase 2 contains a `## VOICE COMPLETENESS CHECK` block listing one checkbox
  per participant tier (e.g., Executive Sponsors, Functional Leads, Technical Reviewers)
  confirming at least one voice from each tier delivered a position. A halt declaration
  asserts that any unticked box prevents Phase 2 from closing. All checkboxes must be
  ticked before PHASE-2-COMMIT.
- **Pass condition**: `## VOICE COMPLETENESS CHECK` block with per-tier checkboxes
  present in Phase 2. Halt declaration present. All checkboxes ticked before
  PHASE-2-COMMIT. Fails if block is absent, any tier is missing, halt declaration is
  omitted, or an unticked checkbox is present at commit time.

### C-15 — INERTIA CITATION AUDIT with AUDIT RESULT
- **Weight**: aspirational
- **Category**: traceability
- **Text**: Phase 3 contains an `## INERTIA CITATION AUDIT` block that cross-references
  each `INERTIA-FINDING-*` token against participant positions to confirm each finding
  was cited by at least one position. Each finding token is listed with a citation count.
  The block concludes with `AUDIT RESULT: COMPLETE` (all findings cited) or `INCOMPLETE`
  (with missing tokens listed). Phase 3 may only proceed past the audit block if
  `AUDIT RESULT: COMPLETE`.
- **Pass condition**: `## INERTIA CITATION AUDIT` block present in Phase 3. Every
  inertia finding token present with citation count. `AUDIT RESULT: COMPLETE` declared.
  Fails if block is absent, any finding token is missing, `AUDIT RESULT:` is absent, or
  result is not `COMPLETE`.

### C-16 — Phase 3 Symmetry Check (Three-Box Gate)
- **Weight**: aspirational
- **Category**: integrity
- **Text**: Phase 3 contains a `## SYMMETRY CHECK` block with exactly three checkboxes:
  (1) every inertia finding cited in at least one position, (2) every position cites at
  least one inertia finding, (3) no orphaned citations (citations referencing
  non-existent finding tokens). All three boxes must be ticked before the tally block
  proceeds. A halt declaration is required.
- **Pass condition**: `## SYMMETRY CHECK` block with three checkboxes present in Phase 3
  before the TALLY block. Halt declaration present. All three boxes ticked. Fails if
  block is absent, fewer than three checkboxes, halt declaration missing, or any box is
  unticked at tally time.

### C-17 — TALLY LEDGER PROTOCOL (Enumerate → Count → Cross-Check → TALLY RESULT)
- **Weight**: aspirational
- **Category**: integrity
- **Text**: The `## TALLY` block follows a four-step labeled protocol: (1) enumerate each
  participant's stance by reading from the STANCE MANIFEST, (2) count totals per stance
  category, (3) cross-check that the sum of all stance-category counts equals the
  participant count declared in the STANCE INVARIANT — a mismatch halts the tally,
  (4) declare `TALLY RESULT:` using the enumerated outcome. Each step is labeled.
- **Pass condition**: Four labeled steps (enumerate, count, cross-check, `TALLY
  RESULT:`) present in the Phase 3 TALLY block. Cross-check confirms participant count
  equality. `TALLY RESULT:` declared. Fails if any step is absent, cross-check is
  skipped, arithmetic mismatch is not surfaced, or `TALLY RESULT:` is missing.

### C-18 — PHASE-3-COMMIT Coupling Pair B
- **Weight**: aspirational
- **Category**: traceability
- **Text**: The PHASE-3-COMMIT carries a `COUPLING PAIR B:` annotation declaring both
  coupling directions: (B→) Phase 3 tally outcome will be reflected in the Phase 5
  verdict; (→B) Phase 5 verdict must be traceable to the Phase 3 TALLY RESULT. Both
  directions are named explicitly at or immediately after PHASE-3-COMMIT.
- **Pass condition**: `COUPLING PAIR B` annotation or block present at or immediately
  after PHASE-3-COMMIT. Both (B→) forward and (→B) backward directions declared. Fails
  if either direction is absent or COUPLING PAIR B is not co-located with
  PHASE-3-COMMIT.

### C-19 — CONSTRAINT REGISTRY with Phase-Tagged Halt Triggers
- **Weight**: aspirational
- **Category**: integrity
- **Text**: Phase 4 contains a `## CONSTRAINT REGISTRY` block listing each structural
  halt trigger defined across all prior phases, tagged with the phase in which the halt
  applies (e.g., `[Phase 2] VOICE COMPLETENESS CHECK: unticked box halts Phase 2`). The
  registry is a reference index — it surfaces constraints already embedded in the
  protocol; it does not introduce new ones. It appears in Phase 4 before any synthesis
  content.
- **Pass condition**: `## CONSTRAINT REGISTRY` block present in Phase 4 before synthesis
  content. At least one halt trigger per gatekeeping block (COMMITTEE TYPE GATE, VOICE
  COMPLETENESS CHECK, INERTIA CITATION AUDIT, SYMMETRY CHECK, MINUTES INTEGRITY CHECK)
  listed with phase tags. Fails if block is absent, any major halt trigger is omitted,
  or entries are untagged.

### C-20 — INERTIA CONTINUITY BRIDGE with BRIDGE RESULT
- **Weight**: aspirational
- **Category**: traceability
- **Text**: Phase 4 contains an `## INERTIA CONTINUITY BRIDGE` block that checks whether
  each inertia finding from Phase 1 has a resolution path visible in Phase 3 outcomes.
  For each finding: `INERTIA-FINDING-*: [RESOLVED / UNRESOLVED / DEFERRED]` with a
  citation to the tally outcome or action that accounts for it. The block concludes with
  `BRIDGE RESULT: YES` (at least one finding has a qualifying resolution) or `NO` (with
  a note explaining why no resolutions were achieved).
- **Pass condition**: `## INERTIA CONTINUITY BRIDGE` block present in Phase 4. Each
  `INERTIA-FINDING-*` token appears with a disposition and citation. `BRIDGE RESULT:`
  declared. If `YES`, at least one finding is marked `RESOLVED` with a qualifying
  citation. Fails if block is absent, any finding is unaccounted, or `BRIDGE RESULT:`
  is missing.

### C-21 — Phase 4 MINUTES INTEGRITY CHECK (Five Core Checkboxes)
- **Weight**: aspirational
- **Category**: integrity
- **Text**: Phase 4 contains a `## MINUTES INTEGRITY CHECK` block with at least five
  checkboxes confirming: (1) Verdict matches TALLY RESULT, (2) Attendees list matches
  STANCE MANIFEST participants, (3) Action Items present with three fields (owner, due
  date, description), (4) Key Discussion Points cite at least one inertia finding token,
  (5) INERTIA CONTINUITY BRIDGE result is declared. A halt declaration asserts all boxes
  must be ticked before Phase 5 begins.
- **Pass condition**: `## MINUTES INTEGRITY CHECK` block with at least five checkboxes
  in Phase 4. Halt declaration present. All five core boxes ticked before Phase 5
  content begins. Fails if block is absent, fewer than five boxes, halt declaration
  missing, or any box unticked at Phase 5 entry.

### C-22 — PHASE-5-COMMIT Coverage Statement
- **Weight**: aspirational
- **Category**: integrity
- **Text**: The PHASE-5-COMMIT line includes a parenthetical or inline coverage statement
  enumerating the structural elements confirmed present in Phase 5 — at minimum: `Verdict
  declared`, `Attendees listed`, `Action Items formatted`, `Discussion Points cited`. The
  statement appears on the same line as or immediately following `PHASE-5-COMMIT:
  [locked]`.
- **Pass condition**: PHASE-5-COMMIT line includes a coverage statement listing at least
  four confirmed elements. Fails if coverage statement is absent or lists fewer than
  four elements.

### C-23 — Phase 5 Dissent Inertia Linkage Checkpoint
- **Weight**: aspirational
- **Category**: traceability
- **Text**: The `## MINUTES INTEGRITY CHECK` block contains a named `DISSENT INERTIA
  LINKAGE` checkbox as an additional phase-entry criterion beyond the original five Phase
  5 section checkboxes. The checkbox confirms that minority positions or dissenting
  stances recorded in Phase 3 are explicitly surfaced in the Phase 5 minutes. The halt
  declaration governing `MINUTES INTEGRITY CHECK` covers this checkbox along with the
  original five: all boxes must be ticked before Phase 5 content is generated. R6 V-03
  introduces this pattern. It extends C-21's completeness-gate mechanism by adding
  explicit dissent traceability as a structural requirement at the Phase 4→5 boundary —
  ensuring that governance minutes capture not only the majority decision path but also
  documented minority positions, making incomplete dissent tracing a structural defect
  rather than a silent omission.
- **Pass condition**: A `DISSENT INERTIA LINKAGE` labeled checkbox present in the
  `## MINUTES INTEGRITY CHECK` block covering dissent surfacing in Phase 5 minutes. Halt
  declaration covers this box. Box ticked before Phase 5 content begins. Fails if
  checkbox is absent, unlabeled, or unticked at Phase 5 entry.

### C-24 — Phase 5 Action-Attribution Linkage
- **Weight**: aspirational
- **Category**: traceability
- **Text**: ACTION ITEMS entries in Phase 5 carry a fourth field `Origin:` naming the
  participant token or stance from the STANCE MANIFEST whose position generated the
  action (e.g., `Origin: LEAD-ENG — opposed on grounds of timeline`). An ACTION
  ATTRIBUTION gate validates every `Origin:` value against STANCE MANIFEST entries;
  mismatched or absent tokens fail the gate. The PHASE-5-COMMIT line includes `ACTION
  ATTRIBUTION validated` as an explicit completion marker. R7 V-01 introduces this
  pattern. It extends C-21's completeness-gate mechanism to the output layer — every
  action item must trace to a named governance source, making untraceable action
  assignments a structural defect rather than an attribution gap.
- **Pass condition**: All ACTION ITEMS entries in Phase 5 contain an `Origin:` field
  with a valid STANCE MANIFEST token. An ACTION ATTRIBUTION gate present in MINUTES
  INTEGRITY CHECK or as a standalone block validates each `Origin:`. PHASE-5-COMMIT
  includes `ACTION ATTRIBUTION validated`. Fails if any `Origin:` field is absent, any
  token is invalid, gate is missing, or commit marker is absent.

### C-25 — Phase 5 Inertia Resolution Summary Block
- **Weight**: aspirational
- **Category**: traceability
- **Text**: A `## INERTIA RESOLUTION SUMMARY` block appears in Phase 5 before
  PHASE-5-COMMIT. The block enumerates each inertia item token from Phase 1
  (`INERTIA-FINDING-A`, `INERTIA-FINDING-B`, …). Each entry carries either `Addressed
  by: [action item or decision reference]` or `No action needed: [reason]`; blank entries
  are not permitted. A `RESOLUTION RESULT:` field at the end of the block declares
  `COMPLETE` when all entries are filled; only `COMPLETE` permits proceeding to
  PHASE-5-COMMIT. A seventh MINUTES INTEGRITY CHECK checkbox confirms `RESOLUTION
  RESULT: COMPLETE`. R7 V-02 introduces this pattern. It closes the structural loop
  between the INERTIA RECORD (Phase 1) and the minutes output (Phase 5) — every inertia
  finding must exit with an explicit disposition.
- **Pass condition**: `## INERTIA RESOLUTION SUMMARY` block present in Phase 5 before
  PHASE-5-COMMIT. Every `INERTIA-FINDING-*` token enumerated with either `Addressed
  by:` or `No action needed:`. `RESOLUTION RESULT: COMPLETE` declared. Seventh MINUTES
  INTEGRITY CHECK checkbox present and ticked. Fails if block is absent, any finding is
  unaccounted, `RESOLUTION RESULT:` is missing or `INCOMPLETE`, or seventh checkbox is
  absent.

### C-26 — Phase 0 Committee-Type-Aware Outcome Vocabulary
- **Weight**: aspirational
- **Category**: integrity
- **Text**: Phase 0 header contains an `Outcome Vocabulary:` field declaring the set of
  valid verdict terms for the declared Committee Type (e.g., `APPROVED / REJECTED /
  DEFERRED` for Budget Approval; `PROCEED / HOLD / ESCALATE` for ROB). A third
  COMMITTEE TYPE GATE checkbox confirms `Outcome Vocabulary:` is declared and non-empty
  before Phase 0 closes. A `VOCABULARY CHECK` step in the Phase 4 TALLY LEDGER PROTOCOL
  validates that the tally verdict uses exactly one term from the declared vocabulary
  set; a term outside the declared set halts the tally. The Phase 5 `Verdict:` field
  must contain a term from the declared vocabulary. The PHASE-4-COMMIT line includes
  `OUTCOME declared using Phase 0 vocabulary` as an explicit marker. R7 V-03 introduces
  this pattern. It anchors verdict semantics to committee function at declaration time —
  vocabulary drift between Phase 0 intent and Phase 5 output is a structural defect.
- **Pass condition**: `Outcome Vocabulary:` field present in Phase 0 with at least two
  valid terms. Third COMMITTEE TYPE GATE checkbox confirms vocabulary declared. A
  `VOCABULARY CHECK` step in the Phase 4 TALLY LEDGER PROTOCOL present and passing.
  Phase 5 `Verdict:` uses a term from the declared vocabulary. PHASE-4-COMMIT includes
  `OUTCOME declared using Phase 0 vocabulary`. Fails if `Outcome Vocabulary:` is absent,
  third gate checkbox is missing, `VOCABULARY CHECK` is absent or fails, Phase 5 verdict
  uses an undeclared term, or PHASE-4-COMMIT marker is absent.
```

---

Three new criteria added. Scoring notes:

- **C-24** (V-01) and **C-25** (V-02) are both Phase 5 output-layer traceability gates — C-24 traces actions back to stances, C-25 traces inertia findings forward to resolutions.
- **C-26** (V-03) is a Phase 0 declaration gate that propagates forward through Phase 4 and Phase 5 — the only new criterion that touches three phases.
- V-04 earns C-24 + C-25 but not C-26 (97.30); V-05 earns all three (97.83). The 0.53 gap between V-04 and V-05 is exactly one criterion unit under the 19-way split.
- The redistribution penalty on R6 V-03/04/05 (−1.58) exceeds their v7 gain from C-23 (they earned 0.00 Δ in v7 vs V-01/V-02). This is expected: each round adds aspirational criteria that dilute prior-round scores regardless of whether those variations were the excellence source.
