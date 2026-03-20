## simulate-argument R5 — Variation Set

Written to `simulations/quest/variations/simulate-argument-variations-R5-2026-03-19.md`.

### Gap analysis: R4 V-04/V-05 fail all three new v5 criteria

| Criterion | R4 failure mode |
|-----------|----------------|
| C-18 | Phase 4 says "CP intersection: YES/NO" — a verdict, not an audit loop |
| C-19 | "The Logician's pass is closed" — a label, not an identity commitment; the Reviewer is not bound |
| C-20 | Gap traces to Phase 3 Advocate assumption, not a Phase 0 pre-committed generalization |

### Variation axes

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **Axis** | C-20 (Phase 0 Gen-registry) | C-18 (CP priority audit loop) | C-19 (identity-anchored closure) | C-20 + C-19 | All three + four specialists |

### Key mechanisms introduced

**V-01**: Phase 0 gains a generalization registry (`Gen-01`, `Gen-02`...). UNSUPPORTED-GEN Gap fields must write `"Needed [Gen-N: exact pre-committed claim], found only Y"`. Phase 4 closing adds a generalization accountability step per Gen-ID.

**V-02**: Phase 4 closing replaces binary "CP intersection: YES/NO" with a structured per-CP-step accountability report — Phase 0 prediction, trace outcome, CONFIRMED/DISCONFIRMED verdict, and a structural risk distribution statement.

**V-03**: Phase 3 closure language becomes first-person identity commitments: `"I, the Logician, commit the above form identifications. The Reviewer is bound to these forms. Any conflict is an INVALID-FORM candidate, not a reclassification."` The Chair's verdicts close with `"I, the Committee Chair, commit..."`.

**V-04**: Gen-registry + identity-anchored roles. The Reviewer's identity commitment explicitly includes accountability to Phase 0 Gen-IDs — making Gen-ID tracing structurally natural rather than a Gap-writing instruction.

**V-05**: All three + four specialists. The Advocate references Phase 0 Gen-IDs in best readings, connecting Phase 3 per-step advocacy directly to Phase 0 pre-commitment. Phase 4 runs both CP priority audit and generalization accountability. First variation predicted to hit 12/12 aspirational.
n pre-commitment changes UNSUPPORTED-GEN fault precision.

**V-02 — CP priority audit loop**: Phase 4 closing replaces the binary "CP intersection: YES/NO" with a structured per-CP-step accountability report. For each CP-flagged step, state Phase 0's prediction, the trace outcome, and an accountability verdict (CONFIRMED / DISCONFIRMED / CONFIRMED-ELSEWHERE). Tests whether making the audit loop explicit changes P1 severity assignment and Phase 4 synthesis quality.

**V-03 — Identity-anchored closure language**: Phase 3 role boundaries reformulated as first-person identity commitments with explicit binding constraints: "I, the Logician, commit these form identifications. The Reviewer is bound to the Logician's forms — disagreement is an INVALID-FORM candidate, not a reclassification." Tests whether identity enforcement at the form-ID/validity boundary changes INVALID-FORM fault detection.

**V-04 — Phase 0 generalization registry + identity-anchored roles**: V-01's Gen-registry combined with V-03's identity-anchored closure. Tests whether identity framing makes Gen-ID tracing more natural for the Reviewer: does "I, the Reviewer, am bound to test against the Logician's forms and the Phase 0 generalizations" make commitment-relative Gap fields structurally inevitable?

**V-05 — All three (C-18 + C-19 + C-20) + four specialists**: Phase 0 carries four pre-commitments (best-case, H0, CP, Gen-registry). Four named specialists: Logician → Advocate → Reviewer → Chair, all identity-anchored. Phase 4 closing is a five-step audit. The Advocate references Phase 0 Gen-IDs when committing best readings, connecting Phase 3 per-step advocacy to Phase 0 pre-commitment — so Gap fields satisfy C-20 structurally. Maximum R5 coverage.

### New excellence signals (R5 targets)

- **phase-0-gen-registry**: Phase 0 names an explicit table of generalizations (Gen-IDs) before reading. UNSUPPORTED-GEN Gap fields cite Gen-IDs. Phase 4 closes with a generalization accountability step. This makes C-20 structurally inevitable rather than dependent on model behavior at Gap-writing time.
- **cp-priority-audit-loop**: Phase 4 closing is a per-CP-step accountability report — not a binary intersection verdict. Each CP-flagged step receives its own accountability line: prediction, outcome, verdict. The loop between structural priority and fault severity is explicit and auditable.
- **identity-bound-role-handoff**: First-person closure language at role boundaries binds the next role to the prior role's committed outputs. The Reviewer cannot silently reclassify the Logician's forms; the Chair cannot re-run validity checks. Identity enforcement makes temporal separation structurally load-bearing rather than a labeling convention.

### Predicted v5 rubric coverage

