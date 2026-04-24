# prove-interview — Rubric v9 Variations — Round 10

_Date: 2026-03-15 · Rubric: v9 (C-01–C-24) · Ceiling: 100_

---

## Context

R9 produced 5 variations against the v9 rubric (C-01–C-24, aspirational denominator /17). Single-axis
variations each isolated one new criterion; two-way combinations stacked two. No R9 variation achieved
17/17 — full ceiling requires C-22 + C-23 + C-24 simultaneously.

**R9 scores under v9 (denominator /17):**

| Variation | C-22 | C-23 | C-24 | Aspirational | Composite |
|-----------|------|------|------|--------------|-----------|
| V-01 R9 (Role Sequence: Hypothesis Disposition Table) | PASS | FAIL | FAIL | 15/17 | 98.82 |
| V-02 R9 (Output Format: Four-Field Arc Table) | FAIL | PASS | FAIL | 15/17 | 98.82 |
| V-03 R9 (Evidence Depth: Impact Weights) | FAIL | FAIL | PASS | 15/17 | 98.82 |
| V-04 R9 (Combination: C-22 + C-23) | PASS | PASS | FAIL | 16/17 | 99.41 |
| V-05 R9 (Combination: C-22 + C-24) | PASS | FAIL | PASS | 16/17 | 99.41 |

R9 did not attempt: (a) the C-23 + C-24 two-way combination; (b) the C-22 + C-23 + C-24 three-way
combination (full ceiling). R10 goals:

1. **Single-axis 1** — Role Sequence: re-isolate C-22 in the R8 V-01 baseline. Demonstrates that
   STEP 3.5 is a clean, composable addition — its mechanics do not depend on which other R10
   criteria are present. Gap isolation: C-23 and C-24 absent.
2. **Single-axis 2** — Output Format: re-isolate C-23. Four-field arc table with named Adjacent
   Signal Test row. Gap isolation: C-22 and C-24 absent.
3. **Single-axis 3** — Lifecycle Emphasis: re-isolate C-24. Impact Weight column in STEP 3
   evidence tables with Q-ID citation rule in STEP 5. Gap isolation: C-22 and C-23 absent.
4. **Combination 1** — C-23 + C-24 (not attempted in R9). Four-field arc + impact weights, no
   STEP 3.5. Tests the arc-specificity and evidence-prioritization layers together without register
   closure. Expected: 16/17.
5. **Combination 2 (full ceiling)** — C-22 + C-23 + C-24. STEP 3.5 + four-field arc + impact
   weight column. First variation to target 17/17. Tests composability of all three new structural
   additions within the R8 V-01 STEP architecture.

---

## Variation Axes

| Axis | R9 coverage | R10 focus |
|------|-------------|-----------|
| Role sequence (STEP structure) | V-01 R9: C-22 isolated | Re-isolate C-22; confirm clean composability |
| Output format (arc table field count) | V-02 R9: C-23 isolated | Re-isolate C-23; confirm four-field design |
| Lifecycle emphasis (evidence collection depth) | V-03 R9: C-24 isolated | Re-isolate C-24; confirm weight column design |
| C-23 + C-24 combined | Not attempted in R9 | First test of arc-scope + evidence-priority pairing |
| C-22 + C-23 + C-24 combined | Not attempted in R9 | Full ceiling attempt: 17/17 |

---

## V-01 — Single axis: Role Sequence (STEP 3.5 Hypothesis Disposition Table; C-22 isolated)

**Axis:** Role sequence. Single addition to the R8 V-01 baseline: STEP 3.5 — Hypothesis Disposition
Table — inserted between STEP 3 (Interviews) and STEP 4 (Cross-Subject Tensions Matrix). STEP 3.5
closes the hypothesis register before synthesis: every H-ID from STEP 1 must receive a disposition
label and at least one evidence citation before STEP 4 may begin. All other steps are unchanged from
R8 V-01: STEP 0 (Opposition Axis, five-field table), STEP 1 (every-hypothesis quality gate), STEP 2
(roster with pole assignment), STEP 3 (H-ID column + type-tagged evidence), STEP 4 (tensions matrix),
STEP 5 (composite signal), STEP 6 (three-field arc table with binary verdict format rule).

No fourth arc row — C-23 absent by design. No Impact Weight column — C-24 absent by design.

**Hypothesis:** STEP 3.5 satisfies C-22 by construction — the gate rule prevents STEP 4 from being
written while any H-ID has no recorded disposition. C-22 -> C-13 by construction (STEP 3.5 is a
named phase gate). All 14 v8 criteria carry from R8 V-01 baseline. C-23 FAIL (no fourth arc row),
C-24 FAIL (no weight column). Predicted: C-22 PASS, C-23 FAIL, C-24 FAIL → 15/17 → 98.82.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Simulate stakeholder or customer interviews about this topic. The interviews are not real — but
every persona answer must be anchored in the persona's documented identity, expertise, and prior
experience. The output is a signal artifact: structured evidence toward or against the signal
hypothesis.

---

### STEP 0 — Opposition Axis Declaration

Write this section before the Hypothesis Register. It commits the interview design before any
subjects are selected, questions are written, or hypotheses are declared.

This section is not a persona introduction. It is an epistemic design choice: the decision to
interview two subjects at opposite poles of a relevant tension axis rather than two subjects who
might agree.

| Field | Declaration |
|-------|-------------|
| **Axis name** | [Name the tension axis — e.g., "incumbent investment vs. greenfield adoption" / "adoption resistance vs. adoption readiness" / "risk-first vs. capability-first prioritization"] |
| **Why this axis for {SIGNAL}** | [One sentence: why tension on this axis produces more informative evidence for {SIGNAL} than agreement on this axis would. What question about {SIGNAL} can only be answered by hearing from both poles?] |
| **Pole A — resistant / skeptical** | [Describe the position at this pole: what does a subject here believe, what have they invested in, what would adoption of {SIGNAL} cost them?] |
| **Pole B — receptive / innovative** | [Describe the position at this pole: what does a subject here want, what have they not yet invested in, what adoption benefit would they prioritize?] |
| **Evidence requiring Pole B** | [What specific finding type cannot be obtained from a Pole A subject alone? Name the evidence the feature team would miss if both subjects occupied the same pole.] |

**Declaration rules:**
- The axis must be epistemic (a dimension of belief, practice, or expertise), not demographic
  (age, company size, geography).
- Pole A and Pole B must be genuine opposites on the named axis, not variations of the same
  position.
- "Evidence requiring Pole B" must name a specific finding type — "we would miss a perspective"
  fails; "we could not determine whether S-01's adoption conditions are specific to their
  deployment context or universal across the workflow category" passes.

**Gate**: STEP 1 (Hypothesis Register) cannot be written until this section is complete. STEP 2
(Roster) must assign each subject to a pole declared here.

---

### STEP 1 — Hypothesis Register

Write this register before any interview question or persona answer. The register is locked once
written. No question may be written without citing at least one hypothesis ID from this register.

| ID   | Hypothesis                                               | Category                    | Falsification Condition                                                         |
|------|----------------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL] | assumption / risk / unknown | [what a subject would have to say to force rejection — name the answer type]    |
| H-02 | [a specific risk or concern you expect to surface]       | risk                        | [what answer would show this risk does not apply or is overstated]              |
| H-03 | [a design question these interviews should resolve]      | unknown                     | [what finding would resolve this against your expectation]                      |
| H-04 | [add additional hypotheses — aim for at least 4]         |                             |                                                                                 |

