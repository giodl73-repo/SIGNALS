# topic-reflect — quest:variate Round 7 (V-01 through V-05)

---

## V-01 — Axis: Pre-Stage Gate Sequence Map

**Variation axis**: Gate topology table (C-15) — the full token map appears before Stage 1 instructions begin.
**Hypothesis**: Front-loading all stage tokens, halt conditions, and execution flow eliminates mid-execution confusion about gate order. The model enters Stage 1 having internalized the full topology rather than discovering it incrementally.

---

You are running **topic-reflect** for the topic: `{{topic}}`.

The one question: *What did we learn that we did not expect?*

This is not a summary of findings. It is a synthesis of surprises — things the signals revealed that your opening model did not predict. Every surprise must be named, traced to its source artifact, and assessed for impact on design direction.

---

### Gate Sequence Overview

Read this table before executing any stage. It maps every commit token, halt condition, and recovery path for the full run.

| Stage | Commit Token(s) | Halt Condition | Recovery |
|-------|----------------|----------------|----------|
| 1 | `COMMIT-STAGE-1` | Fewer than 3 beliefs articulated | Extend belief inventory before proceeding |
| 2 | `COMMIT-STAGE-2` | No signal artifacts found for `{{topic}}` | Stop; report insufficient signal base |
| 3 | `GATE-CONFIRMED` / `GATE-REJECTED` per row; `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | All candidates gate-rejected | Return to Stage 2, extend sweep to adjacent namespaces |
| 4 | `COMMIT-ENTRY` per surprise; `COMMIT-STAGE-4` | — | — |
| 5 | `COMMIT-STAGE-5` | — | — |
| 6 | `COMMIT-STAGE-6` | — | — |

Tokens are binding. Do not advance past a stage without emitting its commit token.

---

### Dimension Vocabulary

The only valid dimension names are:
**Feasibility · Usability · Scalability · Adoptability · Correctness**

Do not substitute synonyms. Prohibited terms and their canonical replacements:

| Prohibited | Replace With |
|-----------|-------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Feasibility or Correctness |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

---

### Stage 1 — Opening Model

Before reading signal artifacts in depth, articulate what you expected.

1. State an **epistemic profile**: for each of the 5 dimensions, rate your prior confidence (Low / Medium / High) and why.
2. Write at least 3 numbered beliefs (**B-1, B-2, B-3, ...**) of the form: *"I expected that [specific aspect of {{topic}}] would reveal [outcome]."* Be concrete. Vague beliefs cannot be tested.
3. Emit `COMMIT-STAGE-1`.

---

### Stage 2 — Signal Survey

1. Locate all signal artifacts for `{{topic}}` under `simulations/`. List each by namespace, skill name, and date.
2. Note any namespaces with no artifacts — these are coverage gaps, not evidence of absence.
3. Emit `COMMIT-STAGE-2`.

---

### Stage 3 — Adversarial Gate

For each candidate surprise identified in Stage 2, run the five-check table:

| Check | Question | Verdict |
|-------|----------|---------|
| Novelty | Was this genuinely absent from the Stage 1 beliefs? | VALID / INVALID |
| Artifact binding | Is there a named artifact as the source? | VALID / INVALID |
| Specificity | Does the surprise name a component, API, flow, or decision — not "the system"? | VALID / INVALID |
| Foreknowledge | Was this known before signals were gathered? | CLEAN / FLAGGED |
| Design relevance | Does this change what the team would build or decide? | VALID / INVALID |

- Rows where any VALID check is INVALID → emit `GATE-REJECTED`.
- Rows where all VALID checks pass → emit `GATE-CONFIRMED`.
- If the Foreknowledge check is FLAGGED on any row → emit `COMMIT-STAGE-3-FLAGGED`; otherwise emit `COMMIT-STAGE-3-CLEAN`.
- If fewer than 2 rows are `GATE-CONFIRMED`, extend the sweep before proceeding.

---

### Stage 4 — Surprise Entries

For each `GATE-CONFIRMED` row, write a numbered prose block. Use the exact sub-field structure below. Do not use a markdown table.

```
**Surprise N**
**Surprise**: [Full sentence describing what was unexpected and why.]
**Signal Source**: [Named artifact — file name, namespace, date. No "multiple sources" generics.]
**Design Impact**: [Full sentence naming the specific component, API, flow, or decision that must change.]
**Build Risk**: [Full sentence naming the specific component, contract, or assumption that could break or require rework.]

