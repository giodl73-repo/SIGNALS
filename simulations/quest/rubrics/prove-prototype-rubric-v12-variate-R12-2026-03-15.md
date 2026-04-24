# Quest Variate — prove-prototype Round 12 (v12 rubric, 260 pts)

**Date**: 2026-03-15
**Rubric version**: v12 (adds C-35 and C-36; ceiling 246 → 260)
**Round 11 winner**: V-04 and V-05 tied at 238 — C-33 (numbered CALIBRATE entry contract) +
C-34 (competitor-labeled baseline column) on R10 V-05 base.

**Why R11 V-04 does not yet reach the v12 ceiling**:

C-35 requires a document-level manifest appearing *before any container body executes* — not
just a CALIBRATE-level entry enumeration. R11 V-04's CONTAINER: CALIBRATE header enumerates
the three pre-build responsibilities (C-33), but no document-level manifest precedes the first
container. A reader opening the output has no structural surface to scan all four containers
before entering any one of them. C-35 is the document-level analogue of C-33: C-33 brackets
the CALIBRATE container; C-35 brackets the entire document.

C-36 requires the terminal CLOSE COMPLETE line to encode the *full experimental result chain*
spanning all containers — hypothesis verdict, inertia competitor name, measured delta, and
prototype conclusion — as a standalone audit record. R11 V-04's CONTAINER: CLOSE COMPLETE
line carries: verdict, B-00 delta, and table-population status. That satisfies C-22 (substantive
values from its own phase body) but does not satisfy C-36 (cross-container result chain: what
did DESIGN lock? what did CALIBRATE commit? what did BUILD measure? what did CLOSE conclude?).
A reader scanning only the terminal line cannot verify the full experimental arc under R11 V-04.

**R12 seed**: Add C-35 (document-level manifest) + C-36 (full-chain terminal line) to the
R11 V-04 base simultaneously. Expected: 238 + C-35 (+7) + C-36 (+7) = **252**.

**Variation axes**:
- V-01 (single): Lifecycle emphasis — add document manifest (C-35 target) to R11 V-04 base.
  No C-36. Tests: does a manifest with principal purpose + expected output fire C-35 alone?
- V-02 (single): Output format — enrich CLOSE COMPLETE with full cross-container result chain
  (C-36 target) on R11 V-04 base. No manifest. Tests: does C-36 fire independently of C-35?
- V-03 (gap probe): Lifecycle emphasis + inertia framing — enrich every CONTAINER COMPLETE
  line to carry a forward-reference to the next container's input requirement, creating a
  running audit chain. No manifest, no C-36. Tests: does a chain-coherent completion-line
  scheme probe a structural surface not yet scored (v13 gap signal)?
- V-04 (combined): C-35 + C-36 — the R12 seed. Both new criteria simultaneously on R11 V-04.
- V-05 (combined + gap): C-35 + C-36 + checkable manifest — manifest includes "Expected output"
  column; CLOSE COMPLETE cross-checks manifest items by container. Tests: does a verifiable
  manifest (not just descriptive) probe any unscored surface beyond C-35 + C-36?

---

## V-01 — Single Axis: Lifecycle Emphasis (Document-Level Container Manifest)

**Axis**: Lifecycle emphasis — document-level container manifest appears before any container
body and enumerates all four containers with their principal purpose and expected output
**Design hypothesis**: R11 V-04 opens directly with CONTAINER: DESIGN. No structural surface
precedes all four containers. Adding an Output Contract manifest — a four-row table naming
each container, its principal purpose, and its expected output — before the first container
header creates the document-level entry contract C-35 requires. C-36 is not introduced:
CONTAINER: CLOSE COMPLETE retains the R11 V-04 format (verdict + B-00 delta). Single-axis
test: does the manifest alone satisfy C-35 without requiring C-36?

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

## Output Contract

This output is organized into four lifecycle containers. The manifest below is the
document-level entry contract. Execute containers in the order listed. No container may
absorb work that belongs to another container.

| Container | Phases | Principal purpose | Expected output |
|-----------|--------|-------------------|-----------------|
| DESIGN | 1-3 | Lock the hypothesis, bound the prototype scope, and freeze measurement criteria — no competitor identification | Stated hypothesis, at least two named exclusions with co-located validity rationale, success and failure thresholds |
| CALIBRATE | 4 | Identify the inertia competitor, commit the B-00 baseline, and state the outperform threshold — all before any build activity | Named inertia competitor, committed B-00 value, explicit outperform threshold |
| BUILD | 5-6 | Build the smallest prototype that tests the hypothesis and record the raw measurement — no comparison or interpretation | Prototype description with minimality trade-off, raw result value on the Phase 3 metric |
| CLOSE | 7-11 | Compare actual vs. predicted vs. B-00, render the hypothesis verdict, close the counter-evidence check, record limitations and replication path | Three-column table with competitor-labeled baseline, verdict word, counter-evidence disposition, one limitation, one next step, full replication path |