**Register rules:**
- Minimum 4 hypotheses.
- **Every declared hypothesis must carry a specific, non-trivial Falsification Condition.** A
  hypothesis with an empty or generic Falsification Condition — e.g., "if people disagree" or
  "if objections arise" — does not satisfy this gate for that H-ID. State the specific evidence
  type, answer pattern, or finding that would force rejection of that specific hypothesis. The
  gate is not satisfied until every H-ID has a non-empty, specific condition.
- Register is locked once written.

**Gate evaluator test:** Could an author satisfy this gate by writing four hypotheses with no
Falsification Conditions and proceed to STEP 3? If yes, this gate fails. STEP 3 (Interviews) may
not begin while any H-ID has an empty or generic Falsification Condition.

---

### STEP 2 — Human Subjects Roster

Assign each subject to a pole declared in STEP 0. A subject with no axis assignment is not
correctly positioned — replace them with a subject at one of the declared poles.

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)             | Key Concern                                                                             |
|------|--------|--------|-----------|--------------------------------|-----------------------------------------------------------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [What this persona is most likely to push back on or champion — grounded in their pole] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [Key concern meaningfully distinct from S-01 — grounded in their pole]                 |

Minimum 2 subjects, one from each declared pole. If both subjects occupy the same pole, return
to STEP 0 and revise the axis declaration.

---

### STEP 3 — Interviews

**Do not write any interview table row until Steps 0, 1, and 2 are complete.** This is a
structural gate: interview rows cannot exist before the Opposition Axis, Hypothesis Register,
and Roster are committed.

For each subject in the roster:

#### [S-nn] — Identity

[2–3 sentences: company type or context, relevant prior experience, at least one concrete concern
or known event. The identity must make the subject's pole assignment legible — a reader should
understand which axis pole this subject occupies from the Identity alone.]

Swap test: substitute another persona's name into this paragraph. If the interview answers would
still read as plausible, revise before writing the table.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn]   | Answer (persona voice)                                 | Evidence Signal [type: ...]                                                           | Surprise?                        |
|-----|-------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------|----------------------------------|
| Q1  | [Question] [H-01] | [Answer — vocabulary and concerns drawn from Identity] | [risk: ...] / [preference: ...] / [constraint: ...] / [validation: ...] / [invalidation: ...] — [one-sentence signal] | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn] |                                                        |                                                                                       |                                  |
| Q3  | [Question] [H-nn] |                                                        |                                                                                       |                                  |

**Table rules:**
- Every question cites at least one H-ID in brackets.
- Every answer fails the swap test — no other persona can be substituted and have the answer
  remain plausible. Generic answers that could belong to any persona fail.
- Every Evidence Signal carries a type tag followed by a one-sentence signal interpretation.
- At least one "Yes" in the Surprise column per subject, with explanation of expected vs. found.
- Minimum 3 rows per subject.

When a STEP 1 Falsification Condition is triggered:
> **[FALSIFICATION — H-nn triggered]:** Condition stated: [exact condition from STEP 1]. Subject
> said: [answer]. Conclusion: [how this forces revision of H-nn].

---

### STEP 3.5 — Hypothesis Disposition Table

Write this section after all STEP 3 interview tables are complete and before STEP 4. This step
closes the hypothesis register. Every H-ID from the STEP 1 register must receive a disposition
label and at least one evidence citation here before STEP 4 may begin.

| H-ID | Disposition | Evidence Citation | Notes |
|------|-------------|-------------------|-------|
| H-01 | CONFIRMED / CHALLENGED / FALSIFIED / UNRESOLVED | [S-nn / Q-nn — cite at least one interview row that drove this disposition] | [Required if UNRESOLVED: state why no question directly tested this H-ID] |
| H-02 | ... | ... | ... |
| H-03 | ... | ... | ... |
| H-04 | ... | ... | ... |

**Disposition definitions:**
- **CONFIRMED**: Evidence from the interviews corroborated this hypothesis — at least one subject
  confirmed the expected pattern, belief, or behavior.
- **CHALLENGED**: Evidence partially contradicted this hypothesis — at least one subject's answer
  conflicts with the stated assumption, but the hypothesis is not fully refuted.
- **FALSIFIED**: The exact Falsification Condition stated in STEP 1 was met. Cite the triggering
  row by Q-ID. The condition was observed, not inferred.
- **UNRESOLVED**: No interview question directly tested this hypothesis. Must state the reason
  explicitly — e.g., "no question addressed H-03's scope" or "removed from final question set
  before interviews ran." UNRESOLVED with no stated reason fails this table.

**Completion rules:**
- Every H-ID from the STEP 1 register must appear in this table — no H-ID may be omitted.
- Each row requires: (1) a disposition label from the four defined options, and (2) at least one
  evidence citation in S-nn or Q-nn format. A disposition with no citation fails.
- UNRESOLVED without a stated reason fails.

**Gate**: STEP 4 (Cross-Subject Tensions Matrix) may not be written until this table is complete
and every H-ID carries a recorded disposition with evidence citation. Evaluator test: could the
Composite Signal section be populated without any H-ID having a recorded disposition here? If
yes, this gate fails.

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after STEP 3.5 is complete (hypothesis register closed).

| Dimension [H-ID if applicable]       | S-01 position | S-02 position | Tension or Agreement [explained]                    | Axis-predicted? | Unresolved? |
|--------------------------------------|---------------|---------------|-----------------------------------------------------|-----------------|-------------|
| [topic / concern / H-ID / axis pole] | [S-01 view]   | [S-02 view]   | TENSION: [describe] / AGREEMENT: [what it signals]  | Expected / Surprise | Yes / No |

**Completion rules:**
- Every row compares at least two subjects on a shared dimension.
- Rows recording agreement must explain why the agreement is meaningful given the Hypothesis
  Register and the opposition axis declared in STEP 0.
- At least one row records an open, unresolved tension. Leave it open.
- Note whether each tension or agreement was predicted by the STEP 0 opposition axis (expected)
  or was a surprise.

---

### STEP 5 — Composite Signal

This section synthesizes — it does not restate. If removing this section would leave the artifact
unchanged, the section has failed. The Composite Signal must add integrated judgment beyond what
a reader can derive from the Interview Tables and Tensions Matrix row by row.

Answer all three of the following in 4–6 sentences:

1. **Integrated verdict**: Does the overall evidence strengthen, weaken, or complicate the
   original SIGNAL hypothesis? State directly.

2. **Dominant finding**: What single finding across all subjects is most decision-relevant?
   Name it specifically — a finding, not a theme.

3. **Key open question**: What is the most important thing these interviews did not resolve?
   What would the feature team need to do next?

Cite subjects by ID (S-01, S-02) and hypothesis IDs (H-nn) where relevant. Reference the
Hypothesis Disposition Table (STEP 3.5) when describing what the evidence confirmed, challenged,
or falsified.

---

### STEP 6 — Arc Signal

**Write this section after the Composite Signal. It is required. It must not restate
feature-level conclusions from STEP 5.**

The Arc Signal answers a question whose scope is wider than {SIGNAL}. It addresses what this
interview run reveals about the adoption pattern, the workflow category, or the class of features
{SIGNAL} belongs to — not whether {SIGNAL} specifically is viable.