COMMIT-ENTRY
```

After all entries, emit `COMMIT-STAGE-4`.

---

### Stage 5 — Cluster Map

Group the Stage 4 surprises by theme. For each cluster, provide:

| Cluster Name | Surprises Included | Implication | Next Team / Skill |
|-------------|-------------------|-------------|-------------------|
| [Name] | [S-N, S-M, ...] | [What this cluster signals for the design] | [Named skill or role — not just "investigate"] |

Emit `COMMIT-STAGE-5`.

---

### Stage 6 — Symmetric Contract Close

Return to each B-# belief from Stage 1. For each:

| Belief | Verdict | Revision Direction |
|--------|---------|--------------------|
| B-1 | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [What changes, if anything] |
| B-2 | … | … |

If any belief is FOREKNOWLEDGE-FLAGGED: name the responsible belief and do not write the artifact — this run is contaminated.

Emit `COMMIT-STAGE-6`.

---

---

## V-02 — Axis: Per-Stage ENTER/EXIT Lifecycle Contracts

**Variation axis**: Every stage is framed as a verifiable contract with explicit ENTER conditions and EXIT criteria (C-19).
**Hypothesis**: Structuring each stage as a pre/post-condition contract — not just a list of instructions — reduces incomplete stage execution. The model can verify it has satisfied exit criteria before advancing, converting instructions into checkpoints.

---

You are running **topic-reflect** for the topic: `{{topic}}`.

The one question: *What did we learn that we did not expect?*

Not a summary. A synthesis of surprises — genuine deviations from the model you held before the signals arrived. Each surprise: name it, trace it to its source artifact, assess its impact on design direction.

---

### Vocabulary Rule

The only valid epistemic dimension names are:
**Feasibility · Usability · Scalability · Adoptability · Correctness**

Do not substitute. "Reliability," "Performance," "Complexity," "Maintainability," and "Discoverability" are prohibited. If you wrote a prohibited term, replace it with its canonical equivalent before emitting.

---

### Stage 1 — Opening Model

**ENTER Stage 1**
- No signal artifacts have been consulted for content. You are articulating priors, not reflections.

**Instructions**
1. Write an epistemic profile: for each of the 5 canonical dimensions, state your prior confidence (Low / Medium / High) and the reasoning behind it.
2. Write at least 3 numbered beliefs (**B-1, B-2, B-3, ...**): *"I expected that [specific aspect] would reveal [outcome]."*
3. Beliefs must be specific enough to be falsifiable. "I expected the signals to be interesting" does not qualify.

**EXIT Stage 1**
- Criterion: Epistemic profile covers all 5 dimensions. At least 3 B-# beliefs are written. All dimension names are canonical.
- Token: `COMMIT-STAGE-1`

---

### Stage 2 — Signal Survey

**ENTER Stage 2**
- `COMMIT-STAGE-1` has been emitted.

**Instructions**
1. Locate all signal artifacts for `{{topic}}` under `simulations/`. List each artifact with namespace, skill name, and date.
2. Note any namespaces with no coverage — these are gaps in the signal base.
3. If no artifacts are found, halt and report: *Insufficient signal base for topic-reflect.*

**EXIT Stage 2**
- Criterion: At least one artifact is listed per namespace with coverage. Gaps are explicitly noted.
- Token: `COMMIT-STAGE-2`

---

### Stage 3 — Adversarial Gate

**ENTER Stage 3**
- `COMMIT-STAGE-2` has been emitted. At least one artifact is in the survey.

**Instructions**

For each candidate surprise, run the five-check table:

| Check | Question | Verdict |
|-------|----------|---------|
| Novelty | Absent from Stage 1 beliefs? | VALID / INVALID |
| Artifact binding | Named source artifact exists? | VALID / INVALID |
| Specificity | Names a specific component, API, flow, or decision? | VALID / INVALID |
| Foreknowledge | Unknown before signal gathering? | CLEAN / FLAGGED |
| Design relevance | Changes a build or design decision? | VALID / INVALID |

- All VALID checks pass → `GATE-CONFIRMED`
- Any VALID check fails → `GATE-REJECTED`
- Any Foreknowledge = FLAGGED → `COMMIT-STAGE-3-FLAGGED`; otherwise → `COMMIT-STAGE-3-CLEAN`
- Fewer than 2 `GATE-CONFIRMED` rows: extend sweep before emitting stage token.

**EXIT Stage 3**
- Criterion: Every candidate has a row with explicit verdicts. At least 2 `GATE-CONFIRMED` rows exist. Foreknowledge resolution is binary (CLEAN or FLAGGED token emitted).
- Token: `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED`

---

### Stage 4 — Surprise Entries

**ENTER Stage 4**
- `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` has been emitted.
- If `COMMIT-STAGE-3-FLAGGED`: record the foreknowledge-implicated belief(s) in Stage 6 and proceed with the non-flagged gate-confirmed rows only.

**Instructions**

For each `GATE-CONFIRMED` row, write a numbered prose block:

```
**Surprise N**
**Surprise**: [Full sentence — what was unexpected and why it matters.]
**Signal Source**: [Named artifact: file name, namespace, date. No "multiple sources" generics.]
**Design Impact**: [Full sentence naming the specific component, API, flow, or decision that must change.]

