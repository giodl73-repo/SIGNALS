Reading the scorecard carefully for PASS+ signals and structural notes before writing.

From the R17 scorecard, three new patterns emerge:

1. **V-01 C-13 PASS+** — entry conditions *read the prior artifact file*, extract the concrete value from disk, and validate the in-flight signal against that extracted value. Mismatch = CHAIN INTEGRITY FAILURE. This is tamper-**resistant** (artifact is the source of truth), not just tamper-evident (signal carries the value). Distinct from C-13 which only requires live payload.

2. **V-03 C-14 PASS+** — Stage 5 declares **three** named blocks, not two: CONFIDENCE CHAIN RESOLUTION → COUNTER-HYPOTHESIS RESOLUTION → DISPLACEMENT INTEGRITY CHECK, with synthesis hard-gated on BLOCK 3 completion. Extends C-14's dual-block floor.

3. **V-02 C-14 note** — dependency-driven block inversion: when BLOCK M requires output from BLOCK N (M < N by declaration order), execution inverts to N-before-M to satisfy the data dependency. Declared structure preserved; execution order adapts causally. New structural pattern, not covered by C-14.

These become C-15, C-16, C-17. Aspirational denominator updates to 9.

---

```markdown
---
skill: quest-rubric
skill_target: prove-topic
date: 2026-03-16
version: 17
---

# prove-topic Rubric — v17

## Overview

Scores the `prove-topic` orchestration skill. The skill runs five sub-skills in order
(prove-hypothesis → prove-websearch → prove-intelligence → prove-analysis →
prove-synthesize), grounding the hypothesis in a prior scout artifact and writing one
artifact per stage. Final output is an evidence brief ready for `topic-story`.

Seventeen criteria total: 5 essential, 3 recommended, 9 aspirational.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 9 * 10)
```

**Golden threshold**: all 5 essential pass AND composite >= 80.

---

## Essential Criteria

All five must pass. A single essential failure makes the output not useful.

---

### C-01 — All five sub-skills orchestrated in sequence

- **Weight**: essential
- **Category**: correctness

**Pass condition**: The response includes all five evidence stages — hypothesis,
web-search, intelligence (internal sources), analysis, and synthesize — presented in
that order with a clear stage boundary between each. Missing any stage is a FAIL.
A stage present but out of order is a FAIL. A stage named but skipped or delegated
to the user is a FAIL.

---

### C-02 — Scout artifact loaded and named before hypothesis formation

- **Weight**: essential
- **Category**: behavior

**Pass condition**: Before the hypothesis stage begins, the response explicitly names
a scout artifact (e.g., `{topic}-scout-record-{date}.md`) as the source that grounds
the hypothesis. General knowledge used without referencing a named scout artifact is
a FAIL. A vague "use your scout research" instruction without naming the file is a FAIL.

---

### C-03 — Progressive artifact writes — one per stage, not batched

- **Weight**: essential
- **Category**: behavior

**Pass condition**: Each stage produces exactly one WRITE instruction followed by a
confirmation signal before the next stage begins. All five writes batched at the end
is a FAIL. A stage that produces output but defers the write is a FAIL. A stage that
writes more than one artifact is a FAIL.

---

### C-04 — Minimum count thresholds enforced at each evidence stage

- **Weight**: essential
- **Category**: correctness

**Pass condition**: Stage 2 (websearch) gates on count >= 5; Stage 3 (intelligence)
gates on count >= 3; Stage 4 (analysis) gates on count >= 3. Each gate must be
explicit — a threshold stated as a requirement, not an aspiration. Proceeding without
meeting the gate is a FAIL. Omitting the gate entirely is a FAIL.

---

### C-05 — Synthesis integrates evidence from all prior stages

- **Weight**: essential
- **Category**: correctness

**Pass condition**: The synthesize stage references output from Stages 2, 3, and 4 by
count or label. A synthesis that re-derives conclusions without citing stage outputs
is a FAIL. A synthesis present but disconnected from the evidence chain is a FAIL.

---

## Recommended Criteria

Strongly expected. Missing one caps the composite below 90.

---

### C-06 — Numeric confidence chain with delta tracking

- **Weight**: recommended
- **Category**: structure

**Pass condition**: A numeric 1-10 confidence chain is maintained across stages with
named delta terms: `prior`, `s2_delta`, `s3_delta`, `s4_delta`, and a `chain_equation`
that sums them to a `final` value. All terms must be explicitly named. A narrative
confidence description without numeric deltas is a FAIL. A final score without a
chain equation is a FAIL.

---

### C-07 — Counter-hypothesis tracked through to resolution

- **Weight**: recommended
- **Category**: behavior

