# topic-retro — Quest Variate R8 — V-01 through V-05

---

## V-01 — Output Format: Table-Dominant

**Variation axis**: Output format
**Hypothesis**: Forcing all three retrospective sections into structured tables eliminates prose drift, makes verdict assignment unambiguous, and produces outputs that score deterministically against rubric criteria.

---

You are running a post-commitment retrospective on a feature topic. A commitment has already been made. Your job is not to re-litigate the decision — it is to measure signal quality and extract one forward-looking practice change.

**Invocation**: `/topic-retro [topic-name]` or `/topic-retro [topic-name] AMEND:[scope]`

---

### Phase 1 — Commitment Context

State the topic name and describe the commitment in one sentence (what was committed to, and when). This is the fixed reference point for all accuracy verdicts.

---

### Phase 2 — Signal Accuracy Table

Produce a table with exactly these columns:

| Signal | Namespace | Predicted Outcome | Actual Outcome | Verdict |
|--------|-----------|-------------------|----------------|---------|

**Verdict values**: `C` (correct) | `P` (partially correct) | `W` (wrong) | `ND` (no data — signal not gathered)

Rules:
- One row per signal that was gathered or should have been gathered.
- `ND` rows represent signals that were in scope but absent — include them.
- Predicted Outcome must be a falsifiable claim, not a description of the signal artifact.
- Actual Outcome must come from post-ship evidence, not from the signal artifact itself.

Immediately below the table, state the accuracy ratio: `X C + Y P out of Z gathered signals (ND excluded from denominator)`.

---

### Phase 3 — Gap Table

Produce a table with exactly these columns:

| Signal | Namespace | Would It Have Changed the Decision? | Why Absent |
|--------|-----------|--------------------------------------|------------|

Rules:
- Only include signals that were absent (ND from Phase 2) or gathered too late to influence the decision.
- "Would It Have Changed the Decision?" must be answered Yes / Possibly / No — not prose.
- "Why Absent" names the structural reason: skipped intentionally, no owner, no process, out of scope.

---

### Phase 4 — Echo Table

The Echo is the single most unexpected finding — something that could not have been predicted from the signals gathered. It must not restate a wrong prediction or a gap.

Produce a single-row table:

| Unexpected Finding | Systemic Pattern | Practice Change |
|--------------------|------------------|-----------------|

Rules:
- Unexpected Finding: one sentence, specific, falsifiable.
- Systemic Pattern: names the recurring failure mode this finding belongs to, not just this instance.
- Practice Change: one concrete action to address the systemic pattern.

Only one row. If multiple candidates exist, select the one with the highest leverage on future signal quality.

---

### Phase 5 — Phase Seal

Close with a seal block:

```
RETRO SEAL
Topic: {topic name}
Commitment: {C/P/W/ND} -- {one-line summary}
Accuracy Rate: {ratio}
Gap Count: {n}
Echo: {one-phrase label}
AMEND Scope: {scope or N/A}
```

Each field carries a format string. Labels alone are not sufficient.

---

### AMEND Modifier

When `AMEND:[scope]` is present:

1. Declare scope at the top of Phase 2: "AMEND scope: [scope]. Signals outside this scope are excluded."
2. Phase 2 primary table contains only in-scope signals.
3. A secondary table lists excluded signals: `| Signal | Namespace | Exclusion Reason |`. No commentary from the primary table bleeds into the secondary table.
4. Accuracy ratio denominates against in-scope signals only.
5. Phase Seal AMEND Scope field must name the scope explicitly.

---

## V-02 — Role Sequence: Gap-First

**Variation axis**: Role sequence
**Hypothesis**: Leading with gap analysis reframes the retrospective as a learning exercise rather than a scorecard. Surfaces what was structurally absent before measuring what was correct, producing richer Echo nominations.

---

You are running a post-commitment retrospective on a feature topic. A commitment has already been made. Do not re-litigate the decision. Measure what was missing first, then score what was gathered, then surface the unexpected.

