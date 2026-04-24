R9 variations written to `simulations/quest/variations/rhythm-rebuttal-variations-R9-2026-03-19.md`.

**Summary:**

| Variation | Axis | C-31 | C-32 | C-33 |
|-----------|------|------|------|------|
| V-01 | J only | Entity-type referent column in Phase 6a | — | — |
| V-02 | K only | — | Branched (a)/(b) repair in all Phase 7 checks | — |
| V-03 | L only | — | — | Forward-annotations in Phase 2, Phase 5, Phase 6a |
| V-04 | J+K | Phase 6a column | Phase 7 branched repair | — |
| V-05 | J+K+L | Phase 6a column | Phase 7 branched repair | All three upstream forward-annotations |

**Predicted scoring against rubric v9 (`/25`):**
- V-01/V-02/V-03: 22/25 each (one new criterion each, two missed)
- V-04: 23/25 (C-31 + C-32, C-33 absent)
- V-05: 25/25 ceiling (all three axes integrated, forward-annotations in three distinct phases)
ls |
| V-05 | J+K+L | Full integration — entity-type column + branched repair + upstream forward-annotations |

**The three structural distinctions from R8:**
- J propagates the Phase 7 Check 2c entity-type constraint upstream into Phase 6a — the same artifact can satisfy C-28 (entity named at gate) but fail C-31 (Phase 6a table has no entity-type column, so referent was inserted last-second)
- K converts every Phase 7 gate from a stop sign into a directed decision fork — C-24 required gates to exist and block; C-32 requires each gate to prescribe what happens next, with structurally distinct paths per failure type
- L closes the gap between gate-level detection (Phase 7) and authoring-time visibility (Phase 2/5/6a) — C-32 embeds repair in Phase 7 after the draft is complete; C-33 surfaces the constraint at the moment the author is making the decision that will later fail

---

## Axis Rationales

**Axis J — entity-type column propagation gap**: C-28 (R8) enforces entity-type resolution at Phase 7 Check 2c. An executor who writes "prior literature (Jones 2019, §3.2)" in Phase 5 and reaches Phase 7 will pass Check 2c because Jones 2019 is a named entity. But an executor who writes "No change — prior literature" in Phase 5, intending to add the citation before submission, can still pass Check 2c by inserting the entity at gate time. The Phase 6a reconciliation table under R8 carries the column "Evidence category + instance" — this column does not specifically require the entity-type referent to be present during Phase 6a reconciliation. C-31 closes this by adding an "Entity-type referent" column to the Phase 6a table schema. The column is required: an executor who cannot fill it during Phase 6a has not yet identified the concrete entity and is caught mid-workflow rather than at the final gate. The same artifact cannot pass C-31's Phase 6a check by inserting the entity only at Check 2c.

**Axis K — branched repair protocol gap**: C-24 (R6) requires Phase 7 to contain numbered gate checks that block write on failure. The current skill does this: each check has an "If FAIL:" clause. But the repair instruction is either absent or generic — "identify missing R-IDs and write the missing exchanges before proceeding" does not tell the executor which kind of missing the failure represents. When an executor fails a gate, they face a choice: was the missing exchange never written, or was it merged into another exchange? The repair action differs. C-32 requires each gate's "If FAIL:" clause to specify two or more structurally distinct repair paths labeled (a)/(b), determined by the failure type. This converts each gate from a stop sign (you failed; go back) into a decision fork (you failed for reason X — take path a; or for reason Y — take path b). The protocol is embedded in the gate check text, not in a separate appendix.

**Axis L — forward-annotation gap**: C-32 (R9) embeds repair protocols in Phase 7 gate checks. But the author only reaches Phase 7 after the full draft is complete. A P1 no-change decision in Phase 5 that lacks a named entity-type referent will fail Check 2c — but the author made that drafting choice in Phase 5, not Phase 7. C-33 surfaces each Phase 7 constraint at the upstream phase where the relevant decision is made: Phase 2 (P1 pre-commitment) carries forward-annotated warnings about Check 2c entity-type requirements and Check 4 Part C anti-deferral; Phase 5 (MANUSCRIPT OUTCOME template) carries a forward-annotated failure note for P1 no-change entries; Phase 6a (reconciliation) carries a forward-annotated warning about Check 6b cover-letter/outcome consistency. An author who reads a forward-annotation while authoring has a chance to avoid the failure class entirely rather than discovering it only at the gate.

---

## V-01 — Entity-Type Column Propagation in Phase 6a

**Axis**: J only — C-31 entity-type referent column in Phase 6a reconciliation table
**Hypothesis**: Adding an explicit entity-type referent column to the Phase 6a audit table forces the executor to name the concrete entity during mid-workflow reconciliation rather than relying on last-second insertion at Phase 7 Check 2c. The column requirement closes the loophole where an executor commits the category label in Phase 5 but defers naming the specific paper/author/statistic/principle until the gate runs.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition, naming evidence by category AND specific instance. Phase 3.5
audits ambiguous type assignments. Phase 3.6 audits P2/P3 severity assignments -- for each
downgraded concern, one sentence states the specific paper-based reason it does not block
acceptance. Forecast rows carry forward as flags into exchange headers. The amendment pass
validates FLAGGED exchanges first, audits P1 pre-commitments with SHIFTED classification --
PRESSURE-DRIVEN entries close to a binary (REINSTATE / NO REINSTATE) with a named rationale;
EVIDENCE-DRIVEN entries record CONFIRM CHANGE with a named evidence sentence -- then checks
for unflagged failures. Phase 6a reconciliation requires each Paragraph 1 change claim to
trace to at least one R-ID and carries an entity-type referent column in the P1 pre-commitment
audit table -- the concrete entity (cited paper/author, named statistic/test, named
methodological principle) must be present during reconciliation, not inserted at gate time.
Phase 7 structural completion gate verifies P1 no-change evidence entity-type resolution,
PRESSURE-DRIVEN decision closure, cover letter traceability, claim-outcome consistency, and
count-based integrity before artifact write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default -- the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia -- use at least one; name the category AND
a specific traceable instance within the category):
  - Prior literature: cite a specific work (Author Year, §Section or Table N)
  - Methodological argument: name the specific inferential claim and its study-design basis
  - Statistical result: name the statistic and its paper location (e.g., F(2,118)=14.3, App. C)

Invalid evidence forms (do NOT overcome inertia -- do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Phase 7 Check 2b enforces category presence; Check 2c enforces instance specificity.
A P1 no-change rationale naming a valid category but no traceable instance fails Check 2c --
the category label alone does not satisfy RULE-1 at editorial submission standard.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max. State the
scientific rationale. Do not over-argue.
Violation: a no-change response longer than 1 paragraph reads as defensive regardless
of content quality.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max. State the
paper's claim space. Do not argue or defend. Close.
Violation: a multi-paragraph scope response concedes that the scope challenge has merit
and invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only. No
response is combative, dismissive, or sycophantic. Professional, non-defensive, grateful.
Violation: combative or dismissive phrasing is a professional failure that may cause
rejection independent of scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns,
even if they appear in the same reviewer paragraph.
Violation: a merged exchange produces a single REVIEWER SAID block quoting multiple
distinct concerns -- the editorial office will return it for revision.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.
Violation: non-integer frontmatter values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.
Violation: fabricated reviewer comments constitute academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change -- rationale]

Violation: any Phase 5 block missing REVIEWER SAID, AUTHOR RESPONDS, or MANUSCRIPT OUTCOME
is structurally incomplete and must be rewritten. RULE-5 and RULE-8 together enforce
atomicity: a merged concern cannot produce a valid REVIEWER SAID block. The type assigned
in Phase 3 (verified in Phase 3.5; severity verified in Phase 3.6) determines the AUTHOR
RESPONDS strategy in Phase 5. Forecast flags from Phase 4 appear in the exchange header.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: the hardest individual
decisions are committed before Phase 5 drafting pressure can erode them. SHIFTED entries
in Phase 6a require classification; PRESSURE-DRIVEN entries close to REINSTATE or NO
REINSTATE with a named rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):
For each P1 concern anticipated to result in no-change, name the concern and the anticipated
evidence form (valid form from RULE-1 -- named by category AND specific traceable instance):

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy -- anticipated no-change
  because: statistical result -- power analysis (80% power at N=120, primary outcome, App. B
  Table B1) showed adequacy before data collection began.

  Example: P1-NC: Reviewer 3 request to adopt Chen 2018 framework -- anticipated no-change
  because: methodological argument -- Chen 2018 assumes panel data; this study uses
  cross-sectional design (§2.1, single observation per participant), making that framework
  inapplicable by structural assumption.

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.
SHIFTED entries require classification. PRESSURE-DRIVEN entries require REINSTATE or NO
REINSTATE with a one-sentence rationale. EVIDENCE-DRIVEN entries require CONFIRM CHANGE
with a named evidence sentence -- see Phase 6a protocol.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide -- type is verified in Phase 3.5 before proceeding. Assign exactly one:

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake in the paper | "Framing" -- factual is an error in the paper; framing is a misread by the reviewer |
| methodological | Existing experiment or analysis design is flawed | "Scope" -- methodological = current work is wrong; scope = reviewer wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" -- scope = paper doesn't claim this; methodological = it tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" -- framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis the paper should include | "Methodological" -- statistical = analysis layer; methodological = experimental design |
| presentation | Clarity, structure, notation, language | Safe fallback for concerns with no scientific content impact |

