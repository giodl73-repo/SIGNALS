Written to `simulations/quest/variations/topic-roadmap-variations-R2-2026-03-17.md`.

---

## Round 2 Variations — topic-roadmap

**R1 baseline:** V-05 scored 92.5 on v1 rubric. Under v2 rubric it maps to ~90+ but leaves C-08 partial, C-09 partial, and C-11/C-12/C-13 unscored (new aspirational criteria).

---

### Single-axis variations

**V-01 — Gate output artifact specification**  
Introduces an upfront **Gate Manifest table** listing each gate's required artifact. Diff table is named Gate 4's artifact. Challenger + calibration are Gate 3's artifacts (3/3). Gate-termination nulls are declared per gate. Targets C-08 full, C-11, C-13.

**V-02 — Per-gate inertia triple enforcement**  
Three explicitly labeled inertia checkpoints (`CHECKPOINT I/II/III`), each phrased as a gate-advancement condition — not a general instruction. Checkpoint I fires at inventory (NEW count = 0 terminates), Checkpoint II fires at delta-to-proposal transition (no YES findings terminates), Checkpoint III fires per proposal row. Directly targets C-12.

**V-03 — Challenger gate mandate**  
Minimal restructuring from R1 V-05. The one change: challenger table + calibration sentence are made a **named gate-completion requirement** with an explicit "Gate does not complete without calibration sentence" rule. Closes the R1 V-05 C-09 partial gap with the smallest possible change. Targets C-09 full.

---

### Combination variations

**V-04 — V-05 R1 + artifact manifest + G-4 diff + challenger mandate**  
Builds directly on the R1 winner. Adds: (1) upfront gate manifest table, (2) diff repositioned as Gate 4's required artifact, (3) challenger table + calibration as Gate 3's three required artifacts (3/3). Closes both R1 partials (C-08, C-09). Gate manifest makes C-11 a structural consequence. Expected to score highest on v2 rubric.

**V-05 — Full gate architecture optimized for C-11/C-12/C-13**  
Designed from scratch around the three new aspirational criteria. Five named gates with explicit advancement conditions (C-12), gate-termination null vocabulary throughout (C-13), and named gate artifacts that make gate-skipping architecturally visible (C-11). Every null is a gate-termination artifact, not a convention. Challenger and diff are named gate artifacts. Most structurally rigorous variation.

---

**Predicted top performers under v2 rubric:** V-04 and V-05 are both designed to close all R1 gaps while targeting the three new aspirational criteria. V-01 targets C-11/C-13 without addressing C-09. V-02 isolates C-12. V-03 isolates C-09. Scoring will reveal whether the new aspirational criteria reward pure gate architecture (V-05) or the combination approach (V-04).
ventory table (filename, date, NEW/PRIOR, namespace) |
| G-2  | Delta            | Delta findings (all 4 categories written)        |
| G-3  | Proposals        | Proposal table + Challenger table + calibration  |
| G-4  | Diff             | Before/After diff table (Dimension / Before / After / evidence) |
| G-5  | Confirmation     | PENDING CONFIRMATION block (YES / NO / REVISED)  |

Gates G-4 and G-5 are behavior gates. G-4 produces the diff artifact.
G-5 is the blocking confirmation. strategy.md is not modified until
the user replies to G-5.

---

## G-1 — Inventory

Read `simulations/TOPICS.md`. Find the strategy file for the named topic.
Read strategy.md. Record STRATEGY DATE (last-modified or frontmatter date).

Extract every planned signal dimension. For each, note whether the
assumption is explicit or implicit.

| Assumption | Explicit / Implicit | Delta-candidate |

Glob `simulations/` for all topic artifacts. Classify each:
- NEW: artifact date > STRATEGY DATE
- PRIOR: artifact date <= STRATEGY DATE

**G-1 ARTIFACT — Signal inventory:**
| Artifact filename | Date | NEW / PRIOR | Namespace |

Check all 9 namespaces: scout / draft / review / flow / trace /
prove / listen / program / topic.

**G-1 TERMINATION:** If no NEW artifacts exist:
"G-1 TERMINATION — INERTIA HOLDS: no NEW artifacts found.
strategy.md unchanged." Stop here.

**G-1 COMPLETE** when the signal inventory table is written.
Do not open G-2 until this artifact is present.

---

## G-2 — Delta

For each NEW artifact, classify its contribution. Write all four
categories. Each entry names its source artifact and states what
understanding changed.

### CONFIRMED
NEW artifact validates an existing strategy assumption.
Format: "[source] confirms [assumption]. Prior: [X]. Now: [Y]."
**G-2 NULL (CONFIRMED):** "CONFIRMED — G-2 termination: inertia holds, no NEW artifacts confirm existing assumptions."

### EXPANDED
NEW artifact extends an assumption to broader scope.
Format: "[source] expands [assumption] to [scope]. Prior: [X]. Now: [Y]."
**G-2 NULL (EXPANDED):** "EXPANDED — G-2 termination: inertia holds, no NEW artifacts expand existing assumptions."

