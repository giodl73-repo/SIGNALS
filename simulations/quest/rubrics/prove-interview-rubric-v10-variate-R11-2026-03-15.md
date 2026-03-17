# prove-interview — Rubric v10 Variations — Round 11

_Date: 2026-03-15 · Rubric: v10 (C-01–C-25) · Ceiling: 100_

---

## Context

R10 achieved 17/17 in V-05 under the v9 rubric (C-01–C-24). Under the v10 rubric (C-01–C-25,
aspirational denominator /18), no R10 variation satisfies C-25 — the cross-reference requirement
connecting C-23's adjacent signal test field to C-24's H-weight Q-IDs. R11 goals:

1. **Single-axis 1** — Role Sequence: re-confirm C-22 isolated (STEP 3.5, no weight column, no
   fourth arc row). Gap isolation: C-23, C-24, C-25 absent. Expected: 15/18.
2. **Single-axis 2** — Output Format: re-confirm C-23 isolated (four-field arc table with Adjacent
   Signal Test row, no STEP 3.5, no weight column). Gap isolation: C-22, C-24, C-25 absent.
   Expected: 15/18.
3. **Single-axis 3** — Lifecycle Emphasis: re-confirm C-24 isolated (weight column + Q-ID citation
   rule, no STEP 3.5, no fourth arc row). Gap isolation: C-22, C-23, C-25 absent. Expected: 15/18.
4. **C-25 on minimal prereq (V-04 baseline + C-25)** — C-23 + C-24 + C-25, no C-22. Tests whether
   C-25 composes without register closure as a structural mediator. Expected: 17/18.
5. **Full ceiling** — C-22 + C-23 + C-24 + C-25 simultaneously. First variation targeting 18/18.

**R10 scores re-scored under v10 (denominator /18):**

| Variation | C-22 | C-23 | C-24 | C-25 | Aspirational | Composite |
|-----------|------|------|------|------|--------------|-----------|
| V-01 R10 (Role Sequence: C-22 isolated) | PASS | FAIL | FAIL | FAIL | 15/18 | 98.33 |
| V-02 R10 (Output Format: C-23 isolated) | FAIL | PASS | FAIL | FAIL | 15/18 | 98.33 |
| V-03 R10 (Lifecycle: C-24 isolated) | FAIL | FAIL | PASS | FAIL | 15/18 | 98.33 |
| V-04 R10 (Combination: C-23 + C-24) | FAIL | PASS | PASS | FAIL | 16/18 | 98.89 |
| V-05 R10 (Full: C-22 + C-23 + C-24) | PASS | PASS | PASS | FAIL | 17/18 | 99.44 |

C-25 requires C-23 (adjacent signal test field) and C-24 (H-weight column) as structural
preconditions. C-25 cannot pass in any variation where C-23 or C-24 is absent.

---

## Variation Axes

| Axis | R10 coverage | R11 focus |
|------|-------------|-----------|
| Role sequence (STEP structure) | V-01: C-22 isolated | Re-confirm C-22; establish 15/18 baseline |
| Output format (arc table field count) | V-02: C-23 isolated | Re-confirm C-23; establish 15/18 baseline |
| Lifecycle emphasis (evidence collection depth) | V-03: C-24 isolated | Re-confirm C-24; establish 15/18 baseline |
| C-23 + C-24 + C-25 (minimal prereq for C-25) | Not attempted in R10 | First test of C-25 without STEP 3.5; expected 17/18 |
| C-22 + C-23 + C-24 + C-25 (full ceiling) | Not attempted in R10 | First 18/18 attempt |

---

## V-01 — Single axis: Role Sequence (STEP 3.5 Hypothesis Disposition; C-22 isolated)

**Axis:** Role sequence. Single addition to the R8 V-01 baseline: STEP 3.5 — Hypothesis Disposition
Table — inserted between STEP 3 (Interviews) and STEP 4 (Cross-Subject Tensions Matrix). Closes the
hypothesis register before synthesis: every H-ID receives a disposition label and evidence citation
before STEP 4 may begin.

No weight column — C-24 absent by design.
No fourth arc row — C-23 absent by design.
No C-25 — adjacent signal test field is absent, so cross-reference cannot exist.

**Hypothesis:** C-22 PASS (STEP 3.5 gate enforces disposition closure). C-23 FAIL (no adjacent
signal test row). C-24 FAIL (no Impact Weight column). C-25 FAIL (C-23 prerequisite missing).
Predicted: 15/18 → 98.33.

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