Severity:
- **P1**: blocks acceptance -- RULE-1 applies; no-change requires valid evidence form category
  AND specific traceable instance; check Phase 2 P1-NC pre-commitments before drafting
- **P2**: moderate -- address or explain; assignment verified in Phase 3.6 before forecast
- **P3**: editorial -- fix or note briefly; assignment verified in Phase 3.6 before forecast

Sort: P1 first, P2 second, P3 third. Within tier, preserve reviewer order.

---

## PHASE 3.5 -- TYPE AUDIT

For every concern assigned scope, framing, or methodological, verify the assignment before
writing the forecast. State one sentence per assignment:

  R-[NN] typed [assigned type] not [most likely alternative] because:
  [specific distinguishing reason for this concern, not a restatement of the type definition]

Example:
  R-03 typed scope not methodological because: reviewer requests new population-level
  replication; the existing study design is not questioned.

  R-07 typed framing not factual because: §2.3 states the claim correctly; the reviewer
  reads the abstract shorthand as a stronger universality claim the paper does not make.

If any assignment looks wrong on audit, correct the Phase 3 table before proceeding.
Only scope, framing, and methodological assignments require audit entries.

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every concern assigned P2 or P3, verify the assignment before writing the forecast.
State one sentence per assignment:

  R-[NN] assigned [P2/P3] not P1 because:
  [specific paper-based or venue-based reason this concern does not block acceptance --
  not a restatement of the severity tier definition]

Valid: "R-05 assigned P2 not P1 because: the journal's author guidelines state secondary
outcome reporting requirements are non-blocking for desk review; R-05 concerns a sensitivity
analysis on the secondary outcome (§4.3, Table 3) and the primary outcome analysis is complete
and unreported."

Invalid: "R-05 assigned P2 not P1 because: this is a moderate concern." (Restates definition.)

If any severity assignment looks wrong on audit, correct the Phase 3 table before proceeding.
All P2 and P3 assignments require audit entries. P1 assignments require no entries.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Specific predictions
only -- generic statements do not count. The trigger column must name a causal mechanism
(not just a concern property). These rows carry forward as flags into Phase 5 headers.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [name the specific mechanism -- reviewer tone, P1 inertia pressure, ambiguous claim -- that will cause over-explanation] |
| F-02 | [R-NN] | concedes too much | [name the reviewer move or pressure that will cause over-concession] |
| F-03 | [R-NN] | too brief | [name the structural reason this concern gets under-addressed -- buried, overlap, deferred] |

When writing Phase 5: flag each exchange whose R-ID matches a forecast row. The flag
appears in the exchange header and keeps the prediction visible during drafting.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange (Violation: see RULE-8 consequence above). Write in severity
order:

--- P1 CONCERNS (RULE-1 applies -- no-change requires valid evidence form category AND
specific traceable instance; see Phase 2 P1-NC pre-commitments) ---
--- P2 CONCERNS (address or explain; severity justified in Phase 3.6) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange. If the R-ID appears in the Phase 4 forecast, add the
forecast flag to the exchange header. Use the type-specific AUTHOR RESPONDS template
(type verified in Phase 3.5; severity verified in Phase 3.6 for P2/P3):

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: append "| FLAGGED: [F-0N] [predicted failure mode -- resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."

  methodological: "We agree that [aspect]. [Scientific justification or fix description.]
                  We have [specific change or explanation] in §N."

  scope:          [2-3 sentences. RULE-3. "This question lies beyond the scope of the present
                  paper, which [state claim space]. We note it as a direction for future work."]

  framing:        "The paper claims [exact manuscript claim]. The reviewer may be reading this
                  as [misread]. We have added [clarifying language] to §N."

  statistical:    "[Added the analysis / explained the constraint.] [Result or rationale.]"

  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change. Or: No change -- [rationale naming the valid RULE-1 evidence
form by category AND a specific traceable instance (citation with Author Year §N, named
analysis with location, or quantitative statistic with paper location) if P1; RULE-2 applies
to all no-change; RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 to reflect changes actually made. Each named change must include
  parenthetical R-ID references: "We [change] (R-NN)" or "We [change] (R-NN, R-NN)".
  An unnamed change claim will fail Phase 7 Check 6.
- Update Paragraph 2 for any shift in disagreement framing.
- P1 pre-commitment audit with SHIFTED classification, entity-type referent, and decision
  closure:

  | P1-NC | Evidence category | Entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|-------------------|----------------------|-----------------|----------------|----------------|----------|-----------|

  **Entity-type referent column**: name the concrete entity the evidence category implies.
  - Prior literature: the cited paper or author (Author Year) -- not §N of this manuscript
  - Statistical result: the specific statistic and its paper location (e.g., F(2,118)=14.3, App. C)
  - Methodological argument: the named inferential principle and its study-design basis
  A category label without a named entity-type referent in this column fails Phase 6a
  reconciliation. The referent must be present here, during authoring -- it cannot be
  inserted at Phase 7 Check 2c to satisfy the constraint.

  HELD: pre-committed no-change was maintained; named evidence form and instance used in
  Phase 5. No re-examination required.

  SHIFTED: position changed during drafting. Classify and re-examine:

    PRESSURE-DRIVEN: author yielded under rhetorical or emotional argument weight without
    encountering specific new scientific evidence. The original no-change position may still
    be scientifically correct.
    Decision required (choose one and state a one-sentence rationale):
      REINSTATE: [name the specific RULE-1 evidence category and instance that was valid
      before Phase 5 and remains valid -- the change should be reversed]
      NO REINSTATE: [name the specific non-scientific improvement achieved by the change
      (clarity, presentation, reduced ambiguity) -- confirm the scientific claim is unaffected]

    EVIDENCE-DRIVEN: author encountered specific evidence in Phase 5 (a named result,
    calculation, or argument not anticipated in Phase 2) that genuinely changed the assessment.
    Decision required: CONFIRM CHANGE: [name the specific evidence encountered -- one sentence].
    Re-examination required: Does cover letter Paragraph 2 accurately reflect the resolved
    disagreement? If this concern was listed as a standing disagreement and the shift resolved
    it, update Paragraph 2 to remove or revise the disagreement claim.

**6b. Forecast validation**: Validate FLAGGED exchanges first, then check unflagged exchanges.

FLAGGED exchanges (from Phase 4 forecast rows):
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|
| F-01 | | too defensive | | |
| F-02 | | concedes too much | | |
| F-03 | | too brief | | |

Unflagged failures: name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen** (FLAGGED exchanges take priority; add unflagged
failures as needed to reach three):
1. [R-NN] -- too defensive: [rewrite AUTHOR RESPONDS opening to remove defensive register]
2. [R-NN] -- concedes too much: [what to hold; why the concession went too far]
3. [R-NN] -- too brief: [what is understated; what to add]

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing the artifact. Each check must PASS. Any FAIL stops
the write -- fix the failing check and re-run before proceeding.

**Check 1 -- Decomposition completeness**:
Count REVIEWER SAID blocks in Phase 5. Count R-ID entries in Phase 3 table.
PASS if counts match. FAIL if Phase 5 has fewer REVIEWER SAID blocks than Phase 3 R-IDs.
CHECK: [n REVIEWER SAID blocks in Phase 5] vs [n R-IDs in Phase 3] -- PASS / FAIL
If FAIL: identify missing R-IDs and write the missing exchanges before proceeding.

**Check 2a -- Outcome resolution completeness**:
Every MANUSCRIPT OUTCOME in Phase 5 must be either "[Section N]: [specific change]" or
"No change -- [rationale]". No placeholder, deferred, or TBD outcomes.
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL: identify unresolved outcomes and complete them before proceeding.

**Check 2b -- P1 no-change evidence form category presence**:
For every P1 MANUSCRIPT OUTCOME that is "No change," verify the rationale names at least
one valid RULE-1 evidence form by category (prior literature / methodological argument /
statistical result). A rationale using only invalid forms (restatement, precedent) fails.
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL: rewrite the MANUSCRIPT OUTCOME rationale to name the evidence form before proceeding.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
For every P1 MANUSCRIPT OUTCOME that passed Check 2b, verify the rationale names a specific
traceable instance within the valid category:
  - Prior literature: Author Year, §Section or Table N (or equivalent locator)
  - Methodological argument: named inferential claim with its study-design basis
  - Statistical result: specific statistic and its paper location
"Prior literature supports our approach" -- fails Check 2c (category present, no instance).
"Prior literature (Jones 2019, §3.2) demonstrates this measurement approach is validated
in equivalent cross-sectional populations" -- passes (category + specific citation + locator).
CHECK: list each P1 no-change R-ID, its evidence category, and its named traceable instance
-- PASS / FAIL per entry
If FAIL: add the specific traceable instance to the MANUSCRIPT OUTCOME rationale before
proceeding. Note: Phase 6a entity-type referent column should have caught this -- update
the Phase 6a table entry to reflect the correction.

**Check 3 -- Cover letter structure**:
Phase 2 (updated in 6a) contains exactly Paragraph 1 (3-4 changes named with R-ID references)
and Paragraph 2 (areas of disagreement named, or explicit statement that none exist).
CHECK: PASS / FAIL
If FAIL: identify which paragraph is missing or malformed and repair before proceeding.

**Check 4 -- Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: Every FLAGGED exchange from Phase 5 must appear as a validated row in Phase 6b
(with ACCURATE / MISSED / OVERSTATED result).
CHECK: [n FLAGGED exchange headers in Phase 5] vs [n validated rows in Phase 6b] -- PASS / FAIL
Part B: Every SHIFTED entry in the Phase 6a pre-commitment audit must have a classification
(PRESSURE-DRIVEN or EVIDENCE-DRIVEN) and a completed re-examination note.
CHECK: [n SHIFTED entries] vs [n classified + re-examined entries] -- PASS / FAIL
Part C: Every PRESSURE-DRIVEN entry from Phase 6a must have a named binary decision
(REINSTATE or NO REINSTATE) with a one-sentence rationale.
CHECK: [n PRESSURE-DRIVEN entries] vs [n with named binary decision + rationale] -- PASS / FAIL
If any part fails: complete the missing element before proceeding.

**Check 5 -- Frontmatter integer verification**:
Compute actual values from Phase 5 outcomes:
- reviewer_count: total distinct reviewers in Phase 3 table
- concerns_addressed: total R-IDs in Phase 3 table (= REVIEWER SAID count after Check 1)
- manuscript_changes: R-IDs with MANUSCRIPT OUTCOME = section + change
- no_change_responses: R-IDs with MANUSCRIPT OUTCOME = No change
CHECK: all four values are integers, sum is consistent -- PASS / FAIL
If FAIL: recompute from Phase 5 outcomes and correct frontmatter values.

**Check 6 -- Cover letter Paragraph 1 traceability**:
Every change claim in Paragraph 1 (Phase 2, updated in 6a) must include at least one
parenthetical R-ID reference. A claim with no R-ID reference is vague and fails this check.
CHECK: list each Paragraph 1 claim and its R-ID reference(s) -- PASS / FAIL per claim
If FAIL: add R-ID references to untraced claims. If no R-ID maps to the claim, the claim
names a change not driven by any reviewer concern -- remove or rephrase before proceeding.

**Check 6b -- Cover letter claim-outcome consistency**:
For every Paragraph 1 change claim that passed Check 6, verify that each referenced R-ID
resolves to a CHANGE MANUSCRIPT OUTCOME (not "No change"). A claim asserting "we changed X
in response to R-NN" while R-NN's MANUSCRIPT OUTCOME is "No change" is a structural
contradiction.
CHECK: list each Paragraph 1 claim, its R-ID reference(s), and each R-ID's MANUSCRIPT OUTCOME
type (CHANGE or NO CHANGE) -- PASS / FAIL per claim
If FAIL: (a) correct the MANUSCRIPT OUTCOME for the R-ID if the change was actually made but
recorded incorrectly in Phase 5; or (b) revise Paragraph 1 to remove or rephrase the claim
asserting a change that was not made.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-02 — Branched Repair Protocols in Phase 7

**Axis**: K only — C-32 branched repair protocols in every Phase 7 gate check
**Hypothesis**: Replacing generic "If FAIL: fix and re-run" instructions with labeled (a)/(b) repair paths per failure type converts each gate from a stop sign into a decision fork. An executor who fails a check knows not only that the artifact is blocked but which of two structurally distinct repairs applies to their specific failure mode.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition, naming evidence by category AND specific instance. Phase 3.5
audits ambiguous type assignments. Phase 3.6 audits P2/P3 severity assignments -- for each
downgraded concern, one sentence states the specific paper-based reason it does not block
acceptance. Forecast rows carry forward as flags into exchange headers. The amendment pass
validates FLAGGED exchanges first, audits P1 pre-commitments with SHIFTED classification --
PRESSURE-DRIVEN entries close to a binary (REINSTATE / NO REINSTATE) with a named rationale;
EVIDENCE-DRIVEN entries record CONFIRM CHANGE with a named evidence sentence -- then checks
for unflagged failures. Phase 6a reconciliation requires each Paragraph 1 change claim to
trace to at least one R-ID. Phase 7 structural completion gate runs ten checks; each check
that can fail includes a branched repair protocol specifying two structurally distinct
corrective paths (a)/(b) -- the repair choice is determined by the failure type, converting
each gate from a stop sign into a decision fork.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default -- the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia -- use at least one; name the category AND
a specific traceable instance within the category):
  - Prior literature: cite a specific work (Author Year, §Section or Table N)
  - Methodological argument: name the specific inferential claim and its study-design basis
  - Statistical result: name the statistic and its paper location (e.g., F(2,118)=14.3, App. C)

Invalid evidence forms (do NOT overcome inertia -- do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Phase 7 Check 2b enforces category presence; Check 2c enforces instance specificity.
A P1 no-change rationale naming a valid category but no traceable instance fails Check 2c --
the category label alone does not satisfy RULE-1 at editorial submission standard.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max. State the
scientific rationale. Do not over-argue.
Violation: a no-change response longer than 1 paragraph reads as defensive regardless
of content quality.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max. State the
paper's claim space. Do not argue or defend. Close.
Violation: a multi-paragraph scope response concedes that the scope challenge has merit
and invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only. No
response is combative, dismissive, or sycophantic. Professional, non-defensive, grateful.
Violation: combative or dismissive phrasing is a professional failure that may cause
rejection independent of scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns,
even if they appear in the same reviewer paragraph.
Violation: a merged exchange produces a single REVIEWER SAID block quoting multiple
distinct concerns -- the editorial office will return it for revision.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.
Violation: non-integer frontmatter values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.
Violation: fabricated reviewer comments constitute academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change -- rationale]

Violation: any Phase 5 block missing REVIEWER SAID, AUTHOR RESPONDS, or MANUSCRIPT OUTCOME
is structurally incomplete and must be rewritten. RULE-5 and RULE-8 together enforce
atomicity: a merged concern cannot produce a valid REVIEWER SAID block. The type assigned
in Phase 3 (verified in Phase 3.5; severity verified in Phase 3.6) determines the AUTHOR
RESPONDS strategy in Phase 5. Forecast flags from Phase 4 appear in the exchange header.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: the hardest individual
decisions are committed before Phase 5 drafting pressure can erode them. SHIFTED entries
in Phase 6a require classification; PRESSURE-DRIVEN entries close to REINSTATE or NO
REINSTATE with a named rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):
For each P1 concern anticipated to result in no-change, name the concern and the anticipated
evidence form (valid form from RULE-1 -- named by category AND specific traceable instance):

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy -- anticipated no-change
  because: statistical result -- power analysis (80% power at N=120, primary outcome, App. B
  Table B1) showed adequacy before data collection began.

  Example: P1-NC: Reviewer 3 request to adopt Chen 2018 framework -- anticipated no-change
  because: methodological argument -- Chen 2018 assumes panel data; this study uses
  cross-sectional design (§2.1, single observation per participant), making that framework
  inapplicable by structural assumption.

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.
SHIFTED entries require classification. PRESSURE-DRIVEN entries require REINSTATE or NO
REINSTATE with a one-sentence rationale. EVIDENCE-DRIVEN entries require CONFIRM CHANGE
with a named evidence sentence -- see Phase 6a protocol.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide -- type is verified in Phase 3.5 before proceeding. Assign exactly one:

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake in the paper | "Framing" -- factual is an error in the paper; framing is a misread by the reviewer |
| methodological | Existing experiment or analysis design is flawed | "Scope" -- methodological = current work is wrong; scope = reviewer wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" -- scope = paper doesn't claim this; methodological = it tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" -- framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis the paper should include | "Methodological" -- statistical = analysis layer; methodological = experimental design |
| presentation | Clarity, structure, notation, language | Safe fallback for concerns with no scientific content impact |

Severity:
- **P1**: blocks acceptance -- RULE-1 applies; no-change requires valid evidence form category
  AND specific traceable instance; check Phase 2 P1-NC pre-commitments before drafting
- **P2**: moderate -- address or explain; assignment verified in Phase 3.6 before forecast
- **P3**: editorial -- fix or note briefly; assignment verified in Phase 3.6 before forecast

Sort: P1 first, P2 second, P3 third. Within tier, preserve reviewer order.

---

## PHASE 3.5 -- TYPE AUDIT

