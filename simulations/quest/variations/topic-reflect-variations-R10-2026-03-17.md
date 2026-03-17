# topic-reflect — Quest Variations Round 10

---

## V-01

**Axis**: Lifecycle emphasis — every stage carries explicit ENTER conditions and EXIT criteria as verifiable pre/post-condition contracts.

**Hypothesis**: Explicit verifiable contracts at each stage boundary allow the model to self-audit progress without relying on sequential instruction parsing alone, reducing mid-execution gate confusion and omission of structural requirements.

---

### Gate Sequence Overview

Before Stage 1 begins, review the full gate topology. This table is your navigation map — every stage transition is controlled by a token; every halt condition is binary.

| Stage | ENTER Condition | Exit Token(s) | Halt Condition |
|-------|----------------|---------------|----------------|
| 1 | Signal artifact list present | COMMIT-STAGE-1 | Missing epistemic profile or fewer than 3 beliefs → do not advance |
| 2 | COMMIT-STAGE-1 emitted | COMMIT-STAGE-2 | No candidate surprises found → halt and report |
| 3 | COMMIT-STAGE-2 emitted | COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED | FLAGGED → halt, do not write artifact; fewer than 2 GATE-CONFIRMED → extend sweep before token |
| 4 | COMMIT-STAGE-3-CLEAN emitted | COMMIT-STAGE-4 | COMMIT-STAGE-3-FLAGGED was emitted → skip Stage 4 entirely |
| 5 | COMMIT-STAGE-4 emitted | COMMIT-STAGE-5 | Every cluster missing a named Next Team / Skill → do not advance |
| 6 | COMMIT-STAGE-5 emitted | COMMIT-STAGE-6 | All beliefs CONFIRMED with no CONTRADICTED → halt and re-examine Stage 4 |

---

### Dimension Vocabulary — Closed Set

The only valid epistemic dimension names are:

> **Feasibility · Usability · Scalability · Adoptability · Correctness**

Do not substitute. The following synonyms are explicitly prohibited and their canonical replacements are:

| Prohibited | Use Instead |
|------------|-------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness or Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

**Self-repair rule**: Before emitting any stage-advance token, scan every dimension name cell. If a prohibited synonym appears, correct it using the table above before emitting.

---

### Stage 1: Opening Model

**ENTER**: A list of gathered signal artifacts is available. If no artifact list is accessible, halt and request it before proceeding.

Record your opening model — beliefs about what the signals will reveal — before reviewing them for surprises. This model is your epistemic commitment; Stage 6 will evaluate it.

Write at least 3 beliefs, labeled B-1, B-2, B-3 (extend as needed). Each belief must be a genuine prior assumption, not a hedge.

For each belief, produce an epistemic profile: rate your confidence on each of the five canonical dimensions as HIGH / MEDIUM / LOW.

```
B-1: [Belief statement]
  Feasibility:   HIGH / MEDIUM / LOW
  Usability:     HIGH / MEDIUM / LOW
  Scalability:   HIGH / MEDIUM / LOW
  Adoptability:  HIGH / MEDIUM / LOW
  Correctness:   HIGH / MEDIUM / LOW
```

**EXIT**: At least 3 beliefs present, each with a complete 5-dimension epistemic profile using only canonical names. No prohibited synonyms present. Emit **COMMIT-STAGE-1**.

---

### Stage 2: Signal Review

**ENTER**: COMMIT-STAGE-1 has been emitted.

Review the signal artifacts. Identify observations that were NOT anticipated by any Stage 1 belief. Do not filter or judge yet. List candidate surprises.

Label each: CS-1, CS-2, CS-3...

For each candidate: one sentence naming the observation and the artifact it came from (artifact name, namespace, or date — no "multiple sources").

**EXIT**: At least 2 candidate surprises listed, each with a source artifact named. Emit **COMMIT-STAGE-2**.

---

### Stage 3: Adversarial Gate

**ENTER**: COMMIT-STAGE-2 has been emitted.

**Foreknowledge check** (before adversarial checks): For each candidate surprise, verify that the source artifact was gathered before the opening model beliefs were formed. If any belief was formed after viewing the artifact, that belief is tainted by foreknowledge.

Emit one of:
- **COMMIT-STAGE-3-CLEAN** — no foreknowledge detected; proceed to adversarial checks
- **COMMIT-STAGE-3-FLAGGED** — foreknowledge detected; name the affected beliefs; halt artifact production

If COMMIT-STAGE-3-FLAGGED is emitted, stop. Do not proceed to Stage 4.

**Adversarial checks** (CLEAN path only):

For each candidate surprise, run the five-check table:

| Check | Question | Verdict per Candidate |
|-------|----------|-----------------------|
| A | Does this contradict a specific B-# belief (not merely add to it)? | VALID / INVALID |
| B | Is the named source artifact a genuine gathered signal (not a re-statement of the brief or task)? | VALID / INVALID |
| C | Would this surprise be obvious to any competent engineer before signals were gathered? | VALID / INVALID |
| D | Is the surprise about the feature or design (not about process, tooling, or logistics)? | VALID / INVALID |
| E | Does this surprise carry a traceable design impact (not purely observational)? | VALID / INVALID |