| Field | Content |
|-------|---------|
| **Arc question** | [State an explicit question whose scope exceeds {SIGNAL} — e.g., "What does this run tell us about how [user type] navigates [workflow category]?" Scope test: if the same question could only be answered by studying {SIGNAL} specifically, it is not an arc question. If a different but adjacent signal in the same category would generate the same arc question, the scope is correct.] |
| **Arc inference** | [State a conclusion that answers the arc question and that a reader could not reconstruct by reading the Composite Signal alone. The inference adds meaning that derives from the evidence but points beyond this specific feature.] |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state specific reason: what the arc inference provides that per-subject findings and the Composite Signal do not]. |

**Arc self-test verdict format:** The answer must be an explicit binary verdict — "yes" or "no"
— followed immediately by a stated rationale. A narrative answer that implies a verdict without
committing to the binary word fails. A binary verdict without a stated rationale fails. Evaluator
test: if a reviewer disagrees with the verdict, can they identify and challenge the specific
reason stated in the artifact? If the rationale is too diffuse to be directly challenged, revise
before treating STEP 6 as complete.

**Arc self-test rule**: the answer to the self-test must be "yes." If the author answers "no,"
the arc inference has not elevated beyond feature scope — revise the arc inference before
proceeding.

**Scope substitution test**: substitute a different but adjacent signal into the arc question.
If the arc question applies equally, scope is arc-level. If the arc question would need to be
rewritten for the adjacent signal, scope is still feature-level — revise.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-02 — Single axis: Output Format (Four-field arc table with Adjacent Signal Test row; C-23 isolated)

**Axis:** Output format. Single addition to the R8 V-01 baseline: STEP 6 arc table gains a
required fourth row — "Adjacent signal test" — in which the author names a specific adjacent signal
and states whether the arc question applies to it equally (yes/no + reason). The three-field
table from R8 V-01 (Arc question, Arc inference, Arc self-test) is preserved unchanged; the fourth
row is added below. All other steps are unchanged from R8 V-01.

No STEP 3.5 — C-22 absent by design. No Impact Weight column — C-24 absent by design.

**Hypothesis:** The fourth arc row satisfies C-23 by construction — the labeled field forces the
author to name a specific adjacent signal, commit to a binary yes/no, and give a reason. A prose
scope comment elsewhere in STEP 6 would not satisfy C-23; the labeled row does. C-23 -> C-21
-> C-20 -> C-17 by construction. All 14 v8 criteria carry from R8 V-01 baseline. C-22 FAIL (no
STEP 3.5), C-24 FAIL (no weight column). Predicted: C-22 FAIL, C-23 PASS, C-24 FAIL → 15/17
→ 98.82.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Simulate stakeholder or customer interviews about this topic. The interviews are not real — but
every persona answer must be anchored in the persona's documented identity, expertise, and prior
experience. The output is a signal artifact: structured evidence toward or against the signal
hypothesis.

---

### STEP 0 — Opposition Axis Declaration

Write this section before the Hypothesis Register. It commits the interview design before any
subjects are selected, questions are written, or hypotheses are declared.

This section is not a persona introduction. It is an epistemic design choice: the decision to
interview two subjects at opposite poles of a relevant tension axis rather than two subjects who
might agree.

| Field | Declaration |
|-------|-------------|
| **Axis name** | [Name the tension axis — e.g., "incumbent investment vs. greenfield adoption" / "adoption resistance vs. adoption readiness" / "risk-first vs. capability-first prioritization"] |
| **Why this axis for {SIGNAL}** | [One sentence: why tension on this axis produces more informative evidence for {SIGNAL} than agreement on this axis would. What question about {SIGNAL} can only be answered by hearing from both poles?] |
| **Pole A — resistant / skeptical** | [Describe the position at this pole: what does a subject here believe, what have they invested in, what would adoption of {SIGNAL} cost them?] |
| **Pole B — receptive / innovative** | [Describe the position at this pole: what does a subject here want, what have they not yet invested in, what adoption benefit would they prioritize?] |
| **Evidence requiring Pole B** | [What specific finding type cannot be obtained from a Pole A subject alone? Name the evidence the feature team would miss if both subjects occupied the same pole.] |

**Declaration rules:**
- The axis must be epistemic (a dimension of belief, practice, or expertise), not demographic
  (age, company size, geography).
- Pole A and Pole B must be genuine opposites on the named axis, not variations of the same
  position.
- "Evidence requiring Pole B" must name a specific finding type.

**Gate**: STEP 1 (Hypothesis Register) cannot be written until this section is complete. STEP 2
(Roster) must assign each subject to a pole declared here.

---

### STEP 1 — Hypothesis Register

Write this register before any interview question or persona answer. The register is locked once
written. No question may be written without citing at least one hypothesis ID from this register.

| ID   | Hypothesis                                               | Category                    | Falsification Condition                                                         |
|------|----------------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL] | assumption / risk / unknown | [what a subject would have to say to force rejection — name the answer type]    |
| H-02 | [a specific risk or concern you expect to surface]       | risk                        | [what answer would show this risk does not apply or is overstated]              |
| H-03 | [a design question these interviews should resolve]      | unknown                     | [what finding would resolve this against your expectation]                      |
| H-04 | [add additional hypotheses — aim for at least 4]         |                             |                                                                                 |

**Register rules:**
- Minimum 4 hypotheses.
- **Every declared hypothesis must carry a specific, non-trivial Falsification Condition.** A
  hypothesis with an empty or generic Falsification Condition does not satisfy this gate for that
  H-ID. The gate is not satisfied until every H-ID has a non-empty, specific condition.
- Register is locked once written.

**Gate evaluator test:** Could an author satisfy this gate by writing four hypotheses with no
Falsification Conditions and proceed to STEP 3? If yes, this gate fails.

---

### STEP 2 — Human Subjects Roster

Assign each subject to a pole declared in STEP 0. A subject with no axis assignment is not
correctly positioned — replace them with a subject at one of the declared poles.

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)             | Key Concern                                                                             |
|------|--------|--------|-----------|--------------------------------|-----------------------------------------------------------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [What this persona is most likely to push back on or champion — grounded in their pole] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [Key concern meaningfully distinct from S-01 — grounded in their pole]                 |

Minimum 2 subjects, one from each declared pole.

---

### STEP 3 — Interviews

**Do not write any interview table row until Steps 0, 1, and 2 are complete.**

For each subject in the roster:

#### [S-nn] — Identity

[2–3 sentences: company type or context, relevant prior experience, at least one concrete concern
or known event. The identity must make the subject's pole assignment legible.]

Swap test: substitute another persona's name into this paragraph. If the interview answers would
still read as plausible, revise before writing the table.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn]   | Answer (persona voice)                                 | Evidence Signal [type: ...]                                                           | Surprise?                        |
|-----|-------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------|----------------------------------|
| Q1  | [Question] [H-01] | [Answer — vocabulary and concerns drawn from Identity] | [risk: ...] / [preference: ...] / [constraint: ...] / [validation: ...] / [invalidation: ...] — [one-sentence signal] | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn] |                                                        |                                                                                       |                                  |
| Q3  | [Question] [H-nn] |                                                        |                                                                                       |                                  |

**Table rules:**
- Every question cites at least one H-ID in brackets.
- Every answer fails the swap test.
- Every Evidence Signal carries a type tag followed by a one-sentence signal interpretation.
- At least one "Yes" in the Surprise column per subject, with explanation of expected vs. found.
- Minimum 3 rows per subject.

