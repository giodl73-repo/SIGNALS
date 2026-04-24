Written to `simulations/quest/variations/simulate-derivation-variations-R1-2026-03-20.md`.

---

## 5 Variations — simulate-derivation R1

| ID | Axis | Hypothesis |
|----|------|-----------|
| **V-01** | Output format | Compress per-step verification blocks into a **single master table** (one row, all checks as columns) — same C-02/C-03 coverage, lower token overhead, more scannable |
| **V-02** | Role sequence | **Type-classifier pass before building the map** — label every step APPROX/EXACT/etc. before filling in expressions, so APPROX detection is primed before verification begins (raises C-03 compliance) |
| **V-03** | Phrasing register | **First-person imperative throughout** ("Do X now. Then do Y.") instead of descriptive phase headers — LLM treats commands more literally, produces fewer skipped sections |
| **V-04** | Lifecycle emphasis | **Collapse Phase 1 to one paragraph; double instruction space on Phase 3** with explicit sub-check structure — concentrates token budget on the highest-weight criteria (C-02, C-03) |
| **V-05** | Combined: format + sequence | Master-table format (V-01) + type-classifier-first sequence (V-02) — tests whether the two axes stack positively or interfere |

### Key structural decisions

- **V-01** is the purest test of whether table-per-row is equivalent to block-per-step for APPROX compliance. The APPROX check columns are N/A for non-APPROX rows, which is the critical slot — if scorers accept N/A as a valid C-03 pass, V-01 is strictly better. If they require prose reasoning, it will underperform.
- **V-02** is the sequencing gamble: the classifier list is a "warm-up output" that makes approximations explicit before the model ever writes a verification block. Risk is that it adds a phase without improving correctness if the model ignores the classifier in Phase 4.
- **V-03** targets the most common failure mode of prompt non-compliance (skipped sections). The imperative phrasing makes Steps 1-6 feel like a checklist rather than documentation.
- **V-04** trades acquisition verbosity for verification depth. The APPROX check sub-block in Phase 2 is the most detailed of any variation — four explicit lines, two for naming the approximation and two for the paper's statements about it.
- **V-05** is the combination bet: if V-01 and V-02 each improve different criteria independently, V-05 should score highest. If they conflict (e.g., the classifier step adds a phase that a compressed-table format doesn't handle well), V-05 will reveal the interference.
| Operation applied | Resulting expression | Justification | Type |
|------|-------------------|------------------|---------------------|---------------|------|
| S-01 | ... | ... | ... | ... | EXACT / APPROX / DEFINITION / PHYSICAL |

Types:
- **EXACT**: exact algebraic identity, mechanically verifiable
- **APPROX**: approximation made — Taylor, small-angle, mean-field, etc.
- **DEFINITION**: symbol introduction or substitution
- **PHYSICAL**: physical assumption encoded algebraically

---

## PHASE 3 — MASTER VERIFICATION TABLE

One row per S-ID. All verification checks as columns. Do not skip any S-ID.

| S-ID | Alg. correct? | Dimensional? | Sign OK? | APPROX: stated? | APPROX: validity stated? | Verdict |
|------|--------------|-------------|---------|----------------|--------------------------|---------|
| S-01 | YES / NO / COND | YES / NO / N/A | YES / NO | YES / NO / N/A | YES / NO / N/A | SOUND / WEAK / BROKEN |

Column definitions:
- **Alg. correct?** — does the algebra hold? COND means only under a stated condition.
- **Dimensional?** — do units on LHS equal units on RHS? N/A if dimensionless or pure algebraic.
- **Sign OK?** — does the sign of each term make physical/mathematical sense?
- **APPROX: stated?** — for APPROX-typed steps only: does the paper name the approximation? N/A for non-APPROX.
- **APPROX: validity stated?** — for APPROX-typed steps only: does the paper give the validity condition? N/A for non-APPROX.
- **Verdict** — SOUND (all checks pass), WEAK (minor issue), BROKEN (algebraically wrong).

After the table, add a brief note for every WEAK or BROKEN row explaining the specific failure.

If the derivation contains zero APPROX steps, add a line: "No APPROX steps found — C-03 auto-passes."

---

## PHASE 4 — DERIVATION FAULT REGISTER

| F-ID | S-ID | Verdict | Type | Description | Fix |
|------|------|---------|------|-------------|-----|

Severity per row:
- **P1**: algebraically wrong — stated result does not follow from stated start
- **P2**: approximation made but not stated — result valid only under unstated conditions
- **P3**: correct but unclear — notational ambiguity or missing intermediate step

Every WEAK or BROKEN row from the master table must have an entry here.
If no faults: state "No faults found" with a one-sentence justification.

---

## PHASE 5 — GLOBAL VERDICT AND AMEND

**Global verdict**: SOUND / CONDITIONALLY SOUND / BROKEN
- SOUND: all steps verified, derivation endpoint follows from starting point
- CONDITIONALLY SOUND: all steps verified under the approximations stated
- BROKEN: at least one P1 error blocks the conclusion

**Amend** — three targeted fixes, each referencing an F-ID:
1. [F-ID]: [specific fix — exact correction, not generic advice]
2. [F-ID]: [specific fix]
3. [F-ID]: [specific fix]

If fewer than three faults exist, the remaining AMEND items may address P3 clarity improvements from steps without a fault register entry.

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]

