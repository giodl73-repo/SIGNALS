# Quest Variate — prove-prototype Round 16 (v15 rubric, 304 pts)

**Date**: 2026-03-15
**Rubric version**: v15 (adds C-40, C-41, C-42; ceiling 279 → 304)

**R15 analysis**: V-03 (manifest competitor lifecycle column), V-04 (CLOSE sub-role split
COMPARATOR/AUDITOR with Phase 8 handoff), and V-05 (Value Flow Ledger) each contributed a
new criterion under v15. V-03 alone = 279 + C-40 (+7) = 286. V-04 alone = 279 + C-41 (+8)
= 287. V-05 alone = 279 + C-42 (+10) = 289. None closes all three gaps independently.

**R16 seed**: Combine V-03's manifest competitor-status column (C-40) with V-04's
COMPARATOR/AUDITOR split and Phase 8 handoff (C-41) with V-05's Value Flow Ledger (C-42)
on the R15 base. Expected: 279 + 7 + 8 + 10 = **304**.

**Variation axes selected**:

- **V-01**: R16 seed — C-40 + C-41 + C-42 combined on R15 base (full elaboration)
- **V-02**: Single-axis — **Lifecycle emphasis** (compressed phase bodies; all three new criteria maintained at structural level)
- **V-03**: Single-axis — **Inertia framing** (C-40 competitor lifecycle elevated as primary document spine)
- **V-04**: Single-axis — **Role sequence** (C-41 COMPARATOR/AUDITOR split as primary CLOSE organizer)
- **V-05**: **Combination** — **Inertia framing + Role sequence** (C-40 + C-41 both elevated; C-42 maintained)

| Variation | Axis | C-40 | C-41 | C-42 | Expected |
|-----------|------|------|------|------|----------|
| V-01 | R16 seed: full combination (all three, elaborated) | PASS | PASS | PASS | 304 |
| V-02 | Lifecycle emphasis (compressed; structural presence only) | PASS | PASS | PASS | 304 |
| V-03 | Inertia framing (C-40 as primary spine) | PASS | PASS | PASS | 304 |
| V-04 | Role sequence (C-41 as primary CLOSE organizer) | PASS | PASS | PASS | 304 |
| V-05 | Combination: inertia framing + role sequence (C-40 + C-41 co-elevated) | PASS | PASS | PASS | 304 |

R16 ceiling target: **304 / 304**. All five variations incorporate the three new criteria;
axes explore which structural surface is elevated as primary vs. secondary.

---

## V-01 — R16 Seed: C-40 + C-41 + C-42 Combined

**Axis**: Full combination — all three R15 gap signals integrated on the R15 base with full
elaboration. Manifest adds competitor-status column tracking four-state progression (C-40).
Value Flow Ledger section appears after manifest and before any container body (C-42). CLOSE
container splits ANALYST into COMPARATOR (Phases 7-8) and AUDITOR (Phases 9-11) with
Phase 8 carrying an explicit handoff marker (C-41). All R15 features maintained: phase-level
inline role declarations (C-38), hard modal operators throughout (C-39), forward-reference
clauses on non-terminal CONTAINER COMPLETE lines (C-37), terminal arc record (C-36).

**Design hypothesis**: The fused structure closes C-40 (manifest competitor-status column
with CONTAINER COMPLETE annotations), C-41 (COMPARATOR/AUDITOR sub-role split with
model-written handoff), and C-42 (Value Flow Ledger with ledger-discharge confirmation at
CLOSE COMPLETE) simultaneously. All prior criteria carry forward from the R15 base. Expected:
304.

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
REQUIRED: The competitor-status column tracks four states across all container boundaries;
each CONTAINER COMPLETE line that advances competitor status MUST carry a status annotation.

| Container | Phases | Principal purpose | Expected output | Competitor status |
|-----------|--------|-------------------|-----------------|-------------------|
| DESIGN | 1-3 | Lock hypothesis, bound prototype scope, freeze measurement criteria — inertia competitor identification is FORBIDDEN here | Hypothesis text, at least two validated exclusions with co-located validity rationale, success threshold, failure threshold | NOT YET IDENTIFIED |
| CALIBRATE | 4 | Identify inertia competitor, commit B-00, state outperform threshold — all pre-build. Scope and hypothesis activity are FORBIDDEN here | Named inertia competitor, B-00 value, outperform threshold | IDENTIFIED AND COMMITTED |
| BUILD | 5-6 | Build the minimum prototype and record the raw measurement — comparison to B-00 and verdict are FORBIDDEN here | Prototype with minimality trade-off, raw result value | REFERENCED |
| CLOSE | 7-11 | Compare, interpret, and close all open analytical questions — new measurement criteria are FORBIDDEN here | Three-column table with competitor-labeled baseline, verdict, counter-evidence disposition, limitation, replication path | DISCHARGED |

REQUIRED: The terminal CONTAINER: CLOSE COMPLETE line MUST encode results from all four
containers, not only the closing phase outcome.

---

## Value Flow Ledger

REQUIRED: This section MUST appear after the manifest and before any container body executes.
REQUIRED: Produce the following ledger, filling in all value cells from your output as each
phase executes. REQUIRED: Every experimental value listed MUST appear; omitting any value
constitutes a ledger failure. FORBIDDEN: Any value MUST NOT be referenced in a phase earlier
than its producing phase — the no-anticipation property applies at the value level.

| Value | Producing phase | First consuming phase |
|-------|----------------|----------------------|
| Hypothesis text | Phase 1 (FRAMER) | Phase 8 (COMPARATOR — verdict grounding) |
| Scope exclusion(s) | Phase 2 (FRAMER) | Phase 5 (BUILDER — minimality trade-off) |
| Success threshold | Phase 3 (FRAMER) | Phase 7 (COMPARATOR — Predicted column) |
| Failure threshold | Phase 3 (FRAMER) | Phase 7 (COMPARATOR — Predicted column) |
| Inertia competitor name | Phase 4 (CALIBRATOR) | Phase 7 (COMPARATOR — Baseline column label) |
| B-00 | Phase 4 (CALIBRATOR) | Phase 7 (COMPARATOR — Baseline column value) |
| Outperform threshold | Phase 4 (CALIBRATOR) | Phase 8 (COMPARATOR — verdict grounding) |
| Prototype description | Phase 5 (BUILDER) | Phase 6 (RECORDER — measurement context) |
| Raw result | Phase 6 (RECORDER) | Phase 7 (COMPARATOR — Observed column) |
| Delta rationale | Phase 7 (COMPARATOR) | Phase 8 (COMPARATOR — verdict grounding) |
| Verdict word | Phase 8 (COMPARATOR) | CLOSE COMPLETE arc record |
| Counter-evidence disposition | Phase 9 (AUDITOR) | CLOSE COMPLETE arc record |

**VALUE FLOW LEDGER DECLARED — [N] values; no-anticipation constraint REQUIRED active
across all phases. Ledger discharge status will be confirmed at CONTAINER: CLOSE COMPLETE.**

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

REQUIRED: Name at least two explicit exclusions. REQUIRED: For each exclusion, state
immediately why the test remains valid without it in the same labeled pair. FORBIDDEN:
Exclusions without co-located validity rationale are INVALID — do not produce them.

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
Competitor status: NOT YET IDENTIFIED. [If PARTIAL: "[element] absent."]
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
inertia content. Competitor status: IDENTIFIED AND COMMITTED — "[name]" committed as B-00
baseline against Phase 3 metric. [If PARTIAL: "responsibility ([1|2|3]) not discharged."]
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
B-00 = [Phase 4 value] for "[inertia competitor]". Competitor status: REFERENCED — B-00 from
"[name]" carried as comparison baseline into CLOSE. [If PARTIAL: "[element] absent."]
→ [CLOSE] receives: raw result = [value], B-00 = [value], inertia competitor = "[name]",
metric = "[name]".**

---

## CONTAINER: CLOSE

REQUIRED: Execute after CONTAINER: BUILD COMPLETE gate is present in output.
REQUIRED: Every phase MUST carry an explicit PREREQUISITE gate marker in output.
FORBIDDEN in this container: new measurement criteria; inertia competitor framing not
established in Phase 4.

**CLOSE sub-role contract — REQUIRED: this contract MUST be declared before Phases 7-11
execute:**

| Sub-role | Phase scope | Writes | FORBIDDEN to write |
|----------|------------|--------|--------------------|
| COMPARATOR | Phases 7-8 | Quantitative comparison table, delta rationale, hypothesis verdict | Counter-evidence disposition, limitations content, replication content |
| AUDITOR | Phases 9-11 | Counter-evidence disposition, limitations, replication path | New measurement criteria, new comparison data, verdict statements |

REQUIRED: COMPARATOR responsibilities MUST be fully discharged before AUDITOR begins.
REQUIRED: Phase 8 COMPLETE line MUST carry an explicit handoff marker naming the transition.
FORBIDDEN: AUDITOR MUST NOT write any Phase 7-8 content; COMPARATOR MUST NOT write any
Phase 9-11 content.

---

### Phase 7 — COMPARATOR (MUST write: three-column comparison table with competitor-labeled baseline, delta rationale for both comparisons co-located with table; FORBIDDEN to write: counter-evidence disposition, limitations, replication content, new measurement criteria)

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

