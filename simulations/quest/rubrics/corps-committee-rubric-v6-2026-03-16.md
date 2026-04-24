```markdown
# corps-committee-rubric-v6-2026-03-16.md

## What changed from v5

**Three new aspirational criteria** sourced from R5 excellence signals.

### C-20 — Phase 0 Committee Type Gate
A printed skeleton block (e.g., `## COMMITTEE TYPE GATE`) appears between the typed
agenda declaration lines and `PHASE-0-COMMIT`. The block ticks both `Committee Type:`
and `Agenda Item:` fields against an accepted-vocabulary list (ROB / shiproom /
arch-board or equivalent). An explicit halting declaration prevents Phase 0 from
committing if either field fails vocabulary validation. R5 V-01 introduces this pattern.
It extends C-01's prose-level enforcement into a structural skeleton gate — applying the
same visible-checkpoint mechanism that SYMMETRY CHECK and MINUTES INTEGRITY CHECK use at
later phase boundaries to the Phase 0 entry point. Type-mismatch failures become
structural defects rather than silent fill-rule violations.

### C-21 — Structured Bridge Completeness Gate
A structured completeness-gate block appears at the Phase 2→3 transition, before Phase 3
content begins. The block enumerates phase-entry criteria as checkboxes. An explicit
halting declaration prevents entry into Phase 3 unless all bridge criteria are ticked.
The bridge expansion does not alter phase count or the placement of any `PHASE-N-COMMIT`
line. R5 V-02 introduces this pattern. It extends the gate-before-phase-entry mechanism
(already present at Phase 4→5 via MINUTES INTEGRITY CHECK) backward into the Phase 2→3
transition, ensuring that deliberation cannot begin until all pre-deliberation entry
criteria are structurally confirmed rather than assumed.

### C-22 — Phase 4 Tally Ledger Protocol
A named protocol block (e.g., `## TALLY LEDGER PROTOCOL`) operates inside Phase 4
before `PHASE-4-COMMIT`. The block enumerates voting positions or decision-count outcomes
from Phase 3, confirming that quorum or the required decision threshold is met. An
explicit result declaration (`TALLY RESULT: QUORUM MET` or equivalent) is required
inside the block. An explicit halting declaration prevents `PHASE-4-COMMIT` from
proceeding until the tally is complete and the result is declared. R5 V-03 introduces
this pattern. It applies the named-protocol audit mechanism (already present via
INERTIA CITATION AUDIT in Phase 3) into Phase 4, replacing implicit vote-counting with
a mandatory structural ledger that catches quorum failures before they propagate silently
into Phase 5.

---

## Scoring impact

Aspirational pool expands from 12-way to **15-way split** (≈0.67 pts each vs 0.83 pts
in v5). Variations that earn all 15 aspirational criteria pay no redistribution penalty;
variations that earned all 12 v5 criteria but lack one or more of C-20/21/22 pay a pool
dilution penalty.

| Variation | v5 score | v6 score | Δ |
|---|---|---|---|
| R4 V-05 (base reference) | 97.83 | **95.83** | −2.00 |
| R5 V-01 (COMMITTEE TYPE GATE) | 97.83 | **96.50** | −1.33 |
| R5 V-02 (BRIDGE COMPLETENESS GATE) | 97.83 | **96.50** | −1.33 |
| R5 V-03 (TALLY LEDGER PROTOCOL) | 97.83 | **96.50** | −1.33 |
| R5 V-04 (V-01 + V-02) | 97.83 | **97.17** | −0.67 |
| R5 V-05 (V-01 + V-02 + V-03) | 97.83 | **97.83** | 0.00 |

R5 V-05 is the only variation that earns all 15 aspirational criteria and therefore
absorbs no redistribution penalty. Under v6 it leads every prior version by ≥1.33 pts.
R4 V-05 drops 2.00 pts because it meets none of C-20, C-21, or C-22 — all three
mechanisms are introduced in R5.

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
  meeting-category term, AND `Agenda Item:` names a specific subject. Fails if type is
  absent, unlabeled, or uses non-standard phrasing (e.g., "product review" instead
  of "ROB").

---

### C-02 — Five-Phase Structure with Terminal Commits
- **Weight**: essential
- **Category**: format
- **Text**: The output contains all five phases (0–5) in sequence, each closed by a
  `PHASE-N-COMMIT: [locked]` line that is the terminal line of that phase. No phase
  content appears after its commit line.
- **Pass condition**: Phases 0 through 5 present in order. Each `PHASE-N-COMMIT:
  [locked]` line is the last line of its phase. Any content appearing after a commit
  line — including headers, notes, or continuation text — is a fail.

---

### C-03 through C-07
*Inherited from v5 — text unchanged.*

---

## Aspirational Criteria

### C-08 through C-12 — R1–R3 Aspirational Pool
*Inherited from v5 — text unchanged.*

---

### C-13 through C-16 — R4 Aspirational Pool
*Inherited from v5 — text unchanged.*

---

### C-17 — Phase 5 Completeness Skeleton Gate (MINUTES INTEGRITY CHECK)
- **Weight**: aspirational
- **Category**: structure / gate
- **Text**: The skeleton embeds a `## MINUTES INTEGRITY CHECK` block between
  `PHASE-4-COMMIT: [locked]` and the Phase 5 section header. The block lists the three
  required Phase 5 sections — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS — as
  checkboxes. An explicit halting declaration ("any unticked box halts Phase 5" or
  equivalent) is present.