A scan of this manifest plus the four CONTAINER: [NAME] COMPLETE lines must be sufficient
to reconstruct the full experimental lifecycle without reading any container body.

---

## CONTAINER: DESIGN
*Phases 1-3. Execute all before entering CONTAINER: CALIBRATE.*
*This container holds hypothesis, scope, and measurement criteria only. No baseline
measurement or inertia competitor identification belongs here. Inertia competitor
identification is prohibited in DESIGN — it belongs exclusively in CALIBRATE.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| FRAMER | Hypothesis restatement, scope exclusions with co-located validity rationale, measurement criteria and success/failure thresholds | Baseline measurement, inertia competitor identification [prohibited in DESIGN — belongs exclusively in CALIBRATE], build activity, raw results, result interpretation |

---

### Phase 1 — FRAMER: Restate the hypothesis
*Execute before Phase 2.*

Write the hypothesis as the first substantive element of your output. Quote or closely
paraphrase from the topic file. Nothing precedes it — no preamble, no context summary,
no prototype description, no result.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"hypothesis not locatable in topic file."]**

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

State what will be measured. State the success threshold (confirms hypothesis). State the
failure threshold (refutes hypothesis). Frozen at this gate.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: measurement defined; success = [threshold]; failure =
[threshold]. [If PARTIAL: "[success|failure] threshold absent."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis locked, scope bounded ([N]
exclusions with validity), measurement thresholds established. Inertia competitor
identification is prohibited in this container — that content belongs exclusively in
CALIBRATE. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container has exactly three pre-build responsibilities, discharged in this order:*
*1. Identify the inertia competitor — name the status-quo approach the prototype challenges.*
*2. Measure B-00 — record what the inertia competitor produces on the Phase 3 metric,*
*   committed before any build activity begins.*
*3. State the outperform threshold — what the prototype must produce relative to B-00 to*
*   confirm the hypothesis.*
*No scope definition, hypothesis activity, build steps, or experimental measurement belongs
here. A scan of the entry list above and the CONTAINER: CALIBRATE COMPLETE line below must
be sufficient to verify that all three responsibilities were discharged with their values.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | Inertia competitor name and identification; B-00 measurement on Phase 3 metric; explicit statement that prototype must exceed B-00 to confirm the hypothesis | Prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims about the prototype |

---

### Phase 4 — CALIBRATOR: Discharge all three CALIBRATE responsibilities in order
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in
your output.*

Discharge responsibilities 1, 2, and 3 in the order declared in the container header:

**(1) Identify the inertia competitor.** Name the current approach the prototype challenges.
State in one sentence why it is the status-quo alternative — the approach that remains in
use if the prototype fails.

**(2) Measure B-00.** Apply the Phase 3 metric to the inertia competitor. Record the result
as B-00. This commits the baseline before any prototype activity begins.

**(3) State the outperform threshold.** State explicitly what the prototype must produce
relative to B-00 to confirm the hypothesis. A result that matches or falls below B-00 does
not confirm the hypothesis; the null counter-interpretation would not be ruled out.

> **Inertia competitor**: [name of current method, tool, or approach being displaced]
> **Why it is the status-quo**: [one sentence]
> **B-00 measurement**: [what the inertia competitor produces on the Phase 3 metric]
> **Outperform threshold**: The prototype must produce [predicted outcome] relative to
>   B-00 = [value]. Matching or underperforming B-00 does not confirm the hypothesis.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: responsibility (1) inertia competitor = "[name]";
(2) B-00 = [value]; (3) outperform threshold stated. [If PARTIAL: "responsibility
(1|2|3) not discharged — [element] absent."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor identified =
"[name]", B-00 committed = [value], outperform threshold stated = prototype must
[direction and condition relative to B-00]. Exclusively pre-build inertia content.
[If PARTIAL: "responsibility ([1|2|3]) not discharged — scan-level audit incomplete."]**

---

## CONTAINER: BUILD
*Phases 5-6. Execute after CONTAINER: CALIBRATE gate is present in your output. Execute all
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
*Phases 7-11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Three-column comparison table with competitor-labeled baseline column, verdict, counter-evidence, limitations, next step, replication | New measurement criteria; inertia competitor framing not established in Phase 4 |

---

### Phase 7 — ANALYST: Three-column results table
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

Populate the three-column results table. The baseline column must be labeled with the
inertia competitor's name — not merely "B-00" or "Baseline (Phase 4)." The inertia
competitor must be identifiable by scanning the column header alone, without reading
the Phase 4 container body. All three columns must be populated with values from prior phases.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline (inertia competitor) |
|--------|--------------------|--------------------|-------------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value from Phase 4] |

> **Delta vs. threshold**: [match or mismatch — how observed compares to success/failure threshold]
> **Delta vs. B-00**: [observed relative to inertia baseline — direction and magnitude]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], baseline ([inertia competitor name]) [value]); delta rationale co-located.
[If PARTIAL: "[predicted | observed | baseline] column absent — structural gap in table."]**

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6-7 including the B-00 comparison.

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

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]: three-column table populated
(competitor-labeled baseline column present), verdict rendered, counter-evidence closed,
limitations and replication recorded; verdict = [word]; B-00 delta = [observed vs B-00
for "[inertia competitor]"]; table columns all populated [FULL | PARTIAL — [column] absent].
[If PARTIAL: "[element] absent."]**
```

---

## V-02 — Single Axis: Output Format (Enriched Terminal Completion Line)

**Axis**: Output format — the terminal CONTAINER: CLOSE COMPLETE line encodes the full
cross-container result chain as a standalone audit record, not just the closing phase outcome
**Design hypothesis**: R11 V-04's CONTAINER: CLOSE COMPLETE line carries verdict + B-00 delta
+ table-population status. A reader scanning only that line can reconstruct the closing
comparison but cannot verify what DESIGN locked, what CALIBRATE committed, or what BUILD
measured without reading the container bodies. Restructuring the CLOSE COMPLETE line to
encode all four containers' key results — hypothesis from DESIGN, competitor and B-00 from
CALIBRATE, raw result from BUILD, verdict from CLOSE — makes the terminal line a standalone
audit record satisfying C-36. No manifest is introduced: single-axis test.

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
*Phases 1-3. Execute all before entering CONTAINER: CALIBRATE.*
*This container holds hypothesis, scope, and measurement criteria only. No baseline
measurement or inertia competitor identification belongs here. Inertia competitor
identification is prohibited in DESIGN — it belongs exclusively in CALIBRATE.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| FRAMER | Hypothesis restatement, scope exclusions with co-located validity rationale, measurement criteria and success/failure thresholds | Baseline measurement, inertia competitor identification [prohibited in DESIGN — belongs exclusively in CALIBRATE], build activity, raw results, result interpretation |

---

### Phase 1 — FRAMER: Restate the hypothesis
*Execute before Phase 2.*

Write the hypothesis as the first substantive element of your output. Quote or closely
paraphrase from the topic file. Nothing precedes it — no preamble, no context summary,
no prototype description, no result.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"hypothesis not locatable in topic file."]**

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

State what will be measured. State the success threshold (confirms hypothesis). State the
failure threshold (refutes hypothesis). Frozen at this gate.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: measurement defined; success = [threshold]; failure =
[threshold]. [If PARTIAL: "[success|failure] threshold absent."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis locked, scope bounded ([N]
exclusions with validity), measurement thresholds established. Inertia competitor
identification is prohibited in this container — that content belongs exclusively in
CALIBRATE. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container has exactly three pre-build responsibilities, discharged in this order:*
*1. Identify the inertia competitor — name the status-quo approach the prototype challenges.*
*2. Measure B-00 — record what the inertia competitor produces on the Phase 3 metric,*
*   committed before any build activity begins.*
*3. State the outperform threshold — what the prototype must produce relative to B-00 to*
*   confirm the hypothesis.*
*No scope definition, hypothesis activity, build steps, or experimental measurement belongs
here. A scan of the entry list above and the CONTAINER: CALIBRATE COMPLETE line below must
be sufficient to verify that all three responsibilities were discharged with their values.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | Inertia competitor name and identification; B-00 measurement on Phase 3 metric; explicit statement that prototype must exceed B-00 to confirm the hypothesis | Prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims about the prototype |

---

### Phase 4 — CALIBRATOR: Discharge all three CALIBRATE responsibilities in order
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in
your output.*

Discharge responsibilities 1, 2, and 3 in the order declared in the container header:

**(1) Identify the inertia competitor.** Name the current approach the prototype challenges.
State in one sentence why it is the status-quo alternative — the approach that remains in
use if the prototype fails.

**(2) Measure B-00.** Apply the Phase 3 metric to the inertia competitor. Record the result
as B-00. This commits the baseline before any prototype activity begins.

**(3) State the outperform threshold.** State explicitly what the prototype must produce
relative to B-00 to confirm the hypothesis. A result that matches or falls below B-00 does
not confirm the hypothesis; the null counter-interpretation would not be ruled out.

> **Inertia competitor**: [name of current method, tool, or approach being displaced]
> **Why it is the status-quo**: [one sentence]
> **B-00 measurement**: [what the inertia competitor produces on the Phase 3 metric]
> **Outperform threshold**: The prototype must produce [predicted outcome] relative to
>   B-00 = [value]. Matching or underperforming B-00 does not confirm the hypothesis.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: responsibility (1) inertia competitor = "[name]";
(2) B-00 = [value]; (3) outperform threshold stated. [If PARTIAL: "responsibility
(1|2|3) not discharged — [element] absent."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor identified =
"[name]", B-00 committed = [value], outperform threshold stated = prototype must
[direction and condition relative to B-00]. Exclusively pre-build inertia content.
[If PARTIAL: "responsibility ([1|2|3]) not discharged — scan-level audit incomplete."]**

---

## CONTAINER: BUILD
*Phases 5-6. Execute after CONTAINER: CALIBRATE gate is present in your output. Execute all
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
*Phases 7-11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Three-column comparison table with competitor-labeled baseline column, verdict, counter-evidence, limitations, next step, replication | New measurement criteria; inertia competitor framing not established in Phase 4 |

---

### Phase 7 — ANALYST: Three-column results table
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

Populate the three-column results table. The baseline column must be labeled with the
inertia competitor's name — not merely "B-00" or "Baseline (Phase 4)." The inertia
competitor must be identifiable by scanning the column header alone. All three columns
must be populated with values from prior phases.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline (inertia competitor) |
|--------|--------------------|--------------------|-------------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value from Phase 4] |

> **Delta vs. threshold**: [match or mismatch — how observed compares to success/failure threshold]
> **Delta vs. B-00**: [observed relative to inertia baseline — direction and magnitude]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], baseline ([inertia competitor name]) [value]); delta rationale co-located.
[If PARTIAL: "[predicted | observed | baseline] column absent — structural gap in table."]**

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6-7 including the B-00 comparison.

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

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]:
[DESIGN] hypothesis = "[text from Phase 1]";
[CALIBRATE] inertia competitor = "[name]", B-00 = [value], outperform threshold = [direction/condition];
[BUILD] prototype result = [value], delta vs. B-00 = [direction and magnitude];
[CLOSE] verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], prototype conclusion = "[one sentence]",
counter-evidence = [ADDRESSED — "[interpretation]" rebutted | CLOSED — no plausible counter].
[If PARTIAL: "[absent element from which container] not encoded — audit chain incomplete."]**
```

