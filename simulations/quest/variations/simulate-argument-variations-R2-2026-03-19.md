Written to `simulations/quest/variations/simulate-argument-variations-R2-2026-03-19.md`.

---

## simulate-argument — Variation Set R2

### Variation Matrix

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **Axis** | Phase 0 depth | Inline hook scoring scale | Fault taxonomy enforcement | Sub-passes + Phase 0/hooks | All mechanisms + taxonomy |
| **Type** | Single | Single | Single | Combined | Combined |

---

**R2 design rationale**: R1 V-05 scored 100 under v1 rubric by introducing C-11/C-12/C-13. Under v2, the aspirational pool grows to five criteria — and all five must pass to reach the ceiling. Three soft spots in R1 V-05 drive all R2 choices:

| Soft spot | Root cause | R2 fix |
|-----------|-----------|--------|
| C-11 free-form Phase 0 | Easy to satisfy with a vague restatement | V-01: 3-part structured template (Central claim / Load-bearing premises / Full-soundness condition) |
| C-12 binary YES/NO hook | Model can write one terse line and pass | V-02: OBVIOUS/NOTABLE/SIGNIFICANT scale + required domain comparison sentence |
| C-13 "name the dominant class" | Model invents a label; criterion is judgment-dependent | V-03: enumerated taxonomy column in Fault Register — closure counts rows, doesn't invent |

---

### Single-axis variations

**V-01 — Phase 0 depth**: Structured 3-part falsification target (Central claim / Load-bearing premises / Full-soundness condition). Phase 4 closure must reference the full-soundness condition by name. Strengthens C-11 from aspiration to mechanical gate.

**V-02 — Inline hook scoring scale**: YES/NO replaced with OBVIOUS/NOTABLE/SIGNIFICANT + required domain comparison sentence. Gap field in Fault Register carries the tier tag. Phase 4 closes by naming the dominant tier. Strengthens C-12 and C-10 simultaneously.

**V-03 — Fault taxonomy enforcement**: Fault Register gains a `Class` column (DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM). Phase 4 closure names the dominant class by code. C-13 becomes countable rather than subjective.

---

### Combined variations

**V-04 — Sub-passes + Phase 0 + hooks**: R1 V-03 (3A/3B/3C gating, DRIFT+C-ID in 3B) stacked with R1 V-05 (Phase 0, reviewer hook in 3C, fault closure). Orthogonal mechanisms — no conflict. Collectively enforces all five aspirationals.

**V-05 — All mechanisms + taxonomy**: V-04 + enumerated fault taxonomy from V-03 single-axis. C-13 becomes fully mechanical: the model counts class rows rather than inventing a label. Maximum coverage under v2 rubric — every aspirational criterion has a specific structural mechanism.

---

### Predicted rubric coverage delta vs R1 V-05

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 term drift | = | = | = | stronger | stronger |
| C-10 structural weakness | = | **strongest** | = | = | = |
| C-11 falsification target | **strongest** | = | = | = | = |
| C-12 inline reviewer hook | = | **stronger** | = | = (3C) | = (3C) |
| C-13 fault pattern closure | **stronger** | stronger | **strongest** | stronger | **strongest** |
c.

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
  - Are key terms used consistently with their definitions? [YES / DRIFT: term, definition claim C-ID, how it shifted]
Verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN: [explain WHY it fails — not just that it does. Would a domain reviewer flag this as non-obvious? YES/NO — one sentence justification]
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

After filling the register, answer: does the fault pattern confirm or refute the **full-soundness condition** stated in PHASE 0? Reference that condition explicitly in your answer. One to two sentences.

---

## PHASE 5 — AMEND

Three structural fixes ordered by severity. Each fix must reference the F-ID and C-ID it addresses and specify the exact change needed — not "add evidence" but what claim, what evidence, or what definition stabilization would close the gap.

1. [P1 fix — F-ID, C-ID: exact repair]
2. [P2 fix — F-ID, C-ID: exact repair]
3. [P3 fix — F-ID, C-ID: if DRIFT found, name the originating definition claim (C-ID) and propose stable replacement wording]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-02 — Axis: Inline Hook Scoring Scale

**Hypothesis**: The binary YES/NO reviewer hook is the weakest enforcement in R1 V-05 — a model can write "Would a domain reviewer flag this? YES" with no further content and technically satisfy C-12. Replacing YES/NO with a three-tier depth scale (OBVIOUS/NOTABLE/SIGNIFICANT) and requiring a one-sentence domain comparison forces the model to classify the fault's non-obviousness, which is exactly what C-10 measures. The Phase 4 closing note can then name which tier dominated rather than inventing a label.

**What changed**: The STEP block reviewer hook becomes a three-tier scale with a required domain comparison sentence. Phase 4 Gap field must include the tier tag. The closing sentence names the dominant tier.

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
  - Are key terms used consistently with their definitions? [YES / DRIFT: term, definition claim C-ID, how it shifted]
Verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN:
  Gap: [explain WHY it fails — not just that it does]
  Reviewer depth: [OBVIOUS — any reader notices | NOTABLE — a careful reader flags | SIGNIFICANT — only a domain expert catches]
  Domain comparison: [one sentence — how a reviewer with domain knowledge would characterize this gap; what standard or expectation does it violate?]
```

---

## PHASE 4 — FAULT REGISTER

| F-ID | C-ID | Verdict | Gap | Fix required | Severity |
|------|------|---------|-----|--------------|----------|
| F-01 | | BROKEN | [SIGNIFICANT/NOTABLE/OBVIOUS] [structural explanation of why the inference fails] | [what claim or evidence closes it] | P1/P2/P3 |

Severity:
- P1: breaks the paper's central conclusion — must fix before submission
- P2: weakens a key section — weakens the paper but doesn't invalidate it
- P3: cosmetic / precision issue — affects rigor but not validity

After filling the register, note: does the fault pattern confirm or refute the PHASE 0 best-case framing? Name the dominant reviewer depth tier (SIGNIFICANT / NOTABLE / OBVIOUS) that characterizes the faults. One sentence.

---

## PHASE 5 — AMEND

Three structural fixes ordered by severity. Each fix must reference the F-ID and C-ID it addresses and specify the exact change needed — not "add evidence" but what claim, what evidence, or what definition stabilization would close the gap.

1. [P1 fix — F-ID, C-ID: exact repair]
2. [P2 fix — F-ID, C-ID: exact repair]
3. [P3 fix — F-ID, C-ID: if DRIFT found, name the originating definition claim (C-ID) and propose stable replacement wording]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-03 — Axis: Fault Taxonomy Enforcement

**Hypothesis**: C-13 requires Phase 4 to name the "dominant fault class" — but without a defined taxonomy, the model invents a label and the criterion becomes judgment-dependent. Providing an enumerated set of named fault classes as a required column in the Fault Register forces categorization at insertion time. The Phase 4 closure then counts rather than invents — it sees which class appeared most and names it. This is the minimum change needed to make C-13 mechanically pass-or-fail.

**What changed**: Fault Register gains a `Class` column with four enumerated fault classes. The Phase 4 closing sentence must name the dominant class by code. The four classes cover the most common academic argument failure modes.

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
  - Are key terms used consistently with their definitions? [YES / DRIFT: term, definition claim C-ID, how it shifted]
Verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN: [explain WHY it fails — not just that it does. Would a domain reviewer flag this as non-obvious? YES/NO — one sentence justification]
```

---

## PHASE 4 — FAULT REGISTER

