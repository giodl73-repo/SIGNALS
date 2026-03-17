**v19 written.** Here's what changed from v18:

**Header**: `version: 18 → 19`, criteria count `Twenty → Twenty-two (5 essential, 3 recommended, **14** aspirational)`.

**Formula**: aspirational denominator `/ 12 → / 14` (each aspirational now worth ~0.71 pts instead of 0.83).

**Two new aspirational criteria from R19 excellence signals:**

| Criterion | Pattern | Source |
|-----------|---------|--------|
| **C-21** — Stage 4 tri-value exit | Stage 4 exit carries count + `running_confidence` + `displacement_momentum_final` simultaneously — the only stage where both chains have resolved their final values; bridges confidence chain and displacement chain in one signal | V-03 C-11 PARTIAL |
| **C-22** — Per-row VERDICT in THREE-STAGE DISPLACEMENT CHAIN table | Each S2/S3/S4 row carries an explicit VERDICT (SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED) alongside INCUMBENT DELTA SUM — `chain_pattern` names the arc but does not substitute for per-stage stance | V-03 C-20 PARTIAL |

**Scoring note**: V-03 under v19 scores: C-09(P), C-11(Pa), C-14(P), C-16(P), C-19(P), C-20(Pa) → pass 4 full + 2 partial. Aspirational: 4 × 0.71 + 2 × 0.36 = 2.84 + 0.71 = 3.55. Score: **60 + 20 + 3.55 = 83.55** (up from 83.33 under v18 denominator — the denominator change is offset by the unchanged pass count; V-03 neither gains nor loses new criteria relative to v19).
fore hypothesis formation

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

Distinguish good output from excellent output. Each adds ~0.71 composite points.

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

---

### C-18 — Multi-field inter-stage validation

- **Weight**: aspirational
- **Category**: correctness

**Pass condition**: Entry conditions at Stages 3 and 4 read the prior artifact from
disk and extract and validate **two independent fields simultaneously** — both
`running_confidence` AND `displacement_momentum` — comparing each against the
in-flight signal. Both validations must be present at each boundary; a mismatch on
either field triggers CHAIN INTEGRITY FAILURE. A single-field disk read (C-15 floor)
without the second field does not satisfy this criterion. This creates two independent
tamper-resistant proof chains at every inter-stage boundary, not one.

---

### C-19 — Momentum trajectory as conclusion ceiling

- **Weight**: aspirational
- **Category**: correctness

**Pass condition**: In Stage 5 BLOCK 3, the trajectory direction of
`displacement_momentum` (ACCELERATING / DECELERATING / FLAT) acts as a hard ceiling
on `displacement_conclusion` — a DECELERATING trajectory forces the conclusion to
PARTIALLY SUPPORTED or lower even when `displacement_momentum_final` is positive.
Trajectory must be computed explicitly (not inferred from the final value alone) and
its ceiling effect on the conclusion must be stated as a rule, not an editorial note.
A displacement conclusion that reads only the final momentum value without checking
trajectory direction does not satisfy this criterion.

---

### C-20 — Per-stage delta column in BLOCK 3 with arc naming

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: BLOCK 3 presents a THREE-STAGE DISPLACEMENT CHAIN table with a
per-stage row for S2, S3, and S4 individually. The table includes an INCUMBENT DELTA
SUM column (cumulative delta through each stage) alongside the aggregate verdict per
stage. A `chain_pattern` field names the arc described by the delta sequence (e.g.,
ACCELERATING, REVERSAL, PLATEAU). Each row flagged as divergent requires an explicit
`conclusion_justification` reconciliation before synthesis closes. A BLOCK 3 that
checks only the final Stage 4 verdict without the per-stage delta table does not
satisfy this criterion.

---

### C-21 — Stage 4 tri-value exit: count + running_confidence + displacement_momentum_final

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: The Stage 4 exit signal carries three named values simultaneously:
a count, a `running_confidence`, and a `displacement_momentum_final`. All three must
be present in the same signal emission. A Stage 4 exit carrying count +
running_confidence (C-11 floor) without `displacement_momentum_final` does not satisfy
this criterion. A Stage 4 exit carrying count + displacement_momentum_final without
`running_confidence` does not satisfy this criterion. This bridges both the confidence
chain and the displacement chain in a single boundary signal at the final evidence
stage — the only stage where both chains have resolved their final values.

---

### C-22 — Per-row VERDICT column in THREE-STAGE DISPLACEMENT CHAIN table

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: The THREE-STAGE DISPLACEMENT CHAIN table (C-20 floor) includes a
VERDICT column alongside the INCUMBENT DELTA SUM column. Each row (S2, S3, S4) carries
an explicit per-stage VERDICT (e.g., SUPPORTED, PARTIALLY SUPPORTED, NOT SUPPORTED)
representing that stage's independent displacement finding — not the cumulative
conclusion and not the overall `chain_pattern`. A table with `chain_pattern` and
INCUMBENT DELTA SUM but no per-row VERDICT column does not satisfy this criterion.
The per-row VERDICT makes each stage's contribution to the arc individually auditable;
`chain_pattern` names the arc but does not substitute for per-row verdicts.
