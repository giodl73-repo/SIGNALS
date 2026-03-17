# Quest Variate — prove-prototype Round 9 (v9 rubric, 218 pts)

**Date**: 2026-03-15
**Rubric version**: v9 (adds C-29 and C-30; sharpens C-27)
**Round 8 winner**: V-05 (DESIGN/CALIBRATE/BUILD/CLOSE + inline FULL|PARTIAL grades +
inertia framing + three-column table in Phase 7)

**New criteria this round**:
- **C-29**: CALIBRATE container must include explicit language framing B-00 as the
  status-quo alternative the prototype must outperform — not merely a calibration number.
  Requires C-28. Seeds the null counter-interpretation before any build activity.
- **C-30**: Three-column table (Predicted | Observed | B-00) in results section. Prose
  restatement of the same three values does not pass. Extends C-26.

**Variation axes**:
- V-01 (single): Inertia framing — explicit "must outperform" statement inside CALIBRATE
- V-02 (single): Table format — clean three-column table with delta rationale as adjacent labeled block
- V-03 (single): Role sequence — CALIBRATOR owns inertia competitor naming, not FRAMER
- V-04 (combined): C-29 explicit framing + C-30 clean table
- V-05 (combined): All three + phrasing register shift ("status-quo competitor" throughout + null hypothesis seeded in Phase 9)

---

## V-01 — Single Axis: Inertia Framing (C-29 Explicit Outperform Language)

**Axis**: Inertia framing — explicit "must outperform" statement inside CALIBRATE container
**Design hypothesis**: R8 V-05 names the inertia competitor in Phase 2 (DESIGN) and imports
that name into CALIBRATE. C-29 requires that the CALIBRATE container itself include explicit
framing of B-00 as "the status-quo alternative the prototype must outperform." V-05 names the
competitor in CALIBRATE but never says "must outperform" — it says "apply the metric to the
competitor." Adding one sentence to CALIBRATE's header and one sentence to Phase 4's
instruction that explicitly states "this is the alternative the prototype must exceed" satisfies
C-29 without structural change. DESIGN no longer needs to name the inertia competitor;
CALIBRATOR holds both the naming and the outperform framing. Inline FULL|PARTIAL grades
preserved from R8 V-01 design. Three-column table not introduced — single-axis test.

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
| FRAMER | Hypothesis restatement, scope exclusions with co-located validity rationale, measurement criteria and success/failure thresholds | Baseline measurement, build activity, raw results, result interpretation, inertia competitor identification |

---

### Phase 1 — FRAMER: Restate the hypothesis
*Execute before Phase 2.*

Write the hypothesis as the first substantive element of your output. Quote or closely
paraphrase from the topic file. Nothing precedes it — no preamble, no context summary,
no prototype description, no result.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"[absent element] — hypothesis not locatable in topic file."]**

---

### Phase 2 — FRAMER: Define prototype scope
*Execute before Phase 3. Execute after Phase 1 gate is present in your output.*

State what the prototype will and will not do. Name at least two explicit exclusions. For
each exclusion, state immediately why the test remains valid without it in the same labeled
pair.

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

State what will be measured. State the success threshold (the result that confirms the
hypothesis). State the failure threshold (the result that refutes it). These criteria are
frozen at this gate.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: measurement defined; success = [threshold]; failure =
[threshold]. [If PARTIAL: "[success|failure] threshold absent — [element] not
quantifiable."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis locked, scope bounded ([N]
exclusions with validity), measurement thresholds established. No baseline measurement in
this container. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container holds exclusively the status-quo baseline measurement (B-00). B-00 is the
current approach — the alternative the prototype must outperform to confirm the hypothesis.
No scope definition, hypothesis activity, build steps, or experimental measurement belongs
here. A container-level scan must confirm that all content is pre-build inertia measurement.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | Name of the status-quo approach being challenged; B-00 measurement of what that approach produces on the Phase 3 metric; explicit statement that the prototype must exceed B-00 to confirm the hypothesis | Prototype description, scope decisions, measurement criteria, experimental results, performance claims about the prototype |

---

### Phase 4 — CALIBRATOR: Measure B-00 and frame the inertia competitor
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in your
output.*

