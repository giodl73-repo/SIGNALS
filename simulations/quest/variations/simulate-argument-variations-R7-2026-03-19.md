R7 variations written. Here's the summary:

---

## simulate-argument R7 — Variation Set

**Gap from R6**: R6 V-05 achieved 15/15 against v6. Against v7 (pool 18), R6 V-05 likely passes C-24/C-25/C-26 already — but each has an untested boundary condition that R7 isolates.

### Variation axes

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **Axis** | C-24 — named form-type examples | C-25 — Phase-4 derivation field (no Logician cross-phase) | C-26 — unconditional adjacency search | C-24 + C-26 | All three |

### Key mechanisms

- **V-01**: ADVOCATE block explicitly names causal inference and argument-from-analogy as form types that must trigger the content-conditional Gen-ID check. Advocate closure attests the scan covered all named form types. Logician closure = specialist-only (no phase extension → fails C-25). CP audit = single-line (fails C-26).
- **V-02**: Boundary test — adds mandatory `Derives from: FORM [C-ID]` derivation reference to every INVALID-FORM row, but **does not** extend Logician closure to phases. Tests whether Phase-4 derivation note alone satisfies C-25. Predicted to FAIL C-25 — the boundary condition requires the Logician's closure to state the prohibition, not merely a Phase-4 instruction.
- **V-03**: Step 2 adjacency search becomes unconditional — runs for every CP step regardless of Step 1. Requires listing the full dependency chain from Phase 2: `CP dependency chain checked: [C-IDs]. Faults in chain: [list / none]`. DISCONFIRMED is never a passive gap.
- **V-04**: V-01 + V-03. Named form examples + unconditional adjacency. No cross-phase Logician extension.
- **V-05**: All three at maximum strength. Named form examples + Logician cross-phase closure with Phase-4 derivation field + unconditional adjacency search with Gen-ID adjacency notes.

### Predicted scores

| Variation | C-24 | C-25 | C-26 | Aspirational | Composite |
|-----------|------|------|------|-------------|-----------|
| V-01 | PASS | FAIL | FAIL | 16/18 | ~99 |
| V-02 | PASS | **FAIL** (boundary test) | FAIL | 16/18 | ~99 |
| V-03 | PASS | FAIL | PASS | 17/18 | ~99 |
| V-04 | PASS | FAIL | PASS | 17/18 | ~99 |
| **V-05** | **PASS** | **PASS** | **PASS** | **18/18** | **100** |

All five predicted golden. V-05 is predicted to be the first variation in any round to score 18/18 aspirational.
ry INVALID-FORM fault row. Logician closure = specialist-only. Predicted FAIL C-25 — the boundary condition explicitly requires the Logician's closure to state the phase prohibition.
- **V-03**: Step 2 adjacency search becomes unconditional — runs for every CP step whether or not Step 1 registered a fault. Format: "CP dependency chain checked: [upstream/downstream C-IDs]. Faults in chain: [F-NN on C-MM / none]." DISCONFIRMED is always documented, never a passive gap.
- **V-04**: V-01 + V-03. Named form-type examples + unconditional adjacency. No cross-phase Logician extension.
- **V-05**: All three at maximum strength. Named form-type examples + Logician cross-phase closure with Phase-4 derivation field + unconditional adjacency search.

### Predicted scores

| Variation | C-24 | C-25 | C-26 | Aspirational | Composite |
|-----------|------|------|------|-------------|-----------|
| V-01 | PASS | FAIL | FAIL | 16/18 | ~99 |
| V-02 | PASS | FAIL | FAIL | 16/18 | ~99 |
| V-03 | PASS | FAIL | PASS | 17/18 | ~99 |
| V-04 | PASS | FAIL | PASS | 17/18 | ~99 |
| V-05 | PASS | PASS | PASS | 18/18 | 100 |

All five predicted golden (composite >= 96). V-05 predicted first variation to score 18/18 aspirational.

---

## V-01 — Axis: C-24 (Explicit Form-Type Trigger Examples)

**Hypothesis**: R6 V-01 passes C-24 by virtue of "form-independent — applies to every inference step" combined with the two-field check. But C-24's boundary case says "causal inference and analogy steps that assume universal mechanism applicability must also trigger the anchor." A variation that names these form types explicitly in the ADVOCATE block instruction and closure is maximally unambiguous. V-01 tests whether explicit naming produces a demonstrably stronger C-24 than the generic "every inference step" language. C-25 uses specialist-only Logician binding (no phase extension) — fails C-25. CP audit uses single-line per-CP-step — fails C-26.

**What changes from R6 V-01**: ADVOCATE block instruction adds two concrete form-type examples with their generalization-trigger pattern. ADVOCATE closure adds an attestation sentence naming causal inference, argument from analogy, and abduction as form types covered by the scan. Everything else from R6 V-01 unchanged.

---

You are running /simulate-argument for: {{topic}}

Four specialists examine every argument. Before any specialist begins, you will commit to: (1) the argument's best case, (2) the null hypothesis, (3) which inference steps are most load-bearing, and (4) which generalizations the paper is expected to make beyond its direct evidence. The Logician names structure. The Advocate commits the author's best reading — scanning every best reading for generalization assumptions and citing Phase 0 Gen-IDs regardless of the Logician's form label, including for causal inference and argument-from-analogy steps. The Reviewer challenges the Advocate's committed readings. The Chair synthesizes verdicts. Phase 4 runs a structured audit: did the priority predictions hold, and were the pre-committed generalizations the ones that failed? The adversary is inertia: the belief that no structural revision is needed.

---

## PHASE 0 — ARGUMENT SETUP

State four things before any specialist begins:

**Best-case argument** (one paragraph):
> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

**Null hypothesis** (one sentence):
> "H0: This argument is structurally sound and requires no revision before submission."

