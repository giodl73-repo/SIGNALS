Here is the complete updated rubric v5:

```markdown
---
skill: quest-rubric
skill_target: topic-roadmap
date: 2026-03-17
version: 5
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
          + (aspirational_raw / 20 * 10)
```

Where `aspirational_raw` = sum of per-criterion scores across C-09–C-18
(full pass = 2, partial = 1, fail = 0; max = 20).

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
  confirmation. The gate is structural, not advisory — execution stops at
  the gate and does not continue until the user provides an explicit reply.
- **Pass condition:** Output contains a visible gate boundary (header, label,
  or explicit stop instruction) after proposals and before any file write.
  The gate text must instruct the model to write nothing further until the
  user replies. An advisory note ("I recommend confirming before writing")
  without a structural stop fails.

---

### C-05 — strategy.md is the sole write target; no write without explicit confirmation
- **Weight:** essential
- **Category:** behavior
- **Text:** Only strategy.md is modified by this skill. No other files are
  written. The write occurs only after explicit user confirmation (YES or
  REVISED). No implicit write path exists (e.g., timer, default, or
  auto-proceed on silence).
- **Pass condition:** The output names strategy.md as the sole write target.
  The write section is gated on YES or REVISED confirmation only. Any
  evidence of writes to other files, or of a write path that does not
  require confirmation, fails.

---

## Recommended Criteria (pass 2/3 for full recommended score)

### R-01 — Conflict audit section present with typed null
- **Weight:** recommended
- **Category:** depth
- **Text:** A dedicated conflict audit section is present that checks whether
  NEW artifacts contradict each other or contradict PRIOR artifacts. If no
  conflicts are found, a typed null declaration is used rather than silence
  or omission.
- **Pass condition:** Output contains a labeled conflict audit section. If
  no conflicts exist, the section includes a verbatim typed null of the
  form: "CONFLICT AUDIT: none — no contradictions detected between NEW
  artifacts." Omitting the section entirely fails.

---

### R-02 — Before/after diff table present
- **Weight:** recommended
- **Category:** depth
- **Text:** A structured before/after diff table shows the current state of
  each strategy dimension targeted by a proposal alongside its proposed
  new state. Dimensions with no change are excluded from the table.
- **Pass condition:** A labeled diff table appears after the proposals
  section. Each row references a specific proposal and shows Before and
  After values. The "If unchanged" consequence column substitutes for this
  table only if it contains the full before-state; a consequence column
  alone does not satisfy R-02.

---

### R-03 — "If unchanged" consequence column required per proposal row
- **Weight:** recommended
- **Category:** depth
- **Text:** Every row in the proposal table includes an "If unchanged" column
  that states the concrete consequence of leaving the strategy dimension at
  its current state. A proposal without a named consequence is a preference,
  not a decision.