---

## V-02 — Role Sequence: Type-Classifier Pass First

**Axis**: Role sequence
**Hypothesis**: Running a dedicated type-classification pass before populating the derivation map primes attention on approximation detection. Steps are labeled APPROX before verification begins, so the verification phase is never surprised by a late-discovered approximation, raising C-03 compliance.

---

You are running /simulate-derivation for: {{topic}}

Trace a mathematical derivation step by step — not the logical argument, but the algebraic manipulation. Every line of the derivation is a claim that the left side equals the right side after some operation. This skill catches sign errors, missing terms, unjustified approximations, and dimensional inconsistencies that simulate-argument misses.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read: simulate-argument, discover-limiting-cases if available.
Extract: the derivation to trace, the stated starting point, the stated endpoint, and any approximations the paper explicitly acknowledges.

---

## PHASE 2 — TYPE CLASSIFICATION PASS (run before building the map)

Before tracing any algebra, classify every derivation step by type. Read through the derivation once and produce a classification list:

```
S-01: EXACT    [brief reason]
S-02: APPROX   [what is approximated]
S-03: DEFINITION [symbol introduced]
S-04: PHYSICAL [assumption encoded]
...
```

Types:
- **EXACT**: exact algebraic identity — can be verified mechanically
- **APPROX**: approximation made (Taylor, small-angle, mean-field, limiting case, etc.)
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically (e.g., "at equilibrium, dR/dt = 0")

For every step you classify APPROX, note immediately: (a) what is being approximated, (b) the validity condition you expect to need, (c) whether the paper names this approximation. This list feeds directly into Phase 4.

---

## PHASE 3 — DERIVATION MAP

Using your type classification from Phase 2, build the full map:

| S-ID | Starting expression | Operation applied | Resulting expression | Justification | Type |
|------|-------------------|------------------|---------------------|---------------|------|
| S-01 | [exact LHS] | [operation] | [exact RHS] | [algebraic identity, substitution, approximation, definition] | [type from Phase 2] |

Types must match your Phase 2 classification exactly. If you find a mismatch while filling in expressions, update the classification and note the revision.

---

## PHASE 4 — STEP-BY-STEP VERIFICATION

For each step S-ID, verify in this block format:

```
S-[NN]: [description]
From: [expression A]
Operation: [what is done]
To: [expression B]
Verification:
  - Algebraically correct? YES / NO / CONDITIONAL (state condition)
  - Dimensional consistency: units LHS = units RHS? YES / NO / NOT APPLICABLE
  - Sign check: does sign of each term make physical/mathematical sense? YES / NO
  - APPROX check (if APPROX): approximation named in paper? YES / NO
  - APPROX check (if APPROX): validity condition given in paper? YES / NO
Verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN: [exact description of failure]
```

For non-APPROX steps, omit the APPROX check lines. For APPROX steps, both APPROX check lines are required.

---

## PHASE 5 — DERIVATION FAULT REGISTER

| F-ID | S-ID | Verdict | Type | Description | Fix |
|------|------|---------|------|-------------|-----|
| F-01 | S-03 | BROKEN | Sign error | RHS should be −β·τ² not +β·τ² — damping must oppose growth | Change sign; verify it recovers correct equilibrium |
| F-02 | S-07 | WEAK | Unstated approx | Mean-field approximation taken without stating validity conditions | Add "assuming weak spatial correlations" or cite mean-field condition |