**Critical path** (one to three sentences): Which 2-3 inference steps are most load-bearing? Write TBD; revise after Phase 1.
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
Formal structure: [If/Then/Therefore skeleton in 1-3 lines]
```

> **I, the Logician, commit the above form identifications for all inference steps.** The Advocate, the Empirical Reviewer, and the Committee Chair are bound to these forms. No subsequent specialist may reclassify logical structure. Any conflict between a later specialist's findings and my committed forms is an INVALID-FORM fault candidate.

### 3B-ADVOCATE — THE ADVOCATE (Author's Best Reading)

The Advocate states the minimum assumption that would make each inference valid, given the Logician's committed form. For every best reading, the Advocate scans whether the key assumption claims that a finding, relationship, or mechanism holds beyond the specific cases, population, or conditions studied in this paper. This scan is **form-independent** — it applies to every inference step regardless of whether the Logician labeled it "inductive generalization." This explicitly includes causal inference steps whose key assumption posits that a studied mechanism operates universally or beyond the studied context, and argument-from-analogy steps whose key assumption extends the analogy's scope to domains or populations not studied. Naming a step "causal inference" or "argument from analogy" does not exempt it from this check — the question is whether the key assumption claims broader applicability than the direct evidence supports. If the assumption extends beyond the studied cases, the Advocate cites the matching Phase 0 Gen-ID.

```
ADVOCATE [C-ID]: [claim text]
Role: Advocate
  Best reading: [The inference is valid if we assume: ...]
  Key assumption: [one sentence — the precise unstated premise that would close the logical gap.
                   If no assumption needed: "The stated premises are sufficient given the Logician's form."]
  Generalization assumed: [YES — this best reading assumes that X holds beyond the specific
                            cases, population, or conditions studied / NO — the key assumption
                            is scoped to the studied cases only]
  Gen-ID anchor: [Gen-NN from Phase 0 whose scope covers this assumption /
                  NEW: this generalization was not pre-committed; flag for Gen-registry revision /
                  — (only if Generalization assumed: NO)]
```

> **I, the Advocate, commit the above best readings for all inference steps.** I have checked every best reading for generalization assumptions by scanning the *content* of the assumption — not by inspecting the Logician's form label. I applied this scan to all inference steps including those the Logician labeled as causal inference, argument from analogy, and abduction — not only those labeled "inductive generalization." A step labeled "causal inference" whose best reading assumes the studied mechanism operates universally received the same generalization scan as a step labeled "inductive generalization." All best readings where "Generalization assumed: YES" cite a Phase 0 Gen-ID or are flagged NEW for registry revision. A best reading where I wrote "Generalization assumed: NO" asserts that the key assumption is specific to the studied cases and does not extend beyond them. I have not evaluated whether any assumption holds — that is the Empirical Reviewer's task.

### 3B-CRITIC — THE EMPIRICAL REVIEWER (Evidence Challenge)

The Reviewer tests whether the evidence supports the Advocate's committed key assumptions. The Reviewer also checks term consistency. The Reviewer is bound to the Logician's forms and the Advocate's committed best readings — no new form classifications, no new best readings. Where the Advocate cited a Phase 0 Gen-ID anchor, the Reviewer's assessment is the direct test of that pre-committed generalization — regardless of the Logician's form label.

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

> **I, the Empirical Reviewer, commit the above evidence challenges for all inference steps.** I have tested the Advocate's committed assumptions — not re-evaluated the Logician's forms or generated new best readings. Where the Advocate cited a Phase 0 Gen-ID anchor, my assessment is the direct test of that pre-committed generalization. The Committee Chair now synthesizes all four analyses.

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
- **UNSUPPORTED-GEN**: a generalization extends beyond what the evidence licenses — Gap must cite a Phase 0 Gen-ID from the Advocate's committed anchor
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure violates the form the Logician committed — the Reviewer's evidence challenge reveals the structure, not just the evidence, is the problem

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity | CP? |
|------|------|---------|-------|-----|--------------|----------|-----|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [Advocate required X; Reviewer found only Y — with Gen-ID for UNSUPPORTED-GEN] | [exact claim, evidence, or definition change that closes the fault] | P1/P2/P3 | YES/— |

Severity: P1 = breaks central conclusion / P2 = weakens key section / P3 = precision issue

**Gap field format for UNSUPPORTED-GEN** — cite the Phase 0 Gen-ID from the Advocate's committed Gen-ID anchor:
> `[SIGNIFICANT] The Advocate required that Gen-02 holds: the claim that the learning algorithm generalizes to low-resource languages. The Reviewer found only results on five high-resource languages with >=10M training tokens. A specialist in low-resource NLP would require explicit low-resource benchmarks before accepting the generalization.`

An assertion-only Gap does not pass for UNSUPPORTED-GEN.

**Phase 4 Closing — Null Rejection Test + CP Priority Audit + Generalization Accountability**:

The Chair delivers the final verdict in five steps:

1. Count rows per class code. Name the dominant fault class by code (most rows).
2. Count P1-severity faults. If P1 count >= 1: "H0 is rejected." If P1 count = 0, assess whether P2 faults collectively challenge the central argument.
3. State: "H0 is [rejected / not rejected]. Inertia — submitting without revision — is [not defensible / defensible with minor fixes / defensible]."
4. Critical path priority audit — for each CP-flagged step committed in Phase 0, write one accountability line:
   > "CP audit [C-ID]: Phase 0 predicted this step as load-bearing. Trace outcome: [F-ID at P_-severity, Class: CODE / SOUND — no fault]. Accountability: [CONFIRMED — the pre-committed load-bearing step carries the most severe fault / DISCONFIRMED — step survived; fault [F-ID] on non-CP step [C-ID] was more severe / CONFIRMED-ELSEWHERE — step survived; CP-adjacent step carried P1 fault]."

   Then state: "Structural risk distribution: [one sentence on where actual risk lies vs. where Phase 0 predicted it]."

5. Generalization accountability: for each Gen-ID from Phase 0, state the trace outcome:
   > "Gen-01: [F-ID — UNSUPPORTED-GEN fault registered at P_-severity / No fault — the Advocate's best reading was supported by evidence]."

   Then synthesize: "Generalization accountability verdict: [one sentence — were the pre-committed generalizations the primary structural risk, or did other fault classes dominate?]"

---

## PHASE 5 — AMEND

Three structural fixes ordered P1 -> P2 -> P3. Each references F-ID, C-ID, and Class code.

1. [P1 fix — F-ID, C-ID, Class: exact repair — what claim, evidence, or definition change closes this fault]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-02 — Axis: C-25 Boundary Test (Phase-4 Derivation Field Without Logician Cross-Phase Extension)

**Hypothesis**: C-25 requires the Logician's closure to explicitly state that no subsequent *phase* may reclassify logical structure — and Phase 4 INVALID-FORM to derive from Phase 3A committed form only. Does adding a mandatory derivation field to Phase 4's INVALID-FORM rows satisfy C-25 even if the Logician closure does not extend the prohibition to phases? V-02 tests this boundary: it adds "Derives from: FORM [C-ID] — [committed form]" as a required INVALID-FORM row field, but retains specialist-only Logician binding. Predicted to FAIL C-25 — the rubric boundary condition requires the closure to name the prohibition, not merely a Phase-4 instruction. C-24 passes (form-independent gen scan with named form examples). C-26 fails (single-line CP audit).

**What changes from V-01**: Phase 4 INVALID-FORM class definition gains a derivation requirement. Fault Register template for INVALID-FORM rows adds a mandatory "Derives from" field. Everything else from V-01 unchanged (including form-independent gen scan, specialist-only Logician closure, single-line CP audit).

---

You are running /simulate-argument for: {{topic}}

Four specialists examine every argument. Before any specialist begins, you will commit to: (1) the argument's best case, (2) the null hypothesis, (3) which inference steps are most load-bearing, and (4) which generalizations the paper is expected to make beyond its direct evidence. The Logician names structure — and INVALID-FORM faults in Phase 4 must trace to the Logician's committed form. The Advocate commits the author's best reading, scanning every inference step for generalization assumptions including causal inference and argument-from-analogy steps. The Reviewer challenges the Advocate's committed readings. The Chair synthesizes verdicts. Phase 4 runs a structured audit: did the priority predictions hold, and were the pre-committed generalizations the ones that failed? The adversary is inertia: the belief that no structural revision is needed.

---

## PHASE 0 — ARGUMENT SETUP

State four things before any specialist begins:

**Best-case argument** (one paragraph):
> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

**Null hypothesis** (one sentence):
> "H0: This argument is structurally sound and requires no revision before submission."

**Critical path** (one to three sentences): Which 2-3 inference steps are most load-bearing? Write TBD; revise after Phase 1.
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
Formal structure: [If/Then/Therefore skeleton in 1-3 lines]
```