| ID   | Hypothesis | Category | Falsification Condition |
|------|------------|----------|------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL] | assumption / risk / unknown | [what a subject would have to say to force rejection — name the answer type] |
| H-02 | [a specific risk or concern you expect to surface] | risk | [what answer would show this risk does not apply or is overstated] |
| H-03 | [a design question these interviews should resolve] | unknown | [what finding would resolve this against your expectation] |
| H-04 | [add additional hypotheses — aim for at least 4] | | |

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

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)            | Key Concern |
|------|--------|--------|-----------|-------------------------------|-------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0) | [What this persona is most likely to push back on or champion — grounded in their pole] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0) | [Key concern meaningfully distinct from S-01 — grounded in their pole] |

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

| Q#  | Question [H-nn]   | Answer (persona voice) | Evidence Signal [type: ...] | Surprise? |
|-----|-------------------|------------------------|----------------------------|-----------|
| Q1  | [Question] [H-01] | [Answer — vocabulary and concerns drawn from Identity] | [risk: ...] / [preference: ...] / [constraint: ...] / [validation: ...] / [invalidation: ...] — [one-sentence signal] | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn] | | | |
| Q3  | [Question] [H-nn] | | | |

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

| Dimension [H-ID if applicable] | S-01 position | S-02 position | Tension or Agreement [explained] | Axis-predicted? | Unresolved? |
|--------------------------------|---------------|---------------|----------------------------------|-----------------|-------------|
| [topic / concern / H-ID / axis pole] | [S-01 view] | [S-02 view] | TENSION: [describe] / AGREEMENT: [what it signals] | Expected / Surprise | Yes / No |

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
| **Arc question** | [State an explicit question whose scope exceeds {SIGNAL} — e.g., "What does this run tell us about how [user type] navigates [workflow category]?" Scope test: if the same question could only be answered by studying {SIGNAL} specifically, it is not an arc question.] |
| **Arc inference** | [State a conclusion that answers the arc question and that a reader could not reconstruct by reading the Composite Signal alone.] |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state specific reason: what the arc inference provides that per-subject findings and the Composite Signal do not]. |

**Arc self-test verdict format:** The answer must be an explicit binary verdict — "yes" or "no"
— followed immediately by a stated rationale. A narrative answer that implies a verdict without
committing to the binary word fails. A binary verdict without a stated rationale fails. Evaluator
test: if a reviewer disagrees with the verdict, can they identify and challenge the specific
reason stated in the artifact? If the rationale is too diffuse to be directly challenged, revise.

**Arc self-test rule**: the answer to the self-test must be "yes." If the author answers "no,"
the arc inference has not elevated beyond feature scope — revise the arc inference before
proceeding.

---

## V-02 — Single axis: Output Format (Four-Field Arc Table; C-23 isolated)

**Axis:** Output format. Single addition to the R8 V-01 baseline: the STEP 6 arc table gains a
fourth labeled row — "Adjacent signal test" — requiring a specific adjacent signal (not a
placeholder), a yes/no verdict, and a stated reason why the arc question does or does not apply
to the adjacent signal equally.

No STEP 3.5 — C-22 absent by design.
No Impact Weight column — C-24 absent by design.
No C-25 — the adjacent signal test field is present, but C-25 requires the field to also cross-
reference H-weight Q-IDs from C-24's weight column, which does not exist here.

**Hypothesis:** C-22 FAIL (no STEP 3.5). C-23 PASS (four-field arc table with labeled Adjacent
Signal Test row: specific adjacent signal required, binary yes/no, stated reason). C-24 FAIL (no
Impact Weight column). C-25 FAIL (C-24 prerequisite missing — no H-weight Q-ID to cross-reference).
Predicted: 15/18 → 98.33.

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
| **Axis name** | [Name the tension axis — e.g., "incumbent investment vs. greenfield adoption" / "adoption resistance vs. adoption readiness" / "risk-first vs. capability-first prioritization"] |
| **Why this axis for {SIGNAL}** | [One sentence: why tension on this axis produces more informative evidence for {SIGNAL} than agreement on this axis would.] |
| **Pole A — resistant / skeptical** | [Describe the position at this pole.] |
| **Pole B — receptive / innovative** | [Describe the position at this pole.] |
| **Evidence requiring Pole B** | [What specific finding type cannot be obtained from a Pole A subject alone?] |

**Declaration rules:**
- The axis must be epistemic, not demographic.
- Pole A and Pole B must be genuine opposites on the named axis.
- "Evidence requiring Pole B" must name a specific finding type.

**Gate**: STEP 1 cannot be written until this section is complete.

---

### STEP 1 — Hypothesis Register

Write before any interview question. Locked once written.

