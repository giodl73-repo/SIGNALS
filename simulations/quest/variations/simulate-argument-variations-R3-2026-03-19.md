Written to `simulations/quest/variations/simulate-argument-variations-R3-2026-03-19.md`.

---

## simulate-argument — Variation Set R3

### Variation Matrix

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **Axis** | Output format (table-dominant) | Phrasing register (adversarial skeptic) | Inertia framing (null-hypothesis) | Table + lifecycle expansion | All three axes |
| **Type** | Single | Single | Single | Combined | Combined |

---

**R3 context**: No R2 variation scores 100 under v3. V-03/V-05 score ~98 (have C-14, miss C-15). V-04 scores ~97 (has C-13 but misses both C-14 and C-15). The gap is that C-15 (depth tier + domain comparison per WEAK/BROKEN step + tier tag in Fault Register) was only present in R2 V-02 — which failed C-13.

All five R3 variations carry **both C-14 and C-15 as table stakes**. The variation axes are the unexplored quest meta-axes (output format, phrasing register, inertia framing) rather than rubric-specific mechanisms.

---

### Single-axis variations

**V-01 — Output format**: Phase 3 becomes a wide **Inference Trace Table** — every inference step is one row, every required field (logical form, 3 validity checks, verdict, reviewer flag, depth tier, domain comparison) is a named column. Empty cells are structurally visible. Tests whether column enforcement closes the same compliance gaps that 3A/3B/3C sub-pass gating was designed to close.

**V-02 — Phrasing register**: R2 V-05 mechanisms (3A/3B/3C, Class column, Phase 0) with tone shifted to **adversarial skeptic reviewer**. The model is cast as the most skeptical reviewer on the program committee with a prior that the argument has a structural problem. Reviewer hooks become natural to the role; depth tiers become natural outputs. Tests whether framing-level changes sharpen C-10/C-12 without changing structure.

**V-03 — Inertia framing**: Phase 0 doubled as a **null hypothesis** ("H0: this argument requires no revision before submission"). Phase 4 closing becomes a formal three-step null-rejection test: count P1 faults, state whether null is rejected, name the dominant fault class by code. Names inertia explicitly as the adversary. Tests whether the null-hypothesis frame produces tighter C-13 synthesis than "confirm or refute."

### Combined variations

**V-04 — Table + lifecycle expansion**: V-01's wide table for Phase 3, plus a **structured three-part Phase 4 synthesis subsection** (dominant class by code count / dominant depth tier / Phase 0 verdict) replacing the single closing sentence. Phase 3 compresses; Phase 4 expands.

**V-05 — All three**: Table format + adversarial voice + inertia framing together. The adversarial role makes the null-hypothesis framing natural (a skeptical reviewer is exactly the adversary of "submit as-is"), and the table makes both operational. Maximum divergence from all prior rounds.

---

**Predicted v3 scores**: All five variations predicted at **100** (7/7 aspirationals). The critical addition in every variation is C-15 (depth tier + domain comparison columns/fields), which was the sole gap between R2 V-03/V-05 and a perfect score under v3.
r on the program committee with a prior that the argument has a structural problem. Reviewer hooks become natural outputs rather than mandated fields. Tests whether framing-level changes affect fault depth without changing structural mechanisms.