Name the status-quo approach that the prototype is challenging. This is the inertia
competitor — the current alternative that will remain in place if the prototype fails.
Apply the Phase 3 metric to it now. Record B-00. State explicitly that the prototype must
exceed B-00 in the predicted direction to confirm the hypothesis. This framing must appear
inside this container, before any build activity.

> **Status-quo approach (inertia competitor)**: [name of current method or baseline system]
> **B-00 measurement**: [value — what the status-quo approach produces on the Phase 3 metric]
> **What must happen to confirm the hypothesis**: The prototype must produce [predicted
>   direction] relative to B-00 = [value] on the Phase 3 metric. If the prototype matches
>   or underperforms B-00, the null counter-interpretation cannot be ruled out.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: B-00 = [value] for status-quo "[approach name]";
inertia competitor named; outperform threshold stated. [If PARTIAL: "B-00 not measurable —
[reason]; B-00 = null inertia baseline."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: B-00 = [value], status-quo competitor
named and framed as alternative to outperform. Exclusively pre-build content. [If PARTIAL:
"[element] absent."]**

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
State what was left out and why in the same block as the scope decision. Include all tools,
inputs, commands, and steps needed to reproduce the build. Name any tool not available in
this context explicitly.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [absent element] not specified]. [If PARTIAL:
"replication path incomplete — [absent element] missing."]**

---

### Phase 6 — RECORDER: Record raw measurements
*Execute before entering CONTAINER: CLOSE. Execute after Phase 5 gate is present in your
output.*

