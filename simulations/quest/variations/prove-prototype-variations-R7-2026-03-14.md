Now I have the complete picture. Round 6 produced C-25 and C-26 — the key new failure modes are:
- **C-25 fails when** one role per lifecycle container makes container scan ≡ role scan (V-04 and V-05 from R6 both have this problem)
- **C-26 requires** B-00 established before build AND at least one results-phase completion line carrying a B-00 comparison

The central design challenge for Round 7: every variation needs lifecycle containers at a **different granularity** than role labels. The fix: put 2+ roles inside at least one lifecycle container.

Writing the 5 complete variations now.

---

# prove-prototype — Round 7 Variations (v7 rubric)

**Date**: 2026-03-15
**Rubric version**: v7 (190 pts; C-25, C-26 added)
**New targets**: C-25 (lifecycle containers and role labels are structurally independent annotation layers) and C-26 (completion lines carry a baseline comparison enabling two-chain audit). Round 6 V-04 and V-05 achieved C-23 and C-24 but collapse on C-25 because each lifecycle container enclosed exactly one role — making container scan equivalent to role scan. All R7 variations break that equivalence by distributing multiple roles within at least one lifecycle container.

**C-25 strategy across all variations**: At least one lifecycle container holds two named roles. Container scan traverses section headers; role scan traverses block-level role labels within sections. The two scans traverse different structural granularities and detect different failure classes.

**C-26 strategy across all variations**: B-00 inertia baseline is established in the setup phase before any build activity. At least one completion line in the results or evaluation phase encodes `observed [X] vs. B-00 [Y], delta [Z], in predicted direction: YES/NO`.

---

## Axis Summary

| Variation | Single/Combined | Primary axis | C-25 mechanism | C-26 mechanism |
|-----------|-----------------|-------------|----------------|----------------|
| V-01 | Single | Role sequence (5-role, 2 roles in DEFINE + 2 roles in EXECUTE) | DEFINE holds FRAMER + CALIBRATOR; EXECUTE holds BUILDER + RECORDER — container scan traverses 3 section headers, role scan traverses 5 block labels | CALIBRATOR writes B-00 in DEFINE; EVALUATE completion line carries B-00 comparison |
| V-02 | Single | Output format (table-centric, role labels as column values) | Container scan reads `## LIFECYCLE: X` section headers; role scan reads `Role` column across table rows — orthogonal structural dimensions | CALIBRATOR row in Define Table D-2; Results Table E-2 completion row carries B-00 comparison |
| V-03 | Single | Lifecycle emphasis (4 dedicated containers: CALIBRATE / DESIGN / EXECUTE / ANALYZE) | 4 containers, 5 roles — EXECUTE holds BUILDER + RECORDER, so container count ≠ role count and boundaries diverge | Isolated CALIBRATE container for B-00 only; ANALYZE completion line carries B-00 delta |
| V-04 | Single | Phrasing register (conversational second-person imperatives) | SETUP holds THINKER + ANCHOR; BUILD holds MAKER + WATCHER — same independence mechanism as V-01, different register | ANCHOR writes B-00 in SETUP; CLOSE completion line carries B-00 comparison |
| V-05 | Single | Inertia framing (B-00 as first element; B-00 comparison in every completion line) | BASELINE holds only ANCHOR (1 role); BUILD holds BUILDER + MEASURER (2 roles in 1 container); 4 containers, 4 roles total | B-00 is the absolute first output element; every completion line from BUILD onward carries a B-00 comparison value |

---

## V-01 — Single Axis: Role Sequence (Five-Role, Multi-Role-Per-Container)

**Variation axis**: Role sequence — five named roles execute in strict sequential order; two lifecycle containers each hold two roles, ensuring the role-label boundary is finer than the container boundary

**Hypothesis**: Assigning two roles to each of the DEFINE and EXECUTE containers — rather than one role per container — ensures that a container-boundary scan and a role-label scan traverse different structural levels, satisfying C-25: one scan detects lifecycle inversions, the other detects in-order out-of-role contamination, and neither subsumes the other.

---

````markdown
You are producing a `prove-prototype` artifact. Five named roles execute in strict sequential
order within three lifecycle containers. Two containers hold two roles each; this forces the
role-label boundary to be finer than the container boundary.

**Container scan**: reads `## LIFECYCLE: X` section headers — detects lifecycle inversions.
**Role scan**: reads `ROLE-NAME:` block headers inside sections — detects in-order, out-of-role contamination.
These are independent checks. A container violation occurs when a phase appears in the wrong
section. A role violation occurs when a role produces content belonging to a different role
within the correct section. Neither scan subsumes the other.

---

## ROLES AND PROHIBITIONS

| Role | Container | Writes | Must Not Write |
|------|-----------|--------|----------------|
| FRAMER | DEFINE | Hypothesis, scope exclusions, measurement criteria | Build steps, observations, B-00, verdicts |
| CALIBRATOR | DEFINE | B-00 inertia baseline only | Any build or results knowledge; hypothesis; scope |
| BUILDER | EXECUTE | Construction, replication steps | Measurement outcomes, interpretations, verdicts |
| RECORDER | EXECUTE | Raw observations including B-00 control | Comparisons, interpretations, verdicts |
| ANALYST | EVALUATE | Comparison, verdict, counter-evidence, limits, replication | New observations, build re-description |

---

## LIFECYCLE: DEFINE
*Phases 1–4. Establish all setup elements before any build activity.*
*Two roles run here: FRAMER then CALIBRATOR.*
*No build content. No observed values. No evaluation content.*

---

### PHASE 1 — HYPOTHESIS
*FRAMER. Execute before anything else. Hypothesis is the first substantive element of your output.*
*Execute before Phase 2 gate is present in your output.*

FRAMER: — Must not describe construction steps, reference B-00, report outcomes, or render a verdict.

Restate the hypothesis being tested. One falsifiable claim. State what confirms it and what refutes it.

**Hypothesis**: [the falsifiable claim]
**Confirmed if**: [observable outcome that confirms]
**Refuted if**: [observable outcome that refutes]

**PHASE 1 COMPLETE — FRAMER: hypothesis = [one-phrase restatement]**

---

### PHASE 2 — PROTOTYPE SCOPE
*FRAMER. Execute after Phase 1 completion line is present in your output.*
*Execute before Phase 3 gate is present in your output.*

FRAMER: — Must not describe construction steps, reference B-00, report outcomes, or render a verdict.

Name at least two items the prototype deliberately excludes. Co-locate the validity rationale
in the same row — do not place it in a separate section.

| Excluded item | Why the hypothesis remains testable without it |
|---------------|------------------------------------------------|
| [item] | [reason — "it wasn't needed" does not answer this question] |
| [item] | [reason] |

**PHASE 2 COMPLETE — FRAMER: scope = [prototype name in one phrase], exclusions = [N named], each validity-justified**

---

### PHASE 3 — MEASUREMENT CRITERIA
*FRAMER. Execute after Phase 2 completion line is present in your output.*
*Execute before Phase 4 gate is present in your output.*
*Criteria are frozen here. BUILDER and RECORDER may not modify them.*

FRAMER: — Must not describe construction steps, reference B-00, report outcomes, or render a verdict.

| Metric | Collection method | Success condition | Failure condition |
|--------|-------------------|-------------------|-------------------|
| [metric] | [how observed] | [value that confirms] | [value that refutes] |

No observed values in this phase.

**PHASE 3 COMPLETE — FRAMER: metric = [name], success threshold = [value], criteria frozen before build**

---

### PHASE 4 — INERTIA BASELINE (B-00)
*CALIBRATOR. Execute after Phase 3 completion line is present in your output.*
*Execute before Phase 5 gate is present in your output.*
*B-00 is frozen here. May not be revised after this phase.*

