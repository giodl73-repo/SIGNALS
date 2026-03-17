# prove-interview — R14 Variations (v13 Rubric)

**Skill:** prove-interview
**Round:** R14
**Rubric version:** v13
**Topic:** Signal Lineage View — a Signal plugin feature that visualizes the full chain from hypothesis to evidence to disposition to arc verification for a given topic, enabling teams to audit signal completeness before committing to a build decision.

---

## Variation Summary

| Var | Axis | C-27 | C-28 | C-29 | Projected Ceiling |
|-----|------|------|------|------|-------------------|
| V-01 | Register Format + Sample Rows (WHERE + WHAT) | PASS | FAIL | PASS | 21/22 |
| V-02 | Lifecycle Emphasis Only (WHEN without WHERE) | FAIL | FAIL* | — | C-26 PASS / C-27 FAIL |
| V-03 | Lifecycle Step Naming (WHERE + WHEN without WHAT) | PASS | PASS | FAIL | 21/22 |
| V-04 | Role Sequence + Register Format (WHERE + WHAT + ordering) | PASS | FAIL | PASS | 21/22 |
| V-05 | Canonical (WHERE + WHEN + WHAT) | PASS | PASS | PASS | 22/22 → 100.00 |

*V-02 C-28 fails by construction: C-28 requires the Arc-Verified column to exist as a named target; without it the step cannot satisfy criterion 1.

---

## V-01 — Register Format + Sample Rows (WHERE + WHAT)

**Axis:** Output format — STEP 3.5 register skeleton includes the Arc-Verified column header plus labeled example rows in the table body demonstrating both legal entry forms (affirmative `Y / Q-nn` and null `N / —`). No named arc-loop closure lifecycle step is present; the arc population instruction is embedded as prose within STEP 6.

**Hypothesis:** Providing both the column definition (WHERE) and in-table example rows (WHAT) satisfies C-27 and C-29 by construction, but the absence of a named dedicated lifecycle step (no STEP 6.5 or equivalent) leaves C-28 unmet. Projected ceiling: 21/22 aspirational.

---