Apply the Phase 3 measurement criteria to the prototype. Record the raw result. Do not
interpret. Do not compare to B-00 or to the threshold. Do not reference the hypothesis
verdict.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value or
observation]. [If PARTIAL: "measurement could not be applied — [absent element] missing."]**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built and measured; raw result =
[value]; B-00 = [Phase 4 value]; raw delta = [Phase 6 minus B-00]. [If PARTIAL: "[element]
absent."]**

---

## CONTAINER: CLOSE
*Phases 7–11. Execute after CONTAINER: BUILD gate is present in your output. This container
absorbs all post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Comparison against threshold and B-00, verdict, counter-evidence, limitations, next step, replication | New measurement criteria not in Phase 3; baseline not committed in Phase 4 |

---

### Phase 7 — ANALYST: Compare actual vs. predicted vs. B-00
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

State the prediction (from Phase 3). State the observation (from Phase 6). State the delta
against threshold. State the delta against B-00. Immediately after all comparisons, explain
why the deltas are what they are — rationale must appear in the same labeled block.

> **Predicted**: [value or condition from Phase 3]
> **Observed**: [value or observation from Phase 6]
> **Delta vs. threshold**: [match or mismatch description]
> **Delta vs. B-00**: [how observation compares to Phase 4 inertia baseline]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: comparison complete; predicted [value], observed
[value], delta vs. threshold [description], B-00 comparison [recorded | absent — [reason]].
[If PARTIAL: "[prediction | observation | delta | B-00 comparison] absent."]**

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
limitations, and replication recorded; verdict = [word]; B-00 delta = [observed vs B-00];
C-27 compliance [FULL — all completion lines carry grade | PARTIAL — phase [N] grade
absent]. [If PARTIAL: "[element] absent."]**
```

---

## V-02 — Single Axis: Table Format (C-30 Clean Three-Column Table)

**Axis**: Output format — three-column table with delta rationale as an adjacent labeled block
**Design hypothesis**: R8 V-05's Phase 7 table merges value rows and delta rows in a single
table body, which is structurally complex and may produce partial-column fills. C-30 requires
that the three columns be unambiguously mapped to predicted / observed / baseline. A simpler
structure — a single-row value table (Predicted | Observed | B-00 Baseline) followed
immediately by a delta rationale labeled block — separates the structural completeness
guarantee (table enforces all three values) from the interpretive content (delta rationale).
The table cannot have a missing column; the rationale block satisfies C-17 co-location. Base
is R8 V-04 (CALIBRATE isolation + inline grades); C-29 framing is not introduced — single
axis. The hypothesis being tested: does the cleaner two-element format (table + rationale
block) score higher than V-05's merged table on C-30 satisfaction?

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
| FRAMER | Hypothesis restatement, scope exclusions with validity rationale, measurement criteria and thresholds | Baseline measurement, build activity, raw results, result interpretation |

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

State what the prototype will and will not do. Name at least two explicit exclusions with
co-located validity rationale.

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
threshold (refutes hypothesis). Frozen at this gate.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: measurement defined; success = [threshold]; failure =
[threshold]. [If PARTIAL: "[success|failure] threshold absent."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis locked, scope bounded ([N]
exclusions), thresholds established. No baseline measurement in this container. [If PARTIAL:
"[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container holds exclusively pre-build baseline measurement. No scope, hypothesis,
build, or experimental measurement belongs here.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | B-00 — what the current approach produces on the Phase 3 metric, committed before any build activity | Prototype description, scope decisions, measurement criteria, experimental results |

---

### Phase 4 — CALIBRATOR: Measure B-00 baseline
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in your
output.*

Measure or describe what the current approach produces for the Phase 3 metric. This is
B-00 — committed here, before any prototype activity. A baseline introduced after BUILD
begins does not pass.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: B-00 committed = [value or description]. [If PARTIAL:
"no measurable current state — [reason]; B-00 = null baseline."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: B-00 = [value]. Exclusively pre-build
content confirmed. [If PARTIAL: "baseline not measurable — [reason]."]**

---

## CONTAINER: BUILD
*Phases 5–6. Execute after CONTAINER: CALIBRATE gate is present in your output. Execute all
before entering CONTAINER: CLOSE.*

### Roles in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| BUILDER | Prototype description, build steps, minimality trade-off, replication path | Result interpretation, comparison to B-00 or threshold, verdict |
| RECORDER | Raw measurements, literal observation | Interpretation, comparison, verdict |

---

### Phase 5 — BUILDER: Build the prototype
*Execute before Phase 6. Execute after Phase 4 gate is present in your output.*

Describe or implement the prototype. Include only what is necessary to test the hypothesis.
State what was left out and why in the same block. Include all tools, inputs, commands, and
steps to reproduce.

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
| ANALYST | Comparison, verdict, counter-evidence, limitations, next step, replication | New measurement criteria; retroactive baseline |

---

### Phase 7 — ANALYST: Compare actual vs. predicted vs. B-00
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

Populate the three-column results table. All three columns must be filled — a missing column
is a visible structural gap. Then provide delta rationale in the immediately adjacent block.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | B-00 Baseline (Phase 4) |
|--------|--------------------|--------------------|------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value] |

> **Delta vs. threshold**: [match or mismatch]
> **Delta vs. B-00**: [observed relative to baseline — direction and magnitude]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], B-00 [value]); delta rationale co-located. [If PARTIAL: "[predicted |
observed | B-00] column absent — structural gap."]**

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6–7. State the reasoning in the same block.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. [If PARTIAL: "verdict asserted without evidentiary grounding."]**

---

### Phase 9 — ANALYST: Counter-evidence check
*Execute before Phase 10. Execute after Phase 8 gate is present in your output.*

Close with exactly one of two dispositions:
- **(a)** Name the counter-interpretation and rebut it with evidence-grounded reasoning.
- **(b)** State explicitly that no plausible counter-interpretation exists, with a reason.

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
PARTIAL: "[element] not specified."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]: comparison table populated, verdict rendered,
counter-evidence closed, limitations and replication recorded; verdict = [word]; B-00 delta
= [observed vs B-00]. [If PARTIAL: "[element] absent."]**
```

---

## V-03 — Single Axis: Role Sequence (CALIBRATOR Owns Inertia Naming)

**Axis**: Role sequence — CALIBRATOR role owns both inertia competitor identification and
B-00 measurement; FRAMER does not name a competitor
**Design hypothesis**: In R8 V-05, the inertia competitor is named by FRAMER in Phase 2
(DESIGN) and then referenced by CALIBRATOR in Phase 4 (CALIBRATE). C-29 requires the
CALIBRATE container to include "explicit language framing the baseline as the status-quo
alternative the prototype must outperform." If FRAMER names the competitor, the inertia
framing is split across two containers (DESIGN and CALIBRATE). If CALIBRATOR names AND
frames the competitor entirely within CALIBRATE, the framing is wholly contained inside the
container that C-29 requires it to be in. This structural change isolates all inertia-
competitor content to CALIBRATE, making C-29's container-scan auditability cleaner: a scan
of CALIBRATE alone reveals the competitor name, the B-00 measurement, and the outperform
framing. FRAMER loses the "Inertia competitor identification" write permission and CALIBRATOR
gains it. The hypothesis is: structural isolation of inertia framing to CALIBRATE is a
stronger C-29 signal than cross-container inertia framing, even if the framing sentences are
identical.

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
measurement or inertia competitor identification belongs here.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| FRAMER | Hypothesis restatement, scope exclusions with co-located validity rationale, measurement criteria and success/failure thresholds | Baseline measurement, inertia competitor identification, build activity, raw results, result interpretation |

---

### Phase 1 — FRAMER: Restate the hypothesis
*Execute before Phase 2.*

Write the hypothesis as the first substantive element of your output. Quote or closely
paraphrase from the topic file. Nothing precedes it.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"hypothesis not locatable in topic file."]**

