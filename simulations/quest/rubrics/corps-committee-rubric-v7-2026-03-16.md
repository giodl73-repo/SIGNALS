Looking at the scorecard, the key R6 excellence signal is the **DISSENT INERTIA LINKAGE** 6th checkbox introduced in V-03/V-04/V-05 — present in 3 of 5 R6 variations but absent in V-01/V-02. That's the new aspirational criterion: C-23.

Scoring mechanics: 16-way split → 0.625 pts each. Full score stays at 97.83; variations missing only C-23 drop to 97.21 (−0.625 from v6).

```markdown
# corps-committee-rubric-v7-2026-03-16.md

## What changed from v6

**One new aspirational criterion** sourced from R6 excellence signals.

### C-23 — Phase 5 Dissent Inertia Linkage Checkpoint
The `## MINUTES INTEGRITY CHECK` block contains a named `DISSENT INERTIA LINKAGE`
checkbox as an additional phase-entry criterion beyond the original five Phase 5
section checkboxes. The checkbox confirms that minority positions or dissenting stances
recorded in Phase 3 are explicitly surfaced in the Phase 5 minutes. The halt declaration
governing `MINUTES INTEGRITY CHECK` covers this checkbox along with the original five:
all boxes must be ticked before Phase 5 content is generated. R6 V-03 introduces this
pattern. It extends C-17's completeness-gate mechanism by adding explicit dissent
traceability as a structural requirement at the Phase 4→5 boundary — ensuring that
governance minutes capture not only the majority decision path but also documented
minority positions, making incomplete dissent tracing a structural defect rather than a
silent omission.

---

## Scoring impact

Aspirational pool expands from 15-way to **16-way split** (≈0.625 pts each vs 0.67 pts
in v6). Variations that earn all 16 aspirational criteria pay no redistribution penalty;
variations that earned all 15 v6 criteria but lack C-23 pay a pool dilution penalty of
0.625 pts.

| Variation | v6 score | v7 score | Δ |
|---|---|---|---|
| R5 V-05 (all v6 criteria; base reference) | 97.83 | **97.21** | −0.625 |
| R6 V-01 (all v6 criteria) | 97.83 | **97.21** | −0.625 |
| R6 V-02 (all v6 criteria) | 97.83 | **97.21** | −0.625 |
| R6 V-03 (DISSENT INERTIA LINKAGE) | 97.83 | **97.83** | 0.00 |
| R6 V-04 (V-03 pattern retained) | 97.83 | **97.83** | 0.00 |
| R6 V-05 (V-03 pattern retained) | 97.83 | **97.83** | 0.00 |

R6 V-03 is the first variation to earn all 16 aspirational criteria and absorbs no
redistribution penalty. Under v7 it leads every v6-complete prior variation by 0.625 pts.
R6 V-01 and V-02 drop 0.625 pts because C-23 is absent — their MINUTES INTEGRITY CHECK
contains five checkboxes only.

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
- **Text**: Phase 1 contains at least one investigation block labeled
  `INVESTIGATION-ATTEMPT-N` (where N is a positive integer). Each attempt block records
  a distinct line of inquiry pursued before the inertia record is sealed.
- **Pass condition**: At least one `INVESTIGATION-ATTEMPT-N` label present inside
  Phase 1, before `PHASE-1-COMMIT`. Fails if the label is absent or appears outside
  Phase 1.

### C-04 — Inertia Record with One-Phrase Anchors
- **Weight**: essential
- **Category**: structure
- **Text**: Phase 1 contains an `INERTIA RECORD` block. Each inertia entry is expressed
  as a one-phrase anchor (a short, noun-phrase summary of a blocking factor). The block
  is sealed by `PHASE-1-COMMIT` and must not be modified after that commit.
- **Pass condition**: `INERTIA RECORD` block present in Phase 1 with at least one
  one-phrase anchor entry. Sealed at `PHASE-1-COMMIT`. Fails if block is absent,
  entries are not anchored, or the block appears outside Phase 1.

### C-05 — Phase 3 Stance Manifest
- **Weight**: essential
- **Category**: structure
- **Text**: Phase 3 contains a `STANCE MANIFEST` section that enumerates at least one
  declared finding or position drawn from the Phase 1 inertia record and Phase 2
  investigation outcomes. The manifest is sealed by `PHASE-3-COMMIT`.
