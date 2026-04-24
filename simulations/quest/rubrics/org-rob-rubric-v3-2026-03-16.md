380 lines, starts and ends correctly. Written to `simulations/quest/rubrics/org-rob-rubric-v3-2026-03-16.md`.

---

Here's what was extracted and added:

**Three new patterns from the R2 scorecard, all aspirational at 2 pts each:**

**C-14 — Lens-anchored findings** (correctness)
Both V-01 and V-02 got `+` on C-02 but not `++`. The gap: role lens shaped the *stage* but no finding-level citation was required. C-14 requires `Lens:` / `Via:` on ≥50% of findings, naming the specific role lens item that triggered each concern. Makes role-loading independently verifiable at the finding level.

**C-15 — Column-invariant verdict format** (format)
V-02 got `++` on C-03; V-01 got `+`. The difference: V-02 used a named-column verdict table; V-01 used prose. C-03's pass condition doesn't distinguish these. C-15 requires stage verdicts as table rows with at least status, rationale, and a finding-ID reference — making omission structurally impossible rather than just policy-discouraged.

**C-16 — Synthesis residual open items** (depth)
V-02 got C-06 `++` partly via a dedicated "Residual Open Items" section flagging every `Acknowledged As = empty` finding. V-01 achieved C-06 `++` via Dual-Direction Check table — a different mechanism. C-16 rewards the dedicated inventory specifically, and requires the section be present even when empty (an empty residual section is a positive signal, not an omission).

**Scoring impact:**
- Aspirational tier: 5 → 8 criteria, 2 pts each → tier max 10 → **16**
- Total max: 100 → **106**
- V-01 R2: 99 → **100** (gains C-16 `+`)
- V-02 R2: 89 → **103** (gains C-14/C-15/C-16 all `++`; still fails C-11)

- **C-15 Column-invariant verdict format** -- stage verdicts are expressed as
  table rows with named columns (Status, Rationale, Condition, Finding-ID), not as
  prose blocks. V-02 reached `++` on C-03 because its Stage Verdict block is a
  structural table row; V-01 only reached `+` because its verdict lives in a prose
  template. C-03 pass condition does not distinguish these two forms. C-15
  captures the structural upgrade explicitly.

- **C-16 Synthesis residual open items** -- synthesis contains a dedicated section
  enumerating all finding escalations that were sent upstream but not yet
  acknowledged downstream (Acknowledged As = empty). V-02 R2 achieved C-06 `++`
  partly via this mechanism ("coherence failure is structurally visible"). V-01
  achieves C-06 `++` via Dual-Direction Check table -- a different mechanism
  serving a similar purpose. C-16 rewards the dedicated residual-items inventory
  as a first-class structural property distinct from C-09 (prospective blocker
  detection) and C-12 (per-finding dual-direction tracing).

**Scoring impact:** N_aspirational 5 -> 8, each aspirational criterion remains 2 pts.
Aspirational tier max 10 -> 16. Total max 100 -> **106**.

V-01 R2 recomputes to **100** (was 99 under v2):
gains C-16 `+` (+1 pt); C-14 and C-15 remain `o` (no per-finding lens field,
prose verdict template).

V-02 R2 recomputes to **103** (was 89 under v2):
gains C-14 `++` (+2), C-15 `++` (+2), C-16 `++` (+2); retains C-11 fail (0).

---

## Essential Criteria

*Output must satisfy all five. Any essential failure = not golden regardless of
composite score.*

### C-01 -- Stage Identity and Labeling
- **Category**: format
- **Weight**: essential
- **Text**: Every stage in the output is explicitly labeled with its name. The
  stage header identifies which stage is running -- not inferred from context or
  implied by position. A reader must be able to locate any stage without parsing
  surrounding prose.
- **Pass condition**: Each stage in the output includes a labeled header
  identifying it by name. No stage is anonymous.

---

### C-02 -- Role-Loaded Perspective
- **Category**: correctness
- **Weight**: essential
- **Text**: Each stage review reflects the perspective of the role loaded from
  `.roles/` -- not a generic review. The role orientation, lens, and
  expertise shape which concerns are raised.
- **Pass condition**: At least one finding per stage is grounded in the loaded
  role documented lens (e.g., a PM flags adoption risk, a TPM flags schedule
  risk, an architect flags coupling). Generic findings that any role could have
  written do not satisfy this criterion.

