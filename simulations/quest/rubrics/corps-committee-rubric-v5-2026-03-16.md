```markdown
# corps-committee-rubric-v5-2026-03-16.md

## What changed from v4

**Three new aspirational criteria** sourced from R4 excellence signals.

### C-17 — Phase 5 Completeness Skeleton Gate (MINUTES INTEGRITY CHECK)
The skeleton embeds a `## MINUTES INTEGRITY CHECK` block between `PHASE-4-COMMIT: [locked]`
and the Phase 5 section header. The block lists the three required Phase 5 sections —
DECISIONS, ACTION ITEMS, DISSENTING OPINIONS — as checkboxes. An explicit halting declaration
("any unticked box halts Phase 5" or equivalent) is present. R4 V-01 introduces this pattern.
It mirrors SYMMETRY CHECK's function at the P3→P4 boundary and applies it to Phase 5
completeness — catching missing sections structurally before Phase 5 begins rather than as
silent omissions after.

### C-18 — Phase 3 Named Correction Protocol (TIER SEQUENCE PROTOCOL)
Phase 3 contains a named, delimited protocol (e.g., `*** TIER SEQUENCE PROTOCOL ***`)
specifying the restart procedure when tier ordering is violated. On repeat failure the
protocol is re-invoked by name — "execute TIER SEQUENCE PROTOCOL again from the top" — not
restated inline. R4 V-02 introduces this pattern. It extends REWRITE PROTOCOL's
self-referencing correction mechanism from Phase 1 into Phase 3, closing the same drift-on-
repeat failure mode that C-16 closes for Phase 1.

### C-19 — Inertia Citation Audit Block
A printed skeleton block (e.g., `## INERTIA CITATION AUDIT`) appears between
`## STANCE MANIFEST` and `PHASE-3-COMMIT: [locked]`. The block enumerates each
INERTIA-FINDING-* label and confirms it is cited in at least one Phase 3 voice (ticked
checkbox or equivalent). An explicit halting declaration prevents Phase 3 from committing
if any finding is uncited. R4 V-03 introduces this pattern. It converts the implicit
citation requirements embedded in C-03 and C-05 into a mandatory printed gate — bare labels
or uncited findings now produce a visible structural failure rather than a quiet partial pass.

---

## Scoring impact

Aspirational pool expands from 9-way to **12-way split** (≈0.83 pts each vs 1.11 pts in v4).
Variations that earn all 12 aspirational criteria pay no redistribution penalty; variations
that earned the previous 9 but lack one or more of C-17/18/19 pay a pool dilution penalty.

| Variation | v4 score | v5 score | Δ |
|---|---|---|---|
| R3 V-05 (base reference) | 96.11 | **93.61** | −2.50 |
| R4 V-01 (MINUTES INTEGRITY CHECK) | 96.67 | **95.83** | −0.84 |
| R4 V-02 (TIER SEQUENCE PROTOCOL) | 96.44 | **95.60** | −0.84 |
| R4 V-03 (CITATION AUDIT) | 96.94 | **96.10** | −0.84 |
| R4 V-04 (V-01 + V-02) | 97.22 | **96.39** | −0.83 |
| R4 V-05 (V-01 + V-02 + V-03) | 97.83 | **97.83** | 0.00 |

R4 V-05 is the only variation that earns all 12 aspirational criteria and therefore absorbs
no redistribution penalty. Under v5 it leads every prior version by ≥1.73 pts. R3 V-05
drops 2.50 pts because it meets none of C-17, C-18, or C-19 — all three mechanisms are
introduced in R4.

---

## Essential Criteria
> Output fails without these. A missing or broken essential criterion disqualifies the
> variation.

### C-01 — Typed Agenda Item Declaration
- **Weight**: essential
- **Category**: format
- **Text**: The output opens with an `Agenda Type:` line declaring the meeting category
  (e.g., `ROB`, `Quarterly Business Review`, `Budget Approval`) AND an `Agenda Item:` line
  naming the specific subject under review. Both lines appear before any phase content.
- **Pass condition**: Both `Agenda Type:` and `Agenda Item:` labels present at output open,
  in that order, before Phase 0 begins. `Agenda Type:` uses a recognized meeting-category
  term, AND `Agenda Item:` names a specific subject. Fails if type is absent, unlabeled, or
  uses non-standard phrasing (e.g., "product review" instead of "ROB").

---

### C-02 — Five-Phase Structure with Terminal Commits
- **Weight**: essential
- **Category**: format
- **Text**: The output contains all five phases (0–5) in sequence, each closed by a
  `PHASE-N-COMMIT: [locked]` line that is the terminal line of that phase. No phase content
  appears after its commit line.
- **Pass condition**: All six commit markers present (PHASE-0-COMMIT through
  PHASE-5-COMMIT), each labeled `[locked]`, each appearing as the last substantive line
  before the next phase separator. Fails if any phase is absent, any commit is missing, or
  content follows a commit line within the same phase.

---