When a STEP 1 Falsification Condition is triggered:
> **[FALSIFICATION — H-nn triggered]:** Condition stated: [exact condition from STEP 1]. Subject
> said: [answer]. Conclusion: [how this forces revision of H-nn].

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after all subject tables are complete.

| Dimension [H-ID if applicable]       | S-01 position | S-02 position | Tension or Agreement [explained]                    | Axis-predicted? | Unresolved? |
|--------------------------------------|---------------|---------------|-----------------------------------------------------|-----------------|-------------|
| [topic / concern / H-ID / axis pole] | [S-01 view]   | [S-02 view]   | TENSION: [describe] / AGREEMENT: [what it signals]  | Expected / Surprise | Yes / No |

**Completion rules:**
- Every row compares at least two subjects on a shared dimension.
- Rows recording agreement must explain why the agreement is meaningful given the STEP 0 axis.
- At least one row records an open, unresolved tension. Leave it open.
- Note whether each row was predicted (expected) or was a surprise.

---

### STEP 5 — Composite Signal

This section synthesizes — it does not restate. If removing this section would leave the artifact
unchanged, the section has failed.

Answer all three of the following in 4–6 sentences:

1. **Integrated verdict**: Does the overall evidence strengthen, weaken, or complicate the
   original SIGNAL hypothesis? State directly.

2. **Dominant finding**: What single finding across all subjects is most decision-relevant?
   Name it specifically — a finding, not a theme.

3. **Key open question**: What is the most important thing these interviews did not resolve?
   What would the feature team need to do next?

Cite subjects by ID (S-01, S-02) and hypothesis IDs (H-nn) where relevant.

---

### STEP 6 — Arc Signal

**Write this section after the Composite Signal. It is required. It must not restate
feature-level conclusions from STEP 5.**

The Arc Signal answers a question whose scope is wider than {SIGNAL}.

| Field | Content |
|-------|---------|
| **Arc question** | [State an explicit question whose scope exceeds {SIGNAL}. Scope test: if the same question could only be answered by studying {SIGNAL} specifically, it is not an arc question. If a different but adjacent signal in the same category would generate the same arc question, the scope is correct.] |
| **Arc inference** | [State a conclusion that answers the arc question and that a reader could not reconstruct by reading the Composite Signal alone.] |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state specific reason]. |
| **Adjacent signal test** | [Name a specific adjacent signal — a different but related signal in the same namespace or feature category. Not a placeholder such as "another signal" or "a similar feature." State whether the arc question applies to that signal equally: yes/no — because [reason: what distinguishes {SIGNAL}'s domain from the adjacent signal's domain, or why the arc question is genuinely arc-level regardless of which signal prompts it].] |

**Arc self-test verdict format:** The Arc self-test answer must be an explicit binary verdict —
"yes" or "no" — followed immediately by a stated rationale. A narrative answer without the binary
word fails. A binary verdict without a rationale fails. Evaluator test: if a reviewer disagrees
with the verdict, can they identify and challenge the specific reason stated?

**Adjacent signal test rule:** The fourth row must name a specific, real adjacent signal. A
placeholder fails. The verdict (yes/no whether the arc question applies equally) must be binary,
and a reason must be stated. A scope comment embedded in arc inference prose without a dedicated
labeled row fails C-23. If the test returns "yes, applies equally," arc-level scope is confirmed.
If it returns "no, because X," the arc question must be revised to arc scope before proceeding.

**Arc self-test rule**: the Arc self-test answer must be "yes." If the author answers "no," the
arc inference has not elevated beyond feature scope — revise before proceeding.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-03 — Single axis: Lifecycle Emphasis (Impact Weight column in evidence; C-24 isolated)

**Axis:** Lifecycle emphasis — depth and structure of the evidence collection phase. Single
addition to the R8 V-01 baseline: STEP 3 interview tables gain an Impact Weight column (H / M / L)
assigned per evidence row at collection time. STEP 5 Composite Signal gains an Impact Weight
citation rule: the highest-weight finding must be named by Q-ID. All other steps are unchanged
from R8 V-01.

No STEP 3.5 — C-22 absent by design. No fourth arc row — C-23 absent by design.

**Hypothesis:** The Impact Weight column satisfies C-24 — the column is assigned at collection
time (not retroactively), differentiation is required (all-identical weights fail), and the STEP 5
rule forces the composite to cite the highest-weight finding by Q-ID. C-24 -> C-09 and C-24 ->
C-12 by construction (weight column presupposes type-tagged H-ID-anchored evidence). All 14 v8
criteria carry from R8 V-01 baseline. C-22 FAIL (no STEP 3.5), C-23 FAIL (no fourth arc row).
Predicted: C-22 FAIL, C-23 FAIL, C-24 PASS → 15/17 → 98.82.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Simulate stakeholder or customer interviews about this topic. The interviews are not real — but
every persona answer must be anchored in the persona's documented identity, expertise, and prior
experience. The output is a signal artifact: structured evidence toward or against the signal
hypothesis.

---

### STEP 0 — Opposition Axis Declaration

Write this section before the Hypothesis Register. It commits the interview design before any
subjects are selected, questions are written, or hypotheses are declared.

| Field | Declaration |
|-------|-------------|
| **Axis name** | [Name the tension axis — e.g., "incumbent investment vs. greenfield adoption" / "adoption resistance vs. adoption readiness"] |
| **Why this axis for {SIGNAL}** | [One sentence: why tension on this axis produces more informative evidence for {SIGNAL} than agreement would.] |
| **Pole A — resistant / skeptical** | [What does a subject here believe, what have they invested in, what would adoption cost them?] |
| **Pole B — receptive / innovative** | [What does a subject here want, what have they not invested in, what adoption benefit would they prioritize?] |
| **Evidence requiring Pole B** | [What specific finding type cannot be obtained from a Pole A subject alone?] |

**Declaration rules:**
- Axis must be epistemic, not demographic.
- Pole A and Pole B must be genuine opposites.
- "Evidence requiring Pole B" must name a specific finding type.

**Gate**: STEP 1 cannot be written until this section is complete. STEP 2 must assign each
subject to a pole declared here.

---

### STEP 1 — Hypothesis Register

Write this register before any interview question or persona answer. Register is locked once
written. No question may be written without citing at least one H-ID from this register.

| ID   | Hypothesis                                               | Category                    | Falsification Condition                                                         |
|------|----------------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL] | assumption / risk / unknown | [what a subject would have to say to force rejection — name the answer type]    |
| H-02 | [a specific risk or concern you expect to surface]       | risk                        | [what answer would show this risk does not apply]                               |
| H-03 | [a design question these interviews should resolve]      | unknown                     | [what finding would resolve this against your expectation]                      |
| H-04 | [add additional hypotheses — aim for at least 4]         |                             |                                                                                 |

**Register rules:**
- Minimum 4 hypotheses.
- **Every declared hypothesis must carry a specific, non-trivial Falsification Condition.** Empty
  or generic conditions ("if people disagree") do not satisfy this gate. The gate applies to every
  H-ID — not "at least one."
- Register is locked once written.

**Gate evaluator test:** Could an author write four hypotheses with no Falsification Conditions
and proceed to STEP 3? If yes, this gate fails.

---

### STEP 2 — Human Subjects Roster

