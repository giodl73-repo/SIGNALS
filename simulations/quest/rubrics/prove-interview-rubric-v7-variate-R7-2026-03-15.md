# prove-interview — Rubric v7 Variations — Round 7

_Date: 2026-03-15 · Rubric: v7 (C-01–C-20) · Ceiling: 100_

---

## Context

Round 6 produced 3 variations scored against the v7 rubric (C-01–C-20). V-01 and V-02 scored
97.69; V-03 scored 96.92. The v7 rubric adds two new aspirational criteria:

- **C-19** — Opposition axis declared as a named structural step before hypothesis formation
- **C-20** — Evaluator test embedded within the arc signal section

Aspirational denominator: 13. Each criterion worth approximately 0.769 points. Ceiling stays 100.

**R6 coverage gaps for C-18, C-19, C-20:**

| Variation | C-18 | C-19 | C-20 | Aspirational | Composite |
|-----------|------|------|------|--------------|-----------|
| V-01 R6 (Role Sequence: STEP 0) | FAIL | PASS | FAIL | 10/13 | 97.69 |
| V-02 R6 (Output Format: Arc Signal) | FAIL | FAIL | PASS | 10/13 | 97.69 |
| V-03 R6 (Phrasing Register) | FAIL | FAIL | FAIL | 9/13 | 96.92 |

Round 7 goals:
1. Three single-axis variations:
   - Role Sequence — extend V-01 R6 with arc section + embedded self-test (targeting C-20 while
     retaining C-19 from STEP 0; C-18 absent as gap isolation test)
   - Output Format — extend V-02 R6 with STEP 0 opposition declaration (targeting C-19 while
     retaining C-20 from arc self-test; C-18 absent as gap isolation test)
   - Lifecycle Emphasis — phase-gated protocol targeting all three gaps simultaneously (C-18 via
     universal quality gate, C-19 via named Phase 0, C-20 via arc self-test in Phase 3)
2. Two combination variations: Role Sequence + Lifecycle (full STEP structure with quality gate +
   arc self-test); Inertia Framing + Full Coverage (inertia-first ordering with all three gaps)
3. Each single-axis variation leaves at least one gap to isolate the contribution of the axis

---

## Variation Axes

| Axis | R6 result | R7 focus |
|------|-----------|----------|
| Role sequence | V-01 C-19 PASS, C-20 FAIL (no arc section) | Add STEP 6 arc section with embedded 3-field self-test table |
| Output format | V-02 C-20 PASS, C-19 FAIL (no named opposition step) | Add STEP 0 opposition declaration as named step before STEP 1 |
| Lifecycle emphasis | ABSENT in all R6 actual variations | Phase-gated protocol with per-hypothesis quality gate (C-18) |
| Phrasing register | V-03 — structural limits confirmed (C-12, C-18 fail) | NOT retried — confirmed limitation |
| Inertia framing | NOT in R6 actual variations | Full combination with inertia-first ordering |

---

## V-01 — Single axis: Role Sequence (STEP 0 + STEP 6 Arc Self-Test)

**Axis:** The role-sequence structure now spans STEP 0 through STEP 6. STEP 0 (Opposition Axis
Declaration) gates the Hypothesis Register — unchanged from V-01 R6. STEP 6 is added: a
mandatory Arc Signal section with a three-field table requiring `Arc question`, `Arc inference`,
and `Arc self-test`. The self-test is a required field the author fills with a yes/no answer and
a stated reason — not a note embedded in instructions. Everything between STEP 0 and STEP 6
follows V-01 R6 exactly. C-18 is NOT addressed: the hypothesis register gate retains the
"at least one" condition from V-01 R6.

**Hypothesis:** Adding STEP 6 with a required `Arc self-test` field satisfies C-20 by construction
— the test and author-supplied answer appear in the artifact body, not in instructions. C-17
passes by cascade (C-20 → C-17). STEP 0 carries C-19 PASS from R6. C-16 passes by cascade from
C-19. C-18 remains absent (single-axis test: only the role-sequence arc step changes; gate quality
not modified). Predicted: C-19 PASS, C-20 PASS, C-18 FAIL. Aspirational 12/13. Composite 99.23.

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
- At least one hypothesis must have a non-empty Falsification Condition naming the specific answer
  type or evidence that would force rejection. "If most people disagree" fails.
- Register is locked once written.

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
| Q1  | [Question] [H-01] | [Answer — vocabulary and concerns drawn from Identity] | [risk: …] / [preference: …] / [constraint: …] / [validation: …] / [invalidation: …] — [one-sentence signal] | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn] |                                                        |                                                                                       |                                  |
| Q3  | [Question] [H-nn] |                                                        |                                                                                       |                                  |

**Table rules:**
- Every question cites at least one H-ID in brackets.
- Every answer fails the swap test — no other persona can be substituted and have the answer
  remain plausible. Generic answers that could belong to any persona fail.
- Every Evidence Signal carries a type tag followed by a one-sentence signal interpretation.
- At least one "Yes" in the Surprise column per subject, with explanation of expected vs. found.
- Minimum 3 rows per subject.

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after all subject tables are complete.

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

Cite subjects by ID (S-01, S-02) and hypothesis IDs (H-nn) where relevant.

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

## V-02 — Single axis: Output Format (STEP 0 + Retained Arc Self-Test)

**Axis:** The output format now has two anchoring structural sections — one at the start
(STEP 0: Opposition Axis Declaration, added in R7) and one at the end (STEP 6: Arc Signal with
embedded self-test, carried from V-02 R6). STEP 0 is added as a named structural step before
the Hypothesis Register, satisfying C-19 by construction. STEP 6's three-field table — arc
question, arc inference, scope test — is retained unchanged from V-02 R6, which already achieved
C-20. C-18 is NOT addressed: the hypothesis register gate retains the "at least one" condition.

**Hypothesis:** STEP 0 forces C-19 PASS: it is a labeled, numbered step placed before STEP 1
(Hypothesis Register) — the evaluator test (could the hypothesis register be populated without
the opposition declaration step?) answers "no" by construction. STEP 6 arc self-test carries
C-20 PASS from V-02 R6. C-16 passes by cascade (C-19 → C-16). C-18 remains absent. Predicted:
C-19 PASS, C-20 PASS, C-18 FAIL. Aspirational 12/13. Composite 99.23.

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