### C-03 — INERTIA RECORD Complete and Sealed
- **Weight**: essential
- **Category**: correctness
- **Text**: Phase 1 produces a `## INERTIA RECORD` section with four labeled findings
  (INERTIA-FINDING-A through INERTIA-FINDING-D), each carrying a non-placeholder content
  anchor. The `INERTIA INVARIANT` line is present with both required contract elements: the
  commit reference and the modification prohibition.
- **Pass condition**: All four INERTIA-FINDING-* labels present with content anchors (not
  bare labels, not `[one-phrase anchor]` placeholders). INERTIA INVARIANT line present,
  contains `sealed at PHASE-1-COMMIT` AND `findings may not be added, removed, or modified
  without reopening Phase 1` (or equivalent modification prohibition). Fails on any missing
  finding, bare label, placeholder, or missing/incomplete INERTIA INVARIANT.

---

### C-04 — Phase 5 Delivers Actionable Minutes
- **Weight**: essential
- **Category**: coverage
- **Text**: Phase 5 contains three required sections — DECISIONS (verdict + conditions),
  ACTION ITEMS (at least two items each with owner/action/deadline), and DISSENTING OPINIONS
  (at least one dissent with objection, resolution path, and named authority — or explicit
  "No dissent — [reason]"). If the verdict is not APPROVED, Owner and Trigger must both be
  present in the DECISIONS section.
- **Pass condition**: All three Phase 5 sections present with content. Each action item has
  all three fields (owner role, specific action, deadline). Every CONDITION or BLOCK stance
  holder from Phase 3 has a corresponding dissent entry, or explicit no-dissent is declared
  with a reason. Fails if any section is absent, any action item is missing a field, or a
  non-APPROVED verdict lacks Owner and Trigger.

---

## Recommended Criteria
> Output is significantly better with these. Failing one or two lowers score but does not
> disqualify.