A candidate is **GATE-CONFIRMED** if it passes at least 4 of 5 checks. Otherwise **GATE-REJECTED**.

**Minimum sweep**: If fewer than 2 GATE-CONFIRMED results after checking all candidates, extend the sweep — review additional signals, add new candidates CS-N, and re-run checks before emitting the gate token.

**EXIT**: Five-check table complete for every candidate. Every candidate has GATE-CONFIRMED or GATE-REJECTED verdict. At least 2 GATE-CONFIRMED rows. Foreknowledge token emitted. Emit **COMMIT-STAGE-4**.

---

### Stage 4: Surprise Documentation

**ENTER**: COMMIT-STAGE-3-CLEAN has been emitted AND COMMIT-STAGE-4 has been emitted.

**Field definitions** for each entry:

- **Surprise**: What was unexpected. Must reference the specific B-# belief it contradicts.
- **Signal Source**: The specific artifact where the observation was found — name it (artifact name, namespace, and/or date). Do not write "multiple sources" or "various signals."
- **Design Impact**: What must change as a result. Name a specific component, API, flow, or decision. Do not write "the system" or "the overall design."
- **Build Risk**: What is implicated by that change — a different component, dependency, or contract that could fail. Design Impact names what must change; Build Risk names what is implicated by that change. These are structurally distinct: one is forward-looking (what to update), the other is risk-surface (what could break or require rework). Write each as a full sentence naming a specific, identifiable thing.

**Format**: Numbered prose blocks with labeled sub-fields. Do not use a table for Stage 4 entries.

---

**Surprise 0 — Worked Calibration Example** (do not modify; use as your format and quality anchor for all live entries):

> **Surprise 0**
>
> Contradicts: B-2
>
> Surprise: The `flow-trigger` skill produced a different event shape than the contract spec described — the `triggered_at` field was absent from 11 of 14 test runs, appearing only in the happy-path scenario, not in retry or timeout paths.
>
> Signal Source: `flow-trigger-golden-2026-02-15.md` (flow namespace)
>
> Design Impact: The `FlowOrchestrator.dispatchTrigger()` method must be updated to validate and inject `triggered_at` before forwarding events downstream — the current pass-through implementation cannot be relied on for non-happy-path runs.
>
> Build Risk: The `EventRouter` contract assumes `triggered_at` is always present for sequencing decisions; if `FlowOrchestrator` inserts validation at the wrong layer, `EventRouter`'s ordering guarantees could silently break without failing existing tests.
>
> COMMIT-ENTRY

---

Write your live entries: **Surprise 1, Surprise 2, ...** for each GATE-CONFIRMED candidate.

Before emitting COMMIT-ENTRY for any entry, verify all four fields:

- Surprise references a specific B-# ✓
- Signal Source names a specific artifact (no "multiple sources") ✓
- Design Impact names a specific component, API, flow, or decision (not "the system") ✓
- Build Risk names a specific component, decision, or contract — not a general risk category; if still general, **rewrite it** before emitting ✓

**EXIT**: All GATE-CONFIRMED surprises documented as numbered prose blocks. Every entry has passed its four-field COMMIT-ENTRY gate. Emit **COMMIT-STAGE-4** (second emission confirms Stage 4 complete).

---

### Stage 5: Cluster Map

**ENTER**: COMMIT-STAGE-4 has been emitted.

Group Stage 4 surprises by theme. For each cluster:

| Cluster | Surprises | Pattern | Next Team / Skill |
|---------|-----------|---------|-------------------|
| [Descriptive name] | S-1, S-3 | [What unifies these surprises structurally] | [Named skill or role — e.g., `/flow:review`, `contract-engineer`, `/trace:permissions`] |

The Next Team / Skill column must name a specific skill or role. "Investigate further" is not sufficient.

**EXIT**: All Stage 4 surprises assigned to a cluster. Every cluster has a named Next Team / Skill entry. Emit **COMMIT-STAGE-5**.

---

### Stage 6: Symmetric Contract Close

**ENTER**: COMMIT-STAGE-5 has been emitted.

For each B-# belief from Stage 1, record its fate:

| Belief | Verdict | Revision Direction |
|--------|---------|-------------------|
| B-1 | CONFIRMED / CONTRADICTED / FOREKNOWLEDGE-FLAGGED | [What changes in the design model, or N/A if confirmed] |
| B-2 | ... | ... |

At least one belief must receive CONTRADICTED. If every belief is CONFIRMED, halt — return to Stage 4 and verify that surprises were genuinely contradictory, not confirmatory.

Foreknowledge final record (choose one):
- **CLEAR** — no flagged beliefs; this artifact is valid evidence
- **FLAGGED** — name the affected beliefs; this artifact should not be treated as clean evidence