This step is written before the Hypothesis Register. It is a structural prerequisite: STEP 1
cannot begin until this step is complete.

Name the epistemic tension axis your subject selection will span. This declaration is not a
persona introduction — it is a design choice that precedes subject selection.

| Field | Declaration |
|-------|-------------|
| **Axis name** | [Name the epistemic dimension — e.g., "incumbent workflow investment vs. modernization appetite" / "operational risk tolerance vs. capability acquisition drive"] |
| **Axis relevance to {SIGNAL}** | [One sentence: why hearing from subjects at opposite poles of this axis produces more informative evidence for {SIGNAL} than hearing from subjects at the same pole. Name what evidence requires two poles.] |
| **Pole A — resistant / skeptical** | [Who occupies this pole? What prior investment or belief does a subject here hold? What would {SIGNAL} cost or threaten for them?] |
| **Pole B — receptive / innovative** | [Who occupies this pole? What does a subject here want or lack that {SIGNAL} could provide?] |
| **Evidence gap without Pole B** | [Name a specific finding type that a Pole A interview alone could not produce. "A different perspective" fails — state the specific evidence type.] |

**Gate rule**: STEP 1 may not be written until this table is complete and both poles are described
at genuinely opposite ends of the named axis. A demographic axis (age, company size, geography)
does not satisfy the gate — the axis must be epistemic.

---

### STEP 1 — Hypothesis Register

Write this register before any interview question or persona answer. The register is locked once
written. No question may reference a hypothesis not listed here.

| ID   | Hypothesis                                               | Category                    | Falsification Condition                                                      |
|------|----------------------------------------------------------|-----------------------------|------------------------------------------------------------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL] | assumption / risk / unknown | [what a subject would have to say to force rejection — name the answer type] |
| H-02 | [a specific risk or concern you expect to surface]       | risk                        | [what answer would show this risk does not apply]                            |
| H-03 | [a design question these interviews should resolve]      | unknown                     | [what finding would resolve this against your expectation]                   |
| H-04 | [add additional hypotheses — aim for at least 4]         |                             |                                                                              |

**Register rules:**
- Minimum 4 hypotheses.
- At least one hypothesis must have a non-empty, specific Falsification Condition.
- Register is locked once written. Do not revise after any interview table row is written.

---

### STEP 2 — Human Subjects Roster

Assign each subject to a pole from STEP 0 before writing their background. A subject who cannot
be assigned to a declared pole has no design rationale for this run — replace them.

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)   | Domain Expertise | Key Concern                                                    |
|------|--------|--------|-----------|----------------------|------------------|----------------------------------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B      | [Domain]         | [What this persona is most likely to push back on or champion] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B      | [Domain]         | [Key concern meaningfully distinct from S-01]                  |

Minimum 2 subjects with one subject from each declared pole.

---

### STEP 3 — Interviews

**Do not write any interview table row until Steps 0, 1, and 2 are complete.**

For each subject in the roster:

#### [S-nn] — Identity

[2–3 sentences: company type or context, relevant prior experience, at least one concrete concern
or known event that makes this persona specific. Identity must make pole assignment legible.]

Swap test: substitute another persona's name into this paragraph. If the interview answers would
still read as plausible, revise before writing the table.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn]   | Answer (persona voice)                                 | Evidence Signal [type: ...]                                                           | Surprise?                        |
|-----|-------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------|----------------------------------|
| Q1  | [Question] [H-01] | [Answer — vocabulary and concerns drawn from Identity] | [risk: …] / [preference: …] / [constraint: …] / [validation: …] / [invalidation: …] — [one-sentence signal] | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn] |                                                        |                                                                                       |                                  |
| Q3  | [Question] [H-nn] |                                                        |                                                                                       |                                  |

**Table rules:**
- Every question cites at least one H-ID in brackets.
- Every answer fails the swap test.
- Every Evidence Signal carries a type tag followed by a one-sentence signal interpretation.
- At least one "Yes" in the Surprise column per subject with explanation.
- Minimum 3 rows per subject.

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after all subject tables are complete.

| Dimension [H-ID if applicable]  | S-01 position | S-02 position | Tension or Agreement [explained]                    | Unresolved? |
|---------------------------------|---------------|---------------|-----------------------------------------------------|-------------|
| [topic / concern / H-ID]        | [S-01 view]   | [S-02 view]   | TENSION: [describe] / AGREEMENT: [what it signals]  | Yes / No    |

Completion rules:
- At least one unresolved tension row.
- Agreement rows explain why the agreement matters or is surprising given the axis declared in STEP 0.

---

### STEP 5 — Composite Signal

This section synthesizes — it does not restate. If removing this section would leave the artifact
unchanged, the section has failed.

Answer all three of the following in 4–6 sentences:

1. **Integrated verdict**: Does the evidence strengthen, weaken, or complicate the original
   SIGNAL hypothesis? State directly.
2. **Dominant finding**: What single finding is most decision-relevant? Name it specifically.
3. **Key open question**: What did these interviews not resolve? What would the feature team
   need to do next?

---

### STEP 6 — Arc Signal

**Write this section after the Composite Signal. It is required. It must not restate
feature-level conclusions from STEP 5.**

The Arc Signal answers a question whose scope is wider than {SIGNAL} — what this interview run
reveals about the adoption pattern, the workflow category, or the class of features {SIGNAL}
belongs to.

| Field | Content |
|-------|---------|
| **Arc question** | [State an explicit question whose scope exceeds {SIGNAL}. Scope test: if the same arc question could only be answered by studying {SIGNAL} specifically, it fails. If a different but adjacent signal in the same category would generate the same arc question, scope is arc-level.] |
| **Arc inference** | [State a conclusion that answers the arc question and that a reader could not reconstruct by reading the Composite Signal alone. Points beyond this specific feature to a pattern about adoption, the workflow, or the user type.] |
| **Arc scope confirmation and self-test** | Adjacent signal substitution: [name an adjacent signal and state whether the arc question applies to it equally — yes = arc-level scope, no = revise]. Removal test: if this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state the specific reason]. |

**Self-test rule**: the removal test answer must be "yes." An arc inference answerable "no" has
not cleared feature scope — revise before treating STEP 6 as complete.

**Anti-restatement test**: if removing the entire Arc Signal section would leave the feature
team with everything they need to decide about {SIGNAL}, the Arc Signal has not elevated the
synthesis. Revise until removal costs something they cannot reconstruct.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-03 — Single axis: Lifecycle Emphasis (Phase-Gated Protocol)

