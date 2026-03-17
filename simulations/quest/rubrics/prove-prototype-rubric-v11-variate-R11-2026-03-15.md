# Quest Variate — prove-prototype Round 11 (v11 rubric, 246 pts)

**Date**: 2026-03-15
**Rubric version**: v11 (adds C-33 and C-34; ceiling 232 → 246)
**Round 10 winner**: V-05 (C-31 + C-32 + C-30; CALIBRATE COMPLETE carries triple with values;
three-column table in Phase 7; scores 231 on v11 rubric)

**Why R10 V-05 does not yet reach the v11 ceiling**:

C-33 requires the CALIBRATE container header to enumerate all three pre-build responsibilities
as a numbered ordered list before the body executes them. R10 V-05's CALIBRATE header is a
dense prose block: "This container holds all inertia-competitor content: the identification
of the status-quo approach being challenged, the B-00 measurement…" That prose describes what
the container holds, but does not enumerate the three responsibilities as a numbered entry
contract. A reader scanning only the container boundary (header + COMPLETE line) can read
the COMPLETE line's triple confirmation (C-32) but cannot read a matching entry declaration
at the header — the bracket is half-open. C-33 requires the entry side to be explicitly
enumerable, not only the exit side.

C-34 requires the baseline column in the three-column results table to be labeled with the
inertia competitor identity, not merely "B-00 Baseline (Phase 4)." R10 V-05's Phase 7 table
uses "B-00 Baseline (Phase 4)" as the column header. That label identifies a measurement and
its source phase but does not name the inertia competitor or frame the column as the
status-quo alternative being displaced. A reader scanning only the table header row cannot
determine who the competitor is without reading the container body. C-34 requires the column
label to make the competitor scannable at the table level.

**R11 seed**: Add C-33 (numbered entry contract in CALIBRATE header) + C-34 (competitor-named
column label) to the R10 V-05 base simultaneously. This is the only path to 246.

**Variation axes**:
- V-01 (single): Inertia framing axis — add C-33 numbered CALIBRATE header to R10 V-04 base.
  No C-34. Tests: does entry contract alone, without three-column table, satisfy C-33?
- V-02 (single): Output format axis — add explicit "Baseline (inertia competitor)" column
  label to R10 V-05 base (which has C-30). No C-33. Tests: does renaming the column satisfy
  C-34 standalone?
- V-03 (single): Lifecycle emphasis axis — add a document-level container manifest at the
  top and strengthen CONTAINER: CLOSE COMPLETE to carry all five phase values for full
  audit-by-scan at the container boundary level. No C-33 or C-34.
- V-04 (combined): C-33 + C-34 — the R11 seed. R10 V-05 base plus both new criteria.
- V-05 (combined): C-33 + C-34 + lifecycle manifest — ceiling attempt targeting 246.

---

## V-01 — Single Axis: C-33 Numbered CALIBRATE Entry Contract

