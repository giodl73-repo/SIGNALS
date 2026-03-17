Saved to `simulations/quest/variations/prove-prototype-variations-R13-2026-03-14.md`.

---

## Round 13 Variations — prove-prototype (v12 rubric, 260 pts)

**Base**: R12 V-04 (252 / 260). **Remaining gap**: 8 pts (C-24–C-28 partial carry-forwards). **Gap signals from R12**: V-03 (chain-coherent handoff) and V-05 (checkable manifest rows + manifest conformance record).

---

### Variation axes

| # | Single/Combined | Axis | Target |
|---|----------------|------|--------|
| V-01 | Single | **Role-sequence** | C-25 — CLOSE split into ANALYST-EVALUATOR (Phases 7-8) + ANALYST-AUDITOR (Phases 9-11), making container/role boundaries demonstrably non-coincident across all four containers |
| V-02 | Single | **Output format** | C-26/C-27 — PHASE 7 COMPLETE and BUILD COMPLETE carry an explicit "delta vs. B-00 = [direction and magnitude]" inline labeled token, not just juxtaposed values |
| V-03 | Single (gap probe) | **Lifecycle emphasis** | Neither — each intermediate CONTAINER COMPLETE adds a `→ [NEXT] receives:` forward-reference field naming the downstream container's principal inputs with their committed values |
| V-04 | Combined (seed) | **Role-sequence + output format** | C-25 + C-26/C-27 simultaneously on R12 V-04 base |
| V-05 | Combined + gap | **V-04 + V-05 R12 signals** | C-25 + C-26/C-27 + manifest rows with COMPLETE-line-verifiable specificity + `manifest conformance:` second field in CLOSE COMPLETE |

---

### Key design decisions

**V-01 vs V-02 single-axis isolation**: V-01 tests C-25 (orthogonality) by making container/role independence structurally explicit — CLOSE gets two sub-roles at different phase subsets. V-02 tests C-26/C-27 (baseline comparison token) by adding the delta inline to results-phase completion lines, covering the gap between C-36 (full chain at terminal) and C-26 (comparison in a results-phase completion line).

**V-03 is the R12 V-03 gap signal**: chain-coherent handoff acknowledgment — each intermediate COMPLETE line names what the next container depends on receiving. Independent of C-25/C-26; tests whether handoff-forward-referencing is a scorable v13 surface.

**V-04 is the R13 seed**: both C-25 and C-26/C-27 targeted simultaneously, preserving C-33, C-34, C-35, C-36.

**V-05 adds two gap surfaces**: checkable manifest rows (field-level specificity against COMPLETE lines) + `manifest conformance:` record in CLOSE COMPLETE as a second terminal audit act distinct from the C-36 result chain — probing C-37 candidate.
BRATE receives: hypothesis text, success threshold, failure threshold"; CALIBRATE COMPLETE → "BUILD receives: inertia competitor name, B-00 value, Phase 3 metric"; BUILD COMPLETE → "CLOSE receives: raw result, B-00, inertia competitor name for three-column comparison." Gap probe: chain-coherent handoff acknowledgment between containers — V-03 R12 signal.

**V-04** — R13 seed attempt. Both V-01 and V-02 axes combined on R12 V-04 base. CLOSE split into ANALYST-EVALUATOR + ANALYST-AUDITOR (C-25 target). PHASE 7 COMPLETE and BUILD COMPLETE carry explicit delta-vs-B-00 inline tokens (C-26/C-27 target). Expected: 252 + C-25/C-26/C-27 uplift up to the 260 ceiling.

**V-05** — V-04 base plus the two V-05 R12 gap signals: (1) manifest rows annotated with "Expected output (verifiable at COMPLETE line)" using field-level specificity so each row's promise is mechanically checkable against the corresponding CONTAINER COMPLETE; (2) CLOSE COMPLETE adds a second terminal audit field: "manifest conformance: DESIGN [FULL|PARTIAL], CALIBRATE [FULL|PARTIAL], BUILD [FULL|PARTIAL], CLOSE [FULL|PARTIAL]" — distinct from the C-36 result chain. Gap probe for C-37 candidate: terminal line cross-verifies document-level manifest.

---

### Predicted scores

| Variation | C-25 | C-26/C-27 | Score |
|-----------|------|-----------|-------|
| V-01 | PASS? | FAIL | **~252 +** |
| V-02 | FAIL | PASS? | **~252 +** |
| V-03 | FAIL | FAIL | **252** (gap only) |
| V-04 | PASS? | PASS? | **~260** (seed attempt) |
| V-05 | PASS? | PASS? | **~260** + gap signal |

---