**V-03 — Inertia framing**: Phase 0 is doubled as a null hypothesis: "the argument is sound and requires no revision." Phase 4 closing is a formal null-rejection test: count P1+P2 faults; if P1 count > 0, null is rejected; name the dominant fault class by code. The inertia competitor (author's satisfaction with the current draft) is named explicitly. Tests whether the null-hypothesis frame produces sharper C-13 synthesis than the "confirm or refute" phrase.

---

### Combined variations

**V-04 — Table Phase 3 + Lifecycle emphasis**: V-01's wide Inference Trace Table stacked with a structured three-part Phase 4 synthesis section (sub-sections: dominant class by code count, dominant depth tier, null-rejection verdict). Phase 4 grows; Phase 3 compresses. Tests whether expanding synthesis space while compressing trace format changes coverage patterns.

**V-05 — All three axes**: V-01 table + V-02 adversarial voice + V-03 inertia framing. The most divergent variation from all prior rounds. Table forces format compliance; adversarial voice raises fault bar; inertia frame stakes the Phase 4 synthesis to a decision. Tests whether the three axes reinforce or interfere with each other.

---

### Predicted rubric coverage delta vs R2 V-05 under v3

| Criterion | R2 V-05 (v3 baseline) | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|---|
| C-09 term drift pinpointed | PASS | = | = | = | = | = |
| C-10 structural weakness | PASS | **stronger** (column forces classification) | **strongest** (adversarial prior) | = | **stronger** | **strongest** |
| C-11 falsification target | PASS | = | = | **stronger** (null-hypothesis + binary verdict) | = | **strongest** |
| C-12 inline reviewer hook | PASS | = (column) | **stronger** (natural to adversarial role) | = | = | **stronger** |
| C-13 fault pattern closure | PASS | = | = | **stronger** (reject/fail-to-reject + class code) | **stronger** (3-part synthesis) | **strongest** |
| C-14 fault class taxonomy | PASS | = | = | = | = | = |
| C-15 reviewer depth tier | FAIL | **PASS** (Depth column) | **PASS** (depth scale in 3C) | **PASS** (depth in STEP blocks) | **PASS** (Depth column) | **PASS** |

All five R3 variations are predicted to score 100 under v3 (7 aspirationals all pass).

---

## V-01 — Axis: Output Format (Table-Dominant Phase 3)

**Hypothesis**: Every R1 and R2 variation used code blocks or sub-pass blocks for Phase 3 inference traces. These free-form structures allow field omission — a model can skip the depth tier line and nothing structural forces the gap visible. Replacing Phase 3 with a wide Inference Trace Table makes every required field a named column. An empty cell in a markdown table is a structural gap, not an invisible omission. This tests whether tabular column enforcement closes the same compliance gaps that 3A/3B/3C sub-pass gating was designed to close — potentially more simply.

**What changed from R2 V-05**: Phase 3 restructured from 3A/3B/3C sub-passes to a single Inference Trace Table. All fields required by C-04, C-06, C-12, and C-15 become named columns. Class column and Phase 4 closing unchanged (C-14 retained). Depth tier and domain comparison added as required table columns (C-15 now covered). Fault Register Gap field must carry tier tag.

---

You are running /simulate-argument for: {{topic}}

Every paper makes an implicit bet: "The reader will accept my chain of reasoning." Your job is to find exactly where that bet fails. The adversary is not missing citations — it is the inference that looks valid on first read but collapses under scrutiny.

---

## PHASE 0 — AUTHOR'S BEST CASE

Before tracing, state the argument in its strongest form — what the author would say if given 60 seconds at a conference podium. One short paragraph. This is the target you are about to test.

> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

This is also the falsification target. Every fault you find should either support or undermine this statement.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

After reading, revise your PHASE 0 statement if necessary. Then proceed.

---

## PHASE 2 — CLAIM MAP

Extract the full argument as a directed graph. Every claim gets an ID.

| C-ID | Claim | Type | Depends on | Status |
|------|-------|------|------------|--------|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify |
| C-02 | | inference | C-01 | to-verify |

Types:
- **premise**: accepted without proof in this paper (cited or stated as assumption)
- **definition**: introduces a term that subsequent claims depend on
- **empirical**: requires data or citation to support
- **inference**: follows logically from prior claims (verify the logic)
- **conclusion**: the paper's output claims

Minimum: 6 claims. At least one claim per major section of the paper.

> Do not proceed to PHASE 3 until every claim has an ID and its dependencies are mapped.

---

## PHASE 3 — INFERENCE TRACE TABLE

For every claim with type=inference, complete one row in the Inference Trace Table.

Column definitions:
- **C-ID**: claim identifier from Phase 2
- **Logical Form**: named structure — modus ponens / modus tollens / hypothetical syllogism / disjunctive syllogism / abduction / inductive generalization / argument from analogy / argument from authority / causal inference / other: describe
- **Formal Structure**: the If/Then/Therefore skeleton in one line (e.g., "If A and B, then C")
- **Logical**: does the conclusion follow from the premises? `YES` / `WEAK: [assumption required]` / `NO: [gap]`
- **Empirical**: are the premises empirically supported? `YES` / `CITED: [ref]` / `ASSUMED: [what]` / `UNSUPPORTED: [what needed]`
- **Consistency**: are key terms used consistently? `YES` / `DRIFT: [term, def claim C-ID, how it shifted]`
- **Verdict**: `SOUND` / `WEAK` / `BROKEN`
- **Reviewer Flag?**: `YES — [one-sentence justification]` / `NO — [one-sentence justification]` (required for every WEAK/BROKEN row; N/A for SOUND)
- **Depth**: `OBVIOUS` / `NOTABLE` / `SIGNIFICANT` / `N/A` (required for WEAK/BROKEN only)
  - OBVIOUS: any careful reader catches it
  - NOTABLE: a careful methodological reader catches it
  - SIGNIFICANT: only a domain specialist catches it
- **Domain Comparison**: one sentence explaining why a domain specialist would rate the gap at the stated tier (required for WEAK/BROKEN only; N/A for SOUND)

| C-ID | Logical Form | Formal Structure | Logical | Empirical | Consistency | Verdict | Reviewer Flag? | Depth | Domain Comparison |
|------|-------------|-----------------|---------|-----------|-------------|---------|---------------|-------|------------------|
| | | | | | | | | | |

> Complete all rows before proceeding to PHASE 4. Every BROKEN or WEAK verdict requires non-empty Reviewer Flag?, Depth, and Domain Comparison columns.

---

## PHASE 4 — FAULT REGISTER

Every row with Verdict = WEAK or BROKEN from Phase 3 must appear here.

Fault classes (assign exactly one per fault):
- **DEF-DRIFT**: a key term shifts meaning between its definition claim and its use in this inference
- **UNSUPPORTED-GEN**: a generalization extends further than the supporting evidence licenses
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure does not match the stated form

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity |
|------|------|---------|-------|-----|--------------|----------|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [structural explanation of why the inference fails — not just that it does] | [exact claim, evidence, or definition change that closes the gap] | P1/P2/P3 |

Severity:
- P1: breaks the paper's central conclusion — must fix before submission
- P2: weakens a key section — weakens but does not invalidate
- P3: precision issue — affects rigor but not validity

Gap field format: begin with the depth tier tag from Phase 3 in brackets, then the structural explanation. Example: `[SIGNIFICANT] The causal claim requires a counterfactual condition that the study design cannot provide; any reviewer in causal inference methodology would flag the absence of a control arm.`

**Phase 4 Closing**: Count rows in the Class column. State the dominant fault class by code (most rows). Assess whether the fault pattern confirms or refutes the Phase 0 best-case statement. One to two sentences.

---

## PHASE 5 — AMEND

Three structural fixes ordered by severity. Each fix references the F-ID, C-ID, and Class code it addresses, and specifies the exact repair — not "add evidence" but what claim, what evidence, or what definition stabilization closes the gap.

1. [P1 fix — F-ID, C-ID, Class: exact repair]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, specify the exact precision gap to close]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-02 — Axis: Phrasing Register (Adversarial Skeptic Voice)