### Phase 8 — COMPARATOR (MUST write: hypothesis verdict grounded in Phases 6-7 including B-00 comparison; FORBIDDEN to write: counter-evidence disposition, limitations, replication content, verdict without evidentiary grounding, new measurement criteria)

*REQUIRED: Execute before Phase 9. REQUIRED: Phase 7 COMPLETE gate MUST be present in output.*

REQUIRED: State whether the hypothesis is CONFIRMED, REFUTED, or INCONCLUSIVE. REQUIRED:
Ground the verdict in Phases 6-7 including the B-00 comparison. FORBIDDEN: A verdict without
evidentiary grounding is INVALID. FORBIDDEN: Counter-evidence disposition — PROHIBITED,
belongs exclusively to AUDITOR in Phase 9.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR.
[If PARTIAL: "verdict without evidentiary grounding — INVALID."]**

---

### Phase 9 — AUDITOR (MUST write: explicit binary counter-evidence disposition — exactly one of: named counter-interpretation with evidence-grounded rebuttal, OR explicit statement that no plausible counter exists with stated reason; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, open-ended counter-evidence section)

*REQUIRED: Execute before Phase 10. REQUIRED: Phase 8 COMPLETE gate MUST be present in
output. REQUIRED: COMPARATOR handoff marker MUST be confirmed before executing.*

REQUIRED: Close with EXACTLY ONE of two dispositions — FORBIDDEN to produce any other form:
- **(a)** REQUIRED: Name the counter-interpretation. REQUIRED: Rebut it with evidence-grounded
  reasoning.
- **(b)** REQUIRED: State explicitly that no plausible counter-interpretation exists. REQUIRED:
  State the reason.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "no explicit disposition —
INVALID."]**

---

### Phase 10 — AUDITOR (MUST write: one limitation and one specific actionable next step; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, multiple limitations without designation, generic next steps)

*REQUIRED: Execute before Phase 11. REQUIRED: Phase 9 COMPLETE gate MUST be present in output.*

REQUIRED: State one limitation. REQUIRED: State one specific next step. FORBIDDEN: Generic
next steps ("investigate further") are INVALID — REQUIRED to be actionable and specific.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[limitation | next step] absent."]**

---

### Phase 11 — AUDITOR (MUST write: full replication path with all tools, inputs, commands, steps explicitly named; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, implicit steps, assumed environment)

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
Competitor status: DISCHARGED — "[name]" fully incorporated in results table baseline column
and terminal arc record.
Value ledger: [FULLY DISCHARGED | PARTIAL — [N] values unresolved].
[If PARTIAL: "[absent element from which container] not encoded — audit chain incomplete."]**
```

---

## V-02 — Single Axis: Lifecycle Emphasis (Compressed, All Three New Criteria)

**Axis**: Lifecycle emphasis — reduce each phase body to minimum structural expression: one
REQUIRED imperative sentence plus the completion-line template. Phase headers retain full
inline role declarations with MUST/FORBIDDEN (C-38). Container headers retain
REQUIRED/FORBIDDEN (C-39). Gate markers retain hard modal. Manifest retains
competitor-status column (C-40). Value Flow Ledger retains all rows (C-42). CLOSE sub-role
contract and Phase 8 handoff retained (C-41). No elaborated block-quote scaffolding, no
multi-sentence instructions, no labeled-pair examples.

**Design hypothesis**: C-40 fires on manifest column presence; C-41 fires on container-header
sub-role declaration and Phase 8 handoff marker; C-42 fires on ledger section presence and
CLOSE COMPLETE ledger-discharge line. None requires phase-body elaboration. A fully
compressed variant should reach 304 if all five criteria fire on structural presence
(manifest column, ledger table, container header declarations, completion-line markers)
rather than on instructional elaboration. Expected: 304.

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
containers in order. FORBIDDEN: No container MAY absorb work from another. REQUIRED: Each
CONTAINER COMPLETE line that advances competitor status MUST carry a status annotation.

| Container | Phases | Principal purpose | Expected output | Competitor status |
|-----------|--------|-------------------|-----------------|-------------------|
| DESIGN | 1-3 | Lock hypothesis, scope, measurement criteria — competitor identification FORBIDDEN | Hypothesis text, validated exclusions with co-located rationale, success and failure thresholds | NOT YET IDENTIFIED |
| CALIBRATE | 4 | Identify competitor, commit B-00, state outperform threshold — all pre-build. Scope, hypothesis, build, measurement FORBIDDEN | Competitor name, B-00, outperform threshold | IDENTIFIED AND COMMITTED |
| BUILD | 5-6 | Build minimum prototype, record raw measurement — comparison and verdict FORBIDDEN | Prototype with minimality trade-off, raw result | REFERENCED |
| CLOSE | 7-11 | Compare, render verdict, close counter-evidence, limitations, replication — new measurement criteria FORBIDDEN | Three-column table, verdict, counter disposition, limitation, replication | DISCHARGED |

REQUIRED: The terminal CONTAINER: CLOSE COMPLETE line MUST encode results from all four
containers.

---

## Value Flow Ledger

REQUIRED: Appear after manifest, before any container body. REQUIRED: All rows MUST be
populated as phases execute. FORBIDDEN: Any value MUST NOT be consumed before its producing
phase executes.

| Value | Producing phase | First consuming phase |
|-------|----------------|----------------------|
| Hypothesis text | Phase 1 | Phase 8 |
| Scope exclusion(s) | Phase 2 | Phase 5 |
| Success threshold | Phase 3 | Phase 7 |
| Failure threshold | Phase 3 | Phase 7 |
| Inertia competitor name | Phase 4 | Phase 7 |
| B-00 | Phase 4 | Phase 7 |
| Outperform threshold | Phase 4 | Phase 8 |
| Prototype description | Phase 5 | Phase 6 |
| Raw result | Phase 6 | Phase 7 |
| Delta rationale | Phase 7 | Phase 8 |
| Verdict word | Phase 8 | CLOSE COMPLETE |
| Counter-evidence disposition | Phase 9 | CLOSE COMPLETE |

**VALUE FLOW LEDGER DECLARED — [N] values; no-anticipation constraint REQUIRED active.**

---

## CONTAINER: DESIGN

REQUIRED: Complete phases 1-3 before entering CONTAINER: CALIBRATE.
FORBIDDEN: baseline measurement, competitor identification, build activity, results,
interpretation.

---

### Phase 1 — FRAMER (MUST write: hypothesis restatement; FORBIDDEN to write: baseline, competitor identification, build activity, results, interpretation)

*REQUIRED: Execute before Phase 2.*

REQUIRED: Write the hypothesis as the first substantive element of output, quoted or
closely paraphrased from the topic file.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]".**

---

### Phase 2 — FRAMER (MUST write: scope exclusions each with co-located validity rationale; FORBIDDEN to write: competitor identification [PROHIBITED — belongs in CALIBRATE], measurement criteria, build activity, results)

*REQUIRED: Execute before Phase 3. REQUIRED: Phase 1 COMPLETE gate MUST be present.*

REQUIRED: Name at least two explicit exclusions, each with co-located validity rationale
in the same labeled pair.

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
exclusions, success threshold = [value], failure threshold = [value]. Competitor
identification FORBIDDEN here — REQUIRED in CALIBRATE. Competitor status: NOT YET
IDENTIFIED. [If PARTIAL: "[element] absent."]
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

REQUIRED: Discharge (1) inertia competitor name and status-quo rationale; (2) B-00 on
Phase 3 metric; (3) outperform threshold relative to B-00. REQUIRED: In that order.
FORBIDDEN: B-00 MUST NOT be revised after this point.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: (1) inertia competitor = "[name]"; (2) B-00 = [value];
(3) outperform threshold stated.**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]", B-00 = [value],
outperform threshold = [condition]. Competitor status: IDENTIFIED AND COMMITTED — "[name]"
committed as B-00 baseline. [If PARTIAL: "[responsibility] not discharged."]
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

REQUIRED: Describe or implement the prototype, state what was left out and why in the same
block, and include all steps to reproduce with no implicit steps.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [element] absent].**

---

### Phase 6 — RECORDER (MUST write: raw measurement on Phase 3 metric only; FORBIDDEN to write: interpretation, comparison to B-00 or competitor, verdict)

*REQUIRED: Execute before CONTAINER: CLOSE. REQUIRED: Phase 5 COMPLETE gate MUST be present.*

REQUIRED: Apply the Phase 3 metric and record the raw result only. FORBIDDEN: Comparison
to B-00 — REQUIRED to appear in CONTAINER: CLOSE.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value].**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built; raw result = [value]; B-00 =
[value] for "[inertia competitor]". Competitor status: REFERENCED — B-00 from "[name]"
carried into CLOSE. [If PARTIAL: "[element] absent."]
→ [CLOSE] receives: raw result = [value], B-00 = [value], inertia competitor = "[name]",
metric = "[name]".**

---

## CONTAINER: CLOSE

REQUIRED: Execute after CONTAINER: BUILD COMPLETE gate present. REQUIRED: Every phase MUST
carry an explicit PREREQUISITE gate marker in output.
FORBIDDEN: new measurement criteria; competitor framing not established in Phase 4.

**CLOSE sub-role contract:**

| Sub-role | Phases | FORBIDDEN to write |
|----------|--------|--------------------|
| COMPARATOR | 7-8 | Counter-evidence disposition, limitations, replication content |
| AUDITOR | 9-11 | New measurement criteria, new comparison data, verdict statements |

REQUIRED: COMPARATOR MUST fully discharge before AUDITOR begins. REQUIRED: Phase 8
COMPLETE MUST carry an explicit handoff marker.

---

### Phase 7 — COMPARATOR (MUST write: three-column table with competitor-labeled baseline, delta rationale for both comparisons co-located; FORBIDDEN to write: counter-evidence disposition, limitations, replication content, new measurement criteria)

*REQUIRED: Execute before Phase 8. REQUIRED: Phase 6 COMPLETE gate MUST be present.*

REQUIRED: Populate the three-column table with competitor-labeled baseline. REQUIRED: State
delta rationale co-located with the table.

| Metric | Predicted (Phase 3) | Observed (Phase 6) | Baseline ([competitor name]) |
|--------|--------------------|--------------------|------------------------------|
| [metric] | [threshold] | [raw result] | [B-00] |

**PHASE 7 COMPLETE — [FULL|PARTIAL]: three-column table populated (predicted [value], observed
[value], baseline ([competitor]) [value]); delta rationale co-located.**

---

### Phase 8 — COMPARATOR (MUST write: verdict word grounded in Phases 6-7 including B-00 comparison; FORBIDDEN to write: counter-evidence disposition, limitations, replication content, ungrounded verdict, new measurement criteria)

*REQUIRED: Execute before Phase 9. REQUIRED: Phase 7 COMPLETE gate MUST be present.*

REQUIRED: State CONFIRMED, REFUTED, or INCONCLUSIVE grounded in Phases 6-7 including B-00.
FORBIDDEN: Ungrounded verdict is INVALID. FORBIDDEN: Counter-evidence — PROHIBITED in
COMPARATOR, belongs to AUDITOR.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. COMPARATOR responsibilities discharged — REQUIRED handoff to
AUDITOR. [If PARTIAL: "verdict ungrounded — INVALID."]**

---

### Phase 9 — AUDITOR (MUST write: explicit binary counter-evidence disposition; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, open-ended counter-evidence section)

*REQUIRED: Execute before Phase 10. REQUIRED: Phase 8 COMPLETE gate MUST be present.
REQUIRED: COMPARATOR handoff confirmed.*

REQUIRED: Close with exactly one disposition — (a) named counter with grounded rebuttal,
or (b) no plausible counter with stated reason. FORBIDDEN: Any other form.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED | CLOSED — reason: [reason]].**

---

### Phase 10 — AUDITOR (MUST write: one limitation and one specific actionable next step; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, generic next steps)

*REQUIRED: Execute before Phase 11. REQUIRED: Phase 9 COMPLETE gate MUST be present.*

REQUIRED: State one limitation and one specific actionable next step. FORBIDDEN: Generic.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded.**

---

### Phase 11 — AUDITOR (MUST write: full replication path with all tools, inputs, commands, steps explicitly named; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, implicit steps)

*REQUIRED: Phase 10 COMPLETE gate MUST be present.*

REQUIRED: List all tools, inputs, commands, steps. FORBIDDEN: Implicit steps.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete.**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]:
[DESIGN] hypothesis = "[text from Phase 1]";
[CALIBRATE] inertia competitor = "[name]", B-00 = [value], outperform threshold = [condition];
[BUILD] prototype result = [value], delta vs. B-00 = [direction and magnitude];
[CLOSE] verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], prototype conclusion = "[one sentence]",
counter-evidence = [ADDRESSED — "[interpretation]" rebutted | CLOSED — no plausible counter].
Competitor status: DISCHARGED — "[name]" incorporated in results table and arc record.
Value ledger: [FULLY DISCHARGED | PARTIAL — [N] values unresolved].
[If PARTIAL: "[absent element] not encoded — audit chain incomplete."]**
```

