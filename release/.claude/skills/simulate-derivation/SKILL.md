---
name: simulate-derivation
description: "Trace a mathematical derivation step by step — algebraic manipulation, not logical argument. Catches sign errors, missing terms, and unstated approximations. EXACT/APPROX/DEFINITION/PHYSICAL step types."
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /simulate-derivation for: {{topic}}

Trace a mathematical derivation step by step -- the algebraic manipulation, not the logical argument. Catch sign errors, missing terms, unjustified approximations, dimensional inconsistencies.

**Before you begin**: read the paper for {{topic}}. If simulate-argument or discover-limiting-cases artifacts exist, read those. Identify the starting expression, the endpoint, and any approximations the paper names. That is all the acquisition you need.

---

## STRUCTURAL COMMITMENTS

Four design principles govern all gates, axis labels, ordering rules, and gate architecture in this skill. Read these before beginning Phase 1. They apply to every phase.

**Gate principle**: Every mandatory gate in this skill names the verdict token that is blocked until compliance -- not merely the corrective action required. The gate instruction states "X BLOCKED for this step" or "An X verdict may not be recorded while [condition] remains." The verification question at any gate is: "Has the condition blocking X been cleared?" not "Did I perform the required action?" A recovery instruction that states only what to do, without naming what cannot happen, does not satisfy this principle.

**Axis-label principle**: Each row label in every commitment table names the precise mechanistic operation being committed to -- specific enough that a non-compliant behavior cannot satisfy the label by reasonable reading. Distinguishing test: "Could a different, non-compliant behavior satisfy this label?" If yes, replace the label with one that names the exact operation and, where relevant, the exact format or condition required.

**Ordering principle**: Every multi-tier ordering rule in this skill is stated as a single unconditional enumeration naming all tiers in order. Conditional chains ("if P1 exists, fix P1; if no P1 but P2 exists, fix P2") state the top tier leads but leave all subordinate-tier ordering implicit. The unconditional enumeration makes every tier relationship explicit in a single declarative statement, leaving no gap invisible.

**Gate-architecture principle**: This skill applies the gate principle at exactly two structurally distinct contexts -- (1) EXACT type classification at Phase 1: a step may not be labeled EXACT while the algebraic rule in the Justification cell remains unnamed; and (2) APPROX verification at Phase 2: a SOUND verdict may not be recorded while the validity statement (b) remains a paraphrase of the source. These two gates operate at non-overlapping contexts -- type assignment versus soundness recording. No gate collapses these contexts; no phase applies both gates simultaneously. The gate-architecture is a design commitment, not an observed property: both gates are active before any derivation step is classified or any verification block is written.

**Cross-reference map** (every application site in this skill and its governing principle -- each site must carry a cross-reference of the form "per the [principle] in Structural Commitments" or equivalent):

| Application site | Phase | Governing principle |
|-----------------|-------|---------------------|
| EXACT classification gate | Phase 1 | Gate principle |
| Axis-commitment table labels | Phase 1b | Axis-label principle |
| APPROX verification gate | Phase 2 | Gate principle |
| Severity ordering rule | Phase 4 | Ordering principle |

An application site with no cross-reference is a missing declaration -- the governing principle is active but invisible at the point of use.

**Cross-evaluation** (these principles govern each other -- apply them before Phase 1):

- *Axis-label principle applied to the gate verdict token*: Does "SOUND BLOCKED" satisfy the distinguishing test -- could a non-compliant behavior (e.g., recording WEAK instead of SOUND) satisfy this label by reasonable reading? No -- "SOUND BLOCKED" names the exact verdict token that cannot be recorded; WEAK is a different token, not a compliance path. Passes.
- *Gate principle applied to the ordering rule*: If the ordering rule were formulated as a gate, would it name the blocked action? The ordering rule blocks a lower-severity fix from preceding a higher-severity fix in the Amend list -- the blocked action is a misordered fix sequence, not a verdict token. The gate principle and the ordering principle govern complementary domains (verdict recording vs fix sequencing); neither subsumes the other.
- *Ordering principle applied to this preamble*: Are the four principles listed as an unconditional enumeration? Gate, Axis-label, Ordering, Gate-architecture -- four named principles in fixed order. Passes.
- *Gate-architecture principle applied to the axis-label principle*: Do "EXACT BLOCKED" and "SOUND BLOCKED" satisfy the axis-label distinguishing test -- could a non-compliant behavior satisfy either label? "EXACT BLOCKED" names the verdict token that cannot be assigned at Phase 1 type classification; only correctly labeling an unnamed-rule step as APPROX/DEFINITION/PHYSICAL clears it. "SOUND BLOCKED" names the verdict token that cannot be recorded at Phase 2 approximation verification; only replacing (b) with a domain-grounded statement clears it. Both gate labels pass. Gate-architecture confirmed.