---

### Phase 2 — FRAMER: Define prototype scope
*Execute before Phase 3. Execute after Phase 1 gate is present in your output.*

State what the prototype will and will not do. Name at least two explicit exclusions with
co-located validity rationale.

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

State what will be measured. State the success threshold (confirms hypothesis). State the
failure threshold (refutes hypothesis). Frozen at this gate.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: measurement defined; success = [threshold]; failure =
[threshold]. [If PARTIAL: "[success|failure] threshold absent."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis locked, scope bounded ([N]
exclusions), thresholds established. No inertia competitor named here — that belongs to
CALIBRATE. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container holds all inertia-competitor content: the identification of the status-quo
approach being challenged, the B-00 measurement of what that approach produces, and the
explicit framing of what the prototype must achieve relative to it. No scope definition,
hypothesis activity, build steps, or experimental measurement belongs here. A scan of this
container alone must be sufficient to answer: what is the current alternative, what does it
produce, and what must the prototype exceed?*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | Inertia competitor name and identification; B-00 measurement on Phase 3 metric; explicit statement that the prototype must exceed B-00 to confirm the hypothesis | Prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims about the prototype |

---

### Phase 4 — CALIBRATOR: Identify inertia competitor and measure B-00
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in your
output.*

Name the current approach that the prototype is challenging. This is the inertia competitor —
the status-quo alternative that will remain in use if the prototype does not outperform it.
Apply the Phase 3 metric to the inertia competitor and record B-00. State explicitly what
the prototype must produce relative to B-00 to confirm the hypothesis. All inertia-competitor
content belongs here; none belongs in DESIGN or BUILD.

> **Inertia competitor**: [name of current method, tool, or approach being displaced]
> **Why it is the status-quo**: [one sentence — why this is the existing alternative,
>   not a custom framing]
> **B-00 measurement**: [what the inertia competitor produces on the Phase 3 metric]
> **Required result to confirm hypothesis**: The prototype must produce [predicted outcome]
>   relative to B-00 = [value]. A result that matches B-00 or moves in the opposite direction
>   does not confirm the hypothesis; the null counter-interpretation would not be ruled out.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]"; B-00 = [value];
outperform requirement stated. [If PARTIAL: "[inertia competitor name | B-00 measurement |
outperform statement] absent."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor identified, B-00
committed, outperform threshold stated. Exclusively pre-build inertia content. [If PARTIAL:
"[element] absent."]**

---

## CONTAINER: BUILD
*Phases 5–6. Execute after CONTAINER: CALIBRATE gate is present in your output. Execute all
before entering CONTAINER: CLOSE.*

### Roles in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| BUILDER | Prototype description, build steps, minimality trade-off, replication path | Comparison to inertia competitor or B-00, result interpretation, verdict |
| RECORDER | Raw measurements on the Phase 3 metric | Interpretation, comparison, verdict |

---

### Phase 5 — BUILDER: Build the prototype
*Execute before Phase 6. Execute after Phase 4 gate is present in your output.*

Describe or implement the prototype. Include only what is necessary to test the hypothesis.
State what was left out and why in the same block. Include all tools, inputs, commands, and
steps to reproduce.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [absent element] not specified]. [If PARTIAL:
"replication path incomplete — [absent element] missing."]**

---

### Phase 6 — RECORDER: Record raw measurements
*Execute before entering CONTAINER: CLOSE. Execute after Phase 5 gate is present in your
output.*

