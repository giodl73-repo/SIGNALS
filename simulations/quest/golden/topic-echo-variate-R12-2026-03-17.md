---
skill: quest-variate
skill_target: topic-echo
topic: topic-reflect
date: 2026-03-17
round: 12
rubric: v11
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v11-2026-03-16.md
rubric_max: 200
---

# Quest Variate — topic-echo (topic-reflect) — Round 12

**Rubric:** v11 (2026-03-16) | **Criteria:** 30 (5 essential / 3 recommended / 22 aspirational)
**Essential max:** 60 | **Recommended max:** 30 | **Aspirational max:** 110 | **Total max:** 200
**Golden threshold:** all C-01–C-05 pass AND composite ≥ 100

---

## Design Context

Round 11 V-01 achieves 170/190 under v10, blocked only by the Stage 6 absence (C-02 fail — 60
pts lost from the essential tier). Two structural patterns from R11 excellence are now v11
criteria: C-29 (Field Reference block before the entry loop) and C-30 (calibration entry
live/example boundary marker). All R12 variations carry the full R11 base — Field Reference,
Surprise 0 with boundary marker, Build Risk triple-anchor, four-field ✓ checklist gate — and
fix the C-02 failure by restoring Stage 6.

**What R12 is testing:**

All five variations satisfy C-29 and C-30 as established base. The variation axes test whether
the register, framing, and structural organization of the Field Reference block and its
surrounding context further affect compliance. Three single-axis variations isolate one axis
each; two combined variations stack axes to test whether they compound.

**Variation axes:**

- V-01 (single): Phrasing register — formal/specification (SHALL/MUST language)
- V-02 (single): Lifecycle emphasis — gate anatomy (gate opens / gate closes framing)
- V-03 (single): Role sequence — three named roles (Historian, Challenger, Synthesizer)
- V-04 (combined): Conversational register + fill-in templates with inline worked examples
- V-05 (combined): Role sequence + inertia framing (Inertia Test + delta framing per entry)

---

## V-01

**Variation axis:** Phrasing register — formal/specification
**Hypothesis:** SHALL/MUST imperative language and numbered execution requirements eliminate
ambiguity about whether instructions are optional. The Field Reference block formatted as
numbered sub-specifications with SHALL requirements creates a formal contract the model
verifies against each entry, reducing omission errors in complex multi-field outputs. When
instructions are stated as requirements rather than suggestions, the COMMIT-ENTRY gate feels
like a compliance check rather than a courtesy reminder.

---

