```markdown
---
skill: quest-rubric
skill_target: topic-roadmap
date: 2026-03-17
version: 4
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
- **Text:** A gate mechanism separates proposal presentation from strategy
  write. The gate must prevent strategy.md from being written before user
  confirmation is shown. Token-based gates (e.g. `GATE CHECK PASSED --
  ANALYSIS-TO-CONFIRMATION`) are the clearest form; any equivalent blocking
  mechanism passes.
- **Pass condition:** The output contains an explicit checkpoint between the
  proposal table and the write step. The gate must be named or labeled, not
  implied. An output that writes strategy.md without showing a confirmation
  checkpoint fails. An output that shows a soft "await user" note but
  continues to the write step without waiting fails.

---

### C-05 — strategy.md write executed after confirmation
- **Weight:** essential
- **Category:** behavior
- **Text:** The write to strategy.md is explicitly conditional on user YES
  (or equivalent). The output names which strategy dimensions will be
  modified and their Before/After state before executing the write.
- **Pass condition:** The apply phase is gated behind user YES / REVISED /
  equivalent. The output traces each proposed change to a specific strategy
  dimension before writing. An output that writes without tracing the change
  to a named dimension fails. An output that writes on user silence fails.

---

## Recommended Criteria (majority should pass)

### C-06 — Null declarations are type-labeled
- **Weight:** recommended
- **Category:** completeness
- **Text:** When any delta category has no entries, the output produces a
  labeled null declaration rather than omitting the category or writing
  "nothing found."
- **Pass condition:** Empty delta categories appear as `{CATEGORY}: none —
  {reason}` (or equivalent labeled form). An output that silently omits a
  delta category fails. An output that writes "nothing found" without
  naming the category fails.

---

### C-07 — All four delta categories present
- **Weight:** recommended
- **Category:** completeness
- **Text:** All four delta categories (CONFIRMED / EXPANDED / UNEXPECTED /
  CHALLENGED) appear as labeled sections. Each has either populated content
  or a type-labeled null declaration.
- **Pass condition:** All four category labels appear in the output. Each
  has either entries or a type-labeled null declaration. An output that
  collapses multiple categories into a single "changes I see" section fails.
  An output that omits any category without a null declaration fails.

---

### C-08 — Evidence citation is two-part (filename + understanding delta)
- **Weight:** recommended
- **Category:** depth
- **Text:** Each signal citation contains the artifact filename and an
  understanding delta statement of the form `{prior understanding} →
  {now understanding}`. A citation that only names the artifact without
  stating what changed in understanding is incomplete.
- **Pass condition:** Every evidence citation in the proposal table contains
  (a) the artifact filename and (b) an understanding delta statement. A
  paraphrase without filename fails. A filename without understanding delta
  fails.

---

## Aspirational Criteria (depth, edge cases, adversarial)

Scored 0 / 1 / 2 per criterion (fail / partial / pass). Max = 12.

### C-09 — Per-proposal adversarial defeat column
- **Weight:** aspirational
- **Category:** adversarial
- **Text:** Every proposal row contains an explicit "Defeats NO CHANGE?"
  column (or equivalent) that forces articulation of why keeping the
  strategy unchanged is inferior to the proposed change. The column is
  required, not optional; vague content ("evidence supports this") does not
  pass the column.
- **Pass (2):** Every proposal row has a populated defeat justification that
  names the specific cost of inaction against a specific NEW signal. The
  column appears in the proposal table header.
- **Partial (1):** Some but not all proposal rows have defeat justification;
  or the column exists but contains generic language not tied to a named
  artifact.
- **Fail (0):** No defeat column or mechanism present in the proposal table.

---

### C-10 — Adversarial register with structured framing
- **Weight:** aspirational
- **Category:** adversarial
- **Text:** The output contains a dedicated adversarial register that
  enumerates assumptions embedded in the current strategy and stress-tests
  each against new signal evidence. Assumptions are named, their source
  strategy dimension identified, and a verdict rendered (HOLDS / WEAKENED /
  DEFEATED).
- **Pass (2):** An adversarial register section exists with named
  assumptions, the signals that challenge each, and a verdict from the
  HOLDS / WEAKENED / DEFEATED set. At least one assumption per strategy
  dimension present in the register.
- **Partial (1):** Some challenge framing exists but not as a structured
  register; or only a subset of strategy assumptions are enumerated; or
  verdicts are absent.
- **Fail (0):** No adversarial framing beyond the proposal table itself.

---

### C-11 — Pre-Signal Defense Register
- **Weight:** aspirational
- **Category:** adversarial
- **Text:** Before reading signal artifacts, the output extracts the
  assumptions embedded in the current strategy.md. This register anchors
  what the strategy was betting on before new evidence arrives, preventing
  post-hoc rationalization of the signal read.
- **Pass (2):** A Pre-Signal Defense Register appears before the signal
  inventory section. It names each strategy assumption with a source
  dimension and a testable condition of the form "this assumption holds
  if {condition}."
- **Partial (1):** Some assumption extraction is present but incomplete; or
  assumptions appear after the signal read rather than before; or testable
  conditions are absent.
- **Fail (0):** No pre-signal assumption extraction.

---

### C-12 — UNEXPECTED delta category receives distinct treatment
- **Weight:** aspirational
- **Category:** depth
- **Text:** UNEXPECTED signals — those that reveal dimensions not present
  in the current strategy — are treated as first-class findings rather than
  collapsed into EXPANDED or omitted. Each UNEXPECTED entry names the new
  dimension, the signal that revealed it, and a coverage recommendation.
- **Pass (2):** UNEXPECTED entries appear in their own labeled section.
  Each entry names the new dimension, the revealing artifact, and either a
  coverage recommendation (ADD proposal candidate) or an explicit null
  declaration explaining why coverage is deferred.
- **Partial (1):** UNEXPECTED signals appear but are not clearly
  distinguished from EXPANDED; or entries lack coverage recommendations
  without null declarations; or the section is present but empty without
  a type-labeled null.
- **Fail (0):** UNEXPECTED category absent, or merged into another category
  without labeling, or empty without a type-labeled null declaration.

---

### C-13 — Reversibility column on all proposal types
- **Weight:** aspirational
- **Category:** depth
- **Text:** Reversibility tracking appears in every proposal subtable
  (additions, removals, and reprioritizations), not only in one. Each
  proposal carries an explicit reversibility attribute so the user can
  calibrate commitment level before confirming.
- **Pass (2):** A reversibility attribute (e.g. REVERSIBLE / COSTLY TO
  REVERSE / PERMANENT, or equivalent) appears in all proposal subtables.
  At least one proposal has a non-trivial reversibility note.
- **Partial (1):** Reversibility tracked for additions but not for removals
  or reprioritizations; or a reversibility attribute is present but not
  labeled or explained; or present in only one subtable.
- **Fail (0):** No reversibility tracking in any proposal subtable.

---

### C-14 — Confidence calibration on proposals
- **Weight:** aspirational
- **Category:** depth
- **Text:** Each proposal carries a stated confidence level (HIGH / MEDIUM /
  LOW or equivalent) tied to the strength of the signal evidence, not the
  strength of the idea. The rationale for the confidence level names the
  artifact count and artifact type that grounds it.
- **Pass (2):** Every proposal has a confidence rating with a brief rationale
  of the form "{rating} — {N} signals of type {namespace}, {artifact
  quality note}." Ratings are differentiated across proposals (not all HIGH).
- **Partial (1):** Confidence ratings present but not tied to signal quality;
  or only some proposals rated; or all proposals rated identically without
  rationale.
- **Fail (0):** No confidence calibration on proposals.
```
