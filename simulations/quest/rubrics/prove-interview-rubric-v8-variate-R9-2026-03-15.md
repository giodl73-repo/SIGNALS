# prove-interview — Rubric v8 Variations — Round 9

_Date: 2026-03-15 · Rubric: v8 (C-01–C-21) · Ceiling: 100_

---

## Context

R8 produced 5 variations. V-01 and V-02 were single-axis gap-isolation tests — V-01 R8 closed
C-18 in the V-01 R7 architecture; V-02 R8 closed C-21 in the V-02 R7 architecture with C-18
intentionally absent. V-03 R8 tested a conversational-technical register — first attempt at full
14-criterion coverage without formal procedural language. V-04 R8 closed both V-02 R7 gaps
(C-18 + C-21) simultaneously. V-05 R8 embedded V-02's combined arc field inside V-03's
phase-gated protocol.

**R8 scores under v8 (denominator /14):**

| Variation | C-18 | C-21 | Aspirational | Composite |
|-----------|------|------|--------------|-----------|
| V-01 R8 (Role Sequence: V-01 R7 + universal quality gate) | PASS | PASS | 14/14 | 100.00 |
| V-02 R8 (Output Format: V-02 R7 + explicit verdict rule, C-18 absent) | FAIL | PASS | 13/14 | 99.29 |
| V-03 R8 (Phrasing Register: conversational-technical) | PASS | PASS | 14/14 | 100.00 |
| V-04 R8 (Output Format + C-21 + C-18 combined) | PASS | PASS | 14/14 | 100.00 |
| V-05 R8 (Output Format + Phase Structure hybrid) | PASS | PASS | 14/14 | 100.00 |

**State entering R9**: Four architectures achieve 14/14. The rubric ceiling of 21 criteria is
saturated. No existing single-axis variation fails more than one criterion. R9 shifts from
gap-closure to **pattern extension**: what structural elements are not yet captured by any
criterion, and which new variation axis produces them?

**R9 new criterion candidates:**

- **C-22** (Role Sequence) — Hypothesis register closed with per-H-ID disposition before synthesis
  begins. C-10 requires pre-declaration; C-14 requires falsifiability; C-18 requires quality
  enforcement. No criterion requires the register to be _closed_ after interviews. A Hypothesis
  Disposition Table (CONFIRMED / CHALLENGED / FALSIFIED / UNRESOLVED per H-ID) after STEP 3
  and before STEP 4 fills this gap.

- **C-23** (Output Format) — Adjacent signal substitution test result embedded as named artifact
  output in the arc section. Currently the scope substitution test is an author-facing instruction.
  No criterion requires the named substitution result to appear in the artifact body. Adding a
  fourth required arc table field — "Adjacent signal test" with a named adjacent signal and
  yes/no + reason — makes scope compliance evaluator-verifiable by inspection.

- **C-24** (Inertia Framing + Scoring) — Evidence signals carry impact weights and the composite
  verdict references the top-weight findings by ID. No current criterion requires evidence to be
  quantified. A 1–3 impact weight per evidence slot + composite synthesis referencing top-weighted
  findings creates a quantification chain the existing rubric does not capture.

---

## R9 Goals

1. **Single-axis 1** — Role Sequence: add a Hypothesis Disposition Table (STEP 3.5) between
   interviews and the Tensions Matrix. Tests C-22 in isolation — all 14 prior criteria pass by
   inheriting V-01 R8 architecture.

2. **Single-axis 2** — Output Format: add a fourth arc table field ("Adjacent signal test")
   requiring a named adjacent signal and a yes/no + reason verdict. Tests C-23 in isolation —
   all 14 prior criteria pass, C-21 carries via the three-field arc structure already present.