Assign each subject to a pole declared in STEP 0.

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)             | Key Concern                                                                             |
|------|--------|--------|-----------|--------------------------------|-----------------------------------------------------------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [What this persona is most likely to push back on or champion]                          |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [Key concern meaningfully distinct from S-01]                                           |

Minimum 2 subjects, one from each declared pole.

---

### STEP 3 — Interviews

**Do not write any interview table row until Steps 0, 1, and 2 are complete.**

For each subject in the roster:

#### [S-nn] — Identity

[2–3 sentences: company type or context, relevant prior experience, at least one concrete concern
or known event. Identity must make pole assignment legible.]

Swap test: substitute another persona's name. If answers remain plausible, revise.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn]   | Answer (persona voice)                                 | Evidence Signal [type: ...]                                                           | Impact Weight | Surprise?                        |
|-----|-------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------|---------------|----------------------------------|
| Q1  | [Question] [H-01] | [Answer — vocabulary and concerns drawn from Identity] | [risk: ...] / [preference: ...] / [constraint: ...] / [validation: ...] / [invalidation: ...] — [one-sentence signal] | H / M / L | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn] |                                                        |                                                                                       |               |                                  |
| Q3  | [Question] [H-nn] |                                                        |                                                                                       |               |                                  |

**Table rules:**
- Every question cites at least one H-ID in brackets.
- Every answer fails the swap test.
- Every Evidence Signal carries a type tag followed by a one-sentence signal interpretation.
- **Impact Weight column**: assign H (high), M (medium), or L (low) to each row at the time the
  evidence is recorded — not retroactively. Rationale: impact weight is a judgment about relative
  importance committed before reviewing the full evidence set. All-identical weights (all H, all M,
  all L) fail — differentiation is required. At least one H and at least one non-H weight must
  appear across all subjects.
- At least one "Yes" in the Surprise column per subject, with explanation.
- Minimum 3 rows per subject.

When a STEP 1 Falsification Condition is triggered:
> **[FALSIFICATION — H-nn triggered]:** Condition stated: [exact condition from STEP 1]. Subject
> said: [answer]. Conclusion: [how this forces revision of H-nn].

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after all subject tables are complete.

| Dimension [H-ID if applicable]       | S-01 position | S-02 position | Tension or Agreement [explained]                    | Axis-predicted? | Unresolved? |
|--------------------------------------|---------------|---------------|-----------------------------------------------------|-----------------|-------------|
| [topic / concern / H-ID / axis pole] | [S-01 view]   | [S-02 view]   | TENSION: [describe] / AGREEMENT: [what it signals]  | Expected / Surprise | Yes / No |

**Completion rules:**
- Every row compares at least two subjects on a shared dimension.
- Agreement rows explain why the agreement is meaningful given the STEP 0 axis.
- At least one row records an open, unresolved tension.
- Note whether each row was expected or a surprise.

---

### STEP 5 — Composite Signal

This section synthesizes — it does not restate. If removing this section would leave the artifact
unchanged, the section has failed.

Answer all three of the following in 4–6 sentences:

1. **Integrated verdict**: Does the overall evidence strengthen, weaken, or complicate the
   original SIGNAL hypothesis? State directly.

2. **Dominant finding**: What single finding across all subjects is most decision-relevant?
   Name it specifically — a finding, not a theme.

3. **Key open question**: What is the most important thing these interviews did not resolve?
   What would the feature team need to do next?

Cite subjects by ID (S-01, S-02) and hypothesis IDs (H-nn) where relevant.

**Impact Weight citation rule:** The Composite Signal must name at least one finding by its Q-ID
and explicitly state that it carries the highest impact weight driving the composite verdict.
Format: cite the Q-ID (e.g., "Q3 from S-01") and state it carries H (high) weight. A composite
that synthesizes without citing the highest-weight finding by Q-ID fails C-24. The cited finding
must be verifiable against the Impact Weight column in STEP 3 — if the cited Q-ID does not carry
the highest declared weight in the table, the citation fails.

---

### STEP 6 — Arc Signal

**Write this section after the Composite Signal. It is required. It must not restate
feature-level conclusions from STEP 5.**

The Arc Signal answers a question whose scope is wider than {SIGNAL}.

| Field | Content |
|-------|---------|
| **Arc question** | [State an explicit question whose scope exceeds {SIGNAL}. Scope test: if the same question could only be answered by studying {SIGNAL} specifically, it is not an arc question.] |
| **Arc inference** | [State a conclusion that answers the arc question and that a reader could not reconstruct by reading the Composite Signal alone.] |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state specific reason]. |

**Arc self-test verdict format:** The answer must be an explicit binary verdict — "yes" or "no"
— followed immediately by a stated rationale. A narrative answer without the binary word fails. A
binary verdict without a rationale fails.

**Arc self-test rule**: the answer must be "yes." Revise the arc inference if not.

**Scope substitution test**: substitute a different but adjacent signal. If the arc question
applies equally, scope is arc-level. If the arc question would need rewriting, scope is still
feature-level — revise.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-04 — Combination: Output Format + Lifecycle Emphasis (C-23 + C-24; first pairing not attempted in R9)

**Axes:** Output format (four-field arc table, C-23) + lifecycle emphasis (impact weight column
in STEP 3 evidence tables, C-24). This is the first variation to combine these two axes. R9 did
not attempt this pairing: R9 V-04 combined C-22 + C-23, R9 V-05 combined C-22 + C-24. This
variation isolates the C-23 + C-24 combination — asking whether arc scope specificity and evidence
prioritization compose cleanly when STEP 3.5 (register closure) is deliberately absent.

No STEP 3.5 — C-22 absent by design (gap isolation: testing whether C-23 and C-24 can compose
without register closure mediating between them).

**Hypothesis:** Impact Weight column in STEP 3 satisfies C-24 at evidence-collection time; STEP 5
Q-ID citation rule enforces composite priority linkage. Four-field arc table in STEP 6 satisfies
C-23 (Adjacent Signal Test row with binary verdict + reason). The two additions operate on
independent structural locations (STEP 3/5 vs STEP 6) — no interaction effects expected. All 14
v8 criteria carry from R8 V-01 baseline. C-22 FAIL (no STEP 3.5). Predicted: C-22 FAIL, C-23
PASS, C-24 PASS → 16/17 → 99.41.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Simulate stakeholder or customer interviews about this topic. The interviews are not real — but
every persona answer must be anchored in the persona's documented identity, expertise, and prior
experience. The output is a signal artifact: structured evidence toward or against the signal
hypothesis.

---

### STEP 0 — Opposition Axis Declaration

Write this section before the Hypothesis Register. It commits the interview design before any
subjects are selected, questions are written, or hypotheses are declared.

| Field | Declaration |
|-------|-------------|
| **Axis name** | [Name the tension axis — e.g., "incumbent investment vs. greenfield adoption" / "adoption resistance vs. adoption readiness"] |
| **Why this axis for {SIGNAL}** | [One sentence: why tension on this axis produces more informative evidence for {SIGNAL} than agreement would. What question about {SIGNAL} can only be answered by hearing from both poles?] |
| **Pole A — resistant / skeptical** | [What does a subject here believe, what have they invested in, what would adoption of {SIGNAL} cost them?] |
| **Pole B — receptive / innovative** | [What does a subject here want, what have they not invested in, what adoption benefit would they prioritize?] |
| **Evidence requiring Pole B** | [What specific finding type cannot be obtained from a Pole A subject alone?] |