Severity:
- **P1**: algebraically wrong — stated result does not follow from stated start
- **P2**: approximation made but not stated — result valid only under unstated conditions
- **P3**: correct but unclear — notational ambiguity or missing intermediate step

Every WEAK or BROKEN verdict from Phase 4 must have an entry here.
If no faults: state "No faults found" and give a one-sentence justification.

---

## PHASE 6 — GLOBAL VERDICT AND AMEND

**Global verdict** (in a summary section, not buried in a step block):
- SOUND: all steps verified, endpoint follows from starting point
- CONDITIONALLY SOUND: all steps verified under stated approximations
- BROKEN: at least one P1 error blocks the conclusion

**Amend** — exactly three targeted fixes, each citing an F-ID:
1. [F-ID]: [specific correction — exact enough to act on]
2. [F-ID]: [specific correction]
3. [F-ID]: [specific correction]

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]

---

## V-03 — Phrasing Register: First-Person Imperative

**Axis**: Phrasing register
**Hypothesis**: Rewriting all instructions as first-person imperatives ("Do X. Then do Y.") rather than passive/descriptive headers forces the LLM to treat each instruction as a command rather than a description of what output might look like, producing more consistent format adherence and fewer skipped sections.

---

You are running /simulate-derivation for: {{topic}}

Your job: trace a mathematical derivation step by step. Not the argument — the algebra. Every line claims LHS equals RHS after some operation. Catch sign errors, missing terms, unjustified approximations, dimensional inconsistencies. Do not summarize the argument. Do not paraphrase conclusions. Trace the algebra.

---

**Step 1. Acquire the source.**

Read the paper or draft artifact for {{topic}}. If simulate-argument or discover-limiting-cases artifacts exist for this topic, read those too. From the source, extract:
- The exact starting expression (the thing being derived from)
- The exact endpoint (the thing being proved or derived)
- Every approximation the paper explicitly names

Write these down before proceeding.

---

**Step 2. Build the derivation map.**

For every non-trivial step in the derivation, add one row to this table:

| S-ID | Starting expression | Operation applied | Resulting expression | Justification | Type |
|------|-------------------|------------------|---------------------|---------------|------|

Assign each step a type:
- **EXACT** — exact algebraic identity, mechanically verifiable
- **APPROX** — an approximation is made; validity conditions required
- **DEFINITION** — a symbol is introduced or substituted
- **PHYSICAL** — a physical assumption is encoded algebraically

Include every non-trivial step. Minimum 3 rows (or all steps if fewer than 3 exist).

---

**Step 3. Verify each step.**

For every S-ID in your map, produce a verification block. Do not skip any S-ID.

```
S-[NN]: [description]
From: [expression A]
Operation: [what is done]
To: [expression B]
  - Algebraically correct? YES / NO / CONDITIONAL (state the condition)
  - Dimensional consistency? YES / NO / NOT APPLICABLE
  - Sign check? YES / NO
  - If APPROX: approximation named in paper? YES / NO
  - If APPROX: validity condition given? YES / NO
Verdict: SOUND / WEAK / BROKEN
[If WEAK or BROKEN: describe the exact failure here]
```

For APPROX steps: the two APPROX lines are not optional. If a step is APPROX and the paper does not name it, mark this WEAK and record it. If the paper names it but gives no validity condition, mark WEAK and record it. If neither is stated, mark BROKEN.

---

**Step 4. Fill the fault register.**

Take every S-ID with verdict WEAK or BROKEN from Step 3. For each, add one row:

| F-ID | S-ID | Verdict | Type | Description | Fix |
|------|------|---------|------|-------------|-----|

Assign severity:
- **P1** — algebraically wrong
- **P2** — approximation made but not stated
- **P3** — correct but unclear, notational, or missing intermediate

If there are no faults, write: "No faults found. All steps verified as SOUND." Give one sentence explaining why you are confident.

---

**Step 5. State the global verdict and write three fixes.**

State the global verdict in a section called "Derivation Soundness":

> **SOUND** — all steps verify; endpoint follows from starting point.
> **CONDITIONALLY SOUND** — all steps verify under the approximations stated.
> **BROKEN** — at least one P1 error blocks the conclusion.

Then write the AMEND section. Exactly three fixes. Each must cite an F-ID. If P1 faults exist, at least one fix must address a P1. If P2 faults exist, at least one fix must address a P2. Make each fix specific enough to act on — do not write "check the algebra."

---

**Step 6. Write the artifact.**