**Axis**: Inertia framing — CALIBRATE container header enumerates all three pre-build
responsibilities as a numbered ordered entry contract
**Design hypothesis**: R10 V-04 satisfies C-32 (CALIBRATE COMPLETE with triple values) and
C-31 (FRAMER routing prohibition) but its CALIBRATE header is a prose block that describes
container contents without enumerating individual responsibilities. Adding a numbered entry
contract to the CALIBRATE header — "1. Identify inertia competitor; 2. Measure B-00;
3. State outperform threshold" — before the container body executes them closes the bracket
that C-32 leaves half-open. C-34 is not introduced: Phase 7 retains the labeled-pair format
without a three-column table. Single-axis test: does the numbered CALIBRATE header alone
satisfy C-33 on top of V-04's C-31 + C-32 base?

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
here. A scan of the entry list above and the CONTAINER: CALIBRATE COMPLETE line below
must be sufficient to verify all three responsibilities were discharged.*

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
[If PARTIAL: "responsibility ([1|2|3]) not discharged — [element] absent."]**

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
| ANALYST | Comparison vs. threshold and inertia competitor, verdict, counter-evidence, limitations, next step, replication | New measurement criteria; inertia competitor framing not established in Phase 4 |

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

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]: comparison, verdict, counter-evidence,
limitations, and replication recorded; verdict = [word]; B-00 delta = [observed vs B-00
for "[inertia competitor]"]. [If PARTIAL: "[element] absent."]**
```

---

## V-02 — Single Axis: C-34 Competitor-Labeled Baseline Column

**Axis**: Output format — the baseline column in the Phase 7 three-column results table
carries an explicit inertia competitor identity label, not merely "B-00 Baseline (Phase 4)"
**Design hypothesis**: R10 V-05 already produces a three-column table satisfying C-30. Its
baseline column is labeled "B-00 Baseline (Phase 4)" — which identifies a measurement and
its source phase but does not name the inertia competitor or frame the column as the
status-quo approach being displaced. C-34 requires the label to make the competitor
identifiable by scanning the column header alone, without reading the Phase 4 body.
Renaming the column to "Baseline (inertia competitor)" or "B-00 — [competitor name]"
creates a third structural surface for competitor identification independent of the CALIBRATE
body (C-29) and CALIBRATE COMPLETE line (C-32). C-33 is not introduced — single-axis test.

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

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis locked, scope bounded ([N]
exclusions with validity), measurement thresholds established. Inertia competitor
identification is prohibited in this container — that content belongs exclusively in
CALIBRATE. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container holds all inertia-competitor content: the identification of the status-quo
approach being challenged, the B-00 measurement of what that approach produces, and the
explicit framing of what the prototype must achieve relative to it. A scan of this container
alone must answer: what is the current alternative, what does it produce, and what must the
prototype exceed? No scope definition, hypothesis activity, build steps, or experimental
measurement belongs here.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | Inertia competitor name and identification; B-00 measurement on Phase 3 metric; explicit statement that prototype must exceed B-00 to confirm the hypothesis | Prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims about the prototype |

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
> **Why it is the status-quo**: [one sentence — why this is the existing alternative]
> **B-00 measurement**: [what the inertia competitor produces on the Phase 3 metric]
> **Required result to confirm hypothesis**: The prototype must produce [predicted outcome]
>   relative to B-00 = [value]. A result that matches B-00 or moves in the opposite direction
>   does not confirm the hypothesis; the null counter-interpretation would not be ruled out.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]"; B-00 = [value];
outperform requirement stated. [If PARTIAL: "[inertia competitor name | B-00 measurement |
outperform statement] absent."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor identified =
"[name]", B-00 committed = [value], outperform threshold stated = prototype must
[direction and condition relative to B-00]. Exclusively pre-build inertia content.
[If PARTIAL: "[absent element] not established — scan-level audit incomplete."]**

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
| ANALYST | Three-column comparison table, verdict, counter-evidence, limitations, next step, replication | New measurement criteria; inertia competitor not established in Phase 4 |

---

### Phase 7 — ANALYST: Three-column results table
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

Populate the three-column results table. The baseline column must be labeled with the
inertia competitor's name — not merely "B-00" or "Baseline." A column labeled only with
a measurement code cannot be verified as the competitor by scanning the table header alone.
All three columns must be populated with values drawn from prior phases.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline (inertia competitor) |
|--------|--------------------|--------------------|-------------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value from Phase 4] |

> **Delta vs. threshold**: [match or mismatch — how observed compares to success/failure threshold]
> **Delta vs. B-00**: [observed relative to inertia baseline — direction and magnitude]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], baseline (inertia competitor) [value]); delta rationale co-located.
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

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]: three-column table populated, verdict
rendered, counter-evidence closed, limitations and replication recorded; verdict = [word];
B-00 delta = [observed vs B-00 for "[inertia competitor]"]; table columns all populated
[FULL | PARTIAL — [column] absent]. [If PARTIAL: "[element] absent."]**
```

---

## V-03 — Single Axis: Lifecycle Emphasis (Document-Level Container Manifest)

**Axis**: Lifecycle emphasis — a document-level container manifest at the top declares all
four containers with their single-function descriptions before any container is read, creating
a structural contract visible at the document boundary level; CONTAINER: CLOSE COMPLETE is
also enriched to carry all five phase-level values for full audit-by-scan
**Design hypothesis**: R10 V-04 declares containers at the point of execution. A reader
scanning the document cannot verify the four-container lifecycle structure without reading
each container header individually. Adding a manifest at the top — listing all four
containers, their phase ranges, and their single-function scope — creates a document-level
entry contract analogous to what C-33 creates for CALIBRATE alone. The enriched CONTAINER:
CLOSE COMPLETE line tests whether carrying all five post-build results (comparison, verdict,
counter-evidence disposition, limitation, replication status) produces a fully audit-scannable
container boundary. C-33 and C-34 are not introduced — single-axis test.

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

This output is organized into four lifecycle containers. Each container has exactly one
function. Execute them in order. No container may absorb work that belongs to another.

| Container | Phases | Single function |
|-----------|--------|-----------------|
| DESIGN | 1-3 | Hypothesis, scope, and measurement criteria only — no competitor identification |
| CALIBRATE | 4 | Inertia competitor identification, B-00, and outperform threshold only — no design or build activity |
| BUILD | 5-6 | Prototype construction and raw measurement only — no comparison or interpretation |
| CLOSE | 7-11 | Comparison, verdict, counter-evidence, limitations, and replication only — no new criteria or competitor framing |