COMMIT-ENTRY
```

Do not use a markdown table. Every field is a full phrase or sentence — no single-word or two-word entries.

**EXIT Stage 4**
- Criterion: Every `GATE-CONFIRMED` row has a prose block. Every sub-field is complete (no empty or one-word fields). Every entry references a B-# from Stage 1. At least one entry contradicts (not merely confirms) a Stage 1 belief.
- Token: `COMMIT-STAGE-4`

---

### Stage 5 — Cluster Map

**ENTER Stage 5**
- `COMMIT-STAGE-4` has been emitted.

**Instructions**

Group Stage 4 surprises by theme:

| Cluster Name | Surprises | Implication | Next Team / Skill |
|-------------|-----------|-------------|-------------------|
| [Name] | [S-N, ...] | [Full sentence] | [Named skill or role] |

The Next Team / Skill column must name a specific skill or role — not just "investigate" or "review."

**EXIT Stage 5**
- Criterion: All Stage 4 surprises appear in at least one cluster. Every cluster has a named next skill or role.
- Token: `COMMIT-STAGE-5`

---

### Stage 6 — Symmetric Contract Close

**ENTER Stage 6**
- `COMMIT-STAGE-5` has been emitted.

**Instructions**

Return to each B-# belief from Stage 1:

| Belief | Verdict | Revision Direction |
|--------|---------|--------------------|
| B-1 | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [What changes in design direction] |
| B-2 | … | … |

If any belief receives FOREKNOWLEDGE-FLAGGED: name it explicitly and note that the artifact should not be written.

**EXIT Stage 6**
- Criterion: Every B-# belief has a verdict and revision direction. FOREKNOWLEDGE-FLAGGED beliefs are named if present.
- Token: `COMMIT-STAGE-6`

---

---

## V-03 — Axis: Surprise 0 Calibration Example + Build Risk Sub-Field

**Variation axis**: A worked calibration example is embedded as Surprise 0 within the Stage 4 entry sequence (C-20), and each entry includes a Build Risk sub-field (C-22).
**Hypothesis**: Positioning a fully-populated entry as Surprise 0 — rather than a sidebar example — pulls the model into the role of extending a sequence already in progress. The model has already "completed one entry" and observes all four sub-fields populated with realistic specificity before producing its own. Build Risk makes the complementary distinction between forward-looking design change and backward-looking breakage surface.

---

You are running **topic-reflect** for the topic: `{{topic}}`.

The one question: *What did we learn that we did not expect?*

Not a summary. A synthesis of surprises — genuine deviations from the model you held before the signals arrived. Each surprise: name it, trace it to its source artifact, assess its impact on design direction and build risk.

---

### Vocabulary Rule

The only valid epistemic dimension names are:
**Feasibility · Usability · Scalability · Adoptability · Correctness**

Do not substitute. Prohibited synonyms: "Reliability," "Performance," "Complexity," "Maintainability," "Discoverability." Replace any prohibited term with its canonical equivalent before emitting.

---

### Stage 1 — Opening Model

Before consulting any signal artifacts:

1. Write an epistemic profile — for each of the 5 canonical dimensions, your prior confidence (Low / Medium / High) and reasoning.
2. Write at least 3 numbered beliefs (**B-1, B-2, B-3, ...**): *"I expected that [specific aspect of {{topic}}] would reveal [outcome]."* Each belief must be specific enough to be contradicted by evidence.

Emit `COMMIT-STAGE-1`.

---

### Stage 2 — Signal Survey

Locate all signal artifacts for `{{topic}}` under `simulations/`. List each by namespace, skill, and date. Note coverage gaps. If no artifacts exist, halt and report insufficient signal base.

Emit `COMMIT-STAGE-2`.

---

### Stage 3 — Adversarial Gate

For each candidate surprise, run the five-check table:

| Check | Question | Verdict |
|-------|----------|---------|
| Novelty | Absent from Stage 1 beliefs? | VALID / INVALID |
| Artifact binding | Named source artifact exists? | VALID / INVALID |
| Specificity | Names a component, API, flow, or decision — not "the system"? | VALID / INVALID |
| Foreknowledge | Unknown before signal gathering? | CLEAN / FLAGGED |
| Design relevance | Changes a build or design decision? | VALID / INVALID |

All VALID checks pass → `GATE-CONFIRMED`. Any VALID check fails → `GATE-REJECTED`.
Foreknowledge check result → `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED`.
Fewer than 2 `GATE-CONFIRMED` rows: extend sweep.

---

### Stage 4 — Surprise Entries

**Surprise 0 is a calibration entry. It is already complete. Do not modify it. Begin your entries at Surprise 1.**

---

**Surprise 0** *(Calibration — do not modify)*
**Surprise**: The throttle namespace required a backpressure negotiation interface that no prior signal had identified as missing — the scout artifacts implied throttle was a configuration concern, not a protocol concern.
**Signal Source**: flow-throttle-analysis-2026-03-14.md (flow namespace, March 2026) — specifically the event queue saturation scenario at line 47.
**Design Impact**: The ThrottleManager API contract must be extended with a backpressure negotiation method; the existing flush-on-full assumption does not hold under distributed load.
**Build Risk**: The EventQueue component will require async refactoring — the current synchronous flush assumption breaks if backpressure signals arrive out-of-order, which is the expected behavior under the distributed scenario.

COMMIT-ENTRY

---

Now write your Stage 4 entries. For each `GATE-CONFIRMED` row from Stage 3, write a numbered prose block in this exact format:

```
**Surprise N**
**Surprise**: [Full sentence — what was unexpected and why.]
**Signal Source**: [Named artifact: file name, namespace, date. No "multiple sources" generics.]
**Design Impact**: [Full sentence naming the specific component, API, flow, or decision that must change.]
**Build Risk**: [Full sentence naming the specific component, contract, or assumption that could break or require rework — not a general risk statement.]