```
# topic-reflect — Skill Body Prompt (V-01: Formal/Specification Register)

## PURPOSE

This skill synthesizes unexpected findings from signal artifacts gathered for a topic. For each
surprise: name it, trace it to its source signal, assess design impact, name build risk. The
output is a reflect artifact suitable for team review and program advancement decisions.

---

## GATE SEQUENCE OVERVIEW

| Stage | Token Emitted | Halt Condition | Flow |
|-------|--------------|----------------|------|
| Stage 1 | COMMIT-STAGE-1 | < 3 beliefs listed | STOP |
| Stage 2 | COMMIT-STAGE-2 | 0 artifacts | STOP |
| Stage 3 | GATE-CONFIRMED or GATE-REJECTED | — | Proceed to Stage 3.5 |
| Stage 3.5 | COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED | FLAGGED | STOP |
| Stage 4 | COMMIT-ENTRY (per entry) + COMMIT-STAGE-4 | < 2 GATE-CONFIRMED entries | Extend sweep |
| Stage 5 | COMMIT-STAGE-5 | — | Proceed |
| Stage 6 | COMMIT-STAGE-6 | FOREKNOWLEDGE-FLAGGED unresolved | STOP |
| Stage 7 | COMMIT-STAGE-7 | — | Artifact written |

---

## VOCABULARY RULE — CLOSED DIMENSION SET

**Requirement 1.** The model SHALL use only the following five canonical dimension names:

  Feasibility · Usability · Scalability · Adoptability · Correctness

**Requirement 2.** The following synonym names are PROHIBITED and SHALL NOT appear in any
dimension field:

  | Prohibited | Canonical Substitute |
  |-----------|---------------------|
  | Reliability | Correctness |
  | Performance | Scalability |
  | Maintainability | Correctness |
  | Learnability | Usability |
  | Viability | Feasibility |

**Requirement 3.** At every Stage EXIT gate, the model SHALL scan all dimension values in that
stage's output and replace any prohibited name with its canonical substitute before emitting
the stage commit token.

**Requirement 4.** Any dimension value not in the closed set is a vocabulary violation and
SHALL be corrected before the commit token is emitted.

---

## STAGE 1 — OPENING MODEL AND EPISTEMIC PROFILE

**ENTER contract:** Topic name and artifact list are available. If no artifacts exist, halt:
"No signal artifacts found. topic-reflect requires at least one source signal."

**Execution Requirements:**

1.1. The model SHALL state the topic name and summarize the feature intent in two to four
sentences. This is the Opening Model.

1.2. The model SHALL produce an Epistemic Profile: a one-paragraph characterization of how
well-understood this topic was before evidence gathering began. The Epistemic Profile SHALL
address: (a) team confidence level, (b) dominant assumptions, (c) primary uncertainty areas.

1.3. The model SHALL enumerate at least three Beliefs held by the team before signals were
gathered. Each belief SHALL be labeled B-01, B-02, B-03, ... (incrementing). Each belief SHALL
be stated as a declarative sentence representing what the team expected to be true.

1.4. The model SHALL NOT skip the Belief enumeration. If fewer than three beliefs can be
inferred from context, the model SHALL write placeholder beliefs and HALT with a request for
clarification.

**EXIT criterion:** Verify: (a) Opening Model present, (b) Epistemic Profile present,
(c) ≥3 beliefs labeled B-01 through B-0N. Scan dimension values; replace any prohibited
synonym. Emit:

`COMMIT-STAGE-1`

---

## STAGE 2 — SIGNAL INVENTORY

**ENTER contract:** COMMIT-STAGE-1 MUST be present.

**Execution Requirements:**

2.1. The model SHALL list all signal artifacts available for this topic. Each artifact SHALL be
recorded with: (a) artifact name, (b) namespace, (c) date.

2.2. The model SHALL note any canonical namespace (scout, draft, review, flow, trace, prove,
listen, program, topic) with no artifact. Missing namespaces are not errors; note them.

2.3. The model SHALL count total artifacts. If count is zero, HALT.

**EXIT criterion:** Artifact inventory complete. Emit:

`COMMIT-STAGE-2`

---

## STAGE 3 — FIVE-CHECK QUALIFICATION TABLE

**ENTER contract:** COMMIT-STAGE-2 MUST be present.

**Execution Requirements:**

3.1. The model SHALL produce a five-row qualification table. Each row SHALL contain:
(a) Check name, (b) Question, (c) Answer, (d) Verdict (VALID or INVALID).

The five checks SHALL be:

| Check | Question |
|-------|----------|
| Check 1: Signal Coverage | Do ≥2 namespaces have artifacts? |
| Check 2: Belief Presence | Are ≥3 beliefs recorded in Stage 1? |
| Check 3: Artifact Specificity | Does ≥1 artifact name a specific file with a date? |
| Check 4: Contradiction Potential | Is ≥1 artifact potentially contradicting a Stage 1 belief? |
| Check 5: Team Readiness | Has the topic been active for ≥1 signal cycle? |

3.2. Each verdict SHALL be exactly VALID or INVALID.

3.3. At the conclusion of the table, the model SHALL emit one of:
  - `GATE-CONFIRMED` — if all five verdicts are VALID
  - `GATE-REJECTED` — if any verdict is INVALID

**EXIT criterion:** Table complete; GATE-CONFIRMED or GATE-REJECTED token emitted.

---

## STAGE 3.5 — GATE RESOLUTION

**ENTER contract:** Stage 3 gate token MUST be present.

3.5.1. If GATE-CONFIRMED: emit `COMMIT-STAGE-3-CLEAN` and proceed to Stage 4.

3.5.2. If GATE-REJECTED: list each INVALID check and a specific remediation action. If
in-session remediation is possible, request the information and re-run Stage 3. If not,
emit `COMMIT-STAGE-3-FLAGGED` and HALT.

3.5.3. The model SHALL NOT proceed to Stage 4 without a COMMIT-STAGE-3-CLEAN token.

---

## STAGE 4 — SURPRISE SYNTHESIS

**ENTER contract:** COMMIT-STAGE-3-CLEAN MUST be present.

---

### FIELD REFERENCE BLOCK

The following sub-specifications govern the four required sub-fields for every Stage 4 entry.
This block SHALL be consulted before writing each entry and before emitting each COMMIT-ENTRY.

**Sub-Spec 4.A.1 — Surprise**

SHALL state the unexpected finding as a declarative sentence. SHALL reference a specific
belief from Stage 1 by label (e.g., "Contradicts B-02"). SHALL be specific enough that a
reader who has not seen the source artifact understands what was expected and what was found.
MUST NOT be a restatement of a belief or a known assumption — it must represent genuine
epistemic deviation.

**Sub-Spec 4.A.2 — Signal Source**

SHALL name exactly one artifact: the specific file or document that is the primary evidence.
SHALL include: artifact name, namespace, date. SHALL NOT use generic phrases such as "multiple
sources," "various artifacts," "the signals," or "the evidence."

Enforcement: If Signal Source contains a generic phrase, HALT and rewrite with a specific
artifact name before proceeding.

**Sub-Spec 4.A.3 — Design Impact**

SHALL name a specific component, API, flow, or architectural decision that must change. SHALL
NOT use abstract subjects such as "the system," "the architecture," or "the codebase." SHALL
be written as a full sentence identifying the named element and the nature of the required
change.

Enforcement: If Design Impact does not name a specific component or API, HALT and rewrite.

**Sub-Spec 4.A.4 — Build Risk**

Purpose: Build Risk names what is implicated by the Design Impact change — the downstream
component, dependency, or contract that could fail or require rework because of that change.

Paired formula: Design Impact names what must change; Build Risk names what is implicated by
that change — a different component, dependency, or contract that could fail.

Abstract structural gloss: One is forward-looking (what to update); the other is risk-surface
(what could break or require rework). These are two different things and SHALL NOT be synonyms
or restatements of each other.

SHALL be written as a full sentence. SHALL name a specific component or contract. If Build Risk
is general or abstract, the model SHALL rewrite before emitting COMMIT-ENTRY.

---

### CALIBRATION ENTRY — Surprise 0

**Surprise 0 — Calibration Entry (not a live entry)**

The following is a complete, correct entry. It is labeled Surprise 0 and is a Calibration
Entry (not a live entry). Live entries begin at Surprise 1. The model SHALL use this entry
as an imitation floor: every live entry SHALL match or exceed the specificity and sentence
completeness demonstrated here.

**Surprise:** Contradicts B-02. The opening model assumed topic readiness was computed fresh
on every query — a stateless derived property. `topic-scanner-state-2026-03-10.md` (namespace:
topic) reveals the scanner caches the last-computed readiness value and only invalidates it on
explicit `topic.invalidate()` events; late-arriving signals do not update readiness until a
forced rescan is triggered.

**Signal Source:** `topic-scanner-state-2026-03-10.md`, namespace: topic, date: 2026-03-10.

**Design Impact:** `TopicScanner.checkReadiness()` must be refactored to accept a
`forceRecompute: boolean` option, or the caching layer must subscribe to signal-arrival events
and self-invalidate; the current contract makes stale readiness invisible to callers that do
not know to trigger a rescan.

**Build Risk:** `ProgramOrchestrator` uses `TopicScanner.checkReadiness()` as a
stage-advancement gate; if readiness can be stale, the orchestrator may advance a program stage
before all signals are present — corrupting downstream program state for skills that depend on
a complete, consistent signal set.

**Dimension:** Correctness

`COMMIT-ENTRY`

---

### ENTRY LOOP

For each surprise identified from the signal inventory, write a numbered prose block (Surprise
1, Surprise 2, ...). Surprise 0 is the calibration entry; live entries start at Surprise 1.

Each entry SHALL have labeled sub-fields: Surprise, Signal Source, Design Impact, Build Risk,
Dimension. Markdown tables SHALL NOT be used for entry content.

After completing each entry, execute the COMMIT-ENTRY gate:

**COMMIT-ENTRY Gate — Scannable Checklist:**

  ✓ Surprise: Does it name a specific B-# from Stage 1 and represent genuine epistemic
    deviation? If not — reference a specific belief label and clarify the expectation vs.
    finding delta before proceeding.

  ✓ Signal Source: Does it name a specific artifact (not a generic phrase) with name,
    namespace, date? If not — identify the single most relevant artifact and rewrite with
    all three fields.

  ✓ Design Impact: Does it name a specific component, API, or flow (not "the system")? If
    not — identify the specific named element and rewrite as a full sentence.

  ✓ Build Risk: Does it name a specific component or contract implicated by the Design Impact
    change, and is it conceptually distinct from Design Impact (not a synonym or restatement)?
    If not — identify what downstream element could fail because of the Design Impact change
    and rewrite.

All four checks pass: emit `COMMIT-ENTRY`. Proceed to the next surprise.
Any check fails: rewrite the failing field(s) and re-execute the checklist.

**EXIT criterion:** All surprises recorded; all COMMIT-ENTRY tokens emitted; ≥1 entry
contradicts a Stage 1 belief; ≥2 GATE-CONFIRMED entries. If fewer than 2, extend the sweep.
Scan all Dimension values; replace prohibited synonyms. Emit:

`COMMIT-STAGE-4`

---

## STAGE 5 — IMPLICATIONS TABLE

**ENTER contract:** COMMIT-STAGE-4 MUST be present.

Produce a table with one row per surprise:

  | Surprise # | Key Implication | Priority | Next Team / Skill |

Priority: Critical · High · Medium · Low.

Next Team / Skill SHALL name at least one specific skill (e.g., `flow-trigger`,
`trace-permissions`) or role (e.g., "API contract owner") per row.

**EXIT criterion:** Table complete; ≥1 named skill or role. Emit:

`COMMIT-STAGE-5`

---

## STAGE 6 — BELIEF REVISION VERDICT TABLE

**ENTER contract:** COMMIT-STAGE-5 MUST be present.

Produce a verdict table with one row per Stage 1 belief:

  | Belief # | Belief Statement | Revision Direction | Verdict |

Revision Direction: how the belief should be updated given evidence, or confirmation unchanged.

Verdict — exactly one of:
- COHERENT — evidence consistent; belief stands
- CONTRADICTORY — evidence directly contradicts; belief must be revised
- FOREKNOWLEDGE-FLAGGED — belief appears written after evidence was seen, not before

Explicitly record foreknowledge status for each belief: CLEAR or FLAGGED. If any belief is
FOREKNOWLEDGE-FLAGGED, note this prominently and do not advance to Stage 7 without user
confirmation.

**EXIT criterion:** All beliefs have Revision Direction + Verdict; foreknowledge status
recorded; no unresolved FOREKNOWLEDGE-FLAGGED beliefs. Scan Dimension values; replace
prohibited synonyms. Emit:

`COMMIT-STAGE-6`

---

## STAGE 7 — ARTIFACT WRITE

**ENTER contract:** COMMIT-STAGE-6 MUST be present; no unresolved FOREKNOWLEDGE-FLAGGED
beliefs.

Write `{topic}-reflect-{date}.md` containing: topic name, date, Opening Model summary (Stage
1), all Stage 4 surprise entries in full numbered prose block format, Stage 5 implications
table, Stage 6 verdict table.

Emit: `COMMIT-STAGE-7`
```

---

## V-02

**Variation axis:** Lifecycle emphasis — gate anatomy
**Hypothesis:** Framing every stage as a formal "Gate opens / Gate closes" ceremony makes the
gate mechanism feel primary rather than decorative — the model treats each stage transition as
an explicit decision point rather than a section break. When the Field Reference block is
declared part of Stage 4's formal gate-open ritual ("as the gate opens, consult the Field
Reference block"), it is more likely to be consulted before entry writing begins rather than
skipped as preamble. The gate-anatomy frame also makes Stage 3.5's FLAGGED path structurally
parallel to the other gate halt conditions, reducing the chance of treating it as advisory.

---

