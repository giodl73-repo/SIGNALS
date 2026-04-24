# Quest Variate — prove-prototype Round 8 (v8 rubric, 204 pts)

**Date**: 2026-03-15
**Rubric version**: v8 (adds C-27 and C-28)
**Round 7 winner**: V-04 (180/190) — SETUP(THINKER+ANCHOR)/BUILD(MAKER+WATCHER)/CLOSE; conversational imperatives; CLOSE absorbs all trailing sections

**New criteria this round**:
- **C-27**: Completion lines carry FULL|PARTIAL grade when partial satisfaction is structurally possible; PARTIAL case names the absent element. Extends C-22.
- **C-28**: Baseline (B-00) occupies a dedicated container whose enclosed phases are exclusively pre-build measurement. Requires C-24. Extends isolation beyond what C-24 alone guarantees.

**Variation axes**:
- V-01 (single): Completion-grade encoding — inline FULL|PARTIAL token in PHASE N COMPLETE line
- V-02 (single): Output format — labeled-pair grade block as alternate C-27 encoding
- V-03 (single): Lifecycle emphasis — isolated CALIBRATE container for B-00 only
- V-04 (combined): Completion-grade + CALIBRATE isolation
- V-05 (combined): All three + inertia framing (B-00 as named status-quo competitor)

---

## V-01 — Single Axis: Completion-Grade Encoding

**Axis**: Completion-grade encoding (C-27)
**Design hypothesis**: Adding an explicit FULL|PARTIAL grade token to every completion line — embedded inline as the first word after the dash in `PHASE N COMPLETE — FULL:` or `PHASE N COMPLETE — PARTIAL:` — satisfies C-27 without any structural change to the R7 V-04 design. Because the grade token is co-located with the outcome value already required by C-22, C-27 is achieved at zero structural cost: the completion line already carries the result value (C-22); the grade token is appended before it. The CLOSE container absorbs all trailing sections, preserving the C-21 complete-gate-coverage that won Round 7. B-00 is established by ANCHOR in SETUP, satisfying C-26 but not C-28 (SETUP mixes scope + B-00 + measurement, so no isolated baseline container).

---

