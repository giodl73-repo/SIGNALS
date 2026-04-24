# prove-interview — Rubric v11 Variations — Round 12

_Date: 2026-03-15 · Rubric: v11 (C-01–C-26) · Ceiling: 100_

---

## Context

R11 achieved 18/19 in V-05 under the v11 rubric (C-01–C-25 all PASS; C-26 FAIL). The V-05 R11
gap: STEP 3.5 closes the hypothesis register (every H-ID carries a disposition) and the Adjacent
Signal Test field names the H-weight Q-ID with a signal-specific verdict — but the artifact never
states which H-ID the H-weight Q-ID traces back to in the disposition register. The register is
closed; the cross-reference is made; the connection between them is absent. C-26 requires that
connection to be explicit. R12 goals:

1. **Single-axis 1** — Role Sequence: re-confirm C-22 isolated (STEP 3.5, no weight column, no
   fourth arc row). Gap isolation: C-23, C-24, C-25, C-26 absent. Expected: 15/19.
2. **Single-axis 2** — Output Format: re-confirm C-23 isolated (four-field arc table with Adjacent
   Signal Test row, no STEP 3.5, no weight column). Gap isolation: C-22, C-24, C-25, C-26 absent.
   Expected: 15/19.
3. **Single-axis 3** — Lifecycle Emphasis: re-confirm C-24 isolated (weight column + Q-ID citation
   rule, no STEP 3.5, no fourth arc row). Gap isolation: C-22, C-23, C-25, C-26 absent.
   Expected: 15/19.
4. **C-25 on minimal prereq (V-04 baseline)** — C-23 + C-24 + C-25, no C-22. Tests whether C-26
   fails by structural necessity (no register to receive the traceability mapping) when C-22 is
   absent. Expected: C-23/24/25 PASS, C-22/26 FAIL → 17/19.
5. **Full ceiling** — C-22 + C-23 + C-24 + C-25 + C-26 simultaneously. First variation targeting
   19/19. Single addition to R11 V-05: the Adjacent Signal Test field adds a Hypothesis
   Traceability statement mapping each H-weight Q-ID back to its H-ID in STEP 3.5 with a
   confirmed non-UNRESOLVED disposition.

**R11 scores re-scored under v11 (denominator /19):**

| Variation | C-22 | C-23 | C-24 | C-25 | C-26 | Aspirational | Composite |
|-----------|------|------|------|------|------|--------------|-----------|
| V-01 R11 (Role Sequence: C-22 isolated) | PASS | FAIL | FAIL | FAIL | FAIL | 15/19 | 98.16 |
| V-02 R11 (Output Format: C-23 isolated) | FAIL | PASS | FAIL | FAIL | FAIL | 15/19 | 98.16 |
| V-03 R11 (Lifecycle: C-24 isolated) | FAIL | FAIL | PASS | FAIL | FAIL | 15/19 | 98.16 |
| V-04 R11 (C-23 + C-24 + C-25, no C-22) | FAIL | PASS | PASS | PASS | FAIL | 17/19 | 98.95 |
| V-05 R11 (C-22 + C-23 + C-24 + C-25) | PASS | PASS | PASS | PASS | FAIL | 18/19 | 99.47 |

C-26 requires C-22 (register must exist and be closed) and C-25 (H-weight Q-ID must be named in
the adjacent signal test field) as structural preconditions. C-26 cannot pass in any variation
where either C-22 or C-25 is absent.

---

## Variation Axes

| Axis | R11 coverage | R12 focus |
|------|-------------|-----------|
| Role sequence (STEP 3.5) | V-01: C-22 isolated | Re-confirm C-22; establish 15/19 baseline |
| Output format (four-field arc table) | V-02: C-23 isolated | Re-confirm C-23; establish 15/19 baseline |
| Lifecycle emphasis (impact weight column) | V-03: C-24 isolated | Re-confirm C-24; establish 15/19 baseline |
| C-23 + C-24 + C-25 (no C-22) | V-04 R11 | Re-confirm C-26 FAIL when C-22 absent; 17/19 baseline |
| C-22 + C-23 + C-24 + C-25 + C-26 (full) | Not attempted in R11 | First 19/19 attempt |