> **I, the Logician, commit the above form identifications for all inference steps.** The Advocate, the Empirical Reviewer, and the Committee Chair are bound to these forms. No subsequent specialist may reclassify logical structure. Any conflict between a later specialist's findings and my committed forms is an INVALID-FORM fault candidate.

### 3B-ADVOCATE — THE ADVOCATE (Author's Best Reading)

The Advocate states the minimum assumption that would make each inference valid, given the Logician's committed form. For every best reading, the Advocate scans whether the key assumption claims that a finding, relationship, or mechanism holds beyond the specific cases, population, or conditions studied in this paper. This scan is **form-independent** — it applies to every inference step regardless of whether the Logician labeled it "inductive generalization." This explicitly includes causal inference steps whose key assumption posits that a studied mechanism operates universally or beyond the studied context, and argument-from-analogy steps whose key assumption extends the analogy's scope to domains or populations not studied. If the assumption extends beyond the studied cases, the Advocate cites the matching Phase 0 Gen-ID.

```
ADVOCATE [C-ID]: [claim text]
Role: Advocate
  Best reading: [The inference is valid if we assume: ...]
  Key assumption: [one sentence — the precise unstated premise that would close the logical gap.
                   If no assumption needed: "The stated premises are sufficient given the Logician's form."]
  Generalization assumed: [YES — this best reading assumes that X holds beyond the specific
                            cases, population, or conditions studied / NO — the key assumption
                            is scoped to the studied cases only]
  Gen-ID anchor: [Gen-NN from Phase 0 whose scope covers this assumption /
                  NEW: this generalization was not pre-committed; flag for Gen-registry revision /
                  — (only if Generalization assumed: NO)]
```

> **I, the Advocate, commit the above best readings for all inference steps.** I have checked every best reading for generalization assumptions by scanning the *content* of the assumption — not by inspecting the Logician's form label. I applied this scan to all inference steps including those the Logician labeled as causal inference, argument from analogy, and abduction — not only those labeled "inductive generalization." All best readings where "Generalization assumed: YES" cite a Phase 0 Gen-ID or are flagged NEW for registry revision. I have not evaluated whether any assumption holds — that is the Empirical Reviewer's task.

### 3B-CRITIC — THE EMPIRICAL REVIEWER (Evidence Challenge)

The Reviewer tests whether the evidence supports the Advocate's committed key assumptions. The Reviewer also checks term consistency. The Reviewer is bound to the Logician's forms and the Advocate's committed best readings — no new form classifications, no new best readings. Where the Advocate cited a Phase 0 Gen-ID anchor, the Reviewer's assessment is the direct test of that pre-committed generalization regardless of the Logician's form label.

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

> **I, the Empirical Reviewer, commit the above evidence challenges for all inference steps.** I have tested the Advocate's committed assumptions — not re-evaluated the Logician's forms or generated new best readings. Where the Advocate cited a Phase 0 Gen-ID anchor, my assessment is the direct test of that pre-committed generalization. The Committee Chair now synthesizes all four analyses.

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
- **UNSUPPORTED-GEN**: a generalization extends beyond what the evidence licenses — Gap must cite a Phase 0 Gen-ID from the Advocate's committed anchor
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure violates the form the Logician committed — this class derives from the Logician's Phase 3A committed form. Every INVALID-FORM row must include a "Derives from" reference naming the specific FORM block and committed form that grounds the structural fault. INVALID-FORM may not be assigned based on a Phase 4 independent form assessment.

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity | CP? |
|------|------|---------|-------|-----|--------------|----------|-----|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [Advocate required X; Reviewer found only Y] | [exact repair] | P1/P2/P3 | YES/— |

For every INVALID-FORM row, append a derivation line immediately after the row:
> `Derives from: FORM [C-ID] committed in Phase 3A as [Logician's committed form]. The Reviewer's evidence challenge reveals that the argument's structure violates this form.`

Severity: P1 = breaks central conclusion / P2 = weakens key section / P3 = precision issue

**Gap field format for UNSUPPORTED-GEN** — cite the Phase 0 Gen-ID from the Advocate's committed Gen-ID anchor:
> `[SIGNIFICANT] The Advocate required that Gen-02 holds: the claim that the learning algorithm generalizes to low-resource languages. The Reviewer found only results on five high-resource languages with >=10M training tokens. A specialist in low-resource NLP would require explicit low-resource benchmarks before accepting the generalization.`

An assertion-only Gap does not pass for UNSUPPORTED-GEN.

**Phase 4 Closing — Null Rejection Test + CP Priority Audit + Generalization Accountability**:

The Chair delivers the final verdict in five steps:

1. Count rows per class code. Name the dominant fault class by code (most rows).
2. Count P1-severity faults. If P1 count >= 1: "H0 is rejected." If P1 count = 0, assess whether P2 faults collectively challenge the central argument.
3. State: "H0 is [rejected / not rejected]. Inertia — submitting without revision — is [not defensible / defensible with minor fixes / defensible]."
4. Critical path priority audit — for each CP-flagged step committed in Phase 0, write one accountability line:
   > "CP audit [C-ID]: Phase 0 predicted this step as load-bearing. Trace outcome: [F-ID at P_-severity, Class: CODE / SOUND — no fault]. Accountability: [CONFIRMED — the pre-committed load-bearing step carries the most severe fault / DISCONFIRMED — step survived; fault [F-ID] on non-CP step [C-ID] was more severe / CONFIRMED-ELSEWHERE — step survived; CP-adjacent step carried P1 fault]."

   Then state: "Structural risk distribution: [one sentence on where actual risk lies vs. where Phase 0 predicted it]."