**Hypothesis**: Instructions framed as "trace the argument and find faults" allow a default toward the safe middle — the model may characterize most inferences as WEAK rather than BROKEN, hedge fault severity, and produce a Phase 4 that documents minor issues rather than structural failures. Casting the model as the most skeptical reviewer on the program committee, with an explicit prior that the argument has a structural problem, inverts this default: the model must retract the fault hypothesis, not hedge it. This framing makes reviewer hooks natural (the model is already playing a reviewer), fault depth authentic (the model must characterize severity as a skeptic would), and Phase 4 synthesis sharper (the model must declare whether inertia — accepting the paper as-is — is defensible). All structural mechanisms from R2 V-05 are retained; only framing and instructional voice change.

**What changed from R2 V-05**: Opening role framing shifted to adversarial skeptic reviewer. Imperative instructions reframed as reviewer directives. Depth tier and domain comparison added to 3C verdict blocks (C-15). Phase 4 Fault Register Class column retained (C-14). Reviewer hook in 3C retained (C-12). Phase 4 closing: dominant class by code count + one-sentence verdict on whether inertia is defensible.

---

You are running /simulate-argument for: {{topic}}

You are the most skeptical reviewer on the program committee for this paper. Your prior is that this argument has a structural problem severe enough to warrant rejection or major revision. Your job is not to find minor issues — it is to either locate the structural fault that justifies your prior or, after a rigorous trace, retract it. Hedging is not available. By the end of this analysis, you will either name the dominant fault class or state that you were wrong.

The adversary is not missing citations. It is the inference that looks valid on first read but doesn't survive scrutiny from someone who knows the field.

---

## PHASE 0 — THE ARGUMENT YOU ARE CHALLENGING

Before tracing, state the argument in its strongest form — the version the authors would present if they had 60 seconds and needed to convince a skeptic like you. One short paragraph.

> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

This is what you are about to challenge. Note: a rigorous trace that finds only minor issues is a valid result. Document what you find.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

After reading, update your Phase 0 statement if necessary. Then proceed.

---

## PHASE 2 — CLAIM MAP

As a skeptical reviewer, your first task is to reconstruct the argument you plan to challenge — every claim with an ID, every dependency made explicit. Arguments often hide their weakest moves in implicit dependencies.

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

Minimum: 6 claims. At least one claim per major section. Pay close attention to definition claims — these are where definitional drift typically originates.

> Do not proceed until every claim has an ID and its dependencies are mapped.

---

## PHASE 3 — STEP-BY-STEP TRACE

Phase 3 runs in three sub-passes. Complete each sub-pass across ALL inference steps before advancing.

### 3A — FORM IDENTIFICATION PASS

Name the logical form of every inference step before evaluating any of them. Committing to a named form before checking validity prevents post-hoc rationalization of the structure.

```
FORM [C-ID]: [claim text]
Logical form: [modus ponens / modus tollens / hypothetical syllogism / disjunctive syllogism /
               abduction / inductive generalization / argument from analogy /
               argument from authority / causal inference / other: describe]
Formal structure: [If/Then/Therefore skeleton in 1–3 lines]
```

### 3B — VALIDITY CHECK PASS

Run three independent checks across ALL inference steps before issuing any verdicts. If you find DRIFT, you must name the term, the definition claim C-ID where it was introduced, and precisely how it has shifted.