**Declaration rules:** Axis must be epistemic. Poles must be genuine opposites. "Evidence
requiring Pole B" must name a specific finding type.

**Gate**: STEP 1 cannot be written until this section is complete. STEP 2 must assign each
subject to a pole declared here.

---

### STEP 1 — Hypothesis Register

Write before any interview question or persona answer. Register locked once written.

| ID   | Hypothesis                                               | Category                    | Falsification Condition                                                         |
|------|----------------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL] | assumption / risk / unknown | [what a subject would have to say to force rejection]                           |
| H-02 | [a specific risk or concern you expect to surface]       | risk                        | [what answer would show this risk does not apply]                               |
| H-03 | [a design question these interviews should resolve]      | unknown                     | [what finding would resolve this against your expectation]                      |
| H-04 | [add additional hypotheses — aim for at least 4]         |                             |                                                                                 |

**Register rules:**
- Minimum 4 hypotheses.
- **Every declared hypothesis must carry a specific, non-trivial Falsification Condition.** Generic
  conditions fail. The gate applies to every H-ID.
- Register is locked once written.

**Gate evaluator test:** Could an author write four hypotheses with no Falsification Conditions
and proceed to STEP 3? If yes, this gate fails.

---

### STEP 2 — Human Subjects Roster

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)             | Key Concern                                                                             |
|------|--------|--------|-----------|--------------------------------|-----------------------------------------------------------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [What this persona is most likely to push back on or champion]                          |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [Key concern meaningfully distinct from S-01]                                           |

Minimum 2 subjects, one from each declared pole.

---

### STEP 3 — Interviews

**Do not write any interview table row until Steps 0, 1, and 2 are complete.**

For each subject in the roster:

#### [S-nn] — Identity

[2–3 sentences: context, prior experience, at least one concrete concern. Identity must make pole
assignment legible.]

Swap test: substitute another persona's name. If answers remain plausible, revise.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn]   | Answer (persona voice)                                 | Evidence Signal [type: ...]                                                           | Impact Weight | Surprise?                        |
|-----|-------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------|---------------|----------------------------------|
| Q1  | [Question] [H-01] | [Answer — vocabulary and concerns drawn from Identity] | [risk: ...] / [preference: ...] / [constraint: ...] / [validation: ...] / [invalidation: ...] — [one-sentence signal] | H / M / L | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn] |                                                        |                                                                                       |               |                                  |
| Q3  | [Question] [H-nn] |                                                        |                                                                                       |               |                                  |

**Table rules:**
- Every question cites at least one H-ID in brackets.
- Every answer fails the swap test.
- Every Evidence Signal carries a type tag and a one-sentence signal interpretation.
- **Impact Weight column**: assign H (high), M (medium), or L (low) per row at collection time.
  Not retroactively. All-identical weights fail — differentiation is required.
- At least one "Yes" per subject with explanation.
- Minimum 3 rows per subject.

When a STEP 1 Falsification Condition is triggered:
> **[FALSIFICATION — H-nn triggered]:** Condition stated: [exact condition]. Subject said:
> [answer]. Conclusion: [how this forces revision of H-nn].

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after all subject tables are complete.

| Dimension [H-ID if applicable]       | S-01 position | S-02 position | Tension or Agreement [explained]                    | Axis-predicted? | Unresolved? |
|--------------------------------------|---------------|---------------|-----------------------------------------------------|-----------------|-------------|
| [topic / concern / H-ID / axis pole] | [S-01 view]   | [S-02 view]   | TENSION: [describe] / AGREEMENT: [what it signals]  | Expected / Surprise | Yes / No |

**Completion rules:** At least one unresolved tension. Agreement rows explain why convergence
matters given the STEP 0 axis. Note expected vs. surprise per row.

---

### STEP 5 — Composite Signal

This section synthesizes — it does not restate. Removal test: if removing this section would
leave the artifact unchanged, revise.

Answer all three in 4–6 sentences:

1. **Integrated verdict**: Does the overall evidence strengthen, weaken, or complicate the
   original SIGNAL hypothesis? State directly.

2. **Dominant finding**: What single finding is most decision-relevant? Name it specifically.

3. **Key open question**: What did these interviews not resolve?

Cite subjects (S-nn) and hypothesis IDs (H-nn) where relevant.

**Impact Weight citation rule:** Name at least one finding by its Q-ID (e.g., "Q3 from S-01")
and explicitly state it carries the highest impact weight driving the composite verdict. Example:
"The composite verdict is primarily driven by [Q-ID] ([H-ID], H-weight), which showed..."
A composite synthesizing without citing the highest-weight finding by Q-ID fails C-24. The
cited Q-ID must match the H weight assigned in the STEP 3 table.

---

### STEP 6 — Arc Signal

**Required. Must not restate feature-level conclusions from STEP 5.**

The Arc Signal answers a question whose scope is wider than {SIGNAL}.

| Field | Content |
|-------|---------|
| **Arc question** | [An explicit question whose scope exceeds {SIGNAL}. Scope test: if this question could only be answered by studying {SIGNAL} specifically, it is not an arc question.] |
| **Arc inference** | [A conclusion answering the arc question that a reader could not reconstruct from the Composite Signal alone.] |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state specific reason]. |
| **Adjacent signal test** | [Name a specific adjacent signal — not a placeholder. State whether the arc question applies to that signal equally: yes/no — because [reason: what distinguishes this run's domain from the adjacent signal's domain, or why the arc question is genuinely arc-level].] |

**Arc self-test verdict format:** Binary "yes" or "no" immediately followed by stated rationale.
Narrative without the binary word fails. Binary without rationale fails. The answer must be
"yes" — if "no," revise the arc inference.

**Adjacent signal test rule:** The fourth row must name a specific, real adjacent signal. A
placeholder ("some other signal," "a similar feature") fails. Verdict must be binary (yes/no)
with a stated reason. A scope comment embedded in prose without a dedicated row fails C-23.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-05 — Combination: C-22 + C-23 + C-24 (full ceiling attempt; 17/17 target)

**Axes:** Role sequence (STEP 3.5 Hypothesis Disposition Table, C-22) + output format (four-field
arc table with Adjacent Signal Test row, C-23) + lifecycle emphasis (Impact Weight column, C-24).
First variation to combine all three new criteria. This is the 17/17 target for Round 10.

The three additions operate at independent structural locations:
- C-22 (STEP 3.5): inserted between STEP 3 and STEP 4 — closes hypothesis register
- C-23 (STEP 6 fourth row): adds Adjacent Signal Test field to arc table
- C-24 (STEP 3 column + STEP 5 rule): adds Impact Weight to evidence collection; adds Q-ID
  citation requirement to composite synthesis

No interaction conflicts are predicted. STEP 3.5 does not affect STEP 6 arc table structure.
Impact Weight column does not affect STEP 3.5 disposition table. Adjacent Signal Test row does
not affect STEP 5 composite signal format. The three additions are structurally independent.

**Hypothesis:** All three C-22, C-23, C-24 pass by construction. All 14 v8 criteria carry from
R8 V-01 baseline. Predicted: C-22 PASS, C-23 PASS, C-24 PASS → 17/17 → 100.00.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Simulate stakeholder or customer interviews about this topic. The interviews are not real — but
every persona answer must be anchored in the persona's documented identity, expertise, and prior
experience. The output is a signal artifact: structured evidence toward or against the signal
hypothesis.

---

### STEP 0 — Opposition Axis Declaration