5. Generalization accountability: for each Gen-ID from Phase 0, state the trace outcome:
   > "Gen-01: [F-ID — UNSUPPORTED-GEN fault registered at P_-severity / No fault — the Advocate's best reading was supported by evidence]."

   Then synthesize: "Generalization accountability verdict: [one sentence — were the pre-committed generalizations the primary structural risk, or did other fault classes dominate?]"

---

## PHASE 5 — AMEND

Three structural fixes ordered P1 -> P2 -> P3. Each references F-ID, C-ID, and Class code.

1. [P1 fix — F-ID, C-ID, Class: exact repair — what claim, evidence, or definition change closes this fault]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-03 — Axis: C-26 (Unconditional Adjacency Search)

**Hypothesis**: R6 V-03/V-05 enforces a mandatory Step 2 adjacency search that runs "only if Step 1 = SOUND." The conditional gate means that if a model determines Step 1 is borderline — or if the fault at the CP step is at P2/P3 rather than P1 — the Step 2 search may be skipped or treated as unnecessary. C-26 says "DISCONFIRMED is an active documented conclusion, not a passive absence of evidence." The strongest C-26 implementation removes the conditional: Step 2 runs for every CP step, always, and produces a documented dependency chain regardless of Step 1's result. When Step 1 finds a fault, the adjacency search still runs to surface whether the fault also propagated to adjacent steps. DISCONFIRMED is only valid after the dependency chain has been explicitly listed and checked.

**What changes from V-01**: Phase 4 Closing step 4 is restructured. Step 2 adjacency search becomes unconditional — runs for all CP steps regardless of Step 1 result. New format template requires listing all upstream and downstream C-IDs in the dependency chain and their fault status before writing the three-way verdict. Logician closure = specialist-only (no phase extension → fails C-25). ADVOCATE block = V-01's form-independent gen scan with named form examples.

---

You are running /simulate-argument for: {{topic}}

Four specialists examine every argument. Before any specialist begins, you will commit to: (1) the argument's best case, (2) the null hypothesis, (3) which inference steps are most load-bearing, and (4) which generalizations the paper is expected to make beyond its direct evidence. The Logician names structure. The Advocate commits the author's best reading — scanning every inference step for generalization assumptions including causal inference and argument-from-analogy steps. The Reviewer challenges the Advocate's committed readings. The Chair synthesizes verdicts. Phase 4 runs a structured audit with an unconditional adjacency search: for every pre-committed load-bearing step, the full dependency chain is documented before any verdict is written. The adversary is inertia: the belief that no structural revision is needed.

---

## PHASE 0 — ARGUMENT SETUP

State four things before any specialist begins:

**Best-case argument** (one paragraph):
> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

**Null hypothesis** (one sentence):
> "H0: This argument is structurally sound and requires no revision before submission."

**Critical path** (one to three sentences): Which 2-3 inference steps are most load-bearing? Write TBD; revise after Phase 1.
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
Formal structure: [If/Then/Therefore skeleton in 1-3 lines]
```

> **I, the Logician, commit the above form identifications for all inference steps.** The Advocate, the Empirical Reviewer, and the Committee Chair are bound to these forms. No subsequent specialist may reclassify logical structure. Any conflict between a later specialist's findings and my committed forms is an INVALID-FORM fault candidate.

### 3B-ADVOCATE — THE ADVOCATE (Author's Best Reading)

The Advocate states the minimum assumption that would make each inference valid, given the Logician's committed form. For every best reading, the Advocate scans whether the key assumption claims that a finding, relationship, or mechanism holds beyond the specific cases, population, or conditions studied in this paper. This scan is **form-independent** — it applies to every inference step regardless of whether the Logician labeled it "inductive generalization." This explicitly includes causal inference steps whose key assumption posits that a studied mechanism operates universally or beyond the studied context, and argument-from-analogy steps whose key assumption extends the analogy's scope to domains or populations not studied. If the assumption extends beyond the studied cases, the Advocate cites the matching Phase 0 Gen-ID.

```
ADVOCATE [C-ID]: [claim text]
Role: Advocate
  Best reading: [The inference is valid if we assume: ...]
  Key assumption: [one sentence — the precise unstated premise that would close the logical gap.
                   If no assumption needed: "The stated premises are sufficient given the Logician's form."]
  Generalization assumed: [YES — this best reading assumes that X holds beyond the specific
                            cases, population, or conditions studied / NO — the key assumption
                            is scoped to the studied cases only]
  Gen-ID anchor: [Gen-NN from Phase 0 whose scope covers this assumption /
                  NEW: this generalization was not pre-committed; flag for Gen-registry revision /
                  — (only if Generalization assumed: NO)]
