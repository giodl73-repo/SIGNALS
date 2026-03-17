# Quest Variate — prove-prototype Round 15 (v14 rubric, 279 pts)

**Date**: 2026-03-15
**Rubric version**: v14 (adds C-38 and C-39; ceiling 267 → 279)

**R14 analysis**: V-04 (phase-level role declarations, mixed register) and V-01 (container-level tables, full imperative register) each contribute one new criterion under v14. V-04 alone = 267 + C-38 (+7) = 274, lacking C-39. V-01 alone = 267 + C-39 (+5) = 272, lacking C-38. Neither closes both gaps independently.

**R15 seed**: Combine V-04's phase-level inline role declarations (C-38: prohibition co-located at phase execution point) with V-01's hard modal operators throughout (C-39: MUST/FORBIDDEN/REQUIRED/PROHIBITED on every prohibition and gate marker) on the R14 base (C-35 manifest + C-36 terminal chain + C-37 forward-reference clauses). Expected: 267 + 7 + 5 = **279**.

**Variation axes selected**:

- **V-01**: R15 seed — phase-level inline role declarations (C-38) + hard modal operators throughout (C-39)
- **V-02**: Single-axis — **Lifecycle emphasis** (compressed phase bodies; phase-level hard modal maintained)
- **V-03**: Single-axis — **Inertia framing** (manifest-level competitor journey column + status annotations in CONTAINER COMPLETE lines)
- **V-04**: Single-axis — **Role sequence** (split CLOSE into COMPARATOR/AUDITOR at Phase 8/9 boundary)
- **V-05**: **Gap probe** — value flow ledger (phase-level data contract + R15 seed; retests R14 V-05 unincorporated signal under v14 ceiling)

| Variation | Axis | C-38 | C-39 | Expected |
|-----------|------|------|------|----------|
| V-01 | Phase-level declarations + hard modal (R15 seed) | PASS | PASS | 279 |
| V-02 | Lifecycle emphasis (compressed, phase-level hard modal) | PASS | PASS | 279 |
| V-03 | Inertia framing (manifest competitor journey) | PASS | PASS | 279 + gap |
| V-04 | Role sequence (split CLOSE: COMPARATOR + AUDITOR) | PASS | PASS | 279 |
| V-05 | Gap probe: value flow ledger | PASS | PASS | 279 + gap |

R15 ceiling target: **279 / 279**. Gap probes in V-03 and V-05 seek v15 signals.

---

## V-01 — R15 Seed: Phase-Level Declarations + Hard Modal Register

**Axis**: Phrasing register (C-39) + lifecycle phase-level co-location (C-38). R14 tested these axes separately: V-04 used phase-level declarations with mixed register (satisfies C-38, fails C-39); V-01 used container-level tables with full imperative register (satisfies C-39, fails C-38). R15 seed fuses both: every role prohibition is an inline phase-header declaration using MUST/FORBIDDEN; every gate marker uses REQUIRED/FORBIDDEN/PROHIBITED. No container-level role tables appear.

**Design hypothesis**: The fused structure closes both C-38 (phase-level co-location) and C-39 (hard modal throughout) simultaneously. All other criteria carry forward from the R14 base. Expected: 279.

---