```
# topic-reflect — Skill Body Prompt (V-02: Lifecycle / Gate Anatomy)

## PURPOSE

This skill synthesizes unexpected findings from signal artifacts gathered for a topic. For each
surprise: name it, trace it to its source signal, assess design impact, name build risk. The
reflect artifact records what the team learned that it did not expect — and what that means for
design, build risk, and belief revision.

---

## GATE SEQUENCE OVERVIEW

| Stage | Gate Opens When | Gate Closes With | Halt Condition |
|-------|----------------|------------------|----------------|
| Stage 1 | Topic + artifact list available | COMMIT-STAGE-1 | < 3 beliefs: HALT |
| Stage 2 | COMMIT-STAGE-1 present | COMMIT-STAGE-2 | 0 artifacts: HALT |
| Stage 3 | COMMIT-STAGE-2 present | GATE-CONFIRMED or GATE-REJECTED | — |
| Stage 3.5 | Stage 3 gate token present | COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED | FLAGGED: HALT |
| Stage 4 | COMMIT-STAGE-3-CLEAN present | COMMIT-STAGE-4 | < 2 GATE-CONFIRMED: extend sweep |
| Stage 5 | COMMIT-STAGE-4 present | COMMIT-STAGE-5 | — |
| Stage 6 | COMMIT-STAGE-5 present | COMMIT-STAGE-6 | FOREKNOWLEDGE-FLAGGED: HALT |
| Stage 7 | COMMIT-STAGE-6 present | COMMIT-STAGE-7 | — |

---

## VOCABULARY RULE — CLOSED DIMENSION SET

**Gate rule:** Active at the close of every stage gate. Before emitting any stage commit token,
scan all dimension values written in that stage and replace any prohibited synonym with its
canonical substitute.

**Canonical set (closed):**

  Feasibility · Usability · Scalability · Adoptability · Correctness

**Prohibited synonyms — replace before any gate closes:**

  | Prohibited | Canonical Substitute |
  |------------|---------------------|
  | Reliability | Correctness |
  | Performance | Scalability |
  | Maintainability | Correctness |
  | Learnability | Usability |
  | Viability | Feasibility |

A dimension value not in the canonical set is a gate violation. The gate does not close until
all dimension values are canonical.

---

## STAGE 1 — GATE: OPENING MODEL

**Gate opens:** Topic name and artifact list are available. If no artifacts exist, the gate
does not open: report "No signal artifacts found — topic-reflect requires at least one source
signal." and halt.

**While the gate is open — execute:**

1. Write the Opening Model: state the topic name and summarize the feature intent in two to
   four sentences from the team's perspective before evidence gathering.

2. Write the Epistemic Profile: a paragraph characterizing how well-understood this topic was
   before signals were gathered. Address: team confidence level, dominant assumptions, primary
   uncertainty areas.

3. Enumerate Beliefs: list at least three beliefs held before evidence gathering, labeled B-01,
   B-02, B-03, ... Each belief is a declarative sentence stating what the team expected to be
   true. If fewer than three beliefs can be inferred, write placeholders and halt with a
   clarification request.

**Gate closes:** Opening Model present + Epistemic Profile present + ≥3 beliefs enumerated.
Scan dimension values; replace any prohibited synonym. Emit:

`COMMIT-STAGE-1`

---

## STAGE 2 — GATE: SIGNAL INVENTORY

**Gate opens:** COMMIT-STAGE-1 is present.

**While the gate is open — execute:**

1. List all signal artifacts available for this topic. For each: artifact name, namespace, date.

2. Note any canonical namespace (scout, draft, review, flow, trace, prove, listen, program,
   topic) with no artifact. Missing namespaces are not errors; note them.

3. Count artifacts. If count is zero, this gate closes with HALT.

**Gate closes:** Inventory complete, count > 0. Emit:

`COMMIT-STAGE-2`

---

## STAGE 3 — GATE: FIVE-CHECK QUALIFICATION

**Gate opens:** COMMIT-STAGE-2 is present.

**While the gate is open — execute:**

Evaluate each of the five qualification checks. Render results as a table.

| Check | Question | Answer | Verdict |
|-------|----------|--------|---------|
| Check 1: Signal Coverage | Do ≥2 namespaces have artifacts? | — | VALID / INVALID |
| Check 2: Belief Presence | Are ≥3 beliefs in Stage 1? | — | VALID / INVALID |
| Check 3: Artifact Specificity | Does ≥1 artifact name a specific file with a date? | — | VALID / INVALID |
| Check 4: Contradiction Potential | Is ≥1 artifact potentially contradicting a B-# belief? | — | VALID / INVALID |
| Check 5: Team Readiness | Has the topic been active for ≥1 signal cycle? | — | VALID / INVALID |

**Gate closes:** All five verdicts rendered. Emit one of:
- `GATE-CONFIRMED` if all five verdicts are VALID
- `GATE-REJECTED` if any verdict is INVALID

Proceed immediately to Stage 3.5.

---

## STAGE 3.5 — GATE: RESOLUTION

**Gate opens:** Stage 3 gate token (GATE-CONFIRMED or GATE-REJECTED) is present.

**While the gate is open — execute:**

- If GATE-CONFIRMED: this gate closes cleanly. Emit `COMMIT-STAGE-3-CLEAN`.

- If GATE-REJECTED: list each INVALID check and its remediation. If in-session remediation is
  possible, request the information and re-run Stage 3. If not, this gate closes flagged —
  emit `COMMIT-STAGE-3-FLAGGED` and halt.

The Stage 4 gate does not open without COMMIT-STAGE-3-CLEAN.

---

## STAGE 4 — GATE: SURPRISE SYNTHESIS

**Gate opens:** COMMIT-STAGE-3-CLEAN is present.

**As the gate opens — consult the Field Reference block before writing any entry.**

---

### FIELD REFERENCE BLOCK — Stage 4 Gate-Open Ritual

This block is the Stage 4 gate-open ritual. Consult it before writing the first entry and
before emitting each COMMIT-ENTRY. It defines the quality contract for all four sub-fields.

**Surprise**
What was unexpected? Name the specific belief (B-#) it contradicts or extends. State what was
assumed and what was actually found. A Surprise that does not reference a specific B-# does not
pass the COMMIT-ENTRY gate.

**Signal Source**
Name the single artifact that is the primary evidence. Include: artifact name, namespace, date.
Generic phrases ("multiple sources," "the signals," "various artifacts") do not pass the
COMMIT-ENTRY gate.

**Design Impact**
Name the specific component, API, flow, or architectural decision that must change. Use its
actual name. Subjects such as "the system," "the architecture," or "the codebase" do not pass
the COMMIT-ENTRY gate.

**Build Risk**
Purpose: Build Risk names what is implicated by the Design Impact change — the downstream
component, dependency, or contract that could fail or require rework.

Paired formula: Design Impact names what must change; Build Risk names what is implicated by
that change — a different component, dependency, or contract that could fail.

Abstract structural gloss: One is forward-looking (what to update); the other is risk-surface
(what could break or require rework). They are two different things and must not be synonyms
or restatements of each other.

A Build Risk that is general ("could affect performance," "may cause issues") or that merely
restates the Design Impact does not pass the COMMIT-ENTRY gate.

---

### CALIBRATION ENTRY — Surprise 0

**Surprise 0 — Calibration Entry (not a live entry)**

This entry demonstrates the complete, correct form. Live entries begin at Surprise 1 and must
match or exceed the specificity and sentence completeness shown here.

**Surprise:** Contradicts B-02. The opening model assumed topic readiness was computed fresh
on every query — a stateless derived property. `topic-scanner-state-2026-03-10.md` (namespace:
topic) reveals the scanner caches the last-computed readiness value and only invalidates it on
explicit `topic.invalidate()` events; late-arriving signals do not update readiness until a
forced rescan is triggered.

**Signal Source:** `topic-scanner-state-2026-03-10.md`, namespace: topic, date: 2026-03-10.

**Design Impact:** `TopicScanner.checkReadiness()` must be refactored to accept a
`forceRecompute: boolean` option, or the caching layer must subscribe to signal-arrival events
and self-invalidate; the current contract makes stale readiness invisible to callers that do
not know to trigger a rescan.

**Build Risk:** `ProgramOrchestrator` uses `TopicScanner.checkReadiness()` as a
stage-advancement gate; if readiness can be stale, the orchestrator may advance a program stage
before all signals are present — corrupting downstream program state for skills that depend on
a complete, consistent signal set.

**Dimension:** Correctness

`COMMIT-ENTRY`

---

### ENTRY LOOP

For each surprise from the signal inventory, write a numbered prose block (Surprise 1,
Surprise 2, ...). Surprise 0 is the calibration entry; live entries start at Surprise 1.

Each entry uses labeled sub-fields: Surprise, Signal Source, Design Impact, Build Risk,
Dimension. Do not use markdown tables for entry content.

After completing each entry, the entry gate opens:

**COMMIT-ENTRY Gate — the entry gate closes only when all four checks pass:**

  ✓ Surprise: Does it reference a specific B-# from Stage 1 and name the expectation-vs-finding
    delta? If not — add the B-# label and restate as expected/found contrast before proceeding.

  ✓ Signal Source: Does it name a specific artifact (not a generic phrase) with name, namespace,
    date? If not — identify the single most relevant artifact and rewrite with all three fields.

  ✓ Design Impact: Does it name a specific component, API, or flow (not "the system" or "the
    architecture")? If not — identify the specific named element and rewrite as a full sentence.

  ✓ Build Risk: Does it name a specific downstream component or contract implicated by the
    Design Impact change, and is it conceptually distinct from Design Impact? If not — identify
    what could fail downstream because of the Design Impact change and rewrite.

When all four checks pass: emit `COMMIT-ENTRY`. The entry gate closes. Open the next entry.

**Also verify before closing Stage 4:**
- At least one live entry contradicts a Stage 1 belief. If none, review artifacts again.
- At least two entries carry GATE-CONFIRMED status. If fewer, extend the sweep.

**Stage 4 gate closes:** All surprises recorded; all COMMIT-ENTRY tokens emitted; ≥1 entry
contradicts a B-# belief; ≥2 GATE-CONFIRMED entries. Scan all Dimension values; replace
prohibited synonyms. Emit:

`COMMIT-STAGE-4`

---

## STAGE 5 — GATE: IMPLICATIONS TABLE

**Gate opens:** COMMIT-STAGE-4 is present.

Produce a table with one row per surprise:

  | Surprise # | Key Implication | Priority | Next Team / Skill |

Priority: Critical · High · Medium · Low.
Next Team / Skill: at least one specific skill (e.g., `flow-trigger`, `trace-permissions`)
or role (e.g., "API contract owner") per row. Generic entries ("TBD") not permitted.

**Gate closes:** Table complete; ≥1 named skill or role. Emit:

`COMMIT-STAGE-5`

---

## STAGE 6 — GATE: BELIEF REVISION VERDICT TABLE

**Gate opens:** COMMIT-STAGE-5 is present.

Produce a verdict table with one row per Stage 1 belief:

  | Belief # | Belief Statement | Revision Direction | Verdict |

Revision Direction: how the belief should be updated given evidence — or confirmation unchanged.

Verdict — exactly one of:
- COHERENT: evidence consistent; belief stands
- CONTRADICTORY: evidence directly contradicts; belief must be revised
- FOREKNOWLEDGE-FLAGGED: belief appears written after evidence was seen, not before

Explicitly record foreknowledge status for each belief: CLEAR or FLAGGED. If any belief is
FOREKNOWLEDGE-FLAGGED, note this prominently. This gate closes flagged and does not advance
to Stage 7 without user confirmation.

**Gate closes (clean):** All beliefs have Revision Direction + Verdict; no unresolved
FOREKNOWLEDGE-FLAGGED beliefs. Scan Dimension values; replace prohibited synonyms. Emit:

`COMMIT-STAGE-6`

---

## STAGE 7 — GATE: ARTIFACT WRITE

**Gate opens:** COMMIT-STAGE-6 is present; no unresolved FOREKNOWLEDGE-FLAGGED beliefs.

Write `{topic}-reflect-{date}.md` containing: topic name, date, Opening Model summary (Stage
1), all Stage 4 surprise entries in full numbered prose block format, Stage 5 implications
table, Stage 6 verdict table.

**Gate closes:** Artifact written or complete content presented for review. Emit:

`COMMIT-STAGE-7`
```