## V-01 — Single Axis: Role-Sequence (CLOSE Split into Two Sub-Roles)

**Axis**: Role sequence — the CLOSE container declares two explicitly named analyst sub-roles operating at different lifecycle sub-stages, making container-boundary/role-boundary independence structurally unambiguous across all four containers.
**Design hypothesis**: R12 V-04's CLOSE container has one ANALYST role spanning Phases 7-11. Combined with DESIGN (one FRAMER) and CALIBRATE (one CALIBRATOR), three of four containers have exactly one role, making container and role boundaries coincident for 75% of the structure. C-25 requires "lifecycle stage boundaries and role label boundaries operate at different structural granularities." BUILD already satisfies this (BUILDER + RECORDER). V-01 extends that independence to CLOSE by splitting its analyst function into ANALYST-EVALUATOR (verdict formation: table + verdict) and ANALYST-AUDITOR (experiment closure: counter-evidence + limitations + replication), creating two non-coincident annotation layers across all four containers simultaneously.

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
*This container has two analyst roles operating at different lifecycle sub-stages:
ANALYST-EVALUATOR handles verdict formation (Phases 7-8); ANALYST-AUDITOR handles
experiment closure (Phases 9-11). Container boundaries and role boundaries are not
coincident — this container spans two roles; each role spans a subset of phases.*

### Roles in this container

| Role | Phases | Writes | Must NOT Write |
|------|--------|--------|----------------|
| ANALYST-EVALUATOR | 7-8 (verdict formation) | Three-column comparison table with competitor-labeled baseline column, verdict | Counter-evidence disposition, limitations, next step, replication path; new measurement criteria; inertia competitor framing not established in Phase 4 |
| ANALYST-AUDITOR | 9-11 (experiment closure) | Counter-evidence check, limitations, next step, replication path | Table content, verdict, B-00 comparison, new result interpretation |

---

### Phase 7 — ANALYST-EVALUATOR: Three-column results table
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

Populate the three-column results table. The baseline column must be labeled with the
inertia competitor's name — not merely "B-00" or "Baseline (Phase 4)." The inertia
competitor must be identifiable by scanning the column header alone, without reading
the Phase 4 container body. All three columns must be populated with values from prior phases.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline ([inertia competitor]) |
|--------|--------------------|--------------------|----------------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value from Phase 4] |

> **Delta vs. threshold**: [match or mismatch — how observed compares to success/failure threshold]
> **Delta vs. B-00**: [observed relative to inertia baseline — direction and magnitude]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], baseline ([inertia competitor name]) [value]); delta rationale co-located.
[If PARTIAL: "[predicted | observed | baseline] column absent — structural gap in table."]**

---

### Phase 8 — ANALYST-EVALUATOR: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6-7 including the B-00 comparison.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. [If PARTIAL: "verdict without evidentiary grounding."]**

---

### Phase 9 — ANALYST-AUDITOR: Counter-evidence check
*Execute before Phase 10. Execute after Phase 8 gate is present in your output.*

Close with exactly one of two dispositions:
- **(a)** Name the counter-interpretation and rebut it with evidence-grounded reasoning.
- **(b)** State explicitly that no plausible counter-interpretation exists, with a reason.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "no explicit disposition."]**

---

### Phase 10 — ANALYST-AUDITOR: Limitations and next step
*Execute before Phase 11. Execute after Phase 9 gate is present in your output.*

State one limitation. State one specific next step.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[limitation | next step] absent."]**

---

### Phase 11 — ANALYST-AUDITOR: Replication path
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

## V-02 — Single Axis: Output Format (PHASE 7 COMPLETE and BUILD COMPLETE Carry Explicit Delta Token)

**Axis**: Output format — the PHASE 7 COMPLETE line and CONTAINER: BUILD COMPLETE line each carry an explicit "delta vs. B-00 = [direction and magnitude]" inline labeled token, not merely reporting B-00 alongside the raw result.
**Design hypothesis**: In R12 V-04, PHASE 7 COMPLETE encodes "three-column table populated (predicted [v], observed [v], baseline ([name]) [v]); delta rationale co-located" — it confirms the table is populated but does not embed the delta value itself in the completion line. BUILD COMPLETE encodes "raw result = [v]; B-00 = [v] for [name]" — the two values are juxtaposed but no explicit comparison appears. C-26 requires "at least one completion line in the results or evaluation phase carries an explicit comparison against that baseline." The CLOSE COMPLETE's C-36 chain carries delta vs. B-00 (at the document terminal level), but C-26 may require the comparison to appear in a results-phase completion line (Phases 6-7), not only the terminal audit record. V-02 adds the delta token explicitly to PHASE 7 COMPLETE and to BUILD COMPLETE, covering both the measurement phase and the results phase. C-27 tests the grade token within these lines. No role changes from R12 V-04.

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
[value]; B-00 = [Phase 4 value] for "[inertia competitor]"; delta vs. B-00 = [direction and
magnitude — observed [above|below|at] B-00 by [amount]]. [If PARTIAL: "[element]
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

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline ([inertia competitor]) |
|--------|--------------------|--------------------|----------------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value from Phase 4] |

