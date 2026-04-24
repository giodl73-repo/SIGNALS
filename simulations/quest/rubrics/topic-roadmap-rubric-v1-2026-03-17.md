---
skill: quest-rubric
skill_target: topic-roadmap
date: 2026-03-17
version: 1
---

# Scoring Rubric — topic-roadmap (topic-plan)

Signal strategy revision as new information arrives. Read current strategy.md
and all gathered signals. Identify what has changed since the strategy was
written, what signals revealed unexpected dimensions needing coverage.
Propose additions, removals, re-prioritizations. User confirms. strategy.md updated.

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold:** all essential pass + composite >= 80

---

## Essential Criteria (must all pass)

### C-01 — Inertia prior enforced
- **Weight:** essential
- **Category:** correctness
- **Text:** Zero-change is a valid, complete output. The skill treats strategy.md
  unchanged as the default outcome. Proposals require evidence from NEW signal
  artifacts; volume of signals alone does not trigger change.
- **Pass condition:** Output either (a) produces proposals each backed by a
  named NEW artifact, OR (b) explicitly declares that inertia holds with a
  type-labeled null declaration. A run that opens with "here are the changes
  I recommend" without naming new artifacts fails.

---

### C-02 — Signal delta established before proposals
- **Weight:** essential
- **Category:** correctness
- **Text:** Signal inventory and delta analysis are present in the output
  before any proposal table is shown. The inventory classifies each artifact
  as NEW (date > strategy date) or PRIOR.
- **Pass condition:** A signal inventory table appears (at minimum: artifact
  filename, date, NEW/PRIOR, namespace). At least one of the four delta
  categories — CONFIRMED / EXPANDED / UNEXPECTED / CHALLENGED — is present
  in the output, even if populated with a null declaration. Proposals that
  appear before any delta analysis fail.

---

