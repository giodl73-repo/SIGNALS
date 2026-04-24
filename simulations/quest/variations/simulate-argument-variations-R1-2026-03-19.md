Written to `simulations/quest/variations/simulate-argument-variations-R1-2026-03-19.md`.

---

## simulate-argument — Variation Set R1

### Variation Matrix

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **Axis** | Role sequence | Output format | Lifecycle emphasis | Lifecycle + phrasing | Inertia framing + role sequence |
| **Type** | Single | Single | Single | Combined | Combined |

---

### V-01 — Role Sequence: Skeptic-First
**Hypothesis**: Seeding an adversarial posture before the trace causes the model to enter phase 3 already looking for failure rather than confirming the author's logic — more BROKEN verdicts, better C-10 gap depth.

**What changed**: Added a `SKEPTIC CHALLENGE` preamble (prior statement before reading) and a `SKEPTIC` vs `TRACER` mode framing. After reading, the model updates its prior. Each STEP cross-checks against the prior.

---

### V-02 — Output Format: Prose Trace
**Hypothesis**: Prose paragraphs will produce richer "why it fails" explanations for C-10, at the cost of C-04 mechanical completeness. Tests whether structure drives compliance.

**What changed**: Phase 3 STEP code blocks replaced with structured prose paragraphs. The three validity checks are embedded as numbered questions within the paragraph. Verdict is still required on the final line.

---

### V-03 — Lifecycle Emphasis: Phase 3 Expanded (Three Sub-Passes)
**Hypothesis**: Splitting phase 3 into sub-passes (3A form identification → 3B validity checks → 3C verdicts) forces the model to slow down and prevents merging or skipping individual checks — improves C-04 and C-06 pass rates.

**What changed**: Phase 3 runs three sequential sub-passes across ALL inferences before advancing. 3A: name the logical form only. 3B: run the three checks, no verdict yet. 3C: issue verdicts only. The gate between sub-passes is explicit.

---

### V-04 — Combined: Lifecycle Emphasis + Phrasing Register (Socratic)
**Hypothesis**: Socratic question framing elicits more natural reasoning and surfaces non-obvious gaps (better C-10), while the explicit gating questions prevent phase-skipping (preserves C-04). Risk: reduced mechanical format compliance on C-07/C-08.

**What changed**: All four phases reframed as Questions 1-4. Each question states what the model is trying to find out, not what procedure to execute. Phase 3 adds `Q2d` as a fourth check (term consistency surfaced explicitly). Conversational but still fully structured.

---

### V-05 — Combined: Inertia Framing + Role Sequence (Claim-vs-Holds-Up)
**Hypothesis**: Leading with the author's best-case statement (Phase 0) gives the model something to actively falsify, sharpening focus on structural rather than surface faults (better C-10 non-obvious gap detection). The fault register closes by asking whether the fault pattern confirms or refutes the Phase 0 frame.

**What changed**: Added `PHASE 0 — AUTHOR'S BEST CASE` before signal acquisition. STEP blocks add a `YES/NO` question "Would a domain reviewer flag this?" after WEAK/BROKEN verdicts. Fault register ends with a one-sentence verdict on whether the best-case framing survived. AMEND fixes require explicit F-ID + C-ID references.

---

### Rubric Coverage by Variation

| Criterion | Base | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|------|
| C-04 inference steps traced | base | = | risk | stronger | = | = |
| C-05 fault register complete | base | stronger | = | = | = | = |
| C-06 logical forms named | base | = | = | stronger | stronger | = |
| C-07 AMEND actionable | base | stronger | = | stronger | = | stronger |
| C-09 term drift | base | = | = | stronger (3B) | stronger (Q2d) | = |
| C-10 structural weakness | base | stronger | stronger | = | stronger | strongest |
SKEPTIC CHALLENGE prior?

---

## PHASE 4 — FAULT REGISTER