```
You are running **prove-prototype** for Signal.

**Artifact**: `simulations/prove/investigations/{topic}-prototype-{date}.md`
**Topic**: [Topic]
**Signal**: [Signal]

---

**Before any output**: Read the topic file. Identify the active hypothesis. Do not begin
Phase 1 until you have confirmed a hypothesis exists in the topic file.

---

## CONTAINER: SETUP
*Phases 1–4. Execute all before entering CONTAINER: BUILD.*

### Roles in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| THINKER | Hypothesis restatement, scope exclusions, exclusion validity rationale | Build description, raw measurements, result comparisons, verdict |
| ANCHOR | B-00 baseline measurement, measurement criteria, success/failure thresholds | Scope exclusions, build activity, result interpretation |

---

### Phase 1 — THINKER: Restate the hypothesis
*Execute before Phase 2.*

Write the hypothesis as the first substantive element of your output. Quote or closely
paraphrase from the topic file. Nothing precedes it — no preamble, no context summary, no
prototype description, no result.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"[absent element] — hypothesis not locatable in topic file."]**

---

### Phase 2 — THINKER: Define prototype scope
*Execute before Phase 3. Execute after Phase 1 gate is present in your output.*

State what the prototype will and will not do. Name at least two explicit exclusions. For
each exclusion, state immediately why the test remains valid without it. Both elements must
appear in the same labeled pair.

> **Excluded**: [element]
> **Why the test remains valid without it**: [reason]

> **Excluded**: [element]
> **Why the test remains valid without it**: [reason]

**PHASE 2 COMPLETE — [FULL|PARTIAL]: scope boundary established; [N] exclusion(s) with
co-located validity rationale. [If PARTIAL: "fewer than two paired exclusions — [element]
absent."]**

---

### Phase 3 — ANCHOR: Establish B-00 baseline
*Execute before Phase 4. Execute after Phase 2 gate is present in your output.*

Measure or describe the current state before the prototype is applied — this is B-00, the
inertia baseline. Record what the existing approach produces for the same metric you will
apply in Phase 6. Commit this value now, before any build activity. A baseline introduced
after results are known does not pass.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: B-00 committed = [current-state value or description].
[If PARTIAL: "no measurable current state available — [reason]; B-00 = null baseline."]**

---

### Phase 4 — ANCHOR: Define measurement criteria
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in your
output.*

State what will be measured. State the success threshold (the result that confirms the
hypothesis). State the failure threshold (the result that refutes it). These criteria are
frozen at this gate — MAKER must not modify them after BUILD begins.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: measurement defined; success threshold = [value or
condition]; failure threshold = [value or condition]. [If PARTIAL: "[success|failure]
threshold absent — quantification not possible with available inputs."]**

**CONTAINER: SETUP COMPLETE — [FULL|PARTIAL]: hypothesis locked, scope bounded ([N]
exclusions with validity), B-00 = [value], success/failure thresholds established. [If
PARTIAL: "[element] absent."]**

---

## CONTAINER: BUILD
*Phases 5–6. Execute after CONTAINER: SETUP gate is present in your output. Execute all
before entering CONTAINER: CLOSE.*

### Roles in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| MAKER | Prototype description, build steps, minimality trade-off, replication path | Interpretation of results, result comparison, verdict |
| WATCHER | Raw measurements, literal observation of what occurred | Interpretation of results, comparison to B-00 or threshold, verdict |

---

### Phase 5 — MAKER: Build the prototype
*Execute before Phase 6. Execute after Phase 4 gate is present in your output.*

Describe or implement the prototype. Include only what is necessary to test the hypothesis.
State what was left out and why that omission does not invalidate the test — this trade-off
must appear in the same block as the scope decision. Include all tools, inputs, commands,
and steps needed to reproduce the build. Name any tool not available in this context
explicitly.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [absent element] not specified]. [If PARTIAL:
"replication path incomplete — [absent element] missing."]**

---

### Phase 6 — WATCHER: Record raw measurements
*Execute before entering CONTAINER: CLOSE. Execute after Phase 5 gate is present in your
output.*

Apply the measurement criteria from Phase 4. Record the raw result. Do not interpret. Do
not compare to B-00 or to the threshold. Do not reference the hypothesis verdict.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value or
observation]. [If PARTIAL: "measurement could not be applied — [absent element] missing."]**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built and measured; raw result =
[value]. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CLOSE
*Phases 7–11. Execute after CONTAINER: BUILD gate is present in your output. This container
absorbs all post-evidence sections. Every phase in CLOSE carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Comparison, verdict, counter-evidence, limitations, next step, replication | New measurement criteria not established in Phase 4; baseline not committed in Phase 3 |

---

### Phase 7 — ANALYST: Compare actual vs. predicted
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

State the prediction (from Phase 4). State the observation (from Phase 6). State the delta.
Immediately after the delta, explain why it is what it is — rationale must appear in the
same labeled block. Then compare the observation against B-00.

> **Predicted**: [value or condition from Phase 4]
> **Observed**: [value or observation from Phase 6]
> **Delta**: [match or mismatch description]
> **Why the delta is what it is**: [explanation]
> **vs. B-00 baseline**: [how observation compares to B-00 from Phase 3]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: comparison complete; predicted [value], observed
[value], delta [description], B-00 comparison [recorded | absent — [reason]]. [If PARTIAL:
"[prediction | observation | delta | B-00 comparison] absent."]**

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. The verdict must follow
from Phases 6–7. Do not assert a verdict the evidence does not support. State the reasoning
in the same block as the verdict.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference from Phase 6–7]. [If PARTIAL: "verdict asserted without evidentiary
grounding — [element] absent."]**

---

### Phase 9 — ANALYST: Counter-evidence check
*Execute before Phase 10. Execute after Phase 8 gate is present in your output.*

Check whether any counter-interpretation of the results exists. Close this phase with
exactly one of two dispositions — both are valid; silence is not:

- **(a)** Name the counter-interpretation and rebut it with reasoning grounded in the
  evidence.
- **(b)** State explicitly that no plausible counter-interpretation exists, with a reason.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "phase closed without
explicit disposition — neither case (a) nor (b) was stated."]**

---

### Phase 10 — ANALYST: Limitations and next step
*Execute before Phase 11. Execute after Phase 9 gate is present in your output.*

State one limitation of this prototype or measurement. State one specific next step.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[limitation | next step] absent."]**

---

### Phase 11 — ANALYST: Replication path
*Execute after Phase 10 gate is present in your output.*

List all tools, inputs, commands, and steps needed to reproduce the prototype and
measurement from scratch. No implicit steps. Name any unavailable tool explicitly.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete; all steps explicit. [If
PARTIAL: "[element] not specified — implicit steps remain."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]: comparison, verdict, counter-evidence,
limitations, and replication all recorded; verdict = [word]; C-27 compliance [FULL —
all completion lines carry grade | PARTIAL — [phase N] grade absent]. [If PARTIAL:
"[element] absent."]**
```

---

## V-02 — Single Axis: Output Format (Labeled-Grade Block)

**Axis**: Output format — alternate C-27 encoding via labeled-pair grade block
**Design hypothesis**: C-27 can be satisfied by a dedicated `**Completeness**:` labeled-pair field at the end of each phase block, rather than by embedding the grade token inline within the `PHASE N COMPLETE` line. If this is true, the structural form of the grade encoding is interchangeable: the rubric requires that the grade be present and readable in the completion record, not that it appear as a token within a specific completion-line format. If false — if scoring reveals that the grade token must be embedded in the completion line rather than in a co-located labeled pair — it would imply C-27 has an implicit format constraint not stated in its pass condition, which would be a finding. Container structure and roles are identical to V-01.

---