---

## V-03 — Gap-Signal Probe: Chain-Coherent Completion Lines

**Axis**: Lifecycle emphasis — every CONTAINER COMPLETE line carries a forward-reference to
the next container's principal input requirement, creating an unbroken chain of acknowledged
handoffs between containers
**Design hypothesis**: R11 V-04 completion lines are self-contained: each reports what its
own container established but does not explicitly name what the next container depends on
receiving. Adding a forward-reference to each intermediate COMPLETE line — "DESIGN COMPLETE
carries: hypothesis text, thresholds; CALIBRATE receives these as input" — tests whether a
chain-coherent handoff scheme between containers creates a structural surface not yet scored.
This is not C-35 (document manifest) or C-36 (full-chain terminal line). It probes whether a
criterion for "completion lines acknowledge their downstream consumers" exists or is absent.
C-35 and C-36 are not introduced. This is a v13 gap-signal probe.

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
*Phases 1-3. Execute all before entering CONTAINER: CALIBRATE.*
*This container holds hypothesis, scope, and measurement criteria only. No baseline
measurement or inertia competitor identification belongs here. Inertia competitor
identification is prohibited in DESIGN — it belongs exclusively in CALIBRATE.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| FRAMER | Hypothesis restatement, scope exclusions with co-located validity rationale, measurement criteria and success/failure thresholds | Baseline measurement, inertia competitor identification [prohibited in DESIGN — belongs exclusively in CALIBRATE], build activity, raw results, result interpretation |

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

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis = "[text]", success threshold =
[threshold], failure threshold = [threshold]. CALIBRATE receives: hypothesis text and
measurement metric. [If PARTIAL: "[element] absent — CALIBRATE input incomplete."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container has exactly three pre-build responsibilities, discharged in this order:*
*1. Identify the inertia competitor — name the status-quo approach the prototype challenges.*
*2. Measure B-00 — record what the inertia competitor produces on the Phase 3 metric,*
*   committed before any build activity begins.*
*3. State the outperform threshold — what the prototype must produce relative to B-00 to*
*   confirm the hypothesis.*
*No scope definition, hypothesis activity, build steps, or experimental measurement belongs
here. A scan of the entry list above and the CONTAINER: CALIBRATE COMPLETE line below must
be sufficient to verify that all three responsibilities were discharged with their values.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | Inertia competitor name and identification; B-00 measurement on Phase 3 metric; explicit statement that prototype must exceed B-00 to confirm the hypothesis | Prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims about the prototype |

---

### Phase 4 — CALIBRATOR: Discharge all three CALIBRATE responsibilities in order
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in
your output.*

Discharge responsibilities 1, 2, and 3 in the order declared in the container header:

**(1) Identify the inertia competitor.** Name the current approach the prototype challenges.
State in one sentence why it is the status-quo alternative.

**(2) Measure B-00.** Apply the Phase 3 metric to the inertia competitor. Record as B-00.

**(3) State the outperform threshold.** State what the prototype must produce relative to
B-00. Matching or underperforming B-00 does not confirm the hypothesis.

> **Inertia competitor**: [name]
> **Why it is the status-quo**: [one sentence]
> **B-00 measurement**: [value]
> **Outperform threshold**: The prototype must produce [predicted outcome] relative to
>   B-00 = [value]. Matching or underperforming B-00 does not confirm the hypothesis.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: responsibility (1) inertia competitor = "[name]";
(2) B-00 = [value]; (3) outperform threshold stated. [If PARTIAL: "responsibility
(1|2|3) not discharged — [element] absent."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]",
B-00 = [value], outperform threshold = prototype must [direction and condition].
BUILD receives: B-00 value and Phase 3 metric for prototype measurement.
[If PARTIAL: "responsibility ([1|2|3]) not discharged — BUILD input incomplete."]**

---

## CONTAINER: BUILD
*Phases 5-6. Execute after CONTAINER: CALIBRATE gate is present in your output. Execute all
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

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built; raw result = [value];
B-00 from CALIBRATE = [value] for "[inertia competitor]".
CLOSE receives: raw result and B-00 for three-column comparison.
[If PARTIAL: "[element] absent — CLOSE input incomplete."]**

---

## CONTAINER: CLOSE
*Phases 7-11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Three-column comparison table with competitor-labeled baseline column, verdict, counter-evidence, limitations, next step, replication | New measurement criteria; inertia competitor framing not established in Phase 4 |

---

### Phase 7 — ANALYST: Three-column results table
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

Populate the three-column results table. The baseline column must be labeled with the
inertia competitor's name. All three columns must be populated with values from prior phases.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline (inertia competitor) |
|--------|--------------------|--------------------|-------------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value from Phase 4] |

> **Delta vs. threshold**: [match or mismatch]
> **Delta vs. B-00**: [direction and magnitude]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], baseline ([inertia competitor name]) [value]); delta rationale co-located.
[If PARTIAL: "[predicted | observed | baseline] column absent."]**

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6-7 including the B-00 comparison.

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

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]: three-column table populated
(competitor-labeled baseline present), verdict rendered, counter-evidence closed,
limitations and replication recorded; verdict = [word]; B-00 delta = [observed vs B-00
for "[inertia competitor]"]; table columns all populated [FULL | PARTIAL — [column] absent].
[If PARTIAL: "[element] absent."]**
```

---

## V-04 — Combined: C-35 + C-36 (R12 Seed)

**Axes**: C-35 document-level container manifest (V-01 axis) + C-36 enriched full-chain
terminal completion line (V-02 axis), both applied simultaneously to R11 V-04 base
**Design hypothesis**: C-35 and C-36 bracket the document at its outermost boundaries:
C-35 opens with a manifest announcing all containers and their expected outputs; C-36 closes
with a terminal line that confirms all containers discharged their results. Neither implies
the other. V-01 tests C-35 alone; V-02 tests C-36 alone. This variation tests whether both
can fire simultaneously on the same prompt without degrading C-33, C-34, C-32, C-31, or C-30.
Expected: 238 (R11 V-04) + C-35 (+7) + C-36 (+7) = **252**.

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

## Output Contract

This output is organized into four lifecycle containers. The manifest below is the
document-level entry contract — it appears before any container body executes. Execute
containers in the order listed. No container may absorb work that belongs to another.

| Container | Phases | Principal purpose | Expected output |
|-----------|--------|-------------------|-----------------|
| DESIGN | 1-3 | Lock the hypothesis, bound the prototype scope, and freeze measurement criteria — no competitor identification | Stated hypothesis, at least two named exclusions with co-located validity rationale, success and failure thresholds |
| CALIBRATE | 4 | Identify the inertia competitor, commit the B-00 baseline, and state the outperform threshold — all before any build activity | Named inertia competitor, committed B-00 value, explicit outperform threshold |
| BUILD | 5-6 | Build the smallest prototype that tests the hypothesis and record the raw measurement — no comparison or interpretation | Prototype description with minimality trade-off, raw result value on the Phase 3 metric |
| CLOSE | 7-11 | Compare actual vs. predicted vs. B-00, render the hypothesis verdict, close the counter-evidence check, record limitations and replication path | Three-column table with competitor-labeled baseline, verdict word, counter-evidence disposition, one limitation, one next step, full replication path |

The CONTAINER: CLOSE COMPLETE line at the end of this document is the terminal audit record
for the full experimental arc — it must encode results from all four containers, not only the
closing phase outcome.

---

## CONTAINER: DESIGN
*Phases 1-3. Execute all before entering CONTAINER: CALIBRATE.*
*This container holds hypothesis, scope, and measurement criteria only. No baseline
measurement or inertia competitor identification belongs here. Inertia competitor
identification is prohibited in DESIGN — it belongs exclusively in CALIBRATE.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| FRAMER | Hypothesis restatement, scope exclusions with co-located validity rationale, measurement criteria and success/failure thresholds | Baseline measurement, inertia competitor identification [prohibited in DESIGN — belongs exclusively in CALIBRATE], build activity, raw results, result interpretation |

---

### Phase 1 — FRAMER: Restate the hypothesis
*Execute before Phase 2.*

Write the hypothesis as the first substantive element of your output. Quote or closely
paraphrase from the topic file. Nothing precedes it — no preamble, no context summary,
no prototype description, no result.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"hypothesis not locatable in topic file."]**

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

State what will be measured. State the success threshold (confirms hypothesis). State the
failure threshold (refutes hypothesis). Frozen at this gate.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: measurement defined; success = [threshold]; failure =
[threshold]. [If PARTIAL: "[success|failure] threshold absent."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis locked, scope bounded ([N]
exclusions with validity), measurement thresholds established. Inertia competitor
identification is prohibited in this container — that content belongs exclusively in
CALIBRATE. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container has exactly three pre-build responsibilities, discharged in this order:*
*1. Identify the inertia competitor — name the status-quo approach the prototype challenges.*
*2. Measure B-00 — record what the inertia competitor produces on the Phase 3 metric,*
*   committed before any build activity begins.*
*3. State the outperform threshold — what the prototype must produce relative to B-00 to*
*   confirm the hypothesis.*
*No scope definition, hypothesis activity, build steps, or experimental measurement belongs
here. A scan of the entry list above and the CONTAINER: CALIBRATE COMPLETE line below must
be sufficient to verify that all three responsibilities were discharged with their values.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | Inertia competitor name and identification; B-00 measurement on Phase 3 metric; explicit statement that prototype must exceed B-00 to confirm the hypothesis | Prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims about the prototype |

---

### Phase 4 — CALIBRATOR: Discharge all three CALIBRATE responsibilities in order
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in
your output.*

Discharge responsibilities 1, 2, and 3 in the order declared in the container header:

**(1) Identify the inertia competitor.** Name the current approach the prototype challenges.
State in one sentence why it is the status-quo alternative — the approach that remains in
use if the prototype fails.

**(2) Measure B-00.** Apply the Phase 3 metric to the inertia competitor. Record the result
as B-00. This commits the baseline before any prototype activity begins.

**(3) State the outperform threshold.** State explicitly what the prototype must produce
relative to B-00 to confirm the hypothesis. A result that matches or falls below B-00 does
not confirm the hypothesis; the null counter-interpretation would not be ruled out.

> **Inertia competitor**: [name of current method, tool, or approach being displaced]
> **Why it is the status-quo**: [one sentence]
> **B-00 measurement**: [what the inertia competitor produces on the Phase 3 metric]
> **Outperform threshold**: The prototype must produce [predicted outcome] relative to
>   B-00 = [value]. Matching or underperforming B-00 does not confirm the hypothesis.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: responsibility (1) inertia competitor = "[name]";
(2) B-00 = [value]; (3) outperform threshold stated. [If PARTIAL: "responsibility
(1|2|3) not discharged — [element] absent."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor identified =
"[name]", B-00 committed = [value], outperform threshold stated = prototype must
[direction and condition relative to B-00]. Exclusively pre-build inertia content.
[If PARTIAL: "responsibility ([1|2|3]) not discharged — scan-level audit incomplete."]**

---

## CONTAINER: BUILD
*Phases 5-6. Execute after CONTAINER: CALIBRATE gate is present in your output. Execute all
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
*Phases 7-11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Three-column comparison table with competitor-labeled baseline column, verdict, counter-evidence, limitations, next step, replication | New measurement criteria; inertia competitor framing not established in Phase 4 |

---

### Phase 7 — ANALYST: Three-column results table
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

Populate the three-column results table. The baseline column must be labeled with the
inertia competitor's name — not merely "B-00" or "Baseline (Phase 4)." The inertia
competitor must be identifiable by scanning the column header alone, without reading
the Phase 4 container body. All three columns must be populated with values from prior phases.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline (inertia competitor) |
|--------|--------------------|--------------------|-------------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value from Phase 4] |

> **Delta vs. threshold**: [match or mismatch — how observed compares to success/failure threshold]
> **Delta vs. B-00**: [observed relative to inertia baseline — direction and magnitude]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], baseline ([inertia competitor name]) [value]); delta rationale co-located.
[If PARTIAL: "[predicted | observed | baseline] column absent — structural gap in table."]**

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6-7 including the B-00 comparison.

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

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]:
[DESIGN] hypothesis = "[text from Phase 1]";
[CALIBRATE] inertia competitor = "[name]", B-00 = [value], outperform threshold = [direction/condition];
[BUILD] prototype result = [value], delta vs. B-00 = [direction and magnitude];
[CLOSE] verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], prototype conclusion = "[one sentence]",
counter-evidence = [ADDRESSED — "[interpretation]" rebutted | CLOSED — no plausible counter].
[If PARTIAL: "[absent element from which container] not encoded — audit chain incomplete."]**
```