For every concern assigned scope, framing, or methodological, verify the assignment before
writing the forecast. State one sentence per assignment:

  R-[NN] typed [assigned type] not [most likely alternative] because:
  [specific distinguishing reason for this concern, not a restatement of the type definition]

If any assignment looks wrong on audit, correct the Phase 3 table before proceeding.
Only scope, framing, and methodological assignments require audit entries.

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every concern assigned P2 or P3, verify the assignment before writing the forecast.
State one sentence per assignment:

  R-[NN] assigned [P2/P3] not P1 because:
  [specific paper-based or venue-based reason this concern does not block acceptance]

If any severity assignment looks wrong on audit, correct the Phase 3 table before proceeding.
All P2 and P3 assignments require audit entries. P1 assignments require no entries.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Specific predictions
only -- generic statements do not count. The trigger column must name a causal mechanism.
These rows carry forward as flags into Phase 5 headers.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [specific mechanism] |
| F-02 | [R-NN] | concedes too much | [reviewer move or pressure] |
| F-03 | [R-NN] | too brief | [structural reason] |

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS (RULE-1 applies) ---
--- P2 CONCERNS ---
--- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: "| FLAGGED: [F-0N] [predicted failure mode -- resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."

  methodological: "We agree that [aspect]. [Scientific justification or fix.] §N."

  scope:          [2-3 sentences. RULE-3.]

  framing:        "The paper claims [exact claim]. The reviewer may be reading this as
                  [misread]. We have added [clarifying language] to §N."

  statistical:    "[Added the analysis / explained the constraint.] [Result or rationale.]"

  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change. Or: No change -- [rationale naming valid RULE-1 evidence form
by category AND a specific traceable instance if P1; RULE-2; RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
- Update Paragraph 1 with parenthetical R-ID references for each named change.
- Update Paragraph 2 for any shift in disagreement framing.
- P1 pre-commitment audit:

  | P1-NC | Evidence category + instance | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|------------------------------|-----------------|----------------|----------------|----------|-----------|

  HELD: no-change maintained; evidence form and instance in Phase 5.

  SHIFTED -- classify:
    PRESSURE-DRIVEN: REINSTATE or NO REINSTATE with one-sentence rationale.
    EVIDENCE-DRIVEN: CONFIRM CHANGE: [specific evidence]. Update Paragraph 2 if needed.

**6b. Forecast validation**:
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|

Unflagged failures: name any quality failure not predicted in Phase 4.

**6c. Three exchanges to strengthen** (FLAGGED priority):
1. [R-NN] -- too defensive
2. [R-NN] -- concedes too much
3. [R-NN] -- too brief

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing the artifact. Each check must PASS. Any FAIL stops
the write -- fix the failing check and re-run before proceeding.

**Check 1 -- Decomposition completeness**:
COUNT REVIEWER SAID blocks in Phase 5. Count R-ID entries in Phase 3 table.
CHECK: [n REVIEWER SAID blocks in Phase 5] vs [n R-IDs in Phase 3] -- PASS / FAIL
If FAIL:
  (a) Concern decomposed in Phase 3 but no exchange written: write the missing exchange in
      severity order before proceeding.
  (b) Two concerns merged into one REVIEWER SAID block: split them into separate exchanges,
      each with its own complete REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME.

**Check 2a -- Outcome resolution completeness**:
Every MANUSCRIPT OUTCOME must be "[Section N]: [specific change]" or "No change -- [rationale]".
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL:
  (a) Change made but MANUSCRIPT OUTCOME contains a placeholder: write the section identifier
      and specific change description before proceeding.
  (b) Outcome genuinely unresolved (no decision made): use Phase 2 pre-commitments as
      baseline and record a no-change rationale or commit to a change before proceeding.

**Check 2b -- P1 no-change evidence form category presence**:
For every P1 MANUSCRIPT OUTCOME that is "No change," verify the rationale names at least one
valid RULE-1 evidence form by category.
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL:
  (a) Valid evidence form present in AUTHOR RESPONDS but absent from MANUSCRIPT OUTCOME: move
      the category name into the MANUSCRIPT OUTCOME rationale before proceeding.
  (b) No valid evidence form used anywhere in the exchange: revise to introduce prior
      literature, methodological argument, or statistical result before proceeding.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
For every P1 MANUSCRIPT OUTCOME that passed Check 2b, verify a specific traceable instance:
Author Year + locator for literature; named statistic + location for statistical; named
principle + study-design basis for methodological.
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL:
  (a) Specific entity exists in the exchange body but absent from MANUSCRIPT OUTCOME: move
      the named entity into the MANUSCRIPT OUTCOME rationale before proceeding.
  (b) No concrete entity named anywhere in the exchange: revise to name a specific entity.
      A location reference alone (§N, Table N) without a named entity does not satisfy this check.

**Check 3 -- Cover letter structure**:
Phase 2 (updated in 6a) contains Paragraph 1 (3-4 changes with R-ID references) and
Paragraph 2 (disagreement framing or explicit statement of none).
CHECK: PASS / FAIL
If FAIL:
  (a) Paragraph present but malformed (Paragraph 1 changes lack R-ID references): add
      parenthetical R-ID references to each change claim before proceeding.
  (b) Paragraph missing entirely: draft from Phase 2 pre-commitments and Phase 5 outcomes.

**Check 4 -- Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: Every FLAGGED exchange must appear as a validated row in Phase 6b.
CHECK: [n FLAGGED headers] vs [n validated rows in Phase 6b] -- PASS / FAIL
If Part A fails:
  (a) Forecast rows exist but no validation entry written: complete Phase 6b FLAGGED
      validation for each forecast row before proceeding.
  (b) Validation entries written but count mismatches: identify the unvalidated row and add it.

Part B: Every SHIFTED entry must have classification and completed re-examination note.
CHECK: [n SHIFTED entries] vs [n classified + re-examined] -- PASS / FAIL
If Part B fails:
  (a) SHIFTED entries with no classification: apply PRESSURE-DRIVEN or EVIDENCE-DRIVEN.
  (b) Classified but re-examination note absent: write the note for each classified entry.

Part C: Every PRESSURE-DRIVEN entry must have REINSTATE or NO REINSTATE with rationale.
CHECK: [n PRESSURE-DRIVEN entries] vs [n with named binary decision + rationale] -- PASS / FAIL
If Part C fails:
  (a) PRESSURE-DRIVEN entry has re-examination note but no binary decision: state REINSTATE
      or NO REINSTATE with a one-sentence rationale naming what holds or was conceded.
  (b) EVIDENCE-DRIVEN entry lacks CONFIRM CHANGE: name the evidence and record CONFIRM CHANGE
      with a one-sentence evidence statement before proceeding.

**Check 5 -- Frontmatter integer verification**:
Compute reviewer_count, concerns_addressed, manuscript_changes, no_change_responses.
CHECK: all four values are integers, sum consistent -- PASS / FAIL
If FAIL:
  (a) Frontmatter contains string placeholders: replace each with the computed integer.
  (b) Integer values inconsistent (manuscript_changes + no_change_responses !=
      concerns_addressed): recount from Phase 5 outcomes and correct all four values.

**Check 6 -- Cover letter Paragraph 1 traceability**:
Every change claim in Paragraph 1 must include at least one parenthetical R-ID reference.
CHECK: list each Paragraph 1 claim and its R-ID reference(s) -- PASS / FAIL per claim
If FAIL:
  (a) R-ID exists for the claim but was omitted: add the parenthetical reference.
  (b) No R-ID maps to the claim: remove or rephrase to reflect a reviewer-driven change.

**Check 6b -- Cover letter claim-outcome consistency**:
For every Paragraph 1 change claim that passed Check 6, verify each referenced R-ID resolves
to a CHANGE MANUSCRIPT OUTCOME (not "No change").
CHECK: list each Paragraph 1 claim, R-ID reference(s), and R-ID MANUSCRIPT OUTCOME type
(CHANGE or NO CHANGE) -- PASS / FAIL per claim
If FAIL:
  (a) Change made but Phase 5 MANUSCRIPT OUTCOME records no change incorrectly: correct the
      MANUSCRIPT OUTCOME for that R-ID before proceeding.
  (b) Change not made: revise Paragraph 1 to remove or rephrase the false change claim.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-03 — Forward-Annotated Gate Constraints in Upstream Phases

**Axis**: L only — C-33 gate failure conditions surfaced in Phase 2, Phase 5, Phase 6a
**Hypothesis**: Gate constraints that only appear in Phase 7 are discovered after the full draft is complete. Forward-annotating each constraint at the upstream decision point gives the author a chance to avoid the failure class at the moment it is still preventable, without waiting for Phase 7 to detect it.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition, naming evidence by category AND specific instance; Phase 2
carries forward-annotated warnings from downstream Phase 7 gate constraints visible at
commitment time. Phase 3.5 audits ambiguous type assignments. Phase 3.6 audits P2/P3
severity assignments. Forecast rows carry forward as flags into exchange headers; Phase 5
MANUSCRIPT OUTCOME template for P1 no-change entries carries forward-annotated failure
conditions from Check 2c and Check 6b. The amendment pass validates FLAGGED exchanges first,
audits P1 pre-commitments with SHIFTED classification -- PRESSURE-DRIVEN entries close to
REINSTATE / NO REINSTATE with a named rationale; EVIDENCE-DRIVEN entries record CONFIRM
CHANGE -- then checks for unflagged failures; Phase 6a carries a forward-annotated Check 6b
failure condition visible during cover-letter reconciliation. Phase 7 structural completion
gate verifies all constraints before write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default -- the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia -- use at least one; name the category AND
a specific traceable instance within the category):
  - Prior literature: cite a specific work (Author Year, §Section or Table N)
  - Methodological argument: name the specific inferential claim and its study-design basis
  - Statistical result: name the statistic and its paper location (e.g., F(2,118)=14.3, App. C)