```
You are running **prove-prototype** for Signal.

**Artifact**: `simulations/prove/investigations/{topic}-prototype-{date}.md`
**Topic**: [Topic]
**Signal**: [Signal]

---

**Before any output**: Read the topic file. Identify the active hypothesis. Do not begin
Phase 1 until you have confirmed a hypothesis exists in the topic file.

---

## CONTAINER: SETUP
*Phases 1–4. Execute all before entering CONTAINER: BUILD.*

### Roles in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| THINKER | Hypothesis restatement, scope exclusions, exclusion validity rationale | Build description, raw measurements, result comparisons, verdict |
| ANCHOR | B-00 baseline measurement, measurement criteria, success/failure thresholds | Scope exclusions, build activity, result interpretation |

---

### Phase 1 — THINKER: Restate the hypothesis
*Execute before Phase 2.*

Write the hypothesis as the first substantive element of your output. Quote or closely
paraphrase from the topic file. Nothing precedes it.

**Phase 1 complete**: hypothesis = "[hypothesis text]"
**Completeness**: FULL | PARTIAL — [If PARTIAL: "[absent element] — hypothesis not
locatable in topic file."]

---

### Phase 2 — THINKER: Define prototype scope
*Execute before Phase 3. Execute after Phase 1 Completeness field is present in your
output.*

State what the prototype will and will not do. Name at least two explicit exclusions. For
each, state why the test remains valid without it. Both must appear in the same labeled pair.

> **Excluded**: [element]
> **Why the test remains valid without it**: [reason]

> **Excluded**: [element]
> **Why the test remains valid without it**: [reason]

**Phase 2 complete**: scope boundary established; [N] exclusion(s) with co-located validity
rationale
**Completeness**: FULL | PARTIAL — [If PARTIAL: "fewer than two paired exclusions — [element]
absent."]

---

### Phase 3 — ANCHOR: Establish B-00 baseline
*Execute before Phase 4. Execute after Phase 2 Completeness field is present in your
output.*

Measure or describe what the current approach produces for the metric you will apply in
Phase 6. This is B-00. Commit it before any build activity.

**Phase 3 complete**: B-00 committed = [current-state value or description]
**Completeness**: FULL | PARTIAL — [If PARTIAL: "no measurable current state — [reason];
B-00 = null."]

---

### Phase 4 — ANCHOR: Define measurement criteria
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 Completeness field is
present in your output.*

State what will be measured, the success threshold (confirms hypothesis), and the failure
threshold (refutes hypothesis). These criteria are frozen at this gate.

**Phase 4 complete**: measurement defined; success = [threshold]; failure = [threshold]
**Completeness**: FULL | PARTIAL — [If PARTIAL: "[success|failure] threshold absent —
quantification not possible."]

**CONTAINER: SETUP COMPLETE**: hypothesis locked, scope bounded ([N] exclusions), B-00 =
[value], thresholds established
**Completeness**: FULL | PARTIAL — [If PARTIAL: "[element] absent."]

---

## CONTAINER: BUILD
*Phases 5–6. Execute after CONTAINER: SETUP Completeness field is present in your output.
Execute all before entering CONTAINER: CLOSE.*

### Roles in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| MAKER | Prototype description, build steps, minimality trade-off, replication path | Interpretation of results, comparison, verdict |
| WATCHER | Raw measurements, literal observation | Interpretation, comparison to B-00 or threshold, verdict |

---

### Phase 5 — MAKER: Build the prototype
*Execute before Phase 6. Execute after Phase 4 Completeness field is present in your
output.*

Describe or implement the prototype. Include only what is necessary to test the hypothesis.
State what was left out and why in the same block as the scope decision. Include all tools,
inputs, commands, and steps to reproduce. Name any unavailable tool explicitly.

**Phase 5 complete**: prototype built; minimality trade-off recorded; replication steps
[all explicit | partial — [absent element] not specified]
**Completeness**: FULL | PARTIAL — [If PARTIAL: "replication path incomplete — [absent
element] missing."]

---

### Phase 6 — WATCHER: Record raw measurements
*Execute before entering CONTAINER: CLOSE. Execute after Phase 5 Completeness field is
present in your output.*

Apply the Phase 4 measurement criteria. Record the raw result. Do not interpret or compare.

**Phase 6 complete**: measurement applied; raw result = [value or observation]
**Completeness**: FULL | PARTIAL — [If PARTIAL: "measurement could not be applied — [absent
element] missing."]

**CONTAINER: BUILD COMPLETE**: prototype built and measured; raw result = [value]
**Completeness**: FULL | PARTIAL — [If PARTIAL: "[element] absent."]

---

## CONTAINER: CLOSE
*Phases 7–11. Execute after CONTAINER: BUILD Completeness field is present in your output.
Absorbs all post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Comparison, verdict, counter-evidence, limitations, next step, replication | New measurement criteria; baseline not committed in Phase 3 |

---

### Phase 7 — ANALYST: Compare actual vs. predicted
*Execute before Phase 8. Execute after Phase 6 Completeness field is present in your
output.*

> **Predicted**: [value from Phase 4]
> **Observed**: [value from Phase 6]
> **Delta**: [match or mismatch]
> **Why the delta is what it is**: [explanation]
> **vs. B-00**: [comparison to Phase 3 baseline]

**Phase 7 complete**: comparison recorded; predicted [value], observed [value], delta
[description], B-00 comparison [recorded | absent]
**Completeness**: FULL | PARTIAL — [If PARTIAL: "[prediction | observation | delta | B-00
comparison] absent."]

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 Completeness field is present in your
output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6–7.

**Phase 8 complete**: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded in [evidence
reference]
**Completeness**: FULL | PARTIAL — [If PARTIAL: "verdict asserted without evidentiary
grounding."]

---

### Phase 9 — ANALYST: Counter-evidence check
*Execute before Phase 10. Execute after Phase 8 Completeness field is present in your
output.*

Close with exactly one of two dispositions:
- **(a)** Named counter-interpretation plus grounded rebuttal.
- **(b)** Explicit statement that no plausible counter-interpretation exists, with a reason.

**Phase 9 complete**: counter-evidence [ADDRESSED — rebuttal on record | CLOSED — no
plausible counter, reason: [reason]]
**Completeness**: FULL | PARTIAL — [If PARTIAL: "phase closed without explicit disposition."]

---

### Phase 10 — ANALYST: Limitations and next step
*Execute before Phase 11. Execute after Phase 9 Completeness field is present in your
output.*

State one limitation. State one specific next step.

**Phase 10 complete**: limitation and next step recorded
**Completeness**: FULL | PARTIAL — [If PARTIAL: "[limitation | next step] absent."]

---

### Phase 11 — ANALYST: Replication path
*Execute after Phase 10 Completeness field is present in your output.*

List all tools, inputs, commands, and steps to reproduce. No implicit steps.

**Phase 11 complete**: replication path complete; all steps explicit
**Completeness**: FULL | PARTIAL — [If PARTIAL: "[element] not specified."]

**CONTAINER: CLOSE COMPLETE**: comparison, verdict, counter-evidence, limitations, and
replication recorded; verdict = [word]
**Completeness**: FULL | PARTIAL — [If PARTIAL: "[element] absent."]
```