- **Pass condition**: `STANCE MANIFEST` present inside Phase 3. At least one finding
  declared. Sealed at `PHASE-3-COMMIT`. Fails if absent or if the manifest appears
  outside Phase 3.

### C-06 — Phase 4 Decision Record
- **Weight**: essential
- **Category**: structure
- **Text**: Phase 4 contains a decision record documenting the outcome of the
  deliberation: either a vote tally, a consensus declaration, or an explicit deferral
  with stated reason. The record must include a named decision result field.
- **Pass condition**: Decision record present inside Phase 4 with an explicit result
  field. Fails if Phase 4 contains no decision record or if the result field is
  absent or blank.

### C-07 — Phase 5 Meeting Minutes
- **Weight**: essential
- **Category**: structure
- **Text**: Phase 5 contains meeting minutes that record the decision reached in Phase 4,
  the participants or roles involved, and any action items or follow-on commitments.
  Minutes must be attributable (role or name) and must not contradict the Phase 4
  decision record.
- **Pass condition**: Phase 5 minutes present with decision, attribution, and at least
  one action item or follow-on commitment. Fails if minutes are absent, unatttributed,
  or contradict the Phase 4 result.

---

## Aspirational Criteria
> Output quality improves with these. Each criterion is worth ≈0.625 pts.
> Base score (all essentials pass, 0 aspirational): ≈87.83.
> Full score (all 16 aspirational): 97.83.

---

### C-08 — Investigation Attempt Structural Labeling
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: Each `INVESTIGATION-ATTEMPT-N` block uses consistent structural labeling
  with a sequential integer suffix. Attempt numbers are contiguous (no gaps). The final
  attempt block immediately precedes the INERTIA RECORD block in Phase 1.
- **Pass condition**: Investigation attempts labeled with contiguous integers in
  ascending order. Final attempt immediately precedes INERTIA RECORD. No unlabeled
  investigation blocks.

### C-09 — Inertia Invariant with Both Elements
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: An `INERTIA INVARIANT` block appears in Phase 1 and contains exactly two
  elements: (1) a declaration that the record is `sealed at PHASE-1-COMMIT`, and (2) a
  modification prohibition stating that the inertia record must not be altered after
  that commit point.
- **Pass condition**: `INERTIA INVARIANT` block present with both `sealed at
  PHASE-1-COMMIT` declaration and explicit modification prohibition. Fails if either
  element is absent.

### C-10 — Gate-N Loop with Rewrite Protocol
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: Phase 1 contains a `GATE-N` loop construct and a named `REWRITE PROTOCOL`
  that governs how failed gates trigger investigation restarts. The protocol is invoked
  by name in the restart clause.
- **Pass condition**: `GATE-N` loop present in Phase 1. `REWRITE PROTOCOL` named block
  present. Restart clause invokes the protocol by name. Fails if either construct is
  absent or if the restart clause does not reference the protocol by name.

### C-11 — Tier Sort with Sort-Check
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: Phase 3 contains a tier sort block that orders findings by severity or
  priority, followed immediately by a `SORT-CHECK` verification step that confirms the
  sort order is valid before proceeding.
- **Pass condition**: Tier sort block and `SORT-CHECK` present in Phase 3 in that order.
  Fails if either is absent or if SORT-CHECK precedes the sort.

### C-12 — Commit Coupling Integrity
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: Both `PHASE-1-COMMIT` and `PHASE-3-COMMIT` include explicit coupling
  declarations that bind the commit to the structural elements that preceded it (e.g.,
  inertia record count, stance manifest entry count). These coupling declarations make
  the commit non-trivially traceable to the content it seals.
- **Pass condition**: `PHASE-1-COMMIT` and `PHASE-3-COMMIT` each contain a coupling
  declaration referencing sealed content by name or count. Fails if either commit is
  uncoupled.

### C-13 — Symmetry Check Block at Phase 3→4 Boundary
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: A `## SYMMETRY CHECK` block appears between `PHASE-3-COMMIT` and the
  `## PHASE 4` header. The block contains exactly three checkboxes covering the symmetry
  conditions that must hold before Phase 4 begins.
- **Pass condition**: `## SYMMETRY CHECK` block present at Phase 3→4 boundary with
  three checkboxes. Fails if absent, mispositioned, or checkbox count ≠ 3.