```
You are running **prove-prototype** for Signal.

**Artifact**: `simulations/prove/investigations/{topic}-prototype-{date}.md`
**Topic**: [Topic]
**Signal**: [Signal]

---

**PREREQUISITE — REQUIRED before any output**: Read the topic file. Identify the active
hypothesis. You MUST NOT begin Phase 1 until you have confirmed a hypothesis exists in the
topic file. If no hypothesis is locatable, HALT and output: "hypothesis absent — FORBIDDEN
to proceed."

---

## Output Contract

REQUIRED: This manifest MUST appear before any container body executes. REQUIRED: Execute
containers in the order listed. FORBIDDEN: No container MAY absorb work belonging to another.

| Container | Phases | Principal purpose | Expected output |
|-----------|--------|-------------------|-----------------|
| DESIGN | 1-3 | Lock hypothesis, bound prototype scope, freeze measurement criteria — inertia competitor identification is FORBIDDEN here | Hypothesis text, at least two validated exclusions with co-located validity rationale, success threshold, failure threshold |
| CALIBRATE | 4 | Identify inertia competitor, commit B-00, state outperform threshold — all pre-build. Scope and hypothesis activity are FORBIDDEN here | Named inertia competitor, B-00 value, outperform threshold |
| BUILD | 5-6 | Build the minimum prototype and record the raw measurement — comparison to B-00 and verdict are FORBIDDEN here | Prototype with minimality trade-off, raw result value |
| CLOSE | 7-11 | Compare, interpret, and close all open analytical questions — new measurement criteria are FORBIDDEN here | Three-column table with competitor-labeled baseline, verdict, counter-evidence disposition, limitation, replication path |

REQUIRED: The terminal CONTAINER: CLOSE COMPLETE line MUST encode results from all four
containers, not only the closing phase outcome.

---

## CONTAINER: DESIGN

REQUIRED: Complete all phases 1-3 before entering CONTAINER: CALIBRATE.
FORBIDDEN in this container: baseline measurement, inertia competitor identification, build
activity, raw results, result interpretation. VIOLATION CONTAMINATES CALIBRATE.

---

### Phase 1 — FRAMER (MUST write: hypothesis restatement; FORBIDDEN to write: baseline measurement, inertia competitor identification, build activity, raw results, interpretation)

*REQUIRED: Execute before Phase 2.*

You MUST write the hypothesis as the first substantive element of your output. REQUIRED:
Quote or closely paraphrase from the topic file. FORBIDDEN: No preamble, no context summary,
no prototype description, no result MUST appear before the hypothesis statement.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"hypothesis not locatable in topic file — HALT."]**

---

### Phase 2 — FRAMER (MUST write: scope exclusions each with co-located validity rationale; FORBIDDEN to write: inertia competitor identification [PROHIBITED — belongs exclusively in CALIBRATE], measurement criteria, build activity, results)

*REQUIRED: Execute before Phase 3. REQUIRED: Phase 1 COMPLETE gate MUST be present in output.*

You MUST state what the prototype will and will not do. REQUIRED: Name at least two explicit
exclusions. REQUIRED: For each exclusion, state immediately why the test remains valid without
it in the same labeled pair. FORBIDDEN: Exclusions without co-located validity rationale are
INVALID — do not produce them.

> **EXCLUDED**: [element]
> **WHY TEST REMAINS VALID**: [reason — REQUIRED in same labeled block]

> **EXCLUDED**: [element]
> **WHY TEST REMAINS VALID**: [reason — REQUIRED in same labeled block]

**PHASE 2 COMPLETE — [FULL|PARTIAL]: scope established; [N] exclusions with co-located
validity rationale. [If PARTIAL: "fewer than two paired exclusions — [element] absent."]**

---

### Phase 3 — FRAMER (MUST write: metric name, success threshold, failure threshold; FORBIDDEN to write: baseline measurement, inertia competitor identification, build steps, experimental results)

*REQUIRED: Execute before CONTAINER: CALIBRATE. REQUIRED: Phase 2 COMPLETE gate MUST be
present in output.*

REQUIRED: State what will be measured. REQUIRED: State the success threshold (CONFIRMS
hypothesis). REQUIRED: State the failure threshold (REFUTES hypothesis). REQUIRED: These
criteria are FROZEN at this gate — FORBIDDEN to change in any subsequent container.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: metric = "[name]"; success = [threshold]; failure =
[threshold]. [If PARTIAL: "[success|failure] threshold absent."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis = "[text]", scope = [N] validated
exclusions, success threshold = [value], failure threshold = [value]. Inertia competitor
identification is FORBIDDEN in this container — REQUIRED to appear exclusively in CALIBRATE.
[If PARTIAL: "[element] absent."]
→ [CALIBRATE] receives: hypothesis = "[text]", metric = "[name]", success threshold = [value],
failure threshold = [value].**

---

## CONTAINER: CALIBRATE

REQUIRED: Execute after CONTAINER: DESIGN COMPLETE gate is present in output.
REQUIRED: Complete Phase 4 before entering CONTAINER: BUILD.
FORBIDDEN in this container: scope definition, hypothesis activity, build steps, experimental
measurement.
REQUIRED: Discharge all three responsibilities in order before entering BUILD.

---

### Phase 4 — CALIBRATOR (MUST write: inertia competitor name and status-quo rationale, B-00 on Phase 3 metric, explicit outperform threshold; FORBIDDEN to write: prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims about the prototype)

*REQUIRED: Execute before CONTAINER: BUILD. REQUIRED: Phase 3 COMPLETE gate MUST be present
in output.*

REQUIRED: Discharge responsibilities 1, 2, and 3 in the declared order:

**(1) IDENTIFY the inertia competitor.** REQUIRED: Name the status-quo approach the prototype
challenges. REQUIRED: State in one sentence why it is the approach that remains in use if
the prototype fails.

**(2) MEASURE B-00.** REQUIRED: Apply the Phase 3 metric to the inertia competitor. REQUIRED:
Record as B-00. FORBIDDEN: B-00 MUST NOT be revised after this point.

**(3) STATE the outperform threshold.** REQUIRED: State explicitly what the prototype MUST
produce relative to B-00. FORBIDDEN: A result matching or falling below B-00 does NOT
confirm the hypothesis — REQUIRED to state this condition explicitly.

> **INERTIA COMPETITOR**: [name — REQUIRED]
> **WHY IT IS STATUS-QUO**: [one sentence — REQUIRED]
> **B-00**: [what the inertia competitor produces on the Phase 3 metric — REQUIRED]
> **OUTPERFORM THRESHOLD**: Prototype MUST produce [outcome] relative to B-00 = [value].
>   FORBIDDEN: Matching or underperforming B-00 does NOT confirm the hypothesis.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: (1) inertia competitor = "[name]"; (2) B-00 = [value];
(3) outperform threshold stated. [If PARTIAL: "responsibility ([1|2|3]) not discharged."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]", B-00 = [value],
outperform threshold = prototype MUST [condition] relative to B-00. Exclusively pre-build
inertia content. [If PARTIAL: "responsibility ([1|2|3]) not discharged."]
→ [BUILD] receives: inertia competitor = "[name]", B-00 = [value], metric = "[name from
Phase 3]", outperform threshold = [condition].**

---

## CONTAINER: BUILD

REQUIRED: Execute after CONTAINER: CALIBRATE COMPLETE gate is present in output.
REQUIRED: Complete phases 5-6 before entering CONTAINER: CLOSE.
FORBIDDEN in this container: comparison to B-00, result interpretation, verdict, new
measurement criteria.

---

### Phase 5 — BUILDER (MUST write: prototype description, build steps, minimality trade-off with co-located rationale, replication path; FORBIDDEN to write: comparison to B-00 or inertia competitor, result interpretation, verdict)

*REQUIRED: Execute before Phase 6. REQUIRED: Phase 4 COMPLETE gate MUST be present in output.*

REQUIRED: Describe or implement the prototype. REQUIRED: Include ONLY what is necessary to
test the hypothesis. REQUIRED: State what was left out and why in the same block. REQUIRED:
Include all tools, inputs, commands, and steps required to reproduce — FORBIDDEN: no implicit
steps.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [absent element] not specified]. [If PARTIAL:
"[element] absent."]**

---

### Phase 6 — RECORDER (MUST write: raw measurement on Phase 3 metric only; FORBIDDEN to write: interpretation, comparison to B-00, comparison to inertia competitor, verdict)

*REQUIRED: Execute before CONTAINER: CLOSE. REQUIRED: Phase 5 COMPLETE gate MUST be present
in output.*

REQUIRED: Apply the Phase 3 metric to the prototype. REQUIRED: Record the raw result ONLY.
FORBIDDEN: Comparison to B-00 or the inertia competitor — REQUIRED to appear exclusively in
CONTAINER: CLOSE.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value]. [If PARTIAL:
"measurement not applicable — [element] absent."]**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built and measured; raw result = [value];
B-00 = [Phase 4 value] for "[inertia competitor]". [If PARTIAL: "[element] absent."]
→ [CLOSE] receives: raw result = [value], B-00 = [value], inertia competitor = "[name]",
metric = "[name]".**

---

## CONTAINER: CLOSE

REQUIRED: Execute after CONTAINER: BUILD COMPLETE gate is present in output.
REQUIRED: Every phase MUST carry an explicit PREREQUISITE gate marker in output.
FORBIDDEN in this container: new measurement criteria; inertia competitor framing not
established in Phase 4.

---

### Phase 7 — ANALYST (MUST write: three-column comparison table with competitor-labeled baseline, delta rationale for both comparisons co-located with table; FORBIDDEN to write: new measurement criteria, inertia competitor framing not established in Phase 4)

*REQUIRED: Execute before Phase 8. REQUIRED: Phase 6 COMPLETE gate MUST be present in output.*

REQUIRED: Populate the three-column results table. REQUIRED: Label the baseline column with
the inertia competitor's name — FORBIDDEN to use "B-00" or "Baseline" as the column label.
REQUIRED: All three columns MUST be populated with values from prior phases.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline ([inertia competitor name]) |
|--------|--------------------|--------------------|--------------------------------------|
| [metric] | [threshold] | [raw result] | [B-00 from Phase 4] |

REQUIRED: State delta rationale co-located with the table:
> **DELTA vs. threshold**: [match or mismatch — REQUIRED]
> **DELTA vs. B-00**: [direction and magnitude — REQUIRED]
> **WHY the deltas are what they are**: [explanation addressing BOTH comparisons — REQUIRED]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value], observed
[value], baseline ([competitor name]) [value]); delta rationale co-located. [If PARTIAL:
"[column] absent."]**

---

### Phase 8 — ANALYST (MUST write: hypothesis verdict grounded in Phases 6-7 including B-00 comparison; FORBIDDEN to write: verdict without evidentiary grounding, new measurement criteria, new competitor framing)

*REQUIRED: Execute before Phase 9. REQUIRED: Phase 7 COMPLETE gate MUST be present in output.*

REQUIRED: State whether the hypothesis is CONFIRMED, REFUTED, or INCONCLUSIVE. REQUIRED:
Ground the verdict in Phases 6-7 including the B-00 comparison. FORBIDDEN: A verdict without
evidentiary grounding is INVALID.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. [If PARTIAL: "verdict without evidentiary grounding — INVALID."]**

---

### Phase 9 — ANALYST (MUST write: explicit binary counter-evidence disposition — exactly one of: named counter-interpretation with evidence-grounded rebuttal, OR explicit statement that no plausible counter exists with stated reason; FORBIDDEN to write: open-ended counter-evidence section, verdict restatement without new reasoning)

*REQUIRED: Execute before Phase 10. REQUIRED: Phase 8 COMPLETE gate MUST be present in output.*

REQUIRED: Close with EXACTLY ONE of two dispositions — FORBIDDEN to produce any other form:
- **(a)** REQUIRED: Name the counter-interpretation. REQUIRED: Rebut it with evidence-grounded
  reasoning.
- **(b)** REQUIRED: State explicitly that no plausible counter-interpretation exists. REQUIRED:
  State the reason.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "no explicit disposition —
INVALID."]**

---

### Phase 10 — ANALYST (MUST write: one limitation and one specific actionable next step; FORBIDDEN to write: multiple limitations without designation, generic next steps)

*REQUIRED: Execute before Phase 11. REQUIRED: Phase 9 COMPLETE gate MUST be present in output.*

REQUIRED: State one limitation. REQUIRED: State one specific next step. FORBIDDEN: Generic
next steps ("investigate further") are INVALID — REQUIRED to be actionable and specific.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[limitation | next step] absent."]**

---

### Phase 11 — ANALYST (MUST write: full replication path with all tools, inputs, commands, steps explicitly named; FORBIDDEN to write: implicit steps, assumed environment, unreferenced dependencies)

*REQUIRED: Phase 10 COMPLETE gate MUST be present in output.*

REQUIRED: List all tools, inputs, commands, and steps to reproduce. FORBIDDEN: Implicit
steps — if a step requires a tool or configuration not previously named, REQUIRED to name
it here.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete. [If PARTIAL: "[element]
not specified."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]:
[DESIGN] hypothesis = "[text from Phase 1]";
[CALIBRATE] inertia competitor = "[name]", B-00 = [value], outperform threshold = [condition];
[BUILD] prototype result = [value], delta vs. B-00 = [direction and magnitude];
[CLOSE] verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], prototype conclusion = "[one sentence]",
counter-evidence = [ADDRESSED — "[interpretation]" rebutted | CLOSED — no plausible counter].
[If PARTIAL: "[absent element from which container] not encoded — audit chain incomplete."]**
```

---

## V-02 — Single Axis: Lifecycle Emphasis (Compressed, Phase-Level Hard Modal)

**Axis**: Lifecycle emphasis — reduce each phase body to minimum structural expression: one REQUIRED imperative sentence plus the completion-line template. Phase headers retain full inline role declarations with MUST/FORBIDDEN. Container headers retain REQUIRED/FORBIDDEN. Gate markers retain hard modal. No elaborated examples, no block-quote scaffolding, no multi-sentence instructions.

**Design hypothesis**: C-38 is satisfied by the phase-header declaration alone — the phase body need not re-elaborate the prohibition. C-39 is satisfied as long as every prohibition and gate marker uses hard modal regardless of body length. A fully compressed variant should reach 279 if criteria fire on structural presence (phase header + completion line) rather than instructional elaboration. Expected: 279.

---