**EXIT**: Every B-# from Stage 1 appears in the verdict table. At least one CONTRADICTED verdict present. Foreknowledge status declared. Emit **COMMIT-STAGE-6**.

---

---

## V-02

**Axis**: Output format — non-Stage-4 components use structured tables throughout; Stage 4 remains labeled prose blocks (per C-11); all gate checks, epistemic profiles, and cluster maps are table-native.

**Hypothesis**: Table scaffolding in gate-intensive stages (especially Stage 3) makes adversarial checks and foreknowledge resolution harder to elide or collapse — the model must populate every cell rather than summarizing across candidates in prose.

---

### Dimension Vocabulary

The only valid epistemic dimension names are:

**Feasibility · Usability · Scalability · Adoptability · Correctness**

Do not substitute. Prohibited synonyms and their canonical replacements:

| Prohibited Synonym | Canonical Replacement |
|--------------------|----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness or Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

Before emitting any gate token, scan all dimension name cells and replace prohibited synonyms using this table.

---

### Stage 1: Opening Model

Record at least 3 prior beliefs about what the signals will reveal, labeled B-1 through B-N. Use the table below for your epistemic profile. All five dimension columns must use canonical names.

| Belief | Statement | Feasibility | Usability | Scalability | Adoptability | Correctness |
|--------|-----------|-------------|-----------|-------------|--------------|-------------|
| B-1 | [Belief] | H/M/L | H/M/L | H/M/L | H/M/L | H/M/L |
| B-2 | [Belief] | H/M/L | H/M/L | H/M/L | H/M/L | H/M/L |
| B-3 | [Belief] | H/M/L | H/M/L | H/M/L | H/M/L | H/M/L |

Extend rows as needed. Do not omit any dimension column. Emit **COMMIT-STAGE-1**.

---

### Stage 2: Signal Review

Review gathered signal artifacts and list candidate surprises — observations not anticipated by any B-# belief. Do not filter yet.

| Candidate | Observation (one sentence) | Source Artifact |
|-----------|---------------------------|-----------------|
| CS-1 | | [artifact name / namespace / date] |
| CS-2 | | [artifact name / namespace / date] |

Extend rows as needed. Source Artifact must name the specific artifact — no "multiple sources." Emit **COMMIT-STAGE-2**.

---

### Stage 3: Adversarial Gate

**Foreknowledge check first**: Determine whether any Stage 1 belief was formed after the source artifact was viewed. If yes: emit **COMMIT-STAGE-3-FLAGGED**, name the affected beliefs, halt. Do not proceed.

If no foreknowledge: emit **COMMIT-STAGE-3-CLEAN**, then run the five-check table.

**Five-check table**: For each candidate, mark VALID or INVALID in each check column.

| Candidate | A: Contradicts B-#? | B: Genuine signal? | C: Non-obvious? | D: Design-relevant? | E: Traceable impact? | Verdict |
|-----------|--------------------|--------------------|-----------------|--------------------|-----------------------|---------|
| CS-1 | VALID/INVALID | VALID/INVALID | VALID/INVALID | VALID/INVALID | VALID/INVALID | GATE-CONFIRMED / GATE-REJECTED |
| CS-2 | VALID/INVALID | VALID/INVALID | VALID/INVALID | VALID/INVALID | VALID/INVALID | GATE-CONFIRMED / GATE-REJECTED |

Check definitions:
- **A**: Contradicts a specific B-# (not merely adds information)
- **B**: Source is a genuine gathered signal, not a re-statement of the brief
- **C**: Would not be obvious to a competent engineer before signals were gathered
- **D**: About the feature or design, not process or tooling
- **E**: Carries a traceable design impact, not purely observational

Verdict: GATE-CONFIRMED if ≥ 4 of 5 VALID; otherwise GATE-REJECTED.

If fewer than 2 GATE-CONFIRMED rows result, extend the sweep: add new CS-N rows from additional signal artifacts and re-run before advancing.

Emit **COMMIT-STAGE-4**.

---

### Stage 4: Surprise Documentation

**ENTER**: COMMIT-STAGE-3-CLEAN and COMMIT-STAGE-4 both emitted.

**Stage 4 uses prose blocks, not a table.** Reason: narrative specificity cannot be reliably compressed into table cells without format pressure causing truncation.

**Field definitions**:
- **Surprise**: The unexpected observation. Must name the specific B-# it contradicts.
- **Signal Source**: Named artifact — name, namespace, and/or date. No "multiple sources."
- **Design Impact**: What must change — a specific component, API, flow, or decision. Not "the system."
- **Build Risk**: What is implicated by that change. Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail. Write as distinct full sentences.

**Surprise 0 — Worked Example** (do not modify):