---

### C-03 -- ROB Document Format Compliance
- **Category**: format
- **Weight**: essential
- **Text**: Output follows the ROB stage document format: stage header, role
  identity, numbered findings with severity, and a stage verdict. All four
  structural elements must be present for each stage.
- **Pass condition**: For each stage run: (1) stage header present, (2) role
  identity stated, (3) at least one finding with severity label (HIGH/MED/LOW
  or equivalent), (4) explicit stage verdict (APPROVED / APPROVED WITH CONDITIONS
  / BLOCKED / DEFERRED or equivalent).

---

### C-04 -- Actionable Findings
- **Category**: depth
- **Weight**: essential
- **Text**: Each stage produces at least 2 concrete findings or decision points.
  Findings name a specific concern, not a category. Each finding has an implied
  or explicit owner and a suggested resolution or next step.
- **Pass condition**: Total findings >= 2 * N_stages_run. Each finding is specific
  (references the artifact, not just the domain). At least half of findings include
  a resolution path or owner.

---

### C-05 -- Go/No-Go Signal
- **Category**: correctness
- **Weight**: essential
- **Text**: When the `tpm` stage runs (including via `--stage all`), output includes
  an explicit go/no-go recommendation with rationale. The verdict is not implied or
  buried -- it is a top-level statement.
- **Pass condition**: `tpm` stage output contains an unambiguous GO / NO-GO /
  GO WITH CONDITIONS verdict as a labeled top-level element, accompanied by at
  least one sentence of rationale citing a specific finding.

---

## Recommended Criteria

*Output is better with these. Each adds material value.*

### C-06 -- Cross-Stage Coherence
- **Category**: depth
- **Weight**: recommended
- **Text**: When multiple stages run, later stages reference or escalate findings
  from earlier stages. The escalation chain (teams -> pm -> tpm) is visible: a
  teams finding becomes a pm alignment item, which becomes a tpm risk.