```
Skill: prove-interview
Topic: Signal Lineage View

Conduct a simulated stakeholder interview investigation for the Signal Lineage View feature —
a Signal plugin capability that renders the full hypothesis → evidence → disposition →
arc-verification chain for any topic, so teams can verify signal completeness before a build
commit.

Produce the artifact in the exact phase order below. Do not begin a later phase until the
prior phase gate is satisfied.

---

STEP 0 — Opposition Axis Declaration

Before declaring any hypothesis or persona, state the axis of epistemic opposition driving
subject selection.

Format:

  Axis: [name the axis]
  Pole A: [label] — [one-sentence epistemic position]
  Pole B: [label] — [one-sentence epistemic position]
  Relevance: [one sentence: why this axis surfaces the most critical unknowns about Signal
  Lineage View]

This step is a structural precondition for STEP 1. No persona may be declared until the
opposition axis is committed.

---

STEP 1 — Subject Profiles

Declare two interview subjects, one per opposition pole. For each:
- Role and experience domain
- Prior knowledge relevant to Signal Lineage View
- Declared concerns or primary interest
- Opposition pole occupied (explicit label matching STEP 0)
- Pairing rationale: what specific question this opposition is designed to answer about the
  feature

---

STEP 2 — Hypothesis Register

Declare H-01 through H-04. Each entry must include:
1. The hypothesis statement
2. A falsification condition: what finding from the interview would force rejection of this
   hypothesis — not just "if they disagree" but the specific evidence type that would require
   the team to abandon the hypothesis

Phase gate: STEP 3 (interview transcripts) cannot begin until every H-ID carries a stated
falsification condition. An H-ID with a hypothesis statement but no falsification condition
is structurally incomplete and blocks the gate.

---

STEP 3 — Interview Transcripts

Conduct one simulated interview per subject. Q-numbering is sequential across both subjects
(Subject 1: Q-01 onward; Subject 2: continues from where Subject 1 left off).

For each interview:
- Open by confirming the subject's role and concerns (consistent with STEP 1 — no new
  attributes may be introduced)
- Ask at least 6 questions
- Each question references at least one H-ID in brackets: [H-nn]
- Include at least one failure-mode probe: what would this subject do if Signal Lineage View
  produced an incomplete or incorrect chain — missing a disposition, misattributing evidence,
  or failing to render arc-verification status?
- Record all answers in the subject's authentic voice, consistent with their declared
  expertise and concerns. No answer may invoke knowledge or capabilities the subject was not
  declared to possess.

---

STEP 3.5 — Hypothesis Disposition Register

After all transcripts are complete, close the hypothesis register. Produce the table below
with all four columns populated for every H-ID row. The two labeled example rows demonstrate
both legal Arc-Verified entry forms and must remain in the table body:

| H-ID | Disposition | Evidence Citation | Arc-Verified |
|------|-------------|-------------------|--------------|
| *[example — affirmative]* | CONFIRMED | Q-05 | Y / Q-05 |
| *[example — null]* | CHALLENGED | Q-11 | N / — |
| H-01 | CONFIRMED / CHALLENGED / FALSIFIED / UNRESOLVED | Q-nn | *(populate after STEP 6)* |
| H-02 | | | |
| H-03 | | | |
| H-04 | | | |

Column definitions:

- Disposition: what the evidence did to this hypothesis. CONFIRMED (evidence supports the
  hypothesis as stated), CHALLENGED (evidence partially undermines it without forcing
  rejection), FALSIFIED (evidence forces rejection — the falsification condition from STEP 2
  was met), UNRESOLVED (no evidence bearing on this hypothesis — requires a stated reason;
  UNRESOLVED without a reason fails).
- Evidence Citation: the Q-ID of the primary evidence row from the evidence table that drives
  the disposition.
- Arc-Verified: whether this H-ID's cited evidence was subsequently verified as
  signal-specific in the arc test. Entry format: Y / Q-nn (affirmative — Q-nn is the Q-ID
  from the adjacent signal test field that received arc verification) or N / — (null — this
  H-ID's evidence was not the arc-verified finding). Populate this column after completing the
  arc signal section at STEP 6.

After completing the arc table at STEP 6, return to this table and populate the Arc-Verified
column for every H-ID row before proceeding to STEP 7.

---

STEP 4 — Evidence Table

Produce the full evidence table covering all Q-IDs from both interviews:

| Q-ID | Subject | Question Summary | Finding | Signal Type | Impact Weight |
|------|---------|-----------------|---------|-------------|---------------|

- Signal Type: one of [risk], [preference], [constraint], [validation], [invalidation]
- Impact Weight: H / M / L — values must be differentiated across rows (not all identical).
  At least one row must carry H weight.

The H-weight row(s) identified here drive the composite signal at STEP 7. Note which row(s)
carry H weight; they will be cited by Q-ID in the composite.

---

STEP 5 — Cross-Subject Tensions Table

| # | Subject A position | Subject B position | Status (Open / Resolved) |
|---|-------------------|--------------------|--------------------------|

Rules:
- At least one tension must be left Open (an unresolved epistemic gap between subjects, not
  explained away or attributed to misunderstanding)
- Agreement rows may be noted but do not count toward tension coverage
- Each row must represent a genuine difference in epistemic position, not a difference in
  phrasing

---

STEP 6 — Arc Signal

Produce a four-row arc table:

| Field | Content |
|-------|---------|
| Arc question | A question whose scope is wider than Signal Lineage View — what this investigation reveals about how [user type] navigates [workflow category] more broadly. This question cannot be answered by feature-level findings alone. |
| Arc inference | The answer to the arc question, stated as a conclusion distinct from any feature-level finding. It must say something about the user type and workflow category that is not already captured in the per-subject evidence. |
| Evaluator self-test | "If this arc inference were removed, would the feature team lose something not reconstructable from the feature-level evidence? Answer: Yes / No — because [stated reason]." |
| Adjacent signal test | "Adjacent signal: [name a specific Signal plugin skill]. Arc question applies equally to it: Yes / No — because [reason]. H-weight finding: Q-[nn] is [signal-specific / portable] — because [reason]. Q-[nn] supports H-[nn] [CONFIRMED / CHALLENGED / FALSIFIED]." |

After completing the arc table, populate the Arc-Verified column in the hypothesis
disposition register at STEP 3.5 using the Q-ID from the adjacent signal test field.

---

STEP 7 — Composite Signal

A dedicated synthesis section — distinct from per-subject evidence, the tensions table, and
the arc signal. This section must:
- Name the H-weight Q-ID(s) explicitly as the finding driving the composite verdict
- State a single artifact-level signal conclusion that synthesizes all subjects, all
  findings, and all tensions

If this section were removed, the artifact must communicate less — the composite conclusion
must not be reconstructable from per-subject evidence alone.
```

---

## V-02 — Lifecycle Emphasis Only (WHEN without WHERE)

**Axis:** Lifecycle emphasis — arc-loop closure described at the synthesis boundary as a prose instruction to annotate the register, without defining an Arc-Verified column in STEP 3.5 or providing any column definition. The register template has three columns only.

**Hypothesis:** Instructing the author to "close the arc loop" at the end of STEP 6 without naming the Arc-Verified column produces a prose annotation rather than a table column entry. C-26 passes (an explicit cross-reference from arc evidence to the register exists) but C-27 fails (no dedicated Arc-Verified column — prose annotation does not satisfy the format-structural requirement). C-28 fails by construction: a lifecycle step cannot name Arc-Verified as the population target if the column does not exist.