### C-14 — Symmetry Declaration with Both Coupling Pairs
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: The SYMMETRY CHECK block or its enclosing structure contains a
  `SYMMETRY DECLARATION` that defines both `COUPLING PAIR A` and `COUPLING PAIR B`,
  naming the paired structural elements that must be in balance before Phase 4 entry.
- **Pass condition**: `SYMMETRY DECLARATION` present with both `COUPLING PAIR A` and
  `COUPLING PAIR B` defined. Fails if either coupling pair is absent or unnamed.

### C-15 — Stance Invariant with Both Elements
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: A `STANCE INVARIANT` block appears in or adjacent to Phase 3 and contains
  exactly two elements: (1) a declaration that the stance manifest is `sealed at
  PHASE-3-COMMIT`, and (2) an explicit modification prohibition preventing stance
  manifest changes after that commit.
- **Pass condition**: `STANCE INVARIANT` block present with both `sealed at
  PHASE-3-COMMIT` declaration and modification prohibition. Fails if either element
  is absent.

### C-16 — Inertia Continuity Bridge with Declared Result
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: An `## INERTIA CONTINUITY BRIDGE` block appears between `PHASE-2-COMMIT`
  and `## PHASE 3`. The block contains a `BRIDGE RESULT` field with a declared value,
  and an explicit halt declaration preventing Phase 3 from beginning if the bridge
  result is undeclared.
- **Pass condition**: `## INERTIA CONTINUITY BRIDGE` block at Phase 2→3 boundary.
  `BRIDGE RESULT` field present and declared. Halt declaration present. Fails if block
  is absent, result is undeclared, or halt declaration is missing.

### C-17 — Phase 5 Completeness Skeleton Gate (MINUTES INTEGRITY CHECK)
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: A `## MINUTES INTEGRITY CHECK` block appears between `PHASE-4-COMMIT` and
  the Phase 5 content header. The block enumerates the required Phase 5 sections as
  named checkboxes. An explicit halting declaration prevents Phase 5 content from being
  generated until all boxes are ticked.
- **Pass condition**: `## MINUTES INTEGRITY CHECK` block at Phase 4→5 boundary. At
  least three named Phase 5 section checkboxes present. Halt declaration present. Fails
  if block is absent, fewer than three section checkboxes, or halt declaration is
  missing.

### C-18 — Phase 3 Named Correction Protocol (TIER SEQUENCE PROTOCOL)
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: A named protocol block delimited by `*** TIER SEQUENCE PROTOCOL ***` and
  `*** END TIER SEQUENCE PROTOCOL ***` appears inside Phase 3 fill rules. The protocol
  governs tier-sort correction. A restart clause within the protocol invokes it by name
  (e.g., `Execute TIER SEQUENCE PROTOCOL again from the top`).
- **Pass condition**: Named delimiters present in Phase 3. Restart clause invokes
  protocol by its exact name. Fails if delimiters are absent, the block is outside
  Phase 3, or the restart clause does not reference the protocol by name.

### C-19 — Inertia Citation Audit Block
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: A `## INERTIA CITATION AUDIT` block appears between `## STANCE MANIFEST`
  and `PHASE-3-COMMIT`. The block contains per-finding entries (e.g.,
  `INERTIA-FINDING-A` through `-D`) each citing the inertia anchor that grounds the
  finding. An `AUDIT RESULT` field is present. An explicit halting declaration prevents
  `PHASE-3-COMMIT` from proceeding until the audit result is declared `COMPLETE`.
- **Pass condition**: `## INERTIA CITATION AUDIT` block at correct position with
  per-finding entries, `AUDIT RESULT` field, and halt declaration. Fails if block is
  absent, entries are missing, or halt declaration is absent.

### C-20 — Phase 0 Committee Type Gate
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: A named gate block (e.g., `## COMMITTEE TYPE GATE`) appears between the
  typed agenda declaration lines and `PHASE-0-COMMIT`. The block ticks both
  `Committee Type:` and `Agenda Item:` fields against an accepted-vocabulary list
  (ROB / shiproom / arch-board or equivalent). An explicit halting declaration prevents
  Phase 0 from committing if either field fails vocabulary validation. R5 V-01
  introduces this pattern. It extends C-01's prose-level enforcement into a structural
  skeleton gate — applying the same visible-checkpoint mechanism that SYMMETRY CHECK and
  MINUTES INTEGRITY CHECK use at later phase boundaries to the Phase 0 entry point.
  Type-mismatch failures become structural defects rather than silent fill-rule
  violations.