---

## V-03 — Single Axis: Inertia Framing (Competitor Lifecycle as Primary Structural Spine)

**Axis**: Inertia framing — elevate the competitor lifecycle as the document's primary
structural commentary. C-40 is the dominant design axis: the manifest's competitor-status
column is introduced with explicit framing explaining the four-state progression; each
CONTAINER COMPLETE line leads with the competitor status transition before the forward-
reference clause; container headers include explicit lifecycle expectations. C-41 and C-42
are maintained at full specification but subordinate to the lifecycle narrative. Phase-level
role declarations and hard modal operators maintained (C-38, C-39).

**Design hypothesis**: When C-40's competitor lifecycle is the dominant structural axis,
the manifest column and CONTAINER COMPLETE status annotations are more prominent — the
temporal competitor-accountability thread is the document's secondary narrative. C-41 and
C-42 structures are fully present but visually subordinate. Expected: 304.

---

```
You are running **prove-prototype** for Signal.

**Artifact**: `simulations/prove/investigations/{topic}-prototype-{date}.md`
**Topic**: [Topic]
**Signal**: [Signal]

---

**PREREQUISITE — REQUIRED before any output**: Read the topic file. Identify the active
hypothesis. You MUST NOT begin Phase 1 until confirmed. If absent, HALT: "hypothesis absent —
FORBIDDEN to proceed."

---

## Output Contract

REQUIRED: This manifest MUST appear before any container body executes. REQUIRED: Execute
containers in the order listed. FORBIDDEN: No container MAY absorb work belonging to another.

**Competitor lifecycle — REQUIRED reading before execution**: The inertia competitor does
not exist yet at DESIGN. It becomes real at CALIBRATE. It is referenced as a baseline at
BUILD. It is fully discharged at CLOSE. This four-state progression (NOT YET IDENTIFIED →
IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED) is the document's accountability thread
for the inertia competitor. REQUIRED: Each CONTAINER COMPLETE line that advances competitor
status MUST carry a status annotation recording the transition. FORBIDDEN: Competitor status
MUST NOT advance before the container whose manifest row carries the new status.

| Container | Phases | Principal purpose | Expected output | Competitor status |
|-----------|--------|-------------------|-----------------|-------------------|
| DESIGN | 1-3 | Lock hypothesis, bound scope, freeze measurement criteria | Hypothesis text, validated exclusions with co-located rationale, success threshold, failure threshold | NOT YET IDENTIFIED — competitor identification is FORBIDDEN in this container |
| CALIBRATE | 4 | Identify inertia competitor, commit B-00, state outperform threshold — all pre-build | Named competitor, B-00, outperform threshold | IDENTIFIED AND COMMITTED — competitor enters the document here and MUST NOT appear earlier |
| BUILD | 5-6 | Build minimum prototype, record raw measurement | Prototype with minimality trade-off, raw result | REFERENCED — B-00 committed in CALIBRATE is referenced as the comparison standard |
| CLOSE | 7-11 | Compare, interpret, close all analytical questions | Three-column table with competitor-labeled baseline, verdict, counter-evidence disposition, limitation, replication | DISCHARGED — competitor fully incorporated in baseline column label, results table, and arc record |

REQUIRED: The terminal CONTAINER: CLOSE COMPLETE line MUST encode results from all four
containers and confirm competitor status has reached DISCHARGED.

---

## Value Flow Ledger

REQUIRED: This section MUST appear after the manifest and before any container body executes.
REQUIRED: Every experimental value listed MUST appear in the ledger; omitting any value
constitutes a ledger failure. FORBIDDEN: Any value MUST NOT be consumed before its producing
phase executes.

| Value | Producing phase | First consuming phase |
|-------|----------------|----------------------|
| Hypothesis text | Phase 1 (FRAMER) | Phase 8 (COMPARATOR — verdict grounding) |
| Scope exclusion(s) | Phase 2 (FRAMER) | Phase 5 (BUILDER — minimality trade-off) |
| Success threshold | Phase 3 (FRAMER) | Phase 7 (COMPARATOR — Predicted column) |
| Failure threshold | Phase 3 (FRAMER) | Phase 7 (COMPARATOR — Predicted column) |
| Inertia competitor name | Phase 4 (CALIBRATOR) | Phase 7 (COMPARATOR — Baseline column label) |
| B-00 | Phase 4 (CALIBRATOR) | Phase 7 (COMPARATOR — Baseline column value) |
| Outperform threshold | Phase 4 (CALIBRATOR) | Phase 8 (COMPARATOR — verdict grounding) |
| Prototype description | Phase 5 (BUILDER) | Phase 6 (RECORDER — measurement context) |
| Raw result | Phase 6 (RECORDER) | Phase 7 (COMPARATOR — Observed column) |
| Delta rationale | Phase 7 (COMPARATOR) | Phase 8 (COMPARATOR — verdict grounding) |
| Verdict word | Phase 8 (COMPARATOR) | CLOSE COMPLETE arc record |
| Counter-evidence disposition | Phase 9 (AUDITOR) | CLOSE COMPLETE arc record |

**VALUE FLOW LEDGER DECLARED — [N] values; no-anticipation constraint REQUIRED active.**

---

## CONTAINER: DESIGN
*Competitor status entering: NOT YET IDENTIFIED*

REQUIRED: Complete all phases 1-3 before entering CONTAINER: CALIBRATE.
FORBIDDEN in this container: baseline measurement, inertia competitor identification [the
competitor does not exist yet — FORBIDDEN to name, infer, or reference any inertia
competitor here], build activity, raw results, result interpretation.

---

### Phase 1 — FRAMER (MUST write: hypothesis restatement; FORBIDDEN to write: baseline measurement, inertia competitor identification [PROHIBITED — competitor status: NOT YET IDENTIFIED], build activity, raw results, interpretation)

*REQUIRED: Execute before Phase 2.*

REQUIRED: Write the hypothesis as the first substantive element of output. REQUIRED: Quote
or closely paraphrase from the topic file. FORBIDDEN: No preamble, no prototype description,
no result MUST precede the hypothesis statement.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]". [If PARTIAL:
"hypothesis not locatable — HALT."]**

---

### Phase 2 — FRAMER (MUST write: scope exclusions each with co-located validity rationale; FORBIDDEN to write: inertia competitor identification [PROHIBITED — competitor status: NOT YET IDENTIFIED in this container], measurement criteria, build activity, results)

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

### Phase 3 — FRAMER (MUST write: metric name, success threshold, failure threshold; FORBIDDEN to write: baseline measurement, inertia competitor identification [PROHIBITED — NOT YET IDENTIFIED], build steps, experimental results)

*REQUIRED: Execute before CONTAINER: CALIBRATE. REQUIRED: Phase 2 COMPLETE gate MUST be
present.*

REQUIRED: State what will be measured, the success threshold, and the failure threshold.
REQUIRED: Frozen at this gate — FORBIDDEN to change in any subsequent container.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: metric = "[name]"; success = [threshold]; failure =
[threshold]. [If PARTIAL: "[threshold] absent."]**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis = "[text]", scope = [N] validated
exclusions, success threshold = [value], failure threshold = [value].
Competitor lifecycle — status at DESIGN exit: NOT YET IDENTIFIED. FORBIDDEN: Identification
MUST NOT occur before CALIBRATE.
[If PARTIAL: "[element] absent."]
→ [CALIBRATE] receives: hypothesis = "[text]", metric = "[name]", success threshold = [value],
failure threshold = [value]. Competitor lifecycle status handed off: NOT YET IDENTIFIED.**

---

## CONTAINER: CALIBRATE
*Competitor status entering: NOT YET IDENTIFIED — competitor first appears in this container*

REQUIRED: Execute after CONTAINER: DESIGN COMPLETE gate is present in output.
REQUIRED: Complete Phase 4 before entering CONTAINER: BUILD.
FORBIDDEN in this container: scope definition, hypothesis activity, build steps, experimental
measurement.
REQUIRED: Competitor status transitions from NOT YET IDENTIFIED to IDENTIFIED AND COMMITTED
before this container closes.

---

### Phase 4 — CALIBRATOR (MUST write: inertia competitor name and status-quo rationale, B-00 on Phase 3 metric, explicit outperform threshold; FORBIDDEN to write: prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims about the prototype)

*REQUIRED: Execute before CONTAINER: BUILD. REQUIRED: Phase 3 COMPLETE gate MUST be present.*

REQUIRED: Discharge responsibilities 1, 2, and 3 in the declared order:

**(1) IDENTIFY the inertia competitor** — competitor status transitions from NOT YET IDENTIFIED
to IDENTIFIED. REQUIRED: Name the status-quo approach the prototype challenges. REQUIRED:
State in one sentence why it remains in use if the prototype fails.

**(2) MEASURE B-00** — competitor status transitions to IDENTIFIED AND COMMITTED. REQUIRED:
Apply the Phase 3 metric to the inertia competitor. REQUIRED: Record as B-00. FORBIDDEN:
B-00 MUST NOT be revised after this point.

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
outperform threshold = prototype MUST [condition] relative to B-00.
Competitor lifecycle — status at CALIBRATE exit: IDENTIFIED AND COMMITTED — "[name]" named
and B-00 committed before any build activity begins.
[If PARTIAL: "responsibility ([1|2|3]) not discharged."]
→ [BUILD] receives: inertia competitor = "[name]" [lifecycle: IDENTIFIED AND COMMITTED],
B-00 = [value], metric = "[name]", outperform threshold = [condition].**

---

## CONTAINER: BUILD
*Competitor status entering: IDENTIFIED AND COMMITTED — B-00 committed in CALIBRATE*

REQUIRED: Execute after CONTAINER: CALIBRATE COMPLETE gate is present in output.
REQUIRED: Complete phases 5-6 before entering CONTAINER: CLOSE.
FORBIDDEN in this container: comparison to B-00, result interpretation, verdict, new
measurement criteria.

---

### Phase 5 — BUILDER (MUST write: prototype description, build steps, minimality trade-off with co-located rationale, replication path; FORBIDDEN to write: comparison to B-00 or inertia competitor, result interpretation, verdict)

*REQUIRED: Execute before Phase 6. REQUIRED: Phase 4 COMPLETE gate MUST be present.*

REQUIRED: Describe or implement the prototype. REQUIRED: Include ONLY what is necessary
to test the hypothesis. REQUIRED: State what was left out and why in the same block.
REQUIRED: Include all steps to reproduce — FORBIDDEN: no implicit steps.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [element] absent]. [If PARTIAL: "[element] absent."]**

---

### Phase 6 — RECORDER (MUST write: raw measurement on Phase 3 metric only; FORBIDDEN to write: interpretation, comparison to B-00, comparison to inertia competitor, verdict)

*REQUIRED: Execute before CONTAINER: CLOSE. REQUIRED: Phase 5 COMPLETE gate MUST be present.*

REQUIRED: Apply the Phase 3 metric. REQUIRED: Record the raw result ONLY. FORBIDDEN:
Comparison to B-00 — REQUIRED to appear exclusively in CONTAINER: CLOSE.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value]. [If PARTIAL:
"[element] absent."]**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built; raw result = [value]; B-00 =
[value] for "[inertia competitor]".
Competitor lifecycle — status at BUILD exit: REFERENCED — B-00 from "[name]" active as
comparison standard; verdict and discharge occur in CLOSE.
[If PARTIAL: "[element] absent."]
→ [CLOSE] receives: raw result = [value], B-00 = [value], inertia competitor = "[name]"
[lifecycle: REFERENCED], metric = "[name]".**

---

## CONTAINER: CLOSE
*Competitor status entering: REFERENCED — B-00 committed; competitor must reach DISCHARGED
before this container closes*

REQUIRED: Execute after CONTAINER: BUILD COMPLETE gate is present in output.
REQUIRED: Every phase MUST carry an explicit PREREQUISITE gate marker in output.
FORBIDDEN in this container: new measurement criteria; competitor framing not established
in Phase 4. REQUIRED: Competitor status MUST reach DISCHARGED by CONTAINER: CLOSE COMPLETE.

**CLOSE sub-role contract — REQUIRED before Phases 7-11 execute:**

| Sub-role | Phase scope | Writes | FORBIDDEN to write |
|----------|------------|--------|--------------------|
| COMPARATOR | Phases 7-8 | Comparison table, delta rationale, verdict | Counter-evidence disposition, limitations, replication content |
| AUDITOR | Phases 9-11 | Counter-evidence disposition, limitations, replication path | New measurement criteria, new comparison data, verdict statements |

REQUIRED: COMPARATOR responsibilities MUST be fully discharged before AUDITOR begins.
REQUIRED: Phase 8 COMPLETE MUST carry an explicit handoff marker.

---

### Phase 7 — COMPARATOR (MUST write: three-column comparison table with competitor-labeled baseline, delta rationale for both comparisons co-located with table; FORBIDDEN to write: counter-evidence disposition, limitations, replication content, new measurement criteria)

*REQUIRED: Execute before Phase 8. REQUIRED: Phase 6 COMPLETE gate MUST be present.*

REQUIRED: Populate the three-column results table. REQUIRED: Label the baseline column
with the inertia competitor's name — this is the third structural surface for competitor
identification and the point where REFERENCED transitions toward DISCHARGED. FORBIDDEN to
use "B-00" or "Baseline" as the column label.

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

### Phase 8 — COMPARATOR (MUST write: hypothesis verdict grounded in Phases 6-7 including B-00 comparison; FORBIDDEN to write: counter-evidence disposition, limitations, replication content, verdict without evidentiary grounding, new measurement criteria)

*REQUIRED: Execute before Phase 9. REQUIRED: Phase 7 COMPLETE gate MUST be present.*

REQUIRED: State CONFIRMED, REFUTED, or INCONCLUSIVE. REQUIRED: Ground the verdict in
Phases 6-7 including the B-00 comparison. FORBIDDEN: Ungrounded verdict is INVALID.
FORBIDDEN: Counter-evidence — PROHIBITED here, belongs to AUDITOR in Phase 9.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR.
[If PARTIAL: "verdict ungrounded — INVALID."]**

---

### Phase 9 — AUDITOR (MUST write: explicit binary counter-evidence disposition; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, open-ended counter-evidence section)

*REQUIRED: Execute before Phase 10. REQUIRED: Phase 8 COMPLETE gate MUST be present.
REQUIRED: COMPARATOR handoff confirmed.*

REQUIRED: EXACTLY ONE disposition — (a) named counter with evidence-grounded rebuttal,
or (b) no plausible counter with stated reason. FORBIDDEN: Any other form.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "no explicit disposition —
INVALID."]**

---

### Phase 10 — AUDITOR (MUST write: one limitation and one specific actionable next step; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, generic next steps)

*REQUIRED: Execute before Phase 11. REQUIRED: Phase 9 COMPLETE gate MUST be present.*

REQUIRED: One limitation. One specific actionable next step. FORBIDDEN: Generic.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[element] absent."]**

---

### Phase 11 — AUDITOR (MUST write: full replication path with all tools, inputs, commands, steps; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, implicit steps)

*REQUIRED: Phase 10 COMPLETE gate MUST be present.*

REQUIRED: All tools, inputs, commands, steps. FORBIDDEN: Implicit steps.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete. [If PARTIAL: "[element]
not specified."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]:
[DESIGN] hypothesis = "[text from Phase 1]";
[CALIBRATE] inertia competitor = "[name]", B-00 = [value], outperform threshold = [condition];
[BUILD] prototype result = [value], delta vs. B-00 = [direction and magnitude];
[CLOSE] verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], prototype conclusion = "[one sentence]",
counter-evidence = [ADDRESSED — "[interpretation]" rebutted | CLOSED — no plausible counter].
Competitor lifecycle — status at CLOSE exit: DISCHARGED — "[name]" incorporated in results
table baseline column (Phase 7), arc record (this line); all four lifecycle states traversed.
Value ledger: [FULLY DISCHARGED | PARTIAL — [N] values unresolved].
[If PARTIAL: "[absent element from which container] not encoded — audit chain incomplete."]**
```