- **Pass condition:** Each proposal row contains an "If unchanged" column
  with a specific consequence statement. Generic fill ("strategy may be
  incomplete") without naming what will be missed fails.

---

## Aspirational Criteria (C-09–C-18, 2 pts each, max 20)

### C-09 — Explicit banned vague phrases list
- **Weight:** aspirational
- **Text:** The skill output includes or enforces a named list of banned
  vague phrases that cannot appear in proposal rationale. Phrases such as
  "compelling reason", "clearly warranted", "obvious improvement", "no
  change needed", "update is needed" are prohibited by name.
- **Pass condition (2):** A labeled banned-phrases list appears, naming at
  least five specific phrases. Any proposal rationale that uses a listed
  phrase is flagged as a gate failure.
- **Partial (1):** Vagueness is discouraged by tone or general instruction
  but no enumerated list appears.

---

### C-10 — "Inertia defeated by" column with specific evidence sentence
- **Weight:** aspirational
- **Text:** Every proposal table includes a dedicated "Inertia defeated by"
  column. The column content must be one sentence naming the specific signal
  evidence or logic that makes keeping-unchanged worse than changing. Generic
  rationale ("new signals suggest change") fails this column.
- **Pass condition (2):** A named "Inertia defeated by" column appears in
  every proposal table with a specific per-row evidence sentence.
- **Partial (1):** Consequence or evidence is present per row but the column
  is not explicitly labeled "Inertia defeated by".

---

### C-11 — Integer-only counts; prose quantities are gate failures
- **Weight:** aspirational
- **Text:** All quantity references in the output use integers. Prose quantity
  words ("several", "a few", "some", "many", "numerous") in any structural
  field (inventory counts, proposal counts, namespace counts) are treated as
  gate failures.
- **Pass condition (2):** Output contains an explicit rule that N and M must
  be integers, and prose quantity words are named as gate failures.
- **Partial (1):** Integers are used throughout but no explicit enforcement
  rule is stated.

---

### C-12 — All 9 namespaces assessed in inventory
- **Weight:** aspirational
- **Text:** The signal inventory section lists all 9 namespaces by name,
  even if a namespace has zero NEW artifacts. Namespaces with zero artifacts
  receive a typed null entry rather than being omitted.
- **Pass condition (2):** All 9 namespaces appear by name in the inventory.
  Namespaces with no artifacts show an explicit zero or null entry.
- **Partial (1):** Namespaces with artifacts are listed but namespaces with
  zero artifacts are omitted.

---

### C-13 — Verbatim typed null declaration forms
- **Weight:** aspirational
- **Text:** The skill defines a NULL DECLARATION CONTRACT that provides
  verbatim forms for every type of null that can occur: all four delta
  categories (CONFIRMED / EXPANDED / UNEXPECTED / CHALLENGED), all three
  change types (ADD / REMOVE / REPRIORITIZE), and at least the conflict
  audit null. Generic "no changes proposed" without type label is prohibited.
- **Pass condition (2):** A labeled NULL DECLARATION CONTRACT section
  provides at least eight verbatim null forms covering all four delta
  categories and all three change types.
- **Partial (1):** Type-labeled nulls are used in practice but no verbatim
  contract section is defined.

---

### C-14 — Verbatim inertia checkpoint reproduced at structural gate points
- **Weight:** aspirational
- **Text:** An INERTIA ENFORCEMENT block is reproduced verbatim at each
  structural gate point in the output (minimum: before proposal evaluation,
  before proposals are shown, and in the unmodified-status declaration).
  A single statement of inertia principle at the top does not satisfy this
  criterion.
- **Pass condition (2):** The inertia enforcement block appears verbatim at
  three or more structural points, with each occurrence labeled by section
  number or gate name.
- **Partial (1):** Inertia principle is restated at more than one point but
  without a verbatim reproduction contract.

---

### C-15 — Per-proposal inertia verdict column (YES / NO / INCONCLUSIVE)
- **Weight:** aspirational
- **Source:** Round 4 V-01 excellence signal
- **Text:** Every proposal row includes an "Inertia Defeated?" verdict column
  with exactly three allowed values: YES, NO, or INCONCLUSIVE. A proposal
  marked NO or INCONCLUSIVE is automatically dropped from the confirmed
  proposal set and cannot proceed to the write gate. This is structurally
  distinct from C-10's evidence citation — the verdict is a binary gate, the
  citation is the supporting record.
- **Pass condition (2):** A named "Inertia Defeated?" column with the
  YES / NO / INCONCLUSIVE value set appears in every proposal table.
  Rows marked NO or INCONCLUSIVE are explicitly excluded from the write gate.
- **Partial (1):** An inertia verdict is applied per proposal but the three-
  value set is not named or NO/INCONCLUSIVE drop behavior is not stated.

---

### C-16 — Structured gate reply options (YES / NO / REVISED)
- **Weight:** aspirational
- **Source:** Round 4 V-01 excellence signal
- **Text:** The confirmation gate presents exactly three reply options,
  verbatim: YES (write strategy.md as proposed), NO (keep strategy.md
  unchanged), REVISED (user provides edits and the skill re-evaluates).
  An open-ended gate ("let me know how to proceed") or a binary YES/NO
  gate without the REVISED path does not satisfy this criterion.
- **Pass condition (2):** The gate section enumerates all three options by
  name with a one-line description of each outcome.
- **Partial (1):** The gate is blocking and names YES and NO but omits the
  REVISED path.

---

### C-17 — Pre-gate unmodified status declaration
- **Weight:** aspirational
- **Source:** Round 4 V-01 excellence signal
- **Text:** Immediately before the confirmation gate, an explicit declaration
  states that strategy.md has not been modified. The declaration must name
  the file by path and confirm its unmodified state. This declaration is
  structurally separate from the gate itself — it precedes the stop
  instruction rather than being part of it.
- **Pass condition (2):** A labeled status declaration names strategy.md
  and confirms unmodified state. The declaration appears before the gate
  stop instruction, not after.
- **Partial (1):** Unmodified state is confirmed but the declaration is
  embedded inside the gate text rather than appearing as a distinct section.

---

### C-18 — Active consent enforcement
- **Weight:** aspirational
- **Source:** Round 4 V-01/V-02 excellence signal
- **Text:** The confirmation gate explicitly states that the absence of a NO
  reply does not constitute YES. Passive assent — silence, timeout, partial
  acknowledgment, or any response that does not contain YES or REVISED — is
  rejected as authorization. The skill remains at the gate until an explicit
  reply matching one of the three options is received.
- **Pass condition (2):** The gate section contains a verbatim statement that
  "The absence of a NO reply does not constitute YES" or equivalent. The
  three recognized reply forms are listed as the exclusive authorization
  paths.
- **Partial (1):** Explicit confirmation is required but the rule against
  passive assent is not stated.

---

## Changes from v4 to v5

- **Formula updated:** aspirational denominator raised from 12 to 20 to
  reflect four new criteria (C-15–C-18, 2 pts each).
- **C-04 completed:** pass condition restored (was truncated in v4).
- **C-15 added:** Per-proposal inertia verdict column (YES/NO/INCONCLUSIVE);
  sourced from Round 4 V-01 section 5 pattern.
- **C-16 added:** Structured gate reply options (YES/NO/REVISED); sourced
  from Round 4 V-01 section 9/10 gate pattern.
- **C-17 added:** Pre-gate unmodified status declaration; sourced from Round 4
  V-01 "strategy.md not modified status declared" pattern.
- **C-18 added:** Active consent enforcement; sourced from Round 4 V-02
  Commitment 5 "absence of NO does not constitute YES" — a partial in V-02
  elevated to aspirational criterion.
```

---

**Key decisions:**

- **C-15 vs C-10 separation** — the inertia verdict (YES/NO/INCONCLUSIVE) is a per-row gate; the "Inertia defeated by" column (C-10) is the evidence record. Different functions, both required for full enforcement.
- **C-17 as distinct from C-04** — C-04 requires the gate to be blocking; C-17 requires a *named-file unmodified declaration before the gate*. V-01's section 9 demonstrates this split.
- **C-18 sourced from V-02** — V-02 scored partial on this (committed to active consent but didn't enumerate all three reply forms). Elevated to aspirational to reward the pattern when fully specified.
- **Formula denominator** — raised to 20; golden threshold (≥ 80) still reachable with essential + recommended full pass alone (90), so the new criteria tighten discrimination at the top without raising the floor.
