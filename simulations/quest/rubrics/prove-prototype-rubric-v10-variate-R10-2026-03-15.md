# Quest Variate — prove-prototype Round 10 (v10 rubric, 232 pts)

**Date**: 2026-03-15
**Rubric version**: v10 (adds C-31 and C-32; ceiling 218 → 232)
**Round 9 winner**: V-03 (CALIBRATOR owns all inertia content; FRAMER prohibited from competitor
identification; CALIBRATE COMPLETE carries "inertia competitor identified, B-00 committed,
outperform threshold stated")

**Why neither R9 variation passes both C-31 and C-32 simultaneously**:

C-31 requires the FRAMER prohibition to name inertia competitor identification as content the
FRAMER must not produce AND — per the criterion description — state that it "must NOT appear in
DESIGN and must reside exclusively in CALIBRATE." R9-V-03 lists "inertia competitor
identification" in Must NOT Write, but the prohibition is a column entry, not an explicit routing
declaration. A role-label scan detects that FRAMER excluded it; it does not detect where it is
required to go. Without the routing language, the prohibition cannot be verified as CALIBRATE-
exclusive by a scan that does not also read the CALIBRATE container body.

C-32 requires the CALIBRATE COMPLETE line to embed the actual B-00 value (criterion: "B-00
committed with its value"). R9-V-03's CALIBRATE COMPLETE says "inertia competitor identified,
B-00 committed, outperform threshold stated" — all three labels present, but B-00 is labeled
without its value. A scan-only auditor cannot confirm the triple contains a committed value
without entering the container body.

**R10 seed**: (1) add routing destination language to the FRAMER prohibition; (2) embed the B-00
value token in the CALIBRATE COMPLETE line. Both C-31 and C-32 should be satisfiable
simultaneously for the first time.

**Variation axes**:
- V-01 (single): C-31 axis — FRAMER prohibition gains explicit routing destination ("must NOT
  appear in DESIGN — belongs exclusively in CALIBRATE")
- V-02 (single): C-32 axis — CALIBRATE COMPLETE embeds B-00 value and all three named elements
  with their values
- V-03 (single): Lifecycle emphasis axis — CALIBRATE container header enumerates its three
  single-function responsibilities, making the container boundary structurally explicit
- V-04 (combined): C-31 + C-32 — both fixes applied simultaneously on R9-V-03 base
- V-05 (combined): C-31 + C-32 + C-30 — V-04 plus three-column results table in Phase 7

---

## V-01 — Single Axis: C-31 Explicit Routing Language in FRAMER Prohibition

**Axis**: C-31 — FRAMER prohibition gains explicit routing destination
**Design hypothesis**: R9-V-03's FRAMER prohibition lists "inertia competitor identification" in
the Must NOT Write column, but the column entry does not say where the content belongs. C-31's
criterion description says the prohibition must state that inertia competitor identification
"must NOT appear in DESIGN and must reside exclusively in CALIBRATE." Adding routing language
to three places — the FRAMER role table cell, the DESIGN container note, and the DESIGN COMPLETE
confirmation — creates a role-label scan surface that not only detects that FRAMER excluded the
content but confirms CALIBRATE is the required destination. The hypothesis: explicit routing
language in the prohibition satisfies C-31 independent of whether CALIBRATE is read. Everything
else from R9-V-03 is unchanged. C-32 is not introduced — single-axis test.

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

State what will be measured. State the success threshold (the result that confirms the
hypothesis). State the failure threshold (the result that refutes it). These criteria are
frozen at this gate.

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
*This container holds all inertia-competitor content: identification of the status-quo
approach being challenged, the B-00 measurement of what that approach produces, and the
explicit framing of what the prototype must achieve relative to it. A scan of this
container alone must answer: what is the current alternative, what does it produce, and
what must the prototype exceed? No scope definition, hypothesis activity, build steps, or
experimental measurement belongs here.*

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
> **Why it is the status-quo**: [one sentence — why this is the existing alternative]
> **B-00 measurement**: [what the inertia competitor produces on the Phase 3 metric]
> **Required result to confirm hypothesis**: The prototype must produce [predicted outcome]
>   relative to B-00 = [value]. A result that matches B-00 or moves in the opposite direction
>   does not confirm the hypothesis; the null counter-interpretation would not be ruled out.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]"; B-00 = [value];
outperform requirement stated. [If PARTIAL: "[inertia competitor name | B-00 measurement |
outperform statement] absent."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor identified,
B-00 committed, outperform threshold stated. Exclusively pre-build inertia content.
[If PARTIAL: "[element] absent."]**

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

## V-02 — Single Axis: C-32 Embedded Values in CALIBRATE COMPLETE

**Axis**: C-32 — CALIBRATE COMPLETE line embeds the actual B-00 value and all three named
elements with committed values
**Design hypothesis**: R9-V-03's CALIBRATE COMPLETE line says "inertia competitor identified,
B-00 committed, outperform threshold stated" — all three labels present, but B-00 is a label
without a value. C-32 requires "B-00 committed with its value" so a scan-only auditor can
confirm the triple without entering the container body. Adding the B-00 value token (e.g.,
"B-00 committed = [value]") to the CALIBRATE COMPLETE line closes the gap. The same treatment
is applied to the inertia competitor name and the outperform threshold, making all three
elements scannable. C-31 routing language is not added — single-axis test. The hypothesis:
embedding values in the CALIBRATE COMPLETE line is sufficient to satisfy C-32, independent of
the FRAMER prohibition wording.

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

State what the prototype will and will not do. Name at least two explicit exclusions. For
each exclusion, state immediately why the test remains valid without it.

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
exclusions with validity), measurement thresholds established. No inertia competitor named
here — that belongs to CALIBRATE. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container holds all inertia-competitor content: the identification of the status-quo
approach, the B-00 measurement, and the explicit outperform framing. A scan of this container
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

Name the current approach that the prototype is challenging. This is the inertia competitor.
Apply the Phase 3 metric to it and record B-00. State explicitly what the prototype must
produce relative to B-00 to confirm the hypothesis.

> **Inertia competitor**: [name of current method, tool, or approach being displaced]
> **Why it is the status-quo**: [one sentence]
> **B-00 measurement**: [what the inertia competitor produces on the Phase 3 metric]
> **Required result to confirm hypothesis**: The prototype must produce [predicted outcome]
>   relative to B-00 = [value]. A result that matches or underperforms B-00 does not confirm
>   the hypothesis; the null counter-interpretation holds.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]"; B-00 = [value];
outperform requirement stated. [If PARTIAL: "[inertia competitor name | B-00 measurement |
outperform statement] absent."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor identified =
"[name]", B-00 committed = [value], outperform threshold stated = prototype must [direction
and condition]. Exclusively pre-build inertia content. [If PARTIAL: "[absent element] not
established — scan-level audit incomplete."]**

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

## V-03 — Single Axis: Lifecycle Emphasis (CALIBRATE Three-Function Header)

**Axis**: Lifecycle emphasis — CALIBRATE container header enumerates its three single-function
responsibilities as a numbered list, making the container boundary structurally explicit and
the three-element audit target visible before the container body is read
**Design hypothesis**: R9-V-03's CALIBRATE header describes what the container holds in one
dense sentence. A numbered list of three responsibilities — (1) identify inertia competitor,
(2) measure B-00, (3) state outperform threshold — creates a structural contract visible at the
container header level, before Phase 4 is read. This makes the CALIBRATE COMPLETE line's triple
confirmation legible as a closure of three stated obligations rather than as a free-form
assertion. The hypothesis: an enumerated three-function header makes C-32's audit-by-scan
semantics readable at the container level, independent of whether the CALIBRATE COMPLETE line
format changes. C-31 and C-32 phrasings are unchanged from R9-V-03 — single-axis test.

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
exclusions with validity), measurement thresholds established. No inertia competitor named
here — that belongs to CALIBRATE. [If PARTIAL: "[element] absent."]**