| ID   | Hypothesis | Category | Falsification Condition |
|------|------------|----------|------------------------|
| H-01 | [belief about stakeholder response] | assumption / risk / unknown | [specific evidence type that would force rejection] |
| H-02 | [risk or concern you expect] | risk | [answer pattern that would show this risk is overstated] |
| H-03 | [design question to resolve] | unknown | [finding that would resolve this against expectation] |
| H-04 | [additional hypothesis] | | |

**Register rules:**
- Minimum 4 hypotheses.
- Every H-ID must carry a specific, non-trivial Falsification Condition. Generic conditions
  ("if people disagree") fail.
- Register is locked once written.

**Gate evaluator test:** Could an author write four hypotheses with no Falsification Conditions
and proceed? If yes, this gate fails.

---

### STEP 2 — Human Subjects Roster

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)            | Key Concern |
|------|--------|--------|-----------|-------------------------------|-------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0) | [Persona's primary concern, grounded in their pole] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0) | [Distinct concern from S-01, grounded in their pole] |

Minimum 2 subjects, one from each pole.

---

### STEP 3 — Interviews

**Gate:** No interview row may be written until STEP 0, 1, and 2 are complete.

For each subject:

#### [S-nn] — Identity

[2–3 sentences: company context, relevant prior experience, at least one concrete concern. The
identity must make the pole assignment legible without referencing STEP 0 directly.]

Swap test: substitute another persona's name. If answers remain plausible, revise before writing
the table.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn]   | Answer (persona voice) | Evidence Signal [type: ...] | Surprise? |
|-----|-------------------|------------------------|----------------------------|-----------|
| Q1  | [Question] [H-01] | [Answer — vocabulary drawn from Identity] | [risk/preference/constraint/validation/invalidation: signal] | Yes — assumed X, found Y / No |
| Q2  | [Question] [H-nn] | | | |
| Q3  | [Question] [H-nn] | | | |

**Table rules:** Every question cites at least one H-ID. Every answer fails the swap test.
Every Evidence Signal carries a type tag. At least one Yes in Surprise per subject. Minimum 3
rows per subject.

---

### STEP 4 — Cross-Subject Tensions Matrix

| Dimension [H-ID if applicable] | S-01 position | S-02 position | Tension or Agreement | Axis-predicted? | Unresolved? |
|--------------------------------|---------------|---------------|----------------------|-----------------|-------------|
| [dimension] | [S-01 view] | [S-02 view] | TENSION / AGREEMENT: [described] | Expected / Surprise | Yes / No |

At least one row records an open, unresolved tension. Agreement rows must explain why agreement
is meaningful given the opposition axis.

---

### STEP 5 — Composite Signal

Synthesize across all findings, subjects, and tensions. Answer in 4–6 sentences:

1. **Integrated verdict**: Does evidence strengthen, weaken, or complicate the SIGNAL hypothesis?
2. **Dominant finding**: What single finding is most decision-relevant? Name it specifically.
3. **Key open question**: What did these interviews not resolve?

Cite subjects (S-nn) and hypotheses (H-nn) where relevant.

---

### STEP 6 — Arc Signal

**Required. Must not restate feature-level conclusions from STEP 5.**