---

```
Skill: prove-interview
Topic: Signal Lineage View

Conduct a simulated stakeholder interview investigation for the Signal Lineage View feature —
a Signal plugin capability that renders the full hypothesis → evidence → disposition →
arc-verification chain for any topic, so teams can verify signal completeness before a build
commit.

Produce the artifact in the phase order below. Do not advance to a later phase until the
prior phase is complete.

---

STEP 0 — Opposition Axis Declaration

Before any hypothesis or persona: state the axis of epistemic opposition. Name two poles and
explain why this axis surfaces the most critical unknowns about Signal Lineage View.

  Axis: [name]
  Pole A: [label + epistemic position]
  Pole B: [label + epistemic position]
  Relevance: [one sentence]

---

STEP 1 — Subject Profiles

Declare two interview subjects, one per pole. For each: role, experience domain, prior
knowledge of Signal Lineage View, declared concerns, opposition pole occupied, and pairing
rationale.

---

STEP 2 — Hypothesis Register

Declare H-01 through H-04. For each:
- Hypothesis statement
- Falsification condition: the specific finding that would force rejection

Phase gate: interviews do not begin until all four hypotheses carry stated falsification
conditions.

---

STEP 3 — Interview Transcripts

One interview per subject, with sequential Q-numbering across both. Each interview: 6+
questions, each referencing at least one H-ID. At least one failure-mode probe per interview:
what would this subject do if Signal Lineage View produced an incorrect or incomplete chain?
Record answers in the subject's voice consistent with their declared profile.

---

STEP 3.5 — Hypothesis Disposition Register

After all transcripts, close the hypothesis register:

| H-ID | Disposition | Evidence Citation |
|------|-------------|-------------------|
| H-01 | CONFIRMED / CHALLENGED / FALSIFIED / UNRESOLVED | Q-nn |
| H-02 | | |
| H-03 | | |
| H-04 | | |

Disposition labels: CONFIRMED, CHALLENGED, FALSIFIED, UNRESOLVED. Each H-ID must cite at
least one Q-ID. UNRESOLVED requires a stated reason.

---

STEP 4 — Evidence Table

| Q-ID | Subject | Question Summary | Finding | Signal Type | Impact Weight (H/M/L) |
|------|---------|-----------------|---------|-------------|----------------------|

Signal types: [risk], [preference], [constraint], [validation], [invalidation]. Impact
weights must be differentiated. At least one H-weight row required.

---

STEP 5 — Cross-Subject Tensions Table

| # | Subject A position | Subject B position | Status |
|---|-------------------|--------------------|--------|

At least one Open tension required.

---

STEP 6 — Arc Signal

Produce a four-row arc table:

| Field | Content |
|-------|---------|
| Arc question | Wider-than-feature question: what this investigation reveals about how [user type] navigates [workflow category] more broadly. |
| Arc inference | Answer to the arc question, distinct from feature-level findings. |
| Evaluator self-test | "If this arc inference were removed, would the feature team lose something not reconstructable from feature-level evidence? Answer: Yes / No — because [reason]." |
| Adjacent signal test | "Adjacent signal: [specific Signal plugin skill]. Arc question applies equally: Yes / No — because [reason]. H-weight finding: Q-[nn] is [signal-specific / portable] — because [reason]. Q-[nn] supports H-[nn] [CONFIRMED / CHALLENGED / FALSIFIED]." |

After completing the arc table, close the arc loop: return to the hypothesis disposition
register at STEP 3.5 and annotate any H-ID whose evidence was cited in the adjacent signal
test field. Record whether that evidence was verified as signal-specific or portable, and
which Q-ID was involved.

---

STEP 7 — Composite Signal

Synthesize all evidence across subjects, all findings, and all tensions into a single
artifact-level conclusion. Name the H-weight Q-ID(s) driving the composite verdict.
```

---

## V-03 — Lifecycle Step Naming (WHERE + WHEN without WHAT)

**Axis:** Lifecycle emphasis — named STEP 6.5 arc-loop closure step explicitly references the Arc-Verified column by name as the population target and identifies the adjacent signal test field as the Q-ID source. STEP 3.5 defines the Arc-Verified column with a format-notation description but contains no pre-populated example rows in the table body.

**Hypothesis:** A named lifecycle step that names Arc-Verified as the column target (C-28) combined with a column definition (C-27) but without in-table example rows demonstrating both entry forms produces C-28 PASS and C-27 PASS but C-29 FAIL. The WHAT dimension — format compliance by demonstration — remains ambiguous. Projected ceiling: 21/22 aspirational.

---