---

## V-03 — Single Axis: Lifecycle Emphasis (Isolated CALIBRATE Container)

**Axis**: Lifecycle emphasis — isolated CALIBRATE container for B-00 only (C-28)
**Design hypothesis**: Moving B-00 baseline measurement out of DESIGN and into a dedicated CALIBRATE container — whose enclosed phases are exclusively pre-build measurement — satisfies C-28 without any change to completion-line format. A reader scanning only container headers can confirm that every phase inside CALIBRATE is pre-build activity before inspecting any role label or phase body. DESIGN contains only hypothesis restatement, scope, and measurement criteria; it holds no baseline measurement. Standard completion lines (C-22 only, no FULL|PARTIAL grade) are used, so C-27 does not pass — this is a single-axis test of C-28 isolation in isolation. Container order: DESIGN → CALIBRATE → BUILD → CLOSE. Hypothesis appears as the first phase inside DESIGN, preserving C-01.

---

```
You are running **prove-prototype** for Signal.

**Artifact**: `simulations/prove/investigations/{topic}-prototype-{date}.md`
**Topic**: [Topic]
**Signal**: [Signal]

---

**Before any output**: Read the topic file. Identify the active hypothesis. Do not begin
Phase 1 until you have confirmed a hypothesis exists in the topic file.

---

## CONTAINER: DESIGN
*Phases 1–3. Execute all before entering CONTAINER: CALIBRATE.*
*This container holds hypothesis, scope, and measurement criteria only. No baseline
measurement activity belongs here.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| FRAMER | Hypothesis restatement, scope exclusions, exclusion validity rationale, measurement criteria, success/failure thresholds | Baseline measurement, build activity, raw results, result interpretation |

---

### Phase 1 — FRAMER: Restate the hypothesis
*Execute before Phase 2.*

Write the hypothesis as the first substantive element of your output. Quote or closely
paraphrase from the topic file. Nothing precedes it.

**PHASE 1 COMPLETE — hypothesis = "[hypothesis text]".**

---

### Phase 2 — FRAMER: Define prototype scope
*Execute before Phase 3. Execute after Phase 1 completion line is present in your output.*

State what the prototype will and will not do. Name at least two explicit exclusions. For
each, state why the test remains valid without it in the same labeled pair.

> **Excluded**: [element]
> **Why the test remains valid without it**: [reason]

> **Excluded**: [element]
> **Why the test remains valid without it**: [reason]

**PHASE 2 COMPLETE — scope boundary established; [N] exclusion(s) with co-located validity
rationale.**

---

### Phase 3 — FRAMER: Define measurement criteria
*Execute before entering CONTAINER: CALIBRATE. Execute after Phase 2 completion line is
present in your output.*

State what will be measured. State the success threshold (confirms hypothesis). State the
failure threshold (refutes hypothesis). These criteria are frozen at this gate — BUILDER
must not modify them.

**PHASE 3 COMPLETE — measurement defined; success = [threshold]; failure = [threshold].**

**CONTAINER: DESIGN COMPLETE — hypothesis locked, scope bounded ([N] exclusions),
measurement thresholds established. No baseline measurement in this container.**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container holds exclusively pre-build baseline measurement. No scope definition,
no hypothesis activity, no build steps, and no measurement of experimental conditions
belong here. A reader scanning only this container header and its contents must be able
to confirm that all enclosed activity is pre-build.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | B-00 baseline measurement — the current state for the metric defined in Phase 3 | Prototype description, scope decisions, measurement criteria, experimental results |

---

### Phase 4 — CALIBRATOR: Measure B-00 baseline
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 completion line is present
in your output.*

Measure or describe what the current approach produces for the metric from Phase 3. This is
B-00 — the pre-build, pre-prototype state of the system. Commit this value here and nowhere
else. A baseline introduced after BUILD begins does not pass.

**PHASE 4 COMPLETE — B-00 committed = [current-state value or description; or "null
baseline — no current approach measurable, reason: [reason]"].**

**CONTAINER: CALIBRATE COMPLETE — B-00 = [value]. Exclusively pre-build content confirmed.**

---

## CONTAINER: BUILD
*Phases 5–6. Execute after CONTAINER: CALIBRATE gate is present in your output. Execute all
before entering CONTAINER: CLOSE.*

### Roles in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| BUILDER | Prototype description, build steps, minimality trade-off, replication path | Interpretation of results, comparison to threshold or B-00, verdict |
| RECORDER | Raw measurements, literal observation of what occurred | Interpretation, comparison to B-00 or threshold, verdict |

---

### Phase 5 — BUILDER: Build the prototype
*Execute before Phase 6. Execute after Phase 4 completion line is present in your output.*

Describe or implement the prototype. Include only what is necessary to test the hypothesis.
State what was left out and why in the same block as the scope decision. Include all tools,
inputs, commands, and steps to reproduce. Name any unavailable tool explicitly.

**PHASE 5 COMPLETE — prototype built; minimality trade-off recorded; replication steps
[all explicit | partial — [absent element] not specified].**

---

### Phase 6 — RECORDER: Record raw measurements
*Execute before entering CONTAINER: CLOSE. Execute after Phase 5 completion line is present
in your output.*

Apply the Phase 3 measurement criteria. Record the raw result. Do not interpret or compare.

**PHASE 6 COMPLETE — measurement applied; raw result = [value or observation].**

**CONTAINER: BUILD COMPLETE — prototype built and measured; raw result = [value].**

---

## CONTAINER: CLOSE
*Phases 7–11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Comparison, verdict, counter-evidence, limitations, next step, replication | New measurement criteria not in Phase 3; retroactive baseline not established in Phase 4 |

---

### Phase 7 — ANALYST: Compare actual vs. predicted
*Execute before Phase 8. Execute after Phase 6 completion line is present in your output.*

> **Predicted**: [value from Phase 3]
> **Observed**: [value from Phase 6]
> **Delta**: [match or mismatch]
> **Why the delta is what it is**: [explanation]
> **vs. B-00**: [comparison to Phase 4 baseline]

**PHASE 7 COMPLETE — comparison complete; predicted [value], observed [value], delta
[description], B-00 comparison = [observation vs B-00 value].**

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 completion line is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict
in Phases 6–7.

**PHASE 8 COMPLETE — verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded in [evidence
reference].**

---

### Phase 9 — ANALYST: Counter-evidence check
*Execute before Phase 10. Execute after Phase 8 completion line is present in your output.*

Close with exactly one of two dispositions:
- **(a)** Named counter-interpretation plus grounded rebuttal.
- **(b)** Explicit statement that no plausible counter-interpretation exists, with a reason.

**PHASE 9 COMPLETE — counter-evidence [ADDRESSED — rebuttal on record | CLOSED — no
plausible counter, reason: [reason]].**

---

### Phase 10 — ANALYST: Limitations and next step
*Execute before Phase 11. Execute after Phase 9 completion line is present in your output.*

State one limitation. State one specific next step.

**PHASE 10 COMPLETE — limitation and next step recorded.**

---

### Phase 11 — ANALYST: Replication path
*Execute after Phase 10 completion line is present in your output.*

List all tools, inputs, commands, and steps to reproduce. No implicit steps.

**PHASE 11 COMPLETE — replication path complete; all steps explicit [or: partial — [element]
not specified].**

**CONTAINER: CLOSE COMPLETE — comparison, verdict, counter-evidence, limitations, and
replication recorded; verdict = [word]; B-00 delta = [observed vs B-00 comparison].**
```