CALIBRATOR: — Must not incorporate knowledge of build steps or measurement results. Must not
restate the hypothesis, describe prototype scope, or define measurement criteria.

Name the inertia baseline: the status-quo or do-nothing condition the prototype competes against.
State what B-00 would produce if the hypothesis is false (null prediction).

**B-00 Name**: [name]
**B-00 Description**: [what the status-quo or control condition is]
**B-00 Null Prediction**: [expected outcome under B-00 if hypothesis does not hold]

**PHASE 4 COMPLETE — CALIBRATOR: B-00 = [name], null prediction = [stated outcome], frozen**

**DEFINE GATE COMPLETE — hypothesis = [phrase], scope = [N in / M excluded], metric = [name + threshold], B-00 = [name + null prediction]**

---

## LIFECYCLE: EXECUTE
*Phases 5 and 6. Build and observe. No evaluation. No verdicts. B-00 is read-only.*
*Two roles run here: BUILDER then RECORDER.*

---

### PHASE 5 — BUILD
*BUILDER. Execute after DEFINE GATE is present in your output.*
*Execute before Phase 6 gate is present in your output.*

BUILDER: — Must not record measurement outcomes, interpret results, render a verdict, or modify B-00.

Describe what was built. State the minimality trade-off in the same block: what was left out
and why the hypothesis can still be tested. List all tools, inputs, and steps for replication.

**What Was Built**: [description]
**Tools and Inputs**: [every tool, library, input, configuration — no implicit entries]
**Minimality Trade-off**: [what was omitted] — [why hypothesis remains testable without it]

**Build Steps**:
1. [step]
2. [step]
3. [continue for every step]

**PHASE 5 COMPLETE — BUILDER: prototype = [name], steps = [N], replication = [COMPLETE — all steps listed | PARTIAL — missing: (list what is absent)]**

---

### PHASE 6 — RAW OBSERVATIONS
*RECORDER. Execute after Phase 5 completion line is present in your output.*
*Execute before Phase 7 gate is present in your output.*

RECORDER: — Must not compare observations to predictions, interpret meaning, or render a verdict.

Record what was observed for each metric. Include at least one concrete data point per metric.
Record a B-00 control reading using the same metric and collection method as Phase 3.

| Metric | Observed value | Context/notes |
|--------|----------------|---------------|
| [metric] | [value] | [observation context] |
| B-00 control | [measured baseline value] | [how B-00 condition was observed] |

**PHASE 6 COMPLETE — RECORDER: observed = [metric = value], B-00 control = [value]**

**EXECUTE GATE COMPLETE — prototype = [name], metrics observed = [N], B-00 control measured = [value vs. null prediction: stated]**

---

## LIFECYCLE: EVALUATE
*Phases 7–11. Analyze evidence and record conclusions.*
*One role runs here: ANALYST.*
*No new observations. No build re-description.*

---

### PHASE 7 — PREDICTED VS. ACTUAL
*ANALYST. Execute after EXECUTE GATE is present in your output.*
*Execute before Phase 8 gate is present in your output.*

ANALYST: — Must not add new observations or re-describe the build.

For each metric, state the prediction, the observation, the delta, and — co-located in the same
row — why the delta is what it is. Include a B-00 comparison row.

| Metric | Predicted | Actual | Delta | Why the delta is what it is |
|--------|-----------|--------|-------|-----------------------------|
| [metric] | [value] | [value] | [±] | [reason co-located here — not in a separate section] |
| B-00 | [null prediction] | [control reading] | [±] | [diverged from B-00 in predicted direction: YES/NO — reason co-located] |

**PHASE 7 COMPLETE — ANALYST: key delta = [phrase], B-00 comparison = [experimental result vs. B-00 null prediction, diverged in predicted direction: YES/NO, magnitude: stated]**

---

### PHASE 8 — VERDICT
*ANALYST. Execute after Phase 7 completion line is present in your output.*
*Execute before Phase 9 gate is present in your output.*

ANALYST: — Must not add new observations or re-describe the build.

| Field | Value |
|-------|-------|
| **Verdict** | Confirmed / Refuted / Inconclusive [choose one] |
| **Reasoning** | [connects Phase 7 delta to verdict — not a restatement of Phase 7; references B-00 comparison explicitly] |

**PHASE 8 COMPLETE — ANALYST: verdict = [Confirmed / Refuted / Inconclusive]**

---

### PHASE 9 — COUNTER-EVIDENCE
*ANALYST. Execute after Phase 8 completion line is present in your output.*
*Execute before Phase 10 gate is present in your output.*
*This phase must close with one of exactly two dispositions.*

ANALYST: — Must not add new observations or re-describe the build.

If a counter-interpretation exists:
- **Counter-interpretation**: [the alternative reading of Phase 6–7 evidence]
- **Rebuttal**: [why it does not hold, using Phase 6–7 evidence; reference B-00 readings where relevant]

If none exists:
- **Counter-interpretation**: None
- **Reason**: [why no alternative reading of the evidence is plausible]

Write exactly one of the following as the terminal element of this phase:

A) `PHASE 9 COMPLETE — ANALYST: DISPOSITION A — counter-interpretation = [name]; rebuttal = [summary]`
B) `PHASE 9 COMPLETE — ANALYST: DISPOSITION B — no plausible counter-interpretation; reason = [stated]`

---

### PHASE 10 — LIMITATIONS AND NEXT STEP
*ANALYST. Execute after Phase 9 completion line is present in your output.*
*Execute before Phase 11 gate is present in your output.*
*This phase must close with one of exactly two dispositions.*

ANALYST: — Must not add new observations or re-describe the build.

**Limitation**: [one specific confound or constraint particular to this prototype run — not a generic disclaimer]
**Next step**: [one specific action: what to build, test, or change — "do more research" does not pass]

Write exactly one of the following as the terminal element of this phase:

A) `PHASE 10 COMPLETE — ANALYST: DISPOSITION A — limitation = [named]; next step = [named]`
B) `PHASE 10 COMPLETE — ANALYST: DISPOSITION B — [what prevented naming a specific limitation or next step, and why]`

---

### PHASE 11 — REPLICATION PATH
*ANALYST. Execute after Phase 10 completion line is present in your output.*
*This phase must close with one of exactly two dispositions.*

ANALYST: — Must not add new observations or re-describe the build.

Every step needed to reproduce this prototype run. A reader unfamiliar with this work must
be able to replicate from this phase alone. No implicit steps. Configuration files named.
Environment requirements stated. Confirm that Phase 5 steps are complete, or fill gaps here.

Write exactly one of the following as the terminal element of this phase:

A) `PHASE 11 COMPLETE — ANALYST: DISPOSITION A — replication path complete; all steps in Phase 5 and above`
B) `PHASE 11 COMPLETE — ANALYST: DISPOSITION B — [which steps cannot be fully specified, and why]`

**EVALUATE GATE COMPLETE — verdict = [Confirmed/Refuted/Inconclusive], B-00 comparison = [experimental vs. null prediction, diverged in predicted direction: YES/NO, magnitude: stated], counter-evidence = [DISPOSITION A/B], limitation = [named], next step = [named], replication = [DISPOSITION A/B]**
````

---

## V-02 — Single Axis: Output Format (Table-Centric, Role Labels as Column Values)

**Variation axis**: Output format — every phase is a structured table; role attribution appears as a `Role` column value rather than a block header or section header; lifecycle containers are section-level headers

**Hypothesis**: Encoding role labels as table-column values rather than block-level section headers produces maximal structural independence from lifecycle container labels: a container scan reads `## LIFECYCLE: X` section headings, while a role scan reads the `Role` column across table rows — two orthogonal traversal paths that detect different failure classes without any shared structural unit.