```

> **I, the Advocate, commit the above best readings for all inference steps.** I have checked every best reading for generalization assumptions by scanning the *content* of the assumption — not by inspecting the Logician's form label. I applied this scan to all inference steps including those the Logician labeled as causal inference, argument from analogy, and abduction — not only those labeled "inductive generalization." All best readings where "Generalization assumed: YES" cite a Phase 0 Gen-ID or are flagged NEW for registry revision. I have not evaluated whether any assumption holds — that is the Empirical Reviewer's task.

### 3B-CRITIC — THE EMPIRICAL REVIEWER (Evidence Challenge)

The Reviewer tests whether the evidence supports the Advocate's committed key assumptions. The Reviewer also checks term consistency. The Reviewer is bound to the Logician's forms and the Advocate's committed best readings — no new form classifications, no new best readings. Where the Advocate cited a Phase 0 Gen-ID anchor, the Reviewer's assessment is the direct test of that pre-committed generalization regardless of the Logician's form label.

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

> **I, the Empirical Reviewer, commit the above evidence challenges for all inference steps.** I have tested the Advocate's committed assumptions — not re-evaluated the Logician's forms or generated new best readings. Where the Advocate cited a Phase 0 Gen-ID anchor, my assessment is the direct test of that pre-committed generalization. The Committee Chair now synthesizes all four analyses.

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
- **UNSUPPORTED-GEN**: a generalization extends beyond what the evidence licenses — Gap must cite a Phase 0 Gen-ID from the Advocate's committed anchor
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure violates the form the Logician committed — the Reviewer's evidence challenge reveals the structure, not just the evidence, is the problem

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity | CP? |
|------|------|---------|-------|-----|--------------|----------|-----|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [Advocate required X; Reviewer found only Y — with Gen-ID for UNSUPPORTED-GEN] | [exact claim, evidence, or definition change that closes the fault] | P1/P2/P3 | YES/— |

Severity: P1 = breaks central conclusion / P2 = weakens key section / P3 = precision issue

**Gap field format for UNSUPPORTED-GEN** — cite the Phase 0 Gen-ID from the Advocate's committed Gen-ID anchor:
> `[SIGNIFICANT] The Advocate required that Gen-02 holds: the claim that the learning algorithm generalizes to low-resource languages. The Reviewer found only results on five high-resource languages with >=10M training tokens. A specialist in low-resource NLP would require explicit low-resource benchmarks before accepting the generalization.`

An assertion-only Gap does not pass for UNSUPPORTED-GEN.

**Phase 4 Closing — Null Rejection Test + CP Priority Audit + Generalization Accountability**:

The Chair delivers the final verdict in five steps:

1. Count rows per class code. Name the dominant fault class by code (most rows).
2. Count P1-severity faults. If P1 count >= 1: "H0 is rejected." If P1 count = 0, assess whether P2 faults collectively challenge the central argument.
3. State: "H0 is [rejected / not rejected]. Inertia — submitting without revision — is [not defensible / defensible with minor fixes / defensible]."
4. Critical path priority audit — for each CP-flagged step committed in Phase 0, run a three-step accountability check. Step 2 runs unconditionally for every CP step regardless of Step 1 result:

   **Step 1 — Fault check**: "Did a fault register at this CP step? [F-ID at P_-severity, Class: CODE / SOUND — no fault registered]"

   **Step 2 — CP-adjacency search** (unconditional — runs for every CP step): "CP dependency chain checked: [list every C-ID that [C-ID] depends on, and every C-ID that depends on [C-ID], drawn from the Phase 2 Claim Map]. Faults in chain: [F-NN on C-MM: one-sentence description, noting any Gen-ID anchor from the Advocate's committed reading / none — each step in the dependency chain checked and found SOUND]."

   **Step 3 — Three-way verdict**:
   - CONFIRMED: Step 1 found a fault (fault registered on this CP step)
   - CONFIRMED-ELSEWHERE: Step 1 SOUND and Step 2 found fault(s) on adjacent step(s)
   - DISCONFIRMED: Step 1 SOUND and Step 2 found no faults in the dependency chain

   Write as: "CP audit [C-ID]: [Step 1 result]. [Step 2 dependency chain and search result]. Verdict: [CONFIRMED / CONFIRMED-ELSEWHERE — F-NN on adjacent C-MM / DISCONFIRMED — dependency chain checked, no faults found]."

   DISCONFIRMED requires a completed Step 2 with the dependency chain listed. A verdict of DISCONFIRMED written without a documented dependency chain search does not pass C-26.

   After all CP steps: "Structural risk distribution: [one sentence on where actual risk lies vs. Phase 0 prediction]."

5. Generalization accountability: for each Gen-ID from Phase 0, state the trace outcome:
   > "Gen-01: [F-ID — UNSUPPORTED-GEN fault registered at P_-severity / No fault — the Advocate's best reading was supported by evidence]."

   Then synthesize: "Generalization accountability verdict: [one sentence — were the pre-committed generalizations the primary structural risk, or did other fault classes dominate?]"

---

## PHASE 5 — AMEND

Three structural fixes ordered P1 -> P2 -> P3. Each references F-ID, C-ID, and Class code.

1. [P1 fix — F-ID, C-ID, Class: exact repair — what claim, evidence, or definition change closes this fault]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-04 — Combined: C-24 + C-26 (Named Form Examples + Unconditional Adjacency Search)

**Hypothesis**: V-01 tests whether explicit form-type naming makes C-24 maximally unambiguous. V-03 tests whether unconditional Step 2 documentation produces a structurally stronger C-26 than the conditional procedure. Combining them tests whether the two axes interact: when the Advocate's gen scan names causal inference and analogy as explicit trigger types (V-01), and the CP adjacency search always documents the full dependency chain (V-03), the CONFIRMED-ELSEWHERE verdict can specifically report "UNSUPPORTED-GEN (Gen-02, causal inference step C-07) found in dependency chain" — identifying not just that a fault is adjacent but that the adjacent fault traces to a form-independent Gen-ID anchor. The C-25 axis is excluded (specialist-only Logician closure) to isolate the combined C-24/C-26 interaction.

**What changes from V-03**: ADVOCATE block instruction gains the explicit form-type examples from V-01. ADVOCATE closure gains the form-type attestation from V-01. Step 2 unconditional adjacency search from V-03 retained and enhanced: when a Gen-ID anchor is present on an adjacent fault, the Step 2 entry notes it. Logician closure = specialist-only.

---

You are running /simulate-argument for: {{topic}}

Four specialists examine every argument. Before any specialist begins, you will commit to: (1) the argument's best case, (2) the null hypothesis, (3) which inference steps are most load-bearing, and (4) which generalizations the paper is expected to make beyond its direct evidence. The Logician names structure. The Advocate commits the author's best reading — scanning every inference step for generalization assumptions including causal inference and argument-from-analogy steps, citing Phase 0 Gen-IDs regardless of form label. The Reviewer challenges the Advocate's committed readings. The Chair synthesizes verdicts. Phase 4 runs a structured audit with an unconditional adjacency search: every CP step's full dependency chain is documented before the verdict is written, and adjacent UNSUPPORTED-GEN faults carry their Gen-ID anchors. The adversary is inertia: the belief that no structural revision is needed.

---

## PHASE 0 — ARGUMENT SETUP

State four things before any specialist begins:

**Best-case argument** (one paragraph):
> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

**Null hypothesis** (one sentence):
> "H0: This argument is structurally sound and requires no revision before submission."

**Critical path** (one to three sentences): Which 2-3 inference steps are most load-bearing? Write TBD; revise after Phase 1.
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
Formal structure: [If/Then/Therefore skeleton in 1-3 lines]
```

> **I, the Logician, commit the above form identifications for all inference steps.** The Advocate, the Empirical Reviewer, and the Committee Chair are bound to these forms. No subsequent specialist may reclassify logical structure. Any conflict between a later specialist's findings and my committed forms is an INVALID-FORM fault candidate.

### 3B-ADVOCATE — THE ADVOCATE (Author's Best Reading)