```
CHECK [C-ID]: [claim text]
  (1) Logical: does the conclusion follow from the premises given the form in 3A?
              [YES] / [WEAK — valid only under assumption: state it explicitly] / [NO — describe the gap]
  (2) Empirical: are the premises feeding this step empirically supported?
              [YES] / [CITED: ref] / [ASSUMED: what is taken for granted] / [UNSUPPORTED: what evidence is needed]
  (3) Consistency: are key terms used with the same meaning as their definition claims?
              [YES] / [DRIFT: term, definition claim C-ID, how it shifted]
```

### 3C — VERDICT PASS

Issue verdicts across all inference steps based on 3A and 3B findings. For every WEAK or BROKEN verdict, you must characterize the fault depth as a skeptical domain reviewer would.

```
VERDICT [C-ID]: SOUND / WEAK / BROKEN
Reason: [one sentence — why SOUND holds, or exactly what makes it WEAK/BROKEN]
If WEAK or BROKEN:
  Reviewer flag: Would a domain reviewer flag this as non-obvious? YES/NO — one-sentence justification
  Depth tier: OBVIOUS / NOTABLE / SIGNIFICANT
    OBVIOUS — any careful reader notices the gap without domain expertise
    NOTABLE — a methodologically careful reader notices it
    SIGNIFICANT — only a specialist in this domain would catch it on first read
  Domain comparison: [one sentence — what standard, expectation, or prior result in the field does this gap violate?]
```

---

## PHASE 4 — FAULT REGISTER

Every WEAK or BROKEN verdict from 3C appears here. Assign exactly one fault class per row.

Fault classes:
- **DEF-DRIFT**: a key term shifts meaning between its definition claim and its use in this inference
- **UNSUPPORTED-GEN**: a generalization extends further than the supporting evidence licenses
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure does not match the stated form in 3A

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity |
|------|------|---------|-------|-----|--------------|----------|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [structural explanation of why the inference fails] | [exact claim, evidence, or definition change that closes it] | P1/P2/P3 |

Severity:
- P1: breaks the paper's central conclusion
- P2: weakens a key section without invalidating the paper
- P3: precision issue affecting rigor, not validity

Gap field: begin with the depth tier tag in brackets, then the structural explanation. Example: `[NOTABLE] The inductive generalization from N=42 participants to clinical practice exceeds what the sample size licenses; a statistician reviewer would ask for a power analysis justifying the generalization claim.`

**Phase 4 Closing**: Count rows per class code. Name the dominant class (most rows). Does the fault pattern confirm or refute your Phase 0 best-case statement? As the skeptical reviewer: was your prior justified — is inertia (no revision) defensible? One to two sentences.

---

## PHASE 5 — AMEND

Three structural fixes ordered P1 → P2 → P3. Each references the F-ID, C-ID, and Class code it addresses, and specifies the exact repair.

1. [P1 fix — F-ID, C-ID, Class: exact repair — what claim, evidence, or definition change closes this fault]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-03 — Axis: Inertia Framing (Null-Hypothesis Frame)

**Hypothesis**: The implicit inertia competitor in argument simulation is the author's satisfaction with the current draft — the belief that no revision is needed and peer review will accept the argument as-is. Framing Phase 0 as a null hypothesis ("this argument is sound; no revision is required") and Phase 4 closing as a formal null-rejection test creates a decision framework. A model following this frame must produce a binary verdict: is inertia defensible or not? This is stricter than "confirm or refute the Phase 0 best-case framing" — confirmation and refutation both pass C-13 in that frame, but null-rejection requires citing fault severity. The null-hypothesis structure also tightens C-11/C-13 interaction: Phase 0 is both the falsification target and the decision criterion for Phase 4.

**What changed from R2 V-05**: Phase 0 is reformulated as a null hypothesis. Phase 4 closing is a formal three-step rejection test: (1) count P1 faults, (2) if P1 > 0 null is rejected, (3) name the dominant fault class by code. Depth tier added to 3C verdict blocks (C-15). Class column in Fault Register retained (C-14). Tier tag required in Fault Register Gap (C-15). Phase 4 now explicitly names the inertia competitor and states whether it is defeated.

---

You are running /simulate-argument for: {{topic}}

Every paper makes an implicit claim: "This argument is good enough to submit as-is." Teams skip argument simulation because they trust that claim. Your job is to test it. The primary adversary is not missing citations — it is inertia: the belief that no structural revision is needed.

---

## PHASE 0 — THE NULL HYPOTHESIS

State two things before you begin:

**Best-case argument** (one paragraph): What would this argument look like if fully sound?
> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

**Null hypothesis** (one sentence): State the null explicitly.
> "H0: This argument is structurally sound and requires no revision before submission."

This null hypothesis is what your trace will attempt to reject. You will return to it in Phase 4.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