> **Surprise 0**
>
> Contradicts: B-3
>
> Surprise: The `topic` skill's signal-count threshold for declaring readiness was crossed in 6 of 7 simulation runs, but the READY verdict was never emitted — the threshold logic exists in the spec but is absent from the skill's emit block.
>
> Signal Source: `topic-plan-golden-2026-02-20.md` (topic namespace)
>
> Design Impact: The `TopicReadinessEvaluator.evaluate()` method must be extended to emit a READY token when the threshold is met — the current implementation only logs the count without branching.
>
> Build Risk: The `quest-score` skill queries `TopicReadinessEvaluator` output to decide when to run scoring; if the READY token is added without updating `quest-score`'s listener contract, scoring may run twice or not at all.
>
> COMMIT-ENTRY

Write live entries for each GATE-CONFIRMED candidate: **Surprise 1, Surprise 2, ...**

Before COMMIT-ENTRY, verify: B-# referenced · artifact named · component-specific Design Impact · specific (not categorical) Build Risk. If Build Risk is still a general category, rewrite it before emitting.

Emit **COMMIT-STAGE-4** when all entries are complete.

---

### Stage 5: Cluster Map

Group Stage 4 surprises by theme. Every row must have a named Next Team / Skill — not "investigate."

| Cluster | Entries | Pattern | Next Team / Skill |
|---------|---------|---------|-------------------|
| | S-1, S-2 | | [e.g., `/signal:trace`, `integration-engineer`] |

Emit **COMMIT-STAGE-5**.

---

### Stage 6: Symmetric Contract Close

Verdict table for each B-# from Stage 1:

| Belief | Verdict | Revision Direction |
|--------|---------|-------------------|
| B-1 | CONFIRMED / CONTRADICTED / FOREKNOWLEDGE-FLAGGED | |
| B-2 | | |

At least one CONTRADICTED required. If none present, return to Stage 4.

Foreknowledge status: **CLEAR** or **FLAGGED** (name affected beliefs if FLAGGED).

Emit **COMMIT-STAGE-6**.

---

---

## V-03

**Axis**: Phrasing register — direct second-person imperative throughout; lower formality, higher directive density; prohibitions stated as active rules not passive conditions.

**Hypothesis**: Imperative voice with explicit named prohibitions reduces instruction-interpretation drift — the model executes rather than interprets, reducing surface-form compliance without semantic compliance.

---

### Before You Begin: Read This Completely

You are running `topic-reflect`. Your job is to synthesize surprises — things you did not expect — from the signals gathered for this topic. This is not a summary of findings. It is a synthesis of what the signals contradicted.

Work through six stages in order. Do not skip a stage. Do not advance past a stage until you have emitted its token.

**The only valid dimension names are: Feasibility · Usability · Scalability · Adoptability · Correctness.** Do not write Reliability, Performance, Complexity, Maintainability, or Discoverability. If you catch yourself writing one of these, replace it: Reliability → Correctness, Performance → Scalability, Complexity → Correctness or Feasibility, Maintainability → Adoptability, Discoverability → Usability or Adoptability. Check this before emitting every token.

---

### Stage 1: Write Your Opening Model

Write at least 3 beliefs about what the gathered signals probably contain. Label them B-1, B-2, B-3. These are your predictions before you look for surprises — commit to them.

For each belief, rate your confidence on each dimension: Feasibility, Usability, Scalability, Adoptability, Correctness — HIGH, MEDIUM, or LOW.

Use this format exactly:

```
B-1: [What you believe the signals will show]
  Feasibility:   HIGH / MEDIUM / LOW
  Usability:     HIGH / MEDIUM / LOW
  Scalability:   HIGH / MEDIUM / LOW
  Adoptability:  HIGH / MEDIUM / LOW
  Correctness:   HIGH / MEDIUM / LOW
```

When you have at least 3 beliefs with complete profiles, emit **COMMIT-STAGE-1**.

---

### Stage 2: Find Your Candidates

Go through the signal artifacts. Write down every observation that your Stage 1 beliefs did not anticipate. Do not filter — just list.

Label each one CS-1, CS-2, CS-3. For each, write one sentence: what you observed, and which artifact you found it in. Name the artifact specifically — don't write "multiple sources" or "various signals."

When you have at least 2 candidates with named sources, emit **COMMIT-STAGE-2**.

---

### Stage 3: Run the Gate

**First, check for foreknowledge.** Did you look at any of these source artifacts before writing your Stage 1 beliefs? If yes, that belief is tainted — emit **COMMIT-STAGE-3-FLAGGED**, name which beliefs are affected, and stop. Do not write the artifact.

If there is no foreknowledge, emit **COMMIT-STAGE-3-CLEAN** and run the five checks.

For each candidate, answer these five questions VALID or INVALID:

| Check | Question | CS-1 | CS-2 | ... |
|-------|----------|------|------|-----|
| A | Does it contradict a specific B-# (not just add to it)? | | | |
| B | Is the source a real gathered signal (not a copy of the brief)? | | | |
| C | Would this have been non-obvious before you gathered signals? | | | |
| D | Is it about the design or feature (not about process or tooling)? | | | |
| E | Does it have a traceable design impact (not just an observation)? | | | |

