---
name: rhythm-rebuttal
description: "Generates formal response-to-reviewers letter. Takes reviewer comments, decomposes each concern, produces point-by-point professional responses with manuscript change commitments."
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 forward-annotations are individually labeled "Forward-annotation from
Check X:" self-contained modules -- Phase 2 carries a canonical "Forward-annotation from
Check 2c:" block (earliest Check 2c decision point) and a canonical "Forward-annotation from
Check 4 Part C:" block (earliest Check 4 Part C decision point). Phase 7 Check 2c back-
reference enumerates all three upstream sources by canonical label: Phase 2, Phase 5, and
Phase 6a. Every Phase 7 "If FAIL" repair block contains only the delegation line -- the
upstream canonical annotation is the sole repair surface; no inline (a)/(b) follows the
delegation. Phase 7 is a detection-and-delegation gate: it identifies the failure class,
names every upstream source that warned about it, and delegates all repair to the upstream
annotations.

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

> **Forward-annotation from Check 2c**: A P1 no-change evidence instance must name a
> concrete entity -- cited paper or author (Author Year, not a section of this manuscript),
> specific statistic with paper location, or named methodological principle with study-design
> basis. A location reference alone (App. B, section 3.2, Table 4) fails Check 2c even when
> the evidence category label is correctly named.
> Repair paths:
> (a) Name the concrete entity now: Author Year + locator (literature), named statistic +
>     paper location (statistical), named principle + study-design basis (methodological).
> (b) If no concrete entity can be named at Phase 2, reconsider whether this P1-NC is
>     defensible -- an unresolved entity at commitment time will fail Check 2c at write time.

> **Forward-annotation from Check 4 Part C**: If this pre-commitment is later SHIFTED to
> PRESSURE-DRIVEN in Phase 6a, a binding decision (REINSTATE or NO REINSTATE with a one-
> sentence rationale) must be recorded in Phase 6a before write. Deferring the decision to
> the cover letter fails Part C regardless of how clearly it appears there.
> Repair paths (if PRESSURE-DRIVEN shift occurs in Phase 6a):
> (a) If the original RULE-1 evidence remains scientifically valid: state REINSTATE with the
>     evidence category and specific instance in Phase 6a.
> (b) If the change improved clarity, presentation, or reduced ambiguity without affecting
>     the scientific claim: state NO REINSTATE with a one-sentence description of the
>     specific non-scientific improvement achieved.

For each P1 concern anticipated to result in no-change:

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

If none: "All P1 concerns will be addressed with manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.

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
[Section + specific change.]
[Or for P1 no-change:
  "No change -- [evidence category: named entity-type referent (Author Year + locator for
  literature; statistic + paper location for statistical; named principle + study-design
  basis for methodological)]"

  > **Forward-annotation from Check 2c**: A P1 no-change rationale naming a valid evidence
  > category without a specific traceable instance fails Check 2c -- naming a location alone
  > (section N, App. C) without the cited paper or author, specific statistic, or named
  > principle does not satisfy the entity-type referent requirement.
  > Repair paths:
  > (a) Add the specific traceable instance: Author Year + locator (literature), named
  >     statistic + paper location (statistical), named principle + study-design basis
  >     (methodological).
  > (b) If no specific instance exists, reclassify MANUSCRIPT OUTCOME to CHANGE and update
  >     Phase 2 Forward-annotation from Check 2c pre-commitment and Phase 6a table accordingly.

  > **Forward-annotation from Check 6b**: If Paragraph 1 currently claims a change citing
  > this R-ID, that claim will fail Check 6b -- a cover letter asserting "we changed X in
  > response to R-NN" paired with a No-change MANUSCRIPT OUTCOME is a structural contradiction.
  > Repair paths:
  > (a) Correct this MANUSCRIPT OUTCOME to CHANGE if the change was actually made but recorded
  >     incorrectly in this exchange.
  > (b) Revise Paragraph 1 to remove or rephrase the claim asserting a change against this
  >     R-ID before continuing past this exchange.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 with parenthetical R-ID references for each named change.
- Update Paragraph 2 for any shift in disagreement framing.

> **Forward-annotation from Check 6b**: A Paragraph 1 change claim asserting "we changed X
> in response to R-NN" while R-NN's Phase 5 MANUSCRIPT OUTCOME is "No change" is a structural
> contradiction -- the cover letter asserts a change the manuscript does not contain, and
> Check 6b will block the write.
> Repair paths:
> (a) Correct the MANUSCRIPT OUTCOME if the change was actually made and Phase 5 recorded
>     it incorrectly -- the claim is accurate, the record is wrong.
> (b) Revise Paragraph 1 to remove or rephrase the false change claim -- the manuscript
>     record is correct and the cover letter overstated.
> Resolve before filling the audit table -- it is faster to fix here where both artifacts
> are simultaneously visible.