Apply the Phase 3 metric to the prototype. Record the raw result only. Do not compare to
B-00 or the inertia competitor here.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value]. [If PARTIAL:
"measurement not applicable — [absent element]."]**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built and measured; raw result =
[value]; B-00 = [Phase 4 value] for "[inertia competitor]". [If PARTIAL: "[element]
absent."]**

---

## CONTAINER: CLOSE
*Phases 7–11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Comparison vs. threshold and inertia competitor, verdict, counter-evidence, limitations, next step, replication | New measurement criteria; inertia competitor not established in Phase 4 |

---

### Phase 7 — ANALYST: Compare actual vs. predicted vs. inertia baseline
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

> **Predicted**: [threshold from Phase 3]
> **Observed**: [raw result from Phase 6]
> **B-00 (inertia competitor)**: [value from Phase 4]
> **Delta vs. threshold**: [match or mismatch]
> **Delta vs. B-00**: [observed relative to inertia baseline — direction and magnitude]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: comparison complete; predicted [value], observed
[value], B-00 [value], both deltas stated with rationale. [If PARTIAL: "[element] absent."]**

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6–7 including the B-00 comparison.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. [If PARTIAL: "verdict without evidentiary grounding."]**

---

### Phase 9 — ANALYST: Counter-evidence check
*Execute before Phase 10. Execute after Phase 8 gate is present in your output.*

Close with exactly one of two dispositions:
- **(a)** Name the counter-interpretation and rebut it with evidence-grounded reasoning.
- **(b)** State explicitly that no plausible counter-interpretation exists, with a reason.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "no explicit disposition."]**

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

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete. [If PARTIAL: "[element]
not specified."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]: comparison, verdict, counter-evidence,
limitations, and replication recorded; verdict = [word]; B-00 delta = [observed vs B-00
for "[inertia competitor]"]. [If PARTIAL: "[element] absent."]**
```

---

## V-04 — Combined: C-29 Explicit Framing + C-30 Clean Three-Column Table

**Axes**: Inertia framing (C-29, V-01 approach) + Clean three-column table (C-30, V-02 approach)
**Design hypothesis**: V-01 satisfies C-29 by adding explicit "must outperform" language to
CALIBRATE while keeping Phase 2 (FRAMER) as the competitor-naming phase. V-02 satisfies C-30
by using a clean single-row three-column table in Phase 7 with an adjacent delta rationale
block. Combining both on top of R8 V-04's structure (CALIBRATE isolation + inline grades)
achieves C-27, C-28, C-29, and C-30. The design hypothesis: the two additions are structurally
independent (one acts in CALIBRATE, one acts in CLOSE/Phase 7) and combining them introduces
no regression. Expected score gain over R8 V-04 (194/204): C-29 adds its weight plus C-30
adds its weight. Both additions are confirmed to not break C-01 (hypothesis still first).

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
| FRAMER | Hypothesis restatement, scope exclusions with co-located validity rationale, measurement criteria and success/failure thresholds | Baseline measurement, build activity, raw results, result interpretation |

---

### Phase 1 — FRAMER: Restate the hypothesis
*Execute before Phase 2.*

Write the hypothesis as the first substantive element of your output. Quote or closely
paraphrase from the topic file. Nothing precedes it.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"hypothesis not locatable in topic file."]**

---

### Phase 2 — FRAMER: Define prototype scope
*Execute before Phase 3. Execute after Phase 1 gate is present in your output.*

State what the prototype will and will not do. Name at least two explicit exclusions with
co-located validity rationale.

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

State what will be measured. State the success threshold (confirms hypothesis). State the
failure threshold (refutes hypothesis). Frozen at this gate.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: measurement defined; success = [threshold]; failure =
[threshold]. [If PARTIAL: "[success|failure] threshold absent."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis locked, scope bounded ([N]
exclusions), thresholds established. No baseline measurement in this container. [If PARTIAL:
"[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container holds exclusively the status-quo baseline measurement (B-00). B-00 is not
a calibration reference — it is the current approach that the prototype must outperform to
confirm the hypothesis. No scope definition, hypothesis activity, build steps, or experimental
measurement belongs here. A container-level scan must confirm all content is pre-build
inertia measurement and outperform framing.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | Name of the status-quo approach; B-00 measurement on Phase 3 metric; explicit statement that the prototype must exceed B-00 to confirm the hypothesis | Prototype description, scope decisions, measurement criteria, experimental results |

---

### Phase 4 — CALIBRATOR: Measure B-00 and state the outperform requirement
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in your
output.*

Name the status-quo approach this prototype challenges. Apply the Phase 3 metric to it. Record
B-00. State explicitly that the prototype must exceed B-00 in the predicted direction to confirm
the hypothesis — this outperform requirement must appear inside this container, before any
build activity begins.

> **Status-quo approach**: [name of current method or system being displaced]
> **B-00 measurement**: [value — what the status-quo approach produces on the Phase 3 metric]
> **Outperform requirement**: The prototype must produce [predicted direction and magnitude]
>   relative to B-00 = [value] to confirm the hypothesis. A result that matches or falls
>   below B-00 does not confirm the hypothesis; the null counter-interpretation holds.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: B-00 = [value] for status-quo "[approach name]";
outperform requirement stated before any build activity. [If PARTIAL: "[B-00 value |
status-quo name | outperform statement] absent."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: B-00 = [value], status-quo competitor
named, outperform requirement stated. Exclusively pre-build inertia content. [If PARTIAL:
"[element] absent."]**

---

## CONTAINER: BUILD
*Phases 5–6. Execute after CONTAINER: CALIBRATE gate is present in your output. Execute all
before entering CONTAINER: CLOSE.*

### Roles in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| BUILDER | Prototype description, build steps, minimality trade-off, replication path | Comparison to B-00, result interpretation, verdict |
| RECORDER | Raw measurements on the Phase 3 metric | Interpretation, comparison, verdict |

---

### Phase 5 — BUILDER: Build the prototype
*Execute before Phase 6. Execute after Phase 4 gate is present in your output.*

Describe or implement the prototype. Include only what is necessary to test the hypothesis.
State what was left out and why in the same block. Include all tools, inputs, commands, and
steps to reproduce.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [absent element] not specified]. [If PARTIAL:
"replication path incomplete — [absent element] missing."]**

---

### Phase 6 — RECORDER: Record raw measurements
*Execute before entering CONTAINER: CLOSE. Execute after Phase 5 gate is present in your
output.*

Apply the Phase 3 metric to the prototype. Record the raw result. Do not interpret or compare.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value]. [If PARTIAL:
"measurement could not be applied — [absent element]."]**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built and measured; raw result =
[value]; B-00 = [Phase 4 value]. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CLOSE
*Phases 7–11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Three-column comparison, verdict, counter-evidence, limitations, next step, replication | New measurement criteria; retroactive baseline |

---

### Phase 7 — ANALYST: Three-column results table
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

Populate the three-column results table. All three columns must be filled with values drawn
from prior phases — a missing column is a visible structural gap. Then provide delta
rationale in the immediately adjacent labeled block.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | B-00 Baseline (Phase 4) |
|--------|--------------------|--------------------|------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value] |

> **Delta vs. threshold**: [match or mismatch — how observed compares to success/failure threshold]
> **Delta vs. B-00**: [observed relative to baseline — direction and magnitude]
> **Why the deltas are what they are**: [explanation addressing both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], B-00 [value]); delta rationale co-located. [If PARTIAL: "[predicted |
observed | B-00] column absent — structural gap in table."]**

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6–7 including the B-00 comparison.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. [If PARTIAL: "verdict without evidentiary grounding."]**

---

### Phase 9 — ANALYST: Counter-evidence check
*Execute before Phase 10. Execute after Phase 8 gate is present in your output.*

Close with exactly one of two dispositions:
- **(a)** Name the counter-interpretation and rebut it with evidence-grounded reasoning.
- **(b)** State explicitly that no plausible counter-interpretation exists, with a reason.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "no explicit disposition."]**

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

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete. [If PARTIAL: "[element]
not specified."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]: three-column table populated, verdict
rendered, counter-evidence closed, limitations and replication recorded; verdict = [word];
B-00 delta = [observed vs B-00 for "[status-quo approach]"]; C-27 compliance [FULL —
all lines carry grade | PARTIAL — phase [N] grade absent]. [If PARTIAL: "[element]
absent."]**
```

---

## V-05 — Combined: All Three + Phrasing Register (Status-Quo Competitor Throughout + Null Hypothesis Seeded in Phase 9)

**Axes**: Inertia framing depth (V-03 CALIBRATOR-owned naming) + Clean three-column table
(V-02 format) + Phrasing register shift ("status-quo competitor" language throughout) +
Phase 9 null hypothesis seeding (the inertia counter-interpretation is the named first
candidate for counter-evidence)
**Design hypothesis**: C-29 seeds the null counter-interpretation ("the prototype achieved
only what the status quo would have achieved") inside CALIBRATE before any build activity.
C-30 makes the three-column table the structural enforcer of all result comparisons. The
phrasing register shift — using "status-quo competitor" consistently, never just "baseline" —
reinforces that B-00 is an active competitor, not a passive reference. Phase 9's counter-
evidence check explicitly names the inertia null as the primary candidate, so the ANALYST
must directly confirm or rule out the inertia interpretation rather than constructing a
generic counter-interpretation from scratch. This is the strongest version of the four axes
and should represent the ceiling for this round.

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
*This container holds hypothesis, scope, and measurement criteria only. No status-quo
competitor identification or baseline measurement belongs here.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| FRAMER | Hypothesis restatement, scope exclusions with co-located validity rationale, measurement criteria and success/failure thresholds | Status-quo competitor identification, baseline measurement, build activity, raw results, result interpretation |

---

### Phase 1 — FRAMER: Restate the hypothesis
*Execute before Phase 2.*

Write the hypothesis as the first substantive element of your output. Quote or closely
paraphrase from the topic file. Nothing precedes it — no preamble, no context summary, no
prototype description, no result.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"hypothesis not locatable in topic file."]**

---

### Phase 2 — FRAMER: Define prototype scope
*Execute before Phase 3. Execute after Phase 1 gate is present in your output.*

State what the prototype will and will not do. Name at least two explicit exclusions with
co-located validity rationale.

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

State what will be measured. State the success threshold (confirms hypothesis). State the
failure threshold (refutes hypothesis). Frozen at this gate — BUILDER and RECORDER must not
modify them.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: measurement defined; success = [threshold]; failure =
[threshold]. [If PARTIAL: "[success|failure] threshold absent."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis locked, scope bounded ([N]
exclusions), thresholds established. No status-quo competitor identified here — that belongs
exclusively to CALIBRATE. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container holds all status-quo competitor content: the identification of the current
approach being challenged, its B-00 measurement on the Phase 3 metric, and the explicit
framing of the result the prototype must exceed. The prototype has not been described or
built anywhere at this point. A scan of this container alone must be sufficient to answer:
what is the status-quo competitor, what does it produce, and what must the prototype
outperform?*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | Status-quo competitor identification; B-00 measurement on Phase 3 metric; explicit outperform requirement; inertia framing for Phase 9 counter-evidence | Prototype description, scope exclusions, measurement criteria, experimental results, performance claims about the prototype |

---

### Phase 4 — CALIBRATOR: Identify status-quo competitor and measure B-00
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in your
output.*

Name the status-quo approach this prototype is challenging. This is the inertia competitor —
the current alternative that will remain in use if the prototype does not outperform it.
Apply the Phase 3 metric to it now. Record B-00. State the outperform requirement. State the
null counter-interpretation that Phase 9 will need to address: "the prototype produced a
result indistinguishable from what the status-quo competitor would have produced."

> **Status-quo competitor**: [name of current method, tool, or approach being displaced]
> **Why it is the current alternative**: [one sentence — what makes this the existing
>   approach, not a custom-framed comparator]
> **B-00 measurement**: [value — what the status-quo competitor produces on the Phase 3
>   metric, measured now before any prototype activity]
> **Outperform requirement**: The prototype must produce [predicted direction] relative to
>   B-00 = [value] on the Phase 3 metric. A result at or below B-00 does not confirm the
>   hypothesis.
> **Null counter-interpretation (seed for Phase 9)**: "The prototype achieved [metric result]
>   — consistent with what the status-quo competitor would have produced given the same
>   conditions." Phase 9 ANALYST must confirm or rule this out.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: status-quo competitor = "[name]"; B-00 = [value];
outperform requirement and null counter-interpretation stated before any build activity.
[If PARTIAL: "[competitor name | B-00 | outperform requirement | null counter] absent."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: status-quo competitor identified, B-00
committed, outperform requirement and inertia null stated. Exclusively pre-build content.
Prototype has not been described or built. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: BUILD
*Phases 5–6. Execute after CONTAINER: CALIBRATE gate is present in your output. Execute all
before entering CONTAINER: CLOSE.*

### Roles in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| BUILDER | Prototype description, build steps, minimality trade-off, replication path | Comparison to status-quo competitor or B-00, result interpretation, verdict |
| RECORDER | Raw measurements on the Phase 3 metric | Interpretation, comparison to B-00 or status-quo competitor, verdict |

---

### Phase 5 — BUILDER: Build the prototype
*Execute before Phase 6. Execute after Phase 4 gate is present in your output.*

Describe or implement the prototype. Include only what is necessary to test the hypothesis.
State what was left out and why in the same block. Include all tools, inputs, commands, and
steps to reproduce.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [absent element] not specified]. [If PARTIAL:
"replication path incomplete — [absent element] missing."]**

---

### Phase 6 — RECORDER: Record raw measurements
*Execute before entering CONTAINER: CLOSE. Execute after Phase 5 gate is present in your
output.*

Apply the Phase 3 metric to the prototype. Record the raw result. Do not compare to B-00 or
the status-quo competitor here. Do not interpret.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value]. [If PARTIAL:
"measurement not applicable — [absent element]."]**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built and measured; raw result =
[value]; B-00 (status-quo competitor) = [Phase 4 value]. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CLOSE
*Phases 7–11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Three-column results table, delta rationale, verdict, counter-evidence addressing the Phase 4 null counter-interpretation, limitations, next step, replication | New measurement criteria not in Phase 3; baseline not committed in Phase 4 |

---

### Phase 7 — ANALYST: Three-column results table
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

Populate the three-column results table with values drawn from Phases 3, 4, and 6. All three
columns must be filled — a missing column is a visible structural gap and the table does not
satisfy its purpose. Provide delta rationale immediately below.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | B-00 Status-Quo (Phase 4) |
|--------|--------------------|--------------------|--------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value] |