---

## CONTAINER: CALIBRATE
*Phase 4 only. Execute after CONTAINER: DESIGN gate is present in your output. Execute
before entering CONTAINER: BUILD.*
*This container has exactly three single-function responsibilities and no others:*
*(1) Identify the inertia competitor — the status-quo approach the prototype is challenging.*
*(2) Measure B-00 — what the inertia competitor produces on the Phase 3 metric, committed
    before any build activity begins.*
*(3) State the outperform threshold — what the prototype must produce relative to B-00 to
    confirm the hypothesis.*
*No scope definition, hypothesis activity, build steps, or experimental measurement belongs
here. A scan of this container alone must confirm all three responsibilities are discharged.*

### Role in this container

| Role | Writes | Must NOT Write |
|------|--------|----------------|
| CALIBRATOR | Inertia competitor name and identification; B-00 measurement on Phase 3 metric; explicit statement that prototype must exceed B-00 to confirm the hypothesis | Prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims about the prototype |

---

### Phase 4 — CALIBRATOR: Discharge all three CALIBRATE responsibilities
*Execute before entering CONTAINER: BUILD. Execute after Phase 3 gate is present in your
output.*

Discharge all three container responsibilities in this phase:

**(1) Identify the inertia competitor.** Name the current approach the prototype challenges.
State in one sentence why it is the status-quo alternative — the approach that will remain
in use if the prototype fails.

**(2) Measure B-00.** Apply the Phase 3 metric to the inertia competitor. Record the
result. This is B-00 — committed before any prototype activity begins.

**(3) State the outperform threshold.** State explicitly what the prototype must produce
relative to B-00 to confirm the hypothesis. A result that matches or falls below B-00 does
not confirm the hypothesis.