- **Pass condition**: Named gate block present between typed agenda lines and
  `PHASE-0-COMMIT`. Both `Committee Type:` and `Agenda Item:` fields checked against
  vocabulary. Vocabulary list (ROB / shiproom / arch-board or equivalent) enumerated.
  Halt declaration present. `PHASE-0-COMMIT` body references gate completion. Fails if
  block is absent, either field is unchecked, vocabulary list is missing, or halt
  declaration is absent.

### C-21 — Structured Bridge Completeness Gate
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: A structured completeness-gate block appears at the Phase 2→3 transition,
  before Phase 3 content begins. The block enumerates phase-entry criteria as checkboxes
  or fill fields. An explicit halting declaration prevents entry into Phase 3 unless all
  bridge criteria are confirmed. The bridge expansion does not alter phase count or the
  placement of any `PHASE-N-COMMIT` line. R5 V-02 introduces this pattern. It extends
  the gate-before-phase-entry mechanism (already present at Phase 4→5 via MINUTES
  INTEGRITY CHECK) backward into the Phase 2→3 transition, ensuring that deliberation
  cannot begin until all pre-deliberation entry criteria are structurally confirmed
  rather than assumed.
- **Pass condition**: Completeness-gate block present at Phase 2→3 boundary enumerating
  phase-entry criteria (checkboxes or fill fields). Halt declaration prevents Phase 3
  entry until criteria are confirmed. Phase count and `PHASE-N-COMMIT` placement
  unaffected. Fails if gate block is absent, criteria are unenumerated, or halt
  declaration is missing.

### C-22 — Phase 4 Tally Ledger Protocol
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: A named protocol block (e.g., `## TALLY LEDGER PROTOCOL`) operates inside
  Phase 4 before `PHASE-4-COMMIT`. The block enumerates voting positions or
  decision-count outcomes from Phase 3, confirming that quorum or the required decision
  threshold is met. An explicit result declaration (`TALLY RESULT: QUORUM MET` or
  equivalent) is required inside the block. An explicit halting declaration prevents
  `PHASE-4-COMMIT` from proceeding until the tally is complete and the result is
  declared. R5 V-03 introduces this pattern. It applies the named-protocol audit
  mechanism (already present via INERTIA CITATION AUDIT in Phase 3) into Phase 4,
  replacing implicit vote-counting with a mandatory structural ledger that catches
  quorum failures before they propagate silently into Phase 5.
- **Pass condition**: Named tally protocol block present inside Phase 4 before
  `PHASE-4-COMMIT`. Voting positions or decision-count outcomes enumerated. Explicit
  result declaration present. Halt declaration prevents `PHASE-4-COMMIT` until result
  is declared. Fails if block is absent, result declaration is missing, or halt
  declaration is absent.

### C-23 — Phase 5 Dissent Inertia Linkage Checkpoint
- **Weight**: aspirational (≈0.625 pts)
- **Category**: structure
- **Text**: The `## MINUTES INTEGRITY CHECK` block contains a named
  `DISSENT INERTIA LINKAGE` checkbox as an additional phase-entry criterion beyond the
  original five Phase 5 section checkboxes. The checkbox confirms that minority
  positions or dissenting stances recorded in Phase 3 are explicitly surfaced in the
  Phase 5 minutes. The existing halt declaration for `MINUTES INTEGRITY CHECK` extends
  to cover this checkbox. R6 V-03 introduces this pattern. It extends C-17's
  completeness-gate mechanism by adding explicit dissent traceability as a structural
  requirement at the Phase 4→5 boundary — ensuring that governance minutes capture not
  only the majority decision path but also documented minority positions, making
  incomplete dissent tracing a structural defect rather than a silent omission.
- **Pass condition**: `DISSENT INERTIA LINKAGE` checkbox present inside
  `## MINUTES INTEGRITY CHECK` as a named entry. Halt declaration covers this checkbox
  (either the existing halt declaration is broad enough or it explicitly includes it).
  Fails if the checkbox is absent or if the halt declaration does not cover it.
```