---

## V-01 — Single axis: Role Sequence (STEP 3.5 Hypothesis Disposition; C-22 isolated)

**Axis:** Role sequence. Single addition to the R8 V-01 baseline: STEP 3.5 — Hypothesis
Disposition Table — inserted between STEP 3 (Interviews) and STEP 4 (Cross-Subject Tensions
Matrix). Closes the hypothesis register before synthesis: every H-ID receives a disposition label
and evidence citation before STEP 4 may begin.

No weight column — C-24 absent by design.
No fourth arc row — C-23 absent by design.
No C-25 — adjacent signal test field is absent, so no Q-ID cross-reference can exist.
No C-26 — C-22's register exists but is never connected to an adjacent signal test field.

**Hypothesis:** C-22 PASS (STEP 3.5 gate enforces disposition closure). C-23 FAIL (no adjacent
signal test row). C-24 FAIL (no Impact Weight column). C-25 FAIL (C-23 prerequisite missing).
C-26 FAIL (C-25 prerequisite missing — no adjacent signal test field in which to place the
traceability statement). Predicted: 15/19 → 98.16.

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
  type, answer pattern, or finding that would force rejection of that specific hypothesis.
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
  explicitly. UNRESOLVED with no stated reason fails this table.

**Completion rules:**
- Every H-ID from the STEP 1 register must appear — no omissions.
- Each row requires: (1) a disposition label, and (2) at least one evidence citation in S-nn or
  Q-nn format. Disposition without citation fails.
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

**Arc self-test verdict format:** Binary verdict — "yes" or "no" — followed immediately by a
stated rationale. Narrative without binary word fails. Binary without rationale fails.

**Arc self-test rule**: the answer must be "yes." If "no," revise the arc inference.

---

## V-02 — Single axis: Output Format (Four-Field Arc Table; C-23 isolated)

**Axis:** Output format. Single addition to the R8 V-01 baseline: the STEP 6 arc table gains a
fourth labeled row — "Adjacent signal test" — requiring a specific adjacent signal (not a
placeholder), a yes/no verdict on whether the arc question applies equally to the adjacent signal,
and a stated reason for that verdict.

No STEP 3.5 — C-22 absent by design.
No Impact Weight column — C-24 absent by design.
No C-25 — the adjacent signal test field is present but C-25 requires the field to cross-reference
H-weight Q-IDs from C-24's weight column, which does not exist here.
No C-26 — C-22 absent (no register to receive traceability mapping); C-25 also absent.

**Hypothesis:** C-22 FAIL (no STEP 3.5). C-23 PASS (four-field arc table with labeled Adjacent
Signal Test row: specific adjacent signal required, binary yes/no, stated reason). C-24 FAIL (no
Impact Weight column). C-25 FAIL (C-24 prerequisite missing). C-26 FAIL (C-22 and C-25
prerequisites both missing). Predicted: 15/19 → 98.16.

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
No C-25 — C-23 prerequisite missing; no field exists for a Q-ID cross-reference.
No C-26 — C-22 absent (no register); C-25 also absent (no adjacent signal test field).

**Hypothesis:** C-22 FAIL (no STEP 3.5). C-23 FAIL (no fourth arc row). C-24 PASS (weight column
with differentiation requirement and Q-ID citation rule in STEP 5). C-25 FAIL (C-23 prerequisite
absent). C-26 FAIL (C-22 and C-25 prerequisites both absent). Predicted: 15/19 → 98.16.

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