After reading, update your Phase 0 statement if necessary. Revise the null hypothesis only if the scope of the paper is materially different from your initial read. Then proceed.

---

## PHASE 2 — CLAIM MAP

Extract the full argument as a directed graph. Every claim gets an ID.

| C-ID | Claim | Type | Depends on | Status |
|------|-------|------|------------|--------|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify |
| C-02 | | inference | C-01 | to-verify |

Types:
- **premise**: accepted without proof in this paper (cited or stated as assumption)
- **definition**: introduces a term that subsequent claims depend on
- **empirical**: requires data or citation to support
- **inference**: follows logically from prior claims (verify the logic)
- **conclusion**: the paper's output claims

Minimum: 6 claims. At least one claim per major section.

> Do not proceed to PHASE 3 until every claim has an ID and its dependencies are mapped.

---

## PHASE 3 — STEP-BY-STEP TRACE

Phase 3 runs in three sub-passes. Complete each sub-pass across ALL inference steps before advancing.

### 3A — FORM IDENTIFICATION PASS

Name the logical form of every inference step. Do not evaluate yet.

```
FORM [C-ID]: [claim text]
Logical form: [modus ponens / modus tollens / hypothetical syllogism / disjunctive syllogism /
               abduction / inductive generalization / argument from analogy /
               argument from authority / causal inference / other: describe]
Formal structure: [If/Then/Therefore skeleton in 1–3 lines]
```

### 3B — VALIDITY CHECK PASS

Run three checks across ALL inference steps. Do not issue verdicts yet. If DRIFT is found, name the term, the definition claim C-ID, and how the meaning shifted.

```
CHECK [C-ID]: [claim text]
  (1) Logical: does the conclusion follow from the premises given the form in 3A?
              [YES] / [WEAK — valid only under assumption: state it] / [NO — describe the gap]
  (2) Empirical: are the premises empirically supported?
              [YES] / [CITED: ref] / [ASSUMED: what is assumed] / [UNSUPPORTED: what evidence is needed]
  (3) Consistency: are key terms used consistently with their definition claims?
              [YES] / [DRIFT: term, definition claim C-ID, how it shifted]
```

### 3C — VERDICT PASS

Issue verdicts based on 3A and 3B. For every WEAK or BROKEN verdict, you must characterize how hard the gap is to catch — your assessment bears on whether a knowledgeable reviewer would catch it before submission.

```
VERDICT [C-ID]: SOUND / WEAK / BROKEN
Reason: [one sentence — why SOUND holds, or what makes it WEAK/BROKEN]
If WEAK or BROKEN:
  Reviewer flag: Would a domain reviewer flag this? YES/NO — one-sentence justification
  Depth tier: OBVIOUS / NOTABLE / SIGNIFICANT
    OBVIOUS — any careful reader notices without domain expertise
    NOTABLE — a methodologically careful reader notices
    SIGNIFICANT — only a domain specialist catches it on first read
  Domain comparison: [one sentence — what domain standard, expectation, or prior result does this gap violate?]
```

---

## PHASE 4 — FAULT REGISTER

Every WEAK or BROKEN verdict from 3C must appear here.

Fault classes (assign exactly one per row):
- **DEF-DRIFT**: a key term shifts meaning between its definition claim and its use
- **UNSUPPORTED-GEN**: a generalization extends beyond what the evidence licenses
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure does not match the stated form

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity |
|------|------|---------|-------|-----|--------------|----------|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [structural explanation] | [exact claim, evidence, or definition change that closes it] | P1/P2/P3 |

Severity:
- P1: breaks the paper's central conclusion
- P2: weakens a key section without invalidating the paper
- P3: precision issue affecting rigor, not validity

Gap field: begin with the depth tier tag from 3C in brackets. Example: `[SIGNIFICANT] The claim that the protocol generalizes across institutional settings is unsupported — no cross-site variance data is reported; a methods reviewer would require it before accepting the generalization.`

**Phase 4 Closing — Null Rejection Test**:

Run the test in three steps:
1. Count rows in the Class column. Name the dominant fault class by code (most rows).
2. Count P1-severity faults. If P1 count > 0, the null is rejected. If P1 count = 0, state whether P2 faults collectively challenge the central argument.
3. State the verdict: "H0 is [rejected / not rejected]. Inertia — submitting without revision — is [not defensible / defensible with minor fixes / defensible]." One sentence.

---

## PHASE 5 — AMEND

Three structural fixes ordered P1 → P2 → P3. Each references the F-ID, C-ID, and Class code it addresses.

1. [P1 fix — F-ID, C-ID, Class: exact repair]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-04 — Combined: Table Phase 3 + Lifecycle Emphasis (Expanded Phase 4 Synthesis)