### C-05 — Inertia Continuity Bridge Correct
- **Weight**: recommended
- **Category**: correctness
- **Text**: The `## INERTIA CONTINUITY BRIDGE` section appears between Phase 2 and Phase 3.
  It correctly answers YES (with a qualifying charter role identified from the tier sort) or
  NO (with Inertia-Advocate INJECTED, appearing first in Tier 1 in Phase 3, and appearing
  in the ## STANCE MANIFEST). The injected or identified voice cites at least one
  INERTIA-FINDING-* label from ## INERTIA RECORD.
- **Pass condition**: Bridge section present and answers YES or NO with justification. If
  YES: the named role's orientation visibly maps to switching-cost analysis or status-quo
  defense — not assumed from a general "risk" orientation. If NO: Inertia-Advocate voice
  appears first in Tier 1 in Phase 3, cites a named INERTIA-FINDING-* label, and appears
  in STANCE MANIFEST. Fails if bridge section absent, YES claimed without a qualifying role
  whose charter explicitly covers switching-cost or status-quo defense, or NO declared
  without injection.

---

### C-06 — Phase 3 Tier Order and Non-Unanimous Stance
- **Weight**: recommended
- **Category**: correctness
- **Text**: Phase 3 voices appear in Tier 1 → Tier 2 → Tier 3 order. Each participant has
  a standalone `STANCE: [BLOCK / CONDITION / APPROVE]` line preceding their prose. At least
  one BLOCK or CONDITION stance is present; all-APPROVE is not a valid Phase 3 outcome
  (triggers Phase 2 restart). The ## STANCE MANIFEST lists all participants with their
  stance tokens.
- **Pass condition**: Voices in tier order without interleaving. Every voice block has an
  unqualified `STANCE:` line. Minimum one CONDITION or BLOCK in the manifest.
  ## STANCE MANIFEST present and complete. Fails if order violated, any STANCE: line absent
  or qualified (e.g., "BLOCK (pending)"), all voices are APPROVE, or manifest is incomplete.

---

### C-07 — Phase 4 Tally Matches Stance Manifest
- **Weight**: recommended
- **Category**: correctness
- **Text**: The `TALLY:` line in Phase 4 counts APPROVE, CONDITION, and BLOCK tokens by
  scanning ## STANCE MANIFEST, not by re-parsing Phase 3 prose. The OUTCOME is derived
  mechanically from that tally: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED
  WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED.
- **Pass condition**: Token counts in TALLY line match the number of each token in
  ## STANCE MANIFEST exactly. OUTCOME label matches the tally rule above. Fails if any
  count is wrong, OUTCOME contradicts the tally, or Phase 3 prose appears to have been
  re-parsed to override the manifest.

---

## Aspirational Criteria
> Each criterion is worth ≈0.83 pts (12-way split of a 10-pt pool). A variation earning
> all 12 reaches full aspirational credit.

### C-08 — [Carried forward from v4 — text unchanged]

### C-09 — [Carried forward from v4 — text unchanged]

### C-10 — [Carried forward from v4 — text unchanged]

### C-11 — [Carried forward from v4 — text unchanged]

### C-12 — [Carried forward from v4 — text unchanged]

### C-13 — [Carried forward from v4 — text unchanged]

### C-14 — [Carried forward from v4 — text unchanged]

---

### C-15 — Skeleton-Embedded Structural Gate
- **Weight**: aspirational
- **Category**: format
- **Text**: At least one verification checkpoint lives in the **printed skeleton itself**
  (not only in fill rules). The gate appears as a labelled block with ticked/unticked
  checkboxes and an explicit "any unticked box halts [next phase]" declaration — embedded
  at a phase boundary so that skipping it requires visible omission of skeleton content.
  V-05 (R3)'s `## SYMMETRY CHECK` block between Phase 3 and Phase 4 is the canonical
  template.
- **Pass condition**: At least one named gate block present in the skeleton at a phase
  boundary. Block contains checkboxes covering the required completeness or coupling checks
  for that transition. Explicit halting declaration present. Fails if all verification
  exists only in fill rules or prose instructions, or if no halting condition is stated.

---

### C-16 — Self-Referencing Named Correction Protocol
- **Weight**: aspirational
- **Category**: format
- **Text**: The rewrite loop uses a **named, delimited block** (e.g.,
  `*** REWRITE PROTOCOL ***`) AND re-invokes it by name on repeat failures: "execute
  REWRITE PROTOCOL again from the top." Variations that have the delimiter but restate
  instructions inline on re-trigger do not earn this criterion. V-05 (R3) uniquely closes
  the loop with a name pointer, preventing instruction drift across successive gate
  failures.
- **Pass condition**: Named, delimited correction protocol present. On-repeat-failure
  instruction uses the protocol name as a pointer, not an inline restatement. Fails if
  protocol is unnamed, if re-trigger restates instructions rather than referencing the
  block, or if no re-trigger instruction is present.

---

### C-17 — Phase 5 Completeness Skeleton Gate (MINUTES INTEGRITY CHECK)
- **Weight**: aspirational
- **Category**: format
- **Text**: A `## MINUTES INTEGRITY CHECK` block (or equivalently named gate) is embedded
  in the skeleton between `PHASE-4-COMMIT: [locked]` and the Phase 5 section header. The
  block lists all three required Phase 5 sections — DECISIONS, ACTION ITEMS, DISSENTING
  OPINIONS — as checkboxes. An explicit halting declaration ("any unticked box halts
  Phase 5" or equivalent) is present. R4 V-01 introduces this pattern. It extends C-15's
  skeleton-gate principle to the P4→P5 transition, ensuring Phase 5 completeness failures
  surface as a halted structural gate rather than a silent section omission.
- **Pass condition**: Named gate block present between PHASE-4-COMMIT and Phase 5. All
  three required Phase 5 sections listed as checkboxes. Explicit halting declaration
  present. Fails if block is absent, any required section is unlisted, or no halting
  condition is stated.

---

### C-18 — Phase 3 Named Correction Protocol (TIER SEQUENCE PROTOCOL)
- **Weight**: aspirational
- **Category**: format
- **Text**: Phase 3 contains a named, delimited protocol (e.g.,
  `*** TIER SEQUENCE PROTOCOL ***`) specifying the restart procedure when tier ordering is
  violated. On repeat failure the protocol is re-invoked by name — "execute TIER SEQUENCE
  PROTOCOL again from the top" — not restated inline. R4 V-02 introduces this pattern. It
  applies C-16's self-referencing correction mechanism to Phase 3 tier violations, closing
  the same protocol-drift failure mode for Phase 3 ordering that REWRITE PROTOCOL closes
  for Phase 1 correctness.
- **Pass condition**: Named, delimited protocol block present in Phase 3 specifying the
  tier-ordering restart procedure. Re-trigger instruction uses the protocol name as a
  pointer, not an inline restatement. Fails if protocol is absent, unnamed, or re-trigger
  restates instructions rather than referencing the block by name.

---

### C-19 — Inertia Citation Audit Block
- **Weight**: aspirational
- **Category**: correctness
- **Text**: A printed skeleton block (e.g., `## INERTIA CITATION AUDIT`) appears between
  `## STANCE MANIFEST` and `PHASE-3-COMMIT: [locked]`. The block enumerates each
  INERTIA-FINDING-* label from the INERTIA RECORD and confirms it is explicitly cited in
  at least one Phase 3 voice, using ticked/unticked checkboxes or an equivalent binary
  confirmation per finding. An explicit halting declaration prevents Phase 3 from
  committing if any finding is uncited. R4 V-03 introduces this pattern. It converts the
  implicit citation requirements in C-03 and C-05 into a mandatory printed gate: bare
  labels and Phase 3 voices that drift from the INERTIA RECORD now produce a visible
  structural failure rather than a silent partial pass.
- **Pass condition**: Named audit block present between STANCE MANIFEST and
  PHASE-3-COMMIT. All INERTIA-FINDING-* labels enumerated with per-finding citation
  confirmation. Explicit halting declaration for any uncited finding. Fails if block is
  absent, any finding label is omitted, confirmation entries are missing, or no halting
  condition is stated.
```