---

````markdown
Produce a `prove-prototype` artifact in structured table format.
Every phase is a table. Prose appears only inside table cells.

**Two annotation layers operate independently**:

- **Lifecycle containers** (`## LIFECYCLE: X`) are section-level boundaries.
  A container scan reads these headers and detects lifecycle inversions
  (a table appearing under the wrong section header).

- **Role labels** appear as values in a `Role` column within tables, at the row level.
  A role scan reads the Role column across all tables and detects in-order out-of-role
  contamination (a wrong-role row within a correctly-placed table).

Container scan traverses section headings. Role scan traverses table rows.
These are different structural dimensions. Neither scan subsumes the other.

---

## ROLE DEFINITIONS

| Role | Permitted content | Prohibited content |
|------|------------------|--------------------|
| FRAMER | Hypothesis, scope exclusions, measurement criteria | Build steps, observations, B-00, verdicts |
| CALIBRATOR | B-00 inertia baseline | Build knowledge, results knowledge, hypothesis, scope |
| BUILDER | Construction, replication steps | Outcome values, interpretations, verdicts |
| RECORDER | Raw observations | Comparisons, interpretations, verdicts |
| ANALYST | Comparisons, verdict, counter-evidence, limits, replication | New observations, build re-description |

---

## LIFECYCLE: DEFINE
*Gate: All tables in this section must be complete before any LIFECYCLE: EXECUTE table appears.*

---

### Table D-1 — Hypothesis and Scope
*Gate: FRAMER rows precede all other rows. Hypothesis row is the first row in the entire output.*
*Execute before Table D-2 gate is present in your output.*

| Phase | Role | Content | Rationale / Validity |
|-------|------|---------|----------------------|
| Hypothesis | FRAMER | [Restate the hypothesis — first element of this output] | — |
| Confirmed if | FRAMER | [Observable outcome that confirms] | — |
| Refuted if | FRAMER | [Observable outcome that refutes] | — |
| Exclusion 1 | FRAMER | [Item excluded from prototype] | [Why test remains valid — co-located here] |
| Exclusion 2 | FRAMER | [Item excluded from prototype] | [Why test remains valid — co-located here] |
| Minimality | FRAMER | [What was left out] | [Why hypothesis can still be tested — co-located here] |
| **Completion** | FRAMER | **D-1 COMPLETE — hypothesis = [phrase], exclusions = [N], each justified** | — |

### Table D-2 — Inertia Baseline (B-00)
*Gate: CALIBRATOR rows only. B-00 frozen at completion row; may not be revised.*
*Execute after Table D-1 completion row is present. Execute before Table D-3 gate is present in your output.*

| Phase | Role | Content |
|-------|------|---------|
| B-00 Name | CALIBRATOR | [Name the inertia baseline] |
| B-00 Description | CALIBRATOR | [What the status-quo or control condition is] |
| B-00 Null Prediction | CALIBRATOR | [What B-00 produces if the hypothesis is false] |
| **Completion** | CALIBRATOR | **D-2 COMPLETE — B-00 = [name], null prediction = [stated outcome], frozen** |

### Table D-3 — Measurement Criteria
*Gate: FRAMER rows only. Criteria frozen at completion row; may not be modified in EXECUTE.*
*Execute after Table D-2 completion row is present. Execute before any LIFECYCLE: EXECUTE table.*

| Metric | Role | Collection method | Success condition | Failure condition | B-00 reference |
|--------|------|-------------------|-------------------|-------------------|----------------|
| [metric] | FRAMER | [how observed] | [value that confirms] | [value that refutes] | [B-00 expected value] |
| **Completion** | FRAMER | **D-3 COMPLETE — metric = [name], success = [value], B-00 ref = [value], criteria frozen** | | | |

**DEFINE GATE COMPLETE — hypothesis = [phrase], scope = [N in / M excluded, each justified], B-00 = [name + null prediction], metric = [name + threshold]**

---

## LIFECYCLE: EXECUTE
*Gate: DEFINE GATE must appear before any table in this section.*

---

### Table E-1 — Construction
*Gate: BUILDER rows only. Execute before Table E-2 gate is present in your output.*

| Phase | Role | Content |
|-------|------|---------|
| What was built | BUILDER | [Description of prototype] |
| Tools and inputs | BUILDER | [Every tool, library, input, configuration — no implicit entries] |
| Minimality trade-off | BUILDER | [What was omitted — and why hypothesis remains testable, co-located] |
| Step 1 | BUILDER | [Step for replication] |
| Step 2 | BUILDER | [Step for replication — add rows as needed] |
| **Completion** | BUILDER | **E-1 COMPLETE — prototype = [name], steps = [N], replication = [COMPLETE — all steps listed \| PARTIAL — missing: (list)]** |

### Table E-2 — Raw Observations
*Gate: RECORDER rows only. Execute after Table E-1 completion row is present. Execute before any LIFECYCLE: EVALUATE table.*
*RECORDER must not compare to predictions, interpret, or render a verdict.*

| Metric | Role | Observed value | Context/notes |
|--------|------|----------------|---------------|
| [metric] | RECORDER | [value] | [observation context] |
| B-00 control | RECORDER | [measured baseline value] | [how B-00 condition was observed] |
| **Completion** | RECORDER | **E-2 COMPLETE — observed: [metric = value], B-00 control = [value]** | |

**EXECUTE GATE COMPLETE — prototype = [name], metrics observed = [N], B-00 control = [measured value vs. null prediction: stated]**

---

## LIFECYCLE: EVALUATE
*Gate: EXECUTE GATE must appear before any table in this section.*

---

### Table V-1 — Predicted vs. Actual
*Gate: ANALYST rows only. Execute before Table V-2 gate is present in your output.*
*Rationale for each delta must appear in the same row — not in a separate section.*

| Metric | Role | Predicted | Actual | Delta | Why the delta is what it is |
|--------|------|-----------|--------|-------|-----------------------------|
| [metric] | ANALYST | [value] | [value] | [±] | [reason co-located here] |
| B-00 | ANALYST | [null prediction] | [control reading] | [±] | [diverged in predicted direction: YES/NO — reason co-located] |
| **Completion** | ANALYST | **V-1 COMPLETE — key delta = [phrase], B-00 comparison = [diverged in predicted direction: YES/NO, magnitude: stated]** | | | |

### Table V-2 — Verdict
*Gate: Execute after Table V-1 completion row is present. Execute before Table V-3 gate is present in your output.*

| Field | Role | Value | Rationale |
|-------|------|-------|-----------|
| Verdict | ANALYST | Confirmed / Refuted / Inconclusive | [connects V-1 delta to verdict; references B-00 comparison] |
| **Completion** | ANALYST | **V-2 COMPLETE — verdict = [Confirmed / Refuted / Inconclusive]** | |

### Table V-3 — Counter-Evidence
*Gate: Execute after Table V-2 completion row is present. Execute before Table V-4 gate is present in your output.*
*This table must close with one of exactly two dispositions. Silence does not pass.*

| Element | Role | Content | Disposition |
|---------|------|---------|-------------|
| Counter-interpretation | ANALYST | [Named alternative reading — OR — "None"] | |
| Rebuttal / Reason | ANALYST | [Why it does not hold using E-2 / V-1 evidence — OR — why none is plausible] | |
| **Completion** | ANALYST | **V-3 COMPLETE — DISPOSITION A: counter = [name], rebuttal = [summary]** — OR — **DISPOSITION B: no plausible counter; reason = [stated]** | |

### Table V-4 — Limitations and Next Step
*Gate: Execute after Table V-3 completion row is present. Execute before Table V-5 gate is present in your output.*
*This table must close with one of exactly two dispositions.*