```
You are running **prove-prototype** for Signal.

**Artifact**: `simulations/prove/investigations/{topic}-prototype-{date}.md`
**Topic**: [Topic]
**Signal**: [Signal]

---

**PREREQUISITE — REQUIRED before any output**: Read the topic file. Confirm a hypothesis
exists. FORBIDDEN to begin Phase 1 until confirmed. If absent, HALT: "hypothesis absent —
FORBIDDEN to proceed."

---

## Output Contract

REQUIRED: This manifest MUST appear before any container body executes. REQUIRED: Execute
containers in order. FORBIDDEN: No container MAY absorb work from another.

| Container | Phases | Principal purpose | Expected output |
|-----------|--------|-------------------|-----------------|
| DESIGN | 1-3 | Lock hypothesis, scope, and measurement criteria — competitor identification FORBIDDEN | Hypothesis text, validated exclusions with co-located rationale, success and failure thresholds |
| CALIBRATE | 4 | Identify competitor, commit B-00, state outperform threshold — all pre-build. FORBIDDEN: scope, hypothesis, build, measurement | Competitor name, B-00, outperform threshold |
| BUILD | 5-6 | Build minimum prototype and record raw measurement — comparison and verdict FORBIDDEN | Prototype with minimality trade-off, raw result |
| CLOSE | 7-11 | Compare, render verdict, close counter-evidence, record limitations and replication — new measurement criteria FORBIDDEN | Three-column table, verdict, counter disposition, limitation, replication |

REQUIRED: The terminal CONTAINER: CLOSE COMPLETE line MUST encode results from all four
containers.

---

## CONTAINER: DESIGN

REQUIRED: Complete phases 1-3 before entering CONTAINER: CALIBRATE.
FORBIDDEN: baseline measurement, competitor identification, build activity, results,
interpretation.

---

### Phase 1 — FRAMER (MUST write: hypothesis restatement; FORBIDDEN to write: baseline, competitor identification, build activity, results, interpretation)

*REQUIRED: Execute before Phase 2.*

REQUIRED: Write the hypothesis as the first substantive element of output, quoted or closely
paraphrased from the topic file.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]".**

---

### Phase 2 — FRAMER (MUST write: scope exclusions each with co-located validity rationale; FORBIDDEN to write: competitor identification [PROHIBITED — belongs in CALIBRATE], measurement criteria, build activity, results)

*REQUIRED: Execute before Phase 3. REQUIRED: Phase 1 COMPLETE gate MUST be present.*

REQUIRED: Name at least two explicit exclusions, each with co-located validity rationale in
the same labeled pair.

**PHASE 2 COMPLETE — [FULL|PARTIAL]: scope established; [N] exclusions with co-located
validity rationale. [If PARTIAL: "[element] absent."]**

---

### Phase 3 — FRAMER (MUST write: metric name, success threshold, failure threshold; FORBIDDEN to write: baseline, competitor identification, build steps, results)

*REQUIRED: Execute before CONTAINER: CALIBRATE. REQUIRED: Phase 2 COMPLETE gate MUST be
present.*

REQUIRED: State the metric, success threshold, and failure threshold. REQUIRED: Frozen at
this gate — FORBIDDEN to change in any subsequent container.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: metric = "[name]"; success = [threshold]; failure =
[threshold].**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis = "[text]", scope = [N] validated
exclusions, success threshold = [value], failure threshold = [value]. Competitor identification
FORBIDDEN here — REQUIRED in CALIBRATE. [If PARTIAL: "[element] absent."]
→ [CALIBRATE] receives: hypothesis = "[text]", metric = "[name]", success threshold = [value],
failure threshold = [value].**

---

## CONTAINER: CALIBRATE

REQUIRED: Execute after CONTAINER: DESIGN COMPLETE gate present.
REQUIRED: Complete Phase 4 before entering CONTAINER: BUILD.
FORBIDDEN: scope, hypothesis activity, build steps, measurement.

---

### Phase 4 — CALIBRATOR (MUST write: inertia competitor name and status-quo rationale, B-00 on Phase 3 metric, outperform threshold; FORBIDDEN to write: prototype description, scope, measurement changes, results, performance claims)

*REQUIRED: Execute before CONTAINER: BUILD. REQUIRED: Phase 3 COMPLETE gate MUST be present.*

REQUIRED: Discharge (1) inertia competitor name and status-quo rationale; (2) B-00 on Phase 3
metric; (3) outperform threshold relative to B-00. REQUIRED: In that order. FORBIDDEN: B-00
MUST NOT be revised after this point.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: (1) inertia competitor = "[name]"; (2) B-00 = [value];
(3) outperform threshold stated.**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]", B-00 = [value],
outperform threshold = [condition]. [If PARTIAL: "[responsibility] not discharged."]
→ [BUILD] receives: inertia competitor = "[name]", B-00 = [value], metric = "[name]",
outperform threshold = [condition].**

---

## CONTAINER: BUILD

REQUIRED: Execute after CONTAINER: CALIBRATE COMPLETE gate present.
REQUIRED: Complete phases 5-6 before entering CONTAINER: CLOSE.
FORBIDDEN: comparison to B-00, interpretation, verdict, new measurement criteria.

---

### Phase 5 — BUILDER (MUST write: prototype description, build steps, minimality trade-off with co-located rationale, replication path; FORBIDDEN to write: comparison to B-00, interpretation, verdict)

*REQUIRED: Execute before Phase 6. REQUIRED: Phase 4 COMPLETE gate MUST be present.*

REQUIRED: Describe or implement the prototype. REQUIRED: State what was left out and why in
the same block. REQUIRED: Include all steps to reproduce with no implicit steps.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [element] absent].**

---

### Phase 6 — RECORDER (MUST write: raw measurement on Phase 3 metric only; FORBIDDEN to write: interpretation, comparison to B-00 or competitor, verdict)

*REQUIRED: Execute before CONTAINER: CLOSE. REQUIRED: Phase 5 COMPLETE gate MUST be present.*

REQUIRED: Apply the Phase 3 metric. REQUIRED: Record the raw result only. FORBIDDEN:
Comparison to B-00 — REQUIRED to appear in CONTAINER: CLOSE.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value].**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built; raw result = [value]; B-00 =
[value] for "[inertia competitor]". [If PARTIAL: "[element] absent."]
→ [CLOSE] receives: raw result = [value], B-00 = [value], inertia competitor = "[name]",
metric = "[name]".**

---

## CONTAINER: CLOSE

REQUIRED: Execute after CONTAINER: BUILD COMPLETE gate present. REQUIRED: Every phase MUST
carry an explicit PREREQUISITE gate marker in output.
FORBIDDEN: new measurement criteria; competitor framing not established in Phase 4.

---

### Phase 7 — ANALYST (MUST write: three-column table with competitor-labeled baseline, delta rationale for both comparisons co-located; FORBIDDEN to write: new measurement criteria, competitor framing not from Phase 4)

*REQUIRED: Execute before Phase 8. REQUIRED: Phase 6 COMPLETE gate MUST be present.*

REQUIRED: Populate the three-column table. REQUIRED: Label the baseline column with the
inertia competitor's name. REQUIRED: State delta rationale co-located with the table.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline ([competitor name]) |
|--------|--------------------|--------------------|------------------------------|
| [metric] | [threshold] | [raw result] | [B-00] |

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value], observed
[value], baseline ([competitor]) [value]); delta rationale co-located.**

---

### Phase 8 — ANALYST (MUST write: verdict word grounded in Phases 6-7 including B-00 comparison; FORBIDDEN to write: ungrounded verdict, new measurement criteria)

*REQUIRED: Execute before Phase 9. REQUIRED: Phase 7 COMPLETE gate MUST be present.*

REQUIRED: State CONFIRMED, REFUTED, or INCONCLUSIVE. REQUIRED: Ground in Phases 6-7
including B-00. FORBIDDEN: Ungrounded verdict is INVALID.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference].**

---

### Phase 9 — ANALYST (MUST write: explicit binary counter-evidence disposition; FORBIDDEN to write: open-ended or unresolved counter-evidence section)

*REQUIRED: Execute before Phase 10. REQUIRED: Phase 8 COMPLETE gate MUST be present.*

REQUIRED: Close with exactly one disposition: (a) named counter-interpretation with
evidence-grounded rebuttal, or (b) explicit statement that no plausible counter exists with
reason. FORBIDDEN: Any other form.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]].**

---

### Phase 10 — ANALYST (MUST write: one limitation and one specific actionable next step; FORBIDDEN to write: generic next steps)

*REQUIRED: Execute before Phase 11. REQUIRED: Phase 9 COMPLETE gate MUST be present.*

REQUIRED: State one limitation. REQUIRED: State one specific next step. FORBIDDEN: Generic
next steps are INVALID.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded.**

---

### Phase 11 — ANALYST (MUST write: full replication path with all tools, inputs, commands, steps explicitly named; FORBIDDEN to write: implicit steps)

*REQUIRED: Phase 10 COMPLETE gate MUST be present.*

REQUIRED: List all tools, inputs, commands, and steps to reproduce. FORBIDDEN: Implicit
steps.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete.**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]:
[DESIGN] hypothesis = "[text from Phase 1]";
[CALIBRATE] inertia competitor = "[name]", B-00 = [value], outperform threshold = [condition];
[BUILD] prototype result = [value], delta vs. B-00 = [direction and magnitude];
[CLOSE] verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], prototype conclusion = "[one sentence]",
counter-evidence = [ADDRESSED — "[interpretation]" rebutted | CLOSED — no plausible counter].
[If PARTIAL: "[absent element from which container] not encoded — audit chain incomplete."]**
```

---

## V-03 — Single Axis: Inertia Framing (Manifest Competitor Journey Column)

**Axis**: Inertia framing — elevate the inertia competitor as a document-level structural concern tracked across all four containers. The manifest gains a "Competitor status" column. Each CONTAINER COMPLETE line carries a competitor-status annotation updating the lifecycle position: NOT YET IDENTIFIED (DESIGN) → IDENTIFIED AND COMMITTED (CALIBRATE) → REFERENCED (BUILD) → DISCHARGED (CLOSE). Phase-level hard modal declarations from V-01 are maintained throughout.