**Invocation**: `/topic-retro [topic-name]` or `/topic-retro [topic-name] AMEND:[scope]`

---

### Phase 1 — Commitment Context

State: (a) the topic name, (b) the nature of the commitment in one sentence.

---

### Phase 2 — Gap Analysis (Run First)

Before scoring anything, enumerate what was absent.

For each of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic), state:
- What signal was gathered (if any)
- What signal was absent

Then identify the 1–3 gaps with highest leverage: signals whose absence could plausibly have changed the decision, delayed commitment, or altered implementation scope.

For each high-leverage gap, name:
- The signal
- Why it was absent (structural reason, not blame)
- Whether its presence would have changed the decision: Yes / Possibly / No

---

### Phase 3 — Signal Accuracy

Now score signals that were gathered.

Use this format for each signal:

```
Signal: [name]
Namespace: [namespace]
Predicted: [what the signal claimed or implied]
Actual: [what post-ship evidence showed]
Verdict: [C / P / W / ND]
```

After all signals, state the accuracy ratio: `X C + Y P out of Z gathered (ND excluded)`.

---

### Phase 4 — Echo

The Echo is the single unexpected finding that no gathered signal predicted and no gap analysis anticipated.

State it in this structure:
- **Finding**: one sentence
- **Why Unexpected**: what the signals implied instead
- **Systemic Pattern**: the recurring failure mode this belongs to
- **Practice Change**: one concrete next action

One Echo only. A wrong prediction restated as unexpected is not an Echo.

---

### Phase 5 — Recommendation

Name one practice change for future signal gathering. The recommendation must name:
- The specific gap or Echo it addresses
- The namespace or process step to change
- The measurable outcome that would indicate success

---

### Phase 6 — Phase Seal

```
RETRO SEAL
Topic: {topic name}
Commitment: {C/P/W/ND} -- {one-line summary}
Accuracy Rate: {ratio}
Gap Count: {n}
Echo: {one-phrase label}
AMEND Scope: {scope or N/A}
```

---

### AMEND Modifier

When `AMEND:[scope]` is present:

1. Declare scope at the top of Phase 2: "AMEND scope: [scope]."
2. Gap analysis covers in-scope signals only.
3. Excluded signals appear in a secondary table after the primary gap analysis: `| Signal | Namespace | Exclusion Reason |`.
4. Signal Accuracy covers in-scope signals only.
5. Accuracy ratio denominates against in-scope signals.
6. Phase Seal AMEND Scope field names the scope explicitly.

---

## V-03 — Phrasing Register: Narrative-First

**Variation axis**: Phrasing register
**Hypothesis**: Conversational, narrative-first framing ("tell the story") produces richer Echo content and more honest wrong-prediction acknowledgment than imperative checklist framing. The risk is structural looseness; the prompt enforces structure as a constraint on the narrative, not as the primary mode.

---

You are running a post-commitment retrospective. Tell the story of this feature's signal journey — what was gathered, what was missed, and what surprised everyone. The story has a required shape, but it should read as a retrospective, not a form.

**Invocation**: `/topic-retro [topic-name]` or `/topic-retro [topic-name] AMEND:[scope]`

---

### Opening: Set the Scene

In 2–3 sentences: what was the topic, what was the commitment, and when did it ship? This grounds all accuracy claims that follow.

---

### Act 1: What the Signals Said

Walk through the signals that were gathered before commitment. For each, describe:

- What it was meant to test
- What it actually found
- Whether it was right, partially right, or wrong

Use a verdict marker at the end of each signal's description: **(C)**, **(P)**, **(W)**, or **(ND)** if the signal was absent.

After all signals, state the accuracy ratio plainly: "X out of Y gathered signals were fully correct."

---

### Act 2: What Was Missing

Describe what the signal map looked like in hindsight. Which namespaces had nothing? Which had something that arrived too late?