```
Skill: prove-interview
Topic: Signal Lineage View

Conduct a simulated stakeholder interview investigation for the Signal Lineage View feature —
a Signal plugin capability that renders the full hypothesis → evidence → disposition →
arc-verification chain for any topic, so teams can verify signal completeness before a build
commit.

Produce the artifact in the exact phase order below. Phase gates are structural: a later
phase cannot begin until the named prior gate condition is satisfied.

---

STEP 0 — Opposition Axis Declaration

Before any hypothesis or persona is declared, state the opposition axis:

  Axis: [name]
  Pole A: [label] — [one-sentence epistemic position]
  Pole B: [label] — [one-sentence epistemic position]
  Relevance: [why this axis surfaces the most critical unknowns about Signal Lineage View]

Structural precondition for STEP 1: the hypothesis register cannot be opened until the
opposition axis is committed in this step.

---

STEP 1 — Subject Profiles

Declare two subjects, one per pole: role, experience domain, prior knowledge of Signal
Lineage View, declared concerns, opposition pole occupied (explicit label), and pairing
rationale.

---

STEP 2 — Hypothesis Register

Declare H-01 through H-04. Each must state:
1. The hypothesis
2. Falsification condition: what specific finding would force rejection

Phase gate: STEP 3 cannot begin until every H-ID has a stated falsification condition. Each
gate check applies the same quality standard — a hypothesis without a falsification condition
cannot be locked.

---

STEP 3 — Interview Transcripts

One interview per subject. Q-numbers are sequential across both subjects.

For each interview:
- Open by confirming role and concerns from STEP 1 (no new attributes)
- 6+ questions, each referencing at least one H-ID in brackets
- At least one failure-mode probe: what does this subject do if Signal Lineage View renders
  an incomplete chain — a hypothesis present but disposition missing, or an arc-verification
  status blank?
- Answers recorded in the subject's voice, consistent with declared expertise

---

STEP 3.5 — Hypothesis Disposition Register

After all transcripts, close the hypothesis register. Produce the table — all four columns
present. Leave Arc-Verified blank until STEP 6.5 executes:

| H-ID | Disposition | Evidence Citation | Arc-Verified |
|------|-------------|-------------------|--------------|
| H-01 | CONFIRMED / CHALLENGED / FALSIFIED / UNRESOLVED | Q-nn | (populate at STEP 6.5) |
| H-02 | | | |
| H-03 | | | |
| H-04 | | | |

Column definitions:
- Disposition: CONFIRMED, CHALLENGED, FALSIFIED, or UNRESOLVED (requires stated reason)
- Evidence Citation: Q-ID driving the disposition
- Arc-Verified: format Y / Q-nn (affirmative) or N / — (null). Populated during STEP 6.5.

---

STEP 4 — Evidence Table

| Q-ID | Subject | Question Summary | Finding | Signal Type | Impact Weight |
|------|---------|-----------------|---------|-------------|---------------|

Signal types: [risk], [preference], [constraint], [validation], [invalidation]. Impact
weights: H / M / L — differentiated values required. At least one H-weight row.

---

STEP 5 — Cross-Subject Tensions Table

| # | Subject A position | Subject B position | Status (Open / Resolved) |
|---|-------------------|--------------------|--------------------------|

At least one Open tension. Agreement rows do not count toward tension coverage.

---

STEP 6 — Arc Signal

Produce a four-row arc table:

| Field | Content |
|-------|---------|
| Arc question | A question whose scope is wider than Signal Lineage View — what this investigation reveals about how [user type] navigates [workflow category] more broadly. Not answerable from feature-level findings alone. |
| Arc inference | Answer to the arc question, stated as a conclusion distinct from any feature-level finding. |
| Evaluator self-test | "If this arc inference were removed, would the feature team lose something not reconstructable from feature-level evidence? Answer: Yes / No — because [stated reason]." |
| Adjacent signal test | "Adjacent signal: [specific Signal plugin skill]. Arc question applies equally: Yes / No — because [reason]. H-weight finding: Q-[nn] is [signal-specific / portable] — because [reason]. Q-[nn] supports H-[nn] [CONFIRMED / CHALLENGED / FALSIFIED]." |

Phase gate: STEP 6 is complete when all four rows are populated, the adjacent signal test
names a specific adjacent signal (not generic), cites a Q-ID by number, and states a
disposition label from the register.

---

STEP 6.5 — Arc-Loop Closure

After STEP 6 is complete, populate the Arc-Verified column in the hypothesis disposition
register at STEP 3.5.

Procedure:
1. Identify the Q-ID cited in the adjacent signal test field as the H-weight finding.
2. In the STEP 3.5 register, locate the H-ID whose Evidence Citation matches that Q-ID.
3. Set that H-ID's Arc-Verified entry to Y / Q-[nn], where Q-nn is the Q-ID from the
   adjacent signal test field.
4. Set all remaining H-ID Arc-Verified entries to N / —.

Phase gate: STEP 7 (Composite Signal) cannot begin until every H-ID row in the STEP 3.5
register has a non-empty Arc-Verified entry — Y / Q-nn or N / —. A blank Arc-Verified cell
constitutes an incomplete register and blocks the gate.

---

STEP 7 — Composite Signal

A dedicated synthesis section distinct from per-subject evidence, the tensions table, and the
arc signal. Must name the H-weight Q-ID(s) driving the composite verdict and state a single
artifact-level signal conclusion synthesizing all subjects, findings, and tensions. If
removed, the artifact must lose a conclusion not reconstructable from per-subject evidence.
```