> **Inertia competitor**: [name of current method, tool, or approach being displaced]
> **Why it is the status-quo**: [one sentence]
> **B-00 measurement**: [what the inertia competitor produces on the Phase 3 metric]
> **Outperform threshold**: The prototype must produce [predicted outcome] relative to
>   B-00 = [value]. Matching or underperforming B-00 does not confirm the hypothesis.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]"; B-00 = [value];
outperform threshold stated. [If PARTIAL: "[inertia competitor name | B-00 measurement |
outperform threshold] absent — CALIBRATE responsibility (1|2|3) not discharged."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor identified,
B-00 committed, outperform threshold stated. Exclusively pre-build inertia content.
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

## V-04 — Combined: C-31 + C-32 (Both Fixes Simultaneously on R9-V-03 Base)

**Axes**: C-31 explicit routing language (V-01) + C-32 embedded values in CALIBRATE COMPLETE
(V-02)
**Design hypothesis**: V-01 satisfies C-31 by adding routing destination language ("must NOT
appear in DESIGN — belongs exclusively in CALIBRATE") to the FRAMER prohibition in three
locations: the role table cell, the DESIGN container note, and the DESIGN COMPLETE confirmation.
V-02 satisfies C-32 by embedding the B-00 value and all three named elements with their committed
values in the CALIBRATE COMPLETE line. The two fixes operate on different structural dimensions:
V-01 acts on the FRAMER role header and DESIGN container; V-02 acts on the CALIBRATE COMPLETE
line. Combining them introduces no structural conflict. The hypothesis: both C-31 and C-32 can
be satisfied simultaneously without degrading any lower-numbered criteria.

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

## V-05 — Combined: C-31 + C-32 + C-30 (Maximum Ceiling)

**Axes**: C-31 explicit routing prohibition (V-01) + C-32 embedded values (V-02) + C-30
three-column results table (R9-V-02/V-04 form)
**Design hypothesis**: V-04 achieves C-31 and C-32 simultaneously. C-30 requires a structured
table with three columns — Predicted | Observed | B-00 Baseline — populated from prior phases,
in the results section. The table is independent of the FRAMER prohibition and CALIBRATE COMPLETE
changes in V-04; it operates exclusively in Phase 7 (CONTAINER: CLOSE). Adding it to V-04
introduces no structural regression. The three-column table also satisfies C-26 (baseline
comparison in a completion line) by construction through the table row, and satisfies C-12
(effect size quantified) by construction when all three columns carry values. The hypothesis:
C-30 can be added to V-04 without degrading C-31 or C-32, achieving the R10 ceiling of 232
points.

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

Populate the three-column results table. All three columns must be filled with values drawn
from prior phases — a missing column is a visible structural gap. Then provide delta rationale
in the immediately adjacent labeled block.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | B-00 Baseline (Phase 4) |
|--------|--------------------|--------------------|-------------------------|
| [metric name] | [threshold value] | [raw result] | [B-00 value] |

> **Delta vs. threshold**: [match or mismatch — how observed compares to success/failure threshold]
> **Delta vs. B-00**: [observed relative to inertia baseline — direction and magnitude]
> **Why the deltas are what they are**: [explanation — must address both comparisons]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value],
observed [value], B-00 [value]); delta rationale co-located. [If PARTIAL: "[predicted |
observed | B-00] column absent — structural gap in table."]**

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

## Scoring Predictions (v10 rubric, 232 pts)

| Variation | Key Changes vs R9-V-03 | C-31 | C-32 | C-30 | Expected Gain | Predicted Score |
|-----------|------------------------|------|------|------|---------------|-----------------|
| V-01 | Routing language in FRAMER prohibition | PASS | FAIL (labels only, no B-00 value) | FAIL | +C-31 pts | ~201 |
| V-02 | B-00 value embedded in CALIBRATE COMPLETE | FAIL (no routing text) | PASS | FAIL | +C-32 pts | ~201 |
| V-03 | Three-function CALIBRATE header | FAIL | FAIL | FAIL | cosmetic structure clarity | ~197 |
| V-04 | C-31 routing + C-32 embedded values | PASS | PASS | FAIL | +C-31 +C-32 | ~211 |
| V-05 | C-31 + C-32 + C-30 three-column table | PASS | PASS | PASS | +C-31 +C-32 +C-30 | ~225+ |

**Note on V-03**: The three-function header improves human readability of the lifecycle boundary
but does not add a scorable criterion unless it also carries the CALIBRATE COMPLETE value
embeddings from V-02. It is included as a single-axis structural clarity test; if it scores
higher than predicted, the implication is that the enumerated header influences how completely
the model fills in Phase 4 and the CALIBRATE COMPLETE line.

**R10 ceiling hypothesis**: V-05 attempts the full 232-point ceiling by combining C-31, C-32,
and C-30. The remaining open question is whether combining three changes simultaneously
introduces any regression in C-01 (hypothesis first) or C-19/C-20 (gate ordering). No
structural conflict is anticipated, but V-04 is the safer bet if regressions occur.