---

## PHASE 1 -- DERIVATION MAP

Build the step table:

| S-ID | Starting expression | Operation applied | Resulting expression | Justification | Type |
|------|-------------------|------------------|---------------------|---------------|------|

Types:
- **EXACT**: exact algebraic identity -- the Justification cell must name the algebraic rule, identity, or substitution that makes this step exact (e.g., "product rule," "distributivity," "substitution of Eq. 3"). A step with an unexplained jump may not be labeled EXACT.
- **APPROX**: approximation made -- state what, under what conditions, whether paper names it
- **DEFINITION**: symbol introduced or substituted
- **PHYSICAL**: physical assumption encoded algebraically -- the Justification cell must state the physical assumption being encoded (e.g., "at equilibrium, dR/dt = 0," "incompressible flow," "quasi-static process")

**EXACT classification gate** (per the gate principle in Structural Commitments): A step may not be labeled EXACT while the Justification cell contains an unexplained jump -- a transition from one expression to a significantly different one with no named algebraic rule, identity, or substitution. If the Justification cell is blank, states only "see paper," or cites an equation number without naming the algebraic operation performed, EXACT is BLOCKED for that step. Relabel as APPROX if an approximation may be hiding the gap, DEFINITION if a symbol is introduced, or PHYSICAL if a physical assumption is encoded. EXACT BLOCKED for any step where the algebraic rule remains unnamed. Cleared state: EXACT may be assigned when the Justification cell names a specific algebraic rule, identity, or substitution (e.g., "product rule," "substitution of Eq. 3") -- specific enough that an independent reader could verify the step using only that name.

Cover every non-trivial step. Minimum 3 rows.

---

## PHASE 1b -- STEP EXPANSION PASS

After completing the derivation map, scan each row for compressed steps -- any step where the paper jumps from one expression to a significantly different one without showing the intermediate algebra.

For each compressed step you identify:
- Insert sub-steps labeled S-NNa and S-NNb (or through S-NNc if more sub-steps are needed)
- The intermediate expression is the Resulting expression of S-NNa and the Starting expression of S-NNb
- Mark sub-step rows with "(interpolated)" in the Justification column -- this distinguishes your reconstruction from the paper's own steps

If no compressed steps exist, add: "No compressed steps identified -- C-10 auto-passes."

Interpolated sub-steps are verified in Phase 2 exactly like paper steps.

---

## PHASE 1b COMPLETION CHECK

Before proceeding to Phase 2, confirm that all three structural axes are active. Fill each Status cell with ACTIVE or ABSENT.

(Axis labels follow the axis-label principle from Structural Commitments: each names the precise mechanistic operation, not the general category.)

| Axis | Requirement | Status |
|------|-------------|--------|
| A -- Interpolated sub-step expansion with S-NNa/S-NNb labeling | At least one interpolated sub-step inserted using the S-NNa/S-NNb format, OR "No compressed steps identified -- C-10 auto-passes" explicitly stated above | |
| B -- Prose-per-check reasoning in all verification blocks | Prose-per-check rule (YES -- [sentence] / NO -- [sentence]) will apply to every check in every verification block in Phase 2 | |
| C -- NEW-tagged fault detection for unacknowledged errors | Every WEAK or BROKEN verdict where the source paper does not acknowledge the issue will receive the exact tag "NEW: not acknowledged by paper" in the fault register Description column | |

All present axes must show ACTIVE before you proceed to Phase 2.
If any axis shows ABSENT: revisit Phase 1b (for Axis A) or reconfirm the Phase 2 rules (for Axes B and C).
Do NOT proceed to Phase 2 until all present axes show ACTIVE.

---

## PHASE 2 -- STEP-BY-STEP VERIFICATION (primary output -- do not abbreviate)

For each step S-ID (including interpolated sub-steps from Phase 1b), produce a full verification block. This phase is the core deliverable of this skill -- allocate as much space as needed. Do not collapse multiple steps into one block. Do not omit a step because it looks trivial.

**Reasoning rule -- applies to all checks**: Do not write a bare YES or NO. Every verdict token must be followed by a dash and at least one sentence of reasoning. "YES -- [sentence]" or "NO -- [sentence]". A block containing only YES or NO tokens for any check fails the minimum standard.

**Density uniformity rule -- per step block**: Within any single step block, prose density must be uniform across the APPROX sub-block and the three primary checks (algebraic, dimensional, sign). If the APPROX sub-block contains at least one explanatory sentence, every primary check in that same block must also contain at least one explanatory sentence. The reverse also applies. Uniform means: sparse throughout the block, or rich throughout the block. Mixed density within a single step block fails this rule.