For the 1–3 most significant gaps, explain:
- What was missing
- Why it wasn't gathered — and be honest about whether that was a structural gap or a skip
- Whether having it would have changed the decision

---

### Act 3: The Echo

Every retrospective has one moment where the team says "we didn't see that coming." Find that moment.

The Echo is not a wrong prediction — it's something that couldn't have been predicted from the signals gathered. Describe it plainly:

- What happened
- What the signals implied would happen instead
- What pattern of failure this belongs to (not just this feature — the recurring one)

One Echo. If you have more than one candidate, pick the highest-leverage one.

---

### Closing: The One Thing to Change

Name one practice change. Connect it explicitly to the gap or Echo you just described. Make it specific enough that someone could act on it next week.

---

### Phase Seal

End with:

```
RETRO SEAL
Topic: {topic name}
Commitment: {C/P/W/ND} -- {one-line summary}
Accuracy Rate: {ratio}
Gap Count: {n}
Echo: {one-phrase label}
AMEND Scope: {scope or N/A}
```

---

### AMEND Modifier

When `AMEND:[scope]` is present:

Open Act 1 with: "This retrospective is scoped to [scope]. The following signals are excluded and listed separately."

Run the primary narrative for in-scope signals only.

After Act 2, add a secondary section: "**Excluded Signals**" — a table listing each excluded signal, its namespace, and why it's out of scope. No prose from Act 1 or Act 2 references excluded signals.

Accuracy ratio covers in-scope signals only. Phase Seal AMEND Scope field names the scope.

---

## V-04 — Combined: Table-Dominant + Inertia Framing

**Variation axes**: Output format + Inertia framing
**Hypothesis**: Adding an explicit "Inertia Competitor" column to the Signal Accuracy table forces the question of whether signals were gathered against the status quo alternative, not just against the new approach. Most wrong predictions are wrong because they compared the feature to an ideal, not to doing nothing. Making inertia visible in the table structure surfaces this bias.

---

You are running a post-commitment retrospective. You will measure signal quality against two baselines: (1) did the signals predict the outcome of the new approach, and (2) did the signals account for the status-quo alternative — the cost of not shipping?

**Invocation**: `/topic-retro [topic-name]` or `/topic-retro [topic-name] AMEND:[scope]`

---

### Phase 1 — Commitment Context

State: (a) topic name, (b) commitment in one sentence, (c) what the status-quo alternative was — what would have happened if the feature had not shipped.

The status-quo alternative is the inertia competitor. It must be named explicitly.

---

### Phase 2 — Signal Accuracy Table

| Signal | Namespace | Predicted Outcome | Inertia Competitor Accounted For? | Actual Outcome | Verdict |
|--------|-----------|-------------------|-----------------------------------|----------------|---------|

**Verdict values**: `C` | `P` | `W` | `ND`

**Inertia Competitor Accounted For?**: `Yes` | `No` | `Partial`
- Yes: the signal explicitly compared to the status-quo alternative
- Partial: the signal mentioned the alternative but did not quantify or test it
- No: the signal evaluated the new approach in isolation

Rules:
- One row per gathered or absent signal.
- ND rows represent absent signals — include them.
- Predicted Outcome is a falsifiable claim against the commitment context.
- Actual Outcome comes from post-ship evidence.

Immediately below the table, state:
- Accuracy ratio: `X C + Y P out of Z gathered (ND excluded)`
- Inertia coverage ratio: `X signals accounted for inertia competitor out of Z gathered`

---

### Phase 3 — Gap Table

| Signal | Namespace | Would It Have Changed the Decision? | Why Absent | Was This an Inertia-Blind Gap? |
|--------|-----------|--------------------------------------|------------|-------------------------------|

**Was This an Inertia-Blind Gap?**: `Yes` if the signal would have tested against the status-quo alternative and that test was skipped. `No` otherwise.

---

### Phase 4 — Echo Table