### UNEXPECTED
NEW artifact reveals a gap strategy.md did not cover.
Format: "[source] reveals [gap]. Prior: not covered. Now: [Y]."
**G-2 NULL (UNEXPECTED):** "UNEXPECTED — G-2 termination: inertia holds, no NEW artifacts reveal uncovered dimensions."

### CHALLENGED
NEW artifact contradicts an existing assumption.
Format: "[source] challenges [assumption]. Prior: [X]. Now contested by: [Y]."
**G-2 NULL (CHALLENGED):** "CHALLENGED — G-2 termination: inertia holds, no NEW artifacts challenge existing strategy."

Mark each finding: Delta-candidate YES / NO / Pending.

**G-2 COMPLETE** when all four categories are written (populated or null-declared).
Do not open G-3 until this artifact is present.

---

## G-3 — Proposals

**G-3 INERTIA CHECK:** Before writing any proposal row, confirm: does this
finding name a NEW artifact + reveal what strategy.md missed + name the
consequence of inaction? If not, it does not beat NO CHANGE. Do not write the row.

**G-3 ARTIFACT — Proposal table:**

For each Delta-candidate YES finding that beats the inertia check, write a proposal row.
Action type must be one of: ADD / REMOVE / REPRIORITIZE.

| # | Action | Dimension | Strategy assumed / Signal revealed | Evidence | Before | After | Confidence | If unchanged | Why this beats NO CHANGE |

"Why this beats NO CHANGE": one sentence naming the specific artifact
and what would be missed without this proposal. Generic statements fail.

Null declarations (each change type separately labeled):
"ADDITIONS — G-3 termination: inertia holds, no candidates beat NO CHANGE."
"REMOVALS — G-3 termination: inertia holds, no candidates beat NO CHANGE."
"REPRIORITIZATIONS — G-3 termination: inertia holds, no candidates beat NO CHANGE."

**G-3 ARTIFACT — Challenger table (required):**

For each proposal, write the strongest argument against making the change.

| Proposal # | Strategic decision defended | Counter-argument | Strength |

Calibration sentence (required, no exceptions):
"Calibration: [balanced / rubber-stamp risk / over-zealous risk] — [one sentence rationale]."
- All Weak ratings → rubber-stamp risk
- All Strong ratings → over-zealous risk
- Mixed → balanced

Null (if no proposals): "CHALLENGER — G-3 termination: no proposals to challenge."

**G-3 COMPLETE** when proposal table + challenger table + calibration sentence are all present.
Do not open G-4 until these three artifacts are written.

---

## Conflict check (between G-3 and G-4)

If two NEW artifacts contradict each other on the same strategy dimension,
surface the conflict before G-4 produces the diff. A proposal built on
conflicting signals is unreliable until the conflict is resolved.

| Conflict ID | Signal A | Signal B | Nature | Resolution |

Null: "CONFLICT AUDIT: none — no contradictions between NEW artifacts on the same dimension."

---

## G-4 — Diff

**G-4 ARTIFACT — Before/After diff table (required):**

Show the net effect on strategy.md if all non-withdrawn proposals apply.
Evidence reference is required in the After cell.

| Dimension | Before | After [evidence: filename] | Proposal # |

This is a required gate artifact. G-4 is not complete without this table.

Null (if no proposals survived to G-4):
"DIFF — G-4 termination: inertia holds, no proposals to diff."

**G-4 COMPLETE** when the diff table is written (populated or null-declared).
Do not open G-5 until this artifact is present.

---

## G-5 — Confirmation

**G-5 ARTIFACT — PENDING CONFIRMATION block (required, blocking):**

strategy.md has NOT been modified. It will not be modified until
the user replies to this gate.

Present G-2 (delta), G-3 (proposals + challenger), G-4 (diff) for review.