- **Pass condition**: At least 2 cross-stage references in any multi-stage run
  (e.g., "teams raised X; pm confirms X is unresolved; tpm registers X as risk
  R-02").

---

### C-07 -- Risk Register Structure
- **Category**: depth
- **Weight**: recommended
- **Text**: The `tpm` stage produces a structured risk register, not a prose list.
  Each entry has a title, severity, likelihood, and mitigation. The register is
  machine-scannable.
- **Pass condition**: `tpm` stage includes a risk register table or structured list
  with >= 3 entries, each containing title, severity, likelihood, and mitigation.
  At least one risk is rated HIGH.

---

### C-08 -- Spire Cascade Tracing
- **Category**: coverage
- **Weight**: recommended
- **Text**: When the `spire` stage runs, output traces how S-office missions cascade
  down to the artifact under review. At least one mission-to-artifact link is
  explicit: mission -> program -> artifact alignment or gap.
- **Pass condition**: `spire` stage output names at least one S-office mission by
  name and traces its alignment or misalignment to the artifact under review with
  a specific example.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable.*

### C-09 -- Inter-Stage Blocker Detection
- **Category**: depth
- **Weight**: aspirational
- **Text**: Output explicitly identifies when a finding from one stage creates a
  hard blocker for a downstream stage. Blockers are surfaced proactively, not
  discovered retroactively.
- **Pass condition**: At least 1 inter-stage blocker is named in a multi-stage run,
  with the upstream stage, the blocking finding, and the downstream stage impact
  stated explicitly (e.g., "teams finding F-03 blocks tpm go/no-go: ownership
  unresolved").

---

### C-10 -- Cross-Cutting Theme Elevation
- **Category**: depth
- **Weight**: aspirational
- **Text**: When the same concern surfaces in 2 or more stages, output recognizes
  the pattern and elevates it as a cross-cutting theme -- above the individual
  stage findings. Cross-cutting themes receive priority weighting.
- **Pass condition**: At least 1 cross-cutting theme is named at the document level
  (not buried inside a single stage), citing the 2+ stages that surfaced it and
  noting why the repetition increases severity.

---

### C-11 -- Phase Gate Contracts
- **Category**: depth
- **Weight**: aspirational
- **Text**: Each stage defines explicit entry and exit conditions that enforce
  cross-stage coherence structurally rather than narratively. Entry conditions
  state what must be true before the stage can proceed; exit conditions state
  what the stage certifies as resolved before handing off downstream.
- **Pass condition**: At least 2 stages in a multi-stage run include a Phase Gate
  block (or equivalent labeled section) with named entry conditions and named exit
  conditions. Exit conditions must reference at least one finding ID or open item
  from that stage, not just generic readiness language.
- **Source**: V-04 Round 1 -- only variation to hit 100. Phase gate contracts make
  C-06 structurally checkable instead of relying on narrative cross-references.
  V-02 R2 fails this criterion: finding registry accumulation is not equivalent
  to phase gate contracts.

---

### C-12 -- Dual-Direction Traceability
- **Category**: depth
- **Weight**: aspirational
- **Text**: Cross-stage finding propagation is acknowledged in both directions:
  the sending stage escalates the finding, and the receiving stage explicitly
  acknowledges receipt by finding ID. Traceability is not one-sided.
- **Pass condition**: In any multi-stage run with escalation, at least 1 receiving
  stage contains a `Responds-to` or `Inherits` field (or equivalent) citing the
  upstream finding ID (e.g., `Inherits: PM-F-02 -- ownership gap`). The downstream
  stage verdict must reference the inherited finding.
- **Source**: V-04 Round 1 -- dual-direction acknowledgment makes the escalation
  chain independently verifiable; no other Round 1 variation enforced the receiving
  side.

---

### C-13 -- Named Blocker Format
- **Category**: correctness
- **Weight**: aspirational
- **Text**: When a downstream finding retroactively invalidates an upstream verdict
  (e.g., arch-board finding overturns a tpm go), the output names this explicitly
  using a triad: upstream stage + blocking finding + required action. Retroactive
  invalidation is surfaced as a named event, not implied by silence.
- **Pass condition**: At least 1 retroactive invalidation scenario in a multi-stage
  run is expressed using the triad format: `{upstream-stage} verdict affected by
  {finding-ID}: {reason}. Required action: {action}.` The upstream stage and its
  original verdict must be identifiable from the named blocker.
- **Source**: V-04 Round 1 -- named format `{AB-01} blocks tpm go/no-go: [reason].
  Upstream stage affected. Required action.` was the sole mechanism enabling
  cross-stage retroactive invalidation. No other variation in Round 1 enforced this.

---

### C-14 -- Lens-Anchored Findings
- **Category**: correctness
- **Weight**: aspirational
- **Text**: Each finding cites the specific lens item or orientation frame from the
  loaded role (`.roles/`) that triggered it. Role-loading is verifiable at
  the finding level, not just at the stage level. A finding that could have been
  written by any role does not clear C-14, even if the stage header names a role.
- **Pass condition**: At least 50% of findings across the run include a `Lens:`,
  `Via:`, or equivalent field naming the specific role lens item that motivated the
  concern (e.g., `Lens: tpm.lens.schedule-risk` or `Via: orientation.frame --
  delivery velocity`). The cited lens item must exist in the loaded role file.
- **Source**: R2 scorecard -- both V-01 and V-02 scored `+` on C-02 (role lens
  shapes the stage orientation) but neither reached `++`. The gap: no per-finding
  lens citation field was required. The `++` path on C-02 requires finding-level
  lens enforcement, which C-14 now rewards explicitly.

---

### C-15 -- Column-Invariant Verdict Format
- **Category**: format
- **Weight**: aspirational
- **Text**: Stage verdicts are expressed as table rows with named columns rather
  than prose blocks. Column-invariant output eliminates the structural ambiguity
  that allows omission of rationale or finding-ID citation. Prose verdicts satisfy
  C-03 but do not satisfy C-15.
- **Pass condition**: At least 2 stage verdicts in the run are expressed as rows
  in a named-column table containing at minimum: (1) status (GO / NO-GO / etc.),
  (2) rationale, (3) at least one finding-ID reference. Prose verdict blocks, even
  if they contain the same information, do not satisfy this criterion.
- **Source**: R2 scorecard -- V-02 scored `++` on C-03 because "verdict table is
  a structural table row, not prose." V-01 scored `+` because "prose template, not
  column invariant." C-03 pass condition does not distinguish these two structural
  forms. C-15 rewards the encoding that makes verdict omission structurally
  impossible.

---

### C-16 -- Synthesis Residual Open Items
- **Category**: depth
- **Weight**: aspirational
- **Text**: Synthesis contains a dedicated section enumerating all finding
  escalations that were sent upstream but not yet acknowledged or resolved
  downstream. This inventory makes gaps in the escalation chain structurally
  visible without requiring manual comparison of sending and receiving stages.
  A Dual-Direction Check table satisfies C-12; a Residual Open Items section
  satisfies C-16 -- they are complementary, not interchangeable.
- **Pass condition**: Synthesis output includes a Residual Open Items section (or
  equivalent labeled section) listing every finding where the downstream
  acknowledgment is absent or empty, naming: (1) the originating stage, (2) the
  finding ID, (3) the intended receiving stage, (4) the gap (e.g., `Acknowledged
  As = empty`). The section must be present even when the list is empty -- an
  empty residual section is a stronger signal than a missing one.
- **Source**: R2 scorecard -- V-02 achieved C-06 `++` partly via "Residual Open
  Items section flags any `Acknowledged As = empty` -- coherence failure is
  structurally visible." V-01 achieved C-06 `++` via Dual-Direction Check table
  instead. C-16 rewards the dedicated residual-items inventory as a distinct
  structural property separate from C-09 (prospective blocker detection) and C-12
  (per-finding dual-direction tracing).

---

## Criterion Summary

| ID   | Text (short)                         | Weight        | Category    |
|------|--------------------------------------|---------------|-------------|
| C-01 | Stage identity and labeling          | essential     | format      |
| C-02 | Role-loaded perspective              | essential     | correctness |
| C-03 | ROB document format compliance       | essential     | format      |
| C-04 | Actionable findings (2x per stage)   | essential     | depth       |
| C-05 | Explicit go/no-go in tpm stage       | essential     | correctness |
| C-06 | Cross-stage coherence                | recommended   | depth       |
| C-07 | Risk register structure in tpm       | recommended   | depth       |
| C-08 | Spire cascade tracing                | recommended   | coverage    |
| C-09 | Inter-stage blocker detection        | aspirational  | depth       |
| C-10 | Cross-cutting theme elevation        | aspirational  | depth       |
| C-11 | Phase gate contracts                 | aspirational  | depth       |
| C-12 | Dual-direction traceability          | aspirational  | depth       |
| C-13 | Named blocker format                 | aspirational  | correctness |
| C-14 | Lens-anchored findings               | aspirational  | correctness |
| C-15 | Column-invariant verdict format      | aspirational  | format      |
| C-16 | Synthesis residual open items        | aspirational  | depth       |

---

## Scoring Model

| Tier | Criteria | Max pts (tier) | Max per criterion | ++ | + | o |
|------|----------|----------------|-------------------|----|---|---|
| Essential | C-01 to C-05 | 60 | 12 | 12 | 12* | 0 |
| Recommended | C-06 to C-08 | 30 | 10 | 10 | 7 | 0 |
| Aspirational | C-09 to C-16 | 16 | 2 | 2 | 1 | 0 |

*Essential `+` = PASS. Both `+` and `++` earn full points for essential criteria.

**Total max: 60 + 30 + 16 = 106**

Any essential failure = not golden regardless of composite score.

---

## Example Score Calculations

**Baseline golden** -- all essential pass, 2/3 recommended, 0/8 aspirational:

```
composite = (5/5 * 60) + (2/3 * 30) + (0/8 * 16)
          = 60 + 20 + 0
          = 80
```

Golden threshold met (all essential pass, composite = 80).

**V-01 R2 equivalent** -- all essential pass, 3/3 recommended,
C-09/C-11/C-12/C-13 at ++, C-10/C-16 at +, C-14/C-15 at o:

```
aspirational = 2 + 1 + 2 + 2 + 2 + 0 + 0 + 1 = 10
composite    = 60 + 30 + 10 = 100
```

**V-02 R2 equivalent** -- all essential pass, 3/3 recommended,
C-09/C-12/C-13/C-14/C-15/C-16 at ++, C-10 at +, C-11 at o:

```
aspirational = 2 + 1 + 0 + 2 + 2 + 2 + 2 + 2 = 13
composite    = 60 + 30 + 13 = 103
```

**Perfect score** -- all essential pass, 3/3 recommended, 8/8 aspirational at ++:

```
composite = 60 + 30 + 16 = 106
```