---

## V-05 — Combined + Gap Probe: Checkable Manifest with Terminal Verification

**Axes**: C-35 document manifest + C-36 enriched terminal line + gap probe: manifest
includes an "Expected output" column whose items are verifiable against each container's
COMPLETE line; the CLOSE COMPLETE cross-checks manifest promises against container deliveries
**Design hypothesis**: V-04 satisfies C-35 (manifest) and C-36 (full-chain terminal line)
independently. This variation makes the manifest *checkable*: each row's "Expected output"
item is paired with a note in the manifest that a reader can cross-reference against the
corresponding CONTAINER: [NAME] COMPLETE line. The CLOSE COMPLETE line additionally encodes
"manifest delivered: [FULL | PARTIAL — [container] fell short on [item]]" — pairing C-36's
cross-container result chain with an explicit manifest-verification statement. The gap probe
tests whether a criterion exists (or is missing) for "CLOSE COMPLETE cross-verifies the
document-level manifest" — a surface nested one level above C-36 itself (C-36 records results;
this probes whether recording manifest-conformance is a separate scorable act). Expected:
252 (V-04) + possible manifest-verification uplift — v13 gap signal candidate.

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

## Output Contract

This output is organized into four lifecycle containers. The manifest below is the
document-level entry contract — it appears before any container body executes. Each row's
"Expected output" column states what the corresponding CONTAINER: [NAME] COMPLETE line must
confirm. Execute containers in the order listed. No container may absorb work belonging to
another.

