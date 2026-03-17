Confirms the aspirational band expands to 6 criteria (C-09 through C-14) in v3. Now writing the complete updated rubric:

```markdown
---
skill: quest-rubric
skill_target: topic-roadmap
date: 2026-03-17
version: 3
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
          + (aspirational_raw / 12 * 10)
```

Where `aspirational_raw` = sum of per-criterion scores across C-09–C-14
(full pass = 2, partial = 1, fail = 0; max = 12).

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
  The skill stops after this block with an explicit STOP instruction. No
  strategy.md write occurs before user reply.

---

### C-05 — strategy.md reflects confirmed proposals only
- **Weight:** essential
- **Category:** behavior
- **Text:** The write step applies only proposals the user explicitly confirmed.
  A REVISED reply triggers re-presentation, not a partial write. The count
  of applied changes must match the count the user confirmed.
- **Pass condition:** Write step is gated on YES or REVISED reply; REVISED
  triggers a new confirmation round before any write; applied-change count
  matches confirmed-proposal count.

---

## Recommended Criteria (all should pass for Golden)

### C-06 — Delta-Finding traceability in proposals
- **Weight:** recommended
- **Category:** traceability
- **Text:** Each proposal row makes the pre/post delta explicit so the reviewer
  can verify that the signal actually defeats inertia. "Strategy assumed /
  Signal revealed" or equivalent column names the specific assumption the
  NEW artifact overturns.
- **Pass condition:** Proposal table contains a column (or inline field) that
  names what the strategy previously assumed AND what the new artifact
  revealed. A proposal that states only the new action without naming the
  prior assumption fails.

---

### C-07 — Null-case declarations are type-labeled
- **Weight:** recommended
- **Category:** completeness
- **Text:** When inertia holds for a proposal type, the output declares it
  explicitly per type rather than silently omitting that type. Each null
  declaration names its type (ADD / REMOVE / REPRIORITIZE) and states that
  inertia held.
- **Pass condition:** For each of ADD, REMOVE, and REPRIORITIZE where no
  proposals were generated, a labeled null appears: e.g.,
  "ADDITIONS: none — inertia holds." or equivalent. A run that omits a type
  entirely without a null declaration fails.

---

### C-08 — Before/after diff table present
- **Weight:** recommended
- **Category:** completeness
- **Text:** A structured diff table accompanies the confirmed proposals,
  showing the strategy dimension, its Before state, and its After state with
  the evidence artifact cited in the After cell. This artifact becomes the
  audit record for the strategy change.
- **Pass condition:** Diff table present with at minimum: dimension name,
  Before state, After state, evidence artifact. Evidence reference is required
  in every After cell; an After cell with no artifact citation fails.

---

## Aspirational Criteria (distinguish top-tier runs)

Scoring: full pass = 2 pts, partial = 1 pt, fail = 0 pt. Max raw = 12.

### C-09 — Defender Challenge Table with Defense ID column and calibration
- **Weight:** aspirational
- **Category:** rigor
- **Text:** Before proposals are confirmed, a Challenger Table presents each
  proposal as a challenge to the inertia position. Each row must include a
  Defense ID (unique per row, e.g. D-01, D-02), the strategic decision being
  defended, the counter-argument, and strength (STRONG / MODERATE / WEAK).
  A calibration section follows, explaining the strength assignments.
  The table and calibration are required gate artifacts, not optional.
- **Pass condition (full, 2 pts):** Challenger Table present with all four
  columns — Defense ID, Strategic decision defended, Counter-argument,
  Strength — plus a calibration section. Table and calibration both labeled
  as required gate artifacts.
- **Pass condition (partial, 1 pt):** Challenger Table present with
  counter-argument and strength but Defense ID column absent; or table present
  without calibration section.

---

### C-10 — Conflict audit between proposal gate and diff gate
- **Weight:** aspirational
- **Category:** correctness
- **Text:** Before writing the diff table, the skill audits proposed changes
  for internal conflicts (e.g., two proposals that contradict each other on
  the same dimension). The audit either identifies conflicts or produces a
  gate-tied null declaration.
- **Pass condition (full, 2 pts):** Conflict check section appears between
  the proposal gate and the diff gate; includes a gate-tied null template
  ("CONFLICTS: none — conflict audit complete") when no conflicts found.