If a candidate gets at least 4 VALID answers: **GATE-CONFIRMED**. Otherwise: **GATE-REJECTED**.

You need at least 2 GATE-CONFIRMED results. If you don't have them, go back to Stage 2, add more candidates, and re-run this table before emitting anything.

When you have at least 2 GATE-CONFIRMED rows and the table is complete, emit **COMMIT-STAGE-4**.

---

### Stage 4: Write Your Surprises

**Write prose blocks, not a table.** Every entry gets four labeled sub-fields. Here is what each one means:

- **Surprise** — what was unexpected; name the B-# it contradicts
- **Signal Source** — which artifact you found this in; give its name, namespace, and/or date; do not write "multiple sources"
- **Design Impact** — what has to change; name a specific component, API, flow, or decision; do not write "the system" or "the design as a whole"
- **Build Risk** — what gets implicated by that change; Design Impact names what must change, Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail; write these as two distinct things, not paraphrases of each other

**Start with Surprise 0.** This is a worked example — do not modify it. Use it as your quality anchor for everything that follows.

---

**Surprise 0** (worked example — do not modify):

> **Surprise 0**
>
> Contradicts: B-1
>
> Surprise: The `listen-support` skill produced actionable triage categories in only 3 of 8 runs — in the remaining 5 it collapsed all input into a single "General Feedback" bucket, losing structure the downstream `listen-adoption` skill depends on.
>
> Signal Source: `listen-support-golden-2026-03-01.md` (listen namespace)
>
> Design Impact: The `SupportTriageRouter.classify()` method needs a minimum-category enforcement rule — the current implementation allows unbounded collapse and the spec never constrained it.
>
> Build Risk: The `listen-adoption` skill's input contract assumes at least 3 triage categories exist before it begins scoring; if `SupportTriageRouter` collapses to 1, `listen-adoption` will silently score against empty buckets without raising an error.
>
> COMMIT-ENTRY

---

Now write **Surprise 1, Surprise 2, ...** for each of your GATE-CONFIRMED candidates.

Before you write COMMIT-ENTRY for any entry, check all four fields:
- Does Surprise name a B-#? ✓
- Does Signal Source name a specific artifact? ✓
- Does Design Impact name a specific component, API, or decision — not "the system"? ✓
- Does Build Risk name a specific component, contract, or dependency — not a general category like "risk to the codebase"? ✓ If it is still general, rewrite it before continuing.

When all GATE-CONFIRMED candidates have entries, emit **COMMIT-STAGE-4**.

---

### Stage 5: Make a Cluster Map

Group your surprises by pattern. For each group, fill in this table:

| Cluster | Surprises | What unifies them | Who addresses this next |
|---------|-----------|-------------------|------------------------|
| | S-1, S-2 | | [Name a skill or role — e.g., `/flow:trigger`, `API-contract-owner`] |

The last column must name something specific. "Investigate" is not an answer.

Emit **COMMIT-STAGE-5**.

---

### Stage 6: Close the Contract

Go back to your Stage 1 beliefs. For each B-#, say what happened to it:

| Belief | What happened | What changes in the design model |
|--------|--------------|----------------------------------|
| B-1 | CONFIRMED / CONTRADICTED / FOREKNOWLEDGE-FLAGGED | |

At least one belief must say CONTRADICTED. If they all say CONFIRMED, go back to Stage 4 — your surprises were not contradictions.

End with foreknowledge status: **CLEAR** (artifact is valid) or **FLAGGED** (name the beliefs; artifact is not clean evidence).

Emit **COMMIT-STAGE-6**.

---

---

## V-04

**Axis combination**: Lifecycle emphasis (per-stage ENTER/EXIT contracts) + Output format (table-dominant for gate and profile stages; prose for Stage 4).

**Hypothesis**: ENTER/EXIT contracts give the model local verifiability at each boundary; table scaffolding in structured stages gives the model a visible completion signal (all cells populated = done). Together they produce a self-auditing execution path that catches omission at two levels simultaneously.

---

### Gate Sequence Overview

| Stage | ENTER Condition | Mandatory Format | Exit Token | Halt If |
|-------|----------------|-----------------|------------|---------|
| 1 | Signal artifact list available | Epistemic profile table | COMMIT-STAGE-1 | Fewer than 3 beliefs or any prohibited dimension name |
| 2 | COMMIT-STAGE-1 emitted | Candidate table | COMMIT-STAGE-2 | Fewer than 2 candidates with named sources |
| 3 | COMMIT-STAGE-2 emitted | Five-check table | COMMIT-STAGE-3-CLEAN or -FLAGGED + COMMIT-STAGE-4 | FLAGGED → halt; fewer than 2 GATE-CONFIRMED → extend sweep first |
| 4 | COMMIT-STAGE-3-CLEAN + COMMIT-STAGE-4 emitted | Numbered prose blocks | COMMIT-STAGE-4 (second) | Any entry missing a field or emitting general Build Risk |
| 5 | COMMIT-STAGE-4 (second) emitted | Cluster table | COMMIT-STAGE-5 | Any cluster missing named Next Team / Skill |
| 6 | COMMIT-STAGE-5 emitted | Verdict table | COMMIT-STAGE-6 | No CONTRADICTED verdict |

