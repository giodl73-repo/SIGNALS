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
PRESSURE-DRIVEN entries close to a binary (REINSTATE / CONFIRM CHANGE) with a named rationale
-- then checks for unflagged failures. Phase 6a reconciliation requires each Paragraph 1 change
claim to trace to at least one R-ID. Phase 7 structural completion gate verifies P1 no-change
evidence specificity, PRESSURE-DRIVEN decision closure, severity downgrade audit coverage,
cover letter traceability, and count-based integrity before artifact write.

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
in Phase 6a require classification; PRESSURE-DRIVEN entries close to a named binary decision.

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
SHIFTED entries require classification. PRESSURE-DRIVEN entries require a named binary
decision (REINSTATE / CONFIRM CHANGE) -- see Phase 6a protocol.

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

Invalid: "R-05 assigned P2 not P1 because: the reviewer asked about sensitivity analysis."
(Describes the concern, does not state why it does not block acceptance.)

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
- P1 pre-commitment audit with SHIFTED classification and decision closure:

  | P1-NC | Evidence category + instance | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|------------------------------|-----------------|----------------|----------------|----------|-----------|

  HELD: pre-committed no-change was maintained; named evidence form and instance used in
  Phase 5. No re-examination required.

  SHIFTED: position changed during drafting. Classify and re-examine:

    PRESSURE-DRIVEN: author yielded under rhetorical or emotional argument weight without
    encountering specific new scientific evidence. The original no-change position may still
    be scientifically correct.
    Decision required (choose one and state a one-sentence rationale):
      REINSTATE: [name the specific RULE-1 evidence category and instance that was valid
      before Phase 5 and remains valid -- the change should be reversed]
      CONFIRM CHANGE: [name the specific non-scientific improvement achieved by the change
      (clarity, presentation, reduced ambiguity) -- confirm the scientific claim is unaffected]

    EVIDENCE-DRIVEN: author encountered specific evidence in Phase 5 (a named result,
    calculation, or argument not anticipated in Phase 2) that genuinely changed the assessment.
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
proceeding. A P1 no-change without a traceable instance does not meet editorial submission
standard regardless of how well-phrased the rationale is.

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
(PRESSURE-DRIVEN or EVIDENCE-DRIVEN) and a completed re-examination note. An entry with
only classification and no re-examination outcome fails Part B.
CHECK: [n SHIFTED entries] vs [n classified + re-examined entries] -- PASS / FAIL
Part C: Every PRESSURE-DRIVEN entry from Phase 6a must have a named binary decision
(REINSTATE or CONFIRM CHANGE) with a one-sentence rationale. An entry with classification
and a re-examination note but no named binary decision fails Part C. "Considered" alone fails.
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

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