**Hypothesis**: V-01's table format closes C-04/C-06/C-12/C-15 compliance risks by making every field a named column. The remaining risk under v3 is C-13: a single closing sentence may pass C-13 but produce shallow synthesis. Expanding Phase 4 with a structured three-part synthesis subsection — (1) dominant class by code count, (2) dominant depth tier from the register, (3) verdict on whether the fault pattern confirms or refutes the Phase 0 best-case — ensures all three dimensions of C-13 are addressed without relying on a single free-form sentence. The lifecycle shift: Phase 3 compresses (table replaces sub-passes), Phase 4 expands (synthesis gains structure). Tests whether the compression/expansion trade-off improves synthesis quality.

**What changed**: Phase 3 uses the Inference Trace Table from V-01. Phase 4 gains a three-part Synthesis subsection after the Fault Register table. Phase 4 synthesis is structured as three named bullets rather than one free-form closing sentence. All other mechanisms from V-01 retained.

---

You are running /simulate-argument for: {{topic}}

Every paper makes an implicit bet: "The reader will accept my chain of reasoning." Your job is to find exactly where that bet fails. The adversary is not missing citations — it is the inference that looks valid on first read but collapses under scrutiny.

---

## PHASE 0 — AUTHOR'S BEST CASE

Before tracing, state the argument in its strongest form. One short paragraph — the version the author would give at a conference if they had 60 seconds.

> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

This is the falsification target. The Phase 4 synthesis will return to this statement explicitly.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

After reading, revise your Phase 0 statement if necessary. Then proceed.

---

## PHASE 2 — CLAIM MAP

Extract the full argument as a directed graph. Every claim gets an ID.

| C-ID | Claim | Type | Depends on | Status |
|------|-------|------|------------|--------|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify |
| C-02 | | inference | C-01 | to-verify |

Types:
- **premise**: accepted without proof (cited or stated as assumption)
- **definition**: introduces a term that subsequent claims depend on
- **empirical**: requires data or citation to support
- **inference**: follows logically from prior claims
- **conclusion**: the paper's output claims

Minimum: 6 claims. At least one per major section.

> Do not proceed to PHASE 3 until every claim has an ID and its dependencies are mapped.

---

## PHASE 3 — INFERENCE TRACE TABLE

For every claim with type=inference, complete one row in the Inference Trace Table.

Column definitions:
- **C-ID**: claim identifier from Phase 2
- **Logical Form**: named structure — modus ponens / modus tollens / hypothetical syllogism / disjunctive syllogism / abduction / inductive generalization / argument from analogy / argument from authority / causal inference / other: describe
- **Formal Structure**: If/Then/Therefore skeleton (one line)
- **Logical**: `YES` / `WEAK: [assumption]` / `NO: [gap]`
- **Empirical**: `YES` / `CITED: [ref]` / `ASSUMED: [what]` / `UNSUPPORTED: [what needed]`
- **Consistency**: `YES` / `DRIFT: [term, def claim C-ID, shift]`
- **Verdict**: `SOUND` / `WEAK` / `BROKEN`
- **Reviewer Flag?**: `YES — [justification]` / `NO — [justification]` for WEAK/BROKEN; `N/A` for SOUND
- **Depth**: `OBVIOUS` / `NOTABLE` / `SIGNIFICANT` / `N/A`
  - OBVIOUS: any careful reader notices; NOTABLE: methodological reader notices; SIGNIFICANT: domain specialist only
- **Domain Comparison**: one sentence — what field standard does this gap violate? (`N/A` for SOUND)

| C-ID | Logical Form | Formal Structure | Logical | Empirical | Consistency | Verdict | Reviewer Flag? | Depth | Domain Comparison |
|------|-------------|-----------------|---------|-----------|-------------|---------|---------------|-------|------------------|
| | | | | | | | | | |

> Every BROKEN or WEAK row must have non-empty Reviewer Flag?, Depth, and Domain Comparison. An empty cell in any column is an incomplete trace.

---

## PHASE 4 — FAULT REGISTER + SYNTHESIS

### Fault Register

Every WEAK or BROKEN row from Phase 3 must appear here. Assign exactly one fault class per row.

Fault classes:
- **DEF-DRIFT**: key term shifts meaning between definition claim and use
- **UNSUPPORTED-GEN**: generalization exceeds what evidence licenses
- **CIRCULAR-DEP**: conclusion appears as implicit premise in its own support chain
- **INVALID-FORM**: logical structure does not match the stated form

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity |
|------|------|---------|-------|-----|--------------|----------|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [structural explanation] | [exact claim, evidence, or definition change] | P1/P2/P3 |

Severity: P1 = breaks central conclusion / P2 = weakens key section / P3 = precision issue

Gap field: begin with the depth tier tag in brackets. Example: `[NOTABLE] The move from laboratory findings to field conditions treats an analogy as an identity; a reviewer in applied research methods would require a separate field validation.`

### Phase 4 Synthesis

After completing the Fault Register, write a structured synthesis with three required elements:

**1. Dominant fault class**: Count rows per class code. State: "Dominant fault class: [CODE] ([n] of [total] faults)."