| Field | Content |
|-------|---------|
| **Arc question** | [Question whose scope exceeds {SIGNAL}. Scope test: if the same question could only be answered by studying {SIGNAL} specifically, it is not an arc question. If a different but adjacent signal in the same category would generate the same arc question, the scope is correct.] |
| **Arc inference** | [Conclusion answering the arc question; not reconstructable from the Composite Signal alone.] |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something not reconstructable from feature evidence alone? Answer: [yes / no] — because [specific reason]. |
| **Adjacent signal test** | Adjacent signal: [name a specific adjacent signal in the same namespace — not a placeholder]. Arc question applies equally: [yes / no] — because [state reason why the arc question's scope does or does not apply to the named adjacent signal equally]. |

**Arc self-test verdict format:** Binary verdict ("yes" or "no") followed immediately by a stated
rationale. Narrative without binary word fails. Binary without rationale fails.

**Arc self-test rule:** Answer must be "yes." If "no," revise the arc inference.

**Adjacent signal test rule:** The named adjacent signal must be specific (e.g., "prove-prototype"
or "scout-feasibility") — not a category label or placeholder. The yes/no verdict must state a
reason. A scope comment embedded in arc inference prose without a dedicated row fails this field.

---

## V-03 — Single axis: Lifecycle Emphasis (Impact Weight Column; C-24 isolated)

**Axis:** Lifecycle emphasis. Single addition to the R8 V-01 baseline: STEP 3 interview tables
gain an Impact Weight column (H/M/L) assigned at collection time — not retroactively. All-
identical weights fail; differentiation is required. STEP 5 gains an Impact Weight citation rule:
the composite must name at least one finding by Q-ID and explicitly cite it as the highest-weight
driver.

No STEP 3.5 — C-22 absent by design.
No fourth arc row — C-23 absent by design; therefore no adjacent signal test field.
No C-25 — C-23 prerequisite missing; no field exists in which a Q-ID cross-reference could appear.

**Hypothesis:** C-22 FAIL (no STEP 3.5). C-23 FAIL (no fourth arc row). C-24 PASS (weight column
with differentiation requirement and Q-ID citation rule in STEP 5). C-25 FAIL (C-23 prerequisite
absent). Predicted: 15/18 → 98.33.

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

Write this section before the Hypothesis Register.

| Field | Declaration |
|-------|-------------|
| **Axis name** | [Name the tension axis] |
| **Why this axis for {SIGNAL}** | [Why tension on this axis produces more informative evidence than agreement] |
| **Pole A — resistant / skeptical** | [Position at this pole] |
| **Pole B — receptive / innovative** | [Position at this pole] |
| **Evidence requiring Pole B** | [Specific finding type unavailable from Pole A alone] |

**Gate**: STEP 1 cannot be written until this section is complete.

---

### STEP 1 — Hypothesis Register

Write before any interview question. Locked once written.

| ID   | Hypothesis | Category | Falsification Condition |
|------|------------|----------|------------------------|
| H-01 | [belief] | assumption / risk / unknown | [specific falsification condition] |
| H-02 | [risk] | risk | [condition] |
| H-03 | [design question] | unknown | [condition] |
| H-04 | [additional] | | |

Minimum 4 hypotheses, each with a specific Falsification Condition. Generic conditions fail.

---

### STEP 2 — Human Subjects Roster

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)            | Key Concern |
|------|--------|--------|-----------|-------------------------------|-------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B | [Concern grounded in pole] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B | [Distinct concern grounded in pole] |

---

### STEP 3 — Interviews

**Gate:** No interview row may be written until STEP 0, 1, and 2 are complete.

Assign Impact Weights (H/M/L) at the time each row is recorded. Do not assign weights
retroactively after all interviews are complete.

For each subject:

#### [S-nn] — Identity

[2–3 sentences: context, prior experience, concrete concern. Pole assignment must be legible
from the Identity alone.]

Swap test: answers must not survive persona substitution.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn] | Answer (persona voice) | Evidence Signal [type: ...] | Impact Weight | Surprise? |
|-----|-----------------|------------------------|----------------------------|---------------|-----------|
| Q1  | [Question] [H-01] | [Answer] | [type: signal] | H / M / L | Yes — assumed X, found Y / No |
| Q2  | [Question] [H-nn] | | | H / M / L | |
| Q3  | [Question] [H-nn] | | | H / M / L | |

**Impact Weight rules:**
- H (High): finding materially changes the feature team's understanding of the problem space,
  adoption risk, or design constraint.
- M (Medium): finding is relevant and informative but does not force a revision of assumptions.
- L (Low): finding confirms existing knowledge or is a weak signal.
- **All-identical weights fail.** At least two distinct weight values must appear across the
  full set of evidence rows. A table where every row is "M" fails this requirement.
- Assign weights when the row is written, not after all interviews are complete.

---

### STEP 4 — Cross-Subject Tensions Matrix

| Dimension [H-ID if applicable] | S-01 position | S-02 position | Tension or Agreement | Axis-predicted? | Unresolved? |
|--------------------------------|---------------|---------------|----------------------|-----------------|-------------|
| [dimension] | [S-01 view] | [S-02 view] | TENSION / AGREEMENT: [described] | Expected / Surprise | Yes / No |

At least one open, unresolved tension required.

---

### STEP 5 — Composite Signal

Synthesize in 4–6 sentences:

1. **Integrated verdict**: Does evidence strengthen, weaken, or complicate the SIGNAL hypothesis?
2. **Dominant finding**: Name the highest-weight finding driving the composite verdict by Q-ID.
   Cite it explicitly: "Q-nn from S-nn (H weight) is the primary driver because..."
3. **Key open question**: What did these interviews not resolve?

**Impact Weight citation rule:** The Composite Signal must name at least one finding by Q-ID and
explicitly identify it as the highest-weight (H-weight) driver. A composite that discusses themes
without citing a specific H-weight finding by Q-ID fails this rule. Evaluator test: can an
evaluator determine which evidence row drove the composite verdict and verify it carries H weight
in the STEP 3 table? If not, revise before treating STEP 5 as complete.

---

### STEP 6 — Arc Signal

**Required. Must not restate feature-level conclusions from STEP 5.**