**Axis:** A four-phase sequential protocol where each phase has a structurally stated gate
condition. Phase 0 is the opposition axis declaration (C-19: named structural phase before
hypothesis formation). Phase 1 contains the hypothesis set with a universal quality-conditional
gate (C-18: each H-ID must carry a falsification condition before Phase 2 begins — not "at least
one"). Phase 2 contains interviews with H-IDs as a structural pre-commit column (C-12). Phase 3
contains cross-subject analysis and an arc signal section with embedded self-test field (C-20).

**Hypothesis:** The lifecycle axis produces all three gap criteria simultaneously:
- Phase 0 as a named structural phase that gates Phase 1 satisfies C-19 by construction.
- The Phase 1 gate sentence "each declared hypothesis must carry a specific falsification
  condition before Phase 2 may begin" satisfies C-18 by construction — an author cannot
  advance with even one hypothesis lacking a falsification condition.
- Phase 3's required arc self-test field with author-supplied answer satisfies C-20 by
  construction. C-12 is addressed via the H-IDs tested column in Phase 2.
Predicted: C-18 PASS, C-19 PASS, C-20 PASS, C-12 PASS. Aspirational 13/13. Composite 100.00.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

This skill runs in four sequential phases. Each phase is explicitly gated — a phase is not
complete until its stated gate condition is satisfied, and the following phase may not begin
until the prior phase gate is cleared. Phase gates are structural rules, not implied by
numbering.

---

### PHASE 0 — Opposition Axis Declaration

**Write this phase before declaring any hypothesis, selecting any subject, or writing any
interview question. Phase 1 may not begin until Phase 0 is complete.**

This phase answers: why will hearing from subjects at opposite poles of a relevant epistemic
tension axis produce more valuable evidence than hearing from subjects who occupy the same pole?

#### Opposition Axis Table

| Field | Declaration |
|-------|-------------|
| **Axis name** | [Name the epistemic tension axis — a dimension of belief, practice, or investment. Not demographic.] |
| **Axis relevance to {SIGNAL}** | [Why tension on this axis is more informative than agreement for {SIGNAL}. What specific evidence requires hearing from both poles?] |
| **Pole A — skeptical / resistant** | [Who occupies this pole? What have they invested in or built that {SIGNAL} would disrupt? What adoption cost do they carry?] |
| **Pole B — receptive / innovative** | [Who occupies this pole? What adoption motivation do they carry that Pole A subjects lack?] |
| **Evidence requiring Pole B** | [Name the specific finding type that a Pole A-only interview cannot produce. Name it precisely — not "a different view."] |

**Phase 0 gate — opposition axis is complete when:**
1. The axis is named as an epistemic dimension (not demographic)
2. Pole A and Pole B are genuine opposites on the named axis, not variations of the same position
3. The evidence requiring Pole B names a specific finding type, not a general perspective

**Phase 1 may not begin until all three Phase 0 gate conditions are satisfied.**

---

### PHASE 1 — Hypothesis Set

Write the hypothesis set before any interview question or persona answer. Committed once written.

**Signal under investigation:** {SIGNAL}
**Topic context:** {TOPIC}

#### Hypothesis Register

Declare every assumption, belief, and risk you carry into these interviews. Label each H-01,
H-02, etc. Aim for at least 4 hypotheses.

| ID   | Hypothesis                                                          | Category                    | Falsification Condition (specific — name the evidence type or answer pattern)         |
|------|---------------------------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------------|
| H-01 | [belief about how stakeholders at each pole will respond to SIGNAL] | assumption / risk / unknown | [what a subject would have to say — name the answer type, not general disagreement]   |
| H-02 | [specific risk or concern expected to surface]                      | risk                        | [what interview answer would show this risk does not apply or is overstated]          |
| H-03 | [design question these interviews should resolve]                   | unknown                     | [what finding would resolve this against your expectation]                            |
| H-04 | [add rows — aim for 4+]                                             |                             |                                                                                       |

**Phase 1 gate — universal falsifiability condition:**

Phase 1 is not complete until **each and every declared hypothesis** carries a specific,
non-trivial falsification condition. This is not an "at least one" gate. The gate condition
is: every H-ID row has a non-empty Falsification Condition that names the evidence type or
answer pattern that would force rejection. A condition that reads "if people generally disagree"
or "if most subjects object" does not satisfy the gate for that H-ID.

**Evaluator test**: could an author satisfy the gate by writing four hypotheses with no
falsification conditions and still advance to Phase 2? If yes, the gate fails C-18. The gate
is only satisfied when no H-ID has an empty or generic falsification condition.

**Phase 2 may not begin while any H-ID has an unsatisfied falsification condition.**

#### Subject Roster

Each subject must be assigned to a pole declared in Phase 0 before their background is written.

| ID   | Name   | Role   | Seniority | Axis Pole (Phase 0)   | H-IDs this subject primarily tests                                          |
|------|--------|--------|-----------|-----------------------|-----------------------------------------------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B       | [H-IDs from the register that this subject's position is best positioned to test] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B       | [H-IDs meaningfully different from S-01's assignment]                      |

Minimum 2 subjects, one from each declared pole. A subject not assignable to a declared pole
does not belong in this run — replace before advancing.

**Phase 1 complete when:** every H-ID has a specific falsification condition AND the
axis-assigned roster is written. Both conditions must be satisfied before Phase 2 begins.

---

### PHASE 2 — Interviews

**Phase 2 may not begin until Phase 1 is complete.** Complete one subject in full (Identity,
Interview Table, Evidence Extraction) before beginning the next subject.

For each subject in the Phase 1 roster:

#### [S-nn] — Identity

[2–3 sentences: company type or domain context, relevant prior experience, at least one concrete
concern or known prior event. The identity must make the axis pole assignment legible — a reader
should understand which pole this subject occupies from the Identity alone.]

Identity test: substitute another persona's name. If the interview answers would still read as
plausible, add specifics until the answer is no.

#### [S-nn] — Interview Table

The "H-IDs tested" column is filled before writing each question. A question may not be written
without a completed H-IDs column for that row.

| Q#  | H-IDs tested | Question (cites H-IDs above)                                        | Answer (persona voice — vocabulary from Identity)               | Evidence Signal [type: …] — one-sentence signal                      | Surprise?                          |
|-----|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------|
| Q1  | H-nn         | [Question targeting listed H-IDs]                                   | [Answer in persona's specific voice and concerns]               | [risk / preference / constraint / validation / invalidation]: [signal] | Yes — expected [X], found [Y] / No |
| Q2  | H-nn         |                                                                     |                                                                 |                                                                      |                                    |
| Q3  | H-nn         |                                                                     |                                                                 |                                                                      |                                    |

**Table rules:**
- The "H-IDs tested" column must be filled before writing the question in that row.
- Every Evidence Signal carries a type tag and a one-sentence signal interpretation.
- Answers fail the swap test — another persona's name cannot be substituted and have the answer
  remain plausible.
- At least one "Yes" in the Surprise column per subject, with explanation of expected vs. found.
- Minimum 3 rows per subject.

When a Phase 1 falsification condition is triggered, mark it inline:
> **[FALSIFICATION — H-nn triggered]:** Condition stated: [exact condition]. Subject said:
> [answer]. Conclusion: [how this forces revision of H-nn].

#### [S-nn] — Evidence Extraction

Extract 3–5 decision-relevant findings from this subject. A finding must be specific enough
that a feature team could act on it. A finding that could come from any persona fails.

1. [finding — specific to this subject's role, pole, and stated concerns]
2. [finding]
3. [finding]

**Phase 2 is complete when all subjects in the roster have written Identity, Interview Table,
and Evidence Extraction. Phase 3 may not begin until Phase 2 is complete.**

---

### PHASE 3 — Cross-Subject Analysis and Synthesis

**Phase 3 may not begin until Phase 2 is complete.**

#### Hypothesis Test Table

| H-ID | Hypothesis (brief)                 | S-01 response                              | S-02 response                              | Falsification triggered?     | Verdict                              |
|------|------------------------------------|--------------------------------------------|--------------------------------------------|------------------------------|--------------------------------------|
| H-01 | [text]                             | [how S-01's interview addressed this]      | [how S-02's interview addressed this]      | Yes / No / Partial           | Confirmed / Contradicted / Split / Untested |
| H-02 | [text]                             |                                            |                                            |                              |                                      |

Every H-ID from Phase 1 must appear here. An untested H-ID is a finding about coverage gaps.

#### Cross-Subject Tensions Table

| Dimension [H-ID / axis pole]         | S-01 position        | S-02 position        | Tension or Agreement                              | Axis-predicted?  | Open signal? |
|--------------------------------------|----------------------|----------------------|---------------------------------------------------|------------------|--------------|
| [topic / H-ID / axis pole dimension] | [S-01 stated position] | [S-02 stated position] | TENSION: [describe] / AGREEMENT: [why it matters] | Expected / Surprise | Yes / No |

Completion rules:
- At least one unresolved tension row. Do not resolve it.
- Agreement rows state why agreement matters given the Phase 0 opposition axis.
- Note whether each tension was predicted by the axis or was a surprise.

#### Composite Signal

**Synthesis gate**: this section is not complete if removing it would leave the artifact's
conclusions unchanged. A Composite Signal that restates per-subject findings without integration
does not satisfy this gate.

Write 4–6 sentences answering all four:

1. **Signal verdict**: Does the Phase 1 signal hypothesis come out strengthened, weakened, or
   complicated? State directly.
2. **Falsification result**: Were any Phase 1 falsification conditions triggered? If yes, what
   must the team revise? If no, what does the absence of triggers signal?
3. **Dominant finding**: What single finding across all subjects is most decision-relevant?
   Name it — not a theme.
4. **Axis verdict**: Did the Phase 0 opposition axis produce the expected tension, or did
   subjects converge unexpectedly? What does the convergence or divergence signal for the feature?

#### Arc Signal

**Write this section after the Composite Signal. It is required. It must not restate
feature-level conclusions from the Composite Signal.**

The Arc Signal answers a question whose scope is wider than {SIGNAL} — what this interview run
reveals about the adoption pattern, the workflow category, or the class of features {SIGNAL}
belongs to.

| Field | Content |
|-------|---------|
| **Arc question** | [State an explicit question wider than {SIGNAL}. Scope test: would a different but adjacent signal generate the same arc question? If yes, the scope is arc-level. If the arc question would need to change for the adjacent signal, it is still feature-scoped — revise.] |
| **Arc inference** | [State a conclusion that answers the arc question. A reader must not be able to reconstruct this inference from the Composite Signal alone. The inference points to a pattern about adoption, the workflow, or the user type beyond this specific feature.] |
| **Arc self-test** | Adjacent signal: [name one adjacent signal]. Arc question applies to it: [yes / no]. If yes, scope is confirmed arc-level. — Removal test: if this arc inference were removed from the artifact, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state the specific reason: what this arc inference provides that per-subject findings and the Composite Signal do not]. |

**Self-test rule**: the removal test answer must be "yes." An arc inference the team can do
without is not arc-level — revise the inference until removing it genuinely costs the feature
team information they cannot reconstruct.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-04 — Combination: Role Sequence + Lifecycle Emphasis

**Axes:** STEP-based structure (from Role Sequence) combined with quality-conditional phase gates
(from Lifecycle Emphasis). STEP 0 is the opposition axis declaration (C-19). STEP 1's gate
sentence requires each H-ID to carry a falsification condition (C-18 — not "at least one").
H-IDs are a structural pre-commit column in STEP 3 interview tables (C-12). STEP 6 arc section
contains the three-field table including the required self-test with author-supplied answer (C-20).

**Hypothesis:** The combination produces C-19, C-18, C-12, and C-20 by construction, achieving
all 13 aspirational criteria simultaneously. C-19 from STEP 0 named structural step before
STEP 1. C-18 from "each hypothesis" gate in STEP 1. C-12 from the H-IDs tested pre-commit
column in STEP 3 interview tables. C-20 from the mandatory self-test field in STEP 6.
All prior-round strengths (C-08 through C-17) carried forward. Predicted: 13/13. Composite 100.00.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Simulate stakeholder or customer interviews about this topic. The interviews are not real — but
every persona answer must be anchored in the persona's documented identity, expertise, and prior
experience. This skill runs through six structured steps. Each step with a gate cannot be left
incomplete — the stated gate condition must be satisfied before the following step begins.

---

### STEP 0 — Opposition Axis Declaration

**This step must be completed before STEP 1 begins.**

Declare the epistemic tension axis your subject selection will span. This declaration shapes
hypothesis formation — hypotheses written before the axis is declared cannot be opposition-aware.

| Field | Declaration |
|-------|-------------|
| **Axis name** | [Name the epistemic tension axis — a dimension of belief, practice, or investment relevant to {SIGNAL}. Must be epistemic, not demographic.] |
| **Why this axis for {SIGNAL}** | [One sentence: why tension on this axis produces more informative evidence than agreement. What question about {SIGNAL} requires both poles?] |
| **Pole A — skeptical / resistant** | [Who occupies this pole? What investment or belief do they hold that {SIGNAL} would cost or threaten?] |
| **Pole B — receptive / innovative** | [Who occupies this pole? What adoption motivation or capability gap do they carry?] |
| **Evidence requiring Pole B** | [Specific finding type that a Pole A interview alone cannot produce — not "a different view."] |

**STEP 0 gate**: STEP 1 may not begin until both poles are described at genuinely opposite ends
of a named epistemic axis and the evidence requiring Pole B is specific. A demographic axis does
not satisfy this gate.

---

### STEP 1 — Hypothesis Register

Write before any interview question or persona answer. Locked once written.

| ID   | Hypothesis                                                   | Category                    | Falsification Condition                                                                    |
|------|--------------------------------------------------------------|-----------------------------|--------------------------------------------------------------------------------------------|
| H-01 | [belief about how subjects at each axis pole respond to {SIGNAL}] | assumption / risk / unknown | [what a subject would have to say — name the specific evidence type or answer pattern] |
| H-02 | [specific risk or concern expected from Pole A subjects]     | risk                        | [what answer would show this risk is inapplicable or overstated]                           |
| H-03 | [design question the interviews should resolve]              | unknown                     | [what finding would resolve this against expectation]                                      |
| H-04 | [add rows — aim for at least 4]                              |                             |                                                                                            |

**STEP 1 gate — universal falsifiability:**

STEP 1 is not complete until **each declared hypothesis** carries a specific, non-trivial
Falsification Condition. This gate requires every H-ID to have a named, testable falsification
condition. A blank Falsification Condition for any H-ID means STEP 1 is not complete for that
H-ID. A condition that reads "if most people disagree" or "if objections arise" does not pass
the gate — state the specific answer type or evidence that would force rejection.

**STEP 2 may not begin while any H-ID has an empty or generic Falsification Condition.**

---

### STEP 2 — Human Subjects Roster

Assign each subject to a pole from STEP 0 before writing their background.

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)  | Domain Marker                                             | H-IDs this subject primarily tests |
|------|--------|--------|-----------|---------------------|-----------------------------------------------------------|------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B     | [specific expertise or investment grounding their pole]   | [H-IDs from register]              |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B     | [expertise distinct from S-01 grounding their pole]       | [H-IDs — different from S-01's]    |

Minimum 2 subjects, one from each declared pole. A subject not assignable to a declared pole
does not belong in this run.

---

### STEP 3 — Interviews

**Do not write any interview row until Steps 0, 1, and 2 are complete.**

For each subject in the STEP 2 roster:

#### [S-nn] — Identity

[2–3 sentences: company type or context, relevant prior experience, at least one concrete concern
or known event. The identity must make the subject's pole assignment legible from the text alone.]

Swap test: substitute another persona's name. If the interview answers would still read as
plausible, add specifics until the answer is no.

#### [S-nn] — Interview Table

Fill the "H-IDs tested" column before writing each question in that row. A question row with a
blank H-IDs column may not be written.

| Q#  | H-IDs tested | Question                                             | Answer (persona voice)                                     | Evidence Signal [type: …] — one-sentence signal                    | Surprise?                           |
|-----|--------------|------------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------|
| Q1  | H-nn         | [Question targeting listed H-IDs]                    | [Answer — vocabulary and concerns drawn from Identity]     | [risk / preference / constraint / validation / invalidation]: […] | Yes — expected [X], found [Y] / No  |
| Q2  | H-nn         |                                                      |                                                            |                                                                    |                                     |
| Q3  | H-nn         |                                                      |                                                            |                                                                    |                                     |

**Table rules:**
- "H-IDs tested" column is a pre-commit structural anchor — fill it before writing the question.
- Every answer fails the swap test.
- Every Evidence Signal carries a type tag and a one-sentence signal interpretation.
- At least one "Yes" in the Surprise column per subject, with explanation.
- Minimum 3 rows per subject.

When a Falsification Condition from STEP 1 is triggered:
> **[FALSIFICATION — H-nn]:** Condition: [exact text from STEP 1]. Subject said: [answer].
> Conclusion: [how this forces revision].

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after all STEP 3 tables are complete.

| Dimension [H-ID / axis pole]     | S-01 position     | S-02 position     | Tension or Agreement [explained]                    | Axis-predicted?     | Unresolved? |
|----------------------------------|-------------------|-------------------|-----------------------------------------------------|---------------------|-------------|
| [topic / H-ID / axis dimension]  | [S-01 view]       | [S-02 view]       | TENSION: [describe] / AGREEMENT: [why it matters]   | Expected / Surprise | Yes / No    |

Completion rules:
- At least one unresolved tension row. Do not resolve it.
- Agreement rows explain why the agreement is meaningful given the STEP 0 axis and STEP 1 hypotheses.
- Note whether each entry was axis-predicted or a surprise.

---

### STEP 5 — Composite Signal

This section synthesizes — it does not restate. If removing this section would leave the
artifact's conclusions unchanged, the section has failed.

Answer all four in 4–6 sentences:

1. **Signal verdict**: Does the overall evidence strengthen, weaken, or complicate the original
   SIGNAL hypothesis? State directly.
2. **Falsification result**: Were any STEP 1 Falsification Conditions triggered? If yes, what
   must the team revise? If no, what does the absence of triggers signal?
3. **Dominant finding**: What single finding across all subjects is most decision-relevant?
   Name it — not a theme.
4. **Axis verdict**: Did the STEP 0 opposition axis produce expected divergence, or did subjects
   converge? What does this convergence or divergence tell the feature team?

Cite subjects by ID (S-01, S-02) and hypothesis IDs (H-nn) where relevant.

---

### STEP 6 — Arc Signal

**Write this section after the Composite Signal. It is required. It must not restate
feature-level conclusions from STEP 5.**

| Field | Content |
|-------|---------|
| **Arc question** | [State an explicit question whose scope exceeds {SIGNAL}. Scope test: a different but adjacent signal in the same category would generate the same arc question — if the arc question is {SIGNAL}-specific, it is not arc-level.] |
| **Arc inference** | [State a conclusion answering the arc question that a reader could not reconstruct from the STEP 5 Composite Signal. Points beyond this specific feature to a pattern about adoption, workflow, or the user type.] |
| **Arc self-test** | Adjacent signal check: [name one adjacent signal]. The arc question applies to it equally: [yes / no]. — Removal test: if this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state the specific reason: what this inference provides that per-subject findings and the Composite Signal do not]. |

**Self-test rule**: the removal test must answer "yes." If "no," the arc inference has not
cleared feature scope. Revise before completing STEP 6.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-05 — Combination: Inertia Framing + Full Coverage

**Axes:** Inertia-first interview ordering (subjects with deepest investment in the current
approach interviewed first; their stated adoption conditions become the test battery for all
subsequent subjects) combined with full structural coverage of all three gap criteria. The
inertia axis declaration is the STEP 0 structural step (C-19 by construction). The Phase 1
hypothesis gate requires each H-ID to carry a falsification condition — anchored to what the
inertia representative would have to say (C-18). H-IDs are a pre-commit column in all interview
tables (C-12). The arc section in STEP 6 contains the three-field table with a required self-test
(C-20).

**Hypothesis:** Inertia framing is the natural carrier for C-19 — the inertia axis declaration
is definitionally a STEP 0 before hypotheses, because the inertia barrier must be named before
any hypothesis about adoption resistance can be formed. Anchoring falsification conditions to
the inertia representative ("what would S-01 have to say?") makes C-18 natural — each
hypothesis is testable against a specific person's stated position. C-12 passes via the H-IDs
pre-commit column. C-20 passes via the arc self-test field. All prior-round inertia-framing
strengths (inertia profile becoming subsequent test battery) are retained.
Predicted: 13/13. Composite 100.00.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

This skill runs in six steps using inertia-first interview ordering. The first subject
interviewed is always the persona with the deepest investment in the current approach — the
person {SIGNAL} would most disrupt. Their stated concerns and adoption conditions become the
test battery for all subsequent interviews. Each step with a gate condition must satisfy that
condition before the following step begins. Gate conditions are structural rules, not implied
by step numbering.

---

### STEP 0 — Inertia Axis Declaration

**This step must be completed before STEP 1 begins.**

Declare the inertia barrier and adoption axis before forming any hypothesis. Hypotheses about
adoption resistance cannot be well-formed until the inertia representative's position is named.

| Field | Declaration |
|-------|-------------|
| **Inertia barrier** | [Name the specific current approach, practice, or investment that {SIGNAL} would disrupt. What does the inertia representative have at stake — specifically, in time, rework, or responsibility?] |
| **Adoption axis** | [Name the tension dimension — e.g., "depth of investment in current approach vs. appetite for workflow change" / "incumbent practice loyalty vs. capability acquisition drive."] |
| **Why inertia-first** | [One sentence: why interviewing the inertia representative first produces evidence that interviewing an adopter first would not. What does the inertia subject surface that must be heard before the adopter can be positioned?] |
| **Pole A — Inertia representative (SKEPTIC)** | [Who lives here? What have they built, what are they responsible for, what would switching cost them in time, risk, or rework? Be specific.] |
| **Pole B — Adopter or evaluator (CHAMPION / EVALUATOR)** | [Who lives here? What adoption motivation or capability gap do they carry that the inertia representative lacks?] |
| **Pre-interview adoption hypothesis** | [Before any interview: what would the inertia representative need to see, hear, or have addressed to consider {SIGNAL} viable? This is a testable hypothesis — it will be confirmed, contradicted, or complicated in STEP 3.] |

**STEP 0 gate**: STEP 0 is not complete until: (1) the inertia barrier is specific — a named
current practice, not a general category; (2) both poles are described at genuinely opposite
ends of the adoption axis; (3) the pre-interview adoption hypothesis names a specific adoption
condition. **STEP 1 may not begin until all three gate conditions are satisfied.**

---

### STEP 1 — Hypothesis Register

Write before any interview question or persona answer. Locked once written. Falsification
conditions are anchored to the inertia representative — what would S-01 (the SKEPTIC) have to
say to force rejection?

| ID   | Hypothesis                                                               | Category                    | Falsification Condition (what S-01 would have to say to force revision)                   |
|------|--------------------------------------------------------------------------|-----------------------------|-------------------------------------------------------------------------------------------|
| H-01 | [belief about how the inertia representative responds to {SIGNAL}]      | assumption / risk / unknown | [what S-01 would have to say — named evidence type or answer pattern]                     |
| H-02 | [expected barrier or risk in the current approach]                       | risk                        | [what S-01's interview would have to reveal for this barrier to not apply]                |
| H-03 | [design question the inertia interview should resolve]                   | unknown                     | [what finding would resolve this against expectation]                                     |
| H-04 | [add rows — aim for 4+]                                                  |                             |                                                                                           |

**STEP 1 gate — universal inertia-anchored falsifiability:**

STEP 1 is not complete until **each declared hypothesis** carries a specific, non-trivial
falsification condition anchored to what the inertia representative (S-01) would have to say.
This gate applies to every H-ID — not "at least one." A falsification condition that reads
"if people generally disagree" or "if objections arise" does not satisfy the gate. The condition
must name what S-01 would have to specifically say or reveal that would force the team to revise
that hypothesis.

**STEP 2 may not begin while any H-ID has an empty or generic falsification condition.**

---

### STEP 2 — Human Subjects Roster (Inertia-First)

S-01 is the inertia representative — the subject with the deepest investment in the current
approach. S-01 is interviewed first.

| ID   | Name   | Role   | Axis Pole              | Inertia or Adoption Marker                                                        | H-IDs primarily tested          |
|------|--------|--------|------------------------|-----------------------------------------------------------------------------------|---------------------------------|
| S-01 | [Name] | [Role] | Pole A — SKEPTIC       | [specific current practice or investment that makes S-01 the inertia representative] | H-01, H-02, ...              |
| S-02 | [Name] | [Role] | Pole B — CHAMPION / EVALUATOR | [adoption motivation or perspective distinguishing S-02 from S-01]        | H-03, ...                   |

S-01's stated adoption conditions (from STEP 3) become the test battery for S-02 and all
subsequent subjects. Minimum 2 subjects — one SKEPTIC, one CHAMPION or EVALUATOR.

---

### STEP 3 — Interviews (Inertia-First)

**Do not write any interview row until Steps 0, 1, and 2 are complete.**

Complete S-01 (Identity, Interview Table, Inertia Profile, Evidence Extraction) before beginning
any subsequent subject.

#### S-01 — Identity (SKEPTIC / Inertia Representative)

[3–4 sentences: name, role, company type. Establish S-01's investment in the current approach
as deep and specific — how long they have used it, what they have built with it, what a switch
would cost. The depth must make S-01's resistance legible as well-founded and role-specific.]

Swap test: substitute S-02's name. If the interview answers would still read as plausible, add
specifics until the answer is no.

#### S-01 — Interview Table

Fill "H-IDs tested" before writing each question. A question row with a blank H-IDs column
may not be written.

| Q#  | H-IDs tested | Question                                                             | Answer (S-01 voice)                                                  | Evidence Signal [type: …] — one-sentence signal              | Surprise?     |
|-----|--------------|----------------------------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------------------|---------------|
| Q1  | H-nn         | [Current-practice baseline: what do you do today for {TOPIC}?]       | [S-01 answer establishing depth of current investment]               | [constraint / preference / risk / validation / invalidation]: […] | No (baseline) |
| Q2  | H-nn         | [What is the hardest part about your current approach?]              | [Friction in S-01's current practice — the crack in the inertia]     |                                                              |               |
| Q3  | H-nn         | [Introduction of {SIGNAL}: S-01's initial reaction]                  | [Skeptic response with specific, role-grounded objection]            |                                                              | Yes / No      |
| Q4  | H-nn         | [What would have to be true for you to adopt this?]                  | [S-01's adoption conditions — each is a testable claim about {SIGNAL}] |                                                            |               |
| Q5+ | H-nn         | [Additional objection probe]                                         |                                                                      |                                                              |               |

Minimum 4 rows for S-01. At least one "Yes" in Surprise column.

When a STEP 1 falsification condition is triggered:
> **[FALSIFICATION — H-nn triggered]:** Condition: [exact text from STEP 1]. S-01 said:
> [answer]. Conclusion: [how this forces revision of H-nn].

#### S-01 — Inertia Profile

Document S-01's stated concerns and adoption conditions. This table becomes the test battery
for all subsequent subjects — every subsequent interview must address at least one row.

| Concern or Objection | H-ID | Basis in S-01's practice                        | Adoption condition stated by S-01                   |
|----------------------|------|-------------------------------------------------|-----------------------------------------------------|
| [stated concern]     | H-nn | [why grounded in S-01's specific role/practice] | [what S-01 said would be needed for adoption]       |

#### S-01 — Evidence Extraction

1. [finding — specific to S-01's role and current-practice context]
2. [finding]
3. [finding]

---

#### S-02+ — Subsequent Subjects (CHAMPION / EVALUATOR)

#### [S-nn] — Identity

[2–3 sentences: name, role, domain distinction from S-01. State explicitly what distinguishes
this persona's axis position from S-01's — different adoption motivation, different investment
level, different risk exposure.]

#### [S-nn] — Interview Table

Fill "H-IDs tested" before writing each question. "Inertia Profile check" column must reference
S-01's stated position specifically for every row where S-01's position is being tested.

| Q#  | H-IDs tested | Question                                              | Answer (persona voice)                            | Evidence Signal [type: …]               | Inertia Profile check (vs. S-01)                                  |
|-----|--------------|-------------------------------------------------------|---------------------------------------------------|-----------------------------------------|-------------------------------------------------------------------|
| Q1  | H-nn         | [Current-practice anchor: what do you do today?]      | [S-nn baseline establishing their domain context] |                                         | Baseline — no S-01 comparison yet                                 |
| Q2  | H-nn         | [Testing S-01 Inertia Profile concern or condition 1] | [Confirm / reject / qualify — in persona's voice] |                                         | S-01 said [X]; [S-nn] said [Y] — confirms / rejects / qualifies  |
| Q3  | H-nn         | [Testing STEP 1 H-ID or adoption condition from S-01] |                                                   |                                         |                                                                   |

"H-IDs tested": fill before writing question. Minimum 3 rows.
"Inertia Profile check": reference S-01's position specifically for all rows testing inertia concerns.
At least one confirm or reject per subsequent subject.

#### [S-nn] — Evidence Extraction

1. [finding — specific to this subject's role and axis pole]
2. [finding]
3. [finding]

---

### STEP 4 — Inertia vs. Adoption Comparison Table

Rows are drawn from the S-01 Inertia Profile — not invented after the fact. Write after all
STEP 3 content is complete.

| S-01 Concern / Adoption Condition (H-ID) | S-01 stated position   | Subsequent subject response                         | Resolution status                        |
|------------------------------------------|------------------------|-----------------------------------------------------|------------------------------------------|
| [concern from Inertia Profile] (H-nn)    | [S-01 stated position] | [confirm / reject / qualify + explanation from S-02+] | Resolved / Unresolved / Context-dependent |

Completion rules:
- Every row references the S-01 Inertia Profile.
- At least one unresolved row. Leave it open.
- A row stating only "agreed with S-01" without explanation does not satisfy the completion rule.

---

### STEP 5 — Composite Signal

This section synthesizes — it does not restate. If removing this section would leave the
artifact's conclusions unchanged, the section has failed.

Write 4–6 sentences answering all four:

1. **Adoption verdict**: Does {SIGNAL} have a viable adoption path given S-01's resistance and
   subsequent subjects' reactions? State directly.
2. **Strongest remaining barrier**: Name S-01's strongest concern from the Inertia Profile that
   subsequent interviews did not address or resolve.
3. **Most surprising finding**: What did a subsequent subject reveal that S-01's Inertia Profile
   would not have predicted? Cite subject ID and H-ID.
4. **Next validation step**: What must the feature team validate before treating this signal as
   evidence of adoption viability?

---

### STEP 6 — Arc Signal

**Write this section after the Composite Signal. It is required. It must not restate
feature-level conclusions from STEP 5.**

The Arc Signal answers a question whose scope is wider than {SIGNAL} — what this inertia-vs.-
adoption interview run reveals about the adoption pattern, the workflow category, or the class
of features {SIGNAL} belongs to.

| Field | Content |
|-------|---------|
| **Arc question** | [State an explicit question wider than {SIGNAL}. Frame it around what this inertia-vs.-adoption pairing reveals about the user type, the workflow category, or adoption dynamics for this class of features — not whether {SIGNAL} specifically is viable. Scope test: would an adjacent signal with the same inertia profile generate the same arc question? If yes, scope is arc-level.] |
| **Arc inference** | [State a conclusion answering the arc question. A reader must not be able to reconstruct this inference from the STEP 5 Composite Signal alone. Points beyond this specific signal to a principle or pattern about adoption dynamics, inertia barriers, or workflow navigation.] |
| **Arc self-test** | Adjacent signal check: [name one adjacent signal with a similar inertia profile]. The arc question applies to it equally: [yes / no — if no, revise the arc question]. — Removal test: if this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state the specific reason: what this arc inference provides that the per-subject findings, Inertia Profile, and Composite Signal do not]. |

**Self-test rule**: the removal test must answer "yes." An arc inference the team can do without
has not cleared feature scope. Revise before treating STEP 6 as complete.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## Axis Coverage Summary

| Axis                              | V-01    | V-02    | V-03      | V-04              | V-05    |
|-----------------------------------|---------|---------|-----------|-------------------|---------|
| Role sequence (STEP 0 + STEP 6)   | PRIMARY | PRESENT | —         | PRIMARY           | PRIMARY |
| Output format (arc self-test)     | PRESENT | PRIMARY | PRESENT   | PRESENT           | PRESENT |
| Lifecycle emphasis (phase gates)  | —       | —       | PRIMARY   | PRIMARY           | —       |
| Phrasing register                 | —       | —       | —         | —                 | —       |
| Inertia framing                   | —       | —       | —         | —                 | PRIMARY |

---

## Predicted R7 Scores (v7 rubric)

| Variation | C-18 | C-19 | C-20 | C-12 | Aspirational | Composite |
|-----------|------|------|------|------|--------------|-----------|
| V-01 (Role Sequence + Arc Self-Test) | FAIL | PASS | PASS | PASS | 12/13 | 99.23 |
| V-02 (Output Format: STEP 0 + Arc Self-Test) | FAIL | PASS | PASS | PASS | 12/13 | 99.23 |
| V-03 (Lifecycle Emphasis: Phase-Gated Protocol) | PASS | PASS | PASS | PASS | 13/13 | 100.00 |
| V-04 (Role Sequence + Lifecycle) | PASS | PASS | PASS | PASS | 13/13 | 100.00 |
| V-05 (Inertia + Full Coverage) | PASS | PASS | PASS | PASS | 13/13 | 100.00 |

*V-01: STEP 0 carries C-19 PASS from R6. STEP 6 three-field table with required self-test field
achieves C-20 by construction — the `Arc self-test` row is a required field the author answers
with yes/no + reason in the artifact body, not an instruction. C-17 passes by cascade (C-20 →
C-17). C-18 absent — STEP 1 gate retains "at least one" condition from V-01 R6.*

*V-02: STEP 0 added before STEP 1 creates a named structural step preceding the hypothesis
register — C-19 PASS by construction; C-16 PASS by cascade (C-19 → C-16). STEP 6 arc self-test
field carries C-20 PASS from V-02 R6. C-18 absent — STEP 1 gate retains "at least one" from
V-02 R6.*

*V-03: Phase 0 is a named structural phase placed before the hypothesis set in Phase 1 — C-19
PASS by construction. Phase 1 gate sentence: "each declared hypothesis must carry a specific,
non-trivial falsification condition... Phase 2 may not begin while any H-ID has an empty or
generic falsification condition" — C-18 PASS by construction (evaluator test: author cannot
advance with even one hypothesis lacking a condition). Phase 2 H-IDs tested column as structural
pre-commit anchor — C-12 PASS. Phase 3 Arc Signal self-test field (author-supplied yes/no +
reason in artifact body) — C-20 PASS by construction.*

*V-04: STEP 0 named structural step before STEP 1 → C-19 PASS. STEP 1 gate "each declared
hypothesis" → C-18 PASS. H-IDs tested pre-commit column in STEP 3 → C-12 PASS. STEP 6
three-field arc table with required self-test → C-20 PASS. All four gap criteria addressed by
construction through distinct structural mechanisms that do not depend on each other.*

*V-05: Inertia Axis Declaration is STEP 0 — definitionally a named structural step before
hypothesis formation, because the inertia barrier must be named before resistance hypotheses
can be formed; C-19 PASS. STEP 1 gate requires every H-ID to carry a falsification condition
anchored to S-01's likely testimony — C-18 PASS. H-IDs tested pre-commit column in all STEP 3
tables — C-12 PASS. STEP 6 arc self-test field with required author-supplied answer — C-20 PASS.
All four gap criteria addressed. Inertia Profile as test battery for subsequent subjects
preserved from R6 V-05.*

---

## What R7 Should Tell Us

The three single-axis variations test two distinct hypotheses:

**H-single-1**: Can Role Sequence (V-01) or Output Format (V-02) achieve both C-19 and C-20
simultaneously without addressing C-18? Predicted: yes at 12/13 — these are structural additions
that do not interact with the gate quality axis. If either fails at C-19 or C-20, the mechanism
is not as self-enforcing as predicted.

**H-single-2**: Can Lifecycle Emphasis (V-03) achieve all three gap criteria simultaneously
(C-18 + C-19 + C-20) in a single variation? Predicted: yes at 13/13 — the phase-gated structure
is the natural carrier for all three because: (a) Phase 0 as a named phase satisfies C-19 more
robustly than a step (a phase has a gate, a step may not); (b) a universal quality gate in
Phase 1 is the canonical C-18 mechanism; (c) a required arc self-test field in Phase 3 is the
canonical C-20 mechanism. If V-03 fails at C-12 (H-IDs not becoming column anchors in Phase 2),
that would replicate V-03's persistent C-12 failure from R6 and confirm that lifecycle emphasis
alone cannot carry C-12.

The two combination variations (V-04, V-05) confirm whether the mechanisms scale to full
combinations without introducing new failures at criteria the single-axis variations already pass.