---

## V-04 — Single Axis: Role Sequence (COMPARATOR/AUDITOR as Primary CLOSE Organizer)

**Axis**: Role sequence — elevate C-41's COMPARATOR/AUDITOR sub-role split as CLOSE's
primary organizing principle. The CLOSE container header leads with the sub-role declaration
before phase enumeration. COMPARATOR and AUDITOR are introduced with the same ceremony
as FRAMER, CALIBRATOR, BUILDER, and RECORDER in the document-level role family. The Phase
8 handoff event is given its own labeled structural marker. Cross-prohibitions appear first
at the container level in a dedicated contract table, then re-stated inline at each phase
header. C-40 and C-42 are maintained at full specification but subordinate to the role-
sequencing narrative.

**Design hypothesis**: When C-41's COMPARATOR/AUDITOR split is the dominant structural
axis, the container-level sub-role contract is more prominent — the intra-CLOSE role
boundary is architecturally visible at the container's entry and confirmed at Phase 8's
handoff event. Container-level role tables plus phase-level inline declarations satisfy
both C-38 (position) and C-23 (existence); hard modal throughout satisfies C-39 (register).
Expected: 304.

---

```
You are running **prove-prototype** for Signal.

**Artifact**: `simulations/prove/investigations/{topic}-prototype-{date}.md`
**Topic**: [Topic]
**Signal**: [Signal]

---

**PREREQUISITE — REQUIRED before any output**: Read the topic file. Identify the active
hypothesis. You MUST NOT begin Phase 1 until confirmed. If absent, HALT: "hypothesis absent —
FORBIDDEN to proceed."

---

## Output Contract

REQUIRED: This manifest MUST appear before any container body executes. REQUIRED: Execute
containers in the order listed. FORBIDDEN: No container MAY absorb work belonging to another.
REQUIRED: Each CONTAINER COMPLETE line that advances competitor status MUST carry a status
annotation.

| Container | Phases | Principal purpose | Expected output | Competitor status |
|-----------|--------|-------------------|-----------------|-------------------|
| DESIGN | 1-3 | Lock hypothesis, bound scope, freeze measurement criteria — competitor identification FORBIDDEN | Hypothesis text, validated exclusions with co-located rationale, success threshold, failure threshold | NOT YET IDENTIFIED |
| CALIBRATE | 4 | Identify inertia competitor, commit B-00, state outperform threshold — all pre-build | Named competitor, B-00, outperform threshold | IDENTIFIED AND COMMITTED |
| BUILD | 5-6 | Build minimum prototype, record raw measurement — comparison and verdict FORBIDDEN | Prototype with minimality trade-off, raw result | REFERENCED |
| CLOSE | 7-11 | COMPARATOR (7-8): compare and render verdict. AUDITOR (9-11): counter-evidence, limitations, replication — new measurement criteria FORBIDDEN | Three-column table with competitor-labeled baseline, verdict, counter-evidence disposition, limitation, replication | DISCHARGED |

REQUIRED: The terminal CONTAINER: CLOSE COMPLETE line MUST encode results from all four
containers.

---

## Value Flow Ledger

REQUIRED: This section MUST appear after the manifest and before any container body executes.
REQUIRED: Every value listed MUST be included; no value MUST be consumed before its
producing phase executes.

| Value | Producing phase | First consuming phase |
|-------|----------------|----------------------|
| Hypothesis text | Phase 1 (FRAMER) | Phase 8 (COMPARATOR — verdict grounding) |
| Scope exclusion(s) | Phase 2 (FRAMER) | Phase 5 (BUILDER — minimality trade-off) |
| Success threshold | Phase 3 (FRAMER) | Phase 7 (COMPARATOR — Predicted column) |
| Failure threshold | Phase 3 (FRAMER) | Phase 7 (COMPARATOR — Predicted column) |
| Inertia competitor name | Phase 4 (CALIBRATOR) | Phase 7 (COMPARATOR — Baseline column label) |
| B-00 | Phase 4 (CALIBRATOR) | Phase 7 (COMPARATOR — Baseline column value) |
| Outperform threshold | Phase 4 (CALIBRATOR) | Phase 8 (COMPARATOR — verdict grounding) |
| Prototype description | Phase 5 (BUILDER) | Phase 6 (RECORDER — measurement context) |
| Raw result | Phase 6 (RECORDER) | Phase 7 (COMPARATOR — Observed column) |
| Delta rationale | Phase 7 (COMPARATOR) | Phase 8 (COMPARATOR — verdict grounding) |
| Verdict word | Phase 8 (COMPARATOR) | CLOSE COMPLETE arc record |
| Counter-evidence disposition | Phase 9 (AUDITOR) | CLOSE COMPLETE arc record |

**VALUE FLOW LEDGER DECLARED — [N] values; no-anticipation constraint REQUIRED active.**

---

## CONTAINER: DESIGN

REQUIRED: Complete all phases 1-3 before entering CONTAINER: CALIBRATE.
FORBIDDEN: baseline measurement, inertia competitor identification, build activity, raw
results, result interpretation.

---

### Phase 1 — FRAMER (MUST write: hypothesis restatement; FORBIDDEN to write: baseline measurement, inertia competitor identification, build activity, raw results, interpretation)

*REQUIRED: Execute before Phase 2.*

REQUIRED: Write the hypothesis as the first substantive element of output, quoted or
closely paraphrased from the topic file.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]".**

---

### Phase 2 — FRAMER (MUST write: scope exclusions each with co-located validity rationale; FORBIDDEN to write: inertia competitor identification [PROHIBITED — belongs exclusively in CALIBRATE], measurement criteria, build activity, results)

*REQUIRED: Execute before Phase 3. REQUIRED: Phase 1 COMPLETE gate MUST be present.*

REQUIRED: Name at least two explicit exclusions, each with co-located validity rationale
in the same labeled pair.

> **EXCLUDED**: [element]
> **WHY TEST REMAINS VALID**: [reason — REQUIRED in same labeled block]

> **EXCLUDED**: [element]
> **WHY TEST REMAINS VALID**: [reason — REQUIRED in same labeled block]

**PHASE 2 COMPLETE — [FULL|PARTIAL]: scope established; [N] exclusions with co-located
validity rationale. [If PARTIAL: "[element] absent."]**

---

### Phase 3 — FRAMER (MUST write: metric name, success threshold, failure threshold; FORBIDDEN to write: baseline measurement, inertia competitor identification, build steps, experimental results)

*REQUIRED: Execute before CONTAINER: CALIBRATE. REQUIRED: Phase 2 COMPLETE gate MUST be
present.*

REQUIRED: State the metric, success threshold, and failure threshold. REQUIRED: Frozen at
this gate — FORBIDDEN to change in any subsequent container.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: metric = "[name]"; success = [threshold]; failure =
[threshold].**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis = "[text]", scope = [N] validated
exclusions, success threshold = [value], failure threshold = [value]. Competitor
identification FORBIDDEN here — REQUIRED in CALIBRATE. Competitor status: NOT YET
IDENTIFIED. [If PARTIAL: "[element] absent."]
→ [CALIBRATE] receives: hypothesis = "[text]", metric = "[name]", success threshold = [value],
failure threshold = [value].**

---

## CONTAINER: CALIBRATE

REQUIRED: Execute after CONTAINER: DESIGN COMPLETE gate is present in output.
REQUIRED: Complete Phase 4 before entering CONTAINER: BUILD.
FORBIDDEN: scope definition, hypothesis activity, build steps, experimental measurement.

---

### Phase 4 — CALIBRATOR (MUST write: inertia competitor name and status-quo rationale, B-00 on Phase 3 metric, explicit outperform threshold; FORBIDDEN to write: prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims)

*REQUIRED: Execute before CONTAINER: BUILD. REQUIRED: Phase 3 COMPLETE gate MUST be present.*

REQUIRED: Discharge (1) inertia competitor name and status-quo rationale; (2) B-00 on Phase
3 metric; (3) outperform threshold relative to B-00. REQUIRED: In that order. FORBIDDEN:
B-00 MUST NOT be revised after this point.

> **INERTIA COMPETITOR**: [name — REQUIRED]
> **WHY IT IS STATUS-QUO**: [one sentence — REQUIRED]
> **B-00**: [what the inertia competitor produces on the Phase 3 metric — REQUIRED]
> **OUTPERFORM THRESHOLD**: Prototype MUST produce [outcome] relative to B-00 = [value].
>   FORBIDDEN: Matching or underperforming B-00 does NOT confirm the hypothesis.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: (1) inertia competitor = "[name]"; (2) B-00 = [value];
(3) outperform threshold stated. [If PARTIAL: "responsibility ([1|2|3]) not discharged."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]", B-00 = [value],
outperform threshold = prototype MUST [condition] relative to B-00. Competitor status:
IDENTIFIED AND COMMITTED — "[name]" committed as B-00 baseline. [If PARTIAL: "[element] absent."]
→ [BUILD] receives: inertia competitor = "[name]", B-00 = [value], metric = "[name]",
outperform threshold = [condition].**

---

## CONTAINER: BUILD

REQUIRED: Execute after CONTAINER: CALIBRATE COMPLETE gate is present in output.
REQUIRED: Complete phases 5-6 before entering CONTAINER: CLOSE.
FORBIDDEN: comparison to B-00, result interpretation, verdict, new measurement criteria.

---

### Phase 5 — BUILDER (MUST write: prototype description, build steps, minimality trade-off with co-located rationale, replication path; FORBIDDEN to write: comparison to B-00 or inertia competitor, result interpretation, verdict)

*REQUIRED: Execute before Phase 6. REQUIRED: Phase 4 COMPLETE gate MUST be present.*

REQUIRED: Describe or implement the prototype. REQUIRED: State what was left out and why
in the same block. REQUIRED: Include all steps to reproduce — FORBIDDEN: no implicit steps.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [element] absent].**

---

### Phase 6 — RECORDER (MUST write: raw measurement on Phase 3 metric only; FORBIDDEN to write: interpretation, comparison to B-00, comparison to inertia competitor, verdict)

*REQUIRED: Execute before CONTAINER: CLOSE. REQUIRED: Phase 5 COMPLETE gate MUST be present.*

REQUIRED: Apply the Phase 3 metric. REQUIRED: Record the raw result ONLY. FORBIDDEN:
Comparison to B-00 — REQUIRED to appear exclusively in CONTAINER: CLOSE.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value].**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built; raw result = [value]; B-00 =
[value] for "[inertia competitor]". Competitor status: REFERENCED — B-00 from "[name]"
carried into CLOSE. [If PARTIAL: "[element] absent."]
→ [CLOSE] receives: raw result = [value], B-00 = [value], inertia competitor = "[name]",
metric = "[name]".**

---

## CONTAINER: CLOSE

REQUIRED: Execute after CONTAINER: BUILD COMPLETE gate is present in output.
REQUIRED: Every phase MUST carry an explicit PREREQUISITE gate marker in output.
FORBIDDEN: new measurement criteria; competitor framing not established in Phase 4.

### CLOSE Sub-Role Architecture

REQUIRED: The CLOSE container is governed by two named sub-roles with disjoint phase scopes.
REQUIRED: Declare this sub-role contract before any phase executes. FORBIDDEN: Neither
sub-role MAY write content belonging to the other.

**COMPARATOR** — governs Phases 7-8
- MUST write: quantitative comparison table, delta rationale, hypothesis verdict
- FORBIDDEN to write: counter-evidence disposition, limitations content, replication path
- Scope rationale: comparison and verdict precede counter-evidence audit

**AUDITOR** — governs Phases 9-11
- MUST write: counter-evidence disposition, limitations, replication path
- FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements
- Scope rationale: counter-evidence audit and close-out follow verdict

**Phase 8/9 handoff — REQUIRED structural event**: The transition from COMPARATOR to
AUDITOR at the Phase 8/9 boundary is a named handoff event. REQUIRED: The Phase 8 COMPLETE
line MUST carry: "COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR."
REQUIRED: AUDITOR MUST confirm the handoff before Phase 9 executes. FORBIDDEN: AUDITOR
MUST NOT begin Phase 9 without the handoff marker present in Phase 8 COMPLETE.

---

### Phase 7 — COMPARATOR (MUST write: three-column comparison table with competitor-labeled baseline, delta rationale for both comparisons co-located with table; FORBIDDEN to write: counter-evidence disposition, limitations, replication content, new measurement criteria)

*REQUIRED: Execute before Phase 8. REQUIRED: Phase 6 COMPLETE gate MUST be present.*

REQUIRED: Populate the three-column results table. REQUIRED: Label the baseline column with
the inertia competitor's name — FORBIDDEN to use "B-00" or "Baseline" as the column label.

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

### Phase 8 — COMPARATOR (MUST write: hypothesis verdict grounded in Phases 6-7 including B-00 comparison; FORBIDDEN to write: counter-evidence disposition, limitations, replication content, verdict without evidentiary grounding, new measurement criteria)

*REQUIRED: Execute before Phase 9. REQUIRED: Phase 7 COMPLETE gate MUST be present.*

REQUIRED: State CONFIRMED, REFUTED, or INCONCLUSIVE. REQUIRED: Ground verdict in Phases
6-7 including B-00 comparison. FORBIDDEN: Ungrounded verdict is INVALID. FORBIDDEN:
Counter-evidence disposition — PROHIBITED to COMPARATOR; REQUIRED to appear in AUDITOR
Phase 9.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR.
[If PARTIAL: "verdict ungrounded — INVALID."]**

---

*AUDITOR takes over from this point. REQUIRED: Confirm Phase 8 handoff marker present before
executing Phase 9.*

---

### Phase 9 — AUDITOR (MUST write: explicit binary counter-evidence disposition; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, open-ended counter-evidence section)

*REQUIRED: Execute before Phase 10. REQUIRED: Phase 8 COMPLETE gate with COMPARATOR handoff
marker MUST be present.*

REQUIRED: EXACTLY ONE disposition — (a) named counter-interpretation with evidence-grounded
rebuttal, or (b) no plausible counter with stated reason. FORBIDDEN: Any other form.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "no explicit disposition —
INVALID."]**

---

### Phase 10 — AUDITOR (MUST write: one limitation and one specific actionable next step; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, generic next steps)

*REQUIRED: Execute before Phase 11. REQUIRED: Phase 9 COMPLETE gate MUST be present.*

REQUIRED: One limitation. One specific actionable next step. FORBIDDEN: Generic next steps
are INVALID.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[element] absent."]**

---

### Phase 11 — AUDITOR (MUST write: full replication path with all tools, inputs, commands, steps; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, implicit steps)

*REQUIRED: Phase 10 COMPLETE gate MUST be present.*

REQUIRED: All tools, inputs, commands, steps. FORBIDDEN: Implicit steps.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete. [If PARTIAL: "[element]
not specified."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]:
[DESIGN] hypothesis = "[text from Phase 1]";
[CALIBRATE] inertia competitor = "[name]", B-00 = [value], outperform threshold = [condition];
[BUILD] prototype result = [value], delta vs. B-00 = [direction and magnitude];
[CLOSE] verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], prototype conclusion = "[one sentence]",
counter-evidence = [ADDRESSED — "[interpretation]" rebutted | CLOSED — no plausible counter].
Competitor status: DISCHARGED — "[name]" fully incorporated in results table baseline column
and arc record. COMPARATOR/AUDITOR sub-role contract: DISCHARGED — Phase 8 handoff executed,
Phases 7-11 completed by assigned sub-roles.
Value ledger: [FULLY DISCHARGED | PARTIAL — [N] values unresolved].
[If PARTIAL: "[absent element from which container] not encoded — audit chain incomplete."]**
```