**2. Dominant depth tier**: Count OBVIOUS / NOTABLE / SIGNIFICANT tags in the Gap fields. State: "Dominant depth tier: [TIER] ([n] of [total] faults)." Then interpret: at this depth, would a standard peer review surface these faults before publication?

**3. Phase 0 verdict**: Does the fault pattern confirm or refute the Phase 0 best-case statement? Reference the best-case statement by paraphrase. Name the dominant fault class in your answer. One to two sentences.

---

## PHASE 5 — AMEND

Three structural fixes ordered P1 → P2 → P3. Each references F-ID, C-ID, and Class code, and specifies the exact repair.

1. [P1 fix — F-ID, C-ID, Class: exact repair]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-05 — Combined: All Three Axes (Table + Adversarial + Inertia)

**Hypothesis**: V-01 (table) closes format compliance; V-02 (adversarial) sharpens fault depth; V-03 (inertia) stakes Phase 4 synthesis to a binary decision. These three axes are predicted to be mutually reinforcing rather than conflicting: the adversarial role makes the inertia frame natural (a skeptical reviewer is exactly the adversary of "submit as-is"), and the table makes the adversarial role operational (every step has a column where the reviewer must classify, not just comment). This is the maximum-divergence variation — furthest from all prior round prompts in voice, format, and framing simultaneously. It tests whether the three axes are combinable without friction or whether they create competing expectations.

**What changed**: Phase 0 carries both adversarial framing and null hypothesis (V-02 + V-03). Phase 3 is the Inference Trace Table from V-01 with adversarial-voice column instructions. Phase 4 is the three-part synthesis from V-04, with the third element reformulated as the null-rejection test from V-03. Adversarial voice sustained throughout.

---

You are running /simulate-argument for: {{topic}}

You are the most skeptical reviewer on the program committee. Your prior: this argument has a structural flaw sufficient to warrant rejection or major revision. You are also the adversary of inertia — the belief that "the paper is good enough as-is." Your job is to test both claims rigorously and reach a verdict. Hedging is not available.

The adversary is not missing citations. It is the inference that looks valid on first read but doesn't survive scrutiny from someone who knows the field.

---

## PHASE 0 — WHAT YOU ARE CHALLENGING

Before tracing, state two things:

**Best-case argument** (one paragraph): What would this argument look like if fully sound? State it as the authors would.
> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

**Null hypothesis** (one sentence): The case for inertia.
> "H0: This argument is structurally sound and requires no revision before submission."

You will attempt to reject H0. If you cannot, you must say so explicitly.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

After reading, update your Phase 0 statement if necessary. Then proceed.

---

## PHASE 2 — CLAIM MAP

Reconstruct the argument you plan to challenge. Explicit dependencies reveal where the argument is load-bearing and where it is implicit.

| C-ID | Claim | Type | Depends on | Status |
|------|-------|------|------------|--------|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify |
| C-02 | | inference | C-01 | to-verify |

Types:
- **premise**: accepted without proof (cited or stated as assumption)
- **definition**: introduces a term that subsequent claims depend on
- **empirical**: requires data or citation to support
- **inference**: follows logically from prior claims
- **conclusion**: the paper's output claims

Minimum: 6 claims. At least one per major section. Definition claims are high priority — they are where DEF-DRIFT originates.

> Do not proceed to PHASE 3 until every claim has an ID and its dependencies are mapped.

---

## PHASE 3 — INFERENCE TRACE TABLE

For every claim with type=inference, complete one row. As the skeptical reviewer, your column entries should reflect what you would write in a review form, not what the authors would write in a rebuttal.

Column definitions:
- **C-ID**: claim identifier from Phase 2
- **Logical Form**: named structure — modus ponens / modus tollens / hypothetical syllogism / disjunctive syllogism / abduction / inductive generalization / argument from analogy / argument from authority / causal inference / other: describe
- **Formal Structure**: If/Then/Therefore skeleton (one line)
- **Logical**: does the conclusion follow given the stated form? `YES` / `WEAK: [hidden assumption]` / `NO: [gap description]`
- **Empirical**: are the premises backed? `YES` / `CITED: [ref]` / `ASSUMED: [what is taken for granted]` / `UNSUPPORTED: [what the review would request]`
- **Consistency**: are terms used as defined? `YES` / `DRIFT: [term, def claim C-ID, how it shifted]`
- **Verdict**: `SOUND` / `WEAK` / `BROKEN`
- **Reviewer Flag?**: As the skeptical reviewer, would you flag this in a written review? `YES — [one-sentence justification]` / `NO — [one-sentence justification]` (`N/A` for SOUND)
- **Depth**: How hard is this to catch? `OBVIOUS` / `NOTABLE` / `SIGNIFICANT` / `N/A`
  - OBVIOUS: any reader catches it; NOTABLE: a careful methodological reader catches it; SIGNIFICANT: only a specialist catches it on first read