| Element | Role | Content |
|---------|------|---------|
| Limitation | ANALYST | [One specific confound or constraint — not a generic disclaimer] |
| Next step | ANALYST | [One specific action — "do more research" does not pass] |
| **Completion** | ANALYST | **V-4 COMPLETE — DISPOSITION A: limitation = [named], next step = [named]** — OR — **DISPOSITION B: [what prevented naming these, and why]** |

### Table V-5 — Replication Path
*Gate: Execute after Table V-4 completion row is present in your output.*
*This table must close with one of exactly two dispositions.*

| Step | Role | Action |
|------|------|--------|
| 1 | ANALYST | [Every tool, input, command — no implicit steps; confirm or supplement E-1 steps] |
| 2 | ANALYST | [Continue for every step] |
| **Completion** | ANALYST | **V-5 COMPLETE — DISPOSITION A: replication path complete** — OR — **DISPOSITION B: [steps that cannot be specified, and why]** |

**EVALUATE GATE COMPLETE — verdict = [Confirmed/Refuted/Inconclusive], B-00 comparison = [diverged in predicted direction: YES/NO, magnitude: stated], counter-evidence = [DISPOSITION A/B], limitation = [named], next step = [named], replication = [DISPOSITION A/B]**
````

---

## V-03 — Single Axis: Lifecycle Emphasis (Four Dedicated Containers: CALIBRATE / DESIGN / EXECUTE / ANALYZE)

**Variation axis**: Lifecycle emphasis — four named lifecycle containers where the first container (CALIBRATE) holds only the inertia baseline, making B-00 a structurally isolated first gate that precedes hypothesis setup; EXECUTE holds two roles (BUILDER + RECORDER), ensuring container boundaries and role boundaries diverge

**Hypothesis**: Isolating the inertia baseline in its own dedicated lifecycle container (CALIBRATE), sequenced before the DESIGN container, structurally prevents B-00 from being authored with any hypothesis knowledge, because the CALIBRATE container closes before DESIGN opens — enforcing baseline isolation through document structure rather than through role prohibitions alone.

---

````markdown
You are producing a `prove-prototype` artifact organized within four lifecycle containers.
Each container maps onto a distinct stage of the experimental method.

| Container | Stage | Holds | Role(s) |
|-----------|-------|-------|---------|
| LIFECYCLE: CALIBRATE | Pre-setup | B-00 inertia baseline only | CALIBRATOR |
| LIFECYCLE: DESIGN | Setup | Hypothesis, scope, measurement criteria | FRAMER |
| LIFECYCLE: EXECUTE | Action | Construction and raw observation | BUILDER + RECORDER |
| LIFECYCLE: ANALYZE | Analysis | Comparison, verdict, counter-evidence, limits, replication | ANALYST |

**Why four containers**: B-00 in its own container (CALIBRATE) ensures the baseline is
committed before the hypothesis is restated. CALIBRATE closes; then DESIGN opens.
A reader scanning container boundaries alone can verify this ordering without reading content.

**Structural independence (C-25)**: Container scan reads four `## LIFECYCLE: X` headers.
Role scan reads five role-block labels (CALIBRATOR / FRAMER / BUILDER / RECORDER / ANALYST),
where EXECUTE holds two roles. These are different structural granularities.

---

## ROLES AND PROHIBITIONS

| Role | Container | Writes | Must Not Write |
|------|-----------|--------|----------------|
| CALIBRATOR | CALIBRATE | B-00 baseline and null prediction | Hypothesis, scope, build steps, results |
| FRAMER | DESIGN | Hypothesis, scope, measurement criteria | B-00 values, build steps, observations |
| BUILDER | EXECUTE | Construction, replication steps | Measurement outcomes, interpretations, verdicts |
| RECORDER | EXECUTE | Raw observations including B-00 control | Comparisons, interpretations, verdicts |
| ANALYST | ANALYZE | Comparison, verdict, counter-evidence, limits, replication | New observations, build re-description |

---

## LIFECYCLE: CALIBRATE
*One phase. B-00 only. No hypothesis. No scope. No build content. No observed values.*
*CALIBRATE closes before LIFECYCLE: DESIGN opens.*

---

### PHASE C-1 — INERTIA BASELINE
*CALIBRATOR. Execute before all other phases. First substantive element of this output.*
*B-00 is frozen at the close of this phase. It may not be revised in any later phase.*
*Execute before Phase D-1 gate is present in your output.*

CALIBRATOR: — Must not state the hypothesis, define prototype scope, describe construction,
or reference results. Must not define measurement criteria.

Name the status-quo condition or do-nothing alternative that the prototype competes against.
State what would be observed if no prototype were built (B-00 null prediction).

**B-00 Name**: [name]
**B-00 Description**: [what the baseline condition is — current behavior, existing tool, control]
**B-00 Null Prediction**: [expected outcome under B-00 if hypothesis does not hold]

**PHASE C-1 COMPLETE — CALIBRATOR: B-00 = [name], null prediction = [stated outcome], frozen**

**CALIBRATE GATE COMPLETE — B-00 = [name + null prediction]**

---

## LIFECYCLE: DESIGN
*Phases D-1 through D-3. Establish hypothesis, scope, and measurement criteria.*
*Execute after CALIBRATE GATE is present in your output.*
*DESIGN closes before LIFECYCLE: EXECUTE opens.*
*No build content. No observed values. No evaluation content.*

---

### PHASE D-1 — HYPOTHESIS
*FRAMER. Execute after CALIBRATE GATE is present in your output.*
*Execute before Phase D-2 gate is present in your output.*

FRAMER: — Must not describe construction steps, report observations, modify B-00, or render a verdict.

Restate the hypothesis being tested. This is a claim that the prototype will produce a result
that diverges from B-00 in a specified direction.

**Hypothesis**: [the falsifiable claim]
**Confirmed if**: [observable outcome that confirms — state in relation to B-00 where relevant]
**Refuted if**: [observable outcome that refutes]

**PHASE D-1 COMPLETE — FRAMER: hypothesis = [one-phrase restatement]**

---

### PHASE D-2 — SCOPE
*FRAMER. Execute after Phase D-1 completion line is present in your output.*
*Execute before Phase D-3 gate is present in your output.*

FRAMER: — Must not describe construction steps, report observations, modify B-00, or render a verdict.

Name at least two exclusions. Co-locate the validity rationale in the same row.

| Excluded item | Why the hypothesis remains testable without it |
|---------------|------------------------------------------------|
| [item] | [reason — "it wasn't needed" does not answer this question] |
| [item] | [reason] |

**PHASE D-2 COMPLETE — FRAMER: scope = [prototype name in one phrase], exclusions = [N], each validity-justified**

---

### PHASE D-3 — MEASUREMENT CRITERIA
*FRAMER. Execute after Phase D-2 completion line is present in your output.*
*Criteria frozen here. Execute before any LIFECYCLE: EXECUTE phase.*

FRAMER: — Must not describe construction steps, report observations, or render a verdict.

| Metric | Collection method | Success condition | Failure condition | B-00 reference value |
|--------|-------------------|-------------------|-------------------|-----------------------|
| [metric] | [how observed] | [value that confirms] | [value that refutes] | [B-00 expected reading] |

No observed values in this phase.

**PHASE D-3 COMPLETE — FRAMER: metric = [name], success = [value], B-00 reference = [value], criteria frozen**

**DESIGN GATE COMPLETE — hypothesis = [phrase], scope exclusions = [N], metric = [name + threshold], B-00 reference = [value]**

---

## LIFECYCLE: EXECUTE
*Phases E-1 and E-2. Build and observe. No evaluation. No verdicts. B-00 is read-only.*
*Execute after DESIGN GATE is present in your output.*
*Two roles run here: BUILDER then RECORDER.*
*EXECUTE closes before LIFECYCLE: ANALYZE opens.*

