# prove-interview — Rubric v8 Variations — Round 8

_Date: 2026-03-15 · Rubric: v8 (C-01–C-21) · Ceiling: 100_

---

## Context

R7 produced 5 variations. V-01 and V-02 were the single-axis variations that drove the new C-21
criterion in v8. V-03, V-04, and V-05 achieved 14/14 under v8 (their arc self-test templates used
`[yes / no] — because [specific reason]` and their structural rules effectively enforced binary
verdict format).

**R7 scores under v8 (denominator /14):**

| Variation | C-18 | C-21 | Aspirational | Composite |
|-----------|------|------|--------------|-----------|
| V-01 R7 (Role Sequence: STEP 0 + STEP 6 three-field arc) | FAIL | PASS | 13/14 | 99.29 |
| V-02 R7 (Output Format: STEP 0 + combined arc scope/self-test) | FAIL | FAIL | 12/14 | 98.57 |
| V-03 R7 (Lifecycle Emphasis: Phase-Gated Protocol) | PASS | PASS | 14/14 | 100.00 |
| V-04 R7 (Role Sequence + Lifecycle) | PASS | PASS | 14/14 | 100.00 |
| V-05 R7 (Inertia + Full Coverage) | PASS | PASS | 14/14 | 100.00 |

R8 goals:
1. **Single-axis 1** — Role Sequence: close C-18 in the V-01 R7 architecture. Single change:
   STEP 1 gate from "at least one" to "every hypothesis." Tests C-18 in isolation within a STEP
   structure that already achieves C-21 via the three-field arc table. C-21 enforcement rule also
   made explicit (strengthens C-21 enforcement without changing structural form).
2. **Single-axis 2** — Output Format: add explicit C-21 binary verdict enforcement to V-02 R7.
   Single change: arc self-test gets a verdict-format rule. C-18 absent as gap isolation test.
   Tests C-21 in isolation within V-02's combined arc field architecture.
3. **Single-axis 3** — Phrasing Register: new axis not tried in R7 with full 14/14 coverage.
   Conversational register ("you" address, plain English, minimal procedural jargon) while
   maintaining all structural discipline. Tests whether C-21 binary verdict survives a register
   change away from formal gate language.
4. **Combination 1** — Output Format + C-21 + C-18: close both remaining gaps in V-02 R7
   simultaneously. V-02's combined arc field design + explicit C-21 rule + universal quality gate.
5. **Combination 2** — Output Format + Phase Structure: novel hybrid. V-02's combined arc field
   design embedded in V-03's phase structure. Tests whether the V-02 arc field design achieves
   C-21 when placed inside a phase-gated context with explicit verdict-format rule.

---

## Variation Axes

| Axis | R7 result | R8 focus |
|------|-----------|----------|
| Role sequence (STEP structure) | V-01: 13/14 (C-18 FAIL intentional) | Add C-18 universal quality gate — isolates C-18 contribution |
| Output format (combined arc field) | V-02: 12/14 (C-18 FAIL, C-21 FAIL) | Add explicit C-21 binary verdict rule — isolates C-21 contribution; C-18 absent |
| Phrasing register (conversational) | Absent in R7 full-coverage variations | New: all 14 criteria in conversational register |
| Output format + C-21 + C-18 | Not combined | Closes both V-02 gaps simultaneously — full 14/14 via V-02 architecture |
| Output format + Phase structure | Not combined | Hybrid: V-02 arc field design inside V-03 phase gating |

---

## V-01 — Single axis: Role Sequence (V-01 R7 + C-18 universal quality gate)

**Axis:** Role sequence. Single change from V-01 R7: STEP 1 gate changed from "at least one
hypothesis must carry a specific Falsification Condition" to "every declared hypothesis must carry
a specific, non-trivial Falsification Condition." STEP 0 (Opposition Axis Declaration) and STEP 6
(three-field arc table: Arc question + Arc inference + Arc self-test) are unchanged from V-01 R7.
An explicit arc self-test verdict-format rule is added in STEP 6 — this does not change the
structural form (V-01 R7 already satisfies C-21 via the template), but makes the binary commitment
evaluator-facing rather than implicit.

