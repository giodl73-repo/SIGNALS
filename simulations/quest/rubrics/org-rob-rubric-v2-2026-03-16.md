Written to `simulations/quest/rubrics/org-rob-rubric-v2-2026-03-16.md`.

---

**13 criteria across 3 tiers** (up from 10):

| ID | Criterion | Weight | Category |
|----|-----------|--------|----------|
| C-01 | Stage identity and labeling | essential | format |
| C-02 | Role-loaded perspective | essential | correctness |
| C-03 | ROB document format compliance | essential | format |
| C-04 | Actionable findings (2x per stage) | essential | depth |
| C-05 | Explicit go/no-go in tpm stage | essential | correctness |
| C-06 | Cross-stage coherence | recommended | depth |
| C-07 | Risk register structure in tpm | recommended | depth |
| C-08 | Spire cascade tracing | recommended | coverage |
| C-09 | Inter-stage blocker detection | aspirational | depth |
| C-10 | Cross-cutting theme elevation | aspirational | depth |
| **C-11** | **Phase gate contracts** | aspirational | depth |
| **C-12** | **Dual-direction traceability** | aspirational | depth |
| **C-13** | **Named blocker format** | aspirational | correctness |

**What changed:**

- **C-11 Phase gate contracts** — each stage declares explicit entry/exit conditions. Exit conditions must cite a finding ID, not generic readiness language. This makes C-06 structurally checkable rather than narratively implied.
- **C-12 Dual-direction traceability** — receiving stages must carry a `Responds-to` or `Inherits` field citing the upstream finding ID. V-02 through V-05 all enforced the sending side; V-04 alone enforced the receiving side.
- **C-13 Named blocker format** — retroactive invalidation (arch-board overturns tpm go) must use the triad `{upstream-stage} verdict affected by {finding-ID}: {reason}. Required action: {action}.` Silence is not a valid signal for this event.

**Scoring impact:** N_aspirational 2 -> 5, so each aspirational criterion is now worth 2 points instead of 5. V-02 score recomputes to 89 (was 95 under v1 math; it now gets partial credit on the new criteria it lacks). V-04 remains 100.
ng it. No stage is anonymous.

---

### C-02 — Role-Loaded Perspective
- **Category**: correctness
- **Weight**: essential
- **Text**: Each stage review reflects the perspective of the role loaded from
  `.roles/` — not a generic review. The role's orientation, lens, and
  expertise shape which concerns are raised.
- **Pass condition**: At least one finding per stage is grounded in the loaded
  role's documented lens (e.g., a PM flags adoption risk, a TPM flags schedule
  risk, an architect flags coupling). Generic findings that any role could have
  written do not satisfy this criterion.

---

### C-03 — ROB Document Format
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

### C-04 — Actionable Findings
- **Category**: depth
- **Weight**: essential
- **Text**: Each stage produces at least 2 concrete findings or decision points.
  Findings name a specific concern, not a category. Each finding has an implied
  or explicit owner and a suggested resolution or next step.
- **Pass condition**: Total findings >= 2 * N_stages_run. Each finding is specific
  (references the artifact, not just the domain). At least half of findings include
  a resolution path or owner.

---

### C-05 — Go/No-Go Signal
- **Category**: correctness
- **Weight**: essential
- **Text**: When the `tpm` stage runs (including via `--stage all`), output includes
  an explicit go/no-go recommendation with rationale. The verdict is not implied or
  buried — it is a top-level statement.
- **Pass condition**: `tpm` stage output contains an unambiguous GO / NO-GO /
  GO WITH CONDITIONS verdict as a labeled top-level element, accompanied by at
  least one sentence of rationale citing a specific finding.

---

## Recommended Criteria

*Output is better with these. Each adds material value.*

### C-06 — Cross-Stage Coherence
- **Category**: depth
- **Weight**: recommended
- **Text**: When multiple stages run, later stages reference or escalate findings
  from earlier stages. The escalation chain (teams -> pm -> tpm) is visible: a
  teams finding becomes a pm alignment item, which becomes a tpm risk.
- **Pass condition**: At least 2 cross-stage references in any multi-stage run
  (e.g., "teams raised X; pm confirms X is unresolved; tpm registers X as risk R-02").

---

### C-07 — Risk Register Structure
- **Category**: depth
- **Weight**: recommended
- **Text**: The `tpm` stage produces a structured risk register, not a prose list.
  Each entry has a title, severity, likelihood, and mitigation. The register is
  machine-scannable.
- **Pass condition**: `tpm` stage includes a risk register table or structured list
  with >= 3 entries, each containing title, severity, likelihood, and mitigation.
  At least one risk is rated HIGH.

---

### C-08 — Spire Cascade Tracing
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

### C-09 — Inter-Stage Blocker Detection
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

### C-10 — Cross-Cutting Theme Elevation
- **Category**: depth
- **Weight**: aspirational
- **Text**: When the same concern surfaces in 2 or more stages, output recognizes
  the pattern and elevates it as a cross-cutting theme — above the individual stage
  findings. Cross-cutting themes receive priority weighting.
- **Pass condition**: At least 1 cross-cutting theme is named at the document level
  (not buried inside a single stage), citing the 2+ stages that surfaced it and
  noting why the repetition increases severity.

---

### C-11 — Phase Gate Contracts
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
- **Source**: V-04 Round 1 — only variation to hit 100. Phase gate contracts make
  C-06 structurally checkable instead of relying on narrative cross-references.

---

### C-12 — Dual-Direction Traceability
- **Category**: depth
- **Weight**: aspirational
- **Text**: Cross-stage finding propagation is acknowledged in both directions:
  the sending stage escalates the finding, and the receiving stage explicitly
  acknowledges receipt by finding ID. Traceability is not one-sided.
- **Pass condition**: In any multi-stage run with escalation, at least 1 receiving
  stage contains a `Responds-to` or `Inherits` field (or equivalent) citing the
  upstream finding ID (e.g., `Inherits: PM-F-02 — ownership gap`). The downstream
  stage verdict must reference the inherited finding.
- **Source**: V-04 Round 1 — dual-direction acknowledgment makes the escalation
  chain independently verifiable; no other Round 1 variation enforced the receiving
  side.

---

### C-13 — Named Blocker Format
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
- **Source**: V-04 Round 1 — named format `{AB-01} blocks tpm go/no-go: [reason].
  Upstream stage affected. Required action.` was the sole mechanism enabling
  cross-stage retroactive invalidation. No other variation in Round 1 enforced this.

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

---

## Example Score Calculations

**Baseline golden** — all essential pass, 2/3 recommended, 0/5 aspirational:

```
composite = (5/5 * 60) + (2/3 * 30) + (0/5 * 10)
          = 60 + 20 + 0
          = 80
```

Golden threshold met (all essential pass, composite = 80).

**V-04 equivalent** — all essential pass, 3/3 recommended, 5/5 aspirational:

```
composite = (5/5 * 60) + (3/3 * 30) + (5/5 * 10)
          = 60 + 30 + 10
          = 100
```

**V-02 equivalent** — all essential pass, 2.5/3 recommended, 2/5 aspirational:

```
composite = (5/5 * 60) + (2.5/3 * 30) + (2/5 * 10)
          = 60 + 25 + 4
          = 89
```

Any essential failure = not golden regardless of composite.