---

### PHASE E-1 — BUILD
*BUILDER. Execute after DESIGN GATE is present in your output.*
*Execute before Phase E-2 gate is present in your output.*

BUILDER: — Must not record measurement outcomes, interpret results, render a verdict, or modify B-00.

Describe what was built. State the minimality trade-off in the same block.
List all tools, inputs, and steps for replication.

**What Was Built**: [description]
**Tools and Inputs**: [every tool, library, input, configuration — no implicit entries]
**Minimality Trade-off**: [what was omitted] — [why the hypothesis can still be tested without it]

**Build Steps**:
1. [step]
2. [step]
3. [continue for every step]

**PHASE E-1 COMPLETE — BUILDER: prototype = [name], steps = [N], replication = [COMPLETE — all steps listed | PARTIAL — missing: (list)]**

---

### PHASE E-2 — RAW OBSERVATIONS
*RECORDER. Execute after Phase E-1 completion line is present in your output.*
*Execute before any LIFECYCLE: ANALYZE phase.*

RECORDER: — Must not compare observations to predictions, interpret meaning, or render a verdict.

Record what was observed for each metric. At least one concrete data point per metric.
Include a B-00 control reading using the same collection method as Phase D-3.

| Metric | Observed value | Context/notes |
|--------|----------------|---------------|
| [metric] | [value] | [observation context] |
| B-00 control | [measured baseline value] | [how B-00 condition was observed] |

**PHASE E-2 COMPLETE — RECORDER: observed = [metric = value], B-00 control = [measured value]**

**EXECUTE GATE COMPLETE — prototype = [name], metrics observed = [N], B-00 control = [value vs. null prediction: stated]**

---

## LIFECYCLE: ANALYZE
*Phases A-1 through A-5. Evaluate evidence. No new observations. No build re-description.*
*Execute after EXECUTE GATE is present in your output.*
*One role runs here: ANALYST.*

---

### PHASE A-1 — PREDICTED VS. ACTUAL
*ANALYST. Execute after EXECUTE GATE is present in your output.*
*Execute before Phase A-2 gate is present in your output.*

ANALYST: — Must not add new observations or re-describe the build.

For each metric, state prediction, observation, delta, and co-locate the rationale in the same
row. Include a B-00 comparison row.

| Metric | Predicted | Actual | Delta | Why the delta is what it is |
|--------|-----------|--------|-------|-----------------------------|
| [metric] | [value] | [value] | [±] | [reason co-located here] |
| B-00 | [null prediction from C-1] | [control reading from E-2] | [±] | [diverged from B-00 in predicted direction: YES/NO — reason] |

**PHASE A-1 COMPLETE — ANALYST: key delta = [phrase], B-00 comparison = [experimental result vs. null prediction, diverged in predicted direction: YES/NO, magnitude: stated]**

---

### PHASE A-2 — VERDICT
*ANALYST. Execute after Phase A-1 completion line is present in your output.*
*Execute before Phase A-3 gate is present in your output.*

ANALYST: — Must not add new observations or re-describe the build.

**Verdict**: Confirmed / Refuted / Inconclusive [choose one]
**Reasoning**: [connects Phase A-1 delta to verdict — not a restatement of A-1; references B-00 comparison]

**PHASE A-2 COMPLETE — ANALYST: verdict = [Confirmed / Refuted / Inconclusive]**

---

### PHASE A-3 — COUNTER-EVIDENCE
*ANALYST. Execute after Phase A-2 completion line is present in your output.*
*Execute before Phase A-4 gate is present in your output.*
*This phase must close with one of exactly two dispositions.*

ANALYST: — Must not add new observations or re-describe the build.

If a counter-interpretation exists:
- **Counter-interpretation**: [the alternative reading of Phase E-2 / A-1 evidence]
- **Rebuttal**: [why it does not hold, using that evidence; reference B-00 readings where relevant]

If none exists:
- **Counter-interpretation**: None
- **Reason**: [why no alternative reading of the evidence is plausible]

Write exactly one terminal element:

A) `PHASE A-3 COMPLETE — ANALYST: DISPOSITION A — counter-interpretation = [name]; rebuttal = [summary]`
B) `PHASE A-3 COMPLETE — ANALYST: DISPOSITION B — no plausible counter-interpretation; reason = [stated]`

---

### PHASE A-4 — LIMITATIONS AND NEXT STEP
*ANALYST. Execute after Phase A-3 completion line is present in your output.*
*Execute before Phase A-5 gate is present in your output.*
*This phase must close with one of exactly two dispositions.*

ANALYST: — Must not add new observations or re-describe the build.

**Limitation**: [one specific confound or constraint — not a generic disclaimer]
**Next step**: [one specific action — "do more research" does not pass]

Write exactly one terminal element:

A) `PHASE A-4 COMPLETE — ANALYST: DISPOSITION A — limitation = [named]; next step = [named]`
B) `PHASE A-4 COMPLETE — ANALYST: DISPOSITION B — [what prevented naming, and why]`

---

### PHASE A-5 — REPLICATION PATH
*ANALYST. Execute after Phase A-4 completion line is present in your output.*
*This phase must close with one of exactly two dispositions.*

ANALYST: — Must not add new observations or re-describe the build.

Complete replication path. Confirm that Phase E-1 steps are sufficient, or add what is missing.
No implicit steps. Configuration files named.

Write exactly one terminal element:

A) `PHASE A-5 COMPLETE — ANALYST: DISPOSITION A — replication path complete; steps in Phase E-1`
B) `PHASE A-5 COMPLETE — ANALYST: DISPOSITION B — [steps missing from Phase E-1, and why]`

**ANALYZE GATE COMPLETE — verdict = [Confirmed/Refuted/Inconclusive], B-00 comparison = [diverged in predicted direction: YES/NO, magnitude: stated], counter-evidence = [DISPOSITION A/B], limitation = [named], next step = [named], replication = [DISPOSITION A/B]**
````

---

## V-04 — Single Axis: Phrasing Register (Conversational Second-Person Imperatives)

**Variation axis**: Phrasing register — all instructions are conversational, second-person, and imperative throughout; section headers use plain-English questions; role names use plain occupational labels (THINKER, ANCHOR, MAKER, WATCHER, JUDGE); structural requirements are identical to V-01 but the register is accessible rather than technical

**Hypothesis**: Conversational, second-person phrasing produces equivalent structural compliance to formal technical phrasing when the underlying structural requirements — gate markers co-located at action points, model-written completion lines with substantive values, binary dispositions on optional sections, role prohibitions, lifecycle containers — are form-independent and do not rely on formal vocabulary for enforcement.

---

````markdown
You're going to run a prototype experiment and document it. Here's how this works: you move
through three stages. Each stage has a gate. You can't start the next stage until you've
finished the current one and marked it done.

Two labeling systems run at the same time:
- **Stage labels** (`## STAGE: X`) are coarse checkpoints — they mark where you are in the experiment.
- **Role labels** mark who writes what inside each stage — they're finer-grained than stages.

Reading stage labels catches sequence errors: did you record observations before you defined
what to measure? Reading role labels catches content errors: did the wrong voice sneak in?
These are two separate checks. Run them independently.

Two stages hold two roles each (SETUP and BUILD), which means stage-boundary scans and
role-label scans cross different structural levels. They detect different problems.

---

## WHO WRITES WHAT (AND WHAT THEY CAN'T TOUCH)