**Design hypothesis**: V-03 from R14 introduced the manifest-level competitor journey as a gap probe candidate for v14, but v14 incorporated C-38 and C-39 instead. With the v14 ceiling closed at 279 by the R15 seed, V-03 retests whether a "competitor lifecycle status column" constitutes a v15 gap signal — a fifth structural surface for competitor identification beyond C-29 (CALIBRATE body), C-32 (CALIBRATE COMPLETE triple), C-34 (results table column), and C-36 (arc record). The four-state journey (NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED) is distinct from all four existing surfaces: it spans all containers at the document manifest level rather than a single container or terminal line. Expected: 279 + possible v15 gap signal.

---

```
You are running **prove-prototype** for Signal.

**Artifact**: `simulations/prove/investigations/{topic}-prototype-{date}.md`
**Topic**: [Topic]
**Signal**: [Signal]

---

**PREREQUISITE — REQUIRED before any output**: Read the topic file. Identify the active
hypothesis. FORBIDDEN to begin Phase 1 until confirmed. If absent, HALT: "hypothesis absent —
FORBIDDEN to proceed."

---

## Output Contract

REQUIRED: This manifest MUST appear before any container body executes. REQUIRED: Execute
containers in order. FORBIDDEN: No container MAY absorb work from another.

| Container | Phases | Principal purpose | Expected output | Competitor status |
|-----------|--------|-------------------|-----------------|-------------------|
| DESIGN | 1-3 | Lock hypothesis, bound scope, freeze measurement criteria — competitor identification FORBIDDEN here | Hypothesis text, validated exclusions with co-located rationale, success threshold, failure threshold | NOT YET IDENTIFIED |
| CALIBRATE | 4 | Identify competitor, commit B-00, state outperform threshold — all pre-build. Scope and hypothesis FORBIDDEN | Named competitor, B-00, outperform threshold | IDENTIFIED AND COMMITTED |
| BUILD | 5-6 | Build minimum prototype and record raw measurement — comparison and verdict FORBIDDEN | Prototype with minimality trade-off, raw result | REFERENCED (B-00 committed pre-build) |
| CLOSE | 7-11 | Compare, render verdict, close counter-evidence, record limitations — new measurement criteria FORBIDDEN | Three-column table, verdict, counter disposition, limitation, replication | DISCHARGED (baseline column anchored to competitor name) |

REQUIRED: The terminal CONTAINER: CLOSE COMPLETE line MUST encode results from all four
containers and the full competitor lifecycle (NOT YET IDENTIFIED → DISCHARGED).

---

## CONTAINER: DESIGN

REQUIRED: Complete all phases 1-3 before entering CONTAINER: CALIBRATE.
FORBIDDEN in this container: baseline measurement, inertia competitor identification, build
activity, raw results, result interpretation. VIOLATION CONTAMINATES CALIBRATE.

---

### Phase 1 — FRAMER (MUST write: hypothesis restatement; FORBIDDEN to write: baseline measurement, inertia competitor identification [PROHIBITED — competitor status: NOT YET IDENTIFIED in this container], build activity, raw results, interpretation)

*REQUIRED: Execute before Phase 2.*

REQUIRED: Write the hypothesis as the first substantive element of your output. REQUIRED:
Quote or closely paraphrase from the topic file. FORBIDDEN: No preamble, no context summary,
no prototype description, no result MUST precede the hypothesis statement.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"hypothesis not locatable — HALT."]**

---

### Phase 2 — FRAMER (MUST write: scope exclusions each with co-located validity rationale; FORBIDDEN to write: inertia competitor identification [PROHIBITED — competitor status: NOT YET IDENTIFIED], measurement criteria, build activity, results)

*REQUIRED: Execute before Phase 3. REQUIRED: Phase 1 COMPLETE gate MUST be present.*

REQUIRED: Name at least two explicit exclusions. REQUIRED: For each, state immediately why
the test remains valid without it in the same labeled pair. FORBIDDEN: Exclusions without
co-located validity rationale are INVALID.

> **EXCLUDED**: [element]
> **WHY TEST REMAINS VALID**: [reason — REQUIRED in same labeled block]

> **EXCLUDED**: [element]
> **WHY TEST REMAINS VALID**: [reason — REQUIRED in same labeled block]

**PHASE 2 COMPLETE — [FULL|PARTIAL]: scope established; [N] exclusions with co-located
validity rationale. [If PARTIAL: "[element] absent."]**

---

### Phase 3 — FRAMER (MUST write: metric name, success threshold, failure threshold; FORBIDDEN to write: baseline, competitor identification [PROHIBITED — NOT YET IDENTIFIED], build steps, results)

*REQUIRED: Execute before CONTAINER: CALIBRATE. REQUIRED: Phase 2 COMPLETE gate MUST be
present.*

REQUIRED: State the metric, success threshold, and failure threshold. REQUIRED: Frozen at
this gate — FORBIDDEN to change in any subsequent container.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: metric = "[name]"; success = [threshold]; failure =
[threshold]. [If PARTIAL: "[threshold] absent."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis = "[text]", scope = [N] validated
exclusions, success threshold = [value], failure threshold = [value].
Competitor status at DESIGN: NOT YET IDENTIFIED — identification is FORBIDDEN here, REQUIRED
in CALIBRATE. [If PARTIAL: "[element] absent."]
→ [CALIBRATE] receives: hypothesis = "[text]", metric = "[name]", success threshold = [value],
failure threshold = [value]. Competitor status handed off as: NOT YET IDENTIFIED.**

---

## CONTAINER: CALIBRATE

REQUIRED: Execute after CONTAINER: DESIGN COMPLETE gate present.
REQUIRED: Complete Phase 4 before entering CONTAINER: BUILD.
FORBIDDEN: scope definition, hypothesis activity, build steps, experimental measurement.
REQUIRED: Competitor status transitions from NOT YET IDENTIFIED to IDENTIFIED AND COMMITTED
in this container.

---

### Phase 4 — CALIBRATOR (MUST write: inertia competitor name and status-quo rationale, B-00 on Phase 3 metric, explicit outperform threshold; FORBIDDEN to write: prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims)

*REQUIRED: Execute before CONTAINER: BUILD. REQUIRED: Phase 3 COMPLETE gate MUST be present.*

REQUIRED: Discharge responsibilities 1, 2, and 3 in the declared order:

**(1) IDENTIFY the inertia competitor.** REQUIRED: Name the status-quo approach. REQUIRED:
State in one sentence why it remains in use if the prototype fails. Competitor status
transitions to IDENTIFIED.

**(2) MEASURE B-00.** REQUIRED: Apply the Phase 3 metric to the inertia competitor. REQUIRED:
Record as B-00. FORBIDDEN: B-00 MUST NOT be revised after this point. Competitor status
transitions to IDENTIFIED AND COMMITTED.

**(3) STATE the outperform threshold.** REQUIRED: State what the prototype MUST produce
relative to B-00. FORBIDDEN: Matching or falling below B-00 does NOT confirm the
hypothesis — REQUIRED to state this condition explicitly.

> **INERTIA COMPETITOR**: [name — REQUIRED]
> **WHY IT IS STATUS-QUO**: [one sentence — REQUIRED]
> **B-00**: [what the inertia competitor produces on the Phase 3 metric — REQUIRED]
> **OUTPERFORM THRESHOLD**: Prototype MUST produce [outcome] relative to B-00 = [value].
>   FORBIDDEN: Matching or underperforming B-00 does NOT confirm the hypothesis.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: (1) inertia competitor = "[name]"; (2) B-00 = [value];
(3) outperform threshold stated. [If PARTIAL: "responsibility ([1|2|3]) not discharged."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]", B-00 = [value],
outperform threshold = prototype MUST [condition] relative to B-00. Exclusively pre-build
inertia content.
Competitor status at CALIBRATE: IDENTIFIED AND COMMITTED — B-00 committed before any build
activity. [If PARTIAL: "responsibility ([1|2|3]) not discharged."]
→ [BUILD] receives: inertia competitor = "[name]" [status: IDENTIFIED AND COMMITTED],
B-00 = [value], metric = "[name]", outperform threshold = [condition].**

---

## CONTAINER: BUILD

REQUIRED: Execute after CONTAINER: CALIBRATE COMPLETE gate present.
REQUIRED: Complete phases 5-6 before entering CONTAINER: CLOSE.
FORBIDDEN: comparison to B-00, result interpretation, verdict, new measurement criteria.
Competitor status in this container: REFERENCED — B-00 committed pre-build. FORBIDDEN to
re-measure or re-identify.

---

### Phase 5 — BUILDER (MUST write: prototype description, build steps, minimality trade-off with co-located rationale, replication path; FORBIDDEN to write: comparison to B-00 or competitor [status: REFERENCED — identification and B-00 are committed], interpretation, verdict)

*REQUIRED: Execute before Phase 6. REQUIRED: Phase 4 COMPLETE gate MUST be present.*

REQUIRED: Describe or implement the prototype. REQUIRED: Include ONLY what is necessary to
test the hypothesis. REQUIRED: State what was left out and why in the same block. REQUIRED:
Include all tools, inputs, commands, and steps to reproduce — FORBIDDEN: no implicit steps.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [element] absent]. [If PARTIAL: "[element]
absent."]**

---

### Phase 6 — RECORDER (MUST write: raw measurement on Phase 3 metric only; FORBIDDEN to write: interpretation, comparison to B-00 [PROHIBITED — competitor status: REFERENCED], comparison to competitor, verdict)

*REQUIRED: Execute before CONTAINER: CLOSE. REQUIRED: Phase 5 COMPLETE gate MUST be present.*

REQUIRED: Apply the Phase 3 metric to the prototype. REQUIRED: Record the raw result ONLY.
FORBIDDEN: Comparison to B-00 or competitor — REQUIRED to appear exclusively in CONTAINER:
CLOSE.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value]. [If PARTIAL:
"[element] absent."]**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built and measured; raw result = [value];
B-00 = [value] for "[inertia competitor]".
Competitor status at BUILD: REFERENCED — B-00 committed in CALIBRATE, discharge REQUIRED in
CLOSE. [If PARTIAL: "[element] absent."]
→ [CLOSE] receives: raw result = [value], B-00 = [value], inertia competitor = "[name]"
[status: REFERENCED — REQUIRED to discharge in CLOSE], metric = "[name]".**

---

## CONTAINER: CLOSE

REQUIRED: Execute after CONTAINER: BUILD COMPLETE gate present.
REQUIRED: Every phase MUST carry an explicit PREREQUISITE gate marker.
FORBIDDEN: new measurement criteria; competitor framing not established in Phase 4.
Competitor status in this container: DISCHARGED — baseline column REQUIRED to anchor to
competitor name.

---

### Phase 7 — ANALYST (MUST write: three-column comparison table with competitor-labeled baseline [competitor status transitions to DISCHARGED when column header anchors to competitor name], delta rationale for both comparisons co-located; FORBIDDEN to write: new measurement criteria, competitor framing not from Phase 4)

*REQUIRED: Execute before Phase 8. REQUIRED: Phase 6 COMPLETE gate MUST be present.*

REQUIRED: Populate the three-column results table. REQUIRED: Label the baseline column with
the inertia competitor's name — FORBIDDEN to use "B-00" or "Baseline." Competitor status
transitions to DISCHARGED when the column header anchors to the competitor name. REQUIRED:
All three columns MUST be populated with values from prior phases.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline ([inertia competitor name]) |
|--------|--------------------|--------------------|--------------------------------------|
| [metric] | [threshold] | [raw result] | [B-00 from Phase 4] |

REQUIRED: State delta rationale co-located:
> **DELTA vs. threshold**: [match or mismatch — REQUIRED]
> **DELTA vs. B-00**: [direction and magnitude — REQUIRED]
> **WHY the deltas are what they are**: [explanation — both comparisons — REQUIRED]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated; competitor status:
DISCHARGED — baseline column anchored to "[competitor name]". [If PARTIAL: "[column] absent."]**

---

### Phase 8 — ANALYST (MUST write: verdict grounded in Phases 6-7 including B-00 comparison; FORBIDDEN to write: ungrounded verdict, new measurement criteria)

*REQUIRED: Execute before Phase 9. REQUIRED: Phase 7 COMPLETE gate MUST be present.*

REQUIRED: State CONFIRMED, REFUTED, or INCONCLUSIVE. REQUIRED: Ground the verdict in
Phases 6-7 including the B-00 comparison. FORBIDDEN: Ungrounded verdict is INVALID.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. [If PARTIAL: "verdict ungrounded — INVALID."]**

---

### Phase 9 — ANALYST (MUST write: explicit binary counter-evidence disposition; FORBIDDEN to write: open-ended counter-evidence section)

*REQUIRED: Execute before Phase 10. REQUIRED: Phase 8 COMPLETE gate MUST be present.*

REQUIRED: Close with exactly one disposition: (a) named counter-interpretation with
evidence-grounded rebuttal, or (b) explicit statement that no plausible counter exists with
reason. FORBIDDEN: Any other form.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "no explicit disposition —
INVALID."]**

---

### Phase 10 — ANALYST (MUST write: one limitation and one specific actionable next step; FORBIDDEN to write: generic next steps)

*REQUIRED: Execute before Phase 11. REQUIRED: Phase 9 COMPLETE gate MUST be present.*

REQUIRED: State one limitation. REQUIRED: State one specific next step. FORBIDDEN: Generic
next steps are INVALID.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[element] absent."]**

---

### Phase 11 — ANALYST (MUST write: full replication path; FORBIDDEN to write: implicit steps)

*REQUIRED: Phase 10 COMPLETE gate MUST be present.*

REQUIRED: List all tools, inputs, commands, and steps to reproduce. FORBIDDEN: Implicit
steps.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete. [If PARTIAL: "[element]
absent."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]:
[DESIGN] hypothesis = "[text from Phase 1]" [competitor status at DESIGN: NOT YET IDENTIFIED];
[CALIBRATE] inertia competitor = "[name]" [IDENTIFIED AND COMMITTED], B-00 = [value],
outperform threshold = [condition];
[BUILD] prototype result = [value], delta vs. B-00 = [direction and magnitude]
[competitor status at BUILD: REFERENCED];
[CLOSE] verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], prototype conclusion = "[one sentence]",
counter-evidence = [ADDRESSED — "[interpretation]" rebutted | CLOSED — no plausible counter],
competitor status: DISCHARGED — baseline column anchored to "[competitor name]".
[If PARTIAL: "[absent element from which container] not encoded — audit chain incomplete."]**
```