**Pass condition**: A counter-hypothesis is declared in Stage 1 and carried forward.
The synthesize stage includes an explicit resolution block that returns one of:
REFUTED, PARTIALLY REFUTED, or OPEN RISK, with supporting evidence. A
counter-hypothesis declared but not resolved is a FAIL. No counter-hypothesis at all
is a FAIL.

---

### C-08 — Resume audit before execution

- **Weight**: recommended
- **Category**: behavior

**Pass condition**: Before Stage 1 begins, the skill runs a Glob pre-scan of
existing artifacts and emits RESUME-SKIP or RUN decisions per stage. A
RESUME AUDIT EXIT signal fires if all stages are already complete. Proceeding
without a resume check when prior artifacts may exist is a FAIL.

---

## Aspirational Criteria

Distinguish good output from excellent output. Each adds ~1.1 composite points.

---

### C-09 — Three named roles confirmed before Stage 1

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: Three named roles — SCOUT LOADER, INERTIA ANALYST, and
CAMPAIGN DIRECTOR — are declared and confirmed before Stage 1 begins. A role
invoked mid-run without prior declaration does not satisfy this criterion. Fewer than
three named roles is a FAIL.

---

### C-10 — Three-point displacement loop

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: A displacement loop is present with three explicit components:
a ROLE 2 displacement anchor established at Stage 3, an `s4_aggregate_displacement_verdict`
at Stage 4, and a `displacement_conclusion` in synthesis. All three must be named and
linked. A displacement verdict without an anchor is a FAIL. An anchor without a
verdict is a FAIL.

---

### C-11 — Compound exit signals with dual-value payload

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: Exit signals at each evidence stage carry two values simultaneously:
a count and a running_confidence. Both must be present in the same signal emission.
A signal that carries only a count or only a confidence value does not satisfy this
criterion.

---

### C-12 — Count-gated exit — threshold enforced in signal, not prose

- **Weight**: aspirational
- **Category**: correctness

**Pass condition**: Each evidence stage includes an explicit gate instruction of the
form "Do not fire exit signal until count >= N." The gate must appear as a hard
constraint in the stage definition, not as a prose suggestion. A threshold mentioned
in the overview but absent from the stage gate is a FAIL.

---

### C-13 — Live payload chaining between stages

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: Exit signals carry live numeric state as payload
(e.g., `hypothesis_locked(confidence_prior=62)`) and the receiving stage's ENTRY
CONDITION validates the specific value, not just the signal name. Count-threshold
variant also satisfies: `websearch_complete(count=N)` → `count >= 5` gate reads N
from the signal. Bare named chaining without payload validation does not satisfy
this criterion.

---

### C-14 — Stage 5 dual-block structure

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: The synthesize stage declares at least two explicitly named,
sequenced resolution blocks: BLOCK 1 CONFIDENCE CHAIN RESOLUTION (containing the
chain_equation) and BLOCK 2 COUNTER-HYPOTHESIS RESOLUTION. Both must be named as
blocks with declared execution order. A single synthesis summary section without
block demarcation is a FAIL.

---

### C-15 — Artifact extraction for chain tamper-resistance

- **Weight**: aspirational
- **Category**: correctness

**Pass condition**: Entry conditions at each stage do not merely check an in-flight
signal value — they read the prior stage's artifact from disk, extract the concrete
value written there, and validate the in-flight signal against the extracted value.
A mismatch between artifact and signal triggers CHAIN INTEGRITY FAILURE and halts
execution. This makes the chain tamper-resistant (artifact is authoritative source),
not merely tamper-evident (signal self-reports). A chain that trusts signal payload
without artifact verification does not satisfy this criterion.

---

### C-16 — Three-block synthesis with displacement integrity gate

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: Stage 5 declares three explicitly named, sequenced blocks:
BLOCK 1 CONFIDENCE CHAIN RESOLUTION, BLOCK 2 COUNTER-HYPOTHESIS RESOLUTION,
BLOCK 3 DISPLACEMENT INTEGRITY CHECK. BLOCK 3 must enforce consistency between the
C-10 displacement verdict and the confidence chain, and synthesis cannot close until
BLOCK 3 completes. A two-block structure (C-14 floor) without the displacement
integrity gate does not satisfy this criterion.

---

### C-17 — Dependency-driven block inversion

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: When a block declared earlier in Stage 5 depends on a value
computed by a block declared later (e.g., BLOCK 1 requires `cr_delta` produced by
BLOCK 2), the execution order explicitly inverts to satisfy the data dependency —
BLOCK 2 runs before BLOCK 1 — and the inversion is annotated with an ORDER
CONSTRAINT stating the causal reason. The declared block structure is preserved;
only execution sequence adapts. An arbitrary reordering without causal annotation
does not satisfy this criterion. A structure with no dependency-driven inversion
need not address this criterion; it applies only when the dependency is present.
```