---

## V-04 — Role Sequence + Register Format (WHERE + WHAT + opposition-ordered interviews)

**Axis:** Role sequence — the opposition axis explicitly dictates interview order: the resistance-pole subject is interviewed first to establish a baseline objection record before any endorsement evidence is collected; the adoption-pole subject is interviewed second and their answers are compared against the resistance record. Register format identical to V-01: Arc-Verified column with in-table example rows demonstrating both entry forms. No named arc-loop closure lifecycle step.

**Hypothesis:** Opposition-anchored sequencing produces richer cross-subject tensions (the resistance record is on paper before the adopter speaks, preventing softening of objections) while maintaining the same register-format compliance ceiling as V-01: C-27 PASS, C-29 PASS, C-28 FAIL. Projected ceiling: 21/22 aspirational; secondary effect: higher C-08/C-11 compliance density from structural sequencing.

---

```
Skill: prove-interview
Topic: Signal Lineage View

Conduct a simulated stakeholder interview investigation for the Signal Lineage View feature —
a Signal plugin capability that renders the full hypothesis → evidence → disposition →
arc-verification chain for any topic, so teams can verify signal completeness before a build
commit.

Produce the artifact in the exact phase order below. Phase gates are structural.

---

STEP 0 — Opposition Axis Declaration + Interview Order Rationale

Before any hypothesis or persona, declare the opposition axis and the interview order it
mandates.

  Axis: [name]
  Pole A (Resistance): [label] — [one-sentence epistemic position — skepticism, inertia, or
    workflow-anchor perspective]
  Pole B (Adoption): [label] — [one-sentence epistemic position — adoption, visibility-need,
    or audit-value perspective]
  Relevance: [why this axis surfaces the most critical unknowns about Signal Lineage View]

Interview order rationale:
- Subject 1 (Resistance anchor) is interviewed first. Their objections, concerns, and
  skepticism are committed to the record before Subject 2 speaks. Subject 1's answers cannot
  be influenced by Subject 2's perspective.
- Subject 2 (Adoption signal) is interviewed second. Their answers are evaluated against the
  resistance record already established. Questions may directly probe the gap between
  Subject 1's stated objections and Subject 2's declared needs.

This sequencing is structural. The resistance record is a fixed baseline; the adoption
evidence is measured against it.

---

STEP 1 — Subject Profiles

Profile Subject 1 (Resistance anchor):
- Role and experience domain
- Prior knowledge of Signal Lineage View
- Declared concerns — specifically: what about the feature's value proposition or overhead
  they would resist
- Opposition pole: Resistance

Profile Subject 2 (Adoption signal):
- Role and experience domain
- Prior knowledge of Signal Lineage View
- Declared interest — specifically: what problem Signal Lineage View would solve for them
- Opposition pole: Adoption

Pairing rationale: state the specific question this resistance-vs-adoption pairing is
designed to answer about Signal Lineage View.

---

STEP 2 — Hypothesis Register

Declare H-01 through H-04. Each entry must include:
1. Hypothesis statement
2. Falsification condition: what finding from the interviews would force rejection

Phase gate: STEP 3A cannot begin until every H-ID has a stated falsification condition.

---

STEP 3A — Subject 1 Interview (Resistance Anchor)

Conduct the full interview with Subject 1. Q-numbering begins at Q-01.

- Open by confirming Subject 1's role and concerns (consistent with STEP 1)
- Ask at least 6 questions, each referencing at least one H-ID in brackets
- Include at least one failure-mode probe: what would Subject 1 do if Signal Lineage View
  produced an incorrect or incomplete chain — and how would this confirm or intensify their
  resistance?
- Record all answers in Subject 1's voice, consistent with their declared expertise

Subject 2's interview does not begin until Subject 1's transcript is complete and all Q-IDs
for Subject 1 are assigned.

---

STEP 3B — Subject 2 Interview (Adoption Signal)

Continue Q-numbering sequentially from Subject 1's final Q-ID.

- Open by confirming Subject 2's role and interests (consistent with STEP 1)
- Ask at least 6 questions, each referencing at least one H-ID in brackets
- At least one question must directly probe the gap between Subject 1's stated resistance
  record and Subject 2's declared needs: "Subject 1 raised [specific concern] — how do you
  respond to that concern?"
- Include at least one failure-mode probe: how would Subject 2 respond if Signal Lineage View
  failed to render arc-verification status for a topic they were about to commit?
- Record all answers in Subject 2's voice, consistent with their declared expertise

---

STEP 3.5 — Hypothesis Disposition Register

After both transcripts are complete, close the hypothesis register. Produce the table — all
four columns populated. The two labeled example rows demonstrate both legal Arc-Verified
entry forms and must remain in the table body:

| H-ID | Disposition | Evidence Citation | Arc-Verified |
|------|-------------|-------------------|--------------|
| *[example — affirmative]* | CONFIRMED | Q-04 | Y / Q-04 |
| *[example — null]* | CHALLENGED | Q-09 | N / — |
| H-01 | CONFIRMED / CHALLENGED / FALSIFIED / UNRESOLVED | Q-nn | *(populate after STEP 6)* |
| H-02 | | | |
| H-03 | | | |
| H-04 | | | |

Column definitions:
- Disposition: CONFIRMED, CHALLENGED, FALSIFIED, or UNRESOLVED (requires stated reason).
- Evidence Citation: Q-ID of the primary evidence row driving the disposition.
- Arc-Verified: populated after STEP 6. Format: Y / Q-nn (affirmative — Q-nn is the Q-ID
  from the adjacent signal test field) or N / — (null — this H-ID's evidence was not the
  arc-verified finding). Return to this table and populate Arc-Verified for all H-IDs after
  completing the arc section.

---

STEP 4 — Evidence Table

| Q-ID | Subject | Question Summary | Finding | Signal Type | Impact Weight |
|------|---------|-----------------|---------|-------------|---------------|

- Signal types: [risk], [preference], [constraint], [validation], [invalidation]
- Impact weights: H / M / L — differentiated values required. At least one H-weight row.
- Note which row(s) carry H weight; they are cited by Q-ID in the composite.

---

STEP 5 — Cross-Subject Tensions Table

| # | Subject 1 resistance position | Subject 2 adoption position | Status (Open / Resolved) |
|---|-------------------------------|----------------------------|--------------------------|

Identify tensions by comparing Subject 1's committed resistance record against Subject 2's
answers. At least one tension must be left Open. The sequencing makes the source of each
tension explicit: Subject 1's position was on the record before Subject 2 spoke.

---

STEP 6 — Arc Signal

Produce a four-row arc table:

| Field | Content |
|-------|---------|
| Arc question | A wider-than-feature question surfaced by the resistance-vs-adoption opposition: what this investigation reveals about how [user type] navigates [workflow commitment decisions] more broadly. |
| Arc inference | Answer to the arc question, distinct from feature-level findings. |
| Evaluator self-test | "If this arc inference were removed, would the feature team lose something not reconstructable from feature-level evidence? Answer: Yes / No — because [stated reason]." |
| Adjacent signal test | "Adjacent signal: [specific Signal plugin skill]. Arc question applies equally: Yes / No — because [reason]. H-weight finding: Q-[nn] is [signal-specific / portable] — because [reason]. Q-[nn] supports H-[nn] [CONFIRMED / CHALLENGED / FALSIFIED]." |

After completing the arc table, populate the Arc-Verified column in the hypothesis
disposition register at STEP 3.5 using the Q-ID from the adjacent signal test field.

---

STEP 7 — Composite Signal

A dedicated synthesis section distinct from per-subject evidence, the tensions table, and the
arc signal. Must name the H-weight Q-ID(s) driving the composite verdict and state a single
artifact-level conclusion synthesizing all subjects, findings, and tensions. If removed, the
artifact must lose a conclusion not reconstructable from per-subject evidence alone.
```