---

## V-04 — Single Axis: Role Sequence (Split CLOSE Into COMPARATOR + AUDITOR)

**Axis**: Role sequence — split the ANALYST role in CONTAINER: CLOSE into two distinct roles with a hard boundary at the Phase 8/9 transition: COMPARATOR (Phases 7-8) handles quantitative comparison and verdict; AUDITOR (Phases 9-11) handles counter-evidence disposition, limitations, and replication path. Each role carries phase-level inline declarations with MUST/FORBIDDEN operators (C-38 + C-39 maintained). The CLOSE container header enumerates both roles and their phase scope.

**Design hypothesis**: ANALYST currently spans Phases 7-11 as a monolithic role covering both the quantitative verdict work (7-8) and the analytical closure work (9-11). Splitting at the verdict/counter-evidence boundary creates a new contamination guard: COMPARATOR is FORBIDDEN to write counter-evidence dispositions or replication content; AUDITOR is FORBIDDEN to write new measurement criteria, new comparison data, or verdict statements. Tests whether role proliferation within a single container — introducing a role-handoff marker inside CLOSE between phases 8 and 9 — creates a new scorable surface. The existing rubric checks prohibition existence (C-23), phase-level co-location (C-38), and hard modal register (C-39). Role proliferation satisfies all three but may probe a gap around explicit intra-container role handoffs. Expected: 279. Gap signal candidate: explicit phase-boundary handoff line inside a container.

---