- **Pass condition**: `## MINUTES INTEGRITY CHECK` block present at the Phase 4→5
  boundary, in that position. Three checkboxes named DECISIONS, ACTION ITEMS, DISSENTING
  OPINIONS present. Halting declaration present. Fails if block is absent, positioned
  elsewhere, or the halting declaration is missing.

---

### C-18 — Phase 3 Named Correction Protocol (TIER SEQUENCE PROTOCOL)
- **Weight**: aspirational
- **Category**: structure / self-correction
- **Text**: Phase 3 contains a named, delimited protocol (e.g.,
  `*** TIER SEQUENCE PROTOCOL ***`) specifying the restart procedure when tier ordering
  is violated. On repeat failure the protocol is re-invoked by name — "execute TIER
  SEQUENCE PROTOCOL again from the top" — not restated inline.
- **Pass condition**: Named protocol block with opening and closing delimiters present
  inside Phase 3. Restart instruction uses the protocol's name (not inline restatement).
  Fails if the protocol is absent, unnamed, undelimited, or the repeat-failure instruction
  restates the procedure inline rather than invoking by name.

---

### C-19 — Inertia Citation Audit Block
- **Weight**: aspirational
- **Category**: structure / gate
- **Text**: A printed skeleton block (e.g., `## INERTIA CITATION AUDIT`) appears between
  `## STANCE MANIFEST` and `PHASE-3-COMMIT: [locked]`. The block enumerates each
  `INERTIA-FINDING-*` label and confirms it is cited in at least one Phase 3 voice
  (ticked checkbox or equivalent). An explicit halting declaration prevents Phase 3 from
  committing if any finding is uncited.
- **Pass condition**: `## INERTIA CITATION AUDIT` block present at correct position.
  Per-finding citation entries present. Halting declaration present. Fails if block is
  absent, any finding label is missing from the audit, or the halting declaration is
  absent.

---

### C-20 — Phase 0 Committee Type Gate
- **Weight**: aspirational
- **Category**: structure / gate
- **Text**: A printed skeleton block (e.g., `## COMMITTEE TYPE GATE`) appears between
  the typed agenda declaration lines (`Committee Type:` / `Agenda Item:`) and
  `PHASE-0-COMMIT`. The block ticks both fields against an accepted-vocabulary list (ROB /
  shiproom / arch-board or equivalent). An explicit halting declaration prevents
  `PHASE-0-COMMIT` from proceeding if either field fails vocabulary validation.
- **Pass condition**: `## COMMITTEE TYPE GATE` block (or equivalent named gate) present
  at the Phase 0 declaration→commit boundary. Both `Committee Type:` and `Agenda Item:`
  fields enumerated and ticked inside the block. Halting declaration present. Fails if
  block is absent, either field is missing from the gate, or the halting declaration is
  absent.

---

### C-21 — Structured Bridge Completeness Gate
- **Weight**: aspirational
- **Category**: structure / gate
- **Text**: A structured completeness-gate block appears at the Phase 2→3 transition
  before Phase 3 content begins. The block enumerates phase-entry criteria as checkboxes.
  An explicit halting declaration prevents Phase 3 from beginning until all bridge
  criteria are ticked. The bridge does not alter phase count or the placement of any
  `PHASE-N-COMMIT` line.
- **Pass condition**: Bridge completeness-gate block present at the Phase 2→3 boundary,
  before Phase 3 content. Entry criteria enumerated as checkboxes. Halting declaration
  present. Phase count unchanged (still 0–5). No `PHASE-N-COMMIT` displaced. Fails if
  block is absent, contains no checkboxes, lacks a halting declaration, or displaces any
  commit line.

---

### C-22 — Phase 4 Tally Ledger Protocol
- **Weight**: aspirational
- **Category**: structure / audit
- **Text**: A named protocol block (e.g., `## TALLY LEDGER PROTOCOL`) operates inside
  Phase 4 before `PHASE-4-COMMIT`. The block enumerates voting positions or
  decision-count outcomes from Phase 3, with an explicit result declaration (`TALLY
  RESULT: QUORUM MET` or equivalent). An explicit halting declaration prevents
  `PHASE-4-COMMIT` from proceeding until the tally is complete and the result is
  declared.
- **Pass condition**: Named tally protocol block present inside Phase 4, before
  `PHASE-4-COMMIT`. Voting/decision outcomes enumerated. Result declaration (QUORUM MET /
  THRESHOLD MET or equivalent) present. Halting declaration present. Fails if block is
  absent, result declaration is missing, halting declaration is absent, or block appears
  after `PHASE-4-COMMIT`.
```

---

Three decisions worth flagging:

**C-21 bridge position.** The scorecard says the bridge "precedes Phase 3" — I fixed the gate at Phase 2→3. If the bridge is actually Phase 1→2 or spans differently in the skill, adjust the position reference accordingly.

**C-22 result vocabulary.** "QUORUM MET" is inferred from context. If the skill uses a different term (e.g., `THRESHOLD REACHED`, `MOTION CARRIED`), update the pass-condition examples to match.

**Scoring arithmetic.** The Δ column uses `10/15 = 0.6̄7` per criterion. The −1.33 and −0.67 entries are exact thirds; if you prefer two-decimal rounding to match prior tables, −1.33 and −0.67 are the correct representations (vs −2.50 and −0.84 in v4→v5, which used `10/12`).