---

## V-05 — Canonical (WHERE + WHEN + WHAT)

**Axis:** Canonical combination — column definition (WHERE: C-27), in-table example rows demonstrating both legal Arc-Verified entry forms (WHAT: C-29), and named STEP 6.5 arc-loop closure lifecycle step explicitly referencing the Arc-Verified column by name as the population target (WHEN: C-28). All three mechanisms present simultaneously.

**Hypothesis:** The full three-mechanism form passes C-27, C-28, and C-29. C-28 → C-27 by construction (the step names the column, presupposing it exists). C-29 → C-27 by construction (example rows presuppose the column header). Combined, all three reinforce the same structural requirement from different angles: WHERE names it, WHEN gates its population, WHAT demonstrates its format. Projected ceiling: 22/22 aspirational → composite 100.00.

---

```
Skill: prove-interview
Topic: Signal Lineage View

Conduct a simulated stakeholder interview investigation for the Signal Lineage View feature —
a Signal plugin capability that renders the full hypothesis → evidence → disposition →
arc-verification chain for any topic, so teams can verify signal completeness before a build
commit.

Produce the artifact in the exact phase order below. Each phase gate is structural: the
stated prior condition must be satisfied before the next phase may begin.

---

STEP 0 — Opposition Axis Declaration

Before any hypothesis or persona is declared, state the axis of epistemic opposition:

  Axis: [name the axis]
  Pole A: [label] — [one-sentence epistemic position]
  Pole B: [label] — [one-sentence epistemic position]
  Relevance: [one sentence: why this axis surfaces the most critical unknowns about Signal
  Lineage View]

This is a structural precondition for STEP 1. The hypothesis register cannot be opened until
the opposition axis is committed.

---

STEP 1 — Subject Profiles

Declare two interview subjects, one per opposition pole. For each:
- Role and experience domain
- Prior knowledge relevant to Signal Lineage View
- Declared concerns or primary interest
- Opposition pole occupied (explicit label matching STEP 0)
- Pairing rationale: what specific question this opposition is designed to answer

---

STEP 2 — Hypothesis Register

Declare H-01 through H-04. Each entry must include:
1. The hypothesis statement
2. A falsification condition: the specific finding that would force rejection — not just
   "if they disagree" but the evidence type that would require abandoning the hypothesis

Phase gate: STEP 3 (interview transcripts) cannot begin until every H-ID carries a stated
falsification condition. An H-ID with a hypothesis but no falsification condition is
structurally incomplete and blocks the gate.

---

STEP 3 — Interview Transcripts

Conduct one simulated interview per subject. Q-numbering is sequential across both subjects.

For each interview:
- Open by confirming the subject's role and concerns (consistent with STEP 1)
- Ask at least 6 questions, each referencing at least one H-ID in brackets: [H-nn]
- Include at least one failure-mode probe: what would this subject do if Signal Lineage View
  rendered an incomplete chain — a disposition missing, an arc-verification status blank, or
  a Q-ID citation that does not resolve to a hypothesis row?
- Record answers in the subject's authentic voice, consistent with declared expertise. No
  answer may invoke knowledge or capabilities the subject was not declared to possess.

---

STEP 3.5 — Hypothesis Disposition Register

After all transcripts are complete, close the hypothesis register. Produce the table — all
four columns present. The two labeled example rows demonstrate both legal Arc-Verified entry
forms and must remain in the table body. Leave Arc-Verified blank until STEP 6.5 executes:

| H-ID | Disposition | Evidence Citation | Arc-Verified |
|------|-------------|-------------------|--------------|
| *[example — affirmative]* | CONFIRMED | Q-05 | Y / Q-05 |
| *[example — null]* | CHALLENGED | Q-11 | N / — |
| H-01 | CONFIRMED / CHALLENGED / FALSIFIED / UNRESOLVED | Q-nn | (populate at STEP 6.5) |
| H-02 | | | |
| H-03 | | | |
| H-04 | | | |

Column definitions:

- Disposition: CONFIRMED (evidence supports), CHALLENGED (partially undermines without
  forcing rejection), FALSIFIED (evidence meets the STEP 2 falsification condition and forces
  rejection), UNRESOLVED (no evidence bearing on this hypothesis — requires a stated reason;
  UNRESOLVED without reason fails).
- Evidence Citation: the Q-ID from the evidence table that drives the disposition.
- Arc-Verified: whether this H-ID's cited evidence was verified as signal-specific in the arc
  test. Entry format — affirmative: Y / Q-nn (Q-nn is the Q-ID from the adjacent signal test
  field that received arc verification); null: N / — (this H-ID's evidence was not the
  arc-verified finding). Leave empty until STEP 6.5.

The two example rows above demonstrate both legal entry forms. An affirmative entry carries
both the Y verdict and the Q-ID (Y / Q-05). A null entry carries both the N verdict and a
dash (N / —). A binary verdict without the second element fails in either case.

---

STEP 4 — Evidence Table

Produce the full evidence table covering all Q-IDs from both interviews:

| Q-ID | Subject | Question Summary | Finding | Signal Type | Impact Weight |
|------|---------|-----------------|---------|-------------|---------------|

- Signal Type: [risk], [preference], [constraint], [validation], or [invalidation]
- Impact Weight: H / M / L — values must be differentiated. Not all identical. At least one
  row must carry H weight.

The H-weight row(s) drive the Composite Signal at STEP 7 and the adjacent signal test at
STEP 6. Note them.

---

STEP 5 — Cross-Subject Tensions Table

| # | Subject A position | Subject B position | Status (Open / Resolved) |
|---|-------------------|--------------------|--------------------------|

At least one tension must be left Open. Agreement rows may be noted but do not count toward
tension coverage. Each row must represent a genuine epistemic gap between subjects.

---

STEP 6 — Arc Signal

Produce a four-row arc table:

| Field | Content |
|-------|---------|
| Arc question | A question whose scope is wider than Signal Lineage View — what this investigation reveals about how [user type] navigates [workflow category] more broadly. This question cannot be answered from feature-level evidence alone. |
| Arc inference | Answer to the arc question, stated as a conclusion distinct from any feature-level finding. It must say something about the user type and workflow category that is not already captured in the per-subject evidence. |
| Evaluator self-test | "If this arc inference were removed, would the feature team lose something not reconstructable from the feature-level evidence? Answer: Yes / No — because [stated reason]." |
| Adjacent signal test | "Adjacent signal: [name a specific Signal plugin skill]. Arc question applies equally to it: Yes / No — because [reason]. H-weight finding: Q-[nn] is [signal-specific / portable] — because [reason]. Q-[nn] supports H-[nn] [CONFIRMED / CHALLENGED / FALSIFIED]." |

Phase gate: STEP 6 is complete when all four rows are populated, the adjacent signal test
names a specific adjacent signal (not generic), cites a Q-ID by number, and states a
disposition label from the STEP 3.5 register.

---

STEP 6.5 — Arc-Loop Closure

After STEP 6 is complete, populate the Arc-Verified column in the hypothesis disposition
register at STEP 3.5.

Procedure:
1. Identify the Q-ID cited in the adjacent signal test field as the H-weight finding.
2. In the STEP 3.5 register, locate the H-ID whose Evidence Citation matches that Q-ID.
3. Set that H-ID's Arc-Verified entry to Y / Q-[nn], where Q-nn is the Q-ID from the
   adjacent signal test field.
4. Set all remaining H-ID Arc-Verified entries to N / —.

The example rows in STEP 3.5 demonstrate the exact format: Y / Q-05 for an affirmative
entry; N / — for a null entry. Follow that format exactly.

Phase gate: STEP 7 (Composite Signal) cannot begin until every H-ID row in the STEP 3.5
register has a non-empty Arc-Verified entry — either Y / Q-nn or N / —. A blank Arc-Verified
cell constitutes an incomplete register and blocks the gate.

---

STEP 7 — Composite Signal

A dedicated synthesis section — distinct from per-subject evidence, the tensions table, and
the arc signal. This section must:
- Name the H-weight Q-ID(s) explicitly as the finding driving the composite verdict
- State a single artifact-level signal conclusion synthesizing all subjects, all findings,
  and all tensions

If this section were removed, the artifact must communicate less — the composite conclusion
must not be reconstructable from per-subject evidence alone.
```