```
You are running **prove-prototype** for Signal.

**Artifact**: `simulations/prove/investigations/{topic}-prototype-{date}.md`
**Topic**: [Topic]
**Signal**: [Signal]

---

**PREREQUISITE — REQUIRED before any output**: Read the topic file. Identify the active
hypothesis. FORBIDDEN to begin Phase 1 until confirmed. If absent, HALT: "hypothesis absent —
FORBIDDEN to proceed."

---

## Output Contract

REQUIRED: This manifest MUST appear before any container body executes. REQUIRED: Execute
containers in order. FORBIDDEN: No container MAY absorb work from another.

| Container | Phases | Principal purpose | Expected output |
|-----------|--------|-------------------|-----------------|
| DESIGN | 1-3 | Lock hypothesis, bound prototype scope, freeze measurement criteria — competitor identification FORBIDDEN here | Hypothesis text, validated exclusions with co-located rationale, success threshold, failure threshold |
| CALIBRATE | 4 | Identify competitor, commit B-00, state outperform threshold — all pre-build. Scope and hypothesis FORBIDDEN | Named competitor, B-00, outperform threshold |
| BUILD | 5-6 | Build minimum prototype and record raw measurement — comparison and verdict FORBIDDEN | Prototype with minimality trade-off, raw result |
| CLOSE | 7-11 | COMPARATOR (phases 7-8): compare and render verdict; AUDITOR (phases 9-11): close counter-evidence, record limitations, confirm replication — new measurement criteria FORBIDDEN | Three-column table, verdict, counter disposition, limitation, replication |

REQUIRED: The terminal CONTAINER: CLOSE COMPLETE line MUST encode results from all four
containers, not only the closing phase outcome.

---

## CONTAINER: DESIGN

REQUIRED: Complete all phases 1-3 before entering CONTAINER: CALIBRATE.
FORBIDDEN in this container: baseline measurement, competitor identification, build activity,
raw results, interpretation. VIOLATION CONTAMINATES CALIBRATE.

---

### Phase 1 — FRAMER (MUST write: hypothesis restatement; FORBIDDEN to write: baseline, competitor identification, build activity, results, interpretation)

*REQUIRED: Execute before Phase 2.*

REQUIRED: Write the hypothesis as the first substantive element of your output. REQUIRED:
Quote or closely paraphrase from the topic file. FORBIDDEN: No preamble, no context summary,
no prototype description, no result MUST precede the hypothesis statement.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"hypothesis not locatable — HALT."]**

---

### Phase 2 — FRAMER (MUST write: scope exclusions each with co-located validity rationale; FORBIDDEN to write: competitor identification [PROHIBITED — belongs in CALIBRATE], measurement criteria, build activity, results)

*REQUIRED: Execute before Phase 3. REQUIRED: Phase 1 COMPLETE gate MUST be present.*

REQUIRED: Name at least two explicit exclusions. REQUIRED: For each, state immediately why
the test remains valid without it in the same labeled pair. FORBIDDEN: Exclusions without
co-located rationale are INVALID.

> **EXCLUDED**: [element]
> **WHY TEST REMAINS VALID**: [reason — REQUIRED in same labeled block]

> **EXCLUDED**: [element]
> **WHY TEST REMAINS VALID**: [reason — REQUIRED in same labeled block]

**PHASE 2 COMPLETE — [FULL|PARTIAL]: scope established; [N] exclusions with co-located
validity rationale. [If PARTIAL: "[element] absent."]**

---

### Phase 3 — FRAMER (MUST write: metric name, success threshold, failure threshold; FORBIDDEN to write: baseline, competitor identification, build steps, results)

*REQUIRED: Execute before CONTAINER: CALIBRATE. REQUIRED: Phase 2 COMPLETE gate MUST be
present.*

REQUIRED: State the metric, success threshold, and failure threshold. REQUIRED: Frozen at
this gate — FORBIDDEN to change in any subsequent container.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: metric = "[name]"; success = [threshold]; failure =
[threshold]. [If PARTIAL: "[threshold] absent."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis = "[text]", scope = [N] validated
exclusions, success threshold = [value], failure threshold = [value]. Competitor identification
FORBIDDEN here — REQUIRED in CALIBRATE. [If PARTIAL: "[element] absent."]
→ [CALIBRATE] receives: hypothesis = "[text]", metric = "[name]", success threshold = [value],
failure threshold = [value].**

---

## CONTAINER: CALIBRATE

REQUIRED: Execute after CONTAINER: DESIGN COMPLETE gate present.
REQUIRED: Complete Phase 4 before entering CONTAINER: BUILD.
FORBIDDEN: scope, hypothesis activity, build steps, measurement.

---

### Phase 4 — CALIBRATOR (MUST write: inertia competitor name and status-quo rationale, B-00 on Phase 3 metric, explicit outperform threshold; FORBIDDEN to write: prototype description, scope, measurement changes, results, performance claims)

*REQUIRED: Execute before CONTAINER: BUILD. REQUIRED: Phase 3 COMPLETE gate MUST be present.*

REQUIRED: Discharge responsibilities 1, 2, and 3 in the declared order:

**(1) IDENTIFY the inertia competitor.** REQUIRED: Name the status-quo approach. REQUIRED:
State in one sentence why it remains in use if the prototype fails.

**(2) MEASURE B-00.** REQUIRED: Apply the Phase 3 metric to the inertia competitor. REQUIRED:
Record as B-00. FORBIDDEN: B-00 MUST NOT be revised after this point.

**(3) STATE the outperform threshold.** REQUIRED: State what the prototype MUST produce
relative to B-00. FORBIDDEN: Matching or falling below B-00 does NOT confirm the hypothesis.

> **INERTIA COMPETITOR**: [name — REQUIRED]
> **WHY IT IS STATUS-QUO**: [one sentence — REQUIRED]
> **B-00**: [value on Phase 3 metric — REQUIRED]
> **OUTPERFORM THRESHOLD**: Prototype MUST produce [outcome] relative to B-00 = [value].
>   FORBIDDEN: Matching or underperforming B-00 does NOT confirm the hypothesis.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: (1) inertia competitor = "[name]"; (2) B-00 = [value];
(3) outperform threshold stated. [If PARTIAL: "responsibility ([1|2|3]) not discharged."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]", B-00 = [value],
outperform threshold = prototype MUST [condition] relative to B-00. Exclusively pre-build
inertia content. [If PARTIAL: "responsibility ([1|2|3]) not discharged."]
→ [BUILD] receives: inertia competitor = "[name]", B-00 = [value], metric = "[name]",
outperform threshold = [condition].**

---

## CONTAINER: BUILD

REQUIRED: Execute after CONTAINER: CALIBRATE COMPLETE gate present.
REQUIRED: Complete phases 5-6 before entering CONTAINER: CLOSE.
FORBIDDEN: comparison to B-00, interpretation, verdict, new measurement criteria.

---

### Phase 5 — BUILDER (MUST write: prototype description, build steps, minimality trade-off with co-located rationale, replication path; FORBIDDEN to write: comparison to B-00 or competitor, interpretation, verdict)

*REQUIRED: Execute before Phase 6. REQUIRED: Phase 4 COMPLETE gate MUST be present.*

REQUIRED: Describe or implement the prototype. REQUIRED: Include ONLY what is necessary to
test the hypothesis. REQUIRED: State what was left out and why in the same block. REQUIRED:
Include all tools, inputs, commands, and steps to reproduce — FORBIDDEN: no implicit steps.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [element] absent]. [If PARTIAL: "[element]
absent."]**

---

### Phase 6 — RECORDER (MUST write: raw measurement on Phase 3 metric only; FORBIDDEN to write: interpretation, comparison to B-00 or competitor, verdict)

*REQUIRED: Execute before CONTAINER: CLOSE. REQUIRED: Phase 5 COMPLETE gate MUST be present.*

REQUIRED: Apply the Phase 3 metric to the prototype. REQUIRED: Record the raw result ONLY.
FORBIDDEN: Comparison to B-00 — REQUIRED to appear in CONTAINER: CLOSE.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value]. [If PARTIAL:
"[element] absent."]**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built and measured; raw result = [value];
B-00 = [value] for "[inertia competitor]". [If PARTIAL: "[element] absent."]
→ [CLOSE] receives: raw result = [value], B-00 = [value], inertia competitor = "[name]",
metric = "[name]".**

---

## CONTAINER: CLOSE

REQUIRED: Execute after CONTAINER: BUILD COMPLETE gate present.
REQUIRED: Every phase MUST carry an explicit PREREQUISITE gate marker.
FORBIDDEN: new measurement criteria; competitor framing not established in Phase 4.
REQUIRED: Two roles operate in strict sequence — COMPARATOR (phases 7-8) then AUDITOR
(phases 9-11). FORBIDDEN: COMPARATOR MUST NOT write counter-evidence, limitations, or
replication content. FORBIDDEN: AUDITOR MUST NOT write new measurement criteria, new
comparison data, or verdict.

---

### Phase 7 — COMPARATOR (MUST write: three-column comparison table with competitor-labeled baseline, delta rationale for both comparisons co-located; FORBIDDEN to write: counter-evidence disposition, limitations, replication content, new measurement criteria)

*REQUIRED: Execute before Phase 8. REQUIRED: Phase 6 COMPLETE gate MUST be present.*

REQUIRED: Populate the three-column results table. REQUIRED: Label the baseline column with
the inertia competitor's name — FORBIDDEN to use "B-00" or "Baseline." REQUIRED: All three
columns MUST be populated with values from prior phases.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline ([inertia competitor name]) |
|--------|--------------------|--------------------|--------------------------------------|
| [metric] | [threshold] | [raw result] | [B-00 from Phase 4] |

REQUIRED: State delta rationale co-located:
> **DELTA vs. threshold**: [match or mismatch — REQUIRED]
> **DELTA vs. B-00**: [direction and magnitude — REQUIRED]
> **WHY the deltas are what they are**: [explanation — both comparisons — REQUIRED]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value], observed
[value], baseline ([competitor]) [value]); delta rationale co-located. [If PARTIAL:
"[column] absent."]**

---

### Phase 8 — COMPARATOR (MUST write: verdict grounded in Phases 6-7 including B-00 comparison; FORBIDDEN to write: counter-evidence disposition, limitations, replication content, ungrounded verdict, new measurement criteria)

*REQUIRED: Execute before Phase 9. REQUIRED: Phase 7 COMPLETE gate MUST be present.*
*REQUIRED: COMPARATOR responsibilities discharge at this phase — REQUIRED handoff to AUDITOR
at Phase 9.*

REQUIRED: State CONFIRMED, REFUTED, or INCONCLUSIVE. REQUIRED: Ground the verdict in
Phases 6-7 including B-00. FORBIDDEN: Ungrounded verdict is INVALID. FORBIDDEN: Counter-
evidence work — REQUIRED to appear in Phase 9 under AUDITOR.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. COMPARATOR responsibilities discharged — REQUIRED handoff to
AUDITOR. [If PARTIAL: "verdict ungrounded — INVALID."]**

---

### Phase 9 — AUDITOR (MUST write: explicit binary counter-evidence disposition; FORBIDDEN to write: new verdict statements, new measurement criteria, new comparison data)

*REQUIRED: Execute before Phase 10. REQUIRED: Phase 8 COMPLETE gate MUST be present.*

REQUIRED: Close with exactly one disposition: (a) named counter-interpretation with
evidence-grounded rebuttal, or (b) explicit statement that no plausible counter exists with
reason. FORBIDDEN: Any other form. FORBIDDEN: Verdict re-entry — verdict is LOCKED at
Phase 8 COMPARATOR.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "no explicit disposition —
INVALID."]**

---

### Phase 10 — AUDITOR (MUST write: one limitation and one specific actionable next step; FORBIDDEN to write: generic next steps, new verdict, new measurement criteria)

*REQUIRED: Execute before Phase 11. REQUIRED: Phase 9 COMPLETE gate MUST be present.*

REQUIRED: State one limitation. REQUIRED: State one specific next step. FORBIDDEN: Generic
next steps are INVALID — REQUIRED to be actionable and specific.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[element] absent."]**

---

### Phase 11 — AUDITOR (MUST write: full replication path with all tools, inputs, commands, steps; FORBIDDEN to write: implicit steps, new verdict, new measurement criteria)

*REQUIRED: Phase 10 COMPLETE gate MUST be present.*

REQUIRED: List all tools, inputs, commands, and steps to reproduce. FORBIDDEN: Implicit
steps — REQUIRED to name all tools and configurations not previously stated.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete. [If PARTIAL: "[element]
absent."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]:
[DESIGN] hypothesis = "[text from Phase 1]";
[CALIBRATE] inertia competitor = "[name]", B-00 = [value], outperform threshold = [condition];
[BUILD] prototype result = [value], delta vs. B-00 = [direction and magnitude];
[CLOSE] COMPARATOR verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], prototype conclusion =
"[one sentence]"; AUDITOR counter-evidence = [ADDRESSED — "[interpretation]" rebutted |
CLOSED — no plausible counter].
[If PARTIAL: "[absent element from which container] not encoded — audit chain incomplete."]**
```