**Hypothesis:** The STEP 1 gate change satisfies C-18 by construction — the evaluator test "could
an author write N hypotheses with no Falsification Conditions and advance?" answers "no" because
the gate condition applies to every H-ID. C-18 PASS. C-19 carries from V-01 R7 (STEP 0 named
structural step before STEP 1). C-21 carries from V-01 R7 (three-field table with `[yes / no] —
because [reason]`; now reinforced with an explicit format rule). C-20 and C-17 pass by cascade.
All prior-round strengths retained. Predicted: C-18 PASS, C-19 PASS, C-20 PASS, C-21 PASS
→ 14/14 → 100.00.

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

## V-02 — Single axis: Output Format (V-02 R7 + C-21 explicit binary verdict enforcement)

**Axis:** Output format. Single change from V-02 R7: an explicit binary verdict format rule is
added in STEP 6 for the arc self-test removal test answer. V-02 R7's combined "Arc scope
confirmation and self-test" field showed `Answer: [yes / no] — because [specific reason]` in the
template but carried no explicit instruction that the format itself was required to be a binary
verdict. C-21 FAIL in R7 was precisely this absence. R8 adds a "Verdict format rule" paragraph
after the STEP 6 table, explicitly requiring yes/no before rationale and stating the evaluator
test for falsifiability. C-18 is NOT addressed: STEP 1 gate retains "at least one" from V-02 R7
(deliberate gap isolation — tests C-21 contribution in isolation).

**Hypothesis:** The explicit verdict format rule satisfies C-21 — an author reading the rule
cannot write a narrative answer and satisfy the format requirement. C-21 PASS. C-19 carries from
V-02 R7 (STEP 0 named structural step). C-20 carries from V-02 R7 (arc self-test field with
author-supplied answer). C-18 absent — no change to STEP 1 gate. Predicted: C-21 PASS, C-18
FAIL, aspirational 13/14, composite 99.29.

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
- Agreement rows explain why the agreement matters or is surprising given the axis declared in
  STEP 0.

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
| **Arc scope confirmation and self-test** | Adjacent signal substitution: [name an adjacent signal and state whether the arc question applies to it equally — yes = arc-level scope, no = revise]. Removal test: if this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state the specific reason: what this arc inference provides that per-subject findings and the Composite Signal do not]. |

**Arc self-test verdict format**: The removal test answer must be structured as an explicit binary
verdict — "yes" or "no" — followed immediately by a stated rationale for that verdict. A
narrative answer that implies a verdict without committing to the binary word fails this
requirement. A binary verdict without a stated rationale also fails. Evaluator test: if a reviewer
disagrees with the verdict, can they identify and challenge the specific reason stated in the
artifact? If the stated reason is too diffuse or qualified to be directly contested, revise
before treating STEP 6 as complete.

**Self-test rule**: the removal test answer must be "yes." An arc inference answerable "no" has
not cleared feature scope — revise before treating STEP 6 as complete.

**Anti-restatement test**: if removing the entire Arc Signal section would leave the feature
team with everything they need to decide about {SIGNAL}, the Arc Signal has not elevated the
synthesis. Revise until removal costs something they cannot reconstruct.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-03 — Single axis: Phrasing Register (conversational-technical, all 14 criteria)