> **Delta vs. threshold**: [match or mismatch — how observed compares to success/failure threshold]
> **Delta vs. B-00**: [observed relative to inertia baseline — direction and magnitude]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], baseline ([inertia competitor name]) [value]); delta vs. B-00 = [direction
and magnitude]; delta rationale co-located. [If PARTIAL: "[predicted | observed | baseline |
delta] absent — structural gap in table or comparison."]**

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

## V-03 — Single Axis: Lifecycle Emphasis (Chain-Coherent Handoff Lines — Gap Probe)

**Axis**: Lifecycle emphasis — each intermediate CONTAINER COMPLETE line carries a forward-reference field naming the downstream container's principal input dependencies with their committed values, creating an unbroken chain of acknowledged handoffs between containers.
**Design hypothesis**: In R12 V-04, each CONTAINER COMPLETE is self-contained: it confirms what its own container discharged but says nothing about what the next container depends on receiving. A structural surface exists between containers that is currently unscored: the acknowledgment that a downstream container requires specific values committed upstream. If DESIGN COMPLETE explicitly states "CALIBRATE receives: hypothesis text = [text], success threshold = [value], failure threshold = [value]," a reader can verify the handoff without reading the CALIBRATE container header. This is the V-03 R12 gap signal: "chain-coherent handoff acknowledgment." This variation tests whether that pattern creates a scorable structural surface distinct from C-22 (backward-looking result values) and C-35/C-36 (document-boundary brackets). No manifest changes, no role changes.

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
CALIBRATE.
→ CALIBRATE receives: hypothesis = "[text]", success threshold = [value], failure
threshold = [value], Phase 3 metric = "[metric name]".
[If PARTIAL: "[element] absent — handoff to CALIBRATE incomplete."]**

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
→ BUILD receives: inertia competitor = "[name]", B-00 = [value], Phase 3 metric =
"[metric name]" for prototype measurement.
[If PARTIAL: "responsibility ([1|2|3]) not discharged — handoff to BUILD incomplete."]**

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
[value]; B-00 = [Phase 4 value] for "[inertia competitor]".
→ CLOSE receives: raw result = [value], B-00 = [value], inertia competitor = "[name]"
for three-column comparison; Phase 3 metric = "[metric name]".
[If PARTIAL: "[element] absent — handoff to CLOSE incomplete."]**

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

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline ([inertia competitor]) |
|--------|--------------------|--------------------|----------------------------------|
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

## V-04 — Combined: Role-Sequence + Output Format (R13 Seed)

**Axes**: V-01 (CLOSE split into ANALYST-EVALUATOR + ANALYST-AUDITOR, targeting C-25) + V-02 (PHASE 7 COMPLETE and BUILD COMPLETE carry explicit delta-vs-B-00 token, targeting C-26/C-27), both applied simultaneously to R12 V-04 base.
**Design hypothesis**: C-25 and C-26/C-27 are independent structural gaps in R12 V-04. C-25 requires container/role annotation layers to be structurally non-coincident; V-01 closes this by making CLOSE have two sub-roles at different phase subsets, so all four containers have either 2 roles or a multi-phase single-role span that differs from its container boundary. C-26 requires an explicit comparison against the baseline to appear in a results-phase completion line; V-02 closes this by embedding delta-vs-B-00 in PHASE 7 COMPLETE (results phase) and BUILD COMPLETE (measurement phase). Neither fix degrades C-33, C-34, C-35, or C-36. Expected: 252 + C-25/C-26/C-27 uplift to ceiling.

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
[value]; B-00 = [Phase 4 value] for "[inertia competitor]"; delta vs. B-00 = [direction and
magnitude — observed [above|below|at] B-00 by [amount]]. [If PARTIAL: "[element]
absent."]**

---

## CONTAINER: CLOSE
*Phases 7-11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*
*This container has two analyst roles operating at different lifecycle sub-stages:
ANALYST-EVALUATOR handles verdict formation (Phases 7-8); ANALYST-AUDITOR handles
experiment closure (Phases 9-11). Container boundaries and role boundaries are not
coincident — this container spans two roles; each role spans a subset of phases.*

### Roles in this container

| Role | Phases | Writes | Must NOT Write |
|------|--------|--------|----------------|
| ANALYST-EVALUATOR | 7-8 (verdict formation) | Three-column comparison table with competitor-labeled baseline column, verdict | Counter-evidence disposition, limitations, next step, replication path; new measurement criteria; inertia competitor framing not established in Phase 4 |
| ANALYST-AUDITOR | 9-11 (experiment closure) | Counter-evidence check, limitations, next step, replication path | Table content, verdict, B-00 comparison, new result interpretation |

---

### Phase 7 — ANALYST-EVALUATOR: Three-column results table
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

Populate the three-column results table. The baseline column must be labeled with the
inertia competitor's name — not merely "B-00" or "Baseline (Phase 4)." The inertia
competitor must be identifiable by scanning the column header alone, without reading
the Phase 4 container body. All three columns must be populated with values from prior phases.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline ([inertia competitor]) |
|--------|--------------------|--------------------|----------------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value from Phase 4] |