Invalid evidence forms (do NOT overcome inertia -- do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Phase 7 Check 2b enforces category presence; Check 2c enforces instance specificity.
A P1 no-change rationale naming a valid category but no traceable instance fails Check 2c.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max. State the
scientific rationale. Do not over-argue.
Violation: a no-change response longer than 1 paragraph reads as defensive.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max.
Violation: a multi-paragraph scope response invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
Violation: combative or dismissive phrasing may cause rejection independent of scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns.
Violation: a merged exchange will be returned by the editorial office for revision.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.
Violation: non-integer frontmatter values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.
Violation: fabricated reviewer comments constitute academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change -- rationale]

Violation: any block missing REVIEWER SAID, AUTHOR RESPONDS, or MANUSCRIPT OUTCOME
is structurally incomplete and must be rewritten.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern.

**Paragraph 1**: Name 3-4 changes this revision will make.
**Paragraph 2**: Name areas of respectful disagreement now. If none: state explicitly.

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):

> **Forward-annotation -- downstream Phase 7 gate constraints visible now**:
> - Check 2c (entity-type): the evidence instance you name must be a concrete entity -- a
>   cited paper or author (Author Year, not §N of this manuscript), a specific statistic with
>   its paper location, or a named methodological principle with its study-design basis.
>   A location reference alone ("App. B", "§3.2", "Table 4") fails Check 2c even when the
>   category label is correctly named.
> - Check 4 Part C (anti-deferral): if this pre-commitment is later SHIFTED to PRESSURE-DRIVEN
>   in Phase 6a, a binary decision (REINSTATE or NO REINSTATE with a one-sentence rationale)
>   must be recorded in Phase 6a before write. Deferring the decision to the cover letter
>   fails Part C regardless of how clearly it is stated there.

For each P1 concern anticipated to result in no-change:

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy -- no-change because:
  statistical result -- power analysis (80% power at N=120, primary outcome, App. B Table B1).

  Example: P1-NC: Reviewer 3 request to adopt Chen 2018 framework -- no-change because:
  methodological argument -- Chen 2018 assumes panel data; cross-sectional design (§2.1)
  makes that framework inapplicable by structural assumption.

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide (verify scope/framing/methodological in Phase 3.5):
factual / methodological / scope / framing / statistical / presentation

Severity: P1 (blocks) / P2 (moderate) / P3 (editorial). Sort P1 first, then P2, then P3.

---

## PHASE 3.5 -- TYPE AUDIT

For every scope, framing, or methodological assignment:
  R-[NN] typed [type] not [most likely alternative] because: [specific distinguishing reason]

Correct Phase 3 table before proceeding if any assignment looks wrong.

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every P2 or P3 assignment:
  R-[NN] assigned [P2/P3] not P1 because: [specific paper-based or venue-based reason]

Correct Phase 3 table before proceeding. All P2/P3 assignments require entries.

---

## PHASE 4 -- WEAKNESS FORECAST

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [specific mechanism] |
| F-02 | [R-NN] | concedes too much | [reviewer move or pressure] |
| F-03 | [R-NN] | too brief | [structural reason] |

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

--- P1 CONCERNS --- P2 CONCERNS --- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[FLAGGED: [F-0N] if applicable]

**REVIEWER SAID:** > "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
  [type-specific template per RULE-8 type guide]

**MANUSCRIPT OUTCOME:**
[Section + specific change.]
[Or for P1 no-change -- forward-annotation from Check 2c and Check 6b:
  "No change -- [evidence category: named entity-type referent (Author Year §N for literature;
  statistic + paper location for statistical; named principle + study-design basis for
  methodological)]"
  Check 2c warning: "Prior literature supports our approach" fails -- the cited paper or
  author must be named; a location reference alone (§N, App. C) does not satisfy this check.
  Check 6b warning: if Paragraph 1 currently claims a change citing this R-ID, that claim
  will fail Check 6b. Resolve now -- update Paragraph 1 or reconsider the no-change decision.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
- Update Paragraph 1 with parenthetical R-ID references for each named change.
- Update Paragraph 2 for any shift in disagreement framing.

> **Forward-annotation -- Check 6b failure condition**:
> Before filling the audit table, scan Paragraph 1 for any change claim that references an
> R-ID whose Phase 5 MANUSCRIPT OUTCOME is "No change." Each such claim is a structural
> contradiction -- the cover letter asserts a change the manuscript does not contain.
> Resolve it now:
>   (a) Correct the MANUSCRIPT OUTCOME if the change was actually made but recorded incorrectly.
>   (b) Revise Paragraph 1 to remove or rephrase the false change claim.
> Do not carry this forward to Phase 7 -- it is faster and cleaner to fix here where both
> Paragraph 1 and Phase 5 outcomes are visible simultaneously.

- P1 pre-commitment audit with SHIFTED classification and decision closure:

  | P1-NC | Evidence category + instance | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|------------------------------|-----------------|----------------|----------------|----------|-----------|

  HELD: pre-committed no-change maintained; evidence form and instance in Phase 5.

  SHIFTED -- classify:
    PRESSURE-DRIVEN: Decision required: REINSTATE or NO REINSTATE with one-sentence rationale.
    EVIDENCE-DRIVEN: Decision required: CONFIRM CHANGE: [specific evidence].
    Re-examination: update Paragraph 2 if resolved disagreement was listed there.

**6b. Forecast validation**: FLAGGED exchanges first, then unflagged.

| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|

**6c. Three exchanges to strengthen**:
1. [R-NN] -- too defensive
2. [R-NN] -- concedes too much
3. [R-NN] -- too brief

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing the artifact. Each check must PASS. Any FAIL stops the write.

**Check 1 -- Decomposition completeness**:
CHECK: [n REVIEWER SAID blocks] vs [n R-IDs in Phase 3] -- PASS / FAIL
If FAIL: identify missing R-IDs and write the missing exchanges before proceeding.

**Check 2a -- Outcome resolution completeness**:
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL: identify unresolved outcomes and complete them before proceeding.

**Check 2b -- P1 no-change evidence form category presence**:
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL: rewrite MANUSCRIPT OUTCOME rationale to name the evidence form before proceeding.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL: add the specific traceable instance before proceeding. Note: the Phase 5 MANUSCRIPT
OUTCOME forward-annotation warned of this constraint -- a well-formed Phase 5 entry should
not fail here. If it does, the Phase 5 forward-annotation was not followed.

**Check 3 -- Cover letter structure**:
CHECK: Paragraph 1 (changes with R-IDs) and Paragraph 2 (disagreement or none) -- PASS / FAIL
If FAIL: identify which paragraph is missing or malformed and repair before proceeding.

**Check 4 -- Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: [n FLAGGED exchange headers] vs [n validated rows in Phase 6b] -- PASS / FAIL
Part B: [n SHIFTED entries] vs [n classified + re-examined] -- PASS / FAIL
Part C: [n PRESSURE-DRIVEN entries] vs [n with REINSTATE or NO REINSTATE + rationale] -- PASS / FAIL
Note on Part C: Phase 2 forward-annotation warned that the decision must be recorded in
Phase 6a -- deferral to the cover letter fails Part C. An entry failing Part C missed the
constraint at its earliest visible point.
If any part fails: complete the missing element before proceeding.

**Check 5 -- Frontmatter integer verification**:
Compute reviewer_count, concerns_addressed, manuscript_changes, no_change_responses.
CHECK: all four values are integers, sum consistent -- PASS / FAIL
If FAIL: recompute from Phase 5 outcomes and correct frontmatter values.

**Check 6 -- Cover letter Paragraph 1 traceability**:
CHECK: list each Paragraph 1 claim and its R-ID reference(s) -- PASS / FAIL per claim
If FAIL: add R-ID references or remove claims with no R-ID mapping before proceeding.

**Check 6b -- Cover letter claim-outcome consistency**:
For every Paragraph 1 claim that passed Check 6, verify each referenced R-ID resolves to a
CHANGE MANUSCRIPT OUTCOME. Note: Phase 6a reconciliation carried a forward-annotation for
this constraint -- a well-formed Phase 6a should have caught it before Phase 7 runs.
CHECK: list each Paragraph 1 claim, R-ID references, and each R-ID MANUSCRIPT OUTCOME type
(CHANGE or NO CHANGE) -- PASS / FAIL per claim
If FAIL: (a) correct MANUSCRIPT OUTCOME if change was actually made; or
(b) revise Paragraph 1 to remove the false change claim.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-04 — Entity-Type Column + Branched Repair Protocols