---

## V-05 — Gap Probe: Value Flow Ledger (R15 Seed + Phase-Level Data Contract)

**Axis**: Gap probe — add a standalone "Value Flow Ledger" section after the manifest that names every experimental value, the phase that produces it, and the phase that first consumes it. Phase-level hard modal declarations from V-01 are maintained throughout (C-38 + C-39). The CLOSE COMPLETE line appends "value ledger: FULLY DISCHARGED / PARTIAL — [N] values unresolved."

**Design hypothesis**: R14 V-05 introduced the value flow ledger as a gap probe and was identified as a v14 candidate, but v14 incorporated C-38 and C-39 instead. The value flow ledger represents a structural layer between C-35 (container-level manifest, document granularity) and C-37 (completion-line forward-reference clauses, container granularity): the ledger operates at phase granularity — it names which specific phase produces each value and which specific phase first consumes it. This creates a third accountability surface for the value-flow family: document-level entry contract (C-35) → phase-level provenance contract (ledger) → container-level forward-reference (C-37). The terminal discharge confirmation at CLOSE COMPLETE creates a fourth surface: a ledger-specific audit line distinct from C-36 (full experimental arc record). With the v14 ceiling closed at 279, V-05 retests whether a phase-granularity value provenance contract is a genuinely new scorable surface for v15. Expected: 279 + possible v15 gap signal.

---