| Field | Content |
|-------|---------|
| **Arc question** | [Question whose scope exceeds {SIGNAL}. Scope test: if the same question could only be answered by studying {SIGNAL} specifically, it is not an arc question.] |
| **Arc inference** | [Conclusion answering the arc question; not reconstructable from the Composite Signal alone.] |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something not reconstructable from feature evidence alone? Answer: [yes / no] — because [specific reason]. |

**Arc self-test verdict:** Binary "yes" / "no" immediately followed by rationale. Answer must
be "yes" — if "no," revise the arc inference.

---

## V-04 — Combination: C-23 + C-24 + C-25 (C-25 on minimal prerequisite baseline)

**Axis:** Output format + lifecycle emphasis — this is the first variation to introduce C-25.
Built on the R10 V-04 baseline (C-23 + C-24), with a single addition: the Adjacent Signal Test
field is extended to include a cross-reference to the H-weight Q-ID(s) from STEP 3's Impact
Weight column, with a stated verdict on whether those findings would arise equally in an interview
about the named adjacent signal.

No STEP 3.5 — C-22 absent by design. Tests whether C-25 composes with C-23 + C-24 without
register closure as a structural mediator.

**Hypothesis:** C-22 FAIL (no STEP 3.5). C-23 PASS (four-field arc table with Adjacent Signal
Test row). C-24 PASS (Impact Weight column with differentiation requirement and Q-ID citation
rule). C-25 PASS (adjacent signal test field names H-weight Q-ID(s) from C-24's column, states
signal-specific verdict with reason). Predicted: 17/18 → 99.44.

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
| **Axis name** | [Name the tension axis — e.g., "incumbent investment vs. greenfield adoption" / "adoption resistance vs. adoption readiness" / "risk-first vs. capability-first prioritization"] |
| **Why this axis for {SIGNAL}** | [One sentence: why tension on this axis produces more informative evidence for {SIGNAL} than agreement on this axis would. What question about {SIGNAL} can only be answered by hearing from both poles?] |
| **Pole A — resistant / skeptical** | [Describe the position at this pole: what does a subject here believe, what have they invested in, what would adoption of {SIGNAL} cost them?] |
| **Pole B — receptive / innovative** | [Describe the position at this pole: what does a subject here want, what have they not yet invested in, what adoption benefit would they prioritize?] |
| **Evidence requiring Pole B** | [What specific finding type cannot be obtained from a Pole A subject alone? Name the evidence the feature team would miss if both subjects occupied the same pole.] |

**Declaration rules:**
- The axis must be epistemic, not demographic.
- Pole A and Pole B must be genuine opposites on the named axis.
- "Evidence requiring Pole B" must name a specific finding type.

**Gate**: STEP 1 (Hypothesis Register) cannot be written until this section is complete.

---

### STEP 1 — Hypothesis Register

Write before any interview question. Locked once written.

| ID   | Hypothesis | Category | Falsification Condition |
|------|------------|----------|------------------------|
| H-01 | [belief about stakeholder response] | assumption / risk / unknown | [specific evidence type that forces rejection] |
| H-02 | [risk you expect to surface] | risk | [answer pattern showing risk is overstated] |
| H-03 | [design question to resolve] | unknown | [finding that resolves against expectation] |
| H-04 | [additional hypothesis] | | |

Minimum 4 hypotheses, each with a specific Falsification Condition. Generic conditions fail.
Register is locked once written.

---

### STEP 2 — Human Subjects Roster

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)            | Key Concern |
|------|--------|--------|-----------|-------------------------------|-------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0) | [Concern grounded in pole] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0) | [Distinct concern grounded in pole] |

Minimum 2 subjects, one from each declared pole.

---

### STEP 3 — Interviews

**Gate:** No interview row may be written until STEP 0, 1, and 2 are complete.

Assign Impact Weights at the time each row is recorded. Do not assign weights retroactively.

For each subject:

#### [S-nn] — Identity

[2–3 sentences: company context, relevant prior experience, at least one concrete concern. The
identity must make the pole assignment legible without referencing STEP 0 directly.]

Swap test: answers must not survive persona substitution.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn] | Answer (persona voice) | Evidence Signal [type: ...] | Impact Weight | Surprise? |
|-----|-----------------|------------------------|----------------------------|---------------|-----------|
| Q1  | [Question] [H-01] | [Answer — vocabulary drawn from Identity] | [type: signal] | H / M / L | Yes — assumed X, found Y / No |
| Q2  | [Question] [H-nn] | | | H / M / L | |
| Q3  | [Question] [H-nn] | | | H / M / L | |

**Impact Weight rules:**
- H: finding materially changes understanding of the problem space or design constraint.
- M: relevant and informative, does not force assumption revision.
- L: confirms existing knowledge or is a weak signal.
- All-identical weights fail — at least two distinct values required across all evidence rows.
- Assign at collection time.