---

## V-05 — Combination: Inertia Framing + Role Sequence (C-40 + C-41 Co-Elevated)

**Axis**: Combination of V-03 (inertia framing) and V-04 (role sequence) — both the
competitor lifecycle thread (C-40) and the CLOSE sub-role sequencing thread (C-41) are
co-elevated as primary structural spines. The manifest competitor-status column anchors the
competitor lifecycle as the document's temporal accountability thread. CLOSE leads with the
COMPARATOR/AUDITOR sub-role architecture as the container's primary organizing principle.
Both structures converge at the terminal CONTAINER: CLOSE COMPLETE line: the competitor
reaches DISCHARGED exactly when AUDITOR completes Phase 11, making the competitor lifecycle
and the role handoff natural complements rather than competing emphases. C-42 maintained at
full specification.

**Design hypothesis**: Two co-elevated structural spines — competitor lifecycle (C-40) and
intra-container role sequencing (C-41) — do not conflict when their convergence point is
explicit. The competitor lifecycle is a document-level temporal thread (spans all four
containers); the role-sequencing thread is a container-level internal thread (spans Phases
7-11 within CLOSE). Neither subsumes the other. When both are foregrounded simultaneously,
the terminal CLOSE COMPLETE line becomes the single point where competitor lifecycle,
sub-role handoff, full arc record, and ledger discharge all converge. Expected: 304.