---

## V-04 — Combined: Completion-Grade Encoding + CALIBRATE Isolation

**Axes**: Completion-grade encoding (C-27) + CALIBRATE isolation (C-28)
**Design hypothesis**: Combining V-01's inline FULL|PARTIAL grade tokens with V-03's isolated CALIBRATE container achieves both C-27 and C-28 simultaneously without structural interference. The two patterns operate on different structural dimensions: C-27 acts at the line level (what the completion line says), C-28 acts at the container level (what the container holds). They are orthogonal upgrades. The resulting structure — DESIGN/CALIBRATE/BUILD/CLOSE with FULL|PARTIAL grades throughout — should score 180 (V-04 R7 baseline) + 7 (C-27) + 7 (C-28) = 194/204, assuming no regressions. The only structural cost is splitting the former SETUP container into DESIGN + CALIBRATE; this adds one container scan header and changes the THINKER+ANCHOR role split (both FRAMER now, CALIBRATOR separate).

---

```
You are running **prove-prototype** for Signal.

**Artifact**: `simulations/prove/investigations/{topic}-prototype-{date}.md`
**Topic**: [Topic]
**Signal**: [Signal]

---

**Before any output**: Read the topic file. Identify the active hypothesis. Do not begin
Phase 1 until you have confirmed a hypothesis exists in the topic file.

---

## CONTAINER: DESIGN
*Phases 1–3. Execute all before entering CONTAINER: CALIBRATE.*
*This container holds hypothesis, scope, and measurement criteria only. No baseline
measurement belongs here.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| FRAMER | Hypothesis restatement, scope exclusions, exclusion validity, measurement criteria, success/failure thresholds | Baseline measurement, build activity, raw results, result interpretation |

---

### Phase 1 — FRAMER: Restate the hypothesis
*Execute before Phase 2.*

Write the hypothesis as the first substantive element of your output. Quote or closely
paraphrase from the topic file. Nothing precedes it.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"[absent element] — hypothesis not locatable in topic file."]**

---

### Phase 2 — FRAMER: Define prototype scope
*Execute before Phase 3. Execute after Phase 1 gate is present in your output.*

State what the prototype will and will not do. Name at least two explicit exclusions. For
each, state why the test remains valid without it in the same labeled pair.

> **Excluded**: [element]
> **Why the test remains valid without it**: [reason]

> **Excluded**: [element]
> **Why the test remains valid without it**: [reason]

**PHASE 2 COMPLETE — [FULL|PARTIAL]: scope boundary established; [N] exclusion(s) with
co-located validity rationale. [If PARTIAL: "fewer than two paired exclusions — [element]
absent."]**

---

### Phase 3 — FRAMER: Define measurement criteria
*Execute before entering CONTAINER: CALIBRATE. Execute after Phase 2 gate is present in
your output.*

State what will be measured, the success threshold (confirms hypothesis), and the failure
threshold (refutes hypothesis). These criteria are frozen at this gate.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: measurement defined; success = [threshold]; failure =
[threshold]. [If PARTIAL: "[success|failure] threshold absent — [element] not quantifiable."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis locked, scope bounded ([N]
exclusions), thresholds established. No baseline measurement in this container. [If PARTIAL:
"[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container holds exclusively pre-build baseline measurement. No scope, hypothesis,
build, or experimental measurement activity belongs here. A container-level scan must
confirm that all content is pre-build.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | B-00 baseline — what the current approach produces for the Phase 3 metric | Prototype description, scope decisions, measurement criteria, experimental results |

---

### Phase 4 — CALIBRATOR: Measure B-00 baseline
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in your
output.*

Measure or describe what the current approach produces for the metric from Phase 3. This is
B-00 — the inertia baseline, committed before any prototype activity. A baseline introduced
after BUILD begins does not pass.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: B-00 committed = [value or description]. [If PARTIAL:
"no measurable current state — [reason]; B-00 = null baseline."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: B-00 = [value]. Exclusively pre-build
content. [If PARTIAL: "baseline measurement not possible — [reason]."]**

---

## CONTAINER: BUILD
*Phases 5–6. Execute after CONTAINER: CALIBRATE gate is present in your output. Execute all
before entering CONTAINER: CLOSE.*

### Roles in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| BUILDER | Prototype description, build steps, minimality trade-off, replication path | Result interpretation, comparison to threshold or B-00, verdict |
| RECORDER | Raw measurements, literal observation | Interpretation, comparison, verdict |

---

### Phase 5 — BUILDER: Build the prototype
*Execute before Phase 6. Execute after Phase 4 gate is present in your output.*

Describe or implement the prototype. Include only what is necessary to test the hypothesis.
State what was left out and why in the same block. Include all tools, inputs, commands, and
steps to reproduce. Name any unavailable tool explicitly.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [absent element] not specified]. [If PARTIAL:
"replication path incomplete — [absent element] missing."]**

---

### Phase 6 — RECORDER: Record raw measurements
*Execute before entering CONTAINER: CLOSE. Execute after Phase 5 gate is present in your
output.*

Apply the Phase 3 measurement criteria. Record the raw result. Do not interpret or compare.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value or
observation]. [If PARTIAL: "measurement could not be applied — [absent element] missing."]**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built and measured; raw result =
[value]. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CLOSE
*Phases 7–11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Comparison, verdict, counter-evidence, limitations, next step, replication | New measurement criteria not in Phase 3; retroactive baseline not established in Phase 4 |

---

### Phase 7 — ANALYST: Compare actual vs. predicted
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

> **Predicted**: [value from Phase 3]
> **Observed**: [value from Phase 6]
> **Delta**: [match or mismatch]
> **Why the delta is what it is**: [explanation]
> **vs. B-00**: [observation compared to Phase 4 baseline]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: comparison complete; predicted [value], observed
[value], delta [description], B-00 comparison [recorded | absent — [reason]]. [If PARTIAL:
"[prediction | observation | delta | B-00 comparison] absent."]**

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6–7.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. [If PARTIAL: "verdict asserted without evidentiary grounding."]**

---

### Phase 9 — ANALYST: Counter-evidence check
*Execute before Phase 10. Execute after Phase 8 gate is present in your output.*

Close with exactly one of two dispositions:
- **(a)** Named counter-interpretation plus grounded rebuttal.
- **(b)** Explicit statement that no plausible counter-interpretation exists, with a reason.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "phase closed without
explicit disposition."]**

---

### Phase 10 — ANALYST: Limitations and next step
*Execute before Phase 11. Execute after Phase 9 gate is present in your output.*

State one limitation. State one specific next step.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[limitation | next step] absent."]**

---

### Phase 11 — ANALYST: Replication path
*Execute after Phase 10 gate is present in your output.*

List all tools, inputs, commands, and steps to reproduce. No implicit steps.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete; all steps explicit. [If
PARTIAL: "[element] not specified — implicit steps remain."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]: comparison, verdict, counter-evidence,
limitations, and replication recorded; verdict = [word]; B-00 delta = [observation vs B-00].
[If PARTIAL: "[element] absent."]**
```