**Table rules:** Every question cites at least one H-ID. Every answer fails the swap test.
Every Evidence Signal carries a type tag. At least one Yes in Surprise per subject. Minimum 3
rows per subject.

---

### STEP 4 — Cross-Subject Tensions Matrix

| Dimension [H-ID if applicable] | S-01 position | S-02 position | Tension or Agreement | Axis-predicted? | Unresolved? |
|--------------------------------|---------------|---------------|----------------------|-----------------|-------------|
| [dimension] | [S-01 view] | [S-02 view] | TENSION / AGREEMENT: [described] | Expected / Surprise | Yes / No |

At least one open, unresolved tension required. Agreement rows must explain significance given
the opposition axis.

---

### STEP 5 — Composite Signal

Synthesize in 4–6 sentences:

1. **Integrated verdict**: Does evidence strengthen, weaken, or complicate the SIGNAL hypothesis?
2. **Dominant finding**: Name the highest-weight finding driving the composite verdict. Cite
   by Q-ID: "Q-nn from S-nn (H weight) is the primary driver because..."
3. **Key open question**: What did these interviews not resolve?

**Impact Weight citation rule:** The composite must name at least one H-weight finding by Q-ID
explicitly. Evaluator test: can an evaluator identify which Q-ID drove the verdict and verify
it carries H weight in the STEP 3 table? If not, revise.

---

### STEP 6 — Arc Signal

**Required. Must not restate feature-level conclusions from STEP 5.**

The Arc Signal answers a question whose scope is wider than {SIGNAL}. It addresses what this
interview run reveals about the adoption pattern, the workflow category, or the class of features
{SIGNAL} belongs to.

| Field | Content |
|-------|---------|
| **Arc question** | [Question whose scope exceeds {SIGNAL}. Scope test: if the same question could only be answered by studying {SIGNAL} specifically, it is not an arc question. If a different but adjacent signal in the same category would generate the same arc question, the scope is correct.] |
| **Arc inference** | [Conclusion answering the arc question; not reconstructable from the Composite Signal alone. The inference adds meaning that derives from the evidence but points beyond this specific feature.] |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something not reconstructable from feature evidence alone? Answer: [yes / no] — because [state specific reason: what the arc inference provides that per-subject findings and the Composite Signal do not]. |
| **Adjacent signal test** | Adjacent signal: [name a specific adjacent signal in the same namespace — e.g., "prove-prototype" or "scout-feasibility" — not a category label or placeholder]. Arc question applies equally: [yes / no] — because [state reason why the arc question's scope does or does not apply equally to the named adjacent signal]. Top-weight evidence check: [cite the H-weight Q-ID(s) identified in STEP 5 as the composite's primary driver(s)]. Signal-specific: [yes / no] — because [state whether the H-weight finding(s) would be expected to arise in an interview about the named adjacent signal, and why. A finding is signal-specific if the adjacent signal's domain would not surface it; a finding is portable if both signals share the same adoption or design dimension that produced it]. |

**Arc self-test verdict format:** Binary "yes" / "no" immediately followed by rationale.
Narrative without binary word fails. Binary without rationale fails. Answer must be "yes" — if
"no," revise arc inference.

**Adjacent signal test rules:**
- The named adjacent signal must be specific — not a category label or placeholder.
- The arc question applicability verdict must be binary (yes/no) with a stated reason.
- The top-weight evidence check must cite at least one Q-ID by ID (e.g., "Q3 from S-01").
  A generic reference to "high-weight findings" without a Q-ID fails.
- The signal-specific verdict must be binary (yes/no) with a stated reason addressing whether
  the named finding would arise in an interview about the adjacent signal.
- Evaluator test: can an evaluator confirm that the H-weight Q-ID(s) driving the composite are
  tied to this signal's domain specifically, not portable to the adjacent signal? If no Q-ID is
  named in the adjacent signal test field, C-25 fails.

---

## V-05 — Full Ceiling: C-22 + C-23 + C-24 + C-25 (18/18 target)

**Axis:** All four simultaneously. Built on R10 V-05 (C-22 + C-23 + C-24, 17/17), with a single
addition to the Adjacent Signal Test row: a cross-reference to the H-weight Q-ID(s) named in
STEP 5, with a signal-specific verdict and stated reason.

**Structural locations of the four additions:**
- STEP 3.5 (between STEP 3 and STEP 4) — C-22
- Impact Weight column in STEP 3 tables + Q-ID citation rule in STEP 5 — C-24
- Fourth row in STEP 6 arc table ("Adjacent signal test") — C-23
- Extension of the Adjacent Signal Test row to include H-weight Q-ID cross-reference — C-25

All four additions operate at non-overlapping structural locations. No addition references or
depends on another's structural element except the declared C-25 → C-23 and C-25 → C-24
cascades (which are the design intent, not an interaction conflict).

**Hypothesis:** C-22 PASS (STEP 3.5 closes register before synthesis). C-23 PASS (four-field
arc table with labeled Adjacent Signal Test row). C-24 PASS (Impact Weight column with H-weight
Q-ID citation in STEP 5). C-25 PASS (Adjacent Signal Test field names H-weight Q-IDs and states
signal-specific verdict with reason). Predicted: 18/18 → 100.00.

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

| ID   | Hypothesis | Category | Falsification Condition |
|------|------------|----------|------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL] | assumption / risk / unknown | [what a subject would have to say to force rejection — name the answer type] |
| H-02 | [a specific risk or concern you expect to surface] | risk | [what answer would show this risk does not apply or is overstated] |
| H-03 | [a design question these interviews should resolve] | unknown | [what finding would resolve this against your expectation] |
| H-04 | [add additional hypotheses — aim for at least 4] | | |

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

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)            | Key Concern |
|------|--------|--------|-----------|-------------------------------|-------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0) | [What this persona is most likely to push back on or champion — grounded in their pole] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0) | [Key concern meaningfully distinct from S-01 — grounded in their pole] |