| Unexpected Finding | Whether Inertia Was the Hidden Cause | Systemic Pattern | Practice Change |
|--------------------|--------------------------------------|------------------|-----------------|

Rules:
- One row only.
- "Whether Inertia Was the Hidden Cause": was the surprise actually the status-quo baseline reasserting itself? Answer Yes / No / Unclear.
- Systemic Pattern and Practice Change follow standard Echo rules.

---

### Phase 5 — Inertia Framing Summary

After all tables, answer in 2–3 sentences: Did the signal set adequately account for the inertia competitor? If not, what type of signal (by namespace) would have closed that gap?

This section informs the recommendation in Phase 6.

---

### Phase 6 — Recommendation

Name one practice change. Connect it to the gap, Echo, or inertia framing gap it addresses. Specify the namespace and the measurable outcome.

---

### Phase 7 — Phase Seal

```
RETRO SEAL
Topic: {topic name}
Commitment: {C/P/W/ND} -- {one-line summary}
Accuracy Rate: {ratio}
Inertia Coverage Rate: {ratio}
Gap Count: {n}
Echo: {one-phrase label}
AMEND Scope: {scope or N/A}
```

---

### AMEND Modifier

When `AMEND:[scope]` is present:

1. Declare scope at top of Phase 2.
2. Primary table: in-scope signals only.
3. Secondary table after primary: `| Signal | Namespace | Exclusion Reason |` for excluded signals. No cross-contamination.
4. Inertia coverage ratio denominates against in-scope signals only.
5. Phase Seal AMEND Scope field names the scope.

---

## V-05 — Combined: Lifecycle Emphasis + AMEND Enforcement

**Variation axes**: Lifecycle emphasis + AMEND scope enforcement
**Hypothesis**: Making the signal lifecycle explicit as a phase structure — from pre-commitment gathering through post-ship measurement — produces cleaner phase boundaries, better AMEND scope compliance, and seal format strings that are contractually precise rather than label-only.

---

You are running a post-commitment retrospective. The retrospective traces the full signal lifecycle: signals gathered before commitment, signals that were absent, signals whose predictions were tested post-ship, and the unexpected finding that no signal covered. Each phase seals before the next opens.

**Invocation**: `/topic-retro [topic-name]` or `/topic-retro [topic-name] AMEND:[scope]`

---

### Lifecycle Phase 1 — Commitment Anchor

**Purpose**: Fix the reference point for all accuracy verdicts.

State:
- Topic name
- Commitment (one sentence: what was decided and when)
- Signal window: the time period during which pre-commitment signals were gathered

Seal Phase 1 before proceeding:

```
PHASE 1 SEAL
Topic: {topic name}
Commitment: {description} -- {date or sprint}
Signal Window: {start} to {end}
AMEND Scope: {scope or N/A}
```

---

### Lifecycle Phase 2 — Pre-Commitment Signal Map

**Purpose**: Enumerate what was gathered during the signal window.

For each namespace (scout, draft, review, flow, trace, prove, listen, program, topic), state:
- Signal gathered: name it, or mark `—` if absent
- Namespace status: `Covered` | `Partial` | `Absent`

Then produce the Signal Accuracy table:

| Signal | Namespace | Gathered In Window? | Predicted Outcome | Actual Outcome | Verdict |
|--------|-----------|---------------------|-------------------|----------------|---------|

**Gathered In Window?**: `Yes` | `Late` (after commitment) | `No`
**Verdict**: `C` | `P` | `W` | `ND`

Accuracy ratio: `X C + Y P out of Z in-window gathered signals`.

Seal Phase 2 before proceeding:

```
PHASE 2 SEAL
Namespaces Covered: {n}/9
Signals In Window: {n}
Late Signals: {n}
Absent Signals: {n}
Accuracy Rate: {ratio}
```

---

### Lifecycle Phase 3 — Gap Analysis

**Purpose**: Identify what was structurally absent and assess its counterfactual impact.

Gap table:

| Signal | Namespace | In Window? | Would It Have Changed the Decision? | Structural Reason Absent |
|--------|-----------|------------|--------------------------------------|--------------------------|

Structural reasons: `No owner` | `No process` | `Skipped intentionally` | `Out of scope (AMEND)` | `Timing — arrived late` | `Unknown`

For gaps where "Would It Have Changed the Decision?" = Yes or Possibly, annotate with an inertia tag: did the gap leave the status-quo alternative unexamined?

Seal Phase 3 before proceeding:

```
PHASE 3 SEAL
Total Gaps: {n}
Decision-Altering Gaps: {n}
Inertia-Blind Gaps: {n}
```

---

### Lifecycle Phase 4 — Post-Ship Measurement Window

**Purpose**: Describe the evidence basis for Actual Outcome verdicts in Phase 2.

State:
- Post-ship measurement window (when post-ship evidence was gathered)
- Evidence sources used (e.g., metrics, user feedback, incident reports)
- Any signals whose verdicts remain unresolved due to insufficient post-ship data — mark these `ND` in Phase 2 and explain here

This phase has no table. Prose only. 3–5 sentences.

Seal Phase 4 before proceeding:

```
PHASE 4 SEAL
Measurement Window: {start} to {end}
Evidence Sources: {list}
Unresolved Verdicts: {n}
```

---

### Lifecycle Phase 5 — Echo

**Purpose**: Surface the one unexpected finding that no signal predicted and no gap anticipated.

State in labeled fields:

- **Finding**: one sentence, specific
- **Signal That Should Have Caught It**: the signal that, if gathered, would have predicted this
- **Why No Signal Caught It**: the structural failure mode
- **Systemic Pattern**: the recurring pattern this belongs to, not just this instance
- **Practice Change**: one concrete action

One Echo only. A restated wrong prediction or gap is not an Echo.

Seal Phase 5:

```
PHASE 5 SEAL
Echo: {one-phrase label}
Systemic Pattern: {pattern name}
Practice Change: {action}
```

---

### Lifecycle Phase 6 — Recommendation

Name one practice change drawn from the gap analysis or Echo. It must:
- Name the specific gap or Echo it addresses
- Name the namespace or lifecycle phase to change
- State the measurable outcome

---

### Final Retro Seal

```
RETRO SEAL
Topic: {topic name}
Commitment: {C/P/W/ND} -- {one-line summary}
Signal Window: {start} to {end}
Measurement Window: {start} to {end}
Accuracy Rate: {ratio}
Gap Count: {n}
Echo: {one-phrase label}
AMEND Scope: {scope or N/A}
```

---

### AMEND Modifier

When `AMEND:[scope]` is present:

1. **Phase 1 Seal**: AMEND Scope field names the scope.
2. **Phase 2**: Primary table contains in-scope signals only. After the primary table, produce a secondary table: `| Signal | Namespace | Exclusion Reason |` for all excluded signals. Primary table prose does not reference excluded signals.
3. **Phase 3**: Gap analysis covers in-scope signals only. Excluded signals do not appear in the gap table — they are already listed in the Phase 2 secondary table.
4. **Phase 2 Seal**: Absent Signals count covers in-scope only.
5. **Accuracy ratio**: denominates against in-scope in-window gathered signals.
6. **Final Retro Seal**: AMEND Scope field names the scope explicitly.

---

## Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | Output format — table-dominant | Tables eliminate prose drift; verdicts become deterministic |
| V-02 | Role sequence — gap-first | Surfacing absences before scoring accuracy reframes the exercise as learning |
| V-03 | Phrasing register — narrative-first | Story framing produces richer Echo content at the cost of structural looseness |
| V-04 | Table-dominant + Inertia framing | Inertia Competitor column surfaces baseline-comparison bias in wrong predictions |
| V-05 | Lifecycle emphasis + AMEND enforcement | Explicit phase seals with format-string contracts produce cleaner AMEND compliance |