---

## V-03

**Variation axis:** Role sequence — three named roles
**Hypothesis:** Assigning three distinct named roles (Belief Historian, Adversarial Challenger,
Surprise Synthesizer) creates cognitive separation between the retrospective, critical, and
synthetic phases of the skill. When the Field Reference block is introduced as the Synthesizer's
toolset — "the Synthesizer owns the Field Reference block" — the model is more likely to
maintain the field contract throughout Stage 4 because it is conceptually owned by a named role
rather than appearing as a generic rubric. The Challenger's bilateral handoff (COMMIT-STAGE-3-
CLEAN unlocks the Synthesizer) makes the foreknowledge gate feel like a professional judgment,
not an advisory check.

---

```
# topic-reflect — Skill Body Prompt (V-03: Three Named Roles)

## PURPOSE

This skill synthesizes unexpected findings from signal artifacts gathered for a topic. For each
surprise: name it, trace it to its source signal, assess design impact, name build risk. The
reflect artifact records what the team learned that it did not expect — and what that means for
design, build risk, and belief revision.

Three roles execute this skill in sequence. Role 1 (Belief Historian) builds the retrospective
record. Role 2 (Adversarial Challenger) tests whether the evidence qualifies. Role 3 (Surprise
Synthesizer) writes the surprise entries and revision verdicts. Each role has a defined handoff
point.

---

## GATE SEQUENCE OVERVIEW

| Stage | Role | Token Emitted | Halt Condition |
|-------|------|--------------|----------------|
| Stage 1 | Belief Historian | COMMIT-STAGE-1 | < 3 beliefs: HALT |
| Stage 2 | Belief Historian | COMMIT-STAGE-2 | 0 artifacts: HALT |
| Stage 3 | Adversarial Challenger | GATE-CONFIRMED / GATE-REJECTED | — |
| Stage 3.5 | Adversarial Challenger | COMMIT-STAGE-3-CLEAN / COMMIT-STAGE-3-FLAGGED | FLAGGED: HALT |
| Stage 4 | Surprise Synthesizer | COMMIT-STAGE-4 | < 2 GATE-CONFIRMED: extend |
| Stage 5 | Surprise Synthesizer | COMMIT-STAGE-5 | — |
| Stage 6 | Surprise Synthesizer | COMMIT-STAGE-6 | FOREKNOWLEDGE-FLAGGED: HALT |
| Stage 7 | Surprise Synthesizer | COMMIT-STAGE-7 | — |

---

## VOCABULARY RULE — CLOSED DIMENSION SET

This rule applies to all three roles at every stage exit.

Canonical set (closed): Feasibility · Usability · Scalability · Adoptability · Correctness

Prohibited synonyms and canonical substitutes:

  | Prohibited | Substitute |
  |------------|-----------|
  | Reliability | Correctness |
  | Performance | Scalability |
  | Maintainability | Correctness |
  | Learnability | Usability |
  | Viability | Feasibility |

Before emitting any commit token, the active role scans all dimension values written in that
stage and replaces any prohibited name with its canonical substitute.

---

## ROLE 1: BELIEF HISTORIAN — STAGES 1 AND 2

The Belief Historian reconstructs the team's epistemic state before evidence was gathered.
The Historian does not evaluate evidence — only records what was believed.

### STAGE 1 — OPENING MODEL AND EPISTEMIC PROFILE

**ENTER contract:** Topic name and artifact list are available. If no artifacts exist, halt:
"No signal artifacts found. topic-reflect requires at least one source signal."

**Historian executes:**

1. Opening Model: State the topic name and summarize the feature intent in two to four
   sentences from the team's pre-evidence perspective.

2. Epistemic Profile: A paragraph characterizing how well-understood the topic was before
   signals were gathered. Address: team confidence level, dominant assumptions, primary
   uncertainty areas.

3. Belief Enumeration: List at least three beliefs held before evidence gathering, labeled
   B-01, B-02, B-03, ... Each belief is a declarative sentence stating what the team expected.
   If fewer than three beliefs can be reconstructed, write placeholders and halt with a request.

**EXIT criterion:** Opening Model + Epistemic Profile + ≥3 labeled beliefs present. Scan
dimension values (none expected). Emit: `COMMIT-STAGE-1`

Historian handoff note: Stage 1 is locked. The beliefs enumerated here are the reference set
for all Stage 4 contradiction checks.

---

### STAGE 2 — SIGNAL INVENTORY

**ENTER contract:** COMMIT-STAGE-1 present.

**Historian executes:**

1. List all signal artifacts for this topic: artifact name, namespace, date.

2. Note any canonical namespace (scout, draft, review, flow, trace, prove, listen, program,
   topic) without an artifact. Missing namespaces are not errors; note them.

3. Count total artifacts. If zero, halt.

**EXIT criterion:** Inventory complete, count > 0. Emit: `COMMIT-STAGE-2`

The Belief Historian's work is complete. Role 2 takes over.

---

## ROLE 2: ADVERSARIAL CHALLENGER — STAGES 3 AND 3.5

The Adversarial Challenger tests whether the evidence is sufficient and structured for surprise
synthesis. The Challenger does not synthesize surprises — only decides whether the gate opens.

### STAGE 3 — FIVE-CHECK QUALIFICATION TABLE

**ENTER contract:** COMMIT-STAGE-2 present.

**Challenger executes:**

| Check | Question | Answer | Verdict |
|-------|----------|--------|---------|
| Check 1: Signal Coverage | Do ≥2 namespaces have artifacts? | — | VALID / INVALID |
| Check 2: Belief Presence | Are ≥3 beliefs in Stage 1? | — | VALID / INVALID |
| Check 3: Artifact Specificity | Does ≥1 artifact name a specific file with date? | — | VALID / INVALID |
| Check 4: Contradiction Potential | Is ≥1 artifact potentially contradicting a B-# belief? | — | VALID / INVALID |
| Check 5: Team Readiness | Has the topic been active ≥1 signal cycle? | — | VALID / INVALID |

Emit one of: `GATE-CONFIRMED` (all VALID) or `GATE-REJECTED` (any INVALID).

---

### STAGE 3.5 — GATE RESOLUTION

**ENTER contract:** Stage 3 gate token present.

- GATE-CONFIRMED: emit `COMMIT-STAGE-3-CLEAN`.

- GATE-REJECTED: list each INVALID check and its remediation. If in-session remediation is
  possible, request information and re-run Stage 3. If not, emit `COMMIT-STAGE-3-FLAGGED`
  and halt.

COMMIT-STAGE-3-CLEAN unlocks the Surprise Synthesizer. The Adversarial Challenger's work is
complete.

---

## ROLE 3: SURPRISE SYNTHESIZER — STAGES 4, 5, AND 6

The Surprise Synthesizer writes the surprise entries, the implications table, and the belief
revision verdict table. The Synthesizer owns the Field Reference block; it is the Synthesizer's
primary toolset and must be consulted before and during every entry.

### STAGE 4 — SURPRISE SYNTHESIS

**ENTER contract:** COMMIT-STAGE-3-CLEAN present.

---

#### SYNTHESIZER'S FIELD REFERENCE BLOCK

This is the Synthesizer's toolset. Consult it before writing the first entry, and before
emitting each COMMIT-ENTRY. These are the quality contracts for the four required sub-fields.

**Surprise**
State the unexpected finding. Reference the specific belief it contradicts by label (e.g.,
"Contradicts B-02"). Name both what was assumed and what was found. A Surprise without a B-#
reference does not pass the COMMIT-ENTRY gate.

**Signal Source**
Name the single artifact that is the primary evidence. Include: artifact name, namespace, date.
Phrases such as "multiple sources," "the signals," or "various artifacts" do not pass the
COMMIT-ENTRY gate.

**Design Impact**
Name the specific component, API, flow, or architectural decision that must change. Use its
actual name. Subjects such as "the system," "the architecture," or "the codebase" do not pass
the COMMIT-ENTRY gate.

**Build Risk**
Purpose: Build Risk names what is implicated by the Design Impact change — the downstream
component, dependency, or contract that could fail or require rework.

Paired formula: Design Impact names what must change; Build Risk names what is implicated by
that change — a different component, dependency, or contract that could fail.

Abstract structural gloss: One is forward-looking (what to update); the other is risk-surface
(what could break or require rework). They are two different things. They must not be synonyms
or restatements of each other.

A Build Risk that is general or that merely restates the Design Impact does not pass the
COMMIT-ENTRY gate.

---

#### CALIBRATION ENTRY — Surprise 0

**Surprise 0 — Calibration Entry (not a live entry)**

This is the Synthesizer's reference example. It demonstrates the complete, correct form for all
four sub-fields. Live entries begin at Surprise 1 and must match or exceed the specificity and
sentence completeness shown here. The Surprise 0 label distinguishes this entry from all live
entries; the Synthesizer does not number live entries starting at 2.

**Surprise:** Contradicts B-02. The opening model assumed topic readiness was computed fresh
on every query — a stateless derived property. `topic-scanner-state-2026-03-10.md` (namespace:
topic) reveals the scanner caches the last-computed readiness value and only invalidates it on
explicit `topic.invalidate()` events; late-arriving signals do not update readiness until a
forced rescan is triggered.

**Signal Source:** `topic-scanner-state-2026-03-10.md`, namespace: topic, date: 2026-03-10.

**Design Impact:** `TopicScanner.checkReadiness()` must be refactored to accept a
`forceRecompute: boolean` option, or the caching layer must subscribe to signal-arrival events
and self-invalidate; the current contract makes stale readiness invisible to callers that do
not know to trigger a rescan.

**Build Risk:** `ProgramOrchestrator` uses `TopicScanner.checkReadiness()` as a
stage-advancement gate; if readiness can be stale, the orchestrator may advance a program stage
before all signals are present — corrupting downstream program state for skills that depend on
a complete, consistent signal set.

**Dimension:** Correctness

`COMMIT-ENTRY`

---

#### ENTRY LOOP

Write one numbered prose block per surprise (Surprise 1, Surprise 2, ...). Surprise 0 is
the calibration entry; live entries start at 1. Each entry has labeled sub-fields: Surprise,
Signal Source, Design Impact, Build Risk, Dimension.

After each entry, execute the COMMIT-ENTRY gate:

**COMMIT-ENTRY Gate — Synthesizer's checklist:**

  ✓ Surprise: References a specific B-# from Stage 1 and states expectation vs. finding
    contrast? If not — add the B-# label and restate the expected/found delta before continuing.

  ✓ Signal Source: Names a specific artifact (not a generic phrase), with name, namespace,
    date? If not — identify the single most relevant artifact and rewrite with all three fields.

  ✓ Design Impact: Names a specific component, API, or flow (not "the system" or "the
    architecture")? If not — identify the specific named element and rewrite as a full sentence.

  ✓ Build Risk: Names a specific downstream component or contract implicated by the Design
    Impact change? Is it conceptually distinct from Design Impact? If not — identify what could
    fail downstream because of the Design Impact change and rewrite.

All four checks pass: emit `COMMIT-ENTRY`. Move to next entry.
Any check fails: rewrite and re-execute checklist before emitting.

**Synthesizer verifies before closing Stage 4:**
- At least one live entry contradicts a Stage 1 belief.
- At least two entries carry GATE-CONFIRMED status. If fewer, extend the sweep.

**EXIT criterion:** All entries written; all COMMIT-ENTRY tokens emitted; ≥1 entry contradicts
a B-# belief; ≥2 GATE-CONFIRMED entries. Scan Dimension values; replace prohibited synonyms.
Emit: `COMMIT-STAGE-4`

---

### STAGE 5 — IMPLICATIONS TABLE

**ENTER contract:** COMMIT-STAGE-4 present.

**Synthesizer executes:**

  | Surprise # | Key Implication | Priority | Next Team / Skill |

Priority: Critical · High · Medium · Low.
Next Team / Skill: at least one specific skill or role per row. Generic entries not permitted.

**EXIT criterion:** Table complete; ≥1 named skill or role. Emit: `COMMIT-STAGE-5`

---

### STAGE 6 — BELIEF REVISION VERDICT TABLE

**ENTER contract:** COMMIT-STAGE-5 present.

**Synthesizer executes:**

  | Belief # | Belief Statement | Revision Direction | Verdict |

Revision Direction: specific instruction to update the belief, or confirmation it stands.

Verdict — exactly one of:
- COHERENT: evidence consistent; belief stands
- CONTRADICTORY: evidence directly contradicts; belief must be revised
- FOREKNOWLEDGE-FLAGGED: belief appears written after evidence was seen

Explicitly record foreknowledge status: CLEAR or FLAGGED. If any belief is FOREKNOWLEDGE-
FLAGGED, note this prominently and do not advance to Stage 7 without user confirmation.

**EXIT criterion:** All beliefs have Revision Direction + Verdict; foreknowledge status
recorded; no unresolved FOREKNOWLEDGE-FLAGGED beliefs. Scan Dimension values; replace
prohibited synonyms. Emit: `COMMIT-STAGE-6`

---

### STAGE 7 — ARTIFACT WRITE

**ENTER contract:** COMMIT-STAGE-6 present; no unresolved FOREKNOWLEDGE-FLAGGED beliefs.

Write `{topic}-reflect-{date}.md` containing: topic name, date, Opening Model summary (Stage
1), all Stage 4 surprise entries in full numbered prose block format, Stage 5 implications
table, Stage 6 verdict table.

Emit: `COMMIT-STAGE-7`
```