| Criterion | R4 V-04 (v5 baseline) | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|---|
| C-09 term drift | PASS | = | = | = | = | = |
| C-10 structural weakness | PASS | **stronger** (Gen-IDs force load-bearing gap characterization) | **stronger** (per-step audit loop connects faults to structural priority) | = | **stronger** | **strongest** |
| C-11 falsification target | PASS | = | = | = | = | = |
| C-12 inline reviewer hook | PASS | = | = | **stronger** (Chair's identity framing makes hook first-person) | **stronger** | **strongest** |
| C-13 fault pattern closure | PASS | **stronger** (gen accountability step names fault class per Gen-ID) | **stronger** (audit loop names dominant class per CP prediction outcome) | = | **stronger** | **strongest** |
| C-14 fault class taxonomy | PASS | = | = | = | = | = |
| C-15 reviewer depth tier | PASS | = | = | = | = | = |
| C-16 null-hypothesis verdict | PASS | PASS | PASS | PASS | PASS | PASS |
| C-17 form-ID sub-pass | PASS | PASS | PASS | **PASS** (identity binding strengthens enforcement) | **PASS** | **PASS** |
| C-18 CP audit loop | **FAIL** | FAIL | **PASS** | FAIL | FAIL | **PASS** |
| C-19 named handoff | **FAIL** | FAIL | FAIL | **PASS** | **PASS** | **PASS** |
| C-20 Phase 0 gap accounts | **FAIL** | **PASS** | FAIL | FAIL | **PASS** | **PASS** |

**Predicted v5 scores**: V-01 → 10/12, V-02 → 10/12, V-03 → 10/12, V-04 → 11/12, V-05 → **12/12**.

---

## V-01 — Axis: C-20 (Phase 0 Generalization Registry)

**Hypothesis**: R4 variations write UNSUPPORTED-GEN Gap fields either as assertions ("the generalization lacks empirical support") or as Advocate-relative accounts ("Advocate required X; Reviewer found Y") — both trace to Phase 3 per-step commitments, not Phase 0. C-20 requires Gap fields to reference a claim pre-committed *before reading*. Adding a named generalization registry to Phase 0 (Gen-01, Gen-02...) creates the structural anchor: UNSUPPORTED-GEN Gap fields must write "Needed [Gen-N: the pre-committed generalization], found only [what the evidence provides]." Phase 4 closing adds a generalization accountability step: for each Gen-ID, confirm or deny fault registration. Tests whether Phase 0 generalization pre-commitment changes the precision of UNSUPPORTED-GEN fault characterization and forces the Gap field to be a structural account rather than an assertion.

**What changes from R4 V-04**: Phase 0 adds a pre-committed generalizations table (Gen-IDs). Phase 3B Reviewer notes which Gen-ID a claim corresponds to (if any). Phase 4 Fault Register Gap field format for UNSUPPORTED-GEN must cite a Gen-ID. Phase 4 Closing gains a step 5 generalization accountability check. Everything else from R4 V-04 unchanged: named roles (Logician/Reviewer/Chair), H0 in Phase 0 (C-16), form-ID sub-pass before validity checks (C-17), CP? column (from R4 V-04 baseline, carried here for completeness).

---

You are running /simulate-argument for: {{topic}}

Three specialists examine every argument. Before any specialist begins, you will pre-commit to which claims the paper is expected to generalize beyond direct evidence. Each generalization gets a Gen-ID. When UNSUPPORTED-GEN faults are found, they must trace back to a named Phase 0 generalization — not assert failure independently. The adversary is inertia: the belief that no structural revision is needed.

---

## PHASE 0 — ARGUMENT SETUP

State three things before any specialist begins:

**Best-case argument** (one paragraph): What would this argument look like if fully sound?
> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

**Null hypothesis** (one sentence): The case for inertia.
> "H0: This argument is structurally sound and requires no revision before submission."

**Pre-committed generalizations**: Name the claims you expect this paper to generalize beyond its direct evidence — the inferences you predict will extend further than the data licenses. If you cannot name them before reading, write TBD and revise after Phase 1.

| Gen-ID | Generalization | Why expected |
|--------|----------------|--------------|
| Gen-01 | [claim text — the specific generalization you predict] | [why you expect this to lack direct evidence] |
| Gen-02 | | |

Minimum: 2 generalizations. These are your UNSUPPORTED-GEN accountability targets. Phase 4 UNSUPPORTED-GEN Gap fields must cite a Gen-ID from this table. An assertion-only Gap ("no empirical support for this claim") does not pass.

These three commitments are your trace targets. Phase 4 will return to all of them.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

After reading, revise Phase 0 if necessary:
- Update the best-case paragraph if the paper's scope differs from your initial read.
- Revise the Gen registry to reflect the paper's actual generalizations. Each Gen-ID should name a specific claim in the paper that extends beyond its direct evidence support.
- Revise H0 only if scope is materially different.

Then proceed.

---

## PHASE 2 — CLAIM MAP

The claim map is the shared record all three specialists work from.

| C-ID | Claim | Type | Depends on | Status |
|------|-------|------|------------|--------|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify |
| C-02 | | inference | C-01 | to-verify |

Types:
- **premise**: accepted without proof in this paper (cited or stated as assumption)
- **definition**: introduces a term that subsequent claims depend on
- **empirical**: requires data or citation to support
- **inference**: follows logically from prior claims
- **conclusion**: the paper's output claims

Minimum: 6 claims. At least one per major section. Definition claims are high priority — they are where DEF-DRIFT originates. Where a claim corresponds to a Phase 0 Gen-ID, note it in the Claim column: e.g., `[Gen-01] The protocol generalizes across institutional contexts.`

> Do not proceed to PHASE 3 until every claim has an ID and dependencies are mapped.

---

## PHASE 3 — SPECIALIST TRACE

Phase 3 runs as three specialist passes in sequence. Each specialist completes their pass across ALL inference steps before the next begins. Specialists do not revise prior commitments.

### 3A — THE LOGICIAN (Form Identification)

The Logician's task: name the logical form of every inference step. The Logician classifies; the Logician does not evaluate. No validity assessments in this pass.

```
FORM [C-ID]: [claim text]
Role: Logician
Logical form: [modus ponens / modus tollens / hypothetical syllogism / disjunctive syllogism /
               abduction / inductive generalization / argument from analogy /
               argument from authority / causal inference / other: describe]
Formal structure: [If/Then/Therefore skeleton in 1–3 lines]
```

> The Logician's pass is closed. All forms committed. The Empirical Reviewer begins.

### 3B — THE EMPIRICAL REVIEWER (Validity Checks)

The Reviewer's task: test whether the premises hold for every inference step using the forms the Logician committed. No verdicts — verdicts belong to the Chair. For inductive generalization forms, note the matching Gen-ID from Phase 0 (if any). If DRIFT is found, name the term, the definition claim C-ID, and how the meaning shifted.

```
CHECK [C-ID]: [claim text]
Role: Empirical Reviewer
  Gen-ID match: [Gen-NN — if this corresponds to a Phase 0 pre-committed generalization / —]
  (1) Logical: given the Logician's form, does the conclusion follow from the premises?
              [YES] / [WEAK — valid only under assumption: state it explicitly] / [NO — describe the gap]
  (2) Empirical: are the premises empirically supported?
              [YES] / [CITED: ref] / [ASSUMED: what is taken for granted] / [UNSUPPORTED: what evidence is needed]
  (3) Consistency: are key terms used consistently with their definition claims?
              [YES] / [DRIFT: term, definition claim C-ID, how it shifted]
```

> The Empirical Reviewer's pass is closed. All checks committed. The Committee Chair begins.

### 3C — THE COMMITTEE CHAIR (Verdicts)

The Chair's task: synthesize the Logician's form classifications and the Reviewer's validity checks into verdicts. For every WEAK or BROKEN verdict, the Chair assesses fault depth as a domain specialist would.

```
VERDICT [C-ID]: SOUND / WEAK / BROKEN
Role: Committee Chair
Reason: [one sentence — why SOUND holds, or what makes it WEAK/BROKEN]
If WEAK or BROKEN:
  Reviewer flag: As committee chair, would you flag this in a written review? YES/NO — one-sentence justification
  Depth tier: OBVIOUS / NOTABLE / SIGNIFICANT
    OBVIOUS — any careful reader notices without domain expertise
    NOTABLE — a methodologically careful reader notices
    SIGNIFICANT — only a domain specialist catches it on first read
  Domain comparison: [one sentence — what domain standard, expectation, or prior result does this gap violate?]
```

---

## PHASE 4 — FAULT REGISTER

Every WEAK or BROKEN verdict from the Committee Chair (3C) must appear here.

Fault classes (assign exactly one per row):
- **DEF-DRIFT**: a key term shifts meaning between its definition claim and its use
- **UNSUPPORTED-GEN**: a generalization extends beyond what the evidence licenses — Gap must cite a Gen-ID from Phase 0
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure does not match the form committed by the Logician in 3A

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity |
|------|------|---------|-------|-----|--------------|----------|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [structural explanation] | [exact claim, evidence, or definition change that closes the gap] | P1/P2/P3 |

Severity: P1 = breaks central conclusion / P2 = weakens key section / P3 = precision issue

**Gap field format for UNSUPPORTED-GEN faults** — cite the Phase 0 Gen-ID:
> `[NOTABLE] Needed [Gen-01: the claim that the protocol generalizes across institutional contexts], found only single-site evidence — no cross-institutional variance data is reported; a methods reviewer would require multi-site validation before accepting the generalization.`

An assertion-only gap ("no empirical support for this claim") does not pass for UNSUPPORTED-GEN. The Gap must name the specific Phase 0 pre-committed generalization.

**Phase 4 Closing — Null Rejection Test + Generalization Accountability**:

Run the closing in five steps:
1. Count rows per class code. Name the dominant fault class by code (most rows).
2. Count P1-severity faults. If P1 count ≥ 1: "H0 is rejected." If P1 count = 0, assess whether P2 faults collectively challenge the central argument.
3. State the inertia verdict: "H0 is [rejected / not rejected]. Inertia — submitting without revision — is [not defensible / defensible with minor fixes / defensible]."
4. Synthesize whether the dominant fault class confirms or refutes the Phase 0 best-case statement. Name the dominant class using structural vocabulary (e.g., unsupported generalization, definitional drift).
5. Generalization accountability: For each Gen-ID from Phase 0, state the trace outcome:
   > "Gen-01: [F-ID — UNSUPPORTED-GEN fault registered, P_-severity / No fault — evidence was sufficient for this generalization]."

---

## PHASE 5 — AMEND

Three structural fixes ordered P1 → P2 → P3. Each references the F-ID, C-ID, and Class code it addresses.

1. [P1 fix — F-ID, C-ID, Class: exact repair — what claim, evidence, or definition change closes this fault]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-02 — Axis: C-18 (Critical-Path Priority Audit Loop)

**Hypothesis**: R4 V-01/V-04/V-05 close Phase 4 with "CP intersection: YES/NO" — a binary verdict. C-18 requires an audit loop: for each CP-flagged step, the closing must state the Phase 0 prediction, the trace outcome, and an accountability verdict connecting fault severity to structural priority. The difference between a verdict and an audit loop: a verdict asks "did P1 land on a CP step?"; an audit loop asks "Phase 0 predicted C-XX as the most load-bearing step — the trace found [fault / no fault] on it — therefore the structural priority assessment was [accurate / inaccurate], and the actual risk distribution is [description]." Tests whether making the priority accountability loop explicit — rather than just checking intersection — changes Phase 4 synthesis quality and P1 severity assignment. A model that knows it must account for every CP prediction may assign P1 more carefully.

**What changes from R4 V-04**: Phase 4 Closing replaces the single "CP intersection: YES/NO" statement (step 4) with a structured per-CP-step accountability report — prediction, outcome, verdict, and a final structural risk assessment. All other mechanisms from R4 V-04 unchanged: Phase 0 CP commitment, Phase 2 CP? column, named roles (C-19 table stakes), H0 (C-16), form-ID sub-pass (C-17).

---

You are running /simulate-argument for: {{topic}}

Three specialists examine every argument. Before any specialist begins, you will commit to which inference steps are most load-bearing. When the trace is complete, Phase 4 will run a structured audit: for each pre-committed load-bearing step, what did the trace find — and does the fault distribution confirm or contradict the structural priority assessment? The audit loop between pre-committed priority and post-trace fault severity is the accountability mechanism. The adversary is inertia: the belief that no structural revision is needed.

---

## PHASE 0 — ARGUMENT SETUP

State three things before any specialist begins:

**Best-case argument** (one paragraph): What would this argument look like if fully sound?
> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

**Null hypothesis** (one sentence): The case for inertia.
> "H0: This argument is structurally sound and requires no revision before submission."

**Critical path** (one to three sentences): Which 2–3 inference steps are most load-bearing — the ones the conclusion would collapse without? Name them with enough specificity to identify them by C-ID in Phase 2. Write TBD if you cannot name them before reading; revise after Phase 1.
> "The conclusion depends most heavily on [inference type or topic area]. If that step fails, [consequence for the conclusion]."

These three commitments are your trace targets. Phase 4 will audit whether the predicted load-bearing steps produced the most severe faults.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

After reading, revise Phase 0 if necessary. Update the critical-path description to name specific C-IDs once Phase 2 is complete. Mark each critical-path inference with YES in the CP? column.

Then proceed.

---

## PHASE 2 — CLAIM MAP

| C-ID | Claim | Type | Depends on | Status | CP? |
|------|-------|------|------------|--------|-----|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify | — |
| C-02 | | inference | C-01 | to-verify | YES / — |

Types:
- **premise**: accepted without proof (cited or stated as assumption)
- **definition**: introduces a term that subsequent claims depend on
- **empirical**: requires data or citation to support
- **inference**: follows logically from prior claims
- **conclusion**: the paper's output claims

Minimum: 6 claims. At least one per major section. Mark critical-path inferences with `YES` in CP?.

> Do not proceed to PHASE 3 until every claim has an ID, dependencies are mapped, and CP? flags are assigned.

---

## PHASE 3 — SPECIALIST TRACE

Phase 3 runs as three specialist passes in sequence. Each specialist completes their pass across ALL inference steps before the next begins.

### 3A — THE LOGICIAN (Form Identification)

The Logician names the logical form of every inference step. No evaluation. CP-flagged steps are noted for the Reviewer and Chair's attention.

```
FORM [C-ID] [CP? YES/—]: [claim text]
Role: Logician
Logical form: [modus ponens / modus tollens / hypothetical syllogism / disjunctive syllogism /
               abduction / inductive generalization / argument from analogy /
               argument from authority / causal inference / other: describe]
Formal structure: [If/Then/Therefore skeleton in 1–3 lines]
```

> The Logician's pass is closed. All forms committed. The Empirical Reviewer begins.

### 3B — THE EMPIRICAL REVIEWER (Validity Checks)

The Reviewer tests whether the premises hold using the Logician's committed forms. No verdicts. If DRIFT is found, name the term, the definition claim C-ID, and how the meaning shifted.

```
CHECK [C-ID]: [claim text]
Role: Empirical Reviewer
  (1) Logical: given the Logician's form, does the conclusion follow from the premises?
              [YES] / [WEAK — valid only under assumption: state it explicitly] / [NO — describe the gap]
  (2) Empirical: are the premises empirically supported?
              [YES] / [CITED: ref] / [ASSUMED: what is taken for granted] / [UNSUPPORTED: what evidence is needed]
  (3) Consistency: are key terms used consistently with their definition claims?
              [YES] / [DRIFT: term, definition claim C-ID, how it shifted]
```

> The Empirical Reviewer's pass is closed. All checks committed. The Committee Chair begins.

### 3C — THE COMMITTEE CHAIR (Verdicts)

The Chair synthesizes both specialist passes into verdicts. CP-flagged steps receive explicit severity attention. For every WEAK or BROKEN verdict, the Chair characterizes fault depth as a domain specialist would.

```
VERDICT [C-ID]: SOUND / WEAK / BROKEN
Role: Committee Chair
Reason: [one sentence — why SOUND holds, or what makes it WEAK/BROKEN]
If WEAK or BROKEN:
  Reviewer flag: As committee chair, would you flag this in a written review? YES/NO — one-sentence justification
  Depth tier: OBVIOUS / NOTABLE / SIGNIFICANT
    OBVIOUS — any careful reader notices without domain expertise
    NOTABLE — a methodologically careful reader notices
    SIGNIFICANT — only a domain specialist catches it on first read
  Domain comparison: [one sentence — what domain standard or prior result does this gap violate?]
```

---

## PHASE 4 — FAULT REGISTER

Every WEAK or BROKEN verdict from the Committee Chair (3C) must appear here.

Fault classes (assign exactly one per row):
- **DEF-DRIFT**: a key term shifts meaning between its definition claim and its use
- **UNSUPPORTED-GEN**: a generalization extends beyond what the evidence licenses
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure does not match the form committed by the Logician

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity | CP? |
|------|------|---------|-------|-----|--------------|----------|-----|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [structural explanation] | [exact change needed] | P1/P2/P3 | YES/— |

Severity: P1 = breaks central conclusion / P2 = weakens key section / P3 = precision issue

Gap field: begin with the depth tier tag from 3C in brackets.

**Phase 4 Closing — Null Rejection Test + Critical Path Priority Audit**:

Run the closing in five steps:
1. Count rows per class code. Name the dominant fault class by code (most rows).
2. Count P1-severity faults. If P1 count ≥ 1: "H0 is rejected." If P1 count = 0, assess whether P2 faults collectively challenge the central argument.
3. State the inertia verdict: "H0 is [rejected / not rejected]. Inertia — submitting without revision — is [not defensible / defensible with minor fixes / defensible]."
4. Synthesize whether the dominant fault class confirms or refutes the Phase 0 best-case statement. Name the dominant class using structural vocabulary.
5. Critical path priority audit — for each CP-flagged step committed in Phase 0, write one accountability line:
   > "CP audit [C-ID]: Phase 0 predicted this step as load-bearing. Trace outcome: [F-ID at P_-severity / SOUND — no fault]. Accountability: [CONFIRMED — the pre-committed load-bearing step carried the most severe fault / DISCONFIRMED — step survived; fault [F-ID] on non-CP step [C-ID] was more severe / CONFIRMED-ELSEWHERE — step survived; but a CP-adjacent step carried a P1 fault]."

   After all CP steps are audited, state: "Structural risk distribution: [one sentence — where the actual structural risk lies vs. where Phase 0 predicted it, and what this implies for revision priority]."

---

## PHASE 5 — AMEND

Three structural fixes ordered P1 → P2 → P3. Each references F-ID, C-ID, and Class code.

1. [P1 fix — F-ID, C-ID, Class: exact repair — what claim, evidence, or definition change closes this fault]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-03 — Axis: C-19 (Identity-Anchored Closure Language)

**Hypothesis**: R4 V-02/V-04 have named roles with closure language ("The Logician's pass is closed. All forms committed."). C-19 says anonymous gates and role labels with no closure language fail — identity must be the enforcement mechanism. The difference: a label says "this sub-section is complete"; an identity commitment binds the next role to the prior role's outputs. First-person closure language — "I, the Logician, commit the above form identifications. The Reviewer is bound to these forms — structural disagreement is an INVALID-FORM candidate, not a reclassification" — creates role accountability at the form-ID/validity boundary. Tests whether identity-anchored first-person closure language changes how the model handles the boundary: do INVALID-FORM fault rates change? Does the model treat form classification as a prior commitment rather than a sliding interpretation?

**What changes from R4 V-04**: Phase 3 closure language at each role boundary reformulated as first-person identity commitments with explicit binding constraints. Role introductions state the identity constraint. 3C verdict format includes "I, the Committee Chair, commit" language. All structural mechanisms from R4 V-04 unchanged: Phase 0 CP commitment, Phase 2 CP? column, H0 (C-16), form-ID sub-pass (C-17), CP? in Fault Register.

---

You are running /simulate-argument for: {{topic}}

The Logician, the Empirical Reviewer, and the Committee Chair examine every argument in strict sequence. Each specialist commits their findings under their role identity. The Reviewer is bound to the Logician's committed forms and cannot reclassify them — structural disagreement between the Reviewer's validity findings and the Logician's committed forms is an INVALID-FORM candidate. The Chair is bound to both prior analyses and cannot re-run validity checks or reclassify forms. The adversary is inertia: the belief that no structural revision is needed.

---

## PHASE 0 — ARGUMENT SETUP

State three things before any specialist begins:

**Best-case argument** (one paragraph): What would this argument look like if fully sound?
> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

**Null hypothesis** (one sentence): The case for inertia.
> "H0: This argument is structurally sound and requires no revision before submission."

**Critical path** (one to three sentences): Which 2–3 inference steps are most load-bearing? Write TBD if you cannot name them before reading; revise after Phase 1.
> "The conclusion depends most heavily on [inference type or topic area]. If that step fails, [consequence for the conclusion]."

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

After reading, revise Phase 0 if necessary. Update the critical path to name specific C-IDs once Phase 2 is complete. Mark each critical-path inference with YES in CP?.

Then proceed.

---

## PHASE 2 — CLAIM MAP

| C-ID | Claim | Type | Depends on | Status | CP? |
|------|-------|------|------------|--------|-----|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify | — |
| C-02 | | inference | C-01 | to-verify | YES / — |

Types: premise / definition / empirical / inference / conclusion

Minimum: 6 claims. At least one per major section. Mark critical-path inferences with `YES` in CP?.

> Do not proceed to PHASE 3 until every claim has an ID, dependencies are mapped, and CP? flags are assigned.

---

## PHASE 3 — IDENTITY-COMMITTED SPECIALIST TRACE

Phase 3 runs as three specialist passes in strict sequence. Each specialist makes first-person commitments under their role identity. The next specialist is bound by those commitments — specialists do not revise prior commitments or re-execute prior passes.

### 3A — THE LOGICIAN (Form Identification)

The Logician's sole task: name the logical form of every inference step. No evaluation, no advocacy. The Logician classifies structure; the Logician makes no validity claims.

```
FORM [C-ID] [CP? YES/—]: [claim text]
Role: Logician
Logical form: [modus ponens / modus tollens / hypothetical syllogism / disjunctive syllogism /
               abduction / inductive generalization / argument from analogy /
               argument from authority / causal inference / other: describe]
Formal structure: [If/Then/Therefore skeleton in 1–3 lines]
```

> **I, the Logician, commit the above form identifications for all inference steps.** The Empirical Reviewer is bound to evaluate validity against these committed forms. The Reviewer does not reclassify logical structure. If the Reviewer's validity findings conflict with the structure I have committed, that conflict is an INVALID-FORM fault candidate — not a correction of my classification.

### 3B — THE EMPIRICAL REVIEWER (Validity Checks)

The Reviewer tests whether the premises hold for every inference step, using the forms the Logician committed. The Reviewer neither reclassifies forms nor issues verdicts — verdicts belong to the Chair. If DRIFT is found, name the term, the definition claim C-ID, and how the meaning shifted.

```
CHECK [C-ID]: [claim text]
Role: Empirical Reviewer
  (1) Logical: given the Logician's committed form, does the conclusion follow from the premises?
              [YES] / [WEAK — valid only under assumption: state it explicitly] /
              [NO — the committed form is not satisfied: describe how the structure fails]
  (2) Empirical: are the premises empirically supported?
              [YES] / [CITED: ref] / [ASSUMED: what is taken for granted] / [UNSUPPORTED: what evidence is needed]
  (3) Consistency: are key terms used consistently with their definition claims?
              [YES] / [DRIFT: term, definition claim C-ID, how it shifted]
```

> **I, the Empirical Reviewer, commit the above validity checks for all inference steps.** I have evaluated validity against the Logician's committed forms — I have not reclassified any form. Where my logical check returns NO or WEAK, the source is either a failed validity condition or a form that the argument's actual structure does not satisfy; the Chair will determine which. The Committee Chair now synthesizes both analyses.

### 3C — THE COMMITTEE CHAIR (Verdicts)

The Chair synthesizes the Logician's committed forms and the Reviewer's committed checks into verdicts. The Chair does not re-run validity checks or reclassify forms — both analyses are sealed. For every WEAK or BROKEN verdict, the Chair characterizes fault depth as a domain specialist would. CP-flagged steps receive explicit severity attention.

```
VERDICT [C-ID]: SOUND / WEAK / BROKEN
Role: Committee Chair
Reason: [one sentence — why SOUND holds, or what makes it WEAK/BROKEN, derived from the
         Logician's committed form and the Reviewer's committed checks]
If WEAK or BROKEN:
  Reviewer flag: As committee chair, would I flag this in a written review? YES/NO — one-sentence justification
  Depth tier: OBVIOUS / NOTABLE / SIGNIFICANT
    OBVIOUS — any careful reader notices without domain expertise
    NOTABLE — a methodologically careful reader notices
    SIGNIFICANT — only a domain specialist catches it on first read
  Domain comparison: [one sentence — what domain standard or prior result does this gap violate?]
```

> **I, the Committee Chair, commit the above verdicts.** These verdicts are derived from the Logician's committed form identifications and the Reviewer's committed validity checks. I have introduced no new form classifications and re-run no validity checks.

---

## PHASE 4 — FAULT REGISTER

Every WEAK or BROKEN verdict from the Committee Chair (3C) must appear here.

Fault classes (assign exactly one per row):
- **DEF-DRIFT**: a key term shifts meaning between its definition claim and its use
- **UNSUPPORTED-GEN**: a generalization extends beyond what the evidence licenses
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure does not satisfy the form the Logician committed — identified when the Reviewer's logical check returns NO and the Logician's committed form is the source of the failure

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity | CP? |
|------|------|---------|-------|-----|--------------|----------|-----|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [structural explanation] | [exact claim, evidence, or definition change] | P1/P2/P3 | YES/— |

Severity: P1 = breaks central conclusion / P2 = weakens key section / P3 = precision issue

Gap field: begin with the depth tier tag from 3C in brackets. For INVALID-FORM faults, reference the Logician's committed form explicitly: `[SIGNIFICANT] The Logician committed this step as an inductive generalization; the Reviewer found the conclusion extends to a population not covered by the stated premises — the committed form is violated, not merely underdetermined.`

**Phase 4 Closing — Committee Chair's Null Rejection Test + CP Intersection**:

The Chair delivers the final verdict in four steps:
1. Count rows per class code. Name the dominant fault class by code (most rows).
2. Count P1-severity faults. If P1 count ≥ 1: "H0 is rejected." If P1 count = 0, assess whether P2 faults collectively challenge the central argument.
3. State: "H0 is [rejected / not rejected]. Inertia — submitting without revision — is [not defensible / defensible with minor fixes / defensible]."
4. Synthesize whether the dominant fault class confirms or refutes the Phase 0 best-case statement. Name the dominant class using structural vocabulary. Then check CP intersection: "CP intersection: [YES — a P1 fault landed on a pre-committed load-bearing step; the conclusion is directly undermined / NO — the conclusion survives critical-path steps but is weakened by faults elsewhere]."

---

## PHASE 5 — AMEND

Three structural fixes ordered P1 → P2 → P3. Each references F-ID, C-ID, and Class code.

1. [P1 fix — F-ID, C-ID, Class: exact repair]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-04 — Combined: C-20 + C-19 (Phase 0 Generalization Registry + Identity-Anchored Roles)

**Hypothesis**: V-01 tests whether Phase 0 Gen-IDs alone produce commitment-relative Gap fields. V-03 tests whether identity-anchored closure alone changes boundary enforcement. Combining them tests whether the two axes interact. The specific interaction: when the Reviewer's identity constraint includes an explicit reference to Phase 0 Gen-IDs — "I, the Reviewer, am bound to test validity against the Logician's committed forms and against the Phase 0 generalizations" — does this make Gen-ID tracing structurally natural rather than dependent on a Gap-writing instruction? The prediction: yes. The Reviewer's identity commitment to Phase 0 creates an earlier checkpoint than the Gap field format instruction alone. When the Reviewer notes "Gen-02 match: this claim extends to a population not represented in the study," the Chair inherits that Gen-ID link and the Gap field writes itself. Tests whether the combination produces C-20 compliance more reliably than either axis alone.

**What changes from R4 V-04**: Phase 0 adds pre-committed generalizations table (V-01). Phase 3 closure language reformulated as first-person identity commitments (V-03). The Reviewer's identity commitment explicitly references Phase 0 Gen-IDs as a check target. Gap field format for UNSUPPORTED-GEN cites Gen-IDs. Phase 4 Closing adds generalization accountability step. Phase 0 CP commitment and Phase 2 CP? column retained from R4 V-04 baseline.

---

You are running /simulate-argument for: {{topic}}

Three specialists examine every argument. Before any specialist begins, you will pre-commit to the paper's key generalizations — the claims you predict will extend beyond direct evidence. Each gets a Gen-ID. Each specialist commits findings under their role identity and is bound by prior commitments. The Reviewer's identity includes accountability to Phase 0 Gen-IDs. UNSUPPORTED-GEN faults must trace back to a named Phase 0 generalization. The adversary is inertia: the belief that no structural revision is needed.

---

## PHASE 0 — ARGUMENT SETUP

State four things before any specialist begins:

**Best-case argument** (one paragraph):
> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

**Null hypothesis** (one sentence):
> "H0: This argument is structurally sound and requires no revision before submission."

**Critical path** (one to three sentences): Which 2–3 inference steps are most load-bearing? Write TBD if you cannot name them before reading; revise after Phase 1.

**Pre-committed generalizations**: Name the claims you expect to extend beyond direct evidence.

| Gen-ID | Generalization | Why expected |
|--------|----------------|--------------|
| Gen-01 | [claim text] | [why you expect this to lack direct evidence] |
| Gen-02 | | |

Minimum: 2 generalizations. UNSUPPORTED-GEN Gap fields must cite a Gen-ID. An assertion-only Gap does not pass.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

After reading, revise Phase 0 if necessary. Update the Gen registry to reflect actual generalizations made. Update the critical path to name specific C-IDs. Mark each critical-path inference with YES in CP?.

Then proceed.

---

## PHASE 2 — CLAIM MAP

| C-ID | Claim | Type | Depends on | Status | CP? |
|------|-------|------|------------|--------|-----|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify | — |
| C-02 | | inference | C-01 | to-verify | YES / — |

Types: premise / definition / empirical / inference / conclusion

Minimum: 6 claims. At least one per major section. Mark CP inferences with `YES`. Where a claim maps to a Phase 0 Gen-ID, note it in the Claim column.

> Do not proceed to PHASE 3 until every claim has an ID, dependencies are mapped, and CP? flags are assigned.

---

## PHASE 3 — IDENTITY-COMMITTED SPECIALIST TRACE

Three specialist passes in strict sequence. Each commits findings under role identity. Subsequent specialists are bound by prior commitments.

### 3A — THE LOGICIAN (Form Identification)

```
FORM [C-ID] [CP? YES/—]: [claim text]
Role: Logician
Logical form: [modus ponens / modus tollens / hypothetical syllogism / disjunctive syllogism /
               abduction / inductive generalization / argument from analogy /
               argument from authority / causal inference / other: describe]
Formal structure: [If/Then/Therefore skeleton in 1–3 lines]
```

> **I, the Logician, commit the above form identifications.** The Empirical Reviewer is bound to evaluate validity against these forms and is not permitted to reclassify them. Any conflict between the Reviewer's validity findings and my committed forms is an INVALID-FORM candidate.

### 3B — THE EMPIRICAL REVIEWER (Validity Checks)

The Reviewer is bound to the Logician's committed forms and is accountable to the Phase 0 Gen-registry. For inductive generalization forms, the Reviewer explicitly checks whether the claim exceeds what the Phase 0 Gen-ID anticipated.

```
CHECK [C-ID]: [claim text]
Role: Empirical Reviewer
  Gen-ID match: [Gen-NN — if this corresponds to a Phase 0 pre-committed generalization / —]
  (1) Logical: given the Logician's committed form, does the conclusion follow?
              [YES] / [WEAK — valid only under assumption: state it explicitly] /
              [NO — the committed form is not satisfied: describe the failure]
  (2) Empirical: are the premises empirically supported?
              [YES] / [CITED: ref] / [ASSUMED: what is assumed] / [UNSUPPORTED: what evidence is needed]
  (3) Consistency: are key terms used consistently with their definition claims?
              [YES] / [DRIFT: term, definition claim C-ID, how it shifted]
```

> **I, the Empirical Reviewer, commit the above validity checks.** I have evaluated against the Logician's committed forms and the Phase 0 Gen-registry. I have not reclassified any form. The Committee Chair now synthesizes both analyses.

### 3C — THE COMMITTEE CHAIR (Verdicts)

The Chair is bound to both prior analyses. No new form classifications or validity re-runs. CP-flagged steps receive explicit severity attention.

```
VERDICT [C-ID]: SOUND / WEAK / BROKEN
Role: Committee Chair
Reason: [one sentence — why SOUND holds, or what makes it WEAK/BROKEN]
If WEAK or BROKEN:
  Reviewer flag: As committee chair, would I flag this in a written review? YES/NO — one-sentence justification
  Depth tier: OBVIOUS / NOTABLE / SIGNIFICANT
    OBVIOUS — any careful reader notices without domain expertise
    NOTABLE — a methodologically careful reader notices
    SIGNIFICANT — only a domain specialist catches it on first read
  Domain comparison: [one sentence — what domain standard or prior result does this gap violate?]
```

> **I, the Committee Chair, commit the above verdicts.**

---

## PHASE 4 — FAULT REGISTER

Every WEAK or BROKEN verdict from the Chair (3C) must appear here.

Fault classes (assign exactly one per row):
- **DEF-DRIFT**: term shifts meaning between definition claim and use
- **UNSUPPORTED-GEN**: generalization beyond what evidence licenses — Gap must cite a Phase 0 Gen-ID
- **CIRCULAR-DEP**: conclusion appears as implicit premise in its own support chain
- **INVALID-FORM**: structure violates the Logician's committed form

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity | CP? |
|------|------|---------|-------|-----|--------------|----------|-----|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [structural explanation] | [exact change needed] | P1/P2/P3 | YES/— |

**Gap field format for UNSUPPORTED-GEN** — cite the Phase 0 Gen-ID:
> `[NOTABLE] Needed [Gen-01: the claim that the approach scales to real-time constraints], found only offline benchmark results — a systems reviewer would require latency measurements under production conditions before accepting the generalization.`

An assertion-only Gap does not pass for UNSUPPORTED-GEN.

**Phase 4 Closing — Null Rejection Test + Generalization Accountability + CP Intersection**:

1. Count rows per class code. Name the dominant fault class by code.
2. Count P1-severity faults. If P1 count ≥ 1: "H0 is rejected." If P1 count = 0, assess whether P2 faults collectively challenge the central argument.
3. State: "H0 is [rejected / not rejected]. Inertia is [not defensible / defensible with minor fixes / defensible]."
4. Synthesize dominant fault class against Phase 0 best-case statement using structural vocabulary.
5. Generalization accountability: for each Gen-ID, state outcome: "Gen-01: [F-ID UNSUPPORTED-GEN registered, P_-severity / No fault — evidence was sufficient]."
6. CP intersection: "CP intersection: [YES — P1 fault on CP-flagged step / NO — conclusion survives critical-path steps]."

---

## PHASE 5 — AMEND

Three structural fixes ordered P1 → P2 → P3.

1. [P1 fix — F-ID, C-ID, Class: exact repair]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating C-ID and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-05 — Combined: All Three (C-18 + C-19 + C-20) + Four Specialists

**Hypothesis**: V-01 achieves C-20 by adding a Phase 0 Gen-registry. V-02 achieves C-18 by replacing the binary CP verdict with a structured per-step audit loop. V-03 achieves C-19 by adding identity-anchored first-person closure language. Combining all three adds a fourth specialist — the Advocate — whose Phase 0 Gen-registry accountability makes the combination more structurally integrated than a sum of three additive changes. The Advocate's best readings can explicitly reference Phase 0 Gen-IDs: "This inference is valid if Gen-02 holds — the claim that [X]." This connects the per-step Phase 3 commitment directly to the Phase 0 pre-commitment, so the Chair's Gap field writes "Needed [Gen-02: the Phase 0 pre-committed generalization], found only Y" as a structurally derived account, not an instruction-following behavior. The CP priority audit loop in Phase 4 inherits four committed analyses, giving the accountability verdict more structural signal. The prediction: the three axes reinforce. Identity accountability makes Gen-ID tracing natural (C-20). Gen-IDs in Phase 0 give the CP audit loop a richer structural context — are the CP-flagged steps the same steps that carry the highest-risk generalizations (C-18)? Named four-specialist roles with first-person closure produce the strongest C-17/C-19 enforcement of any variation in any round.

**What changes from R4 V-05**: Phase 0 adds the pre-committed generalizations table (Gen-IDs). Phase 3 closure language reformulated as first-person identity commitments (all four specialists). The Advocate is instructed to reference Phase 0 Gen-IDs when committing best readings. Phase 4 Closing replaces the binary CP intersection with a structured per-step audit loop. Generalization accountability step added to Phase 4 Closing.

---

You are running /simulate-argument for: {{topic}}

Four specialists examine every argument. Before any specialist begins, you will commit to: (1) the argument's best case, (2) the null hypothesis, (3) which inference steps are most load-bearing, and (4) which generalizations the paper is expected to make beyond its direct evidence. The Logician names structure. The Advocate commits the author's best reading — referencing Phase 0 generalizations where relevant. The Reviewer challenges the Advocate's committed readings. The Chair synthesizes verdicts. Phase 4 runs a structured audit: did the priority predictions hold, and were the pre-committed generalizations the ones that failed? The adversary is inertia: the belief that no structural revision is needed.

---

## PHASE 0 — ARGUMENT SETUP

State four things before any specialist begins:

**Best-case argument** (one paragraph):
> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

**Null hypothesis** (one sentence):
> "H0: This argument is structurally sound and requires no revision before submission."

**Critical path** (one to three sentences): Which 2–3 inference steps are most load-bearing? Write TBD; revise after Phase 1.
> "The conclusion depends most heavily on [inference type or topic area]. If that step fails, [consequence for the conclusion]."

**Pre-committed generalizations**: Name the claims you expect to extend beyond direct evidence. Write TBD; revise after Phase 1.

| Gen-ID | Generalization | Why expected |
|--------|----------------|--------------|
| Gen-01 | [claim text] | [why you expect this to lack direct evidence] |
| Gen-02 | | |

Minimum: 2 generalizations. UNSUPPORTED-GEN Gap fields must cite a Gen-ID. An assertion-only Gap does not pass.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

After reading, revise Phase 0 if necessary. Update the critical path to name specific C-IDs once Phase 2 is complete. Update the Gen registry to reflect actual generalizations made. Mark each critical-path inference with YES in CP?.

Then proceed.

---

## PHASE 2 — CLAIM MAP

The shared record all four specialists work from.

| C-ID | Claim | Type | Depends on | Status | CP? |
|------|-------|------|------------|--------|-----|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify | — |
| C-02 | | inference | C-01 | to-verify | YES / — |

Types: premise / definition / empirical / inference / conclusion

Minimum: 6 claims. At least one per major section. Mark critical-path inferences with `YES`. Where a claim maps to a Phase 0 Gen-ID, note it in the Claim column.

> Do not proceed to PHASE 3 until every claim has an ID, dependencies are mapped, and CP? flags are assigned.

---

## PHASE 3 — FOUR-SPECIALIST TRACE

Phase 3 runs as four specialist passes in strict sequence. Each specialist makes first-person commitments under their role identity. Subsequent specialists are bound by prior commitments and cannot revise them.

### 3A — THE LOGICIAN (Form Identification)

The Logician names the logical form of every inference step. No evaluation, no advocacy. CP-flagged steps are noted.

```
FORM [C-ID] [CP? YES/—]: [claim text]
Role: Logician
Logical form: [modus ponens / modus tollens / hypothetical syllogism / disjunctive syllogism /
               abduction / inductive generalization / argument from analogy /
               argument from authority / causal inference / other: describe]
Formal structure: [If/Then/Therefore skeleton in 1–3 lines]
```

> **I, the Logician, commit the above form identifications for all inference steps.** The Advocate, the Empirical Reviewer, and the Committee Chair are bound to these forms. No subsequent specialist may reclassify logical structure. Any conflict between a later specialist's findings and my committed forms is an INVALID-FORM fault candidate.

### 3B-ADVOCATE — THE ADVOCATE (Author's Best Reading)

The Advocate states the minimum assumption that would make each inference valid, given the Logician's committed form. Where the inference is an inductive generalization, the Advocate names which Phase 0 Gen-ID the claim corresponds to (if any). The Advocate does not evaluate whether the assumption holds.

```
ADVOCATE [C-ID]: [claim text]
Role: Advocate
  Gen-ID reference: [Gen-NN — if this inference corresponds to a Phase 0 pre-committed generalization / —]
  Best reading: [The inference is valid if we assume: ...]
  Key assumption: [one sentence — the precise unstated premise that would close the logical gap.
                   If no assumption needed: "The stated premises are sufficient given the Logician's form."]
```

> **I, the Advocate, commit the above best readings for all inference steps.** I have referenced Phase 0 Gen-IDs where the Logician's committed form is an inductive generalization that corresponds to a pre-committed generalization. I have not evaluated whether any assumption holds — that is the Empirical Reviewer's task.

### 3B-CRITIC — THE EMPIRICAL REVIEWER (Evidence Challenge)

The Reviewer tests whether the evidence supports the Advocate's committed key assumptions. The Reviewer also checks term consistency. The Reviewer is bound to the Logician's forms and the Advocate's committed best readings — no new form classifications, no new best readings.

```
CRITIC [C-ID]: [claim text]
Role: Empirical Reviewer
  (1) Does the evidence support the Advocate's committed key assumption?
              [YES] / [CITED: ref that directly supports the assumption] /
              [ASSUMED: the key assumption is itself taken for granted, not demonstrated] /
              [UNSUPPORTED: what evidence or argument would be needed to establish it]
  (2) Consistency: are key terms used consistently with their definition claims?
              [YES] / [DRIFT: term, definition claim C-ID, how it shifted]
```

> **I, the Empirical Reviewer, commit the above evidence challenges for all inference steps.** I have tested the Advocate's committed assumptions — not re-evaluated the Logician's forms or generated new best readings. Where the Advocate referenced a Phase 0 Gen-ID, my assessment is the direct test of that pre-committed generalization. The Committee Chair now synthesizes all four analyses.

### 3C — THE COMMITTEE CHAIR (Verdicts)

The Chair synthesizes all four committed analyses into verdicts. No new form classifications, no new best readings, no new validity checks. CP-flagged steps receive explicit severity attention. For every WEAK or BROKEN verdict, the Chair characterizes fault depth as a domain specialist would.

```
VERDICT [C-ID]: SOUND / WEAK / BROKEN
Role: Committee Chair
Reason: [one sentence — why SOUND holds; or the structural gap between what the Advocate
         required and what the Reviewer found, with reference to the Logician's committed form]
If WEAK or BROKEN:
  Reviewer flag: As committee chair, would I flag this in a written review? YES/NO — one-sentence justification
  Depth tier: OBVIOUS / NOTABLE / SIGNIFICANT
    OBVIOUS — any careful reader notices without domain expertise
    NOTABLE — a methodologically careful reader notices
    SIGNIFICANT — only a domain specialist catches it on first read
  Domain comparison: [one sentence — what domain standard or prior result does the gap between
                      Advocate's assumption and Reviewer's evidence violate?]
```

> **I, the Committee Chair, commit the above verdicts.** These are derived from the four sealed analyses: the Logician's forms, the Advocate's best readings, the Reviewer's evidence challenges, and my synthesis. I have introduced no new analyses.

---

## PHASE 4 — FAULT REGISTER

Every WEAK or BROKEN verdict from the Committee Chair (3C) must appear here.

Fault classes (assign exactly one per row):
- **DEF-DRIFT**: a key term shifts meaning between its definition claim and its use
- **UNSUPPORTED-GEN**: a generalization extends beyond what the evidence licenses — Gap must cite a Phase 0 Gen-ID
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure violates the form the Logician committed — the Reviewer's evidence challenge reveals the structure, not just the evidence, is the problem

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity | CP? |
|------|------|---------|-------|-----|--------------|----------|-----|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [Advocate required X; Reviewer found only Y — with Gen-ID for UNSUPPORTED-GEN] | [exact claim, evidence, or definition change that closes the fault] | P1/P2/P3 | YES/— |

Severity: P1 = breaks central conclusion / P2 = weakens key section / P3 = precision issue

**Gap field format for UNSUPPORTED-GEN** — cite the Phase 0 Gen-ID:
> `[SIGNIFICANT] The Advocate required that Gen-02 holds: the claim that the learning algorithm generalizes to low-resource languages. The Reviewer found only results on five high-resource languages with ≥10M training tokens. A specialist in low-resource NLP would require explicit low-resource benchmarks before accepting the generalization.`

An assertion-only Gap does not pass for UNSUPPORTED-GEN.

**Phase 4 Closing — Null Rejection Test + CP Priority Audit + Generalization Accountability**:

The Chair delivers the final verdict in five steps:

1. Count rows per class code. Name the dominant fault class by code (most rows).
2. Count P1-severity faults. If P1 count ≥ 1: "H0 is rejected." If P1 count = 0, assess whether P2 faults collectively challenge the central argument.
3. State: "H0 is [rejected / not rejected]. Inertia — submitting without revision — is [not defensible / defensible with minor fixes / defensible]."
4. Critical path priority audit — for each CP-flagged step committed in Phase 0, write one accountability line:
   > "CP audit [C-ID]: Phase 0 predicted this step as load-bearing. Trace outcome: [F-ID at P_-severity, Class: CODE / SOUND — no fault]. Accountability: [CONFIRMED — the pre-committed load-bearing step carries the most severe fault / DISCONFIRMED — step survived; fault [F-ID] on non-CP step [C-ID] was more severe / CONFIRMED-ELSEWHERE — step survived; CP-adjacent step carried P1 fault]."

   Then state: "Structural risk distribution: [one sentence on where actual risk lies vs. where Phase 0 predicted it]."

5. Generalization accountability: for each Gen-ID from Phase 0, state the trace outcome:
   > "Gen-01: [F-ID — UNSUPPORTED-GEN fault registered at P_-severity / No fault — the Advocate's best reading was supported by evidence]."

   Then synthesize: "Generalization accountability verdict: [one sentence — were the pre-committed generalizations the primary structural risk, or did other fault classes dominate?]"

---

## PHASE 5 — AMEND

Three structural fixes ordered P1 → P2 → P3. Each references F-ID, C-ID, and Class code.

1. [P1 fix — F-ID, C-ID, Class: exact repair — what claim, evidence, or definition change closes this fault]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

### Predicted v5 scores by variation

| Variation | C-18 | C-19 | C-20 | Predicted aspirational_pass | Composite |
|-----------|------|------|------|-----------------------------|-----------|
| V-01 (C-20 axis) | FAIL | PASS | **PASS** | 10/12 | ~98 |
| V-02 (C-18 axis) | **PASS** | PASS | FAIL | 10/12 | ~98 |
| V-03 (C-19 axis) | FAIL | **PASS** | FAIL | 10/12 | ~98 |
| V-04 (C-20 + C-19) | FAIL | **PASS** | **PASS** | 11/12 | ~99 |
| V-05 (all three) | **PASS** | **PASS** | **PASS** | **12/12** | **100** |

All five predicted at golden (all essential PASS, composite ≥ 80). V-05 predicted to be the first variation to achieve 12/12 aspirational across any round.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["phase-0-gen-registry", "cp-priority-audit-loop", "identity-bound-role-handoff"]}
```