| Container | Phases | Principal purpose | Expected output (verifiable at COMPLETE line) |
|-----------|--------|-------------------|-----------------------------------------------|
| DESIGN | 1-3 | Lock the hypothesis, bound the prototype scope, and freeze measurement criteria — no competitor identification | Hypothesis text, count of validated exclusions, success threshold value, failure threshold value |
| CALIBRATE | 4 | Identify the inertia competitor, commit the B-00 baseline, and state the outperform threshold — all before any build activity | Inertia competitor name, B-00 numeric value, outperform threshold direction and condition |
| BUILD | 5-6 | Build the smallest prototype that tests the hypothesis and record the raw measurement — no comparison or interpretation | Prototype built (minimality trade-off on record), raw result numeric value on Phase 3 metric |
| CLOSE | 7-11 | Compare actual vs. predicted vs. B-00, render the hypothesis verdict, close the counter-evidence check, record limitations and replication path | Three-column table with competitor-labeled baseline populated, verdict word, counter-evidence disposition (ADDRESSED or CLOSED), limitation named, replication path complete |

The terminal CONTAINER: CLOSE COMPLETE line encodes two things: (1) the full experimental
result chain spanning all four containers, and (2) a manifest conformance record confirming
whether each container delivered its promised expected output.

---

## CONTAINER: DESIGN
*Phases 1-3. Execute all before entering CONTAINER: CALIBRATE.*
*This container holds hypothesis, scope, and measurement criteria only. No baseline
measurement or inertia competitor identification belongs here. Inertia competitor
identification is prohibited in DESIGN — it belongs exclusively in CALIBRATE.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| FRAMER | Hypothesis restatement, scope exclusions with co-located validity rationale, measurement criteria and success/failure thresholds | Baseline measurement, inertia competitor identification [prohibited in DESIGN — belongs exclusively in CALIBRATE], build activity, raw results, result interpretation |

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

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis = "[text]", scope = [N] validated
exclusions, success threshold = [threshold], failure threshold = [threshold]. Inertia
competitor identification is prohibited in this container — belongs exclusively in CALIBRATE.
[If PARTIAL: "[element] absent — manifest expected output not fully delivered."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container has exactly three pre-build responsibilities, discharged in this order:*
*1. Identify the inertia competitor — name the status-quo approach the prototype challenges.*
*2. Measure B-00 — record what the inertia competitor produces on the Phase 3 metric,*
*   committed before any build activity begins.*
*3. State the outperform threshold — what the prototype must produce relative to B-00 to*
*   confirm the hypothesis.*
*No scope definition, hypothesis activity, build steps, or experimental measurement belongs
here. A scan of the entry list above and the CONTAINER: CALIBRATE COMPLETE line below must
be sufficient to verify that all three responsibilities were discharged with their values.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | Inertia competitor name and identification; B-00 measurement on Phase 3 metric; explicit statement that prototype must exceed B-00 to confirm the hypothesis | Prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims about the prototype |

---

### Phase 4 — CALIBRATOR: Discharge all three CALIBRATE responsibilities in order
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in
your output.*

Discharge responsibilities 1, 2, and 3 in the order declared in the container header:

**(1) Identify the inertia competitor.** Name the current approach the prototype challenges.
State in one sentence why it is the status-quo alternative.

**(2) Measure B-00.** Apply the Phase 3 metric to the inertia competitor. Record as B-00.

**(3) State the outperform threshold.** State what the prototype must produce relative to
B-00. Matching or underperforming B-00 does not confirm the hypothesis.

> **Inertia competitor**: [name]
> **Why it is the status-quo**: [one sentence]
> **B-00 measurement**: [value]
> **Outperform threshold**: The prototype must produce [predicted outcome] relative to
>   B-00 = [value]. Matching or underperforming B-00 does not confirm the hypothesis.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: responsibility (1) inertia competitor = "[name]";
(2) B-00 = [value]; (3) outperform threshold stated. [If PARTIAL: "responsibility
(1|2|3) not discharged — [element] absent."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor identified =
"[name]", B-00 committed = [value], outperform threshold stated = prototype must
[direction and condition relative to B-00]. Exclusively pre-build inertia content.
[If PARTIAL: "responsibility ([1|2|3]) not discharged — manifest expected output not
fully delivered."]**

---

## CONTAINER: BUILD
*Phases 5-6. Execute after CONTAINER: CALIBRATE gate is present in your output. Execute all
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

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built; raw result = [value];
B-00 = [Phase 4 value] for "[inertia competitor]"; minimality trade-off [on record | absent].
[If PARTIAL: "[element] absent — manifest expected output not fully delivered."]**

---

## CONTAINER: CLOSE
*Phases 7-11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Three-column comparison table with competitor-labeled baseline column, verdict, counter-evidence, limitations, next step, replication | New measurement criteria; inertia competitor framing not established in Phase 4 |

---

### Phase 7 — ANALYST: Three-column results table
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

Populate the three-column results table. The baseline column must be labeled with the
inertia competitor's name. All three columns must be populated with values from prior phases.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline (inertia competitor) |
|--------|--------------------|--------------------|-------------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value from Phase 4] |

> **Delta vs. threshold**: [match or mismatch]
> **Delta vs. B-00**: [direction and magnitude]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], baseline ([inertia competitor name]) [value]); delta rationale co-located.
[If PARTIAL: "[predicted | observed | baseline] column absent."]**