The Advocate states the minimum assumption that would make each inference valid, given the Logician's committed form. For every best reading, the Advocate scans whether the key assumption claims that a finding, relationship, or mechanism holds beyond the specific cases, population, or conditions studied in this paper. This scan is **form-independent** — it applies to every inference step regardless of whether the Logician labeled it "inductive generalization." This explicitly includes causal inference steps whose key assumption posits that a studied mechanism operates universally or beyond the studied context, and argument-from-analogy steps whose key assumption extends the analogy's scope to domains or populations not studied. Naming a step "causal inference" or "argument from analogy" does not exempt it from this check — the question is whether the key assumption claims broader applicability than the direct evidence supports. If the assumption extends beyond the studied cases, the Advocate cites the matching Phase 0 Gen-ID.

```
ADVOCATE [C-ID]: [claim text]
Role: Advocate
  Best reading: [The inference is valid if we assume: ...]
  Key assumption: [one sentence — the precise unstated premise that would close the logical gap.
                   If no assumption needed: "The stated premises are sufficient given the Logician's form."]
  Generalization assumed: [YES — this best reading assumes that X holds beyond the specific
                            cases, population, or conditions studied / NO — the key assumption
                            is scoped to the studied cases only]
  Gen-ID anchor: [Gen-NN from Phase 0 whose scope covers this assumption /
                  NEW: this generalization was not pre-committed; flag for Gen-registry revision /
                  — (only if Generalization assumed: NO)]
```

> **I, the Advocate, commit the above best readings for all inference steps.** I have checked every best reading for generalization assumptions by scanning the *content* of the assumption — not by inspecting the Logician's form label. I applied this scan to all inference steps including those the Logician labeled as causal inference, argument from analogy, and abduction — not only those labeled "inductive generalization." A step labeled "causal inference" whose best reading assumes the studied mechanism operates universally received the same generalization scan as a step labeled "inductive generalization." All best readings where "Generalization assumed: YES" cite a Phase 0 Gen-ID or are flagged NEW for registry revision. I have not evaluated whether any assumption holds — that is the Empirical Reviewer's task.

### 3B-CRITIC — THE EMPIRICAL REVIEWER (Evidence Challenge)

The Reviewer tests whether the evidence supports the Advocate's committed key assumptions. The Reviewer also checks term consistency. The Reviewer is bound to the Logician's forms and the Advocate's committed best readings — no new form classifications, no new best readings. Where the Advocate cited a Phase 0 Gen-ID anchor, the Reviewer's assessment is the direct test of that pre-committed generalization regardless of the Logician's form label.

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

> **I, the Empirical Reviewer, commit the above evidence challenges for all inference steps.** I have tested the Advocate's committed assumptions — not re-evaluated the Logician's forms or generated new best readings. Where the Advocate cited a Phase 0 Gen-ID anchor, my assessment is the direct test of that pre-committed generalization. The Committee Chair now synthesizes all four analyses.

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
- **UNSUPPORTED-GEN**: a generalization extends beyond what the evidence licenses — Gap must cite a Phase 0 Gen-ID from the Advocate's committed anchor
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure violates the form the Logician committed — the Reviewer's evidence challenge reveals the structure, not just the evidence, is the problem

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity | CP? |
|------|------|---------|-------|-----|--------------|----------|-----|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [Advocate required X; Reviewer found only Y — with Gen-ID for UNSUPPORTED-GEN] | [exact claim, evidence, or definition change that closes the fault] | P1/P2/P3 | YES/— |

Severity: P1 = breaks central conclusion / P2 = weakens key section / P3 = precision issue

**Gap field format for UNSUPPORTED-GEN** — cite the Phase 0 Gen-ID from the Advocate's committed Gen-ID anchor:
> `[SIGNIFICANT] The Advocate required that Gen-02 holds: the claim that the learning algorithm generalizes to low-resource languages. The Reviewer found only results on five high-resource languages with >=10M training tokens. A specialist in low-resource NLP would require explicit low-resource benchmarks before accepting the generalization.`

An assertion-only Gap does not pass for UNSUPPORTED-GEN.

**Phase 4 Closing — Null Rejection Test + CP Priority Audit + Generalization Accountability**:

The Chair delivers the final verdict in five steps:

1. Count rows per class code. Name the dominant fault class by code (most rows).
2. Count P1-severity faults. If P1 count >= 1: "H0 is rejected." If P1 count = 0, assess whether P2 faults collectively challenge the central argument.
3. State: "H0 is [rejected / not rejected]. Inertia — submitting without revision — is [not defensible / defensible with minor fixes / defensible]."
4. Critical path priority audit — for each CP-flagged step committed in Phase 0, run a three-step accountability check. Step 2 runs unconditionally for every CP step:

   **Step 1 — Fault check**: "Did a fault register at this CP step? [F-ID at P_-severity, Class: CODE / SOUND — no fault registered]"

   **Step 2 — CP-adjacency search** (unconditional): "CP dependency chain checked: [list every C-ID that [C-ID] depends on, and every C-ID that depends on [C-ID], drawn from the Phase 2 Claim Map]. Faults in chain: [F-NN on C-MM: one-sentence description; if UNSUPPORTED-GEN, name the Gen-ID anchor from the Advocate's committed Phase 3 reading / none — each step in the dependency chain is SOUND]."

   **Step 3 — Three-way verdict**:
   - CONFIRMED: Step 1 found a fault (fault registered on this CP step)
   - CONFIRMED-ELSEWHERE: Step 1 SOUND and Step 2 found fault(s) on adjacent step(s)
   - DISCONFIRMED: Step 1 SOUND and Step 2 found no faults in the dependency chain

   Write as: "CP audit [C-ID]: [Step 1 result]. [Step 2 dependency chain and search result]. Verdict: [CONFIRMED / CONFIRMED-ELSEWHERE — F-NN on adjacent C-MM / DISCONFIRMED — dependency chain checked, no faults found]."

   DISCONFIRMED requires Step 2 dependency chain to be listed. A verdict of DISCONFIRMED written without a documented dependency chain does not pass C-26.

   After all CP steps: "Structural risk distribution: [one sentence on where actual risk lies vs. Phase 0 prediction]."

5. Generalization accountability: for each Gen-ID from Phase 0, state the trace outcome:
   > "Gen-01: [F-ID — UNSUPPORTED-GEN fault registered at P_-severity / No fault — the Advocate's best reading was supported by evidence]."

   Then synthesize: "Generalization accountability verdict: [one sentence — were the pre-committed generalizations the primary structural risk, or did other fault classes dominate?]"

---