```
You are running **prove-prototype** for Signal.

**Artifact**: `simulations/prove/investigations/{topic}-prototype-{date}.md`
**Topic**: [Topic]
**Signal**: [Signal]

---

**PREREQUISITE — REQUIRED before any output**: Read the topic file. Identify the active
hypothesis. FORBIDDEN to begin Phase 1 until confirmed. If absent, HALT: "hypothesis absent —
FORBIDDEN to proceed."

---

## Output Contract

REQUIRED: This manifest MUST appear before any container body executes. REQUIRED: Execute
containers in order. FORBIDDEN: No container MAY absorb work from another.

| Container | Phases | Principal purpose | Expected output |
|-----------|--------|-------------------|-----------------|
| DESIGN | 1-3 | Lock hypothesis, bound prototype scope, freeze measurement criteria — competitor identification FORBIDDEN | Hypothesis text, validated exclusions with co-located rationale, success threshold, failure threshold |
| CALIBRATE | 4 | Identify competitor, commit B-00, state outperform threshold — all pre-build. Scope and hypothesis FORBIDDEN | Named competitor, B-00, outperform threshold |
| BUILD | 5-6 | Build minimum prototype and record raw measurement — comparison and verdict FORBIDDEN | Prototype with minimality trade-off, raw result |
| CLOSE | 7-11 | Compare, render verdict, close counter-evidence, record limitations and replication — new measurement criteria FORBIDDEN | Three-column table, verdict, counter disposition, limitation, replication |

REQUIRED: The terminal CONTAINER: CLOSE COMPLETE line MUST encode results from all four
containers and confirm that all value flow ledger entries were produced and consumed as
declared.

---

## Value Flow Ledger

REQUIRED: This ledger names every experimental value, the phase that produces it, and the
phase that first consumes it. REQUIRED: The CLOSE COMPLETE line MUST confirm ledger discharge
status. FORBIDDEN: Values declared in this ledger MUST NOT be used before the producing
phase executes.

| Value name | Produced by | First consumed by | Notes |
|------------|-------------|-------------------|-------|
| Hypothesis text | Phase 1 — FRAMER | Phase 3 (measurement validity) + CALIBRATE container entry | Anchor for scope validation |
| Scope exclusions with validity rationale | Phase 2 — FRAMER | Phase 3 (measurement validity check) | REQUIRED co-located at production point |
| Success threshold | Phase 3 — FRAMER | Phase 7 — ANALYST (Predicted column) | FROZEN at Phase 3 gate |
| Failure threshold | Phase 3 — FRAMER | Phase 8 — ANALYST (verdict grounding) | FROZEN at Phase 3 gate |
| Inertia competitor name | Phase 4 — CALIBRATOR | Phase 7 — ANALYST (baseline column label) | FORBIDDEN before Phase 4 |
| B-00 value | Phase 4 — CALIBRATOR | Phase 7 — ANALYST (baseline column value) + Phase 8 (verdict grounding) | COMMITTED at Phase 4 gate — FORBIDDEN to revise |
| Outperform threshold | Phase 4 — CALIBRATOR | Phase 8 — ANALYST (verdict grounding) | Relative to B-00 |
| Prototype description + minimality trade-off | Phase 5 — BUILDER | Phase 11 — ANALYST (replication path) | REQUIRED co-located at production point |
| Raw measurement result | Phase 6 — RECORDER | Phase 7 — ANALYST (Observed column) | FORBIDDEN: interpretation at production point |
| Delta rationale | Phase 7 — ANALYST | Phase 8 — ANALYST (verdict grounding) | Both comparisons REQUIRED |
| Verdict word | Phase 8 — ANALYST | CONTAINER: CLOSE COMPLETE (audit chain) | CONFIRMED, REFUTED, or INCONCLUSIVE |
| Counter-evidence disposition | Phase 9 — ANALYST | CONTAINER: CLOSE COMPLETE (audit chain) | Explicit binary — ADDRESSED or CLOSED |

---

## CONTAINER: DESIGN

REQUIRED: Complete all phases 1-3 before entering CONTAINER: CALIBRATE.
FORBIDDEN in this container: baseline measurement, competitor identification, build activity,
raw results, interpretation. VIOLATION CONTAMINATES CALIBRATE.

---

### Phase 1 — FRAMER (MUST write: hypothesis restatement [ledger: produces hypothesis text for Phase 3 + CALIBRATE entry]; FORBIDDEN to write: baseline, competitor identification, build activity, results, interpretation)

*REQUIRED: Execute before Phase 2.*

REQUIRED: Write the hypothesis as the first substantive element of your output. REQUIRED:
Quote or closely paraphrase from the topic file. FORBIDDEN: No preamble, no context summary,
no prototype description MUST precede the hypothesis statement.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]" [ledger value:
produced]. [If PARTIAL: "hypothesis not locatable — HALT."]**

---

### Phase 2 — FRAMER (MUST write: scope exclusions each with co-located validity rationale [ledger: produces scope exclusions for Phase 3]; FORBIDDEN to write: competitor identification [PROHIBITED — belongs in CALIBRATE], measurement criteria, build activity, results)

*REQUIRED: Execute before Phase 3. REQUIRED: Phase 1 COMPLETE gate MUST be present.*

REQUIRED: Name at least two explicit exclusions. REQUIRED: For each, state immediately why
the test remains valid without it in the same labeled pair. FORBIDDEN: Exclusions without
co-located validity rationale are INVALID.

> **EXCLUDED**: [element]
> **WHY TEST REMAINS VALID**: [reason — REQUIRED in same labeled block]

> **EXCLUDED**: [element]
> **WHY TEST REMAINS VALID**: [reason — REQUIRED in same labeled block]

**PHASE 2 COMPLETE — [FULL|PARTIAL]: scope established; [N] exclusions with co-located
validity rationale [ledger values: produced]. [If PARTIAL: "[element] absent."]**

---

### Phase 3 — FRAMER (MUST write: metric name, success threshold [ledger: produces for Phase 7], failure threshold [ledger: produces for Phase 8]; FORBIDDEN to write: baseline, competitor identification, build steps, results)

*REQUIRED: Execute before CONTAINER: CALIBRATE. REQUIRED: Phase 2 COMPLETE gate MUST be
present.*

REQUIRED: State the metric, success threshold, and failure threshold. REQUIRED: Frozen at
this gate — FORBIDDEN to change in any subsequent container.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: metric = "[name]"; success = [threshold] [ledger:
produced for Phase 7]; failure = [threshold] [ledger: produced for Phase 8]. [If PARTIAL:
"[threshold] absent."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis = "[text]", scope = [N] validated
exclusions, success threshold = [value], failure threshold = [value]. Competitor identification
FORBIDDEN here — REQUIRED in CALIBRATE. [If PARTIAL: "[element] absent."]
→ [CALIBRATE] receives: hypothesis = "[text]", metric = "[name]", success threshold = [value],
failure threshold = [value].**

---

## CONTAINER: CALIBRATE

REQUIRED: Execute after CONTAINER: DESIGN COMPLETE gate present.
REQUIRED: Complete Phase 4 before entering CONTAINER: BUILD.
FORBIDDEN: scope, hypothesis activity, build steps, measurement.

---

### Phase 4 — CALIBRATOR (MUST write: inertia competitor name [ledger: produces for Phase 7 baseline column label], B-00 [ledger: produces for Phase 7 value + Phase 8 grounding], outperform threshold [ledger: produces for Phase 8]; FORBIDDEN to write: prototype description, scope, measurement changes, results, performance claims)

*REQUIRED: Execute before CONTAINER: BUILD. REQUIRED: Phase 3 COMPLETE gate MUST be present.*

REQUIRED: Discharge responsibilities 1, 2, and 3 in the declared order:

**(1) IDENTIFY the inertia competitor.** REQUIRED: Name the status-quo approach. REQUIRED:
State in one sentence why it remains in use if the prototype fails.

**(2) MEASURE B-00.** REQUIRED: Apply the Phase 3 metric to the inertia competitor. REQUIRED:
Record as B-00. FORBIDDEN: B-00 MUST NOT be revised after this point.

**(3) STATE the outperform threshold.** REQUIRED: State what the prototype MUST produce
relative to B-00. FORBIDDEN: Matching or falling below B-00 does NOT confirm the hypothesis.

> **INERTIA COMPETITOR**: [name — REQUIRED]
> **WHY IT IS STATUS-QUO**: [one sentence — REQUIRED]
> **B-00**: [value on Phase 3 metric — REQUIRED]
> **OUTPERFORM THRESHOLD**: Prototype MUST produce [outcome] relative to B-00 = [value].
>   FORBIDDEN: Matching or underperforming B-00 does NOT confirm the hypothesis.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: (1) inertia competitor = "[name]" [ledger: produced];
(2) B-00 = [value] [ledger: produced, COMMITTED]; (3) outperform threshold [ledger:
produced]. [If PARTIAL: "responsibility ([1|2|3]) not discharged."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]", B-00 = [value],
outperform threshold = prototype MUST [condition] relative to B-00. Exclusively pre-build
inertia content. [If PARTIAL: "responsibility ([1|2|3]) not discharged."]
→ [BUILD] receives: inertia competitor = "[name]", B-00 = [value], metric = "[name]",
outperform threshold = [condition].**

---

## CONTAINER: BUILD

REQUIRED: Execute after CONTAINER: CALIBRATE COMPLETE gate present.
REQUIRED: Complete phases 5-6 before entering CONTAINER: CLOSE.
FORBIDDEN: comparison to B-00, interpretation, verdict, new measurement criteria.

---

### Phase 5 — BUILDER (MUST write: prototype description + minimality trade-off with co-located rationale [ledger: produces for Phase 11 replication], replication path; FORBIDDEN to write: comparison to B-00 or competitor, interpretation, verdict)

*REQUIRED: Execute before Phase 6. REQUIRED: Phase 4 COMPLETE gate MUST be present.*

REQUIRED: Describe or implement the prototype. REQUIRED: Include ONLY what is necessary to
test the hypothesis. REQUIRED: State what was left out and why in the same block. REQUIRED:
Include all tools, inputs, commands, and steps to reproduce — FORBIDDEN: no implicit steps.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded [ledger:
produced]; replication steps [all explicit | partial — [element] absent]. [If PARTIAL:
"[element] absent."]**

---

### Phase 6 — RECORDER (MUST write: raw measurement on Phase 3 metric only [ledger: produces raw result for Phase 7 Observed column]; FORBIDDEN to write: interpretation, comparison to B-00 or competitor, verdict)

*REQUIRED: Execute before CONTAINER: CLOSE. REQUIRED: Phase 5 COMPLETE gate MUST be present.*

REQUIRED: Apply the Phase 3 metric to the prototype. REQUIRED: Record the raw result ONLY.
FORBIDDEN: Comparison to B-00 — REQUIRED to appear in CONTAINER: CLOSE.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: raw result = [value] [ledger: produced for Phase 7].
[If PARTIAL: "[element] absent."]**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built; raw result = [value];
B-00 = [value] for "[inertia competitor]". [If PARTIAL: "[element] absent."]
→ [CLOSE] receives: raw result = [value], B-00 = [value], inertia competitor = "[name]",
metric = "[name]".**

---

## CONTAINER: CLOSE

REQUIRED: Execute after CONTAINER: BUILD COMPLETE gate present.
REQUIRED: Every phase MUST carry an explicit PREREQUISITE gate marker.
FORBIDDEN: new measurement criteria; competitor framing not established in Phase 4.

---

### Phase 7 — ANALYST (MUST write: three-column table [ledger: consumes success threshold from Phase 3 Predicted, raw result from Phase 6 Observed, B-00 from Phase 4 Baseline, competitor name from Phase 4 column label; produces delta rationale for Phase 8]; FORBIDDEN to write: new measurement criteria, competitor framing not from Phase 4)

*REQUIRED: Execute before Phase 8. REQUIRED: Phase 6 COMPLETE gate MUST be present.*

REQUIRED: Populate the three-column results table. REQUIRED: Label the baseline column with
the inertia competitor's name — FORBIDDEN to use "B-00" or "Baseline." REQUIRED: All three
columns MUST be populated with values from prior phases.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline ([inertia competitor name]) |
|--------|--------------------|--------------------|--------------------------------------|
| [metric] | [threshold] | [raw result] | [B-00 from Phase 4] |

REQUIRED: State delta rationale co-located [ledger: produces delta rationale]:
> **DELTA vs. threshold**: [match or mismatch — REQUIRED]
> **DELTA vs. B-00**: [direction and magnitude — REQUIRED]
> **WHY the deltas are what they are**: [explanation — both comparisons — REQUIRED]

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated; delta rationale co-located
[ledger values: consumed — competitor name, B-00, raw result, success threshold; delta
rationale produced for Phase 8]. [If PARTIAL: "[column] absent."]**

---

### Phase 8 — ANALYST (MUST write: verdict [ledger: consumes delta rationale from Phase 7, B-00 from Phase 4, failure threshold from Phase 3; produces verdict word for CLOSE COMPLETE]; FORBIDDEN to write: ungrounded verdict, new measurement criteria)

*REQUIRED: Execute before Phase 9. REQUIRED: Phase 7 COMPLETE gate MUST be present.*

REQUIRED: State CONFIRMED, REFUTED, or INCONCLUSIVE. REQUIRED: Ground the verdict in
Phases 6-7 including B-00 and failure threshold. FORBIDDEN: Ungrounded verdict is INVALID.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE] [ledger:
produced for CLOSE COMPLETE], grounded in [evidence reference]. [If PARTIAL: "verdict
ungrounded — INVALID."]**

---

### Phase 9 — ANALYST (MUST write: binary counter-evidence disposition [ledger: produces for CLOSE COMPLETE]; FORBIDDEN to write: open-ended counter-evidence section)

*REQUIRED: Execute before Phase 10. REQUIRED: Phase 8 COMPLETE gate MUST be present.*

REQUIRED: Close with exactly one disposition: (a) named counter-interpretation with
evidence-grounded rebuttal, or (b) explicit statement that no plausible counter exists with
reason. FORBIDDEN: Any other form.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]] [ledger: produced for CLOSE COMPLETE].
[If PARTIAL: "no explicit disposition — INVALID."]**

---

### Phase 10 — ANALYST (MUST write: one limitation and one specific actionable next step; FORBIDDEN to write: generic next steps)

*REQUIRED: Execute before Phase 11. REQUIRED: Phase 9 COMPLETE gate MUST be present.*

REQUIRED: State one limitation. REQUIRED: State one specific actionable next step. FORBIDDEN:
Generic next steps are INVALID.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded.**

---

### Phase 11 — ANALYST (MUST write: full replication path [ledger: consumes prototype description from Phase 5]; FORBIDDEN to write: implicit steps)

*REQUIRED: Phase 10 COMPLETE gate MUST be present.*

REQUIRED: List all tools, inputs, commands, and steps to reproduce. FORBIDDEN: Implicit
steps — REQUIRED to name all tools and configurations not previously stated.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete.**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]:
[DESIGN] hypothesis = "[text from Phase 1]";
[CALIBRATE] inertia competitor = "[name]", B-00 = [value], outperform threshold = [condition];
[BUILD] prototype result = [value], delta vs. B-00 = [direction and magnitude];
[CLOSE] verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], prototype conclusion = "[one sentence]",
counter-evidence = [ADDRESSED — "[interpretation]" rebutted | CLOSED — no plausible counter].
Value ledger: [FULLY DISCHARGED — all 12 values produced and consumed as declared |
PARTIAL — [N] values unresolved: [list]].
[If PARTIAL: "[absent element from which container] not encoded — audit chain incomplete."]**
```