> **Delta vs. threshold**: [match or mismatch — does observed satisfy success or failure
>   threshold from Phase 3?]
> **Delta vs. B-00 status-quo**: [observed relative to status-quo competitor — direction,
>   magnitude, and whether it clears the outperform requirement stated in Phase 4]
> **Why the deltas are what they are**: [explanation addressing both comparisons — what
>   drove the result relative to both the threshold and the status-quo competitor]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], B-00 status-quo [value]); delta rationale co-located. [If PARTIAL:
"[predicted | observed | B-00] column absent — structural gap."]**

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6–7 including the B-00 status-quo comparison.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference including B-00 comparison]. [If PARTIAL: "verdict without evidentiary
grounding."]**

---

### Phase 9 — ANALYST: Counter-evidence check
*Execute before Phase 10. Execute after Phase 8 gate is present in your output.*

The primary counter-interpretation to assess is the inertia null seeded in Phase 4: "The
prototype achieved a result consistent with what the status-quo competitor would have produced
given the same conditions." Address this first. Then close with exactly one of two
dispositions — both are valid; silence is not:

- **(a)** Confirm a counter-interpretation exists (the inertia null or another) and rebut it
  with reasoning grounded in the Phase 7 evidence.
- **(b)** State explicitly that no plausible counter-interpretation exists, including why the
  inertia null does not apply to this result.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: inertia null assessed; counter-evidence [ADDRESSED —
rebuttal on record | CLOSED — inertia null ruled out, reason: [reason]]. [If PARTIAL:
"phase closed without explicit disposition on inertia null."]**

---

### Phase 10 — ANALYST: Limitations and next step
*Execute before Phase 11. Execute after Phase 9 gate is present in your output.*

State one limitation of this prototype or measurement. State one specific next step.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[limitation | next step] absent."]**

---

### Phase 11 — ANALYST: Replication path
*Execute after Phase 10 gate is present in your output.*

List all tools, inputs, commands, and steps needed to reproduce the prototype and measurement
from scratch. No implicit steps. Name any unavailable tool explicitly.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete; all steps explicit. [If
PARTIAL: "[element] not specified — implicit steps remain."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]: three-column table populated, verdict rendered,
inertia null assessed in counter-evidence, limitations and replication recorded; verdict =
[word]; B-00 delta = [observed vs B-00 for "[status-quo competitor]"]; C-27 compliance
[FULL — all completion lines carry grade | PARTIAL — phase [N] grade absent]. [If PARTIAL:
"[element] absent."]**
```