---

### Dimension Vocabulary — Closed Set

> **Feasibility · Usability · Scalability · Adoptability · Correctness**
> No substitutions. Prohibited synonyms → canonical replacements:
> Reliability → Correctness · Performance → Scalability · Complexity → Correctness or Feasibility · Maintainability → Adoptability · Discoverability → Usability or Adoptability · Testability → Correctness or Feasibility

**Exit repair rule**: Before emitting any token, scan dimension name cells. Correct prohibited synonyms using the mapping above.

---

### Stage 1: Opening Model

**ENTER**: Signal artifact list is present and accessible.

Record prior beliefs about what the signals will show. Minimum 3. Use the epistemic profile table — no prose substitution permitted.

| Belief | Statement | Feasibility | Usability | Scalability | Adoptability | Correctness |
|--------|-----------|-------------|-----------|-------------|--------------|-------------|
| B-1 | | H/M/L | H/M/L | H/M/L | H/M/L | H/M/L |
| B-2 | | H/M/L | H/M/L | H/M/L | H/M/L | H/M/L |
| B-3 | | H/M/L | H/M/L | H/M/L | H/M/L | H/M/L |

**EXIT**: Table has at least 3 rows. All dimension cells populated. No prohibited synonym in any dimension column. Emit **COMMIT-STAGE-1**.

---

### Stage 2: Signal Review

**ENTER**: COMMIT-STAGE-1 emitted.

List candidate surprises — observations not anticipated by any B-# belief. Use the candidate table.

| Candidate | Observation (one sentence) | Source Artifact (name / namespace / date) |
|-----------|---------------------------|------------------------------------------|
| CS-1 | | |
| CS-2 | | |

Do not write "multiple sources" or leave Source Artifact blank. Add rows as needed.

**EXIT**: At least 2 rows with populated Source Artifact cells (specific artifact names, not categories). Emit **COMMIT-STAGE-2**.

---

### Stage 3: Adversarial Gate

**ENTER**: COMMIT-STAGE-2 emitted.

**Foreknowledge check**: Were any Stage 1 beliefs formed after viewing the source artifacts?
- Yes → emit **COMMIT-STAGE-3-FLAGGED**, name affected beliefs, halt
- No → emit **COMMIT-STAGE-3-CLEAN**, proceed

**Five-check table** (CLEAN path only):

| Candidate | A: Contradicts B-#? | B: Genuine signal? | C: Non-obvious? | D: Design-relevant? | E: Traceable impact? | Verdict |
|-----------|--------------------|--------------------|-----------------|--------------------|-----------------------|---------|
| CS-1 | | | | | | GATE-CONFIRMED / GATE-REJECTED |
| CS-2 | | | | | | GATE-CONFIRMED / GATE-REJECTED |

Verdict: GATE-CONFIRMED = ≥ 4 VALID. Extend sweep if fewer than 2 GATE-CONFIRMED.

**EXIT**: Table fully populated. Every candidate has a verdict. Minimum 2 GATE-CONFIRMED rows. Foreknowledge token emitted. Emit **COMMIT-STAGE-4**.

---

### Stage 4: Surprise Documentation

**ENTER**: COMMIT-STAGE-3-CLEAN emitted AND COMMIT-STAGE-4 (first) emitted.

**Stage 4 uses prose blocks only.** No table for entries.

**Build Risk definitional formula**: Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail. These are structurally distinct: Design Impact is forward-looking (what to update); Build Risk is risk-surface (what could break). Each must be a full sentence naming a specific, identifiable entity.

**Surprise 0 — Worked Example** (do not modify; this is your entry-zero anchor):

> **Surprise 0**
>
> Contradicts: B-2
>
> Surprise: The `scout-feasibility` skill skipped cost modeling in 4 of 6 simulation runs where the prompt contained a time constraint, producing incomplete feasibility verdicts that omitted the most decision-relevant dimension.
>
> Signal Source: `scout-feasibility-scorecard-R3-2026-03-14.md` (quest/scorecards)
>
> Design Impact: The `FeasibilityAnalyzer.evaluate()` method must be refactored to treat time-constraint detection as a prerequisite gate — cost modeling cannot be optional when a time constraint is present.
>
> Build Risk: The `scout-requirements` skill reads `FeasibilityAnalyzer` output and assumes completeness of the verdict before routing; if `FeasibilityAnalyzer` adds a prerequisite gate, `scout-requirements`'s routing logic will need an updated incomplete-verdict handler or it will route on stale data.
>
> COMMIT-ENTRY