**Axis**: J+K combined — C-31 entity-type column in Phase 6a + C-32 branched repair protocols in Phase 7
**Hypothesis**: Entity-type column propagation (J) and branched repair protocols (K) are structurally independent improvements that reinforce each other: the column forces entity-type resolution during authoring, and the repair protocols give the executor a directed path when a gate detects a failure that the column was meant to prevent.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition, naming evidence by category AND specific instance. Phase 3.5
audits ambiguous type assignments. Phase 3.6 audits P2/P3 severity assignments. Forecast
rows carry forward as flags into exchange headers. The amendment pass validates FLAGGED
exchanges first, audits P1 pre-commitments with SHIFTED classification -- PRESSURE-DRIVEN
entries close to REINSTATE / NO REINSTATE with a named rationale; EVIDENCE-DRIVEN entries
record CONFIRM CHANGE with a named evidence sentence -- then checks for unflagged failures.
Phase 6a reconciliation requires each Paragraph 1 change claim to trace to at least one R-ID
and carries an entity-type referent column in the P1 audit table -- the concrete entity must
be named during reconciliation, not inserted at gate time. Phase 7 structural completion gate
runs ten checks; each failing check includes a branched (a)/(b) repair protocol before write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default -- the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia -- use at least one; name the category AND
a specific traceable instance within the category):
  - Prior literature: cite a specific work (Author Year, §Section or Table N)
  - Methodological argument: name the specific inferential claim and its study-design basis
  - Statistical result: name the statistic and its paper location (e.g., F(2,118)=14.3, App. C)

Invalid evidence forms (do NOT overcome inertia -- do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Check 2b enforces category presence; Check 2c enforces instance specificity.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max.
Violation: a no-change response longer than 1 paragraph reads as defensive.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max.
Violation: a multi-paragraph scope response invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
Violation: combative or dismissive phrasing may cause rejection.

**RULE-5 (Decomposition rule)**: One concern = one exchange.
Violation: a merged exchange will be returned by the editorial office.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers.
Violation: non-integer frontmatter values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error.
Violation: fabricated reviewer comments constitute academic misconduct.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [section + change] or [No change -- rationale]

Violation: any block missing REVIEWER SAID, AUTHOR RESPONDS, or MANUSCRIPT OUTCOME
is structurally incomplete and must be rewritten.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern.

**Paragraph 1**: Name 3-4 changes this revision will make.
**Paragraph 2**: Name areas of respectful disagreement. If none: state explicitly.

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy -- no-change because:
  statistical result -- power analysis (80% power at N=120, primary outcome, App. B Table B1).

  Example: P1-NC: Reviewer 3 request to adopt Chen 2018 framework -- no-change because:
  methodological argument -- Chen 2018 assumes panel data; cross-sectional design (§2.1)
  makes that framework inapplicable by structural assumption.

These pre-commitments are audited in Phase 6a. PRESSURE-DRIVEN SHIFTED entries require
REINSTATE or NO REINSTATE. EVIDENCE-DRIVEN SHIFTED entries require CONFIRM CHANGE.

---

## PHASE 3 -- CONCERN DECOMPOSITION

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type taxonomy (verify scope/framing/methodological in Phase 3.5):
factual / methodological / scope / framing / statistical / presentation

Severity: P1 (blocks) / P2 (moderate) / P3 (editorial). Sort P1, P2, P3.

---

## PHASE 3.5 -- TYPE AUDIT

For scope, framing, or methodological:
  R-[NN] typed [type] not [alternative] because: [specific distinguishing reason]

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every P2 or P3:
  R-[NN] assigned [P2/P3] not P1 because: [paper-based or venue-based reason]

---

## PHASE 4 -- WEAKNESS FORECAST

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [specific mechanism] |
| F-02 | [R-NN] | concedes too much | [reviewer move] |
| F-03 | [R-NN] | too brief | [structural reason] |

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

--- P1 CONCERNS --- P2 CONCERNS --- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [summary]**
[FLAGGED: [F-0N] if applicable]

**REVIEWER SAID:** > "[quote]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
  [type-specific template]

**MANUSCRIPT OUTCOME:**
[Section + change. Or: No change -- [valid RULE-1 category: Author Year §N / named statistic /
named principle]. RULE-2. RULE-3 if scope.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
- Update Paragraph 1 with parenthetical R-ID references for each named change.
- Update Paragraph 2 for any shift in disagreement framing.
- P1 pre-commitment audit:

  | P1-NC | Evidence category | Entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|-------------------|----------------------|-----------------|----------------|----------------|----------|-----------|

  **Entity-type referent column**: name the concrete entity:
  - Prior literature: the cited paper or author (Author Year) -- not a section of this manuscript
  - Statistical result: the specific statistic and its paper location
  - Methodological argument: the named inferential principle and its study-design basis
  An entry without a named entity-type referent fails Phase 6a. The referent must appear
  here -- it cannot be inserted at Phase 7 Check 2c as a last-second addition.

  HELD: no-change maintained; evidence form and instance in Phase 5.

  SHIFTED -- classify and re-examine:
    PRESSURE-DRIVEN: REINSTATE or NO REINSTATE with one-sentence rationale.
    EVIDENCE-DRIVEN: CONFIRM CHANGE: [specific evidence]. Update Paragraph 2 if needed.

**6b. Forecast validation**: FLAGGED first, then unflagged.
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|

**6c. Three exchanges to strengthen** (FLAGGED priority):
1. [R-NN] -- too defensive
2. [R-NN] -- concedes too much
3. [R-NN] -- too brief

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing. Each check must PASS. Any FAIL stops the write.

**Check 1 -- Decomposition completeness**:
CHECK: [n REVIEWER SAID blocks] vs [n R-IDs in Phase 3] -- PASS / FAIL
If FAIL:
  (a) Concern decomposed but exchange not written: write the missing exchange before proceeding.
  (b) Two concerns merged into one block: split into separate exchanges before proceeding.

**Check 2a -- Outcome resolution completeness**:
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL:
  (a) Change made but MANUSCRIPT OUTCOME is a placeholder: write section + specific change.
  (b) Outcome genuinely unresolved: determine and record outcome using Phase 2 baseline.

**Check 2b -- P1 no-change evidence form category presence**:
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL:
  (a) Valid form present in AUTHOR RESPONDS but absent from MANUSCRIPT OUTCOME: move it.
  (b) No valid form anywhere in the exchange: revise to introduce one.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL:
  (a) Specific entity in exchange body but absent from MANUSCRIPT OUTCOME: move it.
  (b) No concrete entity named anywhere: revise to name one. Note: Phase 6a entity-type
      column should have caught this -- update the Phase 6a table entry too.

**Check 3 -- Cover letter structure**:
CHECK: Paragraph 1 (changes with R-IDs) and Paragraph 2 (disagreement or none) -- PASS / FAIL
If FAIL:
  (a) Paragraph malformed (missing R-ID references): add parenthetical R-IDs.
  (b) Paragraph missing: draft from Phase 2 pre-commitments and Phase 5 outcomes.

**Check 4 -- Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: [n FLAGGED headers] vs [n validated rows in Phase 6b] -- PASS / FAIL
If Part A fails:
  (a) Forecast rows without validation: complete Phase 6b FLAGGED validation.
  (b) Count mismatch: identify unvalidated row and add it.

Part B: [n SHIFTED entries] vs [n classified + re-examined] -- PASS / FAIL
If Part B fails:
  (a) SHIFTED without classification: apply PRESSURE-DRIVEN or EVIDENCE-DRIVEN.
  (b) Classified but no re-examination note: write the re-examination note.

Part C: [n PRESSURE-DRIVEN] vs [n with REINSTATE or NO REINSTATE + rationale] -- PASS / FAIL
If Part C fails:
  (a) PRESSURE-DRIVEN with re-examination but no binary decision: state REINSTATE or
      NO REINSTATE with a one-sentence rationale.
  (b) EVIDENCE-DRIVEN without CONFIRM CHANGE: name the evidence and record CONFIRM CHANGE.

**Check 5 -- Frontmatter integer verification**:
CHECK: reviewer_count, concerns_addressed, manuscript_changes, no_change_responses -- PASS / FAIL
If FAIL:
  (a) String placeholders: replace each with computed integer.
  (b) Inconsistent totals: recount from Phase 5 and correct all four values.

**Check 6 -- Cover letter Paragraph 1 traceability**:
CHECK: list each Paragraph 1 claim and its R-ID reference(s) -- PASS / FAIL per claim
If FAIL:
  (a) R-ID exists but was omitted: add the parenthetical reference.
  (b) No R-ID maps to the claim: remove or rephrase to reflect a reviewer-driven change.

**Check 6b -- Cover letter claim-outcome consistency**:
CHECK: list each Paragraph 1 claim, R-ID references, and R-ID MANUSCRIPT OUTCOME type
(CHANGE or NO CHANGE) -- PASS / FAIL per claim
If FAIL:
  (a) Change made but Phase 5 records no change incorrectly: correct MANUSCRIPT OUTCOME.
  (b) Change not made: revise Paragraph 1 to remove or rephrase the false claim.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-05 — Full Integration (J+K+L)

**Axis**: J+K+L — entity-type column + branched repair protocols + upstream forward-annotations
**Hypothesis**: The three axes address three structurally distinct failure windows: J closes the last-second-insertion loophole at Phase 6a authoring time; K converts Phase 7 stop signs into decision forks; L surfaces constraint visibility at the upstream decision point before authoring begins. Together they create three enforcement surfaces per major constraint class rather than one.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition, naming evidence by category AND specific instance; forward-
annotated Phase 7 gate constraints appear at the Phase 2 commitment surface. Phase 3.5 audits
ambiguous type assignments. Phase 3.6 audits P2/P3 severity assignments. Forecast rows carry
forward as flags into exchange headers; Phase 5 MANUSCRIPT OUTCOME template for P1 no-change
carries forward-annotated failure conditions from Check 2c and Check 6b. The amendment pass
validates FLAGGED exchanges first, audits P1 pre-commitments with SHIFTED classification --
PRESSURE-DRIVEN entries close to REINSTATE / NO REINSTATE with a named rationale; EVIDENCE-
DRIVEN entries record CONFIRM CHANGE with a named evidence sentence -- then checks for
unflagged failures; Phase 6a carries an entity-type referent column in the audit table and a
forward-annotated Check 6b failure condition. Phase 7 structural completion gate runs ten
checks; each failing check includes a branched (a)/(b) repair protocol before artifact write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default -- the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia -- use at least one; name the category AND
a specific traceable instance within the category):
  - Prior literature: cite a specific work (Author Year, §Section or Table N)
  - Methodological argument: name the specific inferential claim and its study-design basis
  - Statistical result: name the statistic and its paper location (e.g., F(2,118)=14.3, App. C)

Invalid evidence forms (do NOT overcome inertia -- do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Check 2b enforces category presence; Check 2c enforces instance specificity.
A P1 no-change rationale naming a valid category but no traceable instance fails Check 2c --
the category label alone does not satisfy RULE-1 at editorial submission standard.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max. State the
scientific rationale. Do not over-argue.
Violation: a no-change response longer than 1 paragraph reads as defensive.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max. State the
paper's claim space. Do not argue or defend. Close.
Violation: a multi-paragraph scope response invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only. No
response is combative, dismissive, or sycophantic. Professional, non-defensive, grateful.
Violation: combative or dismissive phrasing may cause rejection independent of scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns,
even if they appear in the same reviewer paragraph.
Violation: a merged exchange will be returned by the editorial office for revision.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.
Violation: non-integer frontmatter values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.
Violation: fabricated reviewer comments constitute academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change -- rationale]

Violation: any block missing REVIEWER SAID, AUTHOR RESPONDS, or MANUSCRIPT OUTCOME
is structurally incomplete and must be rewritten. RULE-5 and RULE-8 together enforce
atomicity: a merged concern cannot produce a valid REVIEWER SAID block.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: the hardest individual
decisions are committed before Phase 5 drafting pressure can erode them. SHIFTED entries
in Phase 6a require classification; PRESSURE-DRIVEN entries close to REINSTATE or NO
REINSTATE with a named rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):