**Axis:** Output format + lifecycle emphasis — re-confirmation of R11 V-04. C-23 (four-field arc
table with Adjacent Signal Test row), C-24 (Impact Weight column, Q-ID citation rule), and C-25
(Adjacent Signal Test field cross-references H-weight Q-IDs with signal-specific verdict) are all
present. STEP 3.5 is absent.

C-26 FAIL by structural necessity: C-26 requires the H-weight Q-ID(s) in the adjacent signal test
field to map back to a specific H-ID in the hypothesis disposition register (STEP 3.5). When STEP
3.5 is absent, no register exists to receive the traceability mapping. The chain terminates at the
adjacent signal test field — the H-weight Q-ID floats without a declared hypothesis behind it.

**Hypothesis:** C-22 FAIL (no STEP 3.5). C-23 PASS (four-field arc table with Adjacent Signal
Test row). C-24 PASS (Impact Weight column with differentiation requirement and Q-ID citation
rule). C-25 PASS (adjacent signal test field names H-weight Q-IDs and states signal-specific
verdict with reason). C-26 FAIL (structural prerequisite C-22 absent — no hypothesis disposition
register to receive the Q-ID-to-H-ID traceability mapping). Predicted: 17/19 → 98.95.

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
- The top-weight evidence check must cite at least one Q-ID by ID. A generic reference to
  "high-weight findings" without a Q-ID fails C-25.
- The signal-specific verdict must be binary (yes/no) with a stated reason addressing whether
  the named finding would arise in an interview about the adjacent signal.
- Evaluator test (C-25): can an evaluator confirm that the H-weight Q-ID(s) driving the
  composite are tied to this signal's domain specifically, not portable to the adjacent signal?
  If no Q-ID is named in the adjacent signal test field, C-25 fails.

---

## V-05 — Full Ceiling: C-22 + C-23 + C-24 + C-25 + C-26 (19/19 target)

**Axis:** All five simultaneously. Built on R11 V-05 (C-22 + C-23 + C-24 + C-25, 18/19), with a
single addition to the Adjacent Signal Test row: a Hypothesis Traceability statement that
explicitly maps each H-weight Q-ID named in the adjacent signal test field back to its H-ID entry
in the STEP 3.5 disposition register, confirming the disposition is CONFIRMED, CHALLENGED, or
FALSIFIED — UNRESOLVED fails.

**Structural locations of the five additions:**
- STEP 3.5 (between STEP 3 and STEP 4) — C-22
- Impact Weight column in STEP 3 tables + Q-ID citation rule in STEP 5 — C-24
- Fourth row in STEP 6 arc table ("Adjacent signal test") — C-23
- Extension of Adjacent Signal Test row: H-weight Q-ID cross-reference with signal-specific
  verdict — C-25
- Extension of Adjacent Signal Test row: Hypothesis Traceability statement mapping H-weight
  Q-IDs to H-IDs in STEP 3.5 with confirmed non-UNRESOLVED dispositions — C-26

All five additions operate at non-overlapping structural locations. C-26 reads across STEP 3.5
(the register) and STEP 6 (the adjacent signal test field), making the Q-ID-to-H-ID connection
explicit as an artifact-level claim rather than requiring evaluator inference.