COMMIT-ENTRY
```

Rules:
- Every entry references at least one B-# from Stage 1.
- At least one entry contradicts (does not merely confirm) a Stage 1 belief.
- No single-word or two-word entries in any sub-field.
- Do not use a markdown table.

After all entries, emit `COMMIT-STAGE-4`.

---

### Stage 5 — Cluster Map

Group Stage 4 surprises by theme:

| Cluster Name | Surprises | Implication | Next Team / Skill |
|-------------|-----------|-------------|-------------------|
| [Name] | [S-N, ...] | [Full sentence] | [Named skill or role — not just "investigate"] |

Emit `COMMIT-STAGE-5`.

---

### Stage 6 — Symmetric Contract Close

Return to each B-# from Stage 1:

| Belief | Verdict | Revision Direction |
|--------|---------|--------------------|
| B-1 | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [What changes] |
| B-2 | … | … |

FOREKNOWLEDGE-FLAGGED beliefs must be named. If any are flagged, note that the artifact should not be published.

Emit `COMMIT-STAGE-6`.

---

---

## V-04 — Axis: Vocabulary Self-Repair Protocol at EXIT Gate

**Variation axis**: The synonym-to-canonical mapping table is an active runtime repair protocol (C-21), embedded as an explicit EXIT audit instruction — not a passive reference list (C-17, C-18).
**Hypothesis**: A mapping table that is merely listed is a reference resource; a mapping table with an explicit EXIT instruction prescribing its use ("before emitting, check this table and correct any violations") converts it into an active repair protocol. The model is not only equipped to detect substitution errors — it is instructed to audit and fix them at a specific gate, closing the vocabulary compliance loop at execution time.

---

You are running **topic-reflect** for the topic: `{{topic}}`.

The one question: *What did we learn that we did not expect?*

Not a summary of what the signals said. A synthesis of surprises — things you did not predict that the signals revealed. Each surprise: name it, trace it to its source, assess its impact on design and build.

---

### Vocabulary Self-Repair Protocol

The only valid epistemic dimension names are:
**Feasibility · Usability · Scalability · Adoptability · Correctness**

**Prohibited synonyms with canonical replacements:**

| Prohibited Term | Canonical Replacement |
|----------------|-----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Feasibility (if about effort) or Correctness (if about behavior) |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |
| Robustness | Correctness |

**Repair rule**: Before emitting any dimension name — in the epistemic profile, in belief statements, or in any later stage — check it against this table. If you wrote a prohibited term, replace it with the canonical equivalent shown. Do not proceed past Stage 1 with a prohibited term in any field.

This table is not a reference. It is a repair protocol. Apply it actively at every emission point.

---

### Stage 1 — Opening Model

Before reading signal artifacts in depth:

1. Write an **epistemic profile**: for each of the 5 canonical dimensions, your prior confidence (Low / Medium / High) and reasoning.

   *EXIT audit*: Before emitting the epistemic profile, check every dimension name against the repair table. Correct any prohibited term before emitting.

2. Write at least 3 numbered beliefs (**B-1, B-2, B-3, ...**): *"I expected that [specific aspect of {{topic}}] would reveal [outcome]."*

   Beliefs must be specific and falsifiable. "I expected signals to confirm the design" does not qualify.

Emit `COMMIT-STAGE-1`.

---

### Stage 2 — Signal Survey

Locate all signal artifacts for `{{topic}}` under `simulations/`. List each by namespace, skill, and date. Note coverage gaps by namespace. If no artifacts exist, halt and report insufficient signal base.

Emit `COMMIT-STAGE-2`.

---

### Stage 3 — Adversarial Gate

For each candidate surprise, run the five-check table:

| Check | Question | Verdict |
|-------|----------|---------|
| Novelty | Absent from Stage 1 beliefs? | VALID / INVALID |
| Artifact binding | Named source artifact exists? | VALID / INVALID |
| Specificity | Names a component, API, flow, or decision — not "the system"? | VALID / INVALID |
| Foreknowledge | Unknown before signal gathering? | CLEAN / FLAGGED |
| Design relevance | Changes a build or design decision? | VALID / INVALID |

All VALID checks pass → `GATE-CONFIRMED`. Any VALID check fails → `GATE-REJECTED`.
Foreknowledge check → `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED`.
Fewer than 2 `GATE-CONFIRMED` rows: extend sweep.

*EXIT audit*: Check all dimension terms in the adversarial gate table against the repair protocol. Correct before emitting.

---

### Stage 4 — Surprise Entries

For each `GATE-CONFIRMED` row, write a numbered prose block:

```
**Surprise N**
**Surprise**: [Full sentence — what was unexpected and why.]
**Signal Source**: [Named artifact: file name, namespace, date. No "multiple sources" generics.]
**Design Impact**: [Full sentence naming the specific component, API, flow, or decision that must change.]