```
S-[NN]: [description of what this step does] [(interpolated) if applicable]
From: [exact expression before the step]
Operation: [the specific algebraic or conceptual operation]
To: [exact expression after the step]

Algebraic correctness check:
  Does the algebra hold exactly?
  YES -- [identify the algebraic identity, rule, or substitution that makes this exact]
  NO -- [identify the exact error: wrong sign, missing term, wrong exponent, incorrect factoring]
  CONDITIONAL -- [state the condition that must hold and why the algebra fails outside it]

Dimensional consistency check:
  Are the units on LHS equal to units on RHS?
  YES -- [confirm which physical dimension appears on each side and how they match]
  NO -- [identify which side carries incorrect dimensions and which factor is responsible]
  NOT APPLICABLE -- [explain why dimensional analysis does not apply here]

Sign check:
  Does the sign of every term make physical or mathematical sense?
  YES -- [state the physical or mathematical principle that governs the expected sign]
  NO -- [identify the specific term, state the expected sign, and give the reasoning]

APPROX check (for APPROX-typed steps only -- skip for EXACT, DEFINITION, PHYSICAL):
  What quantity or relationship is being approximated?
    [state explicitly in the tracer's own words -- do not merely quote the paper]
  Under what conditions does this approximation hold?
    [name the domain regime, physical principle, or first-principles argument --
     e.g., "small-angle regime," "quasi-static assumption," "low Reynolds number."
     Do not paraphrase the source sentence; ground the statement in domain knowledge.]
  Source-removal test: if the source sentence describing this approximation were removed
    entirely, could you support your validity condition from domain knowledge alone?
    YES (independent) / NO (paraphrase)
    If NO: SOUND BLOCKED for this step (per the gate principle in Structural Commitments --
    the gate names the verdict token that is blocked until compliance, not merely the
    corrective action). You must replace (b) with a statement grounded in a named domain
    principle or first-principles argument before proceeding. A SOUND verdict may not be
    recorded for this APPROX block while (b) remains a paraphrase of the source. Correct
    (b) now, then continue to the step verdict line. Cleared state: SOUND may be recorded
    when (b) names a domain regime, physical principle, or first-principles argument that
    would remain fully supportable if the source sentence were removed -- the validity
    statement must stand on domain knowledge alone.
  Does the source paper state this approximation by name or description? YES / NO
  Does the source paper give the validity condition? YES / NO

Step verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN: [exact description of the failure]

Source acknowledgment (complete only when verdict is WEAK or BROKEN):
  Does the source paper flag or acknowledge this specific issue anywhere --
  main text, footnotes, discussion section, or stated limitations? YES / NO
  If NO: this fault is a NEW finding -- the paper does not acknowledge it.
```

If the derivation contains zero APPROX-typed steps, add after all verification blocks:
> "APPROX check: no approximation steps found in this derivation. C-03 auto-passes. C-17 auto-passes."

---

## PHASE 3 -- DERIVATION FAULT REGISTER

| F-ID | S-ID | Verdict | Type | Description | Fix |
|------|------|---------|------|-------------|-----|

Severity:
- **P1** -- algebraically wrong
- **P2** -- approximation made but not stated (any WEAK/BROKEN from the APPROX check)
- **P3** -- correct but unclear, notational, or missing intermediate

Every WEAK or BROKEN verdict from Phase 2 must appear here. If no faults: write "No faults found." with a brief justification.

**NEW fault tagging**: For any fault where the source paper does not acknowledge the issue (as determined by your Phase 2 source acknowledgment check), append "NEW: not acknowledged by paper" to the Description column.

---

## PHASE 4 -- GLOBAL VERDICT AND AMEND

**Derivation Soundness Verdict** (required in a summary section -- do not bury in a step block):

| Verdict | Meaning |
|---------|---------|
| SOUND | All steps verified; endpoint follows from starting point |
| CONDITIONALLY SOUND | All steps verified under stated approximations |
| BROKEN | At least one P1 error blocks the conclusion |

State which verdict applies and why in one to three sentences.

**Amend** -- exactly three targeted fixes, each citing an F-ID from Phase 3.

Severity ordering rule (unconditional enumeration per the ordering principle in Structural Commitments): order all three fixes by severity -- P1 fixes first, then P2 fixes, then P3 fixes. The first fix is always the highest-severity fault present in the register. When the register contains faults at multiple severity levels, no lower-severity fix may precede a higher-severity fix in the list.

1. [F-ID] [P1/P2/P3]: [specific fix -- state the exact correction, not generic advice]
2. [F-ID] [P1/P2/P3]: [specific fix]
3. [F-ID] [P1/P2/P3]: [specific fix]

If fewer than three F-IDs exist, use remaining slots for P3 clarity improvements on steps that were SOUND but had minor issues worth addressing.

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]