---

### Phase 8 — ANALYST: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6-7 including the B-00 comparison.

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

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]:
[DESIGN] hypothesis = "[text]";
[CALIBRATE] inertia competitor = "[name]", B-00 = [value], outperform threshold = [direction/condition];
[BUILD] prototype result = [value], delta vs. B-00 = [direction and magnitude];
[CLOSE] verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], prototype conclusion = "[one sentence]",
counter-evidence = [ADDRESSED — "[interpretation]" rebutted | CLOSED — no plausible counter];
manifest conformance: DESIGN [FULL|PARTIAL], CALIBRATE [FULL|PARTIAL], BUILD [FULL|PARTIAL],
CLOSE [FULL|PARTIAL — [item] not delivered].
[If PARTIAL: "[absent element from which container] not encoded — audit chain or manifest
conformance incomplete."]**
```

---

## Predicted Score Summary

| Variation | Axis | C-35 | C-36 | Base | Expected score |
|-----------|------|------|------|------|----------------|
| V-01 | Lifecycle emphasis: document manifest | PASS | FAIL | R11 V-04 (238) | **245** |
| V-02 | Output format: enriched CLOSE COMPLETE | FAIL | PASS | R11 V-04 (238) | **245** |
| V-03 | Gap probe: chain-coherent handoff lines | FAIL | FAIL | R11 V-04 (238) | **238** (gap signal only) |
| V-04 | Combined C-35 + C-36 (R12 seed) | PASS | PASS | R11 V-04 (238) | **252** |
| V-05 | Combined C-35 + C-36 + checkable manifest | PASS | PASS | R11 V-04 (238) | **252** + possible gap |

**R12 ceiling target**: 252 / 260 (96.9%)
**Remaining 8 pts**: C-24 through C-28 carry-forward criteria — exact pass conditions not
fully specified in v12 rubric. V-05's manifest-conformance encoding in the CLOSE COMPLETE
line is the candidate for a v13 criterion if it creates a structural surface not yet scored.

```json
{"round": 12, "rubric_version": "v12", "ceiling": 260, "seed_variation": "V-04",
 "seed_expected_score": 252, "gap_probe": "V-03 (chain-coherent handoffs) and V-05 (manifest conformance at CLOSE)",
 "new_criteria_targeted": ["C-35 (document manifest)", "C-36 (full-chain terminal line)"],
 "base": "R11 V-04 (238 pts: C-33 + C-34 + R10 V-05)"}
```