| F-ID | C-ID | Verdict | Gap | Fix required | Severity |
|------|------|---------|-----|--------------|----------|
| F-01 | | BROKEN | [what's missing and why the inference fails] | [what claim or evidence closes it] | P1/P2/P3 |

Severity:
- P1: breaks the paper's central conclusion — must fix before submission
- P2: weakens a key section — weakens the paper but doesn't invalidate it
- P3: cosmetic / precision issue — affects rigor but not validity

---

## PHASE 5 — AMEND

Three structural fixes ordered by severity:
1. [P1 fix — reference F-ID and C-ID; name the exact claim, evidence, or definition change needed]
2. [P2 fix — reference F-ID and C-ID; name the exact claim, evidence, or definition change needed]
3. [P3 fix — if term drift was found, name the definition claim (C-ID) where drift originates and propose stable replacement wording]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-02 — Axis: Output Format (Prose Trace)

**Hypothesis**: Replacing the STEP code-block format with flowing prose for each inference step will produce richer "why it fails" explanations (better C-10 gap depth) but risks missing the three validity checks mechanically (hurts C-04). Good test of whether structure drives compliance.

---

You are running /simulate-argument for: {{topic}}

Trace the logical argument chain of a paper step by step — the way simulate-state traces state transitions. Academic papers have causal chains (P01's formula → P02's states → P03's dynamics). Hand-compile the argument to find exactly where it breaks.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

---

## PHASE 2 — CLAIM MAP

Extract the full argument as a directed graph. Every claim gets an ID.

| C-ID | Claim | Type | Depends on | Status |
|------|-------|------|------------|--------|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify |
| C-02 | | inference | C-01 | to-verify |
...

Types:
- **premise**: accepted without proof in this paper (must be cited or stated as assumption)
- **definition**: introduces a term that subsequent claims depend on
- **empirical**: requires data or citation to support
- **inference**: follows logically from prior claims (verify the logic)
- **conclusion**: the paper's output claims

Minimum: 6 claims. Every paper section should contribute at least 1 claim.

> Do not proceed to PHASE 3 until every claim has an ID and its dependencies are mapped.

---

## PHASE 3 — STEP-BY-STEP TRACE

For each inference step (any claim with type=inference), write a prose paragraph structured as follows:

**[C-ID] — [claim text]**

Name the logical form this step uses (modus ponens, abduction, analogy, inductive generalization, etc.). Then address three questions in order:

1. *Logical validity*: Does the stated conclusion actually follow from C-[n] and C-[m]? Work through the argument structure. Note whether it holds (YES), holds conditionally (WEAK — explain the condition), or fails (NO — explain the gap).

2. *Empirical grounding*: Are the premises that feed this step backed by data, citation, or prior proof — or are they assumed? Note: CITED (explicit reference), ASSUMED (stated without support), or UNSUPPORTED (required but absent).

3. *Term consistency*: Do the key terms in this step mean the same thing they meant in their definition claims? If any term has shifted in scope or precision, note: DRIFT and describe exactly what changed and where.

Close the paragraph with a one-line verdict: **SOUND**, **WEAK**, or **BROKEN**, and if WEAK or BROKEN, one sentence on what specifically fails.

---

## PHASE 4 — FAULT REGISTER

| F-ID | C-ID | Verdict | Gap | Fix required | Severity |
|------|------|---------|-----|--------------|----------|
| F-01 | | BROKEN | [what's missing] | [what claim or evidence closes it] | P1/P2/P3 |

Severity:
- P1: breaks the paper's central conclusion — must fix before submission
- P2: weakens a key section — weakens the paper but doesn't invalidate it
- P3: cosmetic / precision issue — affects rigor but not validity

---

## PHASE 5 — AMEND

Three structural fixes ordered by severity:
1. [P1 fix: how to repair or replace the broken inference]
2. [P2 fix: how to strengthen the weakest empirical claim]
3. [P3 fix: where a definition is drifting and how to stabilize it]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-03 — Axis: Lifecycle Emphasis (Phase 3 Expanded)

**Hypothesis**: Giving phase 3 more explicit sub-steps — separating the logical-form identification pass from the validity-check pass from the verdict pass — will improve C-04 and C-06 pass rates because the model is forced to slow down and cannot merge or skip individual checks.

---

You are running /simulate-argument for: {{topic}}

Trace the logical argument chain of a paper step by step — the way simulate-state traces state transitions. Academic papers have causal chains (P01's formula → P02's states → P03's dynamics). Hand-compile the argument to find exactly where it breaks.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

---

## PHASE 2 — CLAIM MAP

Extract the full argument as a directed graph. Every claim gets an ID.

| C-ID | Claim | Type | Depends on | Status |
|------|-------|------|------------|--------|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify |
| C-02 | | inference | C-01 | to-verify |
...

Types:
- **premise**: accepted without proof in this paper (must be cited or stated as assumption)
- **definition**: introduces a term that subsequent claims depend on
- **empirical**: requires data or citation to support
- **inference**: follows logically from prior claims (verify the logic)
- **conclusion**: the paper's output claims

Minimum: 6 claims. Every paper section should contribute at least 1 claim.

> Do not proceed to PHASE 3 until every claim has an ID and its dependencies are mapped.

---

## PHASE 3 — STEP-BY-STEP TRACE

Phase 3 runs in three sub-passes. Complete each sub-pass across ALL inference steps before starting the next.

### 3A — FORM IDENTIFICATION PASS

For every inference claim, name its logical form only. Do not evaluate yet.

```
FORM [C-ID]: [claim text]
Logical form: [modus ponens / modus tollens / hypothetical syllogism / disjunctive syllogism /
               abduction / inductive generalization / argument from analogy /
               argument from authority / causal inference / other: describe]
Formal structure: [write out the If/Then/Therefore skeleton in 1-3 lines]
```

### 3B — VALIDITY CHECK PASS

For every inference claim, run the three checks. Do not issue verdicts yet.

```
CHECK [C-ID]: [claim text]
  (1) Logical: Does the conclusion follow from the premises given the form identified in 3A?
              [YES — deductively valid] / [WEAK — valid under assumption: state it] / [NO — describe the gap]
  (2) Empirical: Are the premises feeding this step supported?
              [YES / CITED: ref] / [ASSUMED: what is assumed] / [UNSUPPORTED: what is needed]
  (3) Consistency: Are key terms used with the same meaning as their definition claims?
              [YES] / [DRIFT: term, definition claim C-ID, and how it shifted]
```

### 3C — VERDICT PASS

For every inference claim, issue the verdict based on 3A and 3B findings.

```
VERDICT [C-ID]: SOUND / WEAK / BROKEN
Reason: [one sentence — why SOUND holds, or exactly what makes it WEAK/BROKEN]
```

---

## PHASE 4 — FAULT REGISTER

Every claim with WEAK or BROKEN verdict from 3C must appear here.

| F-ID | C-ID | Verdict | Gap | Fix required | Severity |
|------|------|---------|-----|--------------|----------|
| F-01 | | BROKEN | [what's missing] | [what claim or evidence closes it] | P1/P2/P3 |

Severity:
- P1: breaks the paper's central conclusion — must fix before submission
- P2: weakens a key section — weakens the paper but doesn't invalidate it
- P3: cosmetic / precision issue — affects rigor but not validity

---

## PHASE 5 — AMEND

Three structural fixes ordered by severity. Each fix must reference the F-ID and C-ID it addresses.

1. [P1 fix — F-ID, C-ID: exact claim, evidence, or definition change needed]
2. [P2 fix — F-ID, C-ID: exact claim, evidence, or definition change needed]
3. [P3 fix — F-ID, C-ID: if DRIFT found, name the definition claim and propose stable wording; otherwise name the precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-04 — Combined Axis: Lifecycle Emphasis + Phrasing Register (Socratic)

**Hypothesis**: Framing each phase as a Socratic question the model must answer — rather than a procedure it must execute — will elicit more natural reasoning and surface non-obvious gaps (better C-10), while the explicit gating questions prevent phase-skipping (preserves C-04). Risk: reduced mechanical format compliance on C-07/C-08.

---

You are running /simulate-argument for: {{topic}}

A paper's argument is a chain of claims. Each link in the chain is an inference. Your job is to ask, for every inference: "Does this actually follow?" Work through it the way a careful reader would — step by step, without giving the author the benefit of the doubt.

---

## QUESTION 1: What does the paper actually claim?

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

When you are done reading, ask yourself: "What is the single conclusion this paper most needs to be true? And what chain of claims does it build to get there?" Write that chain down as a table.

| C-ID | Claim | Type | Depends on | Status |
|------|-------|------|------------|--------|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify |
| C-02 | | inference | C-01 | to-verify |
...

Types:
- **premise**: accepted without proof in this paper (must be cited or stated as assumption)
- **definition**: introduces a term that subsequent claims depend on
- **empirical**: requires data or citation to support
- **inference**: follows logically from prior claims (verify the logic)
- **conclusion**: the paper's output claims

You need at least 6 claims. Every major section of the paper should contribute at least one.

> Do not move to the next question until every claim has an ID and every dependency is mapped.

---

## QUESTION 2: For each inference — does this actually follow?

For every claim you labeled type=inference, ask three questions in sequence:

```
STEP [C-ID]: [claim text]
Depends on: [C-IDs]

Q2a. What kind of move is the author making here?
     Name the logical form: modus ponens, abduction, inductive generalization, analogy, etc.
     Write the skeleton: If [X] and [Y], then [Z].

Q2b. Does Z actually follow from X and Y, given that form?
     [YES] — it follows / [WEAK — it follows IF: state the unstated assumption] / [NO — here is where it breaks: ...]

Q2c. Are X and Y themselves supported, or is the author assuming them?
     [YES / CITED: reference] / [ASSUMED: what is being assumed] / [UNSUPPORTED: what would be needed]

Q2d. Does the author use the same words here as they defined earlier?
     [YES] / [DRIFT: which term, where it was defined (C-ID), and how it shifted here]

Verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN — in one sentence, what specifically fails?
```

---

## QUESTION 3: What breaks, and how badly?

Collect every WEAK and BROKEN verdict into a register. For each one, ask: "Is this a crack in the foundation, a weakness in one wall, or a surface imprecision?"

| F-ID | C-ID | Verdict | Gap | Fix required | Severity |
|------|------|---------|-----|--------------|----------|
| F-01 | | BROKEN | [what's missing and why the inference fails] | [what claim or evidence would close the gap] | P1/P2/P3 |

- **P1**: If this gap stands, the central conclusion doesn't hold.
- **P2**: This gap weakens a key section but the conclusion survives.
- **P3**: This is a precision or consistency issue — real but not fatal.

---

## QUESTION 4: What would you tell the author to fix?

Give three concrete repair instructions, most urgent first. Each one should name the fault (F-ID), the claim it affects (C-ID), and what change — to a claim, a piece of evidence, or a definition — would close the gap.

1. [P1 fix]
2. [P2 fix]
3. [P3 fix — if you found term drift, name the definition claim (C-ID) where it originates and propose exact replacement wording]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-05 — Combined Axis: Inertia Framing + Role Sequence (Claim-vs-Holds-Up)

**Hypothesis**: Leading with an explicit "what the paper claims vs what actually holds up" frame — borrowed from the inertia pattern of identifying the status-quo vs the challenger — will sharpen the model's lens toward non-obvious structural faults (C-10) and cause it to front-load skepticism before the mechanical trace begins. The role sequence variation adds a brief "author's best case" statement that the model then has to falsify, increasing the chance it finds the real gap rather than a surface one.

---

You are running /simulate-argument for: {{topic}}

Every paper makes an implicit bet: "The reader will accept my chain of reasoning." Your job is to find exactly where that bet fails. The primary adversary is not missing citations — it is the inference that looks valid on first read but doesn't survive scrutiny.

---

## PHASE 0 — AUTHOR'S BEST CASE

Before tracing the argument, state it in its strongest form — the version the author would give at a conference if they had 60 seconds. One short paragraph. This is the claim you are about to test.

> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: discover-hypothesis, discover-causal, specify-spec.

After reading, update your PHASE 0 statement if necessary. Then proceed.

---

## PHASE 2 — CLAIM MAP

Extract the full argument as a directed graph. Every claim gets an ID.

| C-ID | Claim | Type | Depends on | Status |
|------|-------|------|------------|--------|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | — | to-verify |
| C-02 | | inference | C-01 | to-verify |
...

Types:
- **premise**: accepted without proof in this paper (must be cited or stated as assumption)
- **definition**: introduces a term that subsequent claims depend on
- **empirical**: requires data or citation to support
- **inference**: follows logically from prior claims (verify the logic)
- **conclusion**: the paper's output claims

Minimum: 6 claims. Every paper section should contribute at least 1 claim.

> Do not proceed to PHASE 3 until every claim has an ID and its dependencies are mapped.

---

## PHASE 3 — STEP-BY-STEP TRACE

For each inference step, your question is: "Does the author's best-case argument survive here, or does it break?"

```
STEP [C-ID]: [claim text]
Depends on: [C-IDs]
Logical form: [name the structure — modus ponens, abduction, inductive generalization, analogy, causal inference, etc.]
Validity check:
  - Does the conclusion follow from the premises? [YES / WEAK / NO]
  - Are the premises empirically supported? [YES / CITED / ASSUMED / UNSUPPORTED]
  - Are key terms used consistently with their definitions? [YES / DRIFT: describe]
Verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN: [explain WHY it fails — not just that it does. Would a domain reviewer flag this as non-obvious? YES/NO]
```

---

## PHASE 4 — FAULT REGISTER

| F-ID | C-ID | Verdict | Gap | Fix required | Severity |
|------|------|---------|-----|--------------|----------|
| F-01 | | BROKEN | [what's missing — and why the inference fails structurally, not just superficially] | [what claim or evidence closes it] | P1/P2/P3 |

Severity:
- P1: breaks the paper's central conclusion — must fix before submission
- P2: weakens a key section — weakens the paper but doesn't invalidate it
- P3: cosmetic / precision issue — affects rigor but not validity

After filling the register, note: does the fault pattern confirm or refute the PHASE 0 best-case framing? One sentence.

---

## PHASE 5 — AMEND

Three structural fixes ordered by severity. Each fix must reference the F-ID and C-ID it addresses and specify the exact change needed — not "add evidence" but what claim, what evidence, or what definition stabilization would close the gap.

1. [P1 fix — F-ID, C-ID: exact repair]
2. [P2 fix — F-ID, C-ID: exact repair]
3. [P3 fix — F-ID, C-ID: if DRIFT found, name the originating definition claim (C-ID) and propose stable replacement wording]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]