> **Delta vs. threshold**: [match or mismatch — how observed compares to success/failure threshold]
> **Delta vs. B-00**: [observed relative to inertia baseline — direction and magnitude]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], baseline ([inertia competitor name]) [value]); delta vs. B-00 = [direction
and magnitude]; delta rationale co-located. [If PARTIAL: "[predicted | observed | baseline |
delta] absent — structural gap in table or comparison."]**

---

### Phase 8 — ANALYST-EVALUATOR: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6-7 including the B-00 comparison.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. [If PARTIAL: "verdict without evidentiary grounding."]**

---

### Phase 9 — ANALYST-AUDITOR: Counter-evidence check
*Execute before Phase 10. Execute after Phase 8 gate is present in your output.*

Close with exactly one of two dispositions:
- **(a)** Name the counter-interpretation and rebut it with evidence-grounded reasoning.
- **(b)** State explicitly that no plausible counter-interpretation exists, with a reason.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "no explicit disposition."]**

---

### Phase 10 — ANALYST-AUDITOR: Limitations and next step
*Execute before Phase 11. Execute after Phase 9 gate is present in your output.*

State one limitation. State one specific next step.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[limitation | next step] absent."]**

---

### Phase 11 — ANALYST-AUDITOR: Replication path
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

## V-05 — Combined + Gap Probe: V-04 Base + Checkable Manifest + Terminal Manifest Conformance

**Axes**: V-04 (C-25 + C-26/C-27) + gap probe 1 (manifest rows annotated with field-level verifiable expected outputs, V-05 R12 signal 1) + gap probe 2 (CLOSE COMPLETE encodes manifest conformance record per container as a second terminal audit field, V-05 R12 signal 2).
**Design hypothesis**: V-04 satisfies C-25, C-26/C-27, C-35, and C-36. Two unscored structural surfaces from V-05 R12 remain: (1) manifest rows that state expected output in terms directly verifiable against specific COMPLETE-line field values — not just describing intent, but naming the exact fields that the COMPLETE line must encode; (2) a "manifest conformance" record in the CLOSE COMPLETE line that explicitly cross-verifies whether each container delivered its manifest-promised output. These are structurally separate from the C-36 result chain: C-36 records what happened; manifest conformance records whether what was promised was delivered. Gap probe for C-37 candidate: "CLOSE COMPLETE cross-verifies the document-level manifest by container."

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
"Expected output (verifiable at COMPLETE line)" column states the specific fields the
corresponding CONTAINER: [NAME] COMPLETE line must confirm. Execute containers in the order
listed. No container may absorb work that belongs to another.

| Container | Phases | Principal purpose | Expected output (verifiable at COMPLETE line) |
|-----------|--------|-------------------|-----------------------------------------------|
| DESIGN | 1-3 | Lock the hypothesis, bound the prototype scope, and freeze measurement criteria — no competitor identification | Hypothesis text (quoted), count of validated exclusions, success threshold value, failure threshold value |
| CALIBRATE | 4 | Identify the inertia competitor, commit the B-00 baseline, and state the outperform threshold — all before any build activity | Inertia competitor name, B-00 numeric value, outperform threshold direction and condition |
| BUILD | 5-6 | Build the smallest prototype that tests the hypothesis and record the raw measurement — no comparison or interpretation | Prototype built (minimality trade-off on record), raw result numeric value on Phase 3 metric, delta vs. B-00 direction and magnitude |
| CLOSE | 7-11 | Compare actual vs. predicted vs. B-00, render the hypothesis verdict, close the counter-evidence check, record limitations and replication path | Three-column table with competitor-labeled baseline populated, verdict word, counter-evidence disposition (ADDRESSED or CLOSED), limitation named, replication path complete |