---

## V-04

**Variation axis:** Combined — conversational register + fill-in templates with inline worked examples
**Hypothesis:** A friendly "you" tone with fill-in templates reduces the cognitive distance
between instruction and execution, making it easier for the model to produce well-formed entries
without needing to mentally translate between abstract rule and concrete action. Inline
_Example:_ annotations at each Stage 4 field make the Field Reference block self-teaching,
reducing the chance the model treats it as a header to scan rather than a contract to apply.
Worked examples adjacent to field definitions calibrate specificity at the definition site —
before the model enters the entry loop — rather than relying solely on Surprise 0 as an
imitation floor.

---

```
# topic-reflect — Skill Body Prompt (V-04: Conversational Register + Fill-In Templates)

## What this skill does

You're going to synthesize the unexpected findings from a topic's signal artifacts. For each
surprise you surface, you'll name it, trace it to its source signal, figure out what it means
for design, and name the build risk it creates. The artifact you produce tells the team: "here
is what we learned that we did not expect — and here is what we need to do about it."

---

## Your stage map (read this first)

| Stage | What you do | Token you emit | When to stop |
|-------|-------------|---------------|-------------|
| Stage 1 | Build the opening model and list beliefs | COMMIT-STAGE-1 | < 3 beliefs: stop and ask |
| Stage 2 | Inventory the signal artifacts | COMMIT-STAGE-2 | 0 artifacts: stop |
| Stage 3 | Run the five qualification checks | GATE-CONFIRMED or GATE-REJECTED | — |
| Stage 3.5 | Resolve the gate result | COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED | FLAGGED: stop |
| Stage 4 | Write the surprise entries | COMMIT-STAGE-4 | < 2 GATE-CONFIRMED: keep looking |
| Stage 5 | Write the implications table | COMMIT-STAGE-5 | — |
| Stage 6 | Write the belief revision verdicts | COMMIT-STAGE-6 | FOREKNOWLEDGE-FLAGGED: stop |
| Stage 7 | Write the artifact | COMMIT-STAGE-7 | — |

---

## Vocabulary rule — the dimension names you're allowed to use

You have exactly five dimension names. Use only these:

  Feasibility · Usability · Scalability · Adoptability · Correctness

Some names sound fine but aren't on the list. Don't use them:

  | If you wrote this... | Replace it with... |
  |---------------------|-------------------|
  | Reliability | Correctness |
  | Performance | Scalability |
  | Maintainability | Correctness |
  | Learnability | Usability |
  | Viability | Feasibility |

Before you close each stage, scan any dimension values you wrote and swap out any prohibited
name for its canonical substitute. A dimension value outside the list means the stage isn't
done yet.

---

## Stage 1 — Your opening model and the beliefs you're tracking

**Before you start Stage 1:** Do you have a topic name and at least one signal artifact? If
you have no artifacts at all, stop here: "No signal artifacts found. topic-reflect needs at
least one source signal."

**What to write:**

Write the Opening Model: your summary of what the feature is about, from the team's point of
view before they gathered evidence. Two to four sentences.

_Example: "The topic is `auto-invalidate`. The feature adds automatic signal-arrival listeners
to TopicScanner so readiness values are always fresh. The team assumed this was a small wiring
change with no downstream impact on program orchestration."_

Then write the Epistemic Profile: a paragraph about how well-understood the topic was going in
— confidence level, main assumptions, and where the uncertainty was.

Then list at least three beliefs the team held before evidence gathering. Label them B-01,
B-02, B-03 (and so on). Each one should be a plain declarative sentence.

_Example beliefs:_
_B-01: TopicScanner computes readiness fresh on every call — no caching involved._
_B-02: Signal arrival events automatically update readiness._
_B-03: The orchestrator is shielded from stale readiness by the scanner's internal design._

If you can't reconstruct three beliefs, write placeholders and stop to ask.

**Before closing Stage 1:** Opening Model, Epistemic Profile, and ≥3 beliefs all present.
Scan for any dimension values and fix any prohibited synonyms. Then emit: `COMMIT-STAGE-1`

---

## Stage 2 — The signal artifact inventory

**You need:** COMMIT-STAGE-1.

List every signal artifact for this topic. For each: artifact name, namespace (one of: scout,
draft, review, flow, trace, prove, listen, program, topic), date.

Note any namespace with no artifact — that's fine, just flag it.

Count your artifacts. Zero? Stop here.

**Before closing Stage 2:** Inventory complete, count > 0. Emit: `COMMIT-STAGE-2`

---

## Stage 3 — Five qualification checks

**You need:** COMMIT-STAGE-2.

| Check | Question | Your answer | Verdict |
|-------|----------|-------------|---------|
| Check 1: Signal Coverage | Do you have artifacts in ≥2 namespaces? | — | VALID / INVALID |
| Check 2: Belief Presence | Are there ≥3 beliefs in Stage 1? | — | VALID / INVALID |
| Check 3: Artifact Specificity | Does ≥1 artifact have a specific filename and date? | — | VALID / INVALID |
| Check 4: Contradiction Potential | Does ≥1 artifact look like it might contradict a belief? | — | VALID / INVALID |
| Check 5: Team Readiness | Has the topic been through ≥1 signal cycle? | — | VALID / INVALID |

All five VALID? Emit `GATE-CONFIRMED`.
Any INVALID? Emit `GATE-REJECTED`.

Go straight to Stage 3.5.

---

## Stage 3.5 — Sort out the gate result

If you emitted GATE-CONFIRMED: you're good. Emit `COMMIT-STAGE-3-CLEAN` and keep going.

If you emitted GATE-REJECTED: list each INVALID check and say what it would take to fix it.
If you can get the missing info in this session, ask for it and re-run Stage 3. If you can't,
emit `COMMIT-STAGE-3-FLAGGED` and stop with an explanation.

You can't open Stage 4 without COMMIT-STAGE-3-CLEAN.

---

## Stage 4 — Writing the surprise entries

**You need:** COMMIT-STAGE-3-CLEAN.

### Your field guide (read this before every entry)

Here is what each of the four entry fields needs to contain. Read it before you write the
first entry, and check back before you emit each COMMIT-ENTRY.

---

**Surprise**
What was unexpected? Name the specific belief it contradicts (use its label — "Contradicts
B-02"). Say what was assumed and what was actually found.

_Example: "Contradicts B-01. The team assumed TopicScanner computed readiness fresh on every
call. The scanner actually caches the last result and only updates it on explicit invalidation
events."_

If you haven't named a B-# belief, the entry isn't done yet.

---

**Signal Source**
Name exactly one artifact — the main evidence for this surprise. Include its name, namespace,
and date.

_Example: "`topic-scanner-state-2026-03-10.md`, namespace: topic, date: 2026-03-10."_

Don't write "multiple sources" or "various signals." If you wrote a generic phrase here,
the entry isn't done yet.

---

**Design Impact**
Name the specific component, API, flow, or decision that has to change. Use its actual name.
Write a full sentence about what the change is.

_Example: "`TopicScanner.checkReadiness()` must be refactored to accept a
`forceRecompute: boolean` option, or the caching layer must subscribe to signal-arrival events
and self-invalidate."_

If you wrote "the system" or "the architecture," the entry isn't done yet.

---

**Build Risk**
This is what could break or require rework *because of* the Design Impact change. It names what
is implicated by that change — a different component, dependency, or contract that could fail.

Design Impact is forward-looking (what to update); Build Risk is the risk surface (what could
break or require rework). They are two different things.

Write a full sentence naming the specific downstream component or contract at risk.

_Example: "`ProgramOrchestrator` uses `TopicScanner.checkReadiness()` as a stage-advancement
gate; if readiness can be stale, the orchestrator may advance a program stage before all signals
are present — corrupting downstream program state."_

If your Build Risk is vague ("could affect performance") or just restates Design Impact, the
entry isn't done yet.

---

### A complete example entry — Surprise 0

**Surprise 0 — Calibration Entry (not a live entry)**

Here is a complete, correct entry. Your live entries start at Surprise 1. Do not number your
live entries starting at 2 — Surprise 0 is the calibration entry only; it is separate from
the live sequence.

**Surprise:** Contradicts B-02. The opening model assumed topic readiness was computed fresh
on every query — a stateless derived property. `topic-scanner-state-2026-03-10.md` (namespace:
topic) reveals the scanner caches the last-computed readiness value and only invalidates it on
explicit `topic.invalidate()` events; late-arriving signals do not update readiness until a
forced rescan is triggered.

**Signal Source:** `topic-scanner-state-2026-03-10.md`, namespace: topic, date: 2026-03-10.

**Design Impact:** `TopicScanner.checkReadiness()` must be refactored to accept a
`forceRecompute: boolean` option, or the caching layer must subscribe to signal-arrival events
and self-invalidate; the current contract makes stale readiness invisible to callers that do
not know to trigger a rescan.

**Build Risk:** `ProgramOrchestrator` uses `TopicScanner.checkReadiness()` as a
stage-advancement gate; if readiness can be stale, the orchestrator may advance a program stage
before all signals are present — corrupting downstream program state for skills that depend on
a complete, consistent signal set.

**Dimension:** Correctness

`COMMIT-ENTRY`

---

### Now write your live entries

For each surprise you find in the signal artifacts, write a numbered prose block (Surprise 1,
Surprise 2, ...) with labeled sub-fields: Surprise, Signal Source, Design Impact, Build Risk,
Dimension. Use labeled prose — not a table.

After each entry, run this checklist:

**COMMIT-ENTRY Checklist:**

  ✓ Surprise — Does it name a specific B-# belief and state what was expected vs. what was
    found? If not — add the B-# label and make the expectation/finding contrast explicit.

  ✓ Signal Source — Does it name one specific artifact with name, namespace, and date (not a
    generic phrase)? If not — pick the single most relevant artifact and rewrite.

  ✓ Design Impact — Does it name a specific component, API, or flow (not "the system" or "the
    architecture")? If not — name the specific element and rewrite as a full sentence.

  ✓ Build Risk — Does it name a specific downstream component or contract at risk from the
    Design Impact change? Is it genuinely different from Design Impact (not a restatement)?
    If not — ask yourself "what could fail because of the Design Impact change?" and rewrite.

All four: yes? Emit `COMMIT-ENTRY`.
Any no? Fix the failing field, then re-run the checklist.

**One more check before you close Stage 4:**
- Does at least one entry contradict a Stage 1 belief? If not, look again.
- Do you have at least two GATE-CONFIRMED entries? If not, extend the sweep.

**Closing Stage 4:** All entries written, all COMMIT-ENTRY tokens emitted, ≥1 contradicts a
B-# belief, ≥2 GATE-CONFIRMED entries. Scan Dimension values; fix prohibited synonyms. Emit:
`COMMIT-STAGE-4`

---

## Stage 5 — What the surprises mean for the team

**You need:** COMMIT-STAGE-4.

Make a table with one row per surprise:

  | Surprise # | Key Implication | Priority | Next Team / Skill |

Priority options: Critical · High · Medium · Low.

For Next Team / Skill, name a specific skill (like `flow-trigger`) or a specific role (like
"API contract owner"). "TBD" doesn't count.

**Before closing Stage 5:** Table complete; every row has a named skill or role. Emit:
`COMMIT-STAGE-5`

---

## Stage 6 — What you now think about each belief

**You need:** COMMIT-STAGE-5.

Make a table with one row per belief from Stage 1:

  | Belief # | Belief Statement | Revision Direction | Verdict |

Revision Direction: how this belief should be updated given what you found. Or confirm it
stands unchanged.

Verdict — pick exactly one:
- COHERENT: the evidence is consistent with this belief
- CONTRADICTORY: the evidence directly contradicts this belief; it needs to be revised
- FOREKNOWLEDGE-FLAGGED: this belief looks like it was written after the evidence was seen

For each belief, also write: CLEAR (no foreknowledge concern) or FLAGGED.

If any belief gets FOREKNOWLEDGE-FLAGGED, flag it prominently and stop before Stage 7 until
the user has confirmed what to do.

**Before closing Stage 6:** All beliefs have a Revision Direction and Verdict; foreknowledge
status recorded for all; no unresolved flags. Scan Dimension values; fix prohibited synonyms.
Emit: `COMMIT-STAGE-6`

---

## Stage 7 — Write the artifact

**You need:** COMMIT-STAGE-6 and no unresolved foreknowledge flags.

Write `{topic}-reflect-{date}.md` including: topic name, date, Opening Model summary, all
Stage 4 surprise entries in full numbered prose block format, Stage 5 implications table,
Stage 6 verdict table.

Confirm the file is written, or paste the complete content if you don't have file system access.

Emit: `COMMIT-STAGE-7`
```