Write **Surprise 1, Surprise 2, ...** for each GATE-CONFIRMED candidate.

Per-entry exit gate before COMMIT-ENTRY:
- B-# referenced ✓
- Specific artifact named in Signal Source ✓
- Specific component/API/flow named in Design Impact (not "the system") ✓
- Specific component/contract named in Build Risk (not a general risk category — if still general, rewrite before emitting) ✓

**EXIT**: All GATE-CONFIRMED surprises documented. Every entry passed its exit gate. Emit **COMMIT-STAGE-4** (second emission).

---

### Stage 5: Cluster Map

**ENTER**: COMMIT-STAGE-4 (second) emitted.

| Cluster | Stage 4 Entries | Unifying Pattern | Next Team / Skill |
|---------|----------------|-----------------|-------------------|
| | | | [specific skill or role — not "investigate"] |

**EXIT**: All Stage 4 entries assigned. Every Next Team / Skill cell names a specific skill or role. Emit **COMMIT-STAGE-5**.

---

### Stage 6: Symmetric Contract Close

**ENTER**: COMMIT-STAGE-5 emitted.

| Belief | Verdict | Revision Direction |
|--------|---------|-------------------|
| B-1 | CONFIRMED / CONTRADICTED / FOREKNOWLEDGE-FLAGGED | |

Every B-# from Stage 1 must appear. At least one CONTRADICTED required.

Foreknowledge final: **CLEAR** or **FLAGGED** (name beliefs if FLAGGED).

**EXIT**: All beliefs in table. At least one CONTRADICTED verdict. Foreknowledge declared. Emit **COMMIT-STAGE-6**.

---

---

## V-05

**Axis combination**: Surprise 0 as entry-zero structural anchor + Build Risk paired definitional formula (C-26) embedded in field definition + vocabulary self-repair as active EXIT-gate protocol.

**Hypothesis**: Three mechanisms working at different levels — a definitional formula that encodes the Design Impact / Build Risk structural relationship as a property of the field pair (conceptual anchor), a worked entry the model extends from position zero (imitation floor), and a self-repair EXIT instruction that converts the vocabulary table into an active runtime protocol (compliance enforcement) — produce higher cross-field specificity and vocabulary correctness than any single mechanism alone.

---

### Dimension Vocabulary — Active Rule

The only valid epistemic dimension names are:

> **Feasibility · Usability · Scalability · Adoptability · Correctness**

No substitutions permitted. Prohibited synonyms with canonical replacements:

| Prohibited | Replace With |
|------------|-------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness or Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

**Active repair protocol**: This table is not a reference resource — it is an execution rule. Before emitting any gate token, scan every dimension name in your output. If a prohibited synonym appears, correct it using the table before emitting. This check is mandatory, not advisory.

---

### Stage Gate Overview

| Stage | Token to Emit | Halt Condition |
|-------|--------------|----------------|
| 1 — Opening Model | COMMIT-STAGE-1 | Fewer than 3 beliefs; any prohibited dimension name uncorrected |
| 2 — Signal Review | COMMIT-STAGE-2 | Fewer than 2 candidates with named artifact sources |
| 3 — Adversarial Gate | COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED + COMMIT-STAGE-4 | FLAGGED → halt; fewer than 2 GATE-CONFIRMED → extend sweep |
| 4 — Surprise Documentation | COMMIT-ENTRY per entry; COMMIT-STAGE-4 | Build Risk is general → rewrite before COMMIT-ENTRY |
| 5 — Cluster Map | COMMIT-STAGE-5 | Any cluster missing named Next Team / Skill |
| 6 — Contract Close | COMMIT-STAGE-6 | No CONTRADICTED verdict in belief table |

Do not advance past any stage without emitting its token.

---

### Stage 1: Opening Model

Record prior beliefs about what the signals contain. Minimum 3, labeled B-1 through B-N. These are genuine predictions, not hedges.

For each belief, rate your confidence on all five canonical dimensions (HIGH / MEDIUM / LOW):

```
B-1: [Belief statement]
  Feasibility:   HIGH / MEDIUM / LOW
  Usability:     HIGH / MEDIUM / LOW
  Scalability:   HIGH / MEDIUM / LOW
  Adoptability:  HIGH / MEDIUM / LOW
  Correctness:   HIGH / MEDIUM / LOW
```

Apply the active repair protocol before emitting: scan all dimension names, correct any prohibited synonym using the replacement table. Emit **COMMIT-STAGE-1**.

---

### Stage 2: Signal Review

Review signal artifacts. Identify observations not anticipated by any B-# belief. List as candidates CS-1, CS-2, ... One sentence each; include the source artifact name, namespace, and/or date. No "multiple sources." Emit **COMMIT-STAGE-2** when at least 2 candidates are listed.

---

### Stage 3: Adversarial Gate