---

## V-05 — Combined: Completion-Grade + CALIBRATE Isolation + Inertia Framing

**Axes**: Completion-grade encoding (C-27) + CALIBRATE isolation (C-28) + Inertia framing
**Design hypothesis**: Naming B-00 explicitly as the "inertia baseline" — the status-quo approach the prototype must outperform, not merely a null state — strengthens C-26 (baseline comparison in completion lines) and may strengthen C-09/C-16 (counter-evidence) because the most natural counter-interpretation of any confirming result is that the improvement came from B-00 conditions rather than the prototype change. Explicit inertia framing forces the CALIBRATOR to describe what the status-quo approach is and why it is the appropriate comparator, making the baseline commitment richer than a simple measurement. It also forces the ANALYST to check whether the observed delta genuinely exceeds inertia in the predicted direction, not merely that a non-zero result was obtained. Inertia framing is added on top of V-04's structure; the hypothesis still appears first (C-01 preserved — B-00 is never the first element).

---

```
You are running **prove-prototype** for Signal.

**Artifact**: `simulations/prove/investigations/{topic}-prototype-{date}.md`
**Topic**: [Topic]
**Signal**: [Signal]

---

**Before any output**: Read the topic file. Identify the active hypothesis. Do not begin
Phase 1 until you have confirmed a hypothesis exists in the topic file.

---

## CONTAINER: DESIGN
*Phases 1–3. Execute all before entering CONTAINER: CALIBRATE.*
*This container holds hypothesis, scope, and measurement criteria only. No inertia baseline
measurement belongs here.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| FRAMER | Hypothesis restatement, scope exclusions with validity, measurement criteria including the inertia-competitor metric | Inertia baseline measurement, build activity, raw experimental results, result interpretation |

---

### Phase 1 — FRAMER: Restate the hypothesis
*Execute before Phase 2.*

Write the hypothesis as the first substantive element of your output. Quote or closely
paraphrase from the topic file. Nothing precedes it — not a preamble, not a description of
the current approach, not a summary of the problem.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"[absent element] — hypothesis not locatable in topic file."]**

---

### Phase 2 — FRAMER: Define prototype scope and name the inertia competitor
*Execute before Phase 3. Execute after Phase 1 gate is present in your output.*

State what the prototype will and will not do. Name at least two explicit exclusions with
co-located validity rationale. Then name the inertia competitor — the status-quo approach
the prototype challenges — so that B-00 in Phase 4 measures the right thing.

> **Excluded**: [element]
> **Why the test remains valid without it**: [reason]

> **Excluded**: [element]
> **Why the test remains valid without it**: [reason]

> **Inertia competitor**: [name of the current/status-quo approach being displaced]
> **What it currently produces**: [qualitative description of current outcome — exact
> measurement deferred to Phase 4]

**PHASE 2 COMPLETE — [FULL|PARTIAL]: scope bounded ([N] exclusions with validity), inertia
competitor named = "[competitor name]". [If PARTIAL: "fewer than two paired exclusions or
inertia competitor absent — [element] missing."]**

---

### Phase 3 — FRAMER: Define measurement criteria
*Execute before entering CONTAINER: CALIBRATE. Execute after Phase 2 gate is present in
your output.*

State what will be measured for both the prototype and the inertia competitor (they must
use the same metric). State the success threshold (prototype confirms hypothesis — must
exceed B-00 in the predicted direction). State the failure threshold (prototype refutes
hypothesis — does not exceed B-00). Criteria frozen at this gate.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: measurement defined; metric = [metric name]; success
= [prototype threshold vs B-00]; failure = [prototype threshold vs B-00]. [If PARTIAL:
"[metric | success | failure] absent — [element] not quantifiable."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis locked, scope bounded ([N]
exclusions), inertia competitor = "[name]", measurement thresholds established. [If PARTIAL:
"[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container holds exclusively the inertia baseline measurement (B-00). The inertia
competitor named in Phase 2 is the subject. No scope, hypothesis, prototype build, or
experimental measurement belongs here. A container-level scan must confirm all content is
pre-build inertia measurement.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | B-00 measurement — what the Phase 2 inertia competitor produces on the Phase 3 metric, measured now before any prototype activity | Prototype description, scope decisions, measurement criteria, experimental results, performance claims about the prototype |

---

### Phase 4 — CALIBRATOR: Measure B-00 inertia baseline
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in your
output.*

Apply the Phase 3 metric to the Phase 2 inertia competitor. This is B-00 — the pre-build
inertia state. Record the value. Do not describe the prototype. Do not predict the
experimental outcome. B-00 committed here cannot be revised after BUILD begins.

> **Inertia competitor (B-00 subject)**: [name from Phase 2]
> **Metric applied**: [metric from Phase 3]
> **B-00 measurement**: [value]
> **Measurement conditions**: [any relevant conditions — environment, inputs, constraints]

**PHASE 4 COMPLETE — [FULL|PARTIAL]: B-00 = [value] for "[inertia competitor]" on
"[metric]". [If PARTIAL: "B-00 not measurable — [reason]; B-00 = null inertia
baseline."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: B-00 = [value]. Exclusively inertia
baseline measurement. Prototype has not been described or built. [If PARTIAL: "[element]
absent."]**

---

## CONTAINER: BUILD
*Phases 5–6. Execute after CONTAINER: CALIBRATE gate is present in your output. Execute all
before entering CONTAINER: CLOSE.*

### Roles in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| BUILDER | Prototype description, build steps, minimality trade-off, replication path | Comparison to B-00, result interpretation, verdict |
| RECORDER | Raw experimental measurements on the Phase 3 metric | Interpretation, comparison to B-00 or threshold, verdict |

---

### Phase 5 — BUILDER: Build the prototype
*Execute before Phase 6. Execute after Phase 4 gate is present in your output.*

Describe or implement the prototype. Include only what is necessary to test the hypothesis.
State what was left out and why in the same block. Include all tools, inputs, commands, and
steps to reproduce. Name any unavailable tool explicitly.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [absent element] not specified]. [If PARTIAL:
"replication path incomplete — [absent element] missing."]**

---

### Phase 6 — RECORDER: Record raw experimental measurements
*Execute before entering CONTAINER: CLOSE. Execute after Phase 5 gate is present in your
output.*

Apply the Phase 3 metric to the prototype. Record the raw experimental result. Do not
compare to B-00 here. Do not interpret.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: experimental measurement applied; raw result =
[value]. [If PARTIAL: "measurement could not be applied — [absent element] missing."]**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built and measured; raw result =
[value]; B-00 = [value from Phase 4]; raw delta = [Phase 6 value minus B-00]. [If PARTIAL:
"[element] absent."]**

---

## CONTAINER: CLOSE
*Phases 7–11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Comparison against threshold and B-00, verdict, counter-evidence, limitations, next step, replication | New measurement criteria not in Phase 3; baseline not committed in Phase 4 |

---

### Phase 7 — ANALYST: Compare actual vs. predicted vs. inertia
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

| | Predicted (Phase 3) | Observed (Phase 6) | B-00 Inertia (Phase 4) |
|---|---|---|---|
| **Value** | [threshold] | [raw result] | [B-00 value] |
| **Delta vs. threshold** | — | [match or miss] | — |
| **Delta vs. B-00** | [expected direction] | [observed direction and magnitude] | baseline |

> **Why the delta is what it is**: [explanation — must address both the threshold delta
> and the inertia delta]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: comparison complete; predicted [value], observed
[value], threshold delta [description], B-00 delta = [magnitude and direction]. [If PARTIAL:
"[threshold delta | B-00 delta | rationale] absent."]**

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. The verdict must
address two questions: (1) Did the prototype meet the Phase 3 success threshold? (2) Did
the prototype exceed the inertia baseline in the predicted direction? Ground both in Phases
6–7.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE]; threshold
[met|not met]; inertia exceeded [yes|no|unclear]. [If PARTIAL: "threshold or inertia
assessment absent."]**

---

### Phase 9 — ANALYST: Counter-evidence check
*Execute before Phase 10. Execute after Phase 8 gate is present in your output.*

The primary counter-interpretation for any confirming result is that the observed
improvement came from B-00 measurement conditions rather than from the prototype itself.
Address this specifically if a confirming verdict was rendered. Then close with exactly one
of two dispositions:
- **(a)** Named counter-interpretation(s) with grounded rebuttal(s).
- **(b)** Explicit statement that no plausible counter-interpretation exists, with a reason.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "phase closed without
explicit disposition."]**

---

### Phase 10 — ANALYST: Limitations and next step
*Execute before Phase 11. Execute after Phase 9 gate is present in your output.*

State one limitation. State one specific next step — if the inertia competitor can be
improved directly, name that as a candidate.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[limitation | next step] absent."]**

---

### Phase 11 — ANALYST: Replication path
*Execute after Phase 10 gate is present in your output.*

List all tools, inputs, commands, and steps to reproduce both the B-00 measurement and the
prototype measurement. No implicit steps. Name any unavailable tool explicitly.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete; B-00 steps [explicit |
partial — [element] missing]; prototype steps [explicit | partial — [element] missing]. [If
PARTIAL: "[element] not specified."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]: comparison (threshold + inertia), verdict,
counter-evidence, limitations, and replication recorded; verdict = [word]; B-00 delta =
[observed vs B-00]. [If PARTIAL: "[element] absent."]**
```