---

## V-05

**Variation axis:** Combined — role sequence + inertia framing
**Hypothesis:** Adding a fourth Auditor role and an explicit Inertia Test in Stage 3 Check 4
sharpens the "genuine surprise" filter. The Inertia Test — "would a status-quo skeptic agree
this is a genuine surprise?" — forces the Challenger to take the perspective of someone looking
for reasons the team already knew this. Combined with an explicit "Opening Model Predicted /
Evidence Showed" delta framing before each Surprise statement, Stage 4 entries carry a before/
after contrast that makes the contradiction crisp and reviewable. The Auditor role adds
independent oversight of the belief revision verdict, separating synthesis (Role 3) from audit
(Role 4) — closing the loop with a role that cannot rationalize surprises away post-hoc.

---

```
# topic-reflect — Skill Body Prompt (V-05: Role Sequence + Inertia Framing)

## PURPOSE

This skill synthesizes unexpected findings from signal artifacts gathered for a topic. For each
surprise: name it, trace it to its source signal, assess design impact, name build risk. The
reflect artifact records what the team learned that it did not expect — and what that means for
design, build risk, and belief revision.

Four roles execute this skill in sequence:
- Role 1: Belief Historian — reconstructs the team's pre-evidence epistemic state (Stages 1–2)
- Role 2: Adversarial Challenger — tests whether the evidence qualifies for synthesis (Stages 3–3.5)
- Role 3: Surprise Synthesizer — writes the surprise entries and implications (Stages 4–5)
- Role 4: Auditor — reviews the verdict table and governs artifact write (Stages 6–7)

---

## GATE SEQUENCE OVERVIEW

| Stage | Role | Token Emitted | Halt Condition |
|-------|------|--------------|----------------|
| Stage 1 | Belief Historian | COMMIT-STAGE-1 | < 3 beliefs: HALT |
| Stage 2 | Belief Historian | COMMIT-STAGE-2 | 0 artifacts: HALT |
| Stage 3 | Adversarial Challenger | GATE-CONFIRMED / GATE-REJECTED | — |
| Stage 3.5 | Adversarial Challenger | COMMIT-STAGE-3-CLEAN / COMMIT-STAGE-3-FLAGGED | FLAGGED: HALT |
| Stage 4 | Surprise Synthesizer | COMMIT-STAGE-4 | < 2 GATE-CONFIRMED: extend |
| Stage 5 | Surprise Synthesizer | COMMIT-STAGE-5 | — |
| Stage 6 | Auditor | COMMIT-STAGE-6 | FOREKNOWLEDGE-FLAGGED: HALT |
| Stage 7 | Auditor | COMMIT-STAGE-7 | — |

---

## VOCABULARY RULE — CLOSED DIMENSION SET

This rule applies to all four roles at every stage exit.

Canonical set (closed): Feasibility · Usability · Scalability · Adoptability · Correctness

Prohibited synonyms — replace before emitting any commit token:

  | Prohibited | Canonical Substitute |
  |------------|---------------------|
  | Reliability | Correctness |
  | Performance | Scalability |
  | Maintainability | Correctness |
  | Learnability | Usability |
  | Viability | Feasibility |

At every stage EXIT gate, the active role scans all dimension values written in that stage
and replaces any prohibited name with its canonical substitute.

---

## ROLE 1: BELIEF HISTORIAN — STAGES 1 AND 2

The Belief Historian reconstructs the team's epistemic state before evidence was gathered.
The Historian does not evaluate evidence. The Historian records what was believed.

### STAGE 1 — OPENING MODEL AND EPISTEMIC PROFILE

**ENTER contract:** Topic name and artifact list available. If no artifacts exist, halt: "No
signal artifacts found. topic-reflect requires at least one source signal."

**Historian executes:**

1. Opening Model: State the topic name and summarize the feature intent in two to four
   sentences from the team's pre-evidence perspective.

2. Epistemic Profile: A paragraph characterizing how well-understood the topic was before
   signals were gathered. Address: team confidence level, dominant assumptions, primary
   uncertainty areas.

3. Belief Enumeration: List at least three beliefs held before evidence gathering, labeled
   B-01, B-02, B-03, ... Each belief is a declarative sentence stating what the team expected
   to be true. If fewer than three beliefs can be reconstructed, write placeholders and halt.

**EXIT criterion:** Opening Model + Epistemic Profile + ≥3 labeled beliefs. Scan dimension
values (none expected). Emit: `COMMIT-STAGE-1`

---

### STAGE 2 — SIGNAL INVENTORY

**ENTER contract:** COMMIT-STAGE-1 present.

**Historian executes:**

1. List all signal artifacts: artifact name, namespace, date.

2. Note canonical namespaces (scout, draft, review, flow, trace, prove, listen, program, topic)
   with no artifact. Missing namespaces are not errors; note them.

3. Count total artifacts. If zero, halt.

**EXIT criterion:** Inventory complete, count > 0. Emit: `COMMIT-STAGE-2`

The Belief Historian's work is complete.

---

## ROLE 2: ADVERSARIAL CHALLENGER — STAGES 3 AND 3.5

The Adversarial Challenger tests whether the evidence is sufficient for synthesis. The
Challenger does not synthesize surprises.

**The Challenger's special mandate:** Check 4 is the Inertia Test. The Challenger must ask:
"Would a status-quo skeptic — someone who believes the team already knew everything important
— agree that at least one artifact constitutes a genuine surprise?" If the skeptic could
plausibly say "we knew this all along," the test fails. Only evidence that passes the Inertia
Test reaches the Surprise Synthesizer.

### STAGE 3 — FIVE-CHECK QUALIFICATION TABLE

**ENTER contract:** COMMIT-STAGE-2 present.

**Challenger executes:**

| Check | Question | Answer | Verdict |
|-------|----------|--------|---------|
| Check 1: Signal Coverage | Do ≥2 namespaces have artifacts? | — | VALID / INVALID |
| Check 2: Belief Presence | Are ≥3 beliefs in Stage 1? | — | VALID / INVALID |
| Check 3: Artifact Specificity | Does ≥1 artifact name a specific file with date? | — | VALID / INVALID |
| Check 4: Inertia Test | Would a status-quo skeptic agree ≥1 artifact is a genuine surprise — something the team could not have confidently predicted? | — | VALID / INVALID |
| Check 5: Team Readiness | Has the topic been active ≥1 signal cycle? | — | VALID / INVALID |

Check 4 — Inertia Test — requires the Challenger to explicitly state: "A status-quo skeptic
[would / would not] accept this as a genuine surprise because [reason]."

Emit one of: `GATE-CONFIRMED` (all VALID) or `GATE-REJECTED` (any INVALID).

---

### STAGE 3.5 — GATE RESOLUTION

**ENTER contract:** Stage 3 gate token present.

- GATE-CONFIRMED: emit `COMMIT-STAGE-3-CLEAN`.

- GATE-REJECTED: list each INVALID check and its remediation. If Check 4 (Inertia Test) is
  INVALID, describe specifically what additional signal evidence would pass the skeptic test.
  If in-session remediation is possible, request information and re-run Stage 3. If not, emit
  `COMMIT-STAGE-3-FLAGGED` and halt.

Stage 4 does not open without COMMIT-STAGE-3-CLEAN.

---

## ROLE 3: SURPRISE SYNTHESIZER — STAGES 4 AND 5

The Surprise Synthesizer writes the surprise entries and implications. The Synthesizer uses
the delta framing and the Field Reference block as primary tools.

### STAGE 4 — SURPRISE SYNTHESIS

**ENTER contract:** COMMIT-STAGE-3-CLEAN present.

---

#### FIELD REFERENCE BLOCK — Synthesizer's toolset

Consult this block before writing the first entry and before emitting each COMMIT-ENTRY.

**Surprise**
State the unexpected finding. Reference the specific belief it contradicts by label (e.g.,
"Contradicts B-02"). Before writing the Surprise statement, write the delta framing:
  - Opening Model Predicted: [what the team assumed]
  - Evidence Showed: [what was actually found]
Then write the Surprise statement synthesizing the delta. A Surprise without a B-# reference
does not pass the COMMIT-ENTRY gate.

**Signal Source**
Name exactly one artifact: the specific file that is the primary evidence. Include: artifact
name, namespace, date. Phrases such as "multiple sources," "the signals," or "various
artifacts" do not pass the COMMIT-ENTRY gate.

**Design Impact**
Name the specific component, API, flow, or architectural decision that must change. Use its
actual name. Subjects such as "the system," "the architecture," or "the codebase" do not pass
the COMMIT-ENTRY gate.

**Build Risk**
Purpose: Build Risk names what is implicated by the Design Impact change — the downstream
component, dependency, or contract that could fail or require rework.

Paired formula: Design Impact names what must change; Build Risk names what is implicated by
that change — a different component, dependency, or contract that could fail.

Abstract structural gloss: One is forward-looking (what to update); the other is risk-surface
(what could break or require rework). They are two different things and must not be synonyms
or restatements of each other.

A Build Risk that is general or that merely restates the Design Impact does not pass the
COMMIT-ENTRY gate.

---

#### CALIBRATION ENTRY — Surprise 0

**Surprise 0 — Calibration Entry (not a live entry)**

This entry demonstrates the complete, correct form including delta framing. Live entries begin
at Surprise 1. The Surprise 0 label distinguishes this entry from all live entries — live
entries are numbered starting at 1, not 2.

**Opening Model Predicted:** Topic readiness is a stateless derived property — computed fresh
on every query. The scanner has no internal cache; calling `checkReadiness()` always reflects
the current signal state.

**Evidence Showed:** `topic-scanner-state-2026-03-10.md` (namespace: topic) reveals the
scanner caches the last-computed readiness value and only invalidates it on explicit
`topic.invalidate()` events. Late-arriving signals do not update readiness until a forced
rescan is triggered.

**Surprise:** Contradicts B-02. The opening model assumed topic readiness was computed fresh
on every query — a stateless derived property. `topic-scanner-state-2026-03-10.md` (namespace:
topic) reveals the scanner caches the last-computed readiness value and only invalidates it on
explicit `topic.invalidate()` events; late-arriving signals do not update readiness until a
forced rescan is triggered.

**Signal Source:** `topic-scanner-state-2026-03-10.md`, namespace: topic, date: 2026-03-10.

**Design Impact:** `TopicScanner.checkReadiness()` must be refactored to accept a
`forceRecompute: boolean` option, or the caching layer must subscribe to signal-arrival events
and self-invalidate; the current contract makes stale readiness invisible to callers that do
not know to trigger a rescan.

**Build Risk:** `ProgramOrchestrator` uses `TopicScanner.checkReadiness()` as a
stage-advancement gate; if readiness can be stale, the orchestrator may advance a program stage
before all signals are present — corrupting downstream program state for skills that depend on
a complete, consistent signal set.

**Dimension:** Correctness

`COMMIT-ENTRY`

---

#### ENTRY LOOP

For each surprise, write a numbered prose block (Surprise 1, Surprise 2, ...). Each entry
begins with the delta framing, then the labeled sub-fields: Surprise, Signal Source, Design
Impact, Build Risk, Dimension. Do not use tables.

Entry structure:

  Opening Model Predicted: [full sentence — what was assumed]
  Evidence Showed: [full sentence — what was found]

  Surprise: [synthesizes the delta; names B-# belief; specific expectation vs. finding]
  Signal Source: [specific artifact name, namespace, date]
  Design Impact: [specific component/API/flow + nature of required change]
  Build Risk: [specific downstream component/contract at risk from the Design Impact change]
  Dimension: [one of the five canonical names]

After each entry, execute the COMMIT-ENTRY gate:

**COMMIT-ENTRY Gate:**

  ✓ Surprise: Does the delta framing name what was predicted vs. what was found? Does the
    Surprise statement reference a specific B-# belief? If not — add the delta framing and
    B-# label before continuing.

  ✓ Signal Source: Does it name a specific artifact (not a generic phrase) with name,
    namespace, date? If not — identify the single most relevant artifact and rewrite.

  ✓ Design Impact: Does it name a specific component, API, or flow (not "the system" or "the
    architecture")? If not — identify the specific named element and rewrite as a full sentence.

  ✓ Build Risk: Does it name a specific downstream component or contract implicated by the
    Design Impact change? Is it conceptually distinct from Design Impact? If not — ask "what
    could fail because of the Design Impact change?" and rewrite.

All four pass: emit `COMMIT-ENTRY`.
Any fail: rewrite, re-run checklist.

**Before closing Stage 4:**
- At least one live entry contradicts a Stage 1 belief. If none, review artifacts.
- At least two GATE-CONFIRMED entries. If fewer, extend sweep.

**EXIT criterion:** All entries written; all COMMIT-ENTRY tokens emitted; ≥1 contradicts a
B-# belief; ≥2 GATE-CONFIRMED entries. Scan Dimension values; replace prohibited synonyms.
Emit: `COMMIT-STAGE-4`

---

### STAGE 5 — IMPLICATIONS TABLE

**ENTER contract:** COMMIT-STAGE-4 present.

**Synthesizer executes:**

  | Surprise # | Key Implication | Priority | Next Team / Skill |

Priority: Critical · High · Medium · Low.
Next Team / Skill: at least one specific skill or role per row. Generic entries not permitted.

**EXIT criterion:** Table complete; ≥1 named skill or role. Emit: `COMMIT-STAGE-5`

The Surprise Synthesizer's work is complete.

---

## ROLE 4: AUDITOR — STAGES 6 AND 7

The Auditor reviews the belief revision verdicts and governs artifact write. The Auditor's
mandate is epistemic integrity: ensuring beliefs were genuinely held before evidence was
gathered, not constructed post-hoc.

### STAGE 6 — BELIEF REVISION VERDICT TABLE

**ENTER contract:** COMMIT-STAGE-5 present.

**Auditor executes:**

  | Belief # | Belief Statement | Revision Direction | Verdict | Foreknowledge Status |

Revision Direction: specific instruction to update the belief given evidence, or confirmation
it stands.

Verdict — exactly one of:
- COHERENT: evidence consistent; belief stands
- CONTRADICTORY: evidence directly contradicts; belief must be revised
- FOREKNOWLEDGE-FLAGGED: belief appears written after evidence was seen, not before

Foreknowledge Status: CLEAR or FLAGGED. If any belief is FOREKNOWLEDGE-FLAGGED, note this
prominently. Do not advance to Stage 7 without user confirmation.

**Auditor's inertia check:** For each COHERENT verdict, ask whether the Inertia Test spirit
applies — is the belief confirmed because evidence genuinely supports it, or because no
evidence was gathered that could challenge it? Note this distinction in Revision Direction
where relevant.

**EXIT criterion:** All beliefs have Revision Direction + Verdict + Foreknowledge Status; no
unresolved FOREKNOWLEDGE-FLAGGED beliefs. Scan Dimension values; replace prohibited synonyms.
Emit: `COMMIT-STAGE-6`

---

### STAGE 7 — ARTIFACT WRITE

**ENTER contract:** COMMIT-STAGE-6 present; no unresolved FOREKNOWLEDGE-FLAGGED beliefs.

**Auditor executes:**

Write `{topic}-reflect-{date}.md` containing: topic name, date, Opening Model summary (Stage
1), all Stage 4 surprise entries in full numbered prose block format (including delta framing),
Stage 5 implications table, Stage 6 verdict table.

Emit: `COMMIT-STAGE-7`
```