- P1 pre-commitment audit with entity-type referent column, SHIFTED classification, and
  decision closure:

  | P1-NC | Evidence category | Entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|-------------------|----------------------|-----------------|----------------|----------------|----------|-----------|

  **Entity-type referent column** -- fill during reconciliation, not at Phase 7:
  - Prior literature: the cited paper or author (Author Year) -- not a section of this ms
  - Statistical result: the specific statistic and its paper location
  - Methodological argument: the named inferential principle and its study-design basis
  An entry with an empty or location-only entity-type referent fails Phase 6a. The referent
  must be present here -- it cannot be inserted at Phase 7 Check 2c as a last-second addition.

  HELD: pre-committed no-change maintained; named evidence form and instance used in Phase 5.

  SHIFTED: position changed during drafting. Classify and re-examine:

    PRESSURE-DRIVEN: author yielded under rhetorical weight without specific new scientific
    evidence. Decision required: REINSTATE or NO REINSTATE with one-sentence rationale.
    EVIDENCE-DRIVEN: author encountered specific named evidence not anticipated in Phase 2.
    Decision required: CONFIRM CHANGE: [specific evidence]. Update Paragraph 2 if needed.

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
For every P1 MANUSCRIPT OUTCOME that passed Check 2b, verify a specific traceable instance:
Author Year + locator (literature); named statistic + location (statistical); named principle
+ study-design basis (methodological).
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL:
  Back-reference: Phase 2 Forward-annotation from Check 2c warned that a traceable instance
  was required at the pre-commitment decision point, Phase 5 Forward-annotation from Check 2c
  warned that entity-type specificity was required at authoring time, and Phase 6a entity-type
  referent column required the entity to be named during mid-workflow reconciliation -- an
  entry failing Check 2c missed that constraint at its earliest visible points.
  Apply the Forward-annotation from Check 2c repair paths.

**Check 3 -- Cover letter structure**:
Phase 2 (updated in 6a) contains Paragraph 1 (3-4 changes with R-ID references) and
Paragraph 2 (disagreement framing or explicit statement of none).
CHECK: PASS / FAIL
If FAIL:
  (a) Paragraph present but malformed: add parenthetical R-ID references to each change claim.
  (b) Paragraph missing entirely: draft from Phase 2 pre-commitments and Phase 5 outcomes.

**Check 4 -- Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: Every FLAGGED exchange must appear as a validated row in Phase 6b.
CHECK: [n FLAGGED exchange headers] vs [n validated rows in Phase 6b] -- PASS / FAIL
If Part A fails:
  (a) Forecast rows without validation: complete Phase 6b FLAGGED validation for each.
  (b) Count mismatch: identify unvalidated row and add it.

Part B: Every SHIFTED entry must have classification and completed re-examination note.
CHECK: [n SHIFTED entries] vs [n classified + re-examined] -- PASS / FAIL
If Part B fails:
  (a) SHIFTED entries with no classification: apply PRESSURE-DRIVEN or EVIDENCE-DRIVEN.
  (b) Classified but note absent: write the re-examination note.

Part C: Every PRESSURE-DRIVEN entry must have REINSTATE or NO REINSTATE with rationale.
CHECK: [n PRESSURE-DRIVEN entries] vs [n with named binary decision + rationale] -- PASS / FAIL
If Part C fails:
  Back-reference: Phase 2 Forward-annotation from Check 4 Part C warned that PRESSURE-DRIVEN
  entries must commit REINSTATE or NO REINSTATE in Phase 6a before write -- an entry failing
  Part C missed that constraint at its earliest visible point.
  Apply the Forward-annotation from Check 4 Part C repair paths.

**Check 5 -- Frontmatter integer verification**:
Compute from Phase 5 outcomes:
- reviewer_count: distinct reviewers in Phase 3
- concerns_addressed: total R-IDs in Phase 3
- manuscript_changes: R-IDs with CHANGE MANUSCRIPT OUTCOME
- no_change_responses: R-IDs with no-change MANUSCRIPT OUTCOME
CHECK: all four are integers, manuscript_changes + no_change_responses = concerns_addressed
-- PASS / FAIL
If FAIL:
  (a) String placeholders: replace each with the computed integer.
  (b) Inconsistent totals: recount from Phase 5 and correct all four values.

**Check 6 -- Cover letter Paragraph 1 traceability**:
Every change claim in Paragraph 1 (updated in 6a) must include at least one parenthetical
R-ID reference.
CHECK: list each Paragraph 1 claim and its R-ID reference(s) -- PASS / FAIL per claim
If FAIL:
  (a) R-ID exists but was omitted: add parenthetical reference.
  (b) No R-ID maps to the claim: remove or rephrase.

**Check 6b -- Cover letter claim-outcome consistency**:
For every Paragraph 1 change claim that passed Check 6, verify each referenced R-ID resolves
to a CHANGE MANUSCRIPT OUTCOME (not "No change").
CHECK: list each Paragraph 1 claim, R-ID references, and each R-ID MANUSCRIPT OUTCOME type
(CHANGE or NO CHANGE) -- PASS / FAIL per claim
If FAIL:
  Back-reference: Phase 6a Forward-annotation from Check 6b warned that Paragraph 1 change
  claims referencing an R-ID must resolve to a CHANGE MANUSCRIPT OUTCOME, and Phase 5
  Forward-annotation from Check 6b warned of this constraint at the moment of authoring the
  MANUSCRIPT OUTCOME -- an entry failing Check 6b missed that constraint at its earliest
  visible points.
  Apply the Forward-annotation from Check 6b repair paths.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