> **Forward-annotation -- downstream Phase 7 gate constraints visible now**:
> - Check 2c (entity-type): the evidence instance you name must be a concrete entity -- a
>   cited paper or author (Author Year, not §N of this manuscript), a specific statistic with
>   its paper location, or a named methodological principle with its study-design basis.
>   A location reference alone ("App. B", "§3.2", "Table 4") fails Check 2c even when the
>   category label is correctly named.
> - Check 4 Part C (anti-deferral): if this pre-commitment is later SHIFTED to PRESSURE-DRIVEN
>   in Phase 6a, a binary decision (REINSTATE or NO REINSTATE with a one-sentence rationale)
>   must be recorded in Phase 6a before write. The decision cannot be deferred to the cover
>   letter -- deferral fails Part C regardless of how clearly it is stated there.

For each P1 concern anticipated to result in no-change:

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy -- no-change because:
  statistical result -- power analysis (80% power at N=120, primary outcome, App. B Table B1)
  showed adequacy before data collection began.
  Entity: App. B Table B1 power analysis result (N=120, power=0.80) -- NOT "App. B alone".

  Example: P1-NC: Reviewer 3 request to adopt Chen 2018 framework -- no-change because:
  methodological argument -- Chen 2018 assumes panel data; cross-sectional design (§2.1,
  single observation per participant) makes that framework inapplicable by structural assumption.
  Entity: Chen 2018 panel-data independence assumption (named principle) -- NOT "§2.1 alone".

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide (verify scope/framing/methodological in Phase 3.5):

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake | "Framing" -- factual = paper error; framing = reviewer misread |
| methodological | Existing experiment or analysis design is flawed | "Scope" -- methodological = current work wrong; scope = wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" -- scope = paper doesn't claim this; methodological = tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" -- framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis | "Methodological" -- statistical = analysis layer; methodological = design |
| presentation | Clarity, structure, notation, language | Safe fallback for no scientific content impact |

Severity: P1 (blocks) / P2 (moderate) / P3 (editorial). Sort P1 first, then P2, then P3.

---

## PHASE 3.5 -- TYPE AUDIT

For every scope, framing, or methodological assignment:
  R-[NN] typed [type] not [most likely alternative] because:
  [specific distinguishing reason -- not a restatement of the type definition]

Correct Phase 3 table before proceeding if any assignment looks wrong.

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every P2 or P3 assignment:
  R-[NN] assigned [P2/P3] not P1 because:
  [specific paper-based or venue-based reason this concern does not block acceptance]

Correct Phase 3 table before proceeding. All P2/P3 assignments require entries.

---

## PHASE 4 -- WEAKNESS FORECAST

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [specific mechanism causing over-explanation] |
| F-02 | [R-NN] | concedes too much | [reviewer move or pressure causing over-concession] |
| F-03 | [R-NN] | too brief | [structural reason this concern gets under-addressed] |

Rows carry forward as flags into Phase 5 headers.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS (RULE-1 applies -- no-change requires valid evidence form category AND
specific traceable instance; see Phase 2 P1-NC pre-commitments) ---
--- P2 CONCERNS (address or explain; severity justified in Phase 3.6) ---
--- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: "| FLAGGED: [F-0N] [predicted failure mode -- resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."

  methodological: "We agree that [aspect]. [Scientific justification or fix.] §N."

  scope:          [2-3 sentences. RULE-3.]

  framing:        "The paper claims [exact claim]. The reviewer may be reading this as
                  [misread]. We have added [clarifying language] to §N."

  statistical:    "[Added the analysis / explained the constraint.] [Result or rationale.]"

  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change.]
[Or for P1 no-change:
  "No change -- [evidence category: Entity: named entity-type referent (Author Year §N for
  literature; statistic + paper location for statistical; named principle + study-design
  basis for methodological)]"
  Forward-annotation from Check 2c: naming only a location (§3.2, App. C) without a named
  entity fails Check 2c -- a cited paper or author, specific statistic, or named principle
  is required here, not a self-reference to this manuscript's sections.
  Forward-annotation from Check 6b: if Paragraph 1 currently claims a change citing this
  R-ID, that claim will fail Check 6b. Resolve now -- update Paragraph 1 or reconsider the
  no-change decision before continuing past this exchange.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 to reflect changes actually made. Each named change must include
  parenthetical R-ID references: "We [change] (R-NN)" or "We [change] (R-NN, R-NN)".
  An unnamed change claim will fail Phase 7 Check 6.
- Update Paragraph 2 for any shift in disagreement framing.

> **Forward-annotation -- Check 6b failure condition**:
> Before filling the audit table, scan Paragraph 1 for any change claim that references an
> R-ID whose Phase 5 MANUSCRIPT OUTCOME is "No change." Each such claim is a structural
> contradiction -- the cover letter asserts a change the manuscript does not contain.
> Resolve it now, during Phase 6a reconciliation:
>   (a) Correct the MANUSCRIPT OUTCOME if the change was actually made and Phase 5 recorded
>       it incorrectly.
>   (b) Revise Paragraph 1 to remove or rephrase the false change claim.
> Do not carry this forward -- Check 6b will catch it in Phase 7, but it is faster to fix
> here where both Paragraph 1 and Phase 5 outcomes are visible simultaneously.