A scan of the four CONTAINER: [NAME] COMPLETE lines must be sufficient to reconstruct the
full outcome chain without reading any container body.

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

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis = "[text]", scope bounded
([N] exclusions validated), success threshold = [threshold], failure threshold = [threshold].
Inertia competitor identification is prohibited in this container — belongs exclusively in
CALIBRATE. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container holds all inertia-competitor content: the identification of the status-quo
approach being challenged, the B-00 measurement of what that approach produces, and the
explicit framing of what the prototype must achieve relative to it. A scan of this container
alone must answer: what is the current alternative, what does it produce, and what must the
prototype exceed? No scope definition, hypothesis activity, build steps, or experimental
measurement belongs here.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | Inertia competitor name and identification; B-00 measurement on Phase 3 metric; explicit statement that prototype must exceed B-00 to confirm the hypothesis | Prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims about the prototype |

---

### Phase 4 — CALIBRATOR: Identify inertia competitor and measure B-00
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in your
output.*

Name the current approach the prototype challenges. Apply the Phase 3 metric to the inertia
competitor and record B-00. State explicitly what the prototype must produce relative to
B-00 to confirm the hypothesis.

> **Inertia competitor**: [name of current method, tool, or approach being displaced]
> **Why it is the status-quo**: [one sentence]
> **B-00 measurement**: [what the inertia competitor produces on the Phase 3 metric]
> **Required result to confirm hypothesis**: The prototype must produce [predicted outcome]
>   relative to B-00 = [value]. Matching or underperforming B-00 does not confirm the
>   hypothesis.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]"; B-00 = [value];
outperform requirement stated. [If PARTIAL: "[inertia competitor name | B-00 measurement |
outperform statement] absent."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor identified =
"[name]", B-00 committed = [value], outperform threshold stated = prototype must
[direction and condition relative to B-00]. Exclusively pre-build inertia content.
[If PARTIAL: "[absent element] not established — scan-level audit incomplete."]**

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
B-00 = [Phase 4 value] for "[inertia competitor]"; replication path [complete | partial —
[absent element]]. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CLOSE
*Phases 7-11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| ANALYST | Comparison vs. threshold and inertia competitor, verdict, counter-evidence, limitations, next step, replication | New measurement criteria; inertia competitor framing not established in Phase 4 |

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

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation = "[one sentence]"; next step =
"[one sentence]". [If PARTIAL: "[limitation | next step] absent."]**

---

### Phase 11 — ANALYST: Replication path
*Execute after Phase 10 gate is present in your output.*