COMMIT-ENTRY
```

Rules:
- Every entry references a B-# from Stage 1. At least one entry contradicts a Stage 1 belief.
- No single-word or two-word entries in any sub-field.
- Do not use a markdown table.

*EXIT audit*: Before emitting `COMMIT-STAGE-4`, verify that no prohibited dimension term appears in any sub-field. Use the repair table to correct violations. Then emit `COMMIT-STAGE-4`.

---

### Stage 5 — Cluster Map

Group Stage 4 surprises by theme:

| Cluster Name | Surprises | Implication | Next Team / Skill |
|-------------|-----------|-------------|-------------------|
| [Name] | [S-N, ...] | [Full sentence] | [Named skill or role — not just "investigate"] |

*EXIT audit*: Check cluster implication text for prohibited terms. Correct before emitting `COMMIT-STAGE-5`.

Emit `COMMIT-STAGE-5`.

---

### Stage 6 — Symmetric Contract Close

Return to each B-# from Stage 1:

| Belief | Verdict | Revision Direction |
|--------|---------|--------------------|
| B-1 | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [What changes] |

FOREKNOWLEDGE-FLAGGED beliefs must be named explicitly. Note that a flagged artifact should not be published.

*EXIT audit*: Final pass — check every dimension name in the full document. Correct any remaining prohibited terms using the repair table before emitting `COMMIT-STAGE-6`.

Emit `COMMIT-STAGE-6`.

---

---

## V-05 — Combination: Gate Map + ENTER/EXIT Contracts + Surprise 0 + Build Risk + Synonym Self-Repair

**Variation axis**: Full stack — gate topology table (C-15), per-stage ENTER/EXIT contracts (C-19), Surprise 0 calibration (C-20), Build Risk sub-field (C-22), synonym self-repair at EXIT (C-17, C-18, C-21).
**Hypothesis**: Each technique closes a different failure mode. Gate topology prevents token ordering errors. ENTER/EXIT contracts prevent incomplete stage execution. Surprise 0 anchors Stage 4 entry quality by imitation. Build Risk makes the Design Impact complement explicit. Synonym self-repair closes vocabulary compliance at execution time. The combination addresses orthogonal failure surfaces simultaneously; no single technique can substitute for another.

---

You are running **topic-reflect** for the topic: `{{topic}}`.

The one question: *What did we learn that we did not expect?*

Not a summary of signals. A synthesis of surprises — genuine deviations from the model you held before the signals arrived. Each surprise is named, traced to its source artifact, and assessed for design impact and build risk.

---

### Vocabulary Self-Repair Protocol

The only valid epistemic dimension names are:
**Feasibility · Usability · Scalability · Adoptability · Correctness**

Do not substitute. Prohibited synonyms and their canonical replacements:

| Prohibited | Replace With |
|-----------|-------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Feasibility or Correctness |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |
| Robustness | Correctness |

**At every stage EXIT**: check all dimension names against this table and correct any violations before emitting the stage token. This table is an active repair protocol, not a reference list.

---

### Gate Sequence Overview

Read this table before executing any stage. It maps every token, halt condition, and recovery path for the full run.

| Stage | Gate Token(s) | Halt Condition | Recovery |
|-------|--------------|----------------|----------|
| 1 | `COMMIT-STAGE-1` | Fewer than 3 beliefs; any prohibited dimension term | Extend beliefs; repair vocabulary |
| 2 | `COMMIT-STAGE-2` | No signal artifacts found | Halt; report insufficient signal base |
| 3 | `GATE-CONFIRMED` / `GATE-REJECTED` per row; `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | Fewer than 2 GATE-CONFIRMED rows | Extend sweep to adjacent namespaces |
| 4 | `COMMIT-ENTRY` per surprise; `COMMIT-STAGE-4` | — | — |
| 5 | `COMMIT-STAGE-5` | — | — |
| 6 | `COMMIT-STAGE-6` | — | — |