| Role | Stage | Writes | Cannot write |
|------|-------|--------|-------------|
| THINKER | SETUP | Hypothesis, scope exclusions, measurement criteria | B-00, build steps, results, verdicts |
| ANCHOR | SETUP | B-00 inertia baseline | Hypothesis, scope, build steps, results |
| MAKER | BUILD | Construction steps, tools, replication path | Outcome values, interpretations, verdicts |
| WATCHER | BUILD | Raw observations | Comparisons, interpretations, verdicts |
| JUDGE | CLOSE | Comparison, verdict, counter-argument, limits, replication path | New observations, build re-description |

---

## STAGE: SETUP
*Do all four steps here before anything in BUILD or CLOSE appears.*

---

### Step 1: What are you testing?
*THINKER writes this. It's the first thing in your output.*
*Write this before Step 2 appears below.*

THINKER: — Don't touch build steps, B-00, observations, or verdicts.

Restate the hypothesis. One falsifiable claim. Say what confirms it and what refutes it.

**Hypothesis**: [what you're testing]
**Confirmed if**: [what you'd observe]
**Refuted if**: [what you'd observe instead]

**STEP 1 DONE — THINKER: hypothesis = [one-phrase restatement]**

---

### Step 2: What's in (and out)?
*THINKER writes this. Write after Step 1 is marked done.*
*Write before Step 3 appears below.*

THINKER: — Don't touch build steps, B-00, observations, or verdicts.

Say what the prototype does. Then name at least two things it deliberately doesn't do, and
for each one, explain right there — in the same line — why that doesn't invalidate the test.

| Excluded item | Why the test still works without it |
|---------------|-------------------------------------|
| [item] | [reason — don't just say "not needed"] |
| [item] | [reason] |

**STEP 2 DONE — THINKER: scope = [prototype name], exclusions = [N], each with co-located rationale**

---

### Step 3: How will you measure success?
*THINKER writes this. Write after Step 2 is marked done.*
*Write before Step 4 appears below. These thresholds are locked — they can't change after BUILD begins.*

THINKER: — Don't touch build steps, B-00, or results.

For each thing you'll measure, say exactly what success looks like and what failure looks like.

| What to measure | Success | Failure |
|----------------|---------|---------|
| [metric] | [threshold] | [threshold] |

**STEP 3 DONE — THINKER: metric = [name], success threshold = [value], locked before build**

---

### Step 4: What are you competing against? (B-00)
*ANCHOR writes this. Write after Step 3 is marked done.*
*Write before any BUILD content. B-00 is locked here — it cannot change after this step.*

ANCHOR: — Don't bring in any hypothesis knowledge, scope, build steps, or results.

Name the do-nothing alternative — the thing that's already working, or what happens if you
build nothing at all. That's B-00. Then say what B-00 would produce if your hypothesis is wrong.

**B-00**: [name it + describe it]
**If the hypothesis is wrong, B-00 produces**: [null outcome]

**STEP 4 DONE — ANCHOR: B-00 = [name], null outcome = [stated], locked**

**SETUP GATE COMPLETE — hypothesis = [phrase], scope = [N in / M excluded, each justified], metric = [name + threshold], B-00 = [name + null outcome]**

---

## STAGE: BUILD
*Start here only after SETUP GATE is marked complete above.*
*Two roles run here: MAKER then WATCHER.*

---

### Step 5: What did you build?
*MAKER writes this. Write after SETUP GATE is marked complete.*
*Write before Step 6 appears below.*

MAKER: — Don't record what happened when you measured it. No outcomes, no interpretations.

Describe the prototype. Name every tool and input you used. State the minimality trade-off
right here — what you left out, and why the hypothesis can still be tested without it.

**Built**: [description]
**Tools / inputs**: [list everything — no implicit entries]
**Left out (minimality trade-off)**: [what was omitted] — [why it's okay]

**Build steps for replication**:
1. [step]
2. [step]
3. [continue for every step]

**STEP 5 DONE — MAKER: prototype = [name], steps = [N], replication = [COMPLETE — all steps listed | PARTIAL — missing: (list)]**

---

### Step 6: What did you observe?
*WATCHER writes this. Write after Step 5 is marked done.*
*Write before any CLOSE content. Record only — don't compare, don't interpret.*

WATCHER: — Record raw data only. No comparisons, no meaning, no verdict.

Write down exactly what you saw for each measure. Include at least one concrete number or
data point. Also record the B-00 control reading — what you saw under the baseline condition.

| Measure | Observed | Notes |
|---------|----------|-------|
| [metric] | [value] | [context] |
| B-00 control | [value] | [how the baseline condition was measured] |

**STEP 6 DONE — WATCHER: observed = [metric = value, B-00 control = value]**

**BUILD GATE COMPLETE — prototype = [name], metrics observed = [N], B-00 control measured = [value vs. null outcome: stated]**

---

## STAGE: CLOSE
*Start here only after BUILD GATE is marked complete above.*
*One role runs here: JUDGE.*

---

### Step 7: How did prediction compare to reality?
*JUDGE writes this. Write after BUILD GATE is marked complete.*
*Write before Step 8 appears below.*

JUDGE: — No new observations. Don't re-describe the build.

For each measure, put the prediction next to the actual result. Write the delta. State right
there — same row or same labeled block — why you got that delta. Include a B-00 row.

| Measure | Predicted | Actual | Delta | Why |
|---------|-----------|--------|-------|-----|
| [metric] | [value] | [value] | [±] | [reason, co-located here] |
| B-00 | [null outcome] | [control reading] | [±] | [diverged in predicted direction: YES/NO — reason] |

**STEP 7 DONE — JUDGE: key delta = [phrase], B-00 comparison = [diverged in predicted direction: YES/NO, magnitude: stated]**

---

### Step 8: What's the verdict?
*JUDGE writes this. Write after Step 7 is marked done.*
*Write before Step 9 appears below.*

JUDGE: — No new observations. Don't re-describe the build. Ground this in Step 7 evidence.

**Verdict**: Confirmed / Refuted / Inconclusive
**Why**: [point to specific observations from Step 7 that support it; reference B-00 comparison]

**STEP 8 DONE — JUDGE: verdict = [Confirmed / Refuted / Inconclusive]**

---

### Step 9: Is there a counter-argument?
*JUDGE writes this. Write after Step 8 is marked done.*
*Write before Step 10 appears below.*
*You must close with one of two specific answers — don't leave this open-ended.*

JUDGE: — No new observations. Don't re-describe the build.

Pick exactly one:
- **Yes, there's a counter-interpretation**: [Name it.] But here's why the evidence doesn't support it: [rebuttal grounded in Steps 6–7, including B-00 readings where relevant].
- **No, there's no plausible counter-interpretation**: [Say so explicitly.] Here's why: [reason].

Write exactly one terminal element:

A) `STEP 9 DONE — JUDGE: DISPOSITION A — counter = [name], rebuttal = [summary]`
B) `STEP 9 DONE — JUDGE: DISPOSITION B — no plausible counter; reason = [stated]`

---

### Step 10: What are the limits? What's next?
*JUDGE writes this. Write after Step 9 is marked done.*
*Write before Step 11 appears below.*
*You must close with one of two specific answers.*

JUDGE: — No new observations. Don't re-describe the build.

**Limitation**: [One honest constraint on this prototype or measurement — not a generic disclaimer]
**Next step**: [One concrete follow-on action — "do more research" doesn't pass]

Write exactly one terminal element:

A) `STEP 10 DONE — JUDGE: DISPOSITION A — limitation = [named], next step = [named]`
B) `STEP 10 DONE — JUDGE: DISPOSITION B — [what prevented naming these, and why]`

---

### Step 11: Can someone else reproduce this?
*JUDGE writes this. Write after Step 10 is marked done.*
*You must close with one of two specific answers.*

JUDGE: — No new observations. Don't re-describe the build.

Pick exactly one:
- **Yes, it's reproducible**: Everything someone needs is in Step 5 above.
- **Not fully**: Here's what's missing from Step 5: [list what's absent and why].

Write exactly one terminal element:

A) `STEP 11 DONE — JUDGE: DISPOSITION A — replication path complete; all steps in Step 5`
B) `STEP 11 DONE — JUDGE: DISPOSITION B — [steps missing from Step 5, and why]`

**CLOSE GATE COMPLETE — verdict = [Confirmed/Refuted/Inconclusive], B-00 comparison = [diverged in predicted direction: YES/NO, magnitude: stated], counter = [DISPOSITION A/B], limitation = [named], next step = [named], replication = [DISPOSITION A/B]**
````

---

## V-05 — Single Axis: Inertia Framing (B-00 as Absolute First Element; B-00 in Every Completion Line)

**Variation axis**: Inertia framing — B-00 is the very first output element (precedes hypothesis restatement); every completion line from the BUILD phase onward encodes a B-00 comparison value; the hypothesis is explicitly framed as a directional claim against B-00; a dedicated LIFECYCLE: BASELINE container holds only B-00; the lifecycle sequence is BASELINE / DEFINE / BUILD / ANALYZE

**Hypothesis**: When B-00 is established as the structurally first element and its value is embedded in every downstream completion line, a reviewer scanning only completion lines can perform a full two-chain audit without reading phase bodies: chain 1 (was each phase completed with its result?) and chain 2 (did the experimental outcome diverge from B-00 in the predicted direction?) are both legible from the completion-line sequence alone.

---

````markdown
You are producing a `prove-prototype` artifact. The inertia baseline (B-00) is the first
element of this output. The hypothesis comes second. Everything that follows is framed
against B-00.

**Why B-00 first**: A baseline introduced after results are known is retrofitted, not
controlled. B-00 must precede any hypothesis restatement to prevent hypothesis framing
from influencing what the baseline is.

**Two-chain audit**: Every completion line from BUILD onward carries a B-00 comparison value.
A reviewer scanning only completion lines can determine:
- Chain 1: was each phase completed with its experimental result?
- Chain 2: did the outcome diverge from B-00 in the predicted direction?
Both chains are readable from completion lines alone.

**Structural independence (C-25)**: Container scan reads four `## LIFECYCLE: X` headers
(BASELINE / DEFINE / BUILD / ANALYZE). Role scan reads four role-block labels
(ANCHOR / FRAMER / BUILDER+MEASURER / ARBITER), where BUILD holds two roles.
Container scan traverses section level; role scan traverses block level within sections.
These are different structural granularities.

---

## ROLES AND PROHIBITIONS

| Role | Container | Writes | Must Not Write |
|------|-----------|--------|----------------|
| ANCHOR | BASELINE | B-00 name, description, null prediction | Hypothesis, scope, build steps, results |
| FRAMER | DEFINE | Hypothesis (framed as directional claim against B-00), scope, measurement criteria | Build steps, observations, verdicts; may read B-00 but not modify |
| BUILDER | BUILD | Construction, replication steps | Measurement outcomes, interpretations, verdicts |
| MEASURER | BUILD | Raw observations including B-00 control | Comparisons, interpretations, verdicts |
| ARBITER | ANALYZE | Comparison against B-00, verdict, counter-evidence, limits, replication | New observations, build re-description |

---

## LIFECYCLE: BASELINE
*One phase. B-00 only. First section of this output. Nothing precedes it.*
*BASELINE closes before LIFECYCLE: DEFINE opens.*

---

### PHASE B-1 — INERTIA BASELINE (B-00)
*ANCHOR writes this. It is the first substantive element of the entire output.*
*Execute before any other phase. B-00 is frozen at the completion line.*
*Execute before Phase F-1 gate is present in your output.*

ANCHOR: — Must not state the hypothesis, define scope, describe construction, or reference results.

Name the status-quo condition: what would be observed if no prototype were built.
This is B-00 — the inertia the prototype must overcome or diverge from.
State what B-00 null prediction looks like across the metric you will measure.

**B-00 Name**: [name]
**B-00 Description**: [what the baseline condition is — existing behavior, control group, do-nothing state]
**B-00 Null Prediction**: [the specific outcome B-00 produces if the hypothesis does not hold;
use the same metric and units as your measurement criteria will use]

**PHASE B-1 COMPLETE — ANCHOR: B-00 = [name], null prediction = [stated outcome + metric value], frozen**

**BASELINE GATE COMPLETE — B-00 = [name], null prediction = [value]**

---

## LIFECYCLE: DEFINE
*Phases F-1 through F-3. Establish hypothesis (framed against B-00), scope, and measurement criteria.*
*Execute after BASELINE GATE is present in your output.*
*DEFINE closes before LIFECYCLE: BUILD opens.*

---

### PHASE F-1 — HYPOTHESIS
*FRAMER. Execute after BASELINE GATE is present in your output.*
*Execute before Phase F-2 gate is present in your output.*

FRAMER: — Must not describe construction steps, modify B-00, report observations, or render a verdict.

Restate the hypothesis as a directional claim: the prototype will produce an outcome that
differs from B-00 in a specified direction and magnitude.

**Hypothesis**: [the falsifiable claim — state explicitly how it diverges from B-00]
**Confirmed if**: [observable outcome that confirms — reference B-00 direction: above / below / different from B-00]
**Refuted if**: [observable outcome that refutes — what would constitute no divergence from B-00]

**PHASE F-1 COMPLETE — FRAMER: hypothesis = [one-phrase restatement including B-00 direction claim]**

---

### PHASE F-2 — SCOPE
*FRAMER. Execute after Phase F-1 completion line is present in your output.*
*Execute before Phase F-3 gate is present in your output.*

FRAMER: — Must not describe construction steps, modify B-00, report observations, or render a verdict.

Name at least two exclusions. Co-locate the validity rationale in the same row.

| Excluded item | Why the hypothesis remains testable without it |
|---------------|------------------------------------------------|
| [item] | [reason] |
| [item] | [reason] |

**PHASE F-2 COMPLETE — FRAMER: scope = [prototype name], exclusions = [N], each validity-justified**

---

### PHASE F-3 — MEASUREMENT CRITERIA
*FRAMER. Execute after Phase F-2 completion line is present in your output.*
*Criteria frozen here. Execute before any LIFECYCLE: BUILD phase.*

FRAMER: — Must not describe construction steps, modify B-00, report observations, or render a verdict.

| Metric | Collection method | Success condition | Failure condition | B-00 reference value |
|--------|-------------------|-------------------|-------------------|----------------------|
| [metric] | [how observed] | [value confirms hypothesis] | [value refutes hypothesis] | [B-00 null prediction from Phase B-1] |

No observed values in this phase.

**PHASE F-3 COMPLETE — FRAMER: metric = [name], success = [value], B-00 reference = [value from B-1], criteria frozen**

**DEFINE GATE COMPLETE — hypothesis = [phrase vs. B-00], scope = [N excluded], metric = [name + threshold], B-00 reference = [value]**

---

## LIFECYCLE: BUILD
*Phases G-1 and G-2. Build and observe. No verdicts. B-00 is read-only.*
*Execute after DEFINE GATE is present in your output.*
*Two roles run here: BUILDER then MEASURER.*
*BUILD closes before LIFECYCLE: ANALYZE opens.*

---

### PHASE G-1 — CONSTRUCTION
*BUILDER. Execute after DEFINE GATE is present in your output.*
*Execute before Phase G-2 gate is present in your output.*

BUILDER: — Must not record measurement outcomes, interpret results, render a verdict, or modify B-00.

Describe what was built. State the minimality trade-off in the same block.
List all tools, inputs, and steps for replication.

**What Was Built**: [description]
**Tools and Inputs**: [every tool, library, input, configuration — no implicit entries]
**Minimality Trade-off**: [what was omitted] — [why the hypothesis can still be tested]

**Build Steps**:
1. [step]
2. [step]
3. [continue for every step]

**PHASE G-1 COMPLETE — BUILDER: prototype = [name], steps = [N], B-00 reference read = [value from F-3], replication = [COMPLETE — all steps listed | PARTIAL — missing: (list)]**

---

### PHASE G-2 — RAW OBSERVATIONS
*MEASURER. Execute after Phase G-1 completion line is present in your output.*
*Execute before any LIFECYCLE: ANALYZE phase.*

MEASURER: — Must not compare to predictions, interpret meaning, or render a verdict.

Record what was observed. At least one concrete data point per metric.
Measure both the experimental condition and the B-00 control condition.

| Metric | Observed value | Context/notes |
|--------|----------------|---------------|
| [metric] | [experimental value] | [observation context] |
| B-00 control | [measured baseline value] | [how B-00 condition was observed; same collection method as F-3] |

**PHASE G-2 COMPLETE — MEASURER: experimental = [value], B-00 control = [measured value], B-00 null prediction from B-1 = [restated], delta direction visible = [experimental above / below / at B-00: stated without interpretation]**

**BUILD GATE COMPLETE — prototype = [name], experimental observed = [value], B-00 control measured = [value], null prediction = [value], raw direction = [above/below/at B-00]**

---

## LIFECYCLE: ANALYZE
*Phases H-1 through H-5. Evaluate evidence. No new observations. No build re-description.*
*Execute after BUILD GATE is present in your output.*
*One role runs here: ARBITER.*

---

### PHASE H-1 — PREDICTED VS. ACTUAL (B-00 COMPARISON)
*ARBITER. Execute after BUILD GATE is present in your output.*
*Execute before Phase H-2 gate is present in your output.*

ARBITER: — Must not add new observations or re-describe the build.

For each metric, state prediction, observation, delta, and rationale co-located in the same row.
The B-00 row is required. State whether the experimental outcome diverged from B-00 in the
predicted direction.

| Metric | Predicted | Actual | Delta | Why the delta is what it is |
|--------|-----------|--------|-------|-----------------------------|
| [metric] | [success threshold from F-3] | [experimental value from G-2] | [±] | [reason co-located here] |
| B-00 | [null prediction from B-1] | [control reading from G-2] | [±] | [diverged from B-00 in predicted direction: YES/NO — reason co-located] |

**PHASE H-1 COMPLETE — ARBITER: experimental delta = [phrase], B-00 comparison = [experimental value vs. B-00 null prediction, diverged in predicted direction: YES/NO, magnitude: stated]**

---

### PHASE H-2 — VERDICT
*ARBITER. Execute after Phase H-1 completion line is present in your output.*
*Execute before Phase H-3 gate is present in your output.*

ARBITER: — Must not add new observations or re-describe the build.

**Verdict**: Confirmed / Refuted / Inconclusive [choose one]
**Reasoning**: [connects H-1 delta to verdict — not a restatement of H-1; states what B-00 comparison implies for the verdict]
**B-00 implication**: [what the B-00 delta means for the decision this prototype informs]

**PHASE H-2 COMPLETE — ARBITER: verdict = [Confirmed / Refuted / Inconclusive], B-00 implication = [stated in one phrase]**

---

### PHASE H-3 — COUNTER-EVIDENCE
*ARBITER. Execute after Phase H-2 completion line is present in your output.*
*Execute before Phase H-4 gate is present in your output.*
*This phase must close with one of exactly two dispositions.*

ARBITER: — Must not add new observations or re-describe the build.

If a counter-interpretation exists:
- **Counter-interpretation**: [the alternative reading of Phase G-2 / H-1 evidence]
- **Rebuttal**: [why it does not hold, using G-2 and H-1 evidence; address whether B-00 comparison survives the counter-interpretation]

If none exists:
- **Counter-interpretation**: None
- **Reason**: [why no alternative reading is plausible; include whether B-00 direction could be explained otherwise]

Write exactly one terminal element:

A) `PHASE H-3 COMPLETE — ARBITER: DISPOSITION A — counter = [name]; rebuttal including B-00 = [summary]`
B) `PHASE H-3 COMPLETE — ARBITER: DISPOSITION B — no plausible counter; B-00 direction unambiguous: [reason]`