List all tools, inputs, commands, and steps to reproduce. No implicit steps.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete — [N] steps,
key tool = [primary tool or method]. [If PARTIAL: "[element] not specified."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE];
B-00 delta = [observed vs B-00 for "[inertia competitor]"]; counter-evidence =
[ADDRESSED — [interpretation] | CLOSED — no counter]; limitation = "[name]";
replication [complete | partial — [absent element]].
[If PARTIAL: "[element] absent."]**
```

---

## V-04 — Combined: C-33 + C-34 (R11 Seed)

**Axes**: C-33 numbered CALIBRATE entry contract (V-01) + C-34 competitor-labeled baseline
column (V-02) applied simultaneously to R10 V-05 base (which has C-31 + C-32 + C-30)
**Design hypothesis**: C-33 fires at CALIBRATE container entry — it requires the header to
enumerate the three responsibilities before the body executes them. C-34 fires at the results
table — it requires the baseline column to name the inertia competitor. The two criteria
operate on different structural surfaces at different lifecycle stages: CALIBRATE entry
(pre-build) vs. Phase 7 table (post-build). Neither implies the other. V-01 tests C-33 alone;
V-02 tests C-34 alone. This variation tests whether both can be satisfied simultaneously
without degrading C-31, C-32, or C-30. Expected: 231 (R10 V-05) + 7 (C-33) = 238.

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
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in your
output.*

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
observed [value], baseline (inertia competitor) [value]); delta rationale co-located.
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

## V-05 — Combined: C-33 + C-34 + Lifecycle Manifest (Ceiling Attempt)

**Axes**: C-33 numbered CALIBRATE entry contract + C-34 competitor-labeled baseline column
+ V-03 document-level container manifest + enriched CONTAINER: CLOSE COMPLETE line
**Design hypothesis**: V-04 achieves C-33 and C-34 simultaneously (predicted 238). V-03's
container manifest creates a document-level structural contract visible before any container
is read — a second entry contract that spans the full output lifecycle, not just CALIBRATE.
Combining V-04 with V-03's manifest tests whether two entry contracts at different scopes
(document-level and CALIBRATE-level) produce any additional scorable structure. The enriched
CONTAINER: CLOSE COMPLETE line carrying all five post-build result values tests whether
container-level completion lines satisfy C-22 more fully than phase-level lines alone.
Expected ceiling: 238 (V-04) + structural improvements — targeting the full 246 if manifest
or CLOSE COMPLETE enrichment unlocks any unscored criteria.

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

This output is organized into four lifecycle containers. Each container has exactly one
function. Execute them in order. No container may absorb work that belongs to another.

| Container | Phases | Single function |
|-----------|--------|-----------------|
| DESIGN | 1-3 | Hypothesis, scope, and measurement criteria only — no competitor identification |
| CALIBRATE | 4 | Inertia competitor identification, B-00, and outperform threshold only — no design or build activity |
| BUILD | 5-6 | Prototype construction and raw measurement only — no comparison or interpretation |
| CLOSE | 7-11 | Comparison, verdict, counter-evidence, limitations, and replication only — no new criteria or competitor framing |

A scan of the four CONTAINER: [NAME] COMPLETE lines must be sufficient to reconstruct the
full outcome chain without reading any container body.

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

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis = "[text]", scope bounded
([N] exclusions validated), success threshold = [threshold], failure threshold = [threshold].
Inertia competitor identification is prohibited in this container — belongs exclusively in
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
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in your
output.*

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

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built; raw result = [value];
B-00 = [Phase 4 value] for "[inertia competitor]"; replication path [complete | partial —
[absent element]]. [If PARTIAL: "[element] absent."]**

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
observed [value], baseline (inertia competitor) [value]); delta rationale co-located.
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

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation = "[one sentence]"; next step =
"[one sentence]". [If PARTIAL: "[limitation | next step] absent."]**

---

### Phase 11 — ANALYST: Replication path
*Execute after Phase 10 gate is present in your output.*

List all tools, inputs, commands, and steps to reproduce. No implicit steps.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete — [N] steps,
key tool = [primary tool or method]. [If PARTIAL: "[element] not specified."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE];
B-00 delta = [observed vs B-00 for "[inertia competitor]"]; counter-evidence =
[ADDRESSED — [interpretation named] | CLOSED — no plausible counter, reason: [reason]];
limitation = "[name]"; replication [complete — [N] steps | partial — [absent element]];
table columns all populated [FULL | PARTIAL — [column] absent].
[If PARTIAL: "[element] absent."]**
```

---

## Scoring Predictions (v11 rubric, 246 pts)

| Variation | Base | Key Changes | C-33 | C-34 | Expected Gain | Predicted Score |
|-----------|------|-------------|------|------|---------------|-----------------|
| V-01 | R10 V-04 (C-31+C-32) | Numbered CALIBRATE header | PASS | FAIL | +C-33 | ~218 |
| V-02 | R10 V-05 (C-31+C-32+C-30) | Competitor-labeled column | FAIL | PASS | C-34 more explicit than R10 V-05 | ~231 |
| V-03 | R10 V-04 (C-31+C-32) | Container manifest + enriched CLOSE COMPLETE | FAIL | FAIL | +structural clarity | ~211+ |
| V-04 | R10 V-05 (C-31+C-32+C-30) | C-33 + C-34 simultaneously | PASS | PASS | +C-33 | ~238 |
| V-05 | V-04 (C-33+C-34) | + container manifest + enriched CLOSE COMPLETE | PASS | PASS | +structural improvements | ~238+ |

**Note on V-01**: Uses R10 V-04 as base (no three-column table) to isolate C-33. If C-33 is
satisfied and C-34 is not attempted, the score tests the C-33 contribution alone.

**Note on V-02**: R10 V-05 may have already satisfied C-34 via "B-00 Baseline (Phase 4)"
labeling. V-02 makes the competitor identity explicit in the column header. If V-02 scores
the same as R10 V-05 (231), C-34 was already satisfied. If V-02 scores higher, C-34 required
the stronger label.

**Note on V-03**: The container manifest is a structural addition not targeted at any known
rubric criterion. If it scores higher than V-01 (which has no manifest), the manifest is
influencing score through an unidentified mechanism — a potential v12 gap signal.

**Note on V-04**: This is the R11 seed. The two-criterion combination requires V-01 and V-02
to have independently established single-axis baselines before V-04's combined score can be
attributed to the combination rather than to confounding changes.

**Note on V-05**: V-05 adds structural depth (manifest + enriched CLOSE COMPLETE) to V-04's
ceiling target. If V-05 outscores V-04, the gap between them is attributable to the manifest
or enriched CLOSE COMPLETE — a potential v12 seed.