Tokens are binding. Do not advance past a stage without its commit token.

---

### Stage 1 — Opening Model

**ENTER Stage 1**
- No signal artifacts have been read for content. You are articulating priors.

**Instructions**
1. Write an **epistemic profile**: for each of the 5 canonical dimensions, state your prior confidence (Low / Medium / High) and reasoning.
2. Write at least 3 numbered beliefs (**B-1, B-2, B-3, ...**) of the form: *"I expected that [specific aspect of {{topic}}] would reveal [outcome]."* Each belief must be specific enough to be falsified by evidence.

**EXIT Stage 1**
- Criterion: Epistemic profile covers all 5 dimensions. At least 3 B-# beliefs are present. All dimension names are canonical.
- Vocabulary repair: before emitting, check all dimension names against the repair table and correct any violations.
- Token: `COMMIT-STAGE-1`

---

### Stage 2 — Signal Survey

**ENTER Stage 2**
- `COMMIT-STAGE-1` emitted.

**Instructions**
1. Locate all signal artifacts for `{{topic}}` under `simulations/`. List each by namespace, skill, and date.
2. Note namespaces with no coverage as explicit gaps.
3. If no artifacts exist, halt: *Insufficient signal base for topic-reflect.*

**EXIT Stage 2**
- Criterion: At least one artifact listed. All gaps named explicitly.
- Token: `COMMIT-STAGE-2`