Write to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> was provided: write flat into <path>/ instead.

Open the file with this frontmatter block — every field required, values must match your map and register exactly:

```yaml
---
skill: simulate-derivation
topic: {{topic}}
date: {{date}}
steps_traced: [integer — count of rows in derivation map]
p1_errors: [integer — count of P1 entries in fault register]
unstated_approx: [integer — count of P2 entries in fault register]
---
```

---

## V-04 — Lifecycle Emphasis: Compressed Acquisition, Expanded Verification

**Axis**: Lifecycle emphasis
**Hypothesis**: Collapsing Phase 1 (acquisition) to a brief preamble and doubling instruction space on Phase 3 (verification) — especially APPROX handling — concentrates token budget on the highest-weight rubric criteria (C-02, C-03) and produces fewer skipped or under-specified verification blocks.

---

You are running /simulate-derivation for: {{topic}}

Trace a mathematical derivation step by step — the algebraic manipulation, not the logical argument. Catch sign errors, missing terms, unjustified approximations, dimensional inconsistencies.

**Before you begin**: read the paper for {{topic}}. If simulate-argument or discover-limiting-cases artifacts exist, read those. Identify the starting expression, the endpoint, and any approximations the paper names. That is all the acquisition you need.

---

## PHASE 1 — DERIVATION MAP

Build the step table:

| S-ID | Starting expression | Operation applied | Resulting expression | Justification | Type |
|------|-------------------|------------------|---------------------|---------------|------|

Types:
- **EXACT**: exact algebraic identity
- **APPROX**: approximation made — state what, under what conditions, whether paper names it
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically

Cover every non-trivial step. Minimum 3 rows.

---

## PHASE 2 — STEP-BY-STEP VERIFICATION (primary output — do not abbreviate)

For each step S-ID, produce a full verification block. This phase is the core deliverable of this skill — allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

```
S-[NN]: [description of what this step does]
From: [exact expression before the step]
Operation: [the specific algebraic or conceptual operation]
To: [exact expression after the step]

Algebraic correctness check:
  Does the algebra hold exactly? YES / NO / CONDITIONAL
  If CONDITIONAL: state the condition explicitly.
  If NO: describe the exact error (wrong sign, missing term, incorrect exponent, etc.).

Dimensional consistency check:
  Are the units on LHS equal to units on RHS? YES / NO / NOT APPLICABLE
  If NO: identify which side has incorrect dimensions and why.

Sign check:
  Does the sign of every term make physical or mathematical sense? YES / NO
  If NO: identify the term and the expected sign with reasoning.

APPROX check (for APPROX-typed steps only — skip for EXACT, DEFINITION, PHYSICAL):
  What quantity or relationship is being approximated?
    [state explicitly — e.g., "x << 1 so sin(x) ≈ x", "weakly-coupled limit so cross-terms drop"]
  Under what conditions does this approximation hold?
    [state the validity condition — e.g., "valid when kT << E_gap", "holds for Re < 1"]
  Does the source paper state this approximation by name or description? YES / NO
  Does the source paper give the validity condition? YES / NO

Step verdict:
  SOUND   — all checks pass
  WEAK    — a minor issue exists (unstated approximation, sign ambiguity, missing intermediate)
  BROKEN  — the step is algebraically wrong; the derivation fails here
```

If the derivation contains zero APPROX-typed steps, add after all verification blocks:
> "APPROX check: no approximation steps found in this derivation. C-03 auto-passes."

---

## PHASE 3 — DERIVATION FAULT REGISTER

| F-ID | S-ID | Verdict | Type | Description | Fix |
|------|------|---------|------|-------------|-----|

Severity:
- **P1** — algebraically wrong
- **P2** — approximation made but not stated (any WEAK/BROKEN from the APPROX check)
- **P3** — correct but unclear, notational, or missing intermediate

Every WEAK or BROKEN verdict from Phase 2 must appear here. If no faults: write "No faults found." with a brief justification.

---

## PHASE 4 — GLOBAL VERDICT AND AMEND

**Derivation Soundness Verdict** (required in a summary section — do not bury in a step block):

| Verdict | Meaning |
|---------|---------|
| SOUND | All steps verified; endpoint follows from starting point |
| CONDITIONALLY SOUND | All steps verified under stated approximations |
| BROKEN | At least one P1 error blocks the conclusion |

State which verdict applies and why in one to three sentences.