## PHASE 5 — AMEND

Three structural fixes ordered P1 -> P2 -> P3. Each references F-ID, C-ID, and Class code.

1. [P1 fix — F-ID, C-ID, Class: exact repair — what claim, evidence, or definition change closes this fault]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

## V-05 — Combined: All Three (C-24 + C-25 + C-26) — Strongest v7 Implementations

**Hypothesis**: V-01 adds named form-type examples to C-24. A full C-25 implementation requires both the Logician closure cross-phase extension ("no subsequent specialist and no subsequent phase") AND the Phase-4 INVALID-FORM derivation field (making the derivation chain structurally mandatory at the row level, not merely instructed). V-03 makes Step 2 unconditional. Combining all three tests whether the mechanisms reinforce across the full analysis: (1) Advocate's form-independent gen scan names the specific form types that must trigger — closing the gap between "every inference step" (generic) and "including causal inference steps that assume universal mechanism applicability" (explicit); (2) Logician closure extends immutability to phases AND Phase 4 INVALID-FORM row carries a mandatory derivation reference — a double-lock on structural provenance; (3) Unconditional Step 2 means the dependency chain is always documented, so CONFIRMED-ELSEWHERE verdicts carry Gen-ID anchors from Phase 3 Advocate commitments when adjacent faults are UNSUPPORTED-GEN. The three mechanisms span Phase 0 through Phase 5 with no bypass paths. Predicted: 18/18 aspirational.

**What changes from R6 V-05**: ADVOCATE block instruction adds explicit form-type examples (V-01). ADVOCATE closure adds form-type attestation (V-01). Logician closure retains cross-phase extension from R6 V-05 and adds "including INVALID-FORM fault classification in Phase 4" to the explicit scope. Phase 4 INVALID-FORM class definition gains mandatory derivation row requirement (V-02). Phase 4 Closing step 4 restructured as unconditional three-step check (V-03 upgrade). Everything else from R6 V-05 unchanged.

---

You are running /simulate-argument for: {{topic}}

Four specialists examine every argument. Before any specialist begins, you will commit to: (1) the argument's best case, (2) the null hypothesis, (3) which inference steps are most load-bearing, and (4) which generalizations the paper is expected to make beyond its direct evidence. The Logician names structure — and the Logician's form identifications are immutable across Phase 3, Phase 4, and Phase 5, including INVALID-FORM fault classification. The Advocate commits the author's best reading — scanning every inference step for generalization assumptions including causal inference and argument-from-analogy steps, citing Phase 0 Gen-IDs regardless of form label. The Reviewer challenges the Advocate's committed readings. The Chair synthesizes verdicts. Phase 4 runs a structured audit with an unconditional adjacency search: every CP step's full dependency chain is documented and checked before any verdict is written, and adjacent UNSUPPORTED-GEN faults carry their Gen-ID anchors. The adversary is inertia: the belief that no structural revision is needed.

---

## PHASE 0 — ARGUMENT SETUP

State four things before any specialist begins:

**Best-case argument** (one paragraph):
> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

**Null hypothesis** (one sentence):
> "H0: This argument is structurally sound and requires no revision before submission."

**Critical path** (one to three sentences): Which 2-3 inference steps are most load-bearing? Write TBD; revise after Phase 1.
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
Formal structure: [If/Then/Therefore skeleton in 1-3 lines]
```

> **I, the Logician, commit the above form identifications for all inference steps. These form identifications are immutable across the entire analysis — Phase 3, Phase 4, and Phase 5, including INVALID-FORM fault classification in Phase 4.** The Advocate, the Empirical Reviewer, and the Committee Chair are bound to these forms. No subsequent specialist and no subsequent phase may reclassify logical structure committed here. In Phase 4, INVALID-FORM is the only fault class available when the source of a fault is structural rather than evidential — no specialist and no phase may re-derive the form. Phase 4 INVALID-FORM rows must carry a derivation reference to the specific FORM block committed here. Phase 5 amendments may not propose form reclassification. Any conflict between a later specialist's findings and my committed forms is an INVALID-FORM fault candidate, not a correction of my classification.

### 3B-ADVOCATE — THE ADVOCATE (Author's Best Reading)

The Advocate states the minimum assumption that would make each inference valid, given the Logician's committed form. For every best reading, the Advocate scans whether the key assumption claims that a finding, relationship, or mechanism holds beyond the specific cases, population, or conditions studied in this paper. This scan is **form-independent** — it applies to every inference step regardless of whether the Logician labeled it "inductive generalization." This explicitly includes causal inference steps whose key assumption posits that a studied mechanism operates universally or beyond the studied context, and argument-from-analogy steps whose key assumption extends the analogy's scope to domains or populations not studied. Naming a step "causal inference" or "argument from analogy" does not exempt it from this check — the question is whether the key assumption claims broader applicability than the direct evidence supports. If the assumption extends beyond the studied cases, the Advocate cites the matching Phase 0 Gen-ID.

```
ADVOCATE [C-ID]: [claim text]
Role: Advocate
  Best reading: [The inference is valid if we assume: ...]
  Key assumption: [one sentence — the precise unstated premise that would close the logical gap.
                   If no assumption needed: "The stated premises are sufficient given the Logician's form."]
  Generalization assumed: [YES — this best reading assumes that X holds beyond the specific
                            cases, population, or conditions studied / NO — the key assumption
                            is scoped to the studied cases only]
  Gen-ID anchor: [Gen-NN from Phase 0 whose scope covers this assumption /
                  NEW: this generalization was not pre-committed; flag for Gen-registry revision /
                  — (only if Generalization assumed: NO)]