---

```
You are running **prove-prototype** for Signal.

**Artifact**: `simulations/prove/investigations/{topic}-prototype-{date}.md`
**Topic**: [Topic]
**Signal**: [Signal]

---

**PREREQUISITE — REQUIRED before any output**: Read the topic file. Identify the active
hypothesis. You MUST NOT begin Phase 1 until confirmed. If absent, HALT: "hypothesis absent —
FORBIDDEN to proceed."

---

## Output Contract

REQUIRED: This manifest MUST appear before any container body executes. REQUIRED: Execute
containers in the order listed. FORBIDDEN: No container MAY absorb work belonging to another.

**Two structural threads govern this document:**

**Thread 1 — Competitor lifecycle (C-40)**: The inertia competitor travels through four
states across the four containers. REQUIRED: Each CONTAINER COMPLETE line that advances
competitor status MUST carry a status annotation. FORBIDDEN: Status MUST NOT advance before
the container whose manifest row carries the new state.

**Thread 2 — CLOSE role sequencing (C-41)**: Within CONTAINER: CLOSE, ANALYST is replaced
by COMPARATOR (Phases 7-8) and AUDITOR (Phases 9-11). REQUIRED: Phase 8 COMPLETE MUST carry
the named handoff marker. FORBIDDEN: COMPARATOR and AUDITOR MUST NOT write each other's
content.

**Convergence**: Both threads terminate at CONTAINER: CLOSE COMPLETE — the competitor
reaches DISCHARGED and the AUDITOR completes Phase 11 simultaneously. The terminal line
confirms both.

| Container | Phases | Principal purpose | Expected output | Competitor status |
|-----------|--------|-------------------|-----------------|-------------------|
| DESIGN | 1-3 | Lock hypothesis, bound scope, freeze measurement criteria — competitor identification FORBIDDEN | Hypothesis text, validated exclusions with co-located rationale, success threshold, failure threshold | NOT YET IDENTIFIED |
| CALIBRATE | 4 | Identify inertia competitor, commit B-00, state outperform threshold — all pre-build | Named competitor, B-00, outperform threshold | IDENTIFIED AND COMMITTED |
| BUILD | 5-6 | Build minimum prototype, record raw measurement — comparison and verdict FORBIDDEN | Prototype with minimality trade-off, raw result | REFERENCED |
| CLOSE | 7-11 | COMPARATOR (7-8): compare + verdict. AUDITOR (9-11): counter-evidence + limitations + replication — new measurement criteria FORBIDDEN | Three-column table with competitor-labeled baseline, verdict, counter-evidence disposition, limitation, replication | DISCHARGED |

REQUIRED: The terminal CONTAINER: CLOSE COMPLETE line MUST encode results from all four
containers, confirm competitor lifecycle DISCHARGED, confirm COMPARATOR/AUDITOR handoff
executed, and confirm ledger discharge status.

---

## Value Flow Ledger

REQUIRED: This section MUST appear after the manifest and before any container body executes.
REQUIRED: Every value listed MUST be included; no value MUST be consumed before its
producing phase executes.

| Value | Producing phase | First consuming phase |
|-------|----------------|----------------------|
| Hypothesis text | Phase 1 (FRAMER) | Phase 8 (COMPARATOR — verdict grounding) |
| Scope exclusion(s) | Phase 2 (FRAMER) | Phase 5 (BUILDER — minimality trade-off) |
| Success threshold | Phase 3 (FRAMER) | Phase 7 (COMPARATOR — Predicted column) |
| Failure threshold | Phase 3 (FRAMER) | Phase 7 (COMPARATOR — Predicted column) |
| Inertia competitor name | Phase 4 (CALIBRATOR) | Phase 7 (COMPARATOR — Baseline column label) |
| B-00 | Phase 4 (CALIBRATOR) | Phase 7 (COMPARATOR — Baseline column value) |
| Outperform threshold | Phase 4 (CALIBRATOR) | Phase 8 (COMPARATOR — verdict grounding) |
| Prototype description | Phase 5 (BUILDER) | Phase 6 (RECORDER — measurement context) |
| Raw result | Phase 6 (RECORDER) | Phase 7 (COMPARATOR — Observed column) |
| Delta rationale | Phase 7 (COMPARATOR) | Phase 8 (COMPARATOR — verdict grounding) |
| Verdict word | Phase 8 (COMPARATOR) | CLOSE COMPLETE arc record |
| Counter-evidence disposition | Phase 9 (AUDITOR) | CLOSE COMPLETE arc record |

**VALUE FLOW LEDGER DECLARED — [N] values; no-anticipation constraint REQUIRED active.**

---

## CONTAINER: DESIGN
*Competitor lifecycle: entering this container as NOT YET IDENTIFIED*

REQUIRED: Complete all phases 1-3 before entering CONTAINER: CALIBRATE.
FORBIDDEN: baseline measurement, inertia competitor identification [NOT YET IDENTIFIED —
PROHIBITED before CALIBRATE], build activity, raw results, result interpretation.

---

### Phase 1 — FRAMER (MUST write: hypothesis restatement; FORBIDDEN to write: baseline measurement, inertia competitor identification [PROHIBITED — NOT YET IDENTIFIED], build activity, raw results, interpretation)

*REQUIRED: Execute before Phase 2.*

REQUIRED: Write the hypothesis as the first substantive element of output, quoted or
closely paraphrased from the topic file.

**PHASE 1 COMPLETE — [FULL|PARTIAL]: hypothesis = "[hypothesis text]".**

---

### Phase 2 — FRAMER (MUST write: scope exclusions each with co-located validity rationale; FORBIDDEN to write: inertia competitor identification [PROHIBITED — NOT YET IDENTIFIED], measurement criteria, build activity, results)

*REQUIRED: Execute before Phase 3. REQUIRED: Phase 1 COMPLETE gate MUST be present.*

REQUIRED: Name at least two explicit exclusions, each with co-located validity rationale
in the same labeled pair.

> **EXCLUDED**: [element]
> **WHY TEST REMAINS VALID**: [reason — REQUIRED in same labeled block]

> **EXCLUDED**: [element]
> **WHY TEST REMAINS VALID**: [reason — REQUIRED in same labeled block]

**PHASE 2 COMPLETE — [FULL|PARTIAL]: scope established; [N] exclusions with co-located
validity rationale. [If PARTIAL: "[element] absent."]**

---

### Phase 3 — FRAMER (MUST write: metric name, success threshold, failure threshold; FORBIDDEN to write: baseline measurement, inertia competitor identification [PROHIBITED — NOT YET IDENTIFIED], build steps, experimental results)

*REQUIRED: Execute before CONTAINER: CALIBRATE. REQUIRED: Phase 2 COMPLETE gate MUST be
present.*

REQUIRED: State the metric, success threshold, and failure threshold. REQUIRED: Frozen at
this gate — FORBIDDEN to change in any subsequent container.

**PHASE 3 COMPLETE — [FULL|PARTIAL]: metric = "[name]"; success = [threshold]; failure =
[threshold].**

**CONTAINER: DESIGN COMPLETE — [FULL|PARTIAL]: hypothesis = "[text]", scope = [N] validated
exclusions, success threshold = [value], failure threshold = [value].
Thread 1 (competitor lifecycle) — status at DESIGN: NOT YET IDENTIFIED. Identification is
FORBIDDEN before CALIBRATE. [If PARTIAL: "[element] absent."]
→ [CALIBRATE] receives: hypothesis = "[text]", metric = "[name]", success threshold = [value],
failure threshold = [value]; competitor lifecycle: NOT YET IDENTIFIED.**

---

## CONTAINER: CALIBRATE
*Competitor lifecycle: this container transitions status from NOT YET IDENTIFIED to IDENTIFIED AND COMMITTED*

REQUIRED: Execute after CONTAINER: DESIGN COMPLETE gate is present in output.
REQUIRED: Complete Phase 4 before entering CONTAINER: BUILD.
FORBIDDEN: scope definition, hypothesis activity, build steps, experimental measurement.
REQUIRED: Competitor lifecycle MUST advance to IDENTIFIED AND COMMITTED before this container
closes.

---

### Phase 4 — CALIBRATOR (MUST write: inertia competitor name and status-quo rationale, B-00 on Phase 3 metric, explicit outperform threshold; FORBIDDEN to write: prototype description, scope exclusions, measurement criteria changes, experimental results, performance claims)

*REQUIRED: Execute before CONTAINER: BUILD. REQUIRED: Phase 3 COMPLETE gate MUST be present.*

REQUIRED: Discharge in order — (1) IDENTIFY inertia competitor [lifecycle: NOT YET IDENTIFIED
→ IDENTIFIED]; (2) MEASURE B-00 [lifecycle: IDENTIFIED → IDENTIFIED AND COMMITTED]; (3)
STATE outperform threshold. FORBIDDEN: B-00 MUST NOT be revised after this point.

> **INERTIA COMPETITOR**: [name — REQUIRED]
> **WHY IT IS STATUS-QUO**: [one sentence — REQUIRED]
> **B-00**: [what the inertia competitor produces on the Phase 3 metric — REQUIRED]
> **OUTPERFORM THRESHOLD**: Prototype MUST produce [outcome] relative to B-00 = [value].
>   FORBIDDEN: Matching or underperforming B-00 does NOT confirm the hypothesis.

**PHASE 4 COMPLETE — [FULL|PARTIAL]: (1) inertia competitor = "[name]"; (2) B-00 = [value];
(3) outperform threshold stated. [If PARTIAL: "responsibility ([1|2|3]) not discharged."]**

**CONTAINER: CALIBRATE COMPLETE — [FULL|PARTIAL]: inertia competitor = "[name]", B-00 = [value],
outperform threshold = prototype MUST [condition] relative to B-00.
Thread 1 (competitor lifecycle) — status at CALIBRATE: IDENTIFIED AND COMMITTED — "[name]"
named and B-00 committed; lifecycle advances to REFERENCED in BUILD.
[If PARTIAL: "[element] absent."]
→ [BUILD] receives: inertia competitor = "[name]" [lifecycle: IDENTIFIED AND COMMITTED],
B-00 = [value], metric = "[name]", outperform threshold = [condition].**

---

## CONTAINER: BUILD
*Competitor lifecycle: entering as IDENTIFIED AND COMMITTED — transitions to REFERENCED when BUILD closes*

REQUIRED: Execute after CONTAINER: CALIBRATE COMPLETE gate is present in output.
REQUIRED: Complete phases 5-6 before entering CONTAINER: CLOSE.
FORBIDDEN: comparison to B-00, result interpretation, verdict, new measurement criteria.

---

### Phase 5 — BUILDER (MUST write: prototype description, build steps, minimality trade-off with co-located rationale, replication path; FORBIDDEN to write: comparison to B-00 or inertia competitor, result interpretation, verdict)

*REQUIRED: Execute before Phase 6. REQUIRED: Phase 4 COMPLETE gate MUST be present.*

REQUIRED: Describe or implement the prototype. REQUIRED: State what was left out and why
in the same block. REQUIRED: Include all steps to reproduce — FORBIDDEN: no implicit steps.

**PHASE 5 COMPLETE — [FULL|PARTIAL]: prototype built; minimality trade-off recorded;
replication steps [all explicit | partial — [element] absent].**

---

### Phase 6 — RECORDER (MUST write: raw measurement on Phase 3 metric only; FORBIDDEN to write: interpretation, comparison to B-00, comparison to inertia competitor, verdict)

*REQUIRED: Execute before CONTAINER: CLOSE. REQUIRED: Phase 5 COMPLETE gate MUST be present.*

REQUIRED: Apply the Phase 3 metric. REQUIRED: Record the raw result ONLY. FORBIDDEN:
Comparison to B-00 — REQUIRED to appear exclusively in CONTAINER: CLOSE.

**PHASE 6 COMPLETE — [FULL|PARTIAL]: measurement applied; raw result = [value].**

**CONTAINER: BUILD COMPLETE — [FULL|PARTIAL]: prototype built; raw result = [value]; B-00 =
[value] for "[inertia competitor]".
Thread 1 (competitor lifecycle) — status at BUILD: REFERENCED — B-00 from "[name]" active
as comparison baseline; competitor reaches DISCHARGED in CLOSE when baseline column is
anchored to its name and arc record is written.
[If PARTIAL: "[element] absent."]
→ [CLOSE] receives: raw result = [value], B-00 = [value], inertia competitor = "[name]"
[lifecycle: REFERENCED], metric = "[name]".**

---

## CONTAINER: CLOSE
*Competitor lifecycle: entering as REFERENCED — must reach DISCHARGED before this container closes*
*Thread 2 (role sequencing): COMPARATOR governs Phases 7-8; AUDITOR governs Phases 9-11*

REQUIRED: Execute after CONTAINER: BUILD COMPLETE gate is present in output.
REQUIRED: Every phase MUST carry an explicit PREREQUISITE gate marker in output.
FORBIDDEN: new measurement criteria; competitor framing not established in Phase 4.

**CLOSE sub-role contract — REQUIRED before Phases 7-11 execute:**

| Sub-role | Phases | MUST write | FORBIDDEN to write |
|----------|--------|------------|--------------------|
| COMPARATOR | 7-8 | Comparison table, delta rationale, verdict | Counter-evidence disposition, limitations, replication content |
| AUDITOR | 9-11 | Counter-evidence disposition, limitations, replication path | New measurement criteria, new comparison data, verdict statements |

REQUIRED: COMPARATOR MUST fully discharge Phases 7-8 before AUDITOR begins Phase 9.
REQUIRED: Phase 8 COMPLETE MUST carry the named handoff marker.
FORBIDDEN: AUDITOR MUST NOT begin Phase 9 without the handoff marker present.

**Convergence note**: The competitor lifecycle reaches DISCHARGED and the AUDITOR completes
Phase 11 simultaneously. Both threads are confirmed at CONTAINER: CLOSE COMPLETE.

---

### Phase 7 — COMPARATOR (MUST write: three-column comparison table with competitor-labeled baseline, delta rationale for both comparisons co-located with table; FORBIDDEN to write: counter-evidence disposition, limitations, replication content, new measurement criteria)

*REQUIRED: Execute before Phase 8. REQUIRED: Phase 6 COMPLETE gate MUST be present.*

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

### Phase 8 — COMPARATOR (MUST write: hypothesis verdict grounded in Phases 6-7 including B-00 comparison; FORBIDDEN to write: counter-evidence disposition, limitations, replication content, verdict without evidentiary grounding, new measurement criteria)

*REQUIRED: Execute before Phase 9. REQUIRED: Phase 7 COMPLETE gate MUST be present.*

REQUIRED: State CONFIRMED, REFUTED, or INCONCLUSIVE. REQUIRED: Ground verdict in Phases
6-7 including B-00 comparison. FORBIDDEN: Ungrounded verdict is INVALID. FORBIDDEN:
Counter-evidence disposition — PROHIBITED to COMPARATOR; belongs to AUDITOR Phase 9.

**PHASE 8 COMPLETE — [FULL|PARTIAL]: verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], grounded
in [evidence reference]. COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR.
[If PARTIAL: "verdict ungrounded — INVALID."]**

---

### Phase 9 — AUDITOR (MUST write: explicit binary counter-evidence disposition; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, open-ended counter-evidence section)

*REQUIRED: Execute before Phase 10. REQUIRED: Phase 8 COMPLETE gate with COMPARATOR handoff
marker MUST be present. REQUIRED: Confirm handoff before executing.*

REQUIRED: EXACTLY ONE disposition — (a) named counter with evidence-grounded rebuttal, or
(b) no plausible counter with stated reason. FORBIDDEN: Any other form.

**PHASE 9 COMPLETE — [FULL|PARTIAL]: counter-evidence [ADDRESSED — rebuttal on record |
CLOSED — no plausible counter, reason: [reason]]. [If PARTIAL: "no explicit disposition —
INVALID."]**

---

### Phase 10 — AUDITOR (MUST write: one limitation and one specific actionable next step; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, generic next steps)

*REQUIRED: Execute before Phase 11. REQUIRED: Phase 9 COMPLETE gate MUST be present.*

REQUIRED: One limitation. One specific actionable next step. FORBIDDEN: Generic next steps
are INVALID.

**PHASE 10 COMPLETE — [FULL|PARTIAL]: limitation and next step recorded. [If PARTIAL:
"[element] absent."]**

---

### Phase 11 — AUDITOR (MUST write: full replication path with all tools, inputs, commands, steps; FORBIDDEN to write: new measurement criteria, new comparison data, verdict statements, implicit steps)

*REQUIRED: Phase 10 COMPLETE gate MUST be present.*

REQUIRED: All tools, inputs, commands, steps. FORBIDDEN: Implicit steps.

**PHASE 11 COMPLETE — [FULL|PARTIAL]: replication path complete. [If PARTIAL: "[element]
not specified."]**

**CONTAINER: CLOSE COMPLETE — [FULL|PARTIAL]:
[DESIGN] hypothesis = "[text from Phase 1]";
[CALIBRATE] inertia competitor = "[name]", B-00 = [value], outperform threshold = [condition];
[BUILD] prototype result = [value], delta vs. B-00 = [direction and magnitude];
[CLOSE] verdict = [CONFIRMED|REFUTED|INCONCLUSIVE], prototype conclusion = "[one sentence]",
counter-evidence = [ADDRESSED — "[interpretation]" rebutted | CLOSED — no plausible counter].
Thread 1 (competitor lifecycle) — DISCHARGED: "[name]" traversed all four states (NOT YET
IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED); incorporated in results
table baseline column and this arc record.
Thread 2 (role sequencing) — DISCHARGED: COMPARATOR executed Phases 7-8 and handed off to
AUDITOR at Phase 8 COMPLETE; AUDITOR executed Phases 9-11; no cross-contamination.
Value ledger: [FULLY DISCHARGED | PARTIAL — [N] values unresolved].
[If PARTIAL: "[absent element from which container] not encoded — audit chain incomplete."]**
```