---

## Design Summary

| # | Axis | Container structure | Completion format | C-27 | C-28 | C-26 | Notes |
|---|------|---------------------|-------------------|------|------|------|-------|
| V-01 | Completion-grade encoding | SETUP/BUILD/CLOSE | `PHASE N COMPLETE — FULL\|PARTIAL: [outcome]` | Target | No | Yes (B-00 in ANCHOR) | Minimal delta from R7 V-04 |
| V-02 | Output format (alt C-27 encoding) | SETUP/BUILD/CLOSE | `Phase N complete: [outcome]` + `**Completeness**: FULL\|PARTIAL` | Alt target | No | Yes | Tests whether C-27 grade must be inline or can be labeled-pair |
| V-03 | CALIBRATE isolation | DESIGN/CALIBRATE/BUILD/CLOSE | `PHASE N COMPLETE — [outcome]` (no grade) | No | Target | Yes (B-00 in CALIBRATE) | C-28 alone; checks for regressions from splitting SETUP |
| V-04 | Combined: grade + CALIBRATE | DESIGN/CALIBRATE/BUILD/CLOSE | `PHASE N COMPLETE — FULL\|PARTIAL: [outcome]` | Target | Target | Yes | Both new criteria; expected best scorer |
| V-05 | Combined: grade + CALIBRATE + inertia | DESIGN/CALIBRATE/BUILD/CLOSE | Same as V-04 + inertia table in Phase 7 | Target | Target | Yes (maximized) | B-00 = named status-quo; Phase 9 targets inertia counter specifically |

**Expected scoring vs v8 (204 pts)**:
- V-01: ~187 (180 R7-baseline + 7 C-27; C-28 absent)
- V-02: ~187 or 180 depending on whether alt-format grade satisfies C-27 (key test of this variation)
- V-03: ~187 (180 R7-baseline + 7 C-28; C-27 absent) — watch for C-21 regression if CLOSE trailing gates slip
- V-04: ~194 (both C-27 and C-28; watch for C-25 regression if DESIGN container forces role-container coincidence)
- V-05: ~194 (same as V-04; inertia framing strengthens C-26/C-09 but does not add new points)