Fault classes:
- **DEF-DRIFT**: a key term shifts meaning between definition and use
- **UNSUPPORTED-GEN**: a generalization exceeds what the evidence licenses
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure does not match the stated form

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity |
|------|------|---------|-------|-----|--------------|----------|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [what's missing — and why the inference fails structurally] | [what claim or evidence closes it] | P1/P2/P3 |

Severity:
- P1: breaks the paper's central conclusion — must fix before submission
- P2: weakens a key section — weakens the paper but doesn't invalidate it
- P3: cosmetic / precision issue — affects rigor but not validity

After filling the register, note: does the fault pattern confirm or refute the PHASE 0 best-case framing? State the dominant fault class by code (most rows in the Class column). One sentence.

---

## PHASE 5 — AMEND

Three structural fixes ordered by severity. Each fix must reference the F-ID and C-ID it addresses and specify the exact change needed — not "add evidence" but what claim, what evidence, or what definition stabilization would close the gap.

1. [P1 fix — F-ID, C-ID: exact repair]
2. [P2 fix — F-ID, C-ID: exact repair]
3. [P3 fix — F-ID, C-ID: if DRIFT found, name the originating definition claim (C-ID) and propose stable replacement wording]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-04 — Combined: Sub-Passes + Phase 0 + Inline Hooks

**Hypothesis**: R1 V-03 (three sub-passes) was the strongest C-04/C-06/C-09 performer because 3A/3B/3C gating prevents check-merging and requires DRIFT with C-ID inside 3B itself. R1 V-05 was the strongest C-10/C-11/C-12/C-13 performer via Phase 0 + inline hooks + fault closure. These mechanisms address orthogonal compliance risks and can be stacked without conflict. Combined, this variation enforces all five aspirationals: 3B provides C-ID in DRIFT (C-09), 3C adds reviewer hook (C-12), Phase 0 provides falsification target (C-11), Phase 4 closure connects to Phase 0 (C-13), and the reviewer hook in 3C provides non-obvious characterization (C-10).

**What changed**: Phase 0 added (V-05 pattern). Phase 3 expanded to 3A/3B/3C (V-03 pattern). DRIFT in 3B requires C-ID. 3C adds reviewer hook on WEAK/BROKEN verdicts. Phase 4 closing sentence names dominant fault class.

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
If WEAK or BROKEN: Would a domain reviewer flag this as non-obvious? YES/NO — one sentence justification
```

---

## PHASE 4 — FAULT REGISTER

Every claim with WEAK or BROKEN verdict from 3C must appear here.

| F-ID | C-ID | Verdict | Gap | Fix required | Severity |
|------|------|---------|-----|--------------|----------|
| F-01 | | BROKEN | [what's missing — and why the inference fails structurally, not just superficially] | [what claim or evidence closes it] | P1/P2/P3 |

Severity:
- P1: breaks the paper's central conclusion — must fix before submission
- P2: weakens a key section — weakens the paper but doesn't invalidate it
- P3: cosmetic / precision issue — affects rigor but not validity

After filling the register, note: does the fault pattern confirm or refute the PHASE 0 best-case framing? Name the dominant fault class (e.g., definitional drift, unsupported generalization, circular dependency, invalid analogy). One sentence.

---

## PHASE 5 — AMEND

Three structural fixes ordered by severity. Each fix must reference the F-ID and C-ID it addresses and specify the exact change needed — not "add evidence" but what claim, what evidence, or what definition stabilization would close the gap.

1. [P1 fix — F-ID, C-ID: exact repair]
2. [P2 fix — F-ID, C-ID: exact repair]
3. [P3 fix — F-ID, C-ID: if DRIFT found, name the originating definition claim (C-ID) and propose stable replacement wording]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-05 — Combined: All Mechanisms + Fault Taxonomy

**Hypothesis**: V-04 stacks R1's two strongest patterns. Adding the enumerated fault taxonomy from V-03 (single-axis) makes C-13 fully mechanical: Phase 4 counts class rows rather than requires the model to invent a dominant class label. The taxonomy also sharpens C-10 fault depth because classifying DEF-DRIFT vs UNSUPPORTED-GEN vs CIRCULAR-DEP forces structural characterization rather than a generic "inference is weak" label. This is the maximum-coverage variation — every aspirational criterion is enforced by a specific structural mechanism rather than an instruction.

**What changed from V-04**: Fault Register gains a `Class` column with four enumerated fault classes. Phase 4 closure must name the dominant class by code (most rows in the Class column). AMEND fixes reference the Class code alongside F-ID and C-ID.

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
If WEAK or BROKEN: Would a domain reviewer flag this as non-obvious? YES/NO — one sentence justification
```

---

## PHASE 4 — FAULT REGISTER

Every claim with WEAK or BROKEN verdict from 3C must appear here.

Fault classes:
- **DEF-DRIFT**: a key term shifts meaning between definition and use
- **UNSUPPORTED-GEN**: a generalization exceeds what the evidence licenses
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure does not match the stated form

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity |
|------|------|---------|-------|-----|--------------|----------|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [what's missing — and why the inference fails structurally, not just superficially] | [what claim or evidence closes it] | P1/P2/P3 |

Severity:
- P1: breaks the paper's central conclusion — must fix before submission
- P2: weakens a key section — weakens the paper but doesn't invalidate it
- P3: cosmetic / precision issue — affects rigor but not validity

After filling the register, note: does the fault pattern confirm or refute the PHASE 0 best-case framing? State the dominant fault class by code (most rows in the Class column). One sentence.

---

## PHASE 5 — AMEND

Three structural fixes ordered by severity. Each fix must reference the F-ID, C-ID, and Class code it addresses, and specify the exact change needed — not "add evidence" but what claim, what evidence, or what definition stabilization would close the gap.

1. [P1 fix — F-ID, C-ID, Class: exact repair]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

### Rubric Coverage by Variation (v2 rubric — 5 aspirationals)

| Criterion | R1 V-05 baseline | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----------------|------|------|------|------|------|
| C-04 inference steps traced | base | = | = | = | stronger (3A/3B/3C gating) | stronger (3A/3B/3C) |
| C-06 logical forms named | base | = | = | = | stronger (3A dedicated) | stronger (3A dedicated) |
| C-09 term drift pinpointed | base (C-ID in AMEND only) | = | = | = | stronger (3B requires DRIFT+C-ID at check time) | stronger (3B) |
| C-10 structural weakness | base | = | stronger (SIGNIFICANT/NOTABLE/OBVIOUS scale) | = | = | = |
| C-11 falsification target | base | strongest (3-part template + closure references it) | = | = | = | = |
| C-12 inline reviewer hook | base | = | stronger (depth scale + domain comparison) | = | = (hook in 3C) | = (hook in 3C) |
| C-13 fault pattern closure | base | stronger (closure references full-soundness condition) | stronger (names dominant depth tier) | strongest (taxonomy count = mechanical) | stronger (names dominant class) | strongest (class code counted from register) |