Write this section before the Hypothesis Register. It commits the interview design before any
subjects are selected, questions are written, or hypotheses are declared.

This section is not a persona introduction. It is an epistemic design choice: the decision to
interview two subjects at opposite poles of a relevant tension axis rather than two subjects who
might agree.

| Field | Declaration |
|-------|-------------|
| **Axis name** | [Name the tension axis — e.g., "incumbent investment vs. greenfield adoption" / "adoption resistance vs. adoption readiness" / "risk-first vs. capability-first prioritization"] |
| **Why this axis for {SIGNAL}** | [One sentence: why tension on this axis produces more informative evidence for {SIGNAL} than agreement on this axis would. What question about {SIGNAL} can only be answered by hearing from both poles?] |
| **Pole A — resistant / skeptical** | [Describe the position at this pole: what does a subject here believe, what have they invested in, what would adoption of {SIGNAL} cost them?] |
| **Pole B — receptive / innovative** | [Describe the position at this pole: what does a subject here want, what have they not yet invested in, what adoption benefit would they prioritize?] |
| **Evidence requiring Pole B** | [What specific finding type cannot be obtained from a Pole A subject alone? Name the evidence the feature team would miss if both subjects occupied the same pole.] |

**Declaration rules:**
- The axis must be epistemic (a dimension of belief, practice, or expertise), not demographic
  (age, company size, geography).
- Pole A and Pole B must be genuine opposites on the named axis.
- "Evidence requiring Pole B" must name a specific finding type.

**Gate**: STEP 1 (Hypothesis Register) cannot be written until this section is complete. STEP 2
(Roster) must assign each subject to a pole declared here.

---

### STEP 1 — Hypothesis Register

Write this register before any interview question or persona answer. The register is locked once
written. No question may be written without citing at least one hypothesis ID from this register.

| ID   | Hypothesis                                               | Category                    | Falsification Condition                                                         |
|------|----------------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL] | assumption / risk / unknown | [what a subject would have to say to force rejection — name the answer type]    |
| H-02 | [a specific risk or concern you expect to surface]       | risk                        | [what answer would show this risk does not apply or is overstated]              |
| H-03 | [a design question these interviews should resolve]      | unknown                     | [what finding would resolve this against your expectation]                      |
| H-04 | [add additional hypotheses — aim for at least 4]         |                             |                                                                                 |

**Register rules:**
- Minimum 4 hypotheses.
- **Every declared hypothesis must carry a specific, non-trivial Falsification Condition.** A
  hypothesis with an empty or generic Falsification Condition does not satisfy this gate for that
  H-ID. The gate is not satisfied until every H-ID has a non-empty, specific condition.
- Register is locked once written.

**Gate evaluator test:** Could an author satisfy this gate by writing four hypotheses with no
Falsification Conditions and proceed to STEP 3? If yes, this gate fails. STEP 3 may not begin
while any H-ID has an empty or generic Falsification Condition.

---

### STEP 2 — Human Subjects Roster

Assign each subject to a pole declared in STEP 0. A subject with no axis assignment is not
correctly positioned — replace them.

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)             | Key Concern                                                                             |
|------|--------|--------|-----------|--------------------------------|-----------------------------------------------------------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [What this persona is most likely to push back on or champion — grounded in their pole] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [Key concern meaningfully distinct from S-01 — grounded in their pole]                 |

Minimum 2 subjects, one from each declared pole.

---

### STEP 3 — Interviews

**Do not write any interview table row until Steps 0, 1, and 2 are complete.** This is a
structural gate: interview rows cannot exist before the Opposition Axis, Hypothesis Register,
and Roster are committed.

For each subject in the roster:

#### [S-nn] — Identity

[2–3 sentences: company type or context, relevant prior experience, at least one concrete concern
or known event. The identity must make the subject's pole assignment legible — a reader should
understand which axis pole this subject occupies from the Identity alone.]

Swap test: substitute another persona's name into this paragraph. If the interview answers would
still read as plausible, revise before writing the table.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn]   | Answer (persona voice)                                 | Evidence Signal [type: ...]                                                           | Impact Weight | Surprise?                        |
|-----|-------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------|---------------|----------------------------------|
| Q1  | [Question] [H-01] | [Answer — vocabulary and concerns drawn from Identity] | [risk: ...] / [preference: ...] / [constraint: ...] / [validation: ...] / [invalidation: ...] — [one-sentence signal] | H / M / L | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn] |                                                        |                                                                                       |               |                                  |
| Q3  | [Question] [H-nn] |                                                        |                                                                                       |               |                                  |

**Table rules:**
- Every question cites at least one H-ID in brackets.
- Every answer fails the swap test — no other persona can be substituted and have the answer
  remain plausible. Generic answers fail.
- Every Evidence Signal carries a type tag followed by a one-sentence signal interpretation.
- **Impact Weight column**: assign H (high), M (medium), or L (low) per row at collection time
  — not retroactively. This is a relative importance judgment committed before reviewing all rows.
  All-identical weights (all H, all M, all L) fail — differentiation is required across the full
  evidence set.
- At least one "Yes" in the Surprise column per subject, with explanation of expected vs. found.
- Minimum 3 rows per subject.

When a STEP 1 Falsification Condition is triggered:
> **[FALSIFICATION — H-nn triggered]:** Condition stated: [exact condition from STEP 1]. Subject
> said: [answer]. Conclusion: [how this forces revision of H-nn].

---

### STEP 3.5 — Hypothesis Disposition Table

Write this section after all STEP 3 interview tables are complete and before STEP 4. This step
closes the hypothesis register. Every H-ID from the STEP 1 register must receive a disposition
label and at least one evidence citation here before STEP 4 may begin.

| H-ID | Disposition | Evidence Citation | Notes |
|------|-------------|-------------------|-------|
| H-01 | CONFIRMED / CHALLENGED / FALSIFIED / UNRESOLVED | [S-nn / Q-nn — cite at least one interview row that drove this disposition] | [Required if UNRESOLVED: state why no question directly tested this H-ID] |
| H-02 | ... | ... | ... |
| H-03 | ... | ... | ... |
| H-04 | ... | ... | ... |

**Disposition definitions:**
- **CONFIRMED**: Interview evidence corroborated this hypothesis.
- **CHALLENGED**: Evidence partially contradicted this hypothesis — at least one answer conflicts
  with the stated assumption, but the hypothesis is not fully refuted.
- **FALSIFIED**: The exact Falsification Condition stated in STEP 1 was met. Cite the triggering
  row by Q-ID.
- **UNRESOLVED**: No interview question directly tested this hypothesis. Must state the reason
  explicitly (e.g., "no question addressed H-03's scope"). UNRESOLVED with no stated reason
  fails this table.

**Completion rules:**
- Every H-ID from the STEP 1 register must appear — no H-ID may be omitted.
- Each row requires: (1) a disposition label from the four defined options, and (2) at least one
  evidence citation in S-nn or Q-nn format. A disposition with no citation fails.
- UNRESOLVED without a stated reason fails.

**Gate**: STEP 4 (Cross-Subject Tensions Matrix) may not be written until this table is complete
and every H-ID carries a recorded disposition with evidence citation. Evaluator test: could the
Composite Signal section be populated without any H-ID having a recorded disposition here? If
yes, this gate fails.

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after STEP 3.5 is complete (hypothesis register closed).