---

### Stage 3 — Adversarial Gate

**ENTER Stage 3**
- `COMMIT-STAGE-2` emitted. At least one artifact is in the survey.

**Instructions**

For each candidate surprise:

| Check | Question | Verdict |
|-------|----------|---------|
| Novelty | Absent from Stage 1 beliefs? | VALID / INVALID |
| Artifact binding | Named source artifact exists? | VALID / INVALID |
| Specificity | Names a component, API, flow, or decision — not "the system"? | VALID / INVALID |
| Foreknowledge | Unknown before signal gathering? | CLEAN / FLAGGED |
| Design relevance | Changes a build or design decision? | VALID / INVALID |

All VALID checks pass → `GATE-CONFIRMED`. Any VALID check fails → `GATE-REJECTED`.
Foreknowledge → `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED`.

**EXIT Stage 3**
- Criterion: Every candidate has explicit per-check verdicts. At least 2 `GATE-CONFIRMED` rows. Foreknowledge token emitted.
- Vocabulary repair: check dimension terms before emitting.
- Token: `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED`

---

### Stage 4 — Surprise Entries

**ENTER Stage 4**
- `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` emitted.
- If FLAGGED: record implicated beliefs in Stage 6; proceed with non-flagged `GATE-CONFIRMED` rows only.

**Surprise 0 is a calibration entry. It is complete. Do not modify it. Begin your entries at Surprise 1.**

---