---

### PHASE H-4 — LIMITATIONS AND NEXT STEP
*ARBITER. Execute after Phase H-3 completion line is present in your output.*
*Execute before Phase H-5 gate is present in your output.*
*This phase must close with one of exactly two dispositions.*

ARBITER: — Must not add new observations or re-describe the build.

**Limitation**: [one specific confound — consider especially threats to B-00 control validity]
**Next step**: [one specific action — consider a cleaner B-00 control, extended test, or replication]

Write exactly one terminal element:

A) `PHASE H-4 COMPLETE — ARBITER: DISPOSITION A — limitation = [named]; next step = [named], B-00 gap addressed: [YES/NO — how]`
B) `PHASE H-4 COMPLETE — ARBITER: DISPOSITION B — [what prevented naming these, and why]`

---

### PHASE H-5 — REPLICATION PATH
*ARBITER. Execute after Phase H-4 completion line is present in your output.*
*This phase must close with one of exactly two dispositions.*

ARBITER: — Must not add new observations or re-describe the build.

Complete replication path including B-00 control measurement procedure.
Confirm Phase G-1 steps are sufficient, or add what is missing.
A reader unfamiliar with this work replicates both the experimental condition and the B-00
control from this phase alone.

Write exactly one terminal element:

A) `PHASE H-5 COMPLETE — ARBITER: DISPOSITION A — replication complete: experimental steps in G-1, B-00 control procedure = [stated here or referenced to G-1]`
B) `PHASE H-5 COMPLETE — ARBITER: DISPOSITION B — [steps missing from G-1, including B-00 procedure gaps, and why]`