The terminal CONTAINER: CLOSE COMPLETE line encodes two independent audit records:
(1) the full experimental result chain spanning all four containers (C-36); and
(2) a manifest conformance record confirming whether each container delivered its
promised expected output.

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
[value]; B-00 = [Phase 4 value] for "[inertia competitor]"; delta vs. B-00 = [direction and
magnitude — observed [above|below|at] B-00 by [amount]]. [If PARTIAL: "[element]
absent — manifest expected output not fully delivered."]**

---

## CONTAINER: CLOSE
*Phases 7-11. Execute after CONTAINER: BUILD gate is present in your output. Absorbs all
post-evidence sections. Every phase carries an explicit gate.*
*This container has two analyst roles operating at different lifecycle sub-stages:
ANALYST-EVALUATOR handles verdict formation (Phases 7-8); ANALYST-AUDITOR handles
experiment closure (Phases 9-11). Container boundaries and role boundaries are not
coincident — this container spans two roles; each role spans a subset of phases.*

### Roles in this container

| Role | Phases | Writes | Must NOT Write |
|------|--------|--------|----------------|
| ANALYST-EVALUATOR | 7-8 (verdict formation) | Three-column comparison table with competitor-labeled baseline column, verdict | Counter-evidence disposition, limitations, next step, replication path; new measurement criteria; inertia competitor framing not established in Phase 4 |
| ANALYST-AUDITOR | 9-11 (experiment closure) | Counter-evidence check, limitations, next step, replication path | Table content, verdict, B-00 comparison, new result interpretation |

---

### Phase 7 — ANALYST-EVALUATOR: Three-column results table
*Execute before Phase 8. Execute after Phase 6 gate is present in your output.*

Populate the three-column results table. The baseline column must be labeled with the
inertia competitor's name — not merely "B-00" or "Baseline (Phase 4)." The inertia
competitor must be identifiable by scanning the column header alone, without reading
the Phase 4 container body. All three columns must be populated with values from prior phases.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline ([inertia competitor]) |
|--------|--------------------|--------------------|----------------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value from Phase 4] |

> **Delta vs. threshold**: [match or mismatch — how observed compares to success/failure threshold]
> **Delta vs. B-00**: [observed relative to inertia baseline — direction and magnitude]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], baseline ([inertia competitor name]) [value]); delta vs. B-00 = [direction
and magnitude]; delta rationale co-located. [If PARTIAL: "[predicted | observed | baseline |
delta] absent — structural gap in table or comparison."]**

---

### Phase 8 — ANALYST-EVALUATOR: Render verdict
*Execute before Phase 9. Execute after Phase 7 gate is present in your output.*

State whether the hypothesis is confirmed, refuted, or inconclusive. Ground the verdict in
Phases 6-7 including the B-00 comparison.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. [If PARTIAL: "verdict without evidentiary grounding."]**

---

### Phase 9 — ANALYST-AUDITOR: Counter-evidence check
*Execute before Phase 10. Execute after Phase 8 gate is present in your output.*

Close with exactly one of two dispositions:
- **(a)** Name the counter-interpretation and rebut it with evidence-grounded reasoning.
- **(b)** State explicitly that no plausible counter-interpretation exists, with a reason.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "no explicit disposition."]**

---

### Phase 10 — ANALYST-AUDITOR: Limitations and next step
*Execute before Phase 11. Execute after Phase 9 gate is present in your output.*

State one limitation. State one specific next step.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[limitation | next step] absent."]**

---

### Phase 11 — ANALYST-AUDITOR: Replication path
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
manifest conformance: DESIGN [FULL|PARTIAL — [item] not delivered], CALIBRATE [FULL|PARTIAL — [item] not delivered], BUILD [FULL|PARTIAL — [item] not delivered], CLOSE [FULL|PARTIAL — [item] not delivered].
[If PARTIAL: "[absent element from which container] not encoded — audit chain or manifest conformance incomplete."]**
```

---

## Summary

| Variation | Axis | C-25 | C-26/C-27 | Score |
|-----------|------|------|-----------|-------|
| V-01 | Role-sequence (CLOSE split) | PASS? | FAIL | ~252+ |
| V-02 | Output format (delta token in P7 + BUILD) | FAIL | PASS? | ~252+ |
| V-03 | Gap probe (chain-coherent handoff) | FAIL | FAIL | 252 (gap only) |
| V-04 | Combined (seed) | PASS? | PASS? | ~260 |
| V-05 | Combined + gap | PASS? | PASS? | ~260 + gap signals |