**Foreknowledge check**: Were any beliefs formed after viewing source artifacts?
- Yes → **COMMIT-STAGE-3-FLAGGED**; name affected beliefs; halt. Do not produce artifact.
- No → **COMMIT-STAGE-3-CLEAN**; proceed.

**Five-check table** (CLEAN path):

| Candidate | A: Contradicts B-#? | B: Genuine signal? | C: Non-obvious? | D: Design-relevant? | E: Traceable impact? | Verdict |
|-----------|--------------------|--------------------|-----------------|--------------------|-----------------------|---------|
| CS-1 | V/I | V/I | V/I | V/I | V/I | GATE-CONFIRMED / GATE-REJECTED |
| CS-2 | V/I | V/I | V/I | V/I | V/I | GATE-CONFIRMED / GATE-REJECTED |

GATE-CONFIRMED = ≥ 4 VALID. If fewer than 2 GATE-CONFIRMED, extend sweep before emitting. Emit **COMMIT-STAGE-4**.

---

### Stage 4: Surprise Documentation

**Stage 4 uses numbered prose blocks only — no table.**

#### Stage 4 Field Definitions

**Surprise**: The unexpected observation. Must name the specific B-# it contradicts.

**Signal Source**: The specific artifact — name, namespace, and/or date. Never "multiple sources" or "various signals."

**Design Impact**: What must change as a result — name a specific component, API, flow, or decision. Never "the system" or "the design."

**Build Risk**: *Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail.* This is the structural distinction between these two fields: Design Impact is forward-looking (the thing to be updated); Build Risk is risk-surface (the thing that could break because of the update). Both must be full sentences naming specific, identifiable entities. They must not be paraphrases of each other. If your Build Risk sentence could be about the same entity as your Design Impact sentence, rewrite Build Risk to name a *different* component, dependency, or contract.

---

**Surprise 0 — Worked Calibration Entry** (do not modify; this is your entry-zero anchor; you will extend a sequence from here):

> **Surprise 0**
>
> Contradicts: B-2
>
> Surprise: The `quest-score` skill emitted a final score even when only 2 of the required 5 signal namespaces had produced artifacts — the coverage gate documented in the spec was absent from the skill's execution path.
>
> Signal Source: `quest-score-variate-R3-2026-03-16.md` (quest/golden)
>
> Design Impact: The `QuestScoreEngine.compute()` method must add a coverage pre-check that counts populated namespaces and halts with INSUFFICIENT-COVERAGE if fewer than the minimum are present — the current implementation proceeds unconditionally.
>
> Build Risk: The `quest-rubric` skill's scoring calibration assumes full-coverage inputs; if `QuestScoreEngine` begins emitting INSUFFICIENT-COVERAGE tokens, `quest-rubric`'s verdict thresholds become miscalibrated for partial-coverage runs and its pass/fail boundary drifts without a corresponding rubric update.
>
> COMMIT-ENTRY

---

You have now seen one complete entry. Extend the sequence with **Surprise 1, Surprise 2, ...** for each GATE-CONFIRMED candidate.

**COMMIT-ENTRY gate**: Before writing COMMIT-ENTRY for any entry, run the four-field check:

1. Surprise references a specific B-# ✓
2. Signal Source names a specific artifact — no "multiple sources" ✓
3. Design Impact names a specific component, API, flow, or decision — not "the system" ✓
4. Build Risk names a specific component, dependency, or contract that is *different* from the Design Impact entity — not a general risk category, not a paraphrase of Design Impact; if still general, **rewrite Build Risk before emitting** ✓

Apply the active vocabulary repair protocol: scan all dimension names in entries produced so far; correct any prohibited synonym using the replacement table before emitting COMMIT-ENTRY.

Emit **COMMIT-STAGE-4** when all GATE-CONFIRMED surprises are documented.

---

### Stage 5: Cluster Map

Group Stage 4 surprises by theme. For each cluster:

| Cluster | Stage 4 Entries | Pattern | Next Team / Skill |
|---------|----------------|---------|-------------------|
| | | | [Named skill or role — e.g., `/signal:flow-trigger`, `contract-reviewer`] |

Next Team / Skill must name a specific skill or role. "Investigate" is not acceptable. Emit **COMMIT-STAGE-5**.

---

### Stage 6: Symmetric Contract Close

Verdict table for every B-# from Stage 1:

| Belief | Verdict | Revision Direction |
|--------|---------|-------------------|
| B-1 | CONFIRMED / CONTRADICTED / FOREKNOWLEDGE-FLAGGED | [What changes in the design model, or N/A] |

At least one CONTRADICTED required. If none present, halt — your Stage 4 surprises were confirmatory rather than contradictory; return and re-evaluate.

Foreknowledge final status:
- **CLEAR** — artifact is valid evidence
- **FLAGGED** — name affected beliefs; artifact is not clean evidence

Apply active vocabulary repair protocol one final time before emitting COMMIT-STAGE-6. Emit **COMMIT-STAGE-6**.

---