**ANALYZE GATE COMPLETE — verdict = [Confirmed/Refuted/Inconclusive], B-00 comparison = [experimental vs. null prediction, diverged in predicted direction: YES/NO, magnitude: stated], B-00 implication = [stated], counter-evidence = [DISPOSITION A/B], limitation = [named, B-00 gap: YES/NO], next step = [named], replication = [DISPOSITION A/B including B-00 procedure]**
````

---

## Design Rationale: Why These Five Satisfy C-25

The prior-round failure (R6 V-04, V-05) was one role per lifecycle container — making container and role boundaries coincide. Each R7 variation breaks coincidence differently:

| Variation | Break mechanism | Container count | Role count | Roles per container (max) |
|-----------|----------------|-----------------|------------|---------------------------|
| V-01 | DEFINE holds FRAMER + CALIBRATOR; EXECUTE holds BUILDER + RECORDER | 3 | 5 | 2 |
| V-02 | Role labels in table `Role` column vs. section-header containers — different structural dimensions, not just different counts | 3 | 5 | All (column values, not block headers) |
| V-03 | EXECUTE holds BUILDER + RECORDER; 4 containers, 5 roles | 4 | 5 | 2 |
| V-04 | Same mechanism as V-01 in conversational register | 3 | 5 | 2 |
| V-05 | BUILD holds BUILDER + MEASURER; 4 containers, 4 roles | 4 | 4 | 2 |

**V-02 is the strongest C-25 case**: role labels are column values in tables, lifecycle containers are section headers — two entirely different structural dimensions that cannot be made to coincide regardless of how many roles map to a container.

**V-05 is the strongest C-26 case**: B-00 appears in every completion line from BUILD onward, and the ANALYZE GATE COMPLETE line encodes both chains explicitly. V-03 is the strongest lifecycle-independence case: CALIBRATE as an isolated B-00-only container makes the baseline's structural position unambiguous.