Individual proposals may be withdrawn before confirmation: WITHDRAW [#].

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited
table to apply custom version | WITHDRAW [#] to remove specific proposals
---

**STOP. Write nothing further until the user replies.**

---

## G-5 POST — Apply (after YES or REVISED only)

Apply exactly the confirmed (non-withdrawn) proposals to strategy.md.
Do not reformat unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."

If NO: "strategy.md unchanged — inertia holds."
```

---

## V-02

**Axis:** Per-gate inertia triple enforcement
**Hypothesis:** Placing three distinct, labeled inertia checkpoints — one at classification (inventory gate), one at delta-to-proposal transition, one at proposal selection — with each phrased as a gate-advancement condition creates three independent enforcement points for C-01 and C-12. A single front-loaded inertia block can be implicitly bypassed by downstream steps; three named checkpoints cannot be skipped without producing a visibly malformed output.

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
---

You are running /topic:plan for the topic named in the user's message.

---

## INERTIA PRIOR

strategy.md unchanged is the default outcome.
Change requires evidence. A run with zero proposals is valid and complete.

Three inertia enforcement points govern this skill. Each one is labeled.
The skill advances past each point only if evidence beats NO CHANGE at
that level. "Strong evidence exists" is not sufficient — the specific
artifact must be named.

---

## Step 1 — Read strategy.md

Read `simulations/TOPICS.md`. Find the strategy file for the named topic.
Read strategy.md. Record STRATEGY DATE.

List every planned signal dimension and whether each assumption is
explicit or implicit.

| Assumption | Explicit / Implicit | Delta-candidate |

---

## Step 2 — Signal inventory

Glob `simulations/` for all topic artifacts. Classify each:
- NEW: date > STRATEGY DATE
- PRIOR: date <= STRATEGY DATE

| Artifact filename | Date | NEW / PRIOR | Namespace |

Check all 9 namespaces: scout / draft / review / flow / trace /
prove / listen / program / topic.

**--- INERTIA CHECKPOINT I (inventory) ---**
This checkpoint advances only if at least one NEW artifact exists.
Condition: NEW artifact count > 0.
If NEW count = 0: output "INERTIA CHECKPOINT I: inertia holds — no NEW
artifacts found. strategy.md unchanged." Stop here.
If NEW count > 0: output "INERTIA CHECKPOINT I: advancing — [N] NEW
artifacts found, proceeding to delta analysis."
**--- END CHECKPOINT I ---**

Null (no artifacts at all): "SIGNAL INVENTORY: null — no artifacts found
for topic [name]. Cannot run /topic:plan."

SIGNAL READ-LOCK: after writing this table, signal files are closed.
All subsequent steps use only the written inventory.

---

## Step 3 — Delta analysis

For each NEW artifact, classify its contribution. Write all four
categories. Each entry names its source artifact and states what
understanding changed.

### CONFIRMED
NEW artifact validates an existing strategy assumption.
Format: "[source] confirms [assumption]. Understanding: [prior] → [now]."
Null: "CONFIRMED: none."

### EXPANDED
NEW artifact extends an assumption to broader scope.
Format: "[source] expands [assumption] to [scope]. Understanding: [prior] → [now]."
Null: "EXPANDED: none."

### UNEXPECTED
NEW artifact reveals a gap strategy.md did not cover.
Format: "[source] reveals [gap]. Understanding: [prior] → [now]."
Null: "UNEXPECTED: none."

### CHALLENGED
NEW artifact contradicts an existing strategy assumption.
Format: "[source] challenges [assumption]. Understanding: [prior] → [now]."
Null: "CHALLENGED: none."

Mark each finding: Delta-candidate YES / NO / Pending.
A finding is Delta-candidate YES only if it names: (a) NEW artifact,
(b) what it revealed, (c) consequence of not updating strategy.md.

**--- INERTIA CHECKPOINT II (delta-to-proposal transition) ---**
This checkpoint advances only if at least one Delta-candidate YES finding exists.
Condition: at least one finding carries Delta-candidate: YES.
If no YES findings: output "INERTIA CHECKPOINT II: inertia holds —
no delta findings qualify as proposal candidates. strategy.md unchanged."
Stop here.
If YES findings exist: output "INERTIA CHECKPOINT II: advancing —
[N] delta-candidate YES findings, proceeding to proposals."
**--- END CHECKPOINT II ---**

---

## Step 4 — Proposals

**--- INERTIA CHECKPOINT III (proposal selection) ---**
This checkpoint fires once per proposal candidate.
For each Delta-candidate YES finding, ask:
  (a) Does it name a specific NEW artifact?
  (b) Does it reveal something strategy.md did not account for?
  (c) Is the consequence of not acting specific and named?
If any test fails: "CHECKPOINT III — [finding ID]: inertia holds,
this finding does not beat NO CHANGE. Row not written."
If all pass: "CHECKPOINT III — [finding ID]: advancing, inertia beaten
by [artifact filename]."
**--- END CHECKPOINT III ---**

Action types: ADD / REMOVE / REPRIORITIZE.

| # | Action | Dimension | Strategy assumed / Signal revealed | Evidence |
  Before | After | Confidence | If unchanged | Inertia beaten by |

"Inertia beaten by": one sentence naming the specific artifact.
Generic statements ("strong evidence exists") do not satisfy this field.

Null declarations (per type, separately labeled):
"ADDITIONS: none — CHECKPOINT III holds, no addition candidates beat NO CHANGE."
"REMOVALS: none — CHECKPOINT III holds, no removal candidates beat NO CHANGE."
"REPRIORITIZATIONS: none — CHECKPOINT III holds, no reprioritization candidates beat NO CHANGE."

---

## Step 5 — Challenger review

For each proposal, write the strongest argument against making the change.

| Proposal # | Strategic decision defended | Counter-argument | Strength |

Calibration sentence (required):
"Calibration: [balanced / rubber-stamp risk / over-zealous risk]."
- All Weak → "rubber-stamp risk"
- All Strong → "over-zealous risk"
- Mixed → "balanced"

Null (no proposals): "CHALLENGER: none — no proposals to challenge."

---

## Step 6 — Conflict audit

If two NEW artifacts contradict each other on the same strategy dimension,
surface the conflict before any proposal referencing either artifact
proceeds to confirmation.

| Conflict ID | Signal A | Signal B | Nature | Resolution |

Null: "CONFLICT AUDIT: none — no contradictions between NEW artifacts."

---

## Step 7 — Diff table

Show the net change to strategy.md if all non-withdrawn proposals apply.
Evidence reference required in After cells.

| Dimension | Before | After [evidence: filename] | Proposal # |

Null: "DIFF: none — no proposals survive to this step."

---

## Step 8 — Confirmation gate

strategy.md has NOT been modified.

Present Steps 3, 4, 5, 6, and 7 for review.

Proposals may be individually withdrawn: WITHDRAW [#].

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited
table to apply custom version | WITHDRAW [#] to remove specific proposals
---

STOP. Write nothing further until the user replies.

---

## Step 9 — Apply (after YES or REVISED only)

Apply exactly the confirmed (non-withdrawn) proposals to strategy.md.
Do not reformat unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."

If NO: "strategy.md unchanged — inertia holds."
```

---

## V-03

**Axis:** Challenger gate mandate
**Hypothesis:** The R1 V-05 gap on C-09 was that the calibration check appeared as a gate annotation rather than a required output section. Making the Challenger table + calibration sentence a named, required gate-completion artifact — where the gate does not advance without both the table AND the calibration sentence — converts C-09 from a partial to a full pass without restructuring the rest of the skill.

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
---

You are running /topic:plan for the topic named in the user's message.

---

## INERTIA PRIOR

strategy.md unchanged is the default outcome. Change requires evidence
from NEW signal artifacts. A run that produces zero proposals is valid
and complete.

---

## Step 1 — Read strategy.md

Read `simulations/TOPICS.md`. Find the strategy file for the named topic.
Read strategy.md. Record STRATEGY DATE.

List every planned signal dimension.

| Assumption | Explicit / Implicit | Delta-candidate |

Null: "ASSUMPTIONS: none — all dimensions explicitly stated."

---

## Step 2 — Signal inventory

Glob `simulations/` for all topic artifacts.

| Artifact filename | Date | NEW / PRIOR | Namespace |

NEW = date > STRATEGY DATE. PRIOR = date <= STRATEGY DATE.

Check all 9 namespaces: scout / draft / review / flow / trace /
prove / listen / program / topic.

SIGNAL READ-LOCK: after writing this table, signal files are closed.

If no NEW artifacts: "INERTIA HOLDS — no NEW artifacts found.
strategy.md unchanged." Stop here.

Null (no artifacts at all): "SIGNAL INVENTORY: null — no artifacts
found for topic [name]. Cannot run /topic:plan."

---

## Step 3 — Delta analysis

For each NEW artifact, classify its contribution. Write all four
categories. Each entry names its source artifact and states what
understanding changed.

### CONFIRMED
NEW artifact validates an existing assumption.
Format: "[source] confirms [assumption]. Prior: [X]. Now: [Y]."
Null: "CONFIRMED: none."

### EXPANDED
NEW artifact extends an assumption to broader scope.
Format: "[source] expands [assumption] to [scope]. Prior: [X]. Now: [Y]."
Null: "EXPANDED: none."

### UNEXPECTED
NEW artifact reveals a gap strategy.md did not cover.
Format: "[source] reveals [gap]. Prior: not covered. Now: [Y]."
Null: "UNEXPECTED: none."

### CHALLENGED
NEW artifact contradicts an existing assumption.
Format: "[source] challenges [assumption]. Prior: [X]. Now contested by: [Y]."
Null: "CHALLENGED: none."

Mark each finding: Delta-candidate YES / NO / Pending.

--- STEP 3 COMPLETE ---
Do not write Step 4 until all four delta categories are written above.

---

## Step 4 — Proposals

For each Delta-candidate YES finding, write a proposal row only if it
names a NEW artifact, reveals something strategy.md missed, and names
the consequence of inaction. If any test fails, the finding does not
produce a proposal.

Action types: ADD / REMOVE / REPRIORITIZE.

| # | Action | Dimension | Strategy assumed / Signal revealed | Evidence |
  Before | After | Confidence | If unchanged | Why this beats NO CHANGE |

"Why this beats NO CHANGE": one sentence naming the specific artifact.
Generic statements do not satisfy this field.

Null declarations (per type, separately labeled):
"ADDITIONS: none — inertia holds."
"REMOVALS: none — inertia holds."
"REPRIORITIZATIONS: none — inertia holds."

---

## Step 5 — CHALLENGER GATE (required, non-skippable)

This is a required gate. Step 6 does not open until both the
Challenger table AND the calibration sentence are written here.

**Challenger table:**

For each proposal in Step 4, write the strongest argument against
making the change. Rate challenge strength: Strong / Moderate / Weak.

| Proposal # | Strategic decision defended | Counter-argument | Strength |

A Challenger table with fewer rows than proposals is incomplete.
If no proposals exist: "CHALLENGER GATE: no proposals to challenge.
Gate artifact: null — no proposals reached Step 4."

**Calibration sentence (required regardless of proposal count):**

Write exactly one calibration sentence in this format:
"Calibration: [balanced / rubber-stamp risk / over-zealous risk] —
challenge strength distribution [description]."

Rules:
- All Weak ratings → "rubber-stamp risk"
- All Strong ratings → "over-zealous risk"
- Mixed distribution → "balanced"
- Absence of this sentence means Step 5 is incomplete. Do not open Step 6.

--- STEP 5 COMPLETE when: Challenger table written (or null declared) +
calibration sentence written. Both required. ---

---

## Step 6 — Conflict audit

If two NEW artifacts contradict each other on the same strategy dimension,
surface the conflict before any proposal that references either artifact
proceeds to confirmation.

| Conflict ID | Signal A | Signal B | Nature | Resolution |

Null: "CONFLICT AUDIT: none — no contradictions between NEW artifacts
on the same strategy dimension."

---

## Step 7 — Diff table

Show the net change to strategy.md if all non-withdrawn proposals apply.
Evidence reference required in After cells.

| Dimension | Before | After [evidence: filename] | Proposal # |

Null: "DIFF: none — no proposals to diff."

---

## Step 8 — Confirmation gate

strategy.md has NOT been modified.

Present Steps 3, 4, 5, 6, and 7 for review.

Proposals may be individually withdrawn: WITHDRAW [#].

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited
table to apply custom version | WITHDRAW [#] to remove specific proposals
---

STOP. Write nothing further until the user replies.

---

## Step 9 — Apply (after YES or REVISED only)

Apply exactly the confirmed (non-withdrawn) proposals to strategy.md.
Do not reformat unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."

If NO: "strategy.md unchanged."
```

---

## V-04

**Axis:** V-05 R1 base + artifact manifest + diff as Gate 4 artifact + challenger mandate
**Hypothesis:** Combining the R1 winner's gate architecture with (1) an upfront artifact manifest that makes each gate's required output visible, (2) a diff table repositioned as Gate 4's named artifact, and (3) a challenger table made a required Gate 3 completion requirement will close the R1 gaps on C-08 and C-09 while inheriting V-05 R1's full essential pass. The manifest makes C-11 a structural consequence of following the table.

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
---

You are running /topic:plan for the topic named in the user's message.

---

## INERTIA PRIOR

strategy.md unchanged is the default outcome. Change requires evidence
from NEW signal artifacts. A run that produces zero proposals is valid
and complete. The burden of proof rests on every proposal row.

---

## GATE MANIFEST

This skill executes through five named gates. Each gate has a required
completion artifact. A gate is not complete without its artifact.
Inertia check conditions govern when a gate terminates early.

| Gate | Name         | Completion artifact                                    | Inertia termination condition |
|------|--------------|--------------------------------------------------------|-------------------------------|
| G-1  | Inventory    | Signal inventory table (filename / date / NEW-PRIOR / namespace) | No NEW artifacts found |
| G-2  | Delta        | Delta findings (all 4 categories, populated or null)   | No Delta-candidate YES findings |
| G-3  | Proposals    | Proposal table + Challenger table + calibration sentence | No proposals survive inertia check |
| G-4  | Diff         | Before/After diff table (Dimension / Before / After / evidence) | No proposals survived G-3 |
| G-5  | Confirmation | PENDING CONFIRMATION block (YES / NO / REVISED)        | — (always runs if G-4 reached) |

The gate manifest defines the full execution path. Do not produce
artifacts out of gate order. Do not skip a gate or its artifact.

---

## G-1 — Inventory

Read `simulations/TOPICS.md`. Find the strategy file for the named topic.
Read strategy.md. Record STRATEGY DATE.

List every planned signal dimension and whether each is explicit or implicit.

| Assumption | Explicit / Implicit | Delta-candidate |

Glob `simulations/` for all topic artifacts.

**G-1 COMPLETION ARTIFACT — Signal inventory:**
| Artifact filename | Date | NEW / PRIOR | Namespace |

Check all 9 namespaces: scout / draft / review / flow / trace /
prove / listen / program / topic.

SIGNAL READ-LOCK: after writing this table, signal files are closed.

**[INERTIA CHECK G-1]** This gate advances only if at least one NEW
artifact exists. If NEW count = 0:
"G-1 TERMINATION — INERTIA HOLDS: no NEW artifacts found.
strategy.md unchanged." Stop here.

**G-1 COMPLETE.** Do not open G-2 until the signal inventory artifact is written.

---

## G-2 — Delta

For each NEW artifact, classify its contribution. Write all four
categories. Each entry: source artifact + what understanding changed.

### CONFIRMED
NEW artifact validates an existing assumption.
Format: "[source] confirms [assumption]. Prior: [X]. Now: [Y]."
**G-2 NULL (CONFIRMED):** "CONFIRMED — G-2 termination: inertia holds,
no NEW artifacts confirm existing assumptions."

### EXPANDED
NEW artifact extends an assumption to broader scope.
Format: "[source] expands [assumption] to [scope]. Prior: [X]. Now: [Y]."
**G-2 NULL (EXPANDED):** "EXPANDED — G-2 termination: inertia holds,
no NEW artifacts expand existing assumptions."

### UNEXPECTED
NEW artifact reveals a gap strategy.md did not cover.
Format: "[source] reveals [gap]. Prior: not covered. Now: [Y]."
**G-2 NULL (UNEXPECTED):** "UNEXPECTED — G-2 termination: inertia holds,
no NEW artifacts reveal uncovered dimensions."

### CHALLENGED
NEW artifact contradicts an existing assumption.
Format: "[source] challenges [assumption]. Prior: [X]. Now contested by: [Y]."
**G-2 NULL (CHALLENGED):** "CHALLENGED — G-2 termination: inertia holds,
no NEW artifacts challenge existing strategy."

Mark each finding: Delta-candidate YES / NO / Pending.

**[INERTIA CHECK G-2]** This gate advances only if at least one
Delta-candidate YES finding exists. If none:
"G-2 TERMINATION — INERTIA HOLDS: no delta findings qualify as proposal
candidates. strategy.md unchanged." Stop here.

**G-2 COMPLETE.** Do not open G-3 until all four delta categories are written.

---

## G-3 — Proposals

**[INERTIA CHECK G-3]** Before writing any row, confirm per finding:
  (a) Names a specific NEW artifact?
  (b) Reveals something strategy.md did not account for?
  (c) Names the consequence of inaction?
If any test fails: inertia holds at G-3 for this finding. Do not write the row.

Action types: ADD / REMOVE / REPRIORITIZE.

**G-3 COMPLETION ARTIFACT (1/3) — Proposal table:**

| # | Action | Dimension | Strategy assumed / Signal revealed | Evidence |
  Before | After | Confidence | If unchanged | Inertia beaten by |

"Inertia beaten by": one sentence naming the specific artifact.

Null declarations (per type, separately labeled):
"ADDITIONS — G-3 termination: inertia holds, no addition candidates beat NO CHANGE."
"REMOVALS — G-3 termination: inertia holds, no removal candidates beat NO CHANGE."
"REPRIORITIZATIONS — G-3 termination: inertia holds, no reprioritization candidates beat NO CHANGE."

**G-3 COMPLETION ARTIFACT (2/3) — Challenger table:**

For each proposal, write the strongest argument against making the change.

| Proposal # | Strategic decision defended | Counter-argument | Strength |

Null (no proposals): "CHALLENGER — G-3 termination: no proposals to challenge."

**G-3 COMPLETION ARTIFACT (3/3) — Calibration sentence (required, non-omittable):**

Write exactly one sentence:
"Calibration: [balanced / rubber-stamp risk / over-zealous risk] — [one-sentence rationale]."

Rules: All Weak → rubber-stamp risk. All Strong → over-zealous risk. Mixed → balanced.
This sentence is a required G-3 artifact. G-3 is not complete without it.
Even when no proposals exist: "Calibration: N/A — no proposals reached G-3."

**G-3 COMPLETE** when all three artifacts are written.
Do not open G-4 until proposal table + challenger table + calibration are present.

---

## Conflict audit (G-3 to G-4 interstitial)

Check for contradictions between NEW artifacts on the same dimension.

| Conflict ID | Signal A | Signal B | Nature | Resolution |

Null: "CONFLICT AUDIT: none — no contradictions between NEW artifacts
on the same strategy dimension."

---

## G-4 — Diff

**G-4 COMPLETION ARTIFACT — Before/After diff table:**

Show the net change to strategy.md if all non-withdrawn proposals apply.
Evidence reference is required in every After cell.

| Dimension | Before | After [evidence: filename] | Proposal # |

This table is a required gate artifact. G-4 is not complete without it.

**G-4 NULL:** "DIFF — G-4 termination: inertia holds, no proposals reached G-4."

**G-4 COMPLETE.** Do not open G-5 until the diff artifact is written.

---

## G-5 — Confirmation

**G-5 COMPLETION ARTIFACT — PENDING CONFIRMATION block:**

strategy.md has NOT been modified. It will not be modified until
the user replies to this gate.

Present G-2, G-3, G-4 for review.

Individual proposals may be withdrawn: WITHDRAW [#].

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited
table to apply custom version | WITHDRAW [#] to remove specific proposals
---

STOP. Write nothing further until the user replies.

---

## G-5 POST — Apply (after YES or REVISED only)

Apply exactly the confirmed (non-withdrawn) proposals to strategy.md.
Do not reformat unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."

If NO: "strategy.md unchanged — inertia holds."
```

---

## V-05

**Axis:** Full gate architecture optimized for C-11/C-12/C-13
**Hypothesis:** Building the skill from the ground up around three structural properties — (1) 5 named gates with explicit gate-termination null artifacts, (2) three independent inertia checkpoints each phrased as an advancement condition, (3) all null declarations produced as gate-termination artifacts rather than instructed conventions — makes C-11/C-12/C-13 pass as structural consequences. C-07 compliance becomes impossible to fail without skipping the gate itself. The diff table and challenger table are named gate artifacts (C-08/C-09 full), and the confirmation is Gate 5 (C-04/C-05 structural). No analytical depth is sacrificed; the architecture enhances it.

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
---

You are running /topic:plan for the topic named in the user's message.

---

## INERTIA PRIOR

strategy.md unchanged is the default outcome. Change requires evidence.
A run with zero proposals is valid and complete.

---

## GATE ARCHITECTURE — five structural gates

Execution flows through five gates in sequence. Each gate produces a
named artifact or a gate-termination null. A gate does not complete
until its artifact is written. Nothing outside a gate's artifact
section belongs to that gate's output.

The three inertia enforcement points are labeled within their gates.
Each is phrased as an advancement condition. Passing the condition
produces output. Failing the condition produces the gate's termination
null and stops execution at that gate.

---

## GATE 1 — INVENTORY

**Advancement condition:** At least one NEW artifact exists.

Read `simulations/TOPICS.md`. Find the strategy file for the named topic.
Read strategy.md. Record STRATEGY DATE.

List every planned signal dimension. For each, note explicit or implicit.
| Assumption | Explicit / Implicit | Delta-candidate |

Glob `simulations/` for all topic artifacts. Classify each:
- NEW: date > STRATEGY DATE
- PRIOR: date <= STRATEGY DATE

**GATE 1 ARTIFACT — Signal inventory:**
| Artifact filename | Date | NEW / PRIOR | Namespace |

Check all 9 namespaces: scout / draft / review / flow / trace /
prove / listen / program / topic.

SIGNAL READ-LOCK: signal files closed after this table is written.

**GATE 1 ADVANCEMENT CHECK:**
Condition: NEW artifact count > 0.
  PASS → "GATE 1: advancing — [N] NEW artifacts, proceeding to delta."
  FAIL → "GATE 1 TERMINATION — INERTIA HOLDS: no NEW artifacts found.
           strategy.md unchanged." Stop here.

---

## GATE 2 — DELTA

**Advancement condition:** At least one Delta-candidate YES finding exists.

For each NEW artifact, classify its finding. Write all four categories.
Each entry names its source artifact and states what understanding changed.

### CONFIRMED
NEW artifact validates an existing assumption.
Format: "[source] confirms [assumption]. Prior: [X]. Now: [Y]."
  GATE 2 TERMINATION NULL (CONFIRMED):
  "GATE 2 TERMINATION (CONFIRMED) — INERTIA HOLDS: no NEW artifacts
   confirm existing assumptions."

### EXPANDED
NEW artifact extends an assumption to broader scope.
Format: "[source] expands [assumption] to [scope]. Prior: [X]. Now: [Y]."
  GATE 2 TERMINATION NULL (EXPANDED):
  "GATE 2 TERMINATION (EXPANDED) — INERTIA HOLDS: no NEW artifacts
   expand existing assumptions."

### UNEXPECTED
NEW artifact reveals a gap strategy.md did not cover.
Format: "[source] reveals [gap]. Prior: not covered. Now: [Y]."
  GATE 2 TERMINATION NULL (UNEXPECTED):
  "GATE 2 TERMINATION (UNEXPECTED) — INERTIA HOLDS: no NEW artifacts
   reveal uncovered dimensions."

### CHALLENGED
NEW artifact contradicts an existing assumption.
Format: "[source] challenges [assumption]. Prior: [X]. Now contested by: [Y]."
  GATE 2 TERMINATION NULL (CHALLENGED):
  "GATE 2 TERMINATION (CHALLENGED) — INERTIA HOLDS: no NEW artifacts
   challenge existing strategy."

Mark each finding: Delta-candidate YES / NO / Pending.

**GATE 2 ADVANCEMENT CHECK:**
Condition: at least one finding carries Delta-candidate: YES.
  PASS → "GATE 2: advancing — [N] Delta-candidate YES findings."
  FAIL → "GATE 2 TERMINATION — INERTIA HOLDS: no delta findings qualify
           as proposal candidates. strategy.md unchanged." Stop here.

---

## GATE 3 — PROPOSALS + CHALLENGER + CALIBRATION

**Advancement condition:** At least one proposal row beats the inertia check.

This gate produces three required artifacts. Gate 3 does not complete
until all three are written.

**Inertia check (per-row, fires before each proposal row):**
Before writing a row, confirm:
  (a) Names a specific NEW artifact?
  (b) Reveals something strategy.md did not account for?
  (c) Names the specific consequence of inaction?
If any test fails:
  "GATE 3 TERMINATION (row [finding ID]) — INERTIA HOLDS: finding does
   not beat NO CHANGE. Row not written."
If all pass:
  "GATE 3 ADVANCING (row [finding ID]): inertia beaten by [artifact filename]."

Action types: ADD / REMOVE / REPRIORITIZE.

**GATE 3 ARTIFACT 1 — Proposal table:**

| # | Action | Dimension | Strategy assumed / Signal revealed | Evidence |
  Before | After | Confidence | If unchanged | Inertia beaten by |

Per-type gate-termination nulls (each labeled):
  "GATE 3 TERMINATION (ADDITIONS) — INERTIA HOLDS: no addition candidates beat NO CHANGE."
  "GATE 3 TERMINATION (REMOVALS) — INERTIA HOLDS: no removal candidates beat NO CHANGE."
  "GATE 3 TERMINATION (REPRIORITIZATIONS) — INERTIA HOLDS: no reprioritization candidates beat NO CHANGE."

**GATE 3 ARTIFACT 2 — Challenger table (required):**

For each proposal row in Artifact 1, write the strongest argument
against making the change.

| Proposal # | Strategic decision defended | Counter-argument | Strength |

Gate-termination null (no proposals):
  "GATE 3 TERMINATION (CHALLENGER) — INERTIA HOLDS: no proposals reached challenger gate."

**GATE 3 ARTIFACT 3 — Calibration sentence (required, non-omittable):**

Write exactly one sentence assessing the challenger strength distribution:
  "Calibration: [balanced / rubber-stamp risk / over-zealous risk] — [one-sentence rationale]."

Rules:
- All Weak → rubber-stamp risk (the proposals were not meaningfully tested)
- All Strong → over-zealous risk (the challenger may be blocking sound proposals)
- Mixed → balanced

Gate-termination null (no proposals): "Calibration: N/A — no proposals reached Gate 3."

This sentence is a required gate artifact. Gate 3 does not complete without it.

**Conflict interstitial (Gate 3 → Gate 4):**

Before advancing to Gate 4, check: do any two NEW artifacts contradict
each other on the same strategy dimension?

| Conflict ID | Signal A | Signal B | Nature | Resolution |

Gate-termination null: "CONFLICT AUDIT: none — no contradictions
between NEW artifacts on the same strategy dimension."

**GATE 3 COMPLETE** when Artifact 1 + Artifact 2 + Artifact 3 are all present.

---

## GATE 4 — DIFF

**This gate produces the diff artifact. Gate 4 does not complete without it.**

**GATE 4 ARTIFACT — Before/After diff table:**

Show the net change to strategy.md if all non-withdrawn proposals apply.
Evidence reference is required in every After cell.

| Dimension | Before | After [evidence: filename] | Proposal # |

Gate-termination null:
  "GATE 4 TERMINATION — INERTIA HOLDS: no proposals reached Gate 4.
   Diff table: null."

**GATE 4 COMPLETE** when the diff table artifact is written (populated or null).

---

## GATE 5 — CONFIRMATION

**This gate produces the confirmation block artifact. It is blocking.**
**strategy.md is not modified until the user replies to this gate.**

Present Gate 2, Gate 3, Gate 4 artifacts for review.

Individual proposals may be withdrawn before confirmation: WITHDRAW [#].

**GATE 5 ARTIFACT — PENDING CONFIRMATION block:**

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited
table to apply custom version | WITHDRAW [#] to remove specific proposals
---

**STOP. Write nothing further until the user replies.**

---

## GATE 5 POST — Apply (after YES or REVISED only)

Apply exactly the confirmed (non-withdrawn) proposals to strategy.md.
Do not reformat unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."

If NO: "strategy.md unchanged — Gate 5 termination, inertia holds."
```

---

## Variation Summary

| ID | Axis | Hypothesis | Key distinguishing mechanism | Primary targets |
|----|------|-----------|------------------------------|-----------------|
| V-01 | Gate output artifact specification | Named gate artifacts make C-08/C-11/C-13 structural | Gate manifest table; each gate has a labeled artifact requirement; diff = Gate 4 artifact | C-08 full, C-11, C-13 |
| V-02 | Per-gate inertia triple enforcement | 3 labeled checkpoints phrased as advancement conditions create 3 independent enforcement points | CHECKPOINT I/II/III labels; each phrased "this gate advances only if X"; per-finding checkpoint at proposal level | C-12, C-01 strengthened |
| V-03 | Challenger gate mandate | Making calibration sentence a required gate artifact (not annotation) converts C-09 partial → full | "CHALLENGER GATE" section; gate does not advance without calibration sentence; null explicitly declared | C-09 full |
| V-04 | V-05 R1 + artifact manifest + G-4 diff + challenger mandate | Manifest makes C-11 structural; G-4 diff artifact fixes C-08; challenger mandate fixes C-09 | Upfront gate manifest table; G-3 three artifacts; G-4 diff table; all gates labeled | C-08 full, C-09 full, C-11, C-13 |
| V-05 | Full gate architecture optimized for C-11/C-12/C-13 | Gate-termination nulls as structural byproducts make C-13 a consequence, not a convention | 5 named gates; per-gate inertia advancement conditions; gate-termination null vocabulary throughout; all artifacts labeled | C-11, C-12, C-13, C-08 full, C-09 full |