3. **Single-axis 3** — Phrasing Register: investigator's notebook (first-person reflexive).
   Prior conversational test (V-03 R8) used "you" address. This uses first-person narration ("I
   am committing to the opposition axis before writing any hypothesis..."). Tests whether
   reflexive register preserves all 14 criterion passes as reliably as imperative register.

4. **Combination 1** — Role Sequence + Output Format: Hypothesis Disposition Table + four-field
   arc table (C-22 + C-23 combined). Tests orthogonality of the two new patterns.

5. **Combination 2** — Inertia Framing + Hypothesis Disposition + Evidence Scoring: status-quo
   competitor named structurally throughout + post-interview H-ID disposition + impact weights
   on every evidence signal. Tests C-22 + C-24 and whether inertia framing generates further
   new criteria.

---

## Variation Axes

| Axis | R8 result | R9 focus |
|------|-----------|----------|
| Role sequence (STEP structure) | V-01 R8: 14/14 (C-18 closed) | Add STEP 3.5 Hypothesis Disposition Table — tests C-22 |
| Output format (arc table fields) | V-02 R8: 13/14 (C-18 absent), V-04 R8: 14/14 | Add fourth arc field (adjacent signal test) — tests C-23 |
| Phrasing register | V-03 R8: 14/14 (conversational "you") | First-person reflexive register — untested in full-coverage form |
| Role Sequence + Output Format | Not combined | C-22 + C-23 coexistence test |
| Inertia framing + Role Sequence + Scoring | V-05 R7 inertia partial; scoring never tried | Three-axis combination — tests C-22 + C-24 |

---

## V-01 — Single axis: Role Sequence (Hypothesis Disposition Table between STEP 3 and STEP 4)

**Axis:** Role sequence. Single addition to V-01 R8: a new STEP 3.5 — Hypothesis Disposition
Table — inserted between the interview tables and the Cross-Subject Tensions Matrix. After all
subject tables in STEP 3 are complete, the author returns to every H-ID in STEP 1 and assigns a
disposition: CONFIRMED, CHALLENGED, FALSIFIED, or UNRESOLVED. STEP 4 cannot begin until every
H-ID has a non-empty disposition entry. All other structure is identical to V-01 R8.

**Hypothesis:** C-22 candidate — the disposition table requires the hypothesis register to be
explicitly closed post-interview before synthesis begins. No existing criterion captures this
lifecycle event. C-10 requires pre-declaration; C-14 requires at least one H-ID to be
falsifiable; C-18 requires the gate to enforce that every H-ID carries a specific Falsification
Condition. None require the author to revisit each H-ID after the interviews and state what
happened to it. An artifact satisfying C-18 can declare four quality hypotheses in STEP 1 and
never mention any of them in STEP 5 — C-22 closes this gap by requiring explicit post-interview
accounting. STEP 0 (C-19), STEP 1 quality gate (C-18), three-field STEP 6 arc table with binary
verdict rule (C-21) all carry unchanged from V-01 R8. Predicted: C-22 PASS (new criterion
candidate), 14/14 existing → composite 100.00 + new candidate.

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

**Write this section after all STEP 3 subject tables are complete. STEP 4 cannot begin until
every H-ID from STEP 1 has a non-empty disposition entry in this table.**

For each hypothesis declared in STEP 1, state what the interview evidence did to it.

| H-ID | Hypothesis (abbreviated) | Disposition | Evidence basis | Falsification triggered? |
|------|--------------------------|-------------|----------------|--------------------------|
| H-01 | [brief restatement]      | CONFIRMED / CHALLENGED / FALSIFIED / UNRESOLVED | [which subject(s), which Q-IDs, what they said that determines the disposition] | Yes — [H-nn triggered: see STEP 3] / No |
| H-02 |                          |             |                |                          |
| H-03 |                          |             |                |                          |
| H-04 |                          |             |                |                          |

**Disposition definitions:**
- **CONFIRMED** — interview evidence strengthens the hypothesis; no subject's answers triggered
  the Falsification Condition or substantially weakened it.
- **CHALLENGED** — at least one subject's answers weakened the hypothesis but did not trigger
  the declared Falsification Condition.
- **FALSIFIED** — a subject's answers triggered the exact Falsification Condition declared in
  STEP 1. The FALSIFICATION callout in STEP 3 must be present.
- **UNRESOLVED** — the interviews did not produce sufficient evidence to confirm, challenge, or
  falsify. State the evidence gap that would be needed to close this.

**Completion rules:**
- Every H-ID from STEP 1 must appear in this table — no row may be omitted.
- "Evidence basis" must cite subject IDs (S-nn) and question IDs (Q-nn) — a disposition without
  evidence reference is not complete.
- UNRESOLVED dispositions must state what evidence would be needed to close them, not merely
  note absence of evidence.

**Gate evaluator test:** Could an author write four UNRESOLVED dispositions with no evidence
basis and satisfy this gate? If yes, the gate fails. STEP 4 may not begin while any H-ID has an
empty disposition or an evidence basis that cites no subject or question ID.

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after STEP 3.5 (Hypothesis Disposition Table) is complete.

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
a reader can derive from the Interview Tables, Hypothesis Disposition Table, and Tensions Matrix
row by row.

Answer all three of the following in 4–6 sentences:

1. **Integrated verdict**: Does the overall evidence strengthen, weaken, or complicate the
   original SIGNAL hypothesis? State directly.

2. **Dominant finding**: What single finding across all subjects is most decision-relevant?
   Name it specifically — a finding, not a theme.

3. **Key open question**: What is the most important thing these interviews did not resolve?
   What would the feature team need to do next?

Cite subjects by ID (S-01, S-02) and hypothesis IDs (H-nn) where relevant. For any FALSIFIED
hypothesis, name it explicitly and state what the falsification implies for the feature decision.

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

## V-02 — Single axis: Output Format (Adjacent Signal Substitution as required arc output field)

**Axis:** Output format. Single addition to V-01 R8: STEP 6 arc table gains a required fourth
row — "Adjacent signal test" — in which the author names an adjacent signal and states whether
the arc question applies to it equally, formatted as yes/no + reason. All other structure
identical to V-01 R8.

The existing scope substitution instruction ("substitute a different but adjacent signal — if
the arc question applies equally, scope is arc-level") appears in V-01 R8 and all prior full-
coverage variations as an author instruction. It tells the author what to verify but does not
require the verification result to appear in the artifact body. An evaluator applying C-17
(arc-level scope) cannot confirm scope compliance by reading the artifact — they must apply the
substitution test independently. The fourth arc field closes this gap: the named adjacent signal
and the yes/no + reason verdict are artifact outputs, not author checks.

**Hypothesis:** C-23 candidate — requires the scope substitution test result to appear in the
artifact body as a named, evaluator-readable output. This is structurally analogous to C-21
(arc self-test answer formatted as a binary verdict rather than just being present): C-23
converts the scope substitution test from an author check to an artifact output verifiable by
inspection. C-21 carries unchanged (three-field arc table retained, binary verdict rule
present). C-19, C-18, C-20 all carry from V-01 R8. Predicted: C-23 PASS (new candidate),
14/14 existing → composite 100.00 + new candidate.

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
- The axis must be epistemic (a dimension of belief, practice, or expertise), not demographic.
- Pole A and Pole B must be genuine opposites on the named axis.
- "Evidence requiring Pole B" must name a specific finding type.

**Gate**: STEP 1 cannot be written until this section is complete. STEP 2 must assign each
subject to a pole declared here.

---

### STEP 1 — Hypothesis Register

Write this register before any interview question or persona answer. The register is locked once
written.

| ID   | Hypothesis                                               | Category                    | Falsification Condition                                                         |
|------|----------------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL] | assumption / risk / unknown | [what a subject would have to say to force rejection — name the answer type]    |
| H-02 | [a specific risk or concern you expect to surface]       | risk                        | [what answer would show this risk does not apply or is overstated]              |
| H-03 | [a design question these interviews should resolve]      | unknown                     | [what finding would resolve this against your expectation]                      |
| H-04 | [add additional hypotheses — aim for at least 4]         |                             |                                                                                 |

**Register rules:**
- Minimum 4 hypotheses.
- Every declared hypothesis must carry a specific, non-trivial Falsification Condition. The gate
  is not satisfied until every H-ID has a non-empty, specific condition — not "at least one."
- Register is locked once written.

**Gate evaluator test:** Could an author satisfy this gate by writing four hypotheses with no
Falsification Conditions and proceed to STEP 3? If yes, this gate fails.

---

### STEP 2 — Human Subjects Roster

Assign each subject to a pole declared in STEP 0.

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
or known event. Identity must make the subject's pole assignment legible.]

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
- Agreement rows explain why convergence is meaningful given the STEP 0 axis.
- At least one row records an open, unresolved tension.
- Note whether each row was axis-predicted or a surprise.

---

### STEP 5 — Composite Signal

This section synthesizes — it does not restate. If removing this section would leave the artifact
unchanged, the section has failed.

Answer all three of the following in 4–6 sentences:

1. **Integrated verdict**: Does the overall evidence strengthen, weaken, or complicate the
   original SIGNAL hypothesis? State directly.
2. **Dominant finding**: What single finding across all subjects is most decision-relevant?
   Name it specifically.
3. **Key open question**: What did these interviews not resolve? What would the feature team
   need to do next?

Cite subjects by ID (S-01, S-02) and hypothesis IDs (H-nn) where relevant.

---

### STEP 6 — Arc Signal

**Write this section after the Composite Signal. It is required. It must not restate
feature-level conclusions from STEP 5.**

The Arc Signal answers a question whose scope is wider than {SIGNAL} — what this interview run
reveals about the adoption pattern, the workflow category, or the class of features {SIGNAL}
belongs to.

| Field | Content |
|-------|---------|
| **Arc question** | [State an explicit question whose scope exceeds {SIGNAL}. Scope test below.] |
| **Arc inference** | [State a conclusion that answers the arc question and that a reader could not reconstruct by reading the Composite Signal alone. Points beyond this specific feature.] |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state specific reason: what the arc inference provides that per-subject findings and the Composite Signal do not]. |
| **Adjacent signal test** | Name an adjacent signal in the same category as {SIGNAL}: [name it]. Does the arc question apply to that adjacent signal equally? [yes / no] — because [one sentence: what the arc question captures that is category-level and not {SIGNAL}-specific, OR why the arc question would need to change and therefore scope must be revised]. |