Minimum 2 subjects, one from each declared pole. If both subjects occupy the same pole, return
to STEP 0 and revise the axis declaration.

---

### STEP 3 — Interviews

**Do not write any interview table row until Steps 0, 1, and 2 are complete.** This is a
structural gate: interview rows cannot exist before the Opposition Axis, Hypothesis Register,
and Roster are committed.

Assign Impact Weights (H/M/L) at the time each row is recorded. Do not assign weights
retroactively after all interviews are complete. The weight must reflect the finding's value at
the moment it surfaces.

For each subject in the roster:

#### [S-nn] — Identity

[2–3 sentences: company type or context, relevant prior experience, at least one concrete concern
or known event. The identity must make the subject's pole assignment legible — a reader should
understand which axis pole this subject occupies from the Identity alone.]

Swap test: substitute another persona's name into this paragraph. If the interview answers would
still read as plausible, revise before writing the table.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn] | Answer (persona voice) | Evidence Signal [type: ...] | Impact Weight | Surprise? |
|-----|-----------------|------------------------|----------------------------|---------------|-----------|
| Q1  | [Question] [H-01] | [Answer — vocabulary and concerns drawn from Identity] | [risk: ...] / [preference: ...] / [constraint: ...] / [validation: ...] / [invalidation: ...] — [one-sentence signal] | H / M / L | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn] | | | H / M / L | |
| Q3  | [Question] [H-nn] | | | H / M / L | |

**Impact Weight rules:**
- H (High): finding materially changes the feature team's understanding of the problem space,
  adoption risk, or design constraint.
- M (Medium): relevant and informative but does not force a revision of assumptions.
- L (Low): confirms existing knowledge or is a weak signal.
- **All-identical weights fail.** At least two distinct weight values must appear across the
  full set of evidence rows.
- Assign at collection time — not retroactively.

**Table rules:**
- Every question cites at least one H-ID in brackets.
- Every answer fails the swap test — no other persona can be substituted and have the answer
  remain plausible.
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
- **CONFIRMED**: Evidence corroborated this hypothesis — at least one subject confirmed the
  expected pattern, belief, or behavior.
- **CHALLENGED**: Evidence partially contradicted this hypothesis — at least one answer conflicts
  with the stated assumption, but the hypothesis is not fully refuted.
- **FALSIFIED**: The exact Falsification Condition stated in STEP 1 was met. Cite the triggering
  row by Q-ID. The condition was observed, not inferred.
- **UNRESOLVED**: No interview question directly tested this hypothesis. Must state the reason
  explicitly. UNRESOLVED with no stated reason fails this table.

**Completion rules:**
- Every H-ID from STEP 1 must appear — no omissions.
- Each row requires a disposition label and at least one S-nn or Q-nn citation. Disposition
  without citation fails.
- UNRESOLVED without a stated reason fails.

**Gate**: STEP 4 (Cross-Subject Tensions Matrix) may not be written until this table is complete
and every H-ID carries a recorded disposition with evidence citation. Evaluator test: could the
Composite Signal section be populated without any H-ID having a recorded disposition? If yes,
this gate fails.

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after STEP 3.5 is complete (hypothesis register closed).