```

> **I, the Advocate, commit the above best readings for all inference steps.** I have checked every best reading for generalization assumptions by scanning the *content* of the assumption — not by inspecting the Logician's form label. I applied this scan to all inference steps including those the Logician labeled as causal inference, argument from analogy, and abduction — not only those labeled "inductive generalization." A step labeled "causal inference" whose best reading assumes the studied mechanism operates universally received the same generalization scan as a step labeled "inductive generalization." All best readings where "Generalization assumed: YES" cite a Phase 0 Gen-ID or are flagged NEW for registry revision. A best reading where I wrote "Generalization assumed: NO" asserts that the key assumption is specific to the studied cases and does not extend beyond them. I have not evaluated whether any assumption holds — that is the Empirical Reviewer's task.

### 3B-CRITIC — THE EMPIRICAL REVIEWER (Evidence Challenge)

The Reviewer tests whether the evidence supports the Advocate's committed key assumptions. The Reviewer also checks term consistency. The Reviewer is bound to the Logician's forms and the Advocate's committed best readings — no new form classifications, no new best readings. Where the Advocate cited a Phase 0 Gen-ID anchor, the Reviewer's assessment is the direct test of that pre-committed generalization — regardless of the Logician's form label.

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

> **I, the Empirical Reviewer, commit the above evidence challenges for all inference steps.** I have tested the Advocate's committed assumptions — not re-evaluated the Logician's forms or generated new best readings. Where the Advocate cited a Phase 0 Gen-ID anchor, my assessment is the direct test of that pre-committed generalization. The Committee Chair now synthesizes all four analyses.

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
- **UNSUPPORTED-GEN**: a generalization extends beyond what the evidence licenses — Gap must cite a Phase 0 Gen-ID from the Advocate's committed anchor
- **CIRCULAR-DEP**: the conclusion appears as an implicit premise in its own support chain
- **INVALID-FORM**: the logical structure violates the form the Logician committed — this class derives from the Logician's Phase 3A committed form; it may not be assigned based on a Phase 4 independent form assessment. Every INVALID-FORM row must include a derivation reference immediately after the row citing the specific FORM block and committed form from Phase 3A.

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity | CP? |
|------|------|---------|-------|-----|--------------|----------|-----|
| F-01 | | BROKEN | [DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM] | [DEPTH-TIER] [Advocate required X; Reviewer found only Y — with Gen-ID for UNSUPPORTED-GEN] | [exact claim, evidence, or definition change that closes the fault] | P1/P2/P3 | YES/— |

For every INVALID-FORM row, add a derivation line immediately after:
> `Derives from: FORM [C-ID] committed in Phase 3A as [Logician's committed form]. The Reviewer's evidence challenge reveals a structural violation of this form.`

Severity: P1 = breaks central conclusion / P2 = weakens key section / P3 = precision issue

**Gap field format for UNSUPPORTED-GEN** — cite the Phase 0 Gen-ID from the Advocate's committed Gen-ID anchor:
> `[SIGNIFICANT] The Advocate required that Gen-02 holds: the claim that the learning algorithm generalizes to low-resource languages. The Reviewer found only results on five high-resource languages with >=10M training tokens. A specialist in low-resource NLP would require explicit low-resource benchmarks before accepting the generalization.`

An assertion-only Gap does not pass for UNSUPPORTED-GEN.

**Phase 4 Closing — Null Rejection Test + CP Priority Audit + Generalization Accountability**:

The Chair delivers the final verdict in five steps:

1. Count rows per class code. Name the dominant fault class by code (most rows).
2. Count P1-severity faults. If P1 count >= 1: "H0 is rejected." If P1 count = 0, assess whether P2 faults collectively challenge the central argument.
3. State: "H0 is [rejected / not rejected]. Inertia — submitting without revision — is [not defensible / defensible with minor fixes / defensible]."
4. Critical path priority audit — for each CP-flagged step committed in Phase 0, run a three-step accountability check. Step 2 runs unconditionally for every CP step regardless of Step 1 result:

   **Step 1 — Fault check**: "Did a fault register at this CP step? [F-ID at P_-severity, Class: CODE / SOUND — no fault registered]"

   **Step 2 — CP-adjacency search** (unconditional — runs for every CP step): "CP dependency chain checked: [list every C-ID that [C-ID] depends on, and every C-ID that depends on [C-ID], drawn from the Phase 2 Claim Map]. Faults in chain: [F-NN on C-MM: one-sentence description; if UNSUPPORTED-GEN, name the Gen-ID anchor from the Advocate's committed Phase 3 reading / none — each step in the dependency chain checked and found SOUND]."

   **Step 3 — Three-way verdict**:
   - CONFIRMED: Step 1 found a fault (fault registered on this CP step)
   - CONFIRMED-ELSEWHERE: Step 1 SOUND and Step 2 found fault(s) on adjacent step(s)
   - DISCONFIRMED: Step 1 SOUND and Step 2 found no faults in the dependency chain

   Write as: "CP audit [C-ID]: [Step 1 result]. [Step 2 dependency chain and search result]. Verdict: [CONFIRMED / CONFIRMED-ELSEWHERE — F-NN on adjacent C-MM, noting Gen-ID if UNSUPPORTED-GEN / DISCONFIRMED — dependency chain checked, no faults found]."

   DISCONFIRMED requires a documented Step 2 dependency chain. A verdict of DISCONFIRMED written without listing the dependency chain does not pass C-26.

   After all CP steps: "Structural risk distribution: [one sentence on where actual risk lies vs. Phase 0 prediction]."

5. Generalization accountability: for each Gen-ID from Phase 0, state the trace outcome:
   > "Gen-01: [F-ID — UNSUPPORTED-GEN fault registered at P_-severity / No fault — the Advocate's best reading was supported by evidence]."

   Then synthesize: "Generalization accountability verdict: [one sentence — were the pre-committed generalizations the primary structural risk, or did other fault classes dominate?]"

---

## PHASE 5 — AMEND

Three structural fixes ordered P1 -> P2 -> P3. Each references F-ID, C-ID, and Class code.

1. [P1 fix — F-ID, C-ID, Class: exact repair — what claim, evidence, or definition change closes this fault]
2. [P2 fix — F-ID, C-ID, Class: exact repair]
3. [P3 fix — F-ID, C-ID, Class: if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]

---

### Predicted v7 scores by variation

| Variation | C-24 | C-25 | C-26 | Predicted aspirational_pass | Composite |
|-----------|------|------|------|-----------------------------|-----------|
| V-01 (C-24 explicit form examples) | **PASS** | FAIL | FAIL | 16/18 | ~99 |
| V-02 (C-25 Phase-4 derivation only) | **PASS** | **FAIL** | FAIL | 16/18 | ~99 |
| V-03 (C-26 unconditional search) | **PASS** | FAIL | **PASS** | 17/18 | ~99 |
| V-04 (C-24 + C-26) | **PASS** | FAIL | **PASS** | 17/18 | ~99 |
| V-05 (all three) | **PASS** | **PASS** | **PASS** | **18/18** | **100** |

All five predicted golden (composite >= 96). V-05 predicted first variation in any round to score 18/18 aspirational.

**V-02 boundary test significance**: If V-02 actually passes C-25 despite lacking the Logician cross-phase extension, then C-25's pass condition is satisfied by the Phase-4 derivation row alone. If V-02 fails C-25 as predicted, then C-25 requires both the Logician closure extension and the Phase-4 note — which is what V-05 implements.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["named-form-type-trigger", "phase4-invalid-form-derivation-chain", "unconditional-adjacency-documentation"]}
```