**Arc self-test verdict format:** The answer must be an explicit binary verdict — "yes" or "no"
— followed immediately by a stated rationale. A narrative answer that implies a verdict without
committing to the binary word fails. A verdict without a stated rationale fails. Evaluator test:
if a reviewer disagrees with the verdict, can they identify and challenge the specific reason
stated in the artifact? If the rationale is too diffuse, revise before treating STEP 6 as
complete.

**Adjacent signal test rules:**
- The adjacent signal must be named by a specific title, not described generically ("a similar
  feature" fails; "the /prove:prototype skill" passes).
- If the answer is "no — because the arc question would need to change for the adjacent signal,"
  the arc question is still feature-level. Revise the arc question before treating STEP 6 as
  complete.
- If the answer is "yes," the scope is arc-level and the field is satisfied.

**Arc self-test rule**: the removal test answer must be "yes." If the author answers "no," revise
the arc inference before proceeding.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-03 — Single axis: Phrasing Register (Investigator's Notebook — first-person reflexive)

**Axis:** Phrasing register. V-03 R8 tested a conversational "you" address register and achieved
14/14. This variation tests a first-person reflexive register: the prompt is written as if the
model is narrating its own investigation. "Before I write any hypotheses, I commit to the
opposition axis." "I cannot proceed to STEP 3 while any H-ID has an empty falsification
condition." The structural mechanisms — named opposition step, universal quality gate, three-
field arc table, binary verdict format rule — are identical to V-01 R8.

**Hypothesis:** The reflexive register does not break criterion compliance because criteria are
format requirements, not language requirements. C-19 passes because STEP 0 is still a named
structural step before STEP 1, regardless of whether it says "Write this before..." or "I am
committing this before...". C-18 passes because the quality gate requires every H-ID to carry a
specific condition, whether stated as "The gate is not satisfied until every H-ID has a specific
condition" or "I verify that every H-ID row has a specific falsification condition before
proceeding." C-21 passes because the binary verdict requirement is a content rule, not a
procedural instruction. What changes: the implied agency (model as investigator vs. model as
procedure executor). What does not change: the evaluable outputs. Predicted: 14/14 → 100.00.
No new criterion expected — pure register robustness test.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

I am running a stakeholder/customer interview simulation for this topic. The interviews are not
real — but every persona answer I write must be anchored in the persona's documented identity,
expertise, and prior experience. The output is a signal artifact: structured evidence toward or
against the signal hypothesis.

I will work through the six steps below in sequence. I cannot begin a later step until the
preceding step is committed.

---

### STEP 0 — I declare the opposition axis before writing any hypothesis

Before I can write a single hypothesis, I need to commit to the epistemic tension axis this
simulation will span. This is not a persona selection decision — it is an epistemic design
commitment: I am choosing to place two subjects at opposite ends of a relevant dimension rather
than picking two people who might agree.

Here is my axis declaration:

| Field | My commitment |
|-------|---------------|
| **Axis name** | [I name the dimension — what kind of belief, practice, or prior investment separates subjects at opposite ends? Not job title or company size — a genuine epistemic dimension.] |
| **Why this axis for {SIGNAL}** | [One sentence: what I can learn by interviewing both poles that I cannot learn from two subjects at the same pole. I name the specific evidence type that requires opposition.] |
| **Pole A — resistant / skeptical** | [I describe who lives at this pole: what have they built or invested in that {SIGNAL} would disrupt? What does adoption cost them specifically?] |
| **Pole B — receptive / innovative** | [I describe who lives at this pole: what are they missing that {SIGNAL} provides? What would drive their adoption that does not drive Pole A?] |
| **What Pole A alone cannot give me** | [I name the specific finding type I would miss if I only interviewed skeptics. "A different perspective" is not a finding type — I name the evidence.] |

I commit: the axis must be epistemic, not demographic. Both poles must be genuine opposites.
I cannot begin STEP 1 until this table is complete and both poles are genuinely opposite ends
of a named epistemic dimension.

---

### STEP 1 — I lock down my hypotheses before the first interview

I write down every assumption and risk I am carrying into these interviews — before I write any
question or persona answer. Once I commit this register, it is locked. I cannot revise it after
the first interview row is written.

| ID   | Hypothesis                                               | Category                    | What would falsify this?                                                        |
|------|----------------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------|
| H-01 | [what I believe about how stakeholders will respond to {SIGNAL}] | assumption / risk / unknown | [what a subject would need to say to force me to reject this — I name the evidence type or answer pattern, not "if people disagree"] |
| H-02 | [a risk or concern I expect to surface]                  | risk                        | [what interview answer would show this risk does not apply]                     |
| H-03 | [a design question I hope these interviews resolve]      | unknown                     | [what finding would resolve it against my expectation]                          |
| H-04+ | [additional hypotheses — I aim for at least 4]          |                             |                                                                                 |

Before I proceed to STEP 2, I verify every H-ID row: every one must have a specific falsification
condition. Not "if people disagree" — the actual evidence type or answer pattern that would force
me to revise that specific hypothesis. If any row has a blank or generic condition, I fill it in
now. This is a quality check, not a count check: four hypotheses each with specific conditions
satisfies this; four hypotheses with one specific condition and three blanks does not.

I cannot proceed to STEP 3 while any H-ID has an empty or generic Falsification Condition.

---

### STEP 2 — I select and position my subjects

I assign each subject to one of the poles I declared in STEP 0. If I cannot assign a subject to
a declared pole, they do not belong in this run and I replace them.

| ID   | Name   | Role   | Seniority | Pole (STEP 0)                  | What grounds their pole                                                                 |
|------|--------|--------|-----------|--------------------------------|-----------------------------------------------------------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [What specifically makes this persona a Pole A or Pole B subject — their investment, belief, or capability gap] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [What distinguishes their pole position from S-01's]                                   |

Minimum 2 subjects, one from each pole.

---

### STEP 3 — I conduct the interviews

I do not write any interview content until STEP 0, STEP 1, and STEP 2 are done. The H-IDs and
pole assignments must be committed before any persona answer appears.

For each subject, I write their identity first, then their interview table.

#### [S-nn] — Who they are

[2–3 sentences: where they work or what context they operate in, what they have built or are
responsible for, at least one concrete concern or event that makes this persona specific. A
reader should be able to identify which axis pole they occupy from this paragraph alone.]

I apply the swap test: if I substitute another persona's name into this paragraph and the
interview answers still read as plausible, I add specifics until the answer is no.

#### [S-nn] — Interview

| Q# | Question [H-nn] | Answer (their voice) | Evidence Signal [type: ...] | Surprise? |
|----|-----------------|---------------------|----------------------------|-----------|
| Q1 | [Question] [H-01] | [Answer using this persona's vocabulary, domain concerns, and context — not general wisdom] | [risk / preference / constraint / validation / invalidation]: [one-sentence interpretation] | Yes — expected [X], found [Y] / No |
| Q2 | [Question] [H-nn] | | | |
| Q3 | [Question] [H-nn] | | | |

My rules for every row:
- I write the H-IDs cited in the question column before writing the question text.
- Every answer is specific to this persona — substituting another persona's name should break
  it. Generic wisdom fails.
- Every evidence entry needs a type tag and a one-sentence interpretation.
- At least one row per person carries "Yes" in the Surprise column, with what I expected vs.
  what I found.
- Minimum 3 rows per subject.

When a STEP 1 falsification condition is triggered:
> **[FALSIFICATION — H-nn triggered]:** The condition I declared was: [exact text from STEP 1].
> They said: [answer]. This forces me to revise H-nn because: [explanation].

---

### STEP 4 — I compare subjects against each other

After all interview tables are done, I build the tensions comparison.

| What I am comparing [H-ID if relevant] | S-01's position | S-02's position | What the comparison tells me | Axis-predicted? | Still open? |
|----------------------------------------|-----------------|-----------------|------------------------------|-----------------|-------------|
| [shared dimension, H-ID, or axis concern] | [S-01 stated view] | [S-02 stated view] | TENSION: [what the disagreement signals to the feature team] / AGREEMENT: [why convergence here is notable given the opposition axis I declared] | Expected / Surprise | Yes / No |

My rules:
- At least one row that remains genuinely unresolved — I leave it open, I do not paper over it.
- Agreement rows explain why the convergence matters given my STEP 0 axis. "Both agreed" without
  an explanation does not satisfy this.
- I note whether each row was predicted by the STEP 0 axis or surprised me.

---

### STEP 5 — I synthesize, I do not restate

I write 4–6 sentences integrating the evidence into a conclusion. If I can remove this section
and the artifact says the same things, it is not done — synthesis adds integrated judgment, not
a restatement of what each person said.

I answer all three:

1. Does the evidence strengthen, weaken, or complicate the {SIGNAL} hypothesis? I say it
   directly.
2. What is the single most decision-relevant finding across all subjects? I name the specific
   finding — not a theme.
3. What did these interviews not resolve? What does the feature team need to do next?

I cite subjects by ID (S-01, S-02) and hypothesis IDs (H-nn) where relevant.

---

### STEP 6 — I write the arc signal

I write this after STEP 5. It is required. I do not repeat conclusions from STEP 5.

The arc signal answers a question wider than {SIGNAL}. What does this interview run tell me
about the adoption pattern, the workflow category, or the class of features {SIGNAL} belongs to?
Not whether {SIGNAL} works — what this run reveals about the broader context it lives in.

| Field | What I write |
|-------|--------------|
| **Arc question** | A question whose scope exceeds {SIGNAL}. I verify scope: would a different but adjacent signal in the same category generate this same arc question? If yes, scope is correct. If the arc question would need to change for the adjacent signal, it is still feature-level and I revise. |
| **Arc inference** | A conclusion answering the arc question that a reader cannot reconstruct from STEP 5 alone. It points beyond this feature to a pattern about adoption, the workflow, or the user type. |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something they cannot reconstruct from the per-subject findings and my STEP 5 synthesis? My answer: [yes / no] — because [I state the specific reason: what the arc inference provides that the rest of the artifact does not]. |

**My arc self-test format commitment:** My answer must begin with the binary word — "yes" or
"no" — followed immediately by my stated rationale. I do not write a paragraph that implies an
answer without committing to the word. I do not write the word without explaining why. Both
halves are required. The test for my rationale: if someone disagreed with my verdict, could they
find and challenge the specific reason I wrote? If my rationale is too vague to be directly
contested, I rewrite it until it is.

My answer must be "yes." An arc inference the team can do without has not cleared feature scope
— I revise until removing it genuinely costs them something they cannot get elsewhere.

---

I write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-04 — Combination: Role Sequence + Output Format (Hypothesis Disposition Table + Adjacent Signal Arc Field)

**Axes:** Role Sequence (V-01 R9) + Output Format (V-02 R9) combined. Adds both new structural
elements to V-01 R8's architecture: STEP 3.5 Hypothesis Disposition Table and a four-field STEP
6 arc table with an "Adjacent signal test" fourth row.

**Hypothesis:** C-22 (disposition table) and C-23 (adjacent signal output) are orthogonal — they
address different lifecycle phases and different artifact sections. C-22 operates between STEP 3
and STEP 4 (post-interview, pre-synthesis); C-23 operates within STEP 6 (arc-level scope
verification). Their coexistence produces a richer lifecycle closure: hypothesis register opened
in STEP 1 (C-10), enforced with quality gate (C-18), closed with dispositions in STEP 3.5
(C-22 candidate), and arc scope verified by named substitution result in STEP 6 (C-23
candidate). All 14 existing criteria maintained. Predicted: C-22 PASS, C-23 PASS, 14/14 existing
→ composite 100.00 + two new candidates.

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
| **Axis name** | [Name the tension axis — epistemic, not demographic] |
| **Why this axis for {SIGNAL}** | [One sentence: why tension on this axis produces more informative evidence for {SIGNAL} than agreement would. What question about {SIGNAL} requires both poles?] |
| **Pole A — resistant / skeptical** | [What does a subject here believe, invest in, or stand to lose from {SIGNAL} adoption?] |
| **Pole B — receptive / innovative** | [What does a subject here want, lack, or stand to gain from {SIGNAL} adoption?] |
| **Evidence requiring Pole B** | [Specific finding type that a Pole A interview alone cannot produce. Name the evidence, not the perspective.] |

**Declaration rules:**
- Axis must be epistemic (belief, practice, expertise), not demographic.
- Poles must be genuine opposites, not variations of the same position.
- "Evidence requiring Pole B" must name a specific finding type.

**Gate**: STEP 1 cannot be written until this section is complete. STEP 2 must assign each
subject to a declared pole.

---

### STEP 1 — Hypothesis Register

Write before any interview question or persona answer. Locked once written.

| ID   | Hypothesis                                               | Category                    | Falsification Condition                                                         |
|------|----------------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL] | assumption / risk / unknown | [what a subject would have to say to force rejection — name the answer type]    |
| H-02 | [a specific risk or concern you expect to surface]       | risk                        | [what answer would show this risk does not apply]                               |
| H-03 | [a design question these interviews should resolve]      | unknown                     | [what finding would resolve this against your expectation]                      |
| H-04 | [additional hypotheses — aim for at least 4]             |                             |                                                                                 |

**Register rules:**
- Minimum 4 hypotheses.
- Every declared hypothesis must carry a specific, non-trivial Falsification Condition. The gate
  requires all H-IDs to satisfy the condition — not "at least one." Generic conditions ("if
  people disagree") do not satisfy the gate.
- Register is locked once written.

**Gate evaluator test:** Could an author write four hypotheses with empty Falsification
Conditions and advance to STEP 3? If yes, this gate fails.

---

### STEP 2 — Human Subjects Roster

Assign each subject to a declared pole before writing their background.

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)             | Key Concern                                                                             |
|------|--------|--------|-----------|--------------------------------|-----------------------------------------------------------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [What this persona is most likely to push back on or champion — grounded in their pole] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [Key concern meaningfully distinct from S-01]                                           |

Minimum 2 subjects, one from each declared pole.

---

### STEP 3 — Interviews

**Do not write any interview table row until Steps 0, 1, and 2 are complete.**

For each subject in the roster:

#### [S-nn] — Identity

[2–3 sentences: context, prior experience, at least one concrete concern. Identity must make
pole assignment legible to a reader.]

Swap test: substitute another persona's name. If answers remain plausible, revise.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn]   | Answer (persona voice)                                 | Evidence Signal [type: ...]                                                           | Surprise?                        |
|-----|-------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------|----------------------------------|
| Q1  | [Question] [H-01] | [Answer — vocabulary and concerns drawn from Identity] | [risk: ...] / [preference: ...] / [constraint: ...] / [validation: ...] / [invalidation: ...] — [one-sentence signal] | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn] |                                                        |                                                                                       |                                  |
| Q3  | [Question] [H-nn] |                                                        |                                                                                       |                                  |

**Table rules:**
- Every question cites at least one H-ID in brackets.
- Every answer fails the swap test.
- Every Evidence Signal carries a type tag and a one-sentence interpretation.
- At least one "Yes" per subject in the Surprise column, with expected vs. found.
- Minimum 3 rows per subject.

When a Falsification Condition is triggered:
> **[FALSIFICATION — H-nn triggered]:** Condition stated: [exact condition from STEP 1]. Subject
> said: [answer]. Conclusion: [how this forces revision of H-nn].

---

### STEP 3.5 — Hypothesis Disposition Table

**Write this section after all STEP 3 subject tables are complete. STEP 4 cannot begin until
every H-ID from STEP 1 has a non-empty disposition entry.**

| H-ID | Hypothesis (abbreviated) | Disposition | Evidence basis (S-nn, Q-nn) | Falsification triggered? |
|------|--------------------------|-------------|----------------------------|--------------------------|
| H-01 | [brief restatement]      | CONFIRMED / CHALLENGED / FALSIFIED / UNRESOLVED | [subject IDs and Q-IDs that determine this disposition] | Yes / No |
| H-02 |                          |             |                            |                          |
| H-03 |                          |             |                            |                          |
| H-04 |                          |             |                            |                          |

**Disposition definitions:**
- **CONFIRMED** — evidence strengthens the hypothesis; no answer triggered the Falsification
  Condition or substantially weakened it.
- **CHALLENGED** — at least one answer weakened the hypothesis without triggering the declared
  Falsification Condition.
- **FALSIFIED** — an answer triggered the exact Falsification Condition from STEP 1.
- **UNRESOLVED** — insufficient evidence to confirm, challenge, or falsify. State the evidence
  gap that would close this.

**Completion rules:**
- Every H-ID from STEP 1 must appear. No row may be omitted.
- Evidence basis must cite subject IDs (S-nn) and question IDs (Q-nn).
- UNRESOLVED dispositions must state what evidence would be needed, not merely note absence.

**Gate evaluator test:** Could an author write four UNRESOLVED dispositions with no evidence
basis and advance to STEP 4? If yes, this gate fails.

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after STEP 3.5 is complete.

| Dimension [H-ID if applicable]       | S-01 position | S-02 position | Tension or Agreement [explained]                    | Axis-predicted? | Unresolved? |
|--------------------------------------|---------------|---------------|-----------------------------------------------------|-----------------|-------------|
| [topic / concern / H-ID / axis pole] | [S-01 view]   | [S-02 view]   | TENSION: [describe] / AGREEMENT: [what it signals]  | Expected / Surprise | Yes / No |

**Completion rules:**
- Every row compares at least two subjects on a shared dimension.
- Agreement rows explain why convergence is meaningful given the STEP 0 axis.
- At least one row records an open, unresolved tension.
- Note whether each row was axis-predicted or a surprise.

---

### STEP 5 — Composite Signal

Synthesizes — does not restate. Removing this section must cost the feature team integrated
judgment they cannot reconstruct from the interview tables and Disposition Table row by row.

Answer all three in 4–6 sentences:

1. **Integrated verdict**: Does the overall evidence strengthen, weaken, or complicate the
   original SIGNAL hypothesis? State directly.
2. **Dominant finding**: What single finding across all subjects is most decision-relevant?
   Name it specifically.
3. **Key open question**: What did these interviews not resolve? What would the feature team
   need to do next?

Cite subjects by ID (S-01, S-02) and hypothesis IDs (H-nn) where relevant. For any FALSIFIED
hypothesis, name it explicitly and state what the falsification implies.

---

### STEP 6 — Arc Signal

**Required. Write after STEP 5. Must not restate STEP 5 conclusions.**

The Arc Signal answers a question whose scope is wider than {SIGNAL} — what this interview run
reveals about the adoption pattern, the workflow category, or the class of features {SIGNAL}
belongs to.

| Field | Content |
|-------|---------|
| **Arc question** | [Explicit question whose scope exceeds {SIGNAL}. Scope test: if the same question could only be answered by studying {SIGNAL} specifically, it is not an arc question.] |
| **Arc inference** | [Conclusion answering the arc question — not reconstructable from STEP 5 alone. Points beyond this feature to a pattern.] |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [specific reason: what the arc inference provides that per-subject findings and STEP 5 do not]. |
| **Adjacent signal test** | Name an adjacent signal in the same category as {SIGNAL}: [name it]. Does the arc question apply to that adjacent signal equally? [yes / no] — because [one sentence: what the arc question captures that is category-level and not {SIGNAL}-specific, OR why the question would need to change and therefore scope must be revised before treating STEP 6 as complete]. |

**Arc self-test verdict format:** The answer must be an explicit binary verdict — "yes" or "no"
— followed immediately by a stated rationale. A narrative answer that implies a verdict without
committing to the binary word fails. A verdict without a stated rationale fails. Evaluator test:
if a reviewer disagrees with the verdict, can they identify and challenge the specific reason?
If the rationale is too diffuse, revise.

**Adjacent signal test rules:**
- The adjacent signal must be named specifically, not described generically.
- If the answer is "no — because the arc question would need to change," the arc question is
  still feature-level. Revise before treating STEP 6 as complete.

**Arc self-test rule**: the removal test answer must be "yes." If "no," revise the arc inference.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-05 — Combination: Inertia Framing + Hypothesis Disposition + Evidence Scoring

**Axes:** Three-axis combination.

1. **Inertia framing**: The status-quo incumbent — what interviewees currently do in the absence
   of {SIGNAL} — is named as a structural element in STEP 0 and referenced in every hypothesis.
   STEP 0 includes an "Incumbent approach" field naming what subjects already use or do instead
   of {SIGNAL}. Every H-ID in STEP 1 states how the hypothesis relates to that incumbent
   approach. The Composite Signal includes an explicit "Inertia assessment" prompt: does the
   evidence suggest {SIGNAL} can overcome the switching cost the incumbent represents?

2. **Hypothesis Disposition Table** (from V-01 R9): post-interview H-ID closure with
   CONFIRMED / CHALLENGED / FALSIFIED / UNRESOLVED dispositions.

3. **Evidence impact scoring**: each Evidence Signal in the interview table carries an impact
   weight (1 = low signal value for the feature team's decision, 2 = medium, 3 = high). The
   Composite Signal must cite the three highest-weight findings by Q-ID and weight.

**C-24 candidate**: evidence signals carry impact weights and the composite verdict references
top-weight findings by ID. No current criterion requires evidence to be quantified. A 1-3
weight column in the interview table + a rule requiring the composite to cite top-weight
findings creates a quantification chain: evidence is not just typed and tagged, it is ranked,
and the ranking must influence the synthesis. Evaluator test: does the Composite Signal cite
the highest-weighted findings by Q-ID? If not, the impact scoring chain is broken.

**Hypothesis:** All 14 existing criteria maintained. Inertia framing enriches C-16 (structural
epistemic opposition now includes incumbent investment as one axis dimension) and C-14 (incumbent
hypotheses are naturally falsifiable — "if interviewees report that switching cost from the
incumbent is below X threshold, H-nn is falsified"). Disposition table (C-22 candidate). Impact
scoring + top-weight citation requirement (C-24 candidate). Predicted: C-22 PASS, C-24 PASS,
14/14 existing → composite 100.00 + two new candidates.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Simulate stakeholder or customer interviews about this topic. The interviews are not real — but
every persona answer must be anchored in the persona's documented identity, expertise, and prior
experience. The output is a signal artifact: structured evidence toward or against the signal
hypothesis.

---

### STEP 0 — Opposition Axis Declaration (with Incumbent Framing)

Write this section before the Hypothesis Register. It commits the interview design — including
what subjects currently do instead of {SIGNAL} — before any hypothesis is formed.

| Field | Declaration |
|-------|-------------|
| **Axis name** | [Name the epistemic tension axis — a dimension of belief, practice, or prior investment, not demographics] |
| **Incumbent approach** | [Name what interviewees currently use or do in the absence of {SIGNAL}. This is the status-quo competitor. Be specific — not "existing tools" but the named practice, workflow, or system. Every hypothesis in STEP 1 must relate to whether {SIGNAL} can displace or complement this incumbent.] |
| **Why this axis for {SIGNAL}** | [One sentence: why tension on this axis produces more informative evidence about {SIGNAL}'s ability to displace the incumbent than agreement on this axis would.] |
| **Pole A — invested in the incumbent** | [Who is here? What have they built around the incumbent approach? What does switching cost them — time, rework, retraining, system redesign?] |
| **Pole B — underserved by the incumbent** | [Who is here? What does the incumbent fail to give them that {SIGNAL} provides? What switching motivation do they have that Pole A lacks?] |
| **Evidence requiring Pole B** | [Specific finding type that a Pole A interview alone cannot produce — particularly regarding adoption conditions, switching triggers, or competitive displacement dynamics.] |

**Declaration rules:**
- Axis must be epistemic, not demographic.
- "Incumbent approach" must name a specific practice or system, not a category.
- Poles must be genuine opposites on the named axis.

**Gate**: STEP 1 cannot be written until this section is complete. Every H-ID in STEP 1 must
relate to the incumbent approach declared here.

---

### STEP 1 — Hypothesis Register (with Incumbent Reference)

Write before any interview question or persona answer. Locked once written.

Every hypothesis must state how it relates to the incumbent approach declared in STEP 0 — either
as a displacement hypothesis (can {SIGNAL} displace the incumbent for this subject?) or a
coexistence hypothesis (will {SIGNAL} augment the incumbent without displacing it?).

| ID   | Hypothesis                                               | Category                    | Incumbent relation                                    | Falsification Condition                                                         |
|------|----------------------------------------------------------|-----------------------------|-------------------------------------------------------|---------------------------------------------------------------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL] | assumption / risk / unknown | displacement / coexistence / threat / complement      | [what a subject would have to say to force rejection — name the answer type]    |
| H-02 | [a specific risk related to switching from the incumbent]| risk                        | displacement / coexistence / threat / complement      | [what answer would show this risk does not apply]                               |
| H-03 | [a design question about incumbent coexistence or displacement] | unknown              | displacement / coexistence / threat / complement      | [what finding would resolve this against your expectation]                      |
| H-04 | [additional hypotheses — aim for at least 4]             |                             |                                                       |                                                                                 |

**Register rules:**
- Minimum 4 hypotheses.
- Every hypothesis must have a non-empty "Incumbent relation" field.
- Every hypothesis must carry a specific, non-trivial Falsification Condition. The gate requires
  all H-IDs — not "at least one."
- Register is locked once written.

**Gate evaluator test:** Could an author satisfy this gate by writing hypotheses with empty
Falsification Conditions or empty Incumbent Relation fields? If yes, this gate fails.

---

### STEP 2 — Human Subjects Roster

Assign each subject to a pole declared in STEP 0. Ground each subject's pole assignment in their
relationship to the incumbent approach named in STEP 0.

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)             | Incumbent investment or gap                                                             | Key Concern                            |
|------|--------|--------|-----------|--------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [How this persona relates to the incumbent approach — what they've built, or what the incumbent fails them on] | [Primary concern grounded in their pole position] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0)  | [Their incumbent relation, distinct from S-01's]                                        | [Key concern distinct from S-01's]     |

Minimum 2 subjects, one from each pole.

---

### STEP 3 — Interviews

**Do not write any interview table row until Steps 0, 1, and 2 are complete.**

For each subject in the roster:

#### [S-nn] — Identity

[2–3 sentences: context, relationship to the incumbent approach named in STEP 0, at least one
concrete concern grounded in their position on the opposition axis. Identity must make both the
pole assignment and the incumbent relationship legible to a reader.]

Swap test: substitute another persona's name. If the interview answers remain plausible, revise.

#### [S-nn] — Interview Table

Every Evidence Signal carries two annotations: (1) a type tag and one-sentence interpretation,
and (2) an **impact weight** (1 = low decision value for the feature team, 2 = medium, 3 = high).
Impact weight reflects how much this specific finding should influence the feature team's
decision about {SIGNAL} — not how surprising it is.

| Q#  | Question [H-nn]   | Answer (persona voice)                                 | Evidence Signal [type: ...] — [interpretation]      | Weight | Surprise?  |
|-----|-------------------|--------------------------------------------------------|-----------------------------------------------------|--------|------------|
| Q1  | [Question] [H-01] | [Answer — vocabulary and concerns drawn from Identity] | [risk / preference / constraint / validation / invalidation]: [one-sentence signal] | 1/2/3  | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn] |                                                        |                                                     |        |            |
| Q3  | [Question] [H-nn] |                                                        |                                                     |        |            |

**Table rules:**
- Every question cites at least one H-ID.
- Every answer fails the swap test.
- Every Evidence Signal carries a type tag, one-sentence interpretation, and an impact weight
  (1, 2, or 3).
- At least one question per subject explicitly addresses the incumbent approach from STEP 0
  — ask about switching cost, displacement conditions, or coexistence requirements.
- At least one "Yes" per subject in Surprise column, with expected vs. found.
- Minimum 3 rows per subject.

When a Falsification Condition is triggered:
> **[FALSIFICATION — H-nn triggered]:** Condition stated: [exact condition from STEP 1]. Subject
> said: [answer]. Conclusion: [how this forces revision of H-nn].

---

### STEP 3.5 — Hypothesis Disposition Table

**Write this section after all STEP 3 subject tables are complete. STEP 4 cannot begin until
every H-ID from STEP 1 has a non-empty disposition entry.**

| H-ID | Hypothesis (abbreviated) | Incumbent relation | Disposition | Evidence basis (S-nn, Q-nn) | Falsification triggered? |
|------|--------------------------|-------------------|-------------|----------------------------|--------------------------|
| H-01 | [brief restatement]      | displacement / coexistence / threat / complement | CONFIRMED / CHALLENGED / FALSIFIED / UNRESOLVED | [S-nn, Q-nn that determines disposition] | Yes / No |
| H-02 |                          |                   |             |                            |                          |
| H-03 |                          |                   |             |                            |                          |
| H-04 |                          |                   |             |                            |                          |

**Disposition definitions:**
- **CONFIRMED** — interview evidence strengthens the hypothesis.
- **CHALLENGED** — evidence weakens it without triggering the Falsification Condition.
- **FALSIFIED** — an answer triggered the exact Falsification Condition from STEP 1.
- **UNRESOLVED** — insufficient evidence. State the specific evidence gap.

**Completion rules:**
- Every H-ID must appear. No row may be omitted.
- Evidence basis must cite S-nn and Q-nn.
- UNRESOLVED dispositions must state what evidence would close them.

**Gate evaluator test:** Could an author write UNRESOLVED entries with no evidence basis and
advance to STEP 4? If yes, the gate fails.

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after STEP 3.5 is complete.

| Dimension [H-ID if applicable]       | S-01 position | S-02 position | Tension or Agreement [explained]                    | Incumbent relation | Axis-predicted? | Unresolved? |
|--------------------------------------|---------------|---------------|-----------------------------------------------------|--------------------|-----------------|-------------|
| [topic / concern / H-ID / axis pole] | [S-01 view]   | [S-02 view]   | TENSION: [describe] / AGREEMENT: [what it signals]  | [Which H-ID's incumbent relation does this row address?] | Expected / Surprise | Yes / No |

**Completion rules:**
- At least one row explicitly addresses the incumbent approach — a tension or agreement about
  switching cost, displacement conditions, or coexistence dynamics.
- At least one row records an open, unresolved tension.
- Agreement rows explain why convergence is meaningful given the STEP 0 axis.
- Note whether each row was axis-predicted or a surprise.

---

### STEP 5 — Composite Signal

Synthesizes — does not restate. Removing this section must cost the feature team integrated
judgment not reconstructable from the tables row by row.

Answer all four of the following in 5–7 sentences:

1. **Integrated verdict**: Does the overall evidence strengthen, weaken, or complicate the
   original SIGNAL hypothesis? State directly.

2. **Top-weight findings**: Name the three highest-weight evidence signals from STEP 3 by Q-ID
   and weight (e.g., "S-01 Q2 [weight: 3], S-02 Q4 [weight: 3], S-01 Q5 [weight: 2]"). State
   in one sentence each what each finding implies for the feature decision.

3. **Inertia assessment**: Does the evidence suggest {SIGNAL} can overcome the switching cost
   the incumbent represents? State directly — name the evidence that most directly addresses
   whether {SIGNAL} can displace or complement the incumbent approach declared in STEP 0.

4. **Key open question**: What did these interviews not resolve? What does the feature team
   need to do next?

Cite subjects by ID (S-01, S-02) and hypothesis IDs (H-nn) where relevant.

---

### STEP 6 — Arc Signal

**Required. Write after STEP 5. Must not restate STEP 5 conclusions.**

The Arc Signal answers a question whose scope is wider than {SIGNAL} — what this interview run
reveals about the adoption pattern, the workflow category, or the class of features {SIGNAL}
belongs to, including what it reveals about how incumbents are displaced or defended in this
domain.

| Field | Content |
|-------|---------|
| **Arc question** | [Explicit question whose scope exceeds {SIGNAL}. Must address the adoption or displacement pattern, not just {SIGNAL}'s viability.] |
| **Arc inference** | [Conclusion answering the arc question — not reconstructable from STEP 5 alone. Points beyond this feature to a pattern about how incumbents are displaced in this domain, or how subjects in this category navigate adoption.] |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [specific reason: what the arc inference provides that per-subject findings and the Composite Signal do not]. |
| **Adjacent signal test** | Name an adjacent signal in the same category as {SIGNAL}: [name it]. Does the arc question apply to that adjacent signal equally? [yes / no] — because [one sentence: what the arc question captures that is category-level and not {SIGNAL}-specific, OR why the question would need to change]. |

**Arc self-test verdict format:** The answer must begin with an explicit binary verdict — "yes"
or "no" — followed immediately by a stated rationale. A narrative answer fails. A verdict
without a rationale fails. Evaluator test: can a reviewer identify and challenge the specific
reason stated? If the rationale is too diffuse, revise.

**Adjacent signal test rules:**
- The adjacent signal must be named specifically.
- If the answer is "no — because the arc question would need to change," the arc question is
  still feature-level. Revise before treating STEP 6 as complete.

**Arc self-test rule**: the removal test answer must be "yes." If "no," revise the arc inference.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## Predicted R9 Scores under v8

| Variation | Axis(es) | New candidate(s) | C-18 | C-19 | C-20 | C-21 | Aspirational | Composite |
|-----------|----------|------------------|------|------|------|------|--------------|-----------|
| V-01 R9 (Role Seq: Disposition Table) | Role sequence | C-22 | PASS | PASS | PASS | PASS | 14/14 + C-22? | 100.00 |
| V-02 R9 (Output: Adjacent Signal Field) | Output format | C-23 | PASS | PASS | PASS | PASS | 14/14 + C-23? | 100.00 |
| V-03 R9 (Register: Investigator's Notebook) | Phrasing register | None expected | PASS | PASS | PASS | PASS | 14/14 | 100.00 |
| V-04 R9 (Role Seq + Output combined) | Role seq + Output | C-22 + C-23 | PASS | PASS | PASS | PASS | 14/14 + C-22? + C-23? | 100.00 |
| V-05 R9 (Inertia + Disposition + Scoring) | Inertia + Role seq + Scoring | C-22 + C-24 | PASS | PASS | PASS | PASS | 14/14 + C-22? + C-24? | 100.00 |

---

## What R9 Is Testing

**C-22 (Hypothesis Disposition Table)**: the hypothesis register is opened in STEP 1 (C-10),
enforced with a quality gate in STEP 1 (C-18), and — in R9 variations — explicitly closed in
STEP 3.5 before synthesis begins. The gap C-22 fills: no existing criterion requires the author
to state what happened to each hypothesis after the interviews. An artifact can satisfy C-18
(universal quality gate) and never reference any hypothesis in STEP 5. C-22 makes the lifecycle
closure mandatory: the disposition table is a structural gate between STEP 3 and STEP 4, not a
synthesis option.

**C-23 (Adjacent Signal as Named Arc Output)**: the scope substitution test already exists as an
author instruction in V-01 R8 and all prior full-coverage variations. C-23 converts it from
author instruction to artifact output. The gap: an evaluator verifying C-17 compliance currently
must apply the substitution test independently. With C-23, the evaluator reads the named
adjacent signal and the yes/no verdict in the artifact body. C-23 is to C-17 as C-21 is to
C-20: it converts a verification requirement from external judgment to artifact inspection.

**C-24 (Evidence Impact Weighting + Top-Weight Citation)**: no current criterion requires
evidence to be quantified. A 1-3 impact weight column in the interview table, combined with a
rule requiring the Composite Signal to cite the top-weight findings by Q-ID, creates a
quantification chain. The gap: C-09 requires type tags on evidence. C-15 requires composite
synthesis. Neither requires the synthesis to reference the most decision-relevant evidence by
weight. C-24 closes this gap: the synthesis cannot be agnostic to relative evidence value.

**Phrasing register robustness (V-03 R9)**: tests whether the first-person reflexive register
("I am committing...") preserves criterion compliance as reliably as the imperative register
("Write this before...") or the "you" address register from V-03 R8. No new criterion expected
— this is a robustness test for the structural mechanisms.