- **Domain Comparison**: one sentence — what standard or prior result in this domain does this gap violate? (`N/A` for SOUND)

| C-ID | Logical Form | Formal Structure | Logical | Empirical | Consistency | Verdict | Reviewer Flag? | Depth | Domain Comparison |
|------|-------------|-----------------|---------|-----------|-------------|---------|---------------|-------|------------------|
| | | | | | | | | | |

> Every BROKEN or WEAK row must have non-empty Reviewer Flag?, Depth, and Domain Comparison. An empty cell is an incomplete review.

---

## PHASE 4 — FAULT REGISTER + SYNTHESIS

### Fault Register

Every WEAK or BROKEN row from Phase 3 must appear here. Assign exactly one fault class per row.

Fault classes:
- **DEF-DRIFT**: key term shifts meaning between its definition claim and its use in this inference
- **UNSUPPORTED-GEN**: generalization extends beyond what the evidence licenses
- **CIRCULAR-DEP**: conclusion appears as implicit premise in its own support chain
- **INVALID-FORM**: logical structure does not match the stated form

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity |
|------|------|---------|-------|-----|--------------|----------|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [structural explanation] | [exact claim, evidence, or definition change] | P1/P2/P3 |

Severity: P1 = breaks central conclusion / P2 = weakens key section / P3 = precision issue

Gap field: begin with the depth tier tag from Phase 3 in brackets. Example: `[SIGNIFICANT] The argument treats a single-cohort finding as sufficient to license a population-level policy claim; a reviewer in public health methodology would require multi-site replication before accepting the generalization.`

### Phase 4 Synthesis

After completing the Fault Register, write a structured synthesis with three elements:

**1. Dominant fault class**: Count rows per class code. State: "Dominant fault class: [CODE] ([n] of [total] faults)."

**2. Dominant depth tier**: Count OBVIOUS / NOTABLE / SIGNIFICANT tags in the Gap fields. State: "Dominant depth tier: [TIER] ([n] of [total] faults)." Then assess: at this depth, would standard peer review catch these faults before publication?

**3. Null rejection verdict**: Run the test. Count P1-severity faults. If P1 count > 0, H0 is rejected — name the dominant fault class in the rejection statement. If P1 count = 0, assess whether the P2 faults collectively undermine the central argument. State: "H0 is [rejected / not rejected]. Inertia is [not defensible / defensible with revisions / defensible]." One sentence.

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

### Rubric Coverage by Variation (v3 rubric — 7 aspirationals)

| Criterion | R2 V-05 (v3 baseline ~98) | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|---|
| C-04 inference steps traced | PASS | PASS (table row = STEP unit) | PASS (3A/3B/3C) | PASS (3A/3B/3C) | PASS (table) | PASS (table) |
| C-06 logical forms named | PASS | **stronger** (column; empty cell = visible) | PASS (3A dedicated) | PASS (3A dedicated) | **stronger** (column) | **stronger** (column) |
| C-09 term drift pinpointed | PASS | = | = (3B DRIFT+C-ID) | = (3B DRIFT+C-ID) | = | = |
| C-10 structural weakness | PASS | **stronger** (Domain Comparison column forces structural characterization) | **strongest** (adversarial prior + depth scale) | = | **stronger** | **strongest** |
| C-11 falsification target | PASS | = | = | **stronger** (null-hypothesis + binary reject verdict) | = | **strongest** (null + adversarial) |
| C-12 inline reviewer hook | PASS | PASS (Reviewer Flag? column) | **stronger** (natural to adversarial role) | = | PASS (column) | **stronger** |
| C-13 fault pattern closure | PASS | = (class code count) | = (class code count) | **stronger** (3-step reject test names class) | **strongest** (3-part synthesis section) | **strongest** |
| C-14 fault class taxonomy | PASS | PASS | PASS | PASS | PASS | PASS |
| C-15 reviewer depth tier | **FAIL** | **PASS** (Depth column + Domain Comparison column + tier tag in Gap field) | **PASS** (depth tier in 3C + domain comparison + tier tag in Gap field) | **PASS** (depth tier in 3C + domain comparison + tier tag in Gap field) | **PASS** (Depth + Domain Comparison columns) | **PASS** (Depth + Domain Comparison columns) |

**Predicted v3 scores**:
- V-01: 7/7 aspirationals → 100 (table format enforces C-15; class column retained for C-14)
- V-02: 7/7 aspirationals → 100 (depth tier added to 3C; class column retained for C-14; C-13 via code count)
- V-03: 7/7 aspirationals → 100 (depth tier added to 3C; null-rejection test satisfies C-13 with class code; C-14 retained)
- V-04: 7/7 aspirationals → 100 (V-01 table + 3-part synthesis; all C-15 columns + C-14 column retained)
- V-05: 7/7 aspirationals → 100 (all mechanisms; adversarial role sharpens depth and C-10; null-rejection sharpens C-13)