- **Pass condition (partial, 1 pt):** Conflict check present but not
  gate-tied (no named gate association) or null template absent.

---

### C-11 — Gate-sequenced architecture with upfront manifest
- **Weight:** aspirational
- **Category:** structure
- **Text:** The skill's output is organized as a sequence of named gates
  (at least four), each with a defined completion artifact and an inertia
  termination condition. An upfront Gate Manifest table lists all gates
  before execution begins. Gates are executed in order; no artifact is
  produced out of sequence.
- **Pass condition (full, 2 pts):** Upfront Gate Manifest table present
  listing at least four named gates with completion artifacts and inertia
  termination conditions; execution follows manifest order; explicit
  instruction prohibits out-of-order or skipped gates.
- **Pass condition (partial, 1 pt):** At least one named gate with a
  completion artifact present, but no upfront manifest; or manifest present
  but fewer than four gates named.

---

### C-12 — Per-gate inertia enforcement at three checkpoints
- **Weight:** aspirational
- **Category:** correctness
- **Text:** Inertia is enforced at three distinct checkpoints: (1) at the
  signal inventory gate — gate advances only if at least one NEW artifact
  exists; (2) at the delta-to-proposal gate — gate advances only if at least
  one delta candidate qualifies; (3) at the per-proposal challenger gate —
  each proposal row is individually tested against the keep-unchanged option.
  Each checkpoint is explicitly labeled as an advancement condition.
- **Pass condition (full, 2 pts):** All three labeled advancement conditions
  present, each phrased as "gate advances only if [condition]" or equivalent.
  Failing each condition produces a gate-termination null, not a skip.
- **Pass condition (partial, 1 pt):** Two of the three advancement conditions
  present with explicit labeling; the third is implied or absent.

---

### C-13 — Gate-termination nulls as named structural artifacts
- **Weight:** aspirational
- **Category:** completeness
- **Text:** Every inertia-hold outcome at a gate is surfaced as a named
  termination artifact tied to the specific gate that triggered it, not as
  a generic "nothing to report." The gate name appears in the null label.
- **Pass condition (full, 2 pts):** All null declarations are gate-tied:
  e.g., "G-1 TERMINATION — INERTIA HOLDS", "ADDITIONS — G-3 termination:
  inertia holds, no addition candidates beat NO CHANGE". Every level (inventory,
  delta, and proposal-type) produces gate-named nulls.
- **Pass condition (partial, 1 pt):** Proposal-type nulls are gate-tied but
  inventory or delta nulls are generic; or gate names present at some levels
  but inconsistently applied.

---

### C-14 — Advancement check PASS/FAIL output branches explicitly labeled
- **Weight:** aspirational
- **Category:** auditability
- **Text:** Each gate advancement check produces explicitly labeled output
  for both the PASS branch (gate advances, execution continues) and the FAIL
  branch (gate-termination null emitted, execution stops). Both branches are
  distinguishable in the output by label or formatting — not by absence alone.
  This enables run auditing: a reviewer can verify which path was taken and
  why, without inferring from silence.
- **Pass condition (full, 2 pts):** Each of the three inertia checkpoints
  (G-1, G-2, G-3 or equivalent) produces a labeled PASS output (e.g.,
  "[INERTIA CHECK G-1: PASS — N NEW artifacts found, gate advances]") and
  a distinct labeled FAIL output template (e.g., "[INERTIA CHECK G-1: FAIL —
  no NEW artifacts, G-1 TERMINATION — INERTIA HOLDS]"). Both branches named
  for all three checkpoints.
- **Pass condition (partial, 1 pt):** PASS/FAIL branching present for at
  least one checkpoint with explicit labels, but not all three; or PASS branch
  labeled but FAIL branch relies on absence rather than an explicit label.
```

---

**Changes from v2:**

- **Formula** — aspirational denominator updated from `/ 5 * 10` to `aspirational_raw / 12 * 10` to accommodate 6 criteria at 2 pts each
- **C-09** — pass condition now names the **Defense ID column** explicitly as a required column in the Challenger Table; this resolves the rubric/spec misalignment that capped all R2 runs at PARTIAL
- **C-14** — new aspirational criterion rewarding explicit PASS/FAIL output branches at all three inertia checkpoints; drawn from the V-05 pattern identified in the R2 scorecard as stronger production quality than bracket-notation alone