- P1 pre-commitment audit with entity-type referent column, SHIFTED classification, and
  decision closure:

  | P1-NC | Evidence category | Entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|-------------------|----------------------|-----------------|----------------|----------------|----------|-----------|

  **Entity-type referent column** -- fill during reconciliation, not at Phase 7:
  - Prior literature: the cited paper or author (Author Year) -- an external cited work,
    not a section of this manuscript
  - Statistical result: the specific statistic and its paper location (e.g., F(2,118)=14.3,
    App. C Table 3)
  - Methodological argument: the named inferential principle and its study-design basis
    (e.g., "independence assumption in panel designs, Chen 2018 §2")
  An entry with an empty or location-only entity-type referent fails Phase 6a. The referent
  must be present here -- it cannot be inserted at Phase 7 Check 2c as a last-second addition.

  HELD: pre-committed no-change maintained; named evidence form and instance used in Phase 5.

  SHIFTED: position changed during drafting. Classify and re-examine:

    PRESSURE-DRIVEN: author yielded under rhetorical or emotional argument weight without
    specific new scientific evidence. Original position may still be scientifically correct.
    Decision required (choose one, state a one-sentence rationale):
      REINSTATE: [the RULE-1 evidence category and instance that was valid before Phase 5
      and remains valid -- the change should be reversed]
      NO REINSTATE: [the specific non-scientific improvement (clarity, reduced ambiguity)
      achieved by the change -- confirm the scientific claim is unaffected]

    EVIDENCE-DRIVEN: author encountered specific evidence in Phase 5 (a named result,
    calculation, or argument not anticipated in Phase 2) that genuinely changed the assessment.
    Decision required: CONFIRM CHANGE: [name the specific evidence -- one sentence].
    Re-examination: Does Paragraph 2 accurately reflect the resolved disagreement? Update
    if the concern was listed as a standing disagreement and the shift resolved it.

**6b. Forecast validation**: Validate FLAGGED exchanges first, then check unflagged exchanges.

FLAGGED exchanges:
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|
| F-01 | | too defensive | | |
| F-02 | | concedes too much | | |
| F-03 | | too brief | | |

Unflagged failures: name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen** (FLAGGED exchanges take priority):
1. [R-NN] -- too defensive: [rewrite AUTHOR RESPONDS opening]
2. [R-NN] -- concedes too much: [what to hold; why the concession went too far]
3. [R-NN] -- too brief: [what is understated; what to add]

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing the artifact. Each check must PASS. Any FAIL stops
the write -- fix the failing check and re-run before proceeding.

**Check 1 -- Decomposition completeness**:
Count REVIEWER SAID blocks in Phase 5. Count R-ID entries in Phase 3 table.
PASS if counts match. FAIL if Phase 5 has fewer REVIEWER SAID blocks than Phase 3 R-IDs.
CHECK: [n REVIEWER SAID blocks in Phase 5] vs [n R-IDs in Phase 3] -- PASS / FAIL
If FAIL:
  (a) Concern in Phase 3 with no exchange written: write the missing exchange in severity
      order before proceeding.
  (b) Two concerns merged into one REVIEWER SAID block: split into separate exchanges,
      each with its own REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME, before proceeding.

**Check 2a -- Outcome resolution completeness**:
Every MANUSCRIPT OUTCOME must be "[Section N]: [specific change]" or "No change -- [rationale]".
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL:
  (a) Change made but MANUSCRIPT OUTCOME is a placeholder or TBD: write the section
      identifier and specific change description before proceeding.
  (b) Outcome genuinely unresolved (no decision made): use Phase 2 pre-commitments as
      baseline -- record a no-change rationale or commit to a change before proceeding.

**Check 2b -- P1 no-change evidence form category presence**:
For every P1 MANUSCRIPT OUTCOME that is "No change," verify the rationale names at least
one valid RULE-1 evidence form by category (prior literature / methodological argument /
statistical result).
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL:
  (a) Valid evidence form in AUTHOR RESPONDS but absent from MANUSCRIPT OUTCOME: move the
      category name into the MANUSCRIPT OUTCOME rationale before proceeding.
  (b) No valid evidence form anywhere in the exchange: revise to introduce prior literature,
      methodological argument, or statistical result before proceeding.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
For every P1 MANUSCRIPT OUTCOME that passed Check 2b, verify a specific traceable instance:
Author Year + locator (literature); named statistic + location (statistical); named principle
+ study-design basis (methodological).
"Prior literature supports our approach" -- fails (category present, no instance).
"Prior literature (Jones 2019, §3.2) validates this approach in cross-sectional populations"
-- passes (category + entity + locator).
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL:
  (a) Specific entity exists in exchange body but absent from MANUSCRIPT OUTCOME: move it.
  (b) No concrete entity named anywhere: revise the exchange to name a specific entity. Note:
      Phase 6a entity-type column and Phase 5 MANUSCRIPT OUTCOME forward-annotation both
      warned of this constraint -- update Phase 6a table to reflect the correction.

**Check 3 -- Cover letter structure**:
Phase 2 (updated in 6a) contains Paragraph 1 (3-4 changes with R-ID references) and
Paragraph 2 (disagreement framing or explicit statement of none).
CHECK: PASS / FAIL
If FAIL:
  (a) Paragraph present but malformed (changes lack R-ID references): add parenthetical
      R-ID references to each change claim before proceeding.
  (b) Paragraph missing entirely: draft from Phase 2 pre-commitments and Phase 5 outcomes.

**Check 4 -- Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: Every FLAGGED exchange must appear as a validated row in Phase 6b.
CHECK: [n FLAGGED exchange headers] vs [n validated rows in Phase 6b] -- PASS / FAIL
If Part A fails:
  (a) Forecast rows without validation: complete Phase 6b FLAGGED validation for each.
  (b) Validation entries written but count mismatches: identify unvalidated row and add it.

Part B: Every SHIFTED entry must have classification and completed re-examination note.
CHECK: [n SHIFTED entries] vs [n classified + re-examined] -- PASS / FAIL
If Part B fails:
  (a) SHIFTED entries with no classification: apply PRESSURE-DRIVEN or EVIDENCE-DRIVEN.
  (b) Classified but re-examination note absent: write the note for each classified entry.

Part C: Every PRESSURE-DRIVEN entry must have REINSTATE or NO REINSTATE with rationale.
Note: Phase 2 forward-annotation warned that this decision must be recorded in Phase 6a --
an entry failing Part C missed that constraint at its earliest visible point.
CHECK: [n PRESSURE-DRIVEN entries] vs [n with named binary decision + rationale] -- PASS / FAIL
If Part C fails:
  (a) PRESSURE-DRIVEN with re-examination but no binary decision: state REINSTATE or NO
      REINSTATE with a one-sentence rationale naming what holds or was conceded.
  (b) EVIDENCE-DRIVEN without CONFIRM CHANGE: name the specific evidence and record CONFIRM
      CHANGE with a one-sentence evidence statement before proceeding.

**Check 5 -- Frontmatter integer verification**:
Compute from Phase 5 outcomes:
- reviewer_count: distinct reviewers in Phase 3
- concerns_addressed: total R-IDs in Phase 3
- manuscript_changes: R-IDs with CHANGE MANUSCRIPT OUTCOME
- no_change_responses: R-IDs with no-change MANUSCRIPT OUTCOME
CHECK: all four are integers, manuscript_changes + no_change_responses = concerns_addressed
-- PASS / FAIL
If FAIL:
  (a) String placeholders in frontmatter: replace each with the computed integer.
  (b) Inconsistent totals: recount from Phase 5 outcomes and correct all four values.

**Check 6 -- Cover letter Paragraph 1 traceability**:
Every change claim in Paragraph 1 (updated in 6a) must include at least one parenthetical
R-ID reference.
CHECK: list each Paragraph 1 claim and its R-ID reference(s) -- PASS / FAIL per claim
If FAIL:
  (a) R-ID exists but was omitted from parenthetical: add it before proceeding.
  (b) No R-ID maps to the claim (not driven by any reviewer concern): remove the claim or
      rephrase to reflect an actual reviewer-driven change before proceeding.

**Check 6b -- Cover letter claim-outcome consistency**:
For every Paragraph 1 claim that passed Check 6, verify each referenced R-ID resolves to a
CHANGE MANUSCRIPT OUTCOME (not "No change"). A claim asserting "we changed X in response to
R-NN" while R-NN records no-change is a structural contradiction.
Note: Phase 6a reconciliation carried a forward-annotation for this constraint -- a
well-formed Phase 6a should have resolved contradictions before Phase 7 runs.
CHECK: list each Paragraph 1 claim, R-ID references, and each R-ID MANUSCRIPT OUTCOME type
(CHANGE or NO CHANGE) -- PASS / FAIL per claim
If FAIL:
  (a) Change was actually made but Phase 5 MANUSCRIPT OUTCOME records no change incorrectly:
      correct the MANUSCRIPT OUTCOME for that R-ID before proceeding.
  (b) Change was not made: revise Paragraph 1 to remove or rephrase the false claim. This is
      the only check that can detect cover-letter/manuscript-outcome divergence -- no prior
      check can catch a traced R-ID whose outcome type is no-change.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```