**Hypothesis:** C-22 PASS (STEP 3.5 closes register before synthesis). C-23 PASS (four-field arc
table with labeled Adjacent Signal Test row). C-24 PASS (Impact Weight column with H-weight Q-ID
citation in STEP 5). C-25 PASS (Adjacent Signal Test field names H-weight Q-IDs with
signal-specific verdict and reason). C-26 PASS (Adjacent Signal Test field contains explicit
Hypothesis Traceability statement mapping each H-weight Q-ID to a specific H-ID in STEP 3.5 with
a non-UNRESOLVED disposition). Predicted: 19/19 → 100.00.

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
- Each row requires: (1) a disposition label, and (2) at least one S-nn or Q-nn citation.
  Disposition without citation fails.
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
| **Adjacent signal test** | Adjacent signal: [name a specific adjacent signal in the same namespace — e.g., "prove-prototype" or "scout-feasibility" — not a category label or placeholder]. Arc question applies equally: [yes / no] — because [state reason why the arc question's scope does or does not apply equally to the named adjacent signal]. Top-weight evidence check: [cite the H-weight Q-ID(s) from STEP 5 — the specific finding(s) named as the composite's primary driver]. Signal-specific: [yes / no] — because [state whether those H-weight finding(s) would be expected to arise in an interview about the named adjacent signal, and why. A finding is signal-specific if the adjacent signal's domain would not surface it; a finding is portable if both signals share the adoption or design dimension that produced it]. Hypothesis traceability: [for each H-weight Q-ID cited above, state its H-ID mapping and confirmed disposition from STEP 3.5 — e.g., "Q-03 supports H-02 [CONFIRMED]" or "Q-05 challenges H-01 [CHALLENGED]"]. |

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
- **Hypothesis traceability**: every H-weight Q-ID cited in this field must be explicitly mapped
  to a specific H-ID entry in the STEP 3.5 disposition register. The mapping must appear as an
  explicit statement — e.g., "Q-03 supports H-02 [CONFIRMED]" — not as inference from proximity
  or shared numbering. The H-ID's disposition in STEP 3.5 must be CONFIRMED, CHALLENGED, or
  FALSIFIED; a traceability statement pointing to an UNRESOLVED H-ID fails. Evaluator test
  (C-26): starting from the H-weight Q-ID(s) named in this field, can an evaluator follow an
  explicit reference to a specific H-ID entry in STEP 3.5 and confirm its disposition is not
  UNRESOLVED? If no mapping is stated, or if the associated H-ID disposition is UNRESOLVED,
  C-26 fails.

---

## Variation Summary

| Variation | Axis | C-22 | C-23 | C-24 | C-25 | C-26 | Aspirational | Predicted Composite |
|-----------|------|------|------|------|------|------|--------------|---------------------|
| V-01 | Role Sequence: STEP 3.5 only | PASS | FAIL | FAIL | FAIL | FAIL | 15/19 | 98.16 |
| V-02 | Output Format: four-field arc only | FAIL | PASS | FAIL | FAIL | FAIL | 15/19 | 98.16 |
| V-03 | Lifecycle Emphasis: weight column only | FAIL | FAIL | PASS | FAIL | FAIL | 15/19 | 98.16 |
| V-04 | C-23 + C-24 + C-25 (no C-22) | FAIL | PASS | PASS | PASS | FAIL | 17/19 | 98.95 |
| V-05 | Full ceiling: C-22 + C-23 + C-24 + C-25 + C-26 | PASS | PASS | PASS | PASS | PASS | 19/19 | 100.00 |

**Key test for R12:** V-04 re-confirms that C-26 FAIL is structural when C-22 is absent — the
H-weight Q-ID in the adjacent signal test field cannot be traced to an H-ID with a resolved
disposition when no disposition register exists. V-05 stakes the full-ceiling claim: a single
Hypothesis Traceability statement added to the Adjacent Signal Test row, connecting the H-weight
Q-ID named in C-25's cross-reference back to its H-ID entry in STEP 3.5 with a non-UNRESOLVED
disposition, closes the last open link in the evidence chain.

**The full chain V-05 makes verifiable:** declared hypothesis [H-nn] -> collected evidence with
weight [Q-nn: H weight] -> register closure [H-nn: CONFIRMED/CHALLENGED/FALSIFIED, evidence
Q-nn] -> composite [Q-nn cited as highest-weight driver] -> arc cross-reference [Q-nn verified
as signal-specific] -> traceability statement [Q-nn -> H-nn {DISPOSITION}]. Each link was
individually inspectable under v10 and v11. C-26 makes the complete chain verifiable as a single
explicit claim.