**Surprise 0** *(Calibration — do not modify)*
**Surprise**: The throttle namespace required a backpressure negotiation interface that no prior signal had identified as missing — scout artifacts implied throttle was a configuration concern, but the flow signals revealed it as a protocol concern with ordering guarantees.
**Signal Source**: flow-throttle-analysis-2026-03-14.md (flow namespace, March 2026) — the event queue saturation scenario at line 47 directly contradicted B-2's assumption about configuration-only throttle scope.
**Design Impact**: The ThrottleManager API contract must be extended with a backpressure negotiation method; the existing flush-on-full assumption does not hold under distributed load conditions.
**Build Risk**: The EventQueue component will require async refactoring — the synchronous flush assumption embedded in the current implementation breaks if backpressure signals arrive out-of-order, which is the expected behavior in the distributed scenario.

COMMIT-ENTRY

---

For each `GATE-CONFIRMED` row, write a numbered prose block in this exact format:

```
**Surprise N**
**Surprise**: [Full sentence — what was unexpected and why it matters.]
**Signal Source**: [Named artifact: file name, namespace, date. No "multiple sources" generics.]
**Design Impact**: [Full sentence naming the specific component, API, flow, or decision that must change.]
**Build Risk**: [Full sentence naming the specific component, contract, or assumption that could break or require rework — not a general risk statement.]

COMMIT-ENTRY
```

Rules:
- Every entry references a B-# from Stage 1. At least one entry contradicts (does not merely confirm) a Stage 1 belief.
- No single-word or two-word entries in any sub-field. Every field is a full phrase or sentence.
- Do not use a markdown table.

**EXIT Stage 4**
- Criterion: Every `GATE-CONFIRMED` row has a complete prose block. All four sub-fields populated. At least one entry contradicts a B-# belief.
- Vocabulary repair: check all dimension references before emitting.
- Token: `COMMIT-STAGE-4`

---

### Stage 5 — Cluster Map

**ENTER Stage 5**
- `COMMIT-STAGE-4` emitted.

**Instructions**

Group Stage 4 surprises by theme:

| Cluster Name | Surprises | Implication | Next Team / Skill |
|-------------|-----------|-------------|-------------------|
| [Name] | [S-N, ...] | [Full sentence] | [Named skill or role — not just "investigate"] |

**EXIT Stage 5**
- Criterion: All Stage 4 surprises appear in at least one cluster. Every cluster has a named next skill or role.
- Vocabulary repair: check implication text before emitting.
- Token: `COMMIT-STAGE-5`

---

### Stage 6 — Symmetric Contract Close

**ENTER Stage 6**
- `COMMIT-STAGE-5` emitted.

**Instructions**

Return to each B-# belief from Stage 1:

| Belief | Verdict | Revision Direction |
|--------|---------|--------------------|
| B-1 | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [What changes in design direction, if anything] |
| B-2 | … | … |

FOREKNOWLEDGE-FLAGGED beliefs: name each explicitly. Note that the artifact should not be published if any are present.

**EXIT Stage 6**
- Criterion: Every B-# belief has a verdict and revision direction. FOREKNOWLEDGE-FLAGGED beliefs named if present.
- Final vocabulary repair: scan the complete document for any prohibited dimension term. Correct all violations using the repair table before emitting.
- Token: `COMMIT-STAGE-6`

---

---

## Variation Summary

| ID | Primary Axis | Key Criteria Targeted | Hypothesis |
|----|-------------|----------------------|------------|
| V-01 | Gate Sequence Map first | C-15, C-17, C-18 | Front-loading token topology prevents mid-execution gate confusion |
| V-02 | Per-stage ENTER/EXIT contracts | C-19, all essentials | Stage-as-contract converts instructions into verifiable checkpoints |
| V-03 | Surprise 0 + Build Risk | C-20, C-22 | Entry-zero imitation pulls quality across all four sub-fields simultaneously |
| V-04 | Vocabulary self-repair at EXIT | C-17, C-18, C-21 | Repair-table-as-active-protocol closes vocabulary loop at execution time |
| V-05 | Full stack combination | C-15, C-17–C-22, all essentials + recommended | Orthogonal failure modes require orthogonal techniques; no single technique substitutes for another |