### C-03 — Proposals are concrete and action-typed
- **Weight:** essential
- **Category:** depth
- **Text:** Every proposal names its action type (ADD, REMOVE, or REPRIORITIZE),
  the specific strategy dimension it targets, and the new signal evidence
  that defeats the keep-unchanged option. Vague proposals ("consider expanding
  coverage") do not pass.
- **Pass condition:** Each proposal row contains: (a) action type from the
  ADD / REMOVE / REPRIORITIZE set, (b) a named strategy dimension with
  Before/After state, and (c) a specific signal artifact cited as evidence.
  A proposal row missing any of the three elements fails.

---

### C-04 — User confirmation gate is present and blocking
- **Weight:** essential
- **Category:** behavior
- **Text:** The skill pauses before modifying strategy.md and presents
  proposals to the user with explicit YES / NO / REVISED options. strategy.md
  is not touched until the user replies.
- **Pass condition:** Output includes a "PENDING CONFIRMATION" block (or
  equivalent) listing proposal counts and YES / NO / REVISED reply options.
  The skill stops after this block. No strategy.md write occurs before
  confirmation. A skill that writes strategy.md without pausing fails
  unconditionally.

---

### C-05 — strategy.md reflects only confirmed proposals
- **Weight:** essential
- **Category:** correctness
- **Text:** After confirmation, strategy.md is updated with exactly the
  confirmed (non-withdrawn) proposals. Unconfirmed proposals are not applied.
  If the user replies NO, strategy.md is not modified.
- **Pass condition:** Post-confirmation output confirms the count of applied
  changes (e.g., "strategy.md updated: 2 additions, 0 removals, 1
  reprioritization"). A NO reply results in no write. Applying proposals
  the user did not confirm fails.

---

## Recommended Criteria (output is better with these)

### C-06 — Delta-Finding traceability in proposal rows
- **Weight:** recommended
- **Category:** depth
- **Text:** Each proposal row names the delta finding that motivates it,
  using the format "Strategy assumed [X] / Signal revealed [Y]". This
  distinguishes evidence-driven change from preference-driven change.
- **Pass condition:** At least half of all proposal rows carry a Delta Finding
  cell in the format "Strategy assumed ... / Signal revealed ...". Cells
  containing only a filename or a generic claim fail the format check.

---

### C-07 — Null-case declarations are type-labeled
- **Weight:** recommended
- **Category:** format
- **Text:** For each change type (additions, removals, reprioritizations)
  where no change is proposed, an explicit type-labeled null declaration is
  present. A single unlabeled "No changes proposed" covering multiple change
  types does not pass.
- **Pass condition:** Each absent change type has its own labeled null
  declaration, e.g., "ADDITIONS: none -- inertia holds." or
  "REMOVALS: none -- inertia holds." Generic or unlabeled null statements fail.

---

### C-08 — Before/after diff table
- **Weight:** recommended
- **Category:** format
- **Text:** A diff table showing the before and after state per changed
  dimension is present, with evidence references in the After cell.
- **Pass condition:** A table with columns Dimension / Before / After
  appears at or after the proposal tables. After cells reference evidence
  (filename or proposal cross-ref). A diff table with After cells that
  contain no evidence reference fails.

---

## Aspirational Criteria (raise the bar once essential/recommended are stable)

### C-09 — Defender Challenge Table with calibrated strength
- **Weight:** aspirational
- **Category:** depth
- **Text:** Proposed changes are challenged by a counter-argument table.
  Challenge strength is calibrated: a table where all challenges are Weak
  signals rubber-stamp processing; a table where all are Strong signals
  over-zealous rejection. A calibration check sentence is present.
- **Pass condition:** A Defender Challenge Table is present with columns
  Defense ID / Proposal # / Strategic decision defended / Defensive argument /
  Challenge strength. A calibration check sentence appears after the table
  (e.g., "Calibration: balanced -- challenge strength distribution is varied.")
  All-Weak or All-Strong tables without a calibration note fail.

---

### C-10 — Conflict audit across NEW artifacts
- **Weight:** aspirational
- **Category:** coverage
- **Text:** If two NEW artifacts contradict each other on the same strategy
  dimension, the conflict is surfaced and resolved before proposals are
  written. Conflicting signals that feed unchallenged proposals are a
  structural gap.
- **Pass condition:** A conflict audit section is present, either with a
  populated conflict table (Conflict ID / Signal A / Signal B / Nature /
  Resolution) or with a type-labeled null: "CONFLICT AUDIT: none -- no
  contradictions detected between NEW artifacts on the same strategy
  dimension." Absence of any conflict audit section fails.

---

## Criterion Summary

| ID   | Text (short)                              | Weight        | Category    |
|------|-------------------------------------------|---------------|-------------|
| C-01 | Inertia prior enforced                    | essential     | correctness |
| C-02 | Signal delta established before proposals | essential     | correctness |
| C-03 | Proposals are concrete and action-typed   | essential     | depth       |
| C-04 | User confirmation gate present/blocking   | essential     | behavior    |
| C-05 | strategy.md reflects only confirmed props | essential     | correctness |
| C-06 | Delta-Finding traceability in proposals   | recommended   | depth       |
| C-07 | Null-case declarations are type-labeled   | recommended   | format      |
| C-08 | Before/after diff table                   | recommended   | format      |
| C-09 | Defender Challenge Table + calibration    | aspirational  | depth       |
| C-10 | Conflict audit across NEW artifacts       | aspirational  | coverage    |

---

## Scoring Examples

**Passes golden (all essential + composite >= 80):**
- C-01 thru C-05 all pass (60 pts)
- C-06 + C-07 pass, C-08 fails (20 pts)
- C-09 passes, C-10 fails (5 pts)
- Composite = 60 + 20 + 5 = 85 -- GOLDEN

**Fails golden (essential gap):**
- C-04 fails (no confirmation gate -- skill writes strategy.md immediately)
- Composite cannot reach golden regardless of other scores

**Fails golden (composite gap):**
- All essential pass (60 pts)
- All recommended fail (0 pts)
- All aspirational pass (10 pts)
- Composite = 70 -- below threshold