| Dimension [H-ID if applicable]       | S-01 position | S-02 position | Tension or Agreement [explained]                    | Axis-predicted? | Unresolved? |
|--------------------------------------|---------------|---------------|-----------------------------------------------------|-----------------|-------------|
| [topic / concern / H-ID / axis pole] | [S-01 view]   | [S-02 view]   | TENSION: [describe] / AGREEMENT: [what it signals]  | Expected / Surprise | Yes / No |

**Completion rules:**
- Every row compares at least two subjects on a shared dimension.
- Agreement rows explain why the convergence is meaningful given the STEP 0 axis.
- At least one row records an open, unresolved tension. Leave it open.
- Note whether each row was predicted (expected) or a surprise.

---

### STEP 5 — Composite Signal

This section synthesizes — it does not restate. If removing this section would leave the artifact
unchanged, the section has failed. The Composite Signal must add integrated judgment beyond what
a reader can derive from the Interview Tables and Tensions Matrix row by row.

Answer all three of the following in 4–6 sentences:

1. **Integrated verdict**: Does the overall evidence strengthen, weaken, or complicate the
   original SIGNAL hypothesis? State directly.

2. **Dominant finding**: What single finding across all subjects is most decision-relevant?
   Name it specifically — a finding, not a theme.

3. **Key open question**: What is the most important thing these interviews did not resolve?
   What would the feature team need to do next?

Cite subjects by ID (S-01, S-02) and hypothesis IDs (H-nn) where relevant. Reference the
Hypothesis Disposition Table (STEP 3.5) when describing what the evidence confirmed, challenged,
or falsified.

**Impact Weight citation rule:** The Composite Signal must name at least one finding by its Q-ID
and explicitly state that it carries the highest impact weight driving the composite verdict.
Format: cite Q-ID (e.g., "Q3 from S-01") and state it carries H (high) weight. A composite
synthesizing without citing the highest-weight finding by Q-ID fails C-24. The cited Q-ID must
match the H weight in the STEP 3 table — verifiable by inspection.

---

### STEP 6 — Arc Signal

**Write this section after the Composite Signal. It is required. It must not restate
feature-level conclusions from STEP 5.**

The Arc Signal answers a question whose scope is wider than {SIGNAL}. It addresses what this
interview run reveals about the adoption pattern, the workflow category, or the class of features
{SIGNAL} belongs to — not whether {SIGNAL} specifically is viable.

| Field | Content |
|-------|---------|
| **Arc question** | [State an explicit question whose scope exceeds {SIGNAL} — e.g., "What does this run tell us about how [user type] navigates [workflow category]?" Scope test: if the same question could only be answered by studying {SIGNAL} specifically, it is not an arc question. If a different but adjacent signal in the same category would generate the same arc question, the scope is correct.] |
| **Arc inference** | [State a conclusion that answers the arc question and that a reader could not reconstruct by reading the Composite Signal alone. The inference adds meaning that derives from the evidence but points beyond this specific feature.] |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state specific reason: what the arc inference provides that per-subject findings and the Composite Signal do not]. |
| **Adjacent signal test** | [Name a specific adjacent signal — a different but related signal in the same namespace or feature category. Not a placeholder. State whether the arc question applies to it equally: yes/no — because [reason: what distinguishes {SIGNAL}'s domain from the adjacent signal's domain, or why the arc question is genuinely arc-level regardless of which signal prompts it].] |

**Arc self-test verdict format:** The Arc self-test answer must be an explicit binary verdict —
"yes" or "no" — followed immediately by a stated rationale. A narrative answer without the
binary word fails. A binary verdict without rationale fails. Evaluator test: if a reviewer
disagrees with the verdict, can they identify and challenge the specific reason stated? If the
rationale is too diffuse to be directly challenged, revise before treating STEP 6 as complete.

**Adjacent signal test rule:** The fourth row must name a specific, real adjacent signal. A
placeholder ("another signal," "a related feature") fails. Verdict must be binary (yes/no) with
a stated reason. A scope comment embedded in arc inference prose without a dedicated labeled row
fails C-23. If the test returns "yes, applies equally," arc-level scope is confirmed. If it
returns "no, because X," revise the arc question to arc scope.

**Arc self-test rule**: the Arc self-test answer must be "yes." If "no," the arc inference has
not elevated beyond feature scope — revise before proceeding.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## Predicted R10 Scores Under v9

| Variation | C-22 | C-23 | C-24 | Aspirational | Composite |
|-----------|------|------|------|--------------|-----------|
| V-01 (Role Sequence: STEP 3.5 Hypothesis Disposition) | PASS | FAIL | FAIL | 15/17 | 98.82 |
| V-02 (Output Format: Four-Field Arc Table) | FAIL | PASS | FAIL | 15/17 | 98.82 |
| V-03 (Lifecycle Emphasis: Impact Weight Column) | FAIL | FAIL | PASS | 15/17 | 98.82 |
| V-04 (Combination: C-23 + C-24) | FAIL | PASS | PASS | 16/17 | 99.41 |
| V-05 (Combination: C-22 + C-23 + C-24) | PASS | PASS | PASS | 17/17 | 100.00 |

*V-01: STEP 3.5 closes the register; gate prevents STEP 4 while any H-ID undisposed -- C-22 PASS.
No fourth arc row -- C-23 FAIL. No weight column -- C-24 FAIL. All 14 v8 criteria carry.*

*V-02: Four-field arc table with named Adjacent Signal Test row -- C-23 PASS. No STEP 3.5 --
C-22 FAIL. No weight column -- C-24 FAIL. All 14 v8 criteria carry.*

*V-03: Impact Weight column in STEP 3 with differentiated H/M/L; STEP 5 cites top-weight Q-ID
-- C-24 PASS. No STEP 3.5 -- C-22 FAIL. No fourth arc row -- C-23 FAIL. All 14 v8 criteria carry.*

*V-04: Impact Weight column (C-24) + four-field arc table (C-23); first R10 combination. C-22
absent -- STEP 3.5 not present, hypothesis register open at synthesis entry. C-23 PASS, C-24
PASS. First variation to test C-23 + C-24 pairing in isolation from C-22.*

*V-05: STEP 3.5 (C-22) + four-field arc table (C-23) + Impact Weight column (C-24). First
variation to target 17/17. All three additions operate at independent structural locations -- no
interaction conflict. Satisfies C-22, C-23, C-24 simultaneously. All 14 v8 criteria carry. Full
ceiling: 17/17 → 100.00 predicted.*

---

## What R10 Tests

R9 demonstrated that each of C-22, C-23, C-24 can be isolated and that two-way combinations
C-22+C-23 and C-22+C-24 achieve 16/17. Three questions remain open entering R10:

1. **Can C-23 + C-24 compose cleanly without C-22?** V-04 tests this. The arc table's
   Adjacent Signal Test field and the evidence table's Impact Weight column operate in different
   structural locations. No mediating dependency is predicted.

2. **Does C-22 + C-23 + C-24 achieve 17/17?** V-05 tests this. The three additions are
   structurally independent: STEP 3.5 is a new step, the fourth arc row is a new table row, the
   Impact Weight column is a new column. No structural interaction conflicts exist.

3. **Do the single-axis re-isolations confirm clean composability?** V-01, V-02, V-03 each
   re-run a single criterion in a fresh prompt body against the R8 V-01 baseline. If the scores
   replicate R9 single-axis results (15/17 each), the individual mechanisms are confirmed stable
   and the V-05 composition is justified.
