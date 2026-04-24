Reading the scorecard carefully, the 8 scored aspirational patterns map to C-09–C-16. C-17 and C-18 were unscored ("content not provided"). The two new criteria I'll extract from excellence signals not yet formalized: (1) guards labeled with the bias they block, and (2) WITHDRAW as a row-level partial-acceptance operator distinct from NO.

Here is the complete rubric v6:

```markdown
---
skill: quest-rubric
skill_target: topic-roadmap
date: 2026-03-17
version: 6
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
- **Text:** After producing the Defeat Assessment and Proposal Table, the skill
  halts with an explicit stop instruction and presents the user with structured
  reply modes. No apply step executes without a user reply.
- **Pass condition:** The output renders the Defeat Assessment and Proposal
  Table, then writes an explicit stop instruction ("Stop here. Do not write
  anything further until the user replies" or equivalent). Four reply modes
  are defined: YES (accept all), NO (reject all), REVISED + edited table
  (partial accept via table edit), WITHDRAW [#] (row-level removal). A skill
  that writes changes to strategy.md before receiving a reply fails.

---

### C-05 — Apply is write-only and scope-bounded
- **Weight:** essential
- **Category:** behavior
- **Text:** The apply step writes exactly the confirmed changes to strategy.md.
  It does not re-evaluate signals, introduce new proposals, or modify
  dimensions not listed in confirmed proposals.
- **Pass condition:** Apply section is scoped to "write exactly the confirmed
  changes." No dimension outside the confirmed proposal set is touched.
  An apply step that narrates its reasoning, introduces additional suggestions,
  or modifies unconfirmed dimensions fails.

---

## Recommended Criteria (at least 2 of 3 must pass)

### C-06 — Null path vocabulary is type-labeled
- **Weight:** recommended
- **Category:** correctness
- **Text:** Null declarations use consistent vocabulary that distinguishes
  outcome type. "Null path complete" signals a valid zero-change run.
  "Null path did not complete" signals that gates were not reached.
  Per-delta-category nulls and per-proposal-table nulls are separately labeled.
- **Pass condition:** At least one type-labeled null declaration is present.
  "PROPOSALS: null -- no NEW artifacts defeated inertia" or equivalent appears
  when no proposals are generated. Terminal phrase distinguishes complete from
  incomplete null path.

---

### C-07 — Namespace coverage is enforced
- **Weight:** recommended
- **Category:** completeness
- **Text:** All 9 namespaces (scout / draft / review / flow / trace / prove /
  listen / program / topic) are assessed explicitly in the signal inventory.
  A signal inventory that omits namespaces without explanation fails.
- **Pass condition:** The signal inventory mandates assessment of all 9
  namespaces. Each namespace appears in the inventory table with at least
  a null entry if no artifacts exist for it.

---

### C-08 — Consequence-of-no-change is required per proposal
- **Weight:** recommended
- **Category:** depth
- **Text:** Every proposal must state what happens if the strategy is NOT
  updated. This prevents proposals that feel compelling but carry no actual
  cost to inaction.
- **Pass condition:** Either the proposal table has a "Consequence of no
  change" column, or the Defeat Assessment table requires a stated consequence
  as a condition for a proposal to advance. Proposals lacking a consequence
  statement do not pass the defeat assessment.

---

## Aspirational Criteria (scored 0 / 1 / 2 per criterion; max = 20)

### C-09 — Inertia Defense Protocol pre-registered before signal read
- **Text:** The skill pre-registers its inertia defense for each active
  strategy dimension before reading any signal artifact. This prevents
  anchor bias: the defense is written without knowledge of what the signals say.
- **Full pass (2):** A defense table appears before the signal inventory step,
  with one row per active strategy dimension and a "Best reason to keep
  unchanged / What would defeat this" pair per row.
- **Partial (1):** Defense is present but appears after the signal inventory
  or is not per-dimension.
- **Fail (0):** No pre-signal defense present.

---

### C-10 — SIGNAL READ-LOCK enforced after inventory is written
- **Text:** Once the signal inventory is written, signal files may not be
  re-read. This prevents post-hoc rationalization: the evidence record is
  fixed before evaluation begins.
- **Full pass (2):** An explicit read-lock instruction appears in the prompt
  ("signal files may not be re-read after inventory is written" or
  equivalent). The step structure enforces this sequentially.
- **Partial (1):** Sequencing implies the lock but no explicit instruction
  is present.
- **Fail (0):** No read-lock or sequential enforcement present.

---

### C-11 — Defeat Assessment is an intermediate layer between evidence and proposals
- **Text:** The skill does not move directly from signal inventory to proposals.
  A Defeat Assessment step appears between them, evaluating each inertia
  defense against the inventory before any proposal is generated.
- **Full pass (2):** A distinct Defeat Assessment section appears between the
  signal inventory and the proposal table. Each defense entry is evaluated
  and marked defeated or held.
- **Partial (1):** Assessment is present but merged with either the inventory
  or the proposal table.
- **Fail (0):** No intermediate assessment layer present.

---

### C-12 — Inertia defense table includes "What would defeat this" column
- **Text:** The pre-signal defense table operationalizes its defeat criterion
  before it is tested. Each dimension states in advance what evidence would
  overturn it, making the defeat assessment falsifiable rather than
  retrospective.
- **Full pass (2):** Defense table has an explicit "What would defeat this"
  column with per-dimension entries written before signal read.
- **Partial (1):** Defeat criterion is described in prose but not per-dimension
  in a structured column.
- **Fail (0):** No defeat criterion stated before signal read.

---

### C-13 — Null declaration is total across all output sections
- **Text:** Null declarations cover every structured output section independently.
  Per-delta-category nulls and per-proposal-table nulls are separate. There
  are no silent partial nulls: if a section has nothing to report, it says so
  explicitly.
- **Full pass (2):** Null declaration is present for all four delta categories
  (even if empty) AND for the proposal table. No section is silently omitted.
- **Partial (1):** Null declaration covers the proposal table but not all delta
  categories, or vice versa.
- **Fail (0):** No null declaration structure present.

---

### C-14 — Confirmation gate offers four structured reply modes
- **Text:** The confirmation gate does not present a binary yes/no. Four
  reply modes are defined: YES (accept all), NO (reject all), REVISED +
  edited table (partial accept via inline edit), WITHDRAW [#] (row-level
  removal). This gives the user surgical control without restarting.
- **Full pass (2):** All four reply modes are explicitly named and defined
  at the confirmation gate.
- **Partial (1):** At least two reply modes are defined, including one
  partial-acceptance mode (REVISED or WITHDRAW).
- **Fail (0):** Only YES/NO or no structured modes defined.

---

### C-15 — Completion verb distinguishes outcome type
- **Text:** The terminal phrase of a run names the outcome type, not just
  completion. "Null path complete" and "Null path did not complete" are
  distinct. A run that reaches apply emits a different terminal phrase than
  one that halts at inertia.
- **Full pass (2):** Terminal phrases are outcome-typed. At minimum: null
  path complete / null path did not complete / proposals applied are distinct.
- **Partial (1):** A completion phrase is present but does not distinguish
  outcome type.
- **Fail (0):** No terminal phrase or completion signal present.

---

### C-16 — Consequence-of-no-change appears in both Defeat Assessment and Proposal Table
- **Text:** The consequence of inaction is enforced at two stages: at the
  Defeat Assessment (to qualify for proposal generation) and at the Proposal
  Table (as a visible column for user review). Single-stage enforcement
  allows consequences to be stated but invisible to the user at decision time.
- **Full pass (2):** Consequence appears as a required field in the Defeat
  Assessment table AND as a column in the Proposal Table.
- **Partial (1):** Consequence is required in one of the two locations but
  not both.
- **Fail (0):** Consequence of no change is not required at any stage.

---

### C-17 — Each structural guard is labeled with the bias it blocks
- **Text:** Guards (pre-registration, read-lock, defeat assessment) are not
  presented as process steps alone. Each names the cognitive failure it
  prevents (e.g., "prevents anchor bias," "prevents post-hoc rationalization").
  This transforms procedural compliance into epistemic commitment and makes
  the rationale auditable.
- **Full pass (2):** At least three guards are each labeled with a named
  bias or failure mode they block. Labels appear inline, not in a separate
  rationale section.
- **Partial (1):** At least one guard is labeled with a named failure mode,
  or all guards are labeled but in a separate rationale section only.
- **Fail (0):** Guards are described procedurally with no failure-mode labels.

---

### C-18 — WITHDRAW operator is distinct from NO and REVISED
- **Text:** The WITHDRAW [#] reply mode is a row-level removal operator: it
  removes specific proposals from the table without rejecting the rest and
  without requiring the user to re-edit the full table. It is distinct from
  NO (reject all) and REVISED (table edit requiring re-submission). This
  enables surgical partial acceptance in a single reply.
- **Full pass (2):** WITHDRAW [#] is defined with row-level semantics.
  The skill's apply step handles a WITHDRAW reply by removing only the
  named rows and applying the remainder. The distinction from NO and REVISED
  is explicit.
- **Partial (1):** WITHDRAW is mentioned or implied as a reply mode but its
  row-level semantics or distinction from REVISED is not spelled out.
- **Fail (0):** WITHDRAW is absent or collapsed into REVISED or NO.
```

The two new criteria:

- **C-17** captures the pattern from V-01 where every guard was paired with a named bias ("prevents anchor bias," "prevents post-hoc rationalization"). This was observable in V-01 scoring but not yet a standalone criterion.
- **C-18** formalizes the WITHDRAW operator that scored partially in C-14 — WITHDRAW as row-level surgical rejection is meaningfully distinct from REVISED (table resubmission) and deserves its own criterion with precise semantics.