| Dimension [H-ID if applicable] | S-01 position | S-02 position | Tension or Agreement [explained] | Axis-predicted? | Unresolved? |
|--------------------------------|---------------|---------------|----------------------------------|-----------------|-------------|
| [topic / concern / H-ID / axis pole] | [S-01 view] | [S-02 view] | TENSION: [describe] / AGREEMENT: [what it signals] | Expected / Surprise | Yes / No |

**Completion rules:**
- Every row compares at least two subjects on a shared dimension.
- Agreement rows must explain why the agreement is meaningful given the Hypothesis Register
  and the STEP 0 opposition axis.
- At least one row records an open, unresolved tension. Leave it open.
- Note whether each tension or agreement was predicted by STEP 0 (expected) or was a surprise.

---

### STEP 5 — Composite Signal

This section synthesizes — it does not restate. If removing this section would leave the artifact
unchanged, the section has failed. The Composite Signal must add integrated judgment beyond what
a reader can derive from the Interview Tables and Tensions Matrix row by row.

Answer all three of the following in 4–6 sentences:

1. **Integrated verdict**: Does the overall evidence strengthen, weaken, or complicate the
   original SIGNAL hypothesis? State directly.

2. **Dominant finding**: What single finding across all subjects is most decision-relevant?
   Name the H-weight finding by Q-ID. Cite explicitly: "Q-nn from S-nn (H weight) is the
   primary driver because..."

3. **Key open question**: What is the most important thing these interviews did not resolve?
   What would the feature team need to do next?

**Impact Weight citation rule:** The composite must name at least one H-weight finding by Q-ID
and identify it as the highest-weight driver. Evaluator test: can an evaluator identify which
Q-ID drove the verdict and verify it carries H weight in the STEP 3 table? If not, revise.

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
| **Adjacent signal test** | Adjacent signal: [name a specific adjacent signal in the same namespace — e.g., "prove-prototype" or "scout-feasibility" — not a category label or placeholder]. Arc question applies equally: [yes / no] — because [state reason why the arc question's scope does or does not apply equally to the named adjacent signal]. Top-weight evidence check: [cite the H-weight Q-ID(s) from STEP 5 — the specific finding(s) named as the composite's primary driver]. Signal-specific: [yes / no] — because [state whether those H-weight finding(s) would be expected to arise in an interview about the named adjacent signal, and why. A finding is signal-specific if the adjacent signal's domain would not surface it; a finding is portable if both signals share the adoption or design dimension that produced it]. |

**Arc self-test verdict format:** Binary verdict — "yes" or "no" — followed immediately by a
stated rationale. Narrative without binary word fails. Binary without rationale fails. Evaluator
test: if a reviewer disagrees with the verdict, can they identify and challenge the specific
reason stated? If the rationale is too diffuse to be directly challenged, revise.

**Arc self-test rule**: the answer must be "yes." If "no," revise the arc inference.

**Adjacent signal test rules:**
- The named adjacent signal must be specific — not a category label or placeholder. "Another
  prove signal" fails; "prove-prototype" passes.
- The arc question applicability verdict must be binary (yes/no) with a stated reason.
- The top-weight evidence check must cite at least one Q-ID by ID. A generic reference to
  "high-weight findings" without a Q-ID fails C-25.
- The signal-specific verdict must be binary (yes/no) with a stated reason. The reason must
  address whether the specific named finding would arise in an interview about the named
  adjacent signal — not whether the arc question scope differs.
- Evaluator test (C-25): can an evaluator confirm that the H-weight Q-ID(s) driving the
  composite are tied to this signal's domain specifically, not portable to the adjacent signal?
  If no Q-ID is named in the adjacent signal test field, C-25 fails.

---

## Variation Summary

| Variation | Axis | C-22 | C-23 | C-24 | C-25 | Aspirational | Predicted Composite |
|-----------|------|------|------|------|------|--------------|---------------------|
| V-01 | Role Sequence: STEP 3.5 only | PASS | FAIL | FAIL | FAIL | 15/18 | 98.33 |
| V-02 | Output Format: four-field arc only | FAIL | PASS | FAIL | FAIL | 15/18 | 98.33 |
| V-03 | Lifecycle Emphasis: weight column only | FAIL | FAIL | PASS | FAIL | 15/18 | 98.33 |
| V-04 | C-23 + C-24 + C-25 (no C-22) | FAIL | PASS | PASS | PASS | 17/18 | 99.44 |
| V-05 | Full ceiling: C-22 + C-23 + C-24 + C-25 | PASS | PASS | PASS | PASS | 18/18 | 100.00 |

**Key test for R11:** V-04 confirms that C-25 composes with C-23 + C-24 without register closure
(C-22) as a structural mediator. If V-04 scores 17/18, then C-25 is independently composable
with its direct prerequisites. V-05 then stakes the full-ceiling claim with all four additions
active at non-overlapping structural locations.