**Amend** — exactly three targeted fixes, each citing an F-ID from Phase 3:
1. [F-ID] [severity]: [specific fix — state the exact correction, not generic advice]
2. [F-ID] [severity]: [specific fix]
3. [F-ID] [severity]: [specific fix]

If fewer than three F-IDs exist, use remaining slots for P3 clarity improvements on steps that were SOUND but had minor issues worth addressing.

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]

---

## V-05 — Combined: Master Table Format + Type-Classifier-First Sequence

**Axes**: Output format (V-01) + Role sequence (V-02)
**Hypothesis**: Combining master-table format compression with the type-classifier-first sequence stacks both advantages — the classifier pass primes APPROX detection (C-03), while the master table keeps verification output compact and scannable (C-02). Tests whether these two axes reinforce or interfere.

---

You are running /simulate-derivation for: {{topic}}

Trace a mathematical derivation step by step — the algebraic manipulation, not the logical argument. Every line is a claim that LHS equals RHS after some operation. This skill catches sign errors, missing terms, unjustified approximations, and dimensional inconsistencies that simulate-argument misses.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read: simulate-argument, discover-limiting-cases if available.
Extract: the starting expression, the endpoint, and every approximation the paper explicitly names.

---

## PHASE 2 — TYPE CLASSIFICATION PASS

Before building the derivation map, read the derivation once and classify every step:

```
S-01: EXACT    [brief reason]
S-02: APPROX   [what is approximated — be specific]
S-03: DEFINITION [symbol introduced]
S-04: PHYSICAL [assumption encoded]
...
```

Types:
- **EXACT**: exact algebraic identity
- **APPROX**: an approximation is made
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically

For every APPROX step, note immediately:
- What is being approximated
- The validity condition you expect to need
- Whether the paper names this approximation

This classification is the input to Phase 3. Types in the derivation map must match this list.

---

## PHASE 3 — DERIVATION MAP

Using your Phase 2 classification, build the full step table. Types must match exactly.

| S-ID | Starting expression | Operation applied | Resulting expression | Justification | Type |
|------|-------------------|------------------|---------------------|---------------|------|
| S-01 | ... | ... | ... | ... | [from Phase 2] |

---

## PHASE 4 — MASTER VERIFICATION TABLE

One row per S-ID. All verification checks as columns. Do not skip any row.

| S-ID | Alg. correct? | Dimensional? | Sign OK? | APPROX: stated? | APPROX: validity? | Verdict |
|------|--------------|-------------|---------|----------------|-------------------|---------|
| S-01 | YES/NO/COND | YES/NO/N/A | YES/NO | YES/NO/N/A | YES/NO/N/A | SOUND/WEAK/BROKEN |

Column definitions:
- **Alg. correct?** — does the algebra hold? COND = only under a stated condition.
- **Dimensional?** — LHS units = RHS units? N/A for dimensionless or pure algebraic steps.
- **Sign OK?** — does sign of each term make physical/mathematical sense?
- **APPROX: stated?** — for APPROX steps: does the paper name the approximation? N/A for non-APPROX.
- **APPROX: validity?** — for APPROX steps: does the paper give the validity condition? N/A for non-APPROX.
- **Verdict** — SOUND / WEAK / BROKEN.

After the table: one line per WEAK or BROKEN row explaining the exact failure. If zero APPROX rows exist, add: "No APPROX steps — C-03 auto-passes."

---

## PHASE 5 — DERIVATION FAULT REGISTER

| F-ID | S-ID | Verdict | Type | Description | Fix |
|------|------|---------|------|-------------|-----|

Severity:
- **P1**: algebraically wrong
- **P2**: approximation made but not stated
- **P3**: correct but unclear or missing intermediate

Every WEAK or BROKEN row from Phase 4 must have an entry here.
If no faults: write "No faults found." with a one-sentence justification.

---

## PHASE 6 — GLOBAL VERDICT AND AMEND

**Derivation Soundness** (in a named summary section):
- **SOUND**: all steps verified; endpoint follows from starting point
- **CONDITIONALLY SOUND**: all steps verified under stated approximations
- **BROKEN**: at least one P1 blocks the conclusion

State the verdict in one sentence.

**Amend** — exactly three fixes, each citing an F-ID:
1. [F-ID] [P1/P2/P3]: [specific fix — exact enough to act on]
2. [F-ID] [P1/P2/P3]: [specific fix]
3. [F-ID] [P1/P2/P3]: [specific fix]

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]