**Axis:** Phrasing register. First time full 14-criterion coverage is attempted in a
conversational-technical register. Prior full-coverage variations (V-03, V-04, V-05 in R7) used
formal procedural language ("This step is a structural prerequisite", "Phase N may not begin
until"). This variation uses a "you" address, plain imperatives, and minimal procedural jargon —
while maintaining identical structural discipline: STEP 0 named opposition axis (C-19), quality
gate requiring every hypothesis to carry a falsification condition (C-18), H-IDs as structural
pre-commit column (C-12), three-field arc table with explicit binary verdict format rule (C-21).
Tests whether the structural guarantees that produce criterion passes are a function of the
mechanisms themselves or of the formal language that describes them.

**Hypothesis:** C-21 survives the register change because the binary verdict requirement is stated
as a content rule ("start with yes or no — the binary word — then give your reason") rather than
procedural jargon. C-18 survives because the quality gate is phrased as a direct instruction
("before moving on, every H-ID row must have a specific falsification condition — not just one or
two, every one") rather than formal gate language. C-19 survives because STEP 0 is still a named
step before STEP 1. C-12 survives because the "H-IDs tested" column is still filled before the
question. All prior-round strengths (C-08 through C-17 from cascade) carry through mechanism, not
language. Predicted: 14/14 → 100.00.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Your goal: simulate interviews with stakeholders or customers about {TOPIC} to build evidence for
or against the {SIGNAL} hypothesis. The interviews are fictional but grounded — every answer must
come from the persona's specific expertise and experience, not general wisdom any person could
offer.

Work through the six steps below in order. Steps with a checkpoint must be completed before the
next step begins.

---

### STEP 0 — Name the axis first [CHECKPOINT]

Before you write a single hypothesis, name the tension axis your two subjects will span. You're
choosing two people at opposite ends of a relevant dimension — not two people who happen to
disagree, but two people structurally positioned on opposite poles of a dimension that matters
for understanding {SIGNAL}.

Fill in this table:

| Field | Your answer |
|-------|-------------|
| **Axis name** | What is the dimension? Name something about how people think, work, or have invested — not their job title or company size. |
| **Why this axis for {SIGNAL}** | One sentence: what you can learn by hearing from both poles that you can't learn from two people at the same pole. |
| **Pole A — the skeptic** | Who lives here? What have they built or invested in that {SIGNAL} would disrupt? What does switching cost them specifically — time, rework, responsibility? |
| **Pole B — the adopter** | Who lives here? What are they missing that {SIGNAL} would give them? What adoption motivation do they carry that Pole A lacks? |
| **What Pole A alone can't tell you** | Name a specific evidence type you'd miss if you only interviewed skeptics. "A different perspective" doesn't count — name the finding. |

You can't write STEP 1 until this table is complete and both poles are genuinely opposite ends of
a named epistemic dimension (not demographic).

---

### STEP 1 — Lock down your hypotheses before interviewing [CHECKPOINT]

Write down every assumption and risk you're carrying into these interviews — before you write any
question or persona answer. The point is to commit before you test.

| ID | Hypothesis | Category | What would falsify this? |
|----|------------|----------|--------------------------|
| H-01 | [what you believe about how {SIGNAL} will land] | assumption / risk / unknown | [what a subject would need to say to force you to reject this — name the evidence type or answer pattern, not "if people disagree"] |
| H-02 | [a risk or concern you expect to surface] | risk | [what interview answer would show this risk doesn't apply] |
| H-03 | [a design question you hope these interviews resolve] | unknown | [what finding would resolve it against your expectation] |
| H-04+ | [add rows — aim for 4 or more] | | |

**Before moving to STEP 2:** check every single H-ID row — every one must have a specific
falsification condition in the last column. Not "if people disagree" — the actual evidence type
or answer pattern that would force you to revise that specific hypothesis. If any row has a blank
or generic condition, fill it in now. This is a quality gate, not a count gate: four hypotheses
each with specific conditions satisfies it; four hypotheses with one specific condition and three
blanks does not.

You cannot proceed to STEP 3 (Interviews) while any H-ID has an empty or generic Falsification
Condition.

---

### STEP 2 — Choose your subjects

Assign each subject to one of the poles you declared in STEP 0. If you can't assign a subject to
a declared pole, they don't belong in this run — replace them.

| ID | Name | Role | Seniority | Pole (STEP 0) | What grounds their pole |
|----|------|------|-----------|---------------|-------------------------|
| S-01 | | | | Pole A / Pole B | [what specifically makes this persona a Pole A or Pole B subject — their investment, belief, or capability gap] |
| S-02 | | | | Pole A / Pole B | [what distinguishes their pole position from S-01's] |

Minimum 2 subjects, one from each pole.

---

### STEP 3 — Run the interviews

Don't write any interview content until STEP 0, STEP 1, and STEP 2 are done. The H-IDs and pole
assignments must exist before any answers appear.

For each subject, write their identity first, then their interview table.

#### [S-nn] — Who they are

2–3 sentences: where they work or what context they operate in, what they've built or are
responsible for, at least one concrete concern or event that makes this persona specific. A reader
should be able to tell which axis pole they're on just from reading this paragraph.

Quick check: substitute another persona's name into this paragraph. If the interview answers
would still read as plausible for that other persona, add specifics until the answer is no.

#### [S-nn] — Interview

Fill the "H-IDs tested" column before writing each question. A question row without a completed
H-IDs column may not be written.

| Q# | H-IDs tested | Question | Answer (their voice) | Evidence [type: ...] | Surprise? |
|----|--------------|----------|---------------------|---------------------|-----------|
| Q1 | H-nn | [question, written after H-IDs column is filled] | [answer using this persona's vocabulary, domain concerns, and context — not general wisdom] | [risk / preference / constraint / validation / invalidation]: [one-sentence interpretation] | Yes — expected [X], found [Y] / No |
| Q2 | H-nn | | | | |
| Q3 | H-nn | | | | |

Rules:
- Fill "H-IDs tested" before writing the question in that row.
- Every answer must be specific to this persona — another persona's name can't be dropped in
  and have the answer still work. Generic wisdom fails the swap test.
- Every evidence entry needs a type tag and a one-sentence interpretation.
- At least one "Yes" in the Surprise column per person, with what you expected vs. what you found.
- Minimum 3 rows per subject.

When a STEP 1 falsification condition gets triggered:
> **[FALSIFICATION — H-nn triggered]:** The condition was: [exact text from STEP 1]. They said:
> [answer]. This means: [how it forces revision of H-nn].

---

### STEP 4 — Compare subjects against each other

After all interview tables are done, build the tensions comparison.

| What's being compared [H-ID if relevant] | S-01's position | S-02's position | What it tells us | Axis-predicted? | Still open? |
|------------------------------------------|-----------------|-----------------|------------------|-----------------|-------------|
| [shared dimension, H-ID, or axis concern] | [S-01 stated view] | [S-02 stated view] | TENSION: [what the disagreement signals] / AGREEMENT: [why convergence here is notable given the axis] | Expected / Surprise | Yes / No |

Rules:
- At least one row that's genuinely unresolved — leave it open, don't paper over it.
- Agreement rows need to explain why the convergence matters given the STEP 0 opposition axis.
  "Both agreed" without an explanation doesn't satisfy this.
- Note whether each row was predicted by the STEP 0 axis or was a surprise.

---

### STEP 5 — Synthesize, don't restate

Write 4–6 sentences integrating the evidence into a conclusion. If you can remove this section
and the artifact says the same things, it's not done yet — synthesis adds integrated judgment,
not a restatement of what each person said.

Answer all three:
1. Does the evidence strengthen, weaken, or complicate the {SIGNAL} hypothesis? Say it directly.
2. What's the single most decision-relevant finding across all subjects? Name the specific
   finding — not a theme.
3. What did these interviews not resolve? What does the feature team need to do next?

Cite subjects by ID and hypothesis IDs where relevant.

---

### STEP 6 — Arc signal

Write this after STEP 5. Required. Must not repeat conclusions from STEP 5.

The arc signal answers a question wider than {SIGNAL}. What does this interview run tell you
about the adoption pattern, the workflow category, or the class of features {SIGNAL} belongs to?
Not whether {SIGNAL} works — what this run reveals about the broader context it lives in.

| Field | Content |
|-------|---------|
| **Arc question** | A question whose scope exceeds {SIGNAL}. Check: would a different but adjacent signal in the same category generate this same arc question? If yes, scope is right. If the arc question would need to change for the adjacent signal, it's still feature-level — revise. |
| **Arc inference** | A conclusion answering the arc question that a reader can't reconstruct from STEP 5 alone. It points beyond this feature to a pattern about adoption, the workflow, or the user type. |
| **Arc self-test** | If this arc inference were removed, would the feature team lose something they can't reconstruct from the per-subject findings and the STEP 5 synthesis? Answer: [yes / no] — because [state the specific reason: what the arc inference provides that the rest of the artifact does not]. |

**Arc self-test format:** Your answer must start with the binary word — "yes" or "no" — followed
immediately by your stated rationale. Don't write a paragraph that implies an answer without
committing to the word. Don't write the word without explaining why. Both halves are required.
The test for the rationale: if someone disagreed with your verdict, could they find and challenge
the specific reason you wrote? If your rationale is too vague to be directly contested, rewrite
it until it is.

The answer must be "yes." An arc inference the team can do without hasn't cleared feature scope
— revise until removing it genuinely costs them something they can't get elsewhere.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-04 — Combination: Output Format + C-21 + C-18 (both V-02 gaps closed)

**Axes:** Output Format (V-02 architecture) with both remaining gaps closed simultaneously.
V-02 R7 failed C-18 (gate quality) and C-21 (arc verdict format). V-03 R8 closes C-21 in
isolation. V-01 R8 closes C-18 in isolation (different architecture). This combination variant
closes both within V-02's output format architecture — combined arc scope/self-test field,
simpler roster table, no H-IDs pre-commit column — by adding (a) the universal quality gate to
STEP 1 and (b) the explicit binary verdict format rule to STEP 6.

**Hypothesis:** STEP 1 universal quality gate satisfies C-18 (every H-ID must have a specific
Falsification Condition; the evaluator test is built into the gate instruction). STEP 6 explicit
verdict format rule satisfies C-21 (binary word + rationale required; evaluator challenge test
stated explicitly). C-19 carries from V-02 R7 (STEP 0 named step before STEP 1). C-20 carries
from V-02 R7 (arc self-test field with author-supplied answer). All four closing R7 criteria pass
by construction within V-02's output format. Predicted: C-18 PASS, C-19 PASS, C-20 PASS, C-21
PASS → 14/14 → 100.00.

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
at genuinely opposite ends of the named axis. A demographic axis does not satisfy the gate.

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
- **Every declared hypothesis must carry a specific, non-trivial Falsification Condition.** A
  hypothesis row with an empty Falsification Condition, or a condition that reads "if people
  disagree" or "if objections arise," does not satisfy this gate for that row. State the specific
  evidence type, answer pattern, or finding that would force rejection of that specific
  hypothesis. The gate requires all H-IDs to satisfy the condition — not "at least one."
- Register is locked once written. Do not revise after any interview table row is written.

**Gate evaluator test:** Could an author write four hypotheses with empty Falsification Conditions
and advance to STEP 3? If yes, this gate fails. STEP 3 may not begin while any H-ID has an empty
or generic Falsification Condition.

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
- Agreement rows explain why the agreement matters or is surprising given the STEP 0 axis.

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
| **Arc scope confirmation and self-test** | Adjacent signal substitution: [name an adjacent signal and state whether the arc question applies to it equally — yes = arc-level scope, no = revise]. Removal test: if this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state the specific reason: what this arc inference provides that per-subject findings and the Composite Signal do not]. |

**Arc self-test verdict format**: The removal test answer must be structured as an explicit binary
verdict — "yes" or "no" — followed immediately by a stated rationale. A narrative answer that
implies a verdict without committing to the binary word fails. A verdict without a stated rationale
fails. Evaluator test: if a reviewer disagrees with the verdict, can they identify and challenge
the specific reason stated in the artifact? If the rationale is too diffuse or qualified to be
directly contested, revise before treating STEP 6 as complete.

**Self-test rule**: the removal test answer must be "yes." An arc inference the team can do without
has not cleared feature scope — revise before treating STEP 6 as complete.

**Anti-restatement test**: if removing the entire Arc Signal section would leave the feature
team with everything they need to decide about {SIGNAL}, the Arc Signal has not elevated the
synthesis. Revise until removal costs something they cannot reconstruct.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-05 — Combination: Output Format + Phase Structure (V-02 arc field inside V-03 phase gating)

**Axes:** Output format (V-02's combined arc scope/self-test field) + lifecycle emphasis (V-03's
phase-gated protocol). V-03 R7 demonstrated that phase gating is the natural carrier for C-18
and C-19 simultaneously. V-02 R7 demonstrated a compact combined arc field design that passed
C-20 without the separate three-field table. This combination tests whether V-02's arc field
design achieves C-21 when placed inside a phase-gated context that includes an explicit binary
verdict rule, and whether V-03's phase structure carries V-02's arc format without degradation.

**Hypothesis:** Phase 0 as a named structural phase before Phase 1 satisfies C-19 by
construction. Phase 1 universal quality gate ("each declared hypothesis must carry a specific
falsification condition before Phase 2 may begin") satisfies C-18 by construction. Phase 2 H-IDs
tested pre-commit column satisfies C-12. Phase 3's V-02-style combined arc scope/self-test field
with an explicit binary verdict format rule satisfies C-21. The format hybrid is the novel test:
V-02's combined field passed C-20 but failed C-21 in R7; placing it inside V-03's phase context
with the explicit verdict rule added should satisfy both. Predicted: C-18 PASS, C-19 PASS, C-20
PASS, C-21 PASS → 14/14 → 100.00.

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
falsification conditions and still advance to Phase 2? If yes, the gate fails. The gate
is only satisfied when no H-ID has an empty or generic falsification condition.

**Phase 2 may not begin while any H-ID has an unsatisfied falsification condition.**

#### Subject Roster

Each subject must be assigned to a pole declared in Phase 0 before their background is written.

| ID   | Name   | Role   | Seniority | Axis Pole (Phase 0)  | Domain Expertise                                          |
|------|--------|--------|-----------|----------------------|-----------------------------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B      | [specific expertise or investment grounding their pole]   |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B      | [expertise distinct from S-01 grounding their pole]       |

Minimum 2 subjects, one from each declared pole. A subject not assignable to a declared pole
does not belong in this run — replace before advancing.

**Phase 1 complete when:** every H-ID has a specific falsification condition AND the
axis-assigned roster is written.

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
- Answers fail the swap test.
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
   subjects converge unexpectedly? What does the convergence or divergence signal?

#### Arc Signal

**Write this section after the Composite Signal. It is required. It must not restate
feature-level conclusions from the Composite Signal.**

The Arc Signal answers a question whose scope is wider than {SIGNAL} — what this interview run
reveals about the adoption pattern, the workflow category, or the class of features {SIGNAL}
belongs to.

| Field | Content |
|-------|---------|
| **Arc question** | [State an explicit question wider than {SIGNAL}. Scope test: would a different but adjacent signal generate the same arc question? If yes, the scope is confirmed arc-level.] |
| **Arc inference** | [State a conclusion that answers the arc question. A reader must not be able to reconstruct this inference from the Composite Signal alone. Points to a pattern about adoption, the workflow, or the user type beyond this specific feature.] |
| **Arc scope confirmation and self-test** | Adjacent signal check: [name one adjacent signal]. Arc question applies to it equally: [yes / no — if no, revise the arc question]. — Removal test: if this arc inference were removed, would the feature team lose something not reconstructable from the feature evidence alone? Answer: [yes / no] — because [state the specific reason: what this arc inference provides that per-subject findings and the Composite Signal do not]. |

**Arc self-test verdict format**: The removal test answer must begin with an explicit binary
verdict — "yes" or "no" — followed immediately by a stated rationale. A narrative that implies
a verdict without committing to the binary word fails. A verdict without a rationale fails.
Evaluator test: if a reviewer disagrees with the verdict, can they locate and challenge the
specific reason stated? If the rationale cannot be directly contested, revise before treating
Phase 3 as complete.

**Self-test rule**: the removal test must answer "yes." An arc inference the team can do without
has not cleared feature scope — revise the inference until removing it genuinely costs the
feature team information they cannot reconstruct.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## Axis Coverage Summary

| Axis                                   | V-01    | V-02    | V-03      | V-04              | V-05              |
|----------------------------------------|---------|---------|-----------|-------------------|-------------------|
| Role sequence (STEP 0 + STEP 6)        | PRIMARY | PRESENT | —         | PRESENT           | —                 |
| Output format (combined arc field)     | —       | PRIMARY | —         | PRIMARY           | PRIMARY           |
| Lifecycle emphasis (phase gates)       | —       | —       | —         | —                 | PRIMARY           |
| Phrasing register (conversational)     | —       | —       | PRIMARY   | —                 | —                 |
| C-18 universal quality gate            | ADDED   | —       | PRESENT   | ADDED             | PRESENT           |
| C-21 explicit verdict format rule      | ADDED   | ADDED   | PRESENT   | ADDED             | ADDED             |

---

## Predicted R8 Scores (v8 rubric, denominator /14)

| Variation | C-18 | C-19 | C-20 | C-21 | C-12 | Aspirational | Composite |
|-----------|------|------|------|------|------|--------------|-----------|
| V-01 (Role Sequence + C-18 universal gate) | PASS | PASS | PASS | PASS | PASS | 14/14 | 100.00 |
| V-02 (Output Format + C-21 explicit) | FAIL | PASS | PASS | PASS | PASS | 13/14 | 99.29 |
| V-03 (Phrasing Register, all 14 criteria) | PASS | PASS | PASS | PASS | PASS | 14/14 | 100.00 |
| V-04 (Output Format + C-21 + C-18) | PASS | PASS | PASS | PASS | PASS | 14/14 | 100.00 |
| V-05 (Output Format + Phase Structure) | PASS | PASS | PASS | PASS | PASS | 14/14 | 100.00 |

*V-01: Single change from V-01 R7 — STEP 1 gate now requires every H-ID to carry a specific
falsification condition ("not 'at least one'"). Evaluator test embedded in gate instruction makes
C-18 pass by construction. C-19 carries (STEP 0 unchanged). C-21 carries and is now reinforced
with an explicit verdict-format rule. C-12 carries (STEP 3 H-IDs column unchanged from V-01 R7).
Full 14/14.*

*V-02: Single change from V-02 R7 — arc self-test verdict format rule added in STEP 6. The rule
explicitly states: binary word first, rationale second, evaluator-challenge test included. C-18
absent — STEP 1 gate retains "at least one" condition from V-02 R7. This is the single-axis
isolation test for C-21 within V-02's architecture. C-19 carries (STEP 0 unchanged from V-02 R7).
C-20 carries (self-test field with author-supplied answer). 13/14.*

*V-03: New axis — phrasing register. All structural mechanisms present but expressed in
conversational-technical register ("you" address, plain imperatives, plain English gate language).
C-19 PASS: STEP 0 named step before STEP 1. C-18 PASS: quality gate phrased as "before moving
on, every H-ID row must have a specific falsification condition — not just one or two, every one."
C-12 PASS: "H-IDs tested" pre-commit column with instruction "fill this before writing the
question." C-21 PASS: "start with yes or no — the binary word — then give your reason" is
structurally equivalent to the formal verdict-format rule. All cascade chains preserved. 14/14.*

*V-04: Both V-02 R7 gaps closed within V-02's output format architecture. STEP 1 universal
quality gate (evaluator test embedded) satisfies C-18. STEP 6 explicit verdict format rule
satisfies C-21. STEP 0 and arc field structure unchanged from V-02 R7 — C-19 and C-20 carry.
This variation answers the question: can V-02's combined arc field design achieve all 14 criteria?
14/14.*

*V-05: Novel hybrid. V-02's combined arc scope/self-test field placed inside V-03's four-phase
gating structure. Phase 0 satisfies C-19. Phase 1 universal quality gate satisfies C-18. Phase 2
H-IDs pre-commit column satisfies C-12. Phase 3 arc section uses V-02's combined field format
with explicit verdict-format rule — satisfies C-20 (author-supplied self-test answer in artifact
body) and C-21 (binary verdict required by explicit rule). The hybrid test: does V-02's arc field
achieve C-21 when placed inside a phase context rather than a STEP context? Predicted: yes —
because C-21 is a content requirement on the arc self-test answer, independent of whether the
containing structure is STEP-based or PHASE-based. 14/14.*

---

## What R8 Should Tell Us

**H-single-1**: Does the V-01 R7 architecture reach 14/14 when only the STEP 1 gate changes?
Predicted: yes — C-18 is the only gap in V-01 R7 under v8, and the gate change is a pure
mechanism addition that does not interact with any other criterion. If V-01 R8 fails at any
criterion other than C-18, a previously invisible structural interaction exists.

**H-single-2**: Does explicit binary verdict enforcement (without C-18) push V-02 from 12/14 to
13/14? Predicted: yes — the verdict format rule is a self-contained addition to STEP 6 that does
not interact with STEP 1. If V-02 R8 fails at C-20 (which should carry from V-02 R7), the added
rule degraded the arc section rather than strengthening it.

**H-register**: Does the conversational-technical register survive full structural discipline
(14/14) without the formal gate language? Predicted: yes — the mechanisms that generate criterion
passes are structural (STEP 0 before STEP 1, every-H quality condition, pre-commit column, binary
verdict rule), not linguistic. The phrasing register changes the surface while preserving the
structure. If V-03 R8 fails at any aspirational criterion, a specific mechanism was accidentally
removed in the register translation, identifying an interaction between phrasing and structural
enforcement.

**H-combo-1**: Does closing both V-02 gaps simultaneously achieve 14/14 within V-02's architecture?
Predicted: yes — the two changes (quality gate + verdict format rule) are independent and do not
interact. If V-04 fails at any criterion V-02 R7 passed, a structural interaction between
quality gating and the combined arc field architecture exists.

**H-combo-2**: Does the phase structure successfully host V-02's combined arc field design
while adding C-21 compliance? Predicted: yes — the phase structure provides C-18 and C-19 by
construction; the arc field provides C-20; the verdict rule adds C-21. The format hybrid should
inherit all four from their respective mechanisms without interference.