---

## Structural Difference Matrix

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Arc-Verified column in STEP 3.5 header | YES | NO | YES | YES | YES |
| Example rows in STEP 3.5 table body (both forms) | YES | NO | NO | YES | YES |
| Named STEP 6.5 with Arc-Verified named as target | NO | NO | YES | NO | YES |
| Arc closure as prose within STEP 6 | YES | YES | NO | YES | NO |
| Opposition-ordered interview sequence (3A / 3B) | NO | NO | NO | YES | NO |
| C-27 projected | PASS | FAIL | PASS | PASS | PASS |
| C-28 projected | FAIL | FAIL | PASS | FAIL | PASS |
| C-29 projected | PASS | FAIL | FAIL | PASS | PASS |

---

## Evaluator Notes

**C-29 test for V-01, V-04, V-05:** The STEP 3.5 table body contains two labeled example rows — one showing `Y / Q-nn` (affirmative) and one showing `N / —` (null). Both are in the table body, not in a legend or footnote. C-29 passes by inspection.

**C-29 test for V-03:** The STEP 3.5 table body contains no example rows. The Arc-Verified column is defined with a format-notation description in the column definition block below the table. A format description outside the table body fails C-29.

**C-28 test for V-03, V-05:** STEP 6.5 is a named dedicated step after STEP 6. It names "Arc-Verified" as the population target (criterion 1), instructs using the Q-ID from arc analysis (criterion 2), and identifies the adjacent signal test field as the Q-ID source (criterion 3). C-28 passes.

**C-28 test for V-01, V-02, V-04:** The arc population instruction is prose embedded within STEP 6 ("After completing the arc table, populate the Arc-Verified column...") or in the register description, not a named dedicated step. No step after STEP 6 names Arc-Verified as the population target. C-28 fails.

**V-02 cascade:** No Arc-Verified column exists in STEP 3.5. The closure instruction at the end of STEP 6 ("annotate any H-ID whose evidence was cited") produces a prose annotation adjacent to the register, not a column entry. C-26 borderline PASS (explicit cross-reference exists in prose). C-27 FAIL (prose annotation is not a named column with binary verdict + Q-ID). C-28 FAIL by construction (step cannot name Arc-Verified as target if column does not exist).
