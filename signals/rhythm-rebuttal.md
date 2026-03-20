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
  - Prior literature: cite a specific work (Author Year, Section or Table N)
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

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max.
Violation: reads as defensive regardless of content quality.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max.
Violation: invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
Violation: may cause rejection independent of scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange.
Violation: editorial office will return it.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers.
Violation: fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error.
Violation: academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:
  REVIEWER SAID / AUTHOR RESPONDS [stance] / MANUSCRIPT OUTCOME
Violation: structurally incomplete -- rewrite.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: review artifact or reviewer comments. Read: original paper if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: hardest decisions committed
before Phase 5 drafting pressure can erode them. SHIFTED entries in Phase 6a require
classification; PRESSURE-DRIVEN entries close to REINSTATE or NO REINSTATE with a named
rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE.

**Paragraph 1**: Name 3-4 changes this revision will make.
**Paragraph 2**: Name areas of respectful disagreement. If none: state explicitly.

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

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every P2 or P3 assignment:
  R-[NN] assigned [P2/P3] not P1 because:
  [specific paper-based or venue-based reason this concern does not block acceptance]

---

## PHASE 4 -- WEAKNESS FORECAST

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [specific mechanism] |
| F-02 | [R-NN] | concedes too much | [reviewer move or pressure] |
| F-03 | [R-NN] | too brief | [structural reason] |

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS --- P2 CONCERNS --- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: "| FLAGGED: [F-0N] [predicted failure mode -- resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data.] We have updated [location]."
  methodological: "We agree that [aspect]. [Justification or fix.] N."
  scope:          [2-3 sentences. RULE-3.]
  framing:        "The paper claims [exact claim]. The reviewer may be reading this as
                  [misread]. We have added [clarifying language] to N."
  statistical:    "[Added analysis / explained constraint.] [Result or rationale.]"
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

| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|

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
CHECK: [n REVIEWER SAID blocks in Phase 5] vs [n R-IDs in Phase 3] -- PASS / FAIL
If FAIL:
  (a) Concern in Phase 3 with no exchange written: write the missing exchange in severity
      order before proceeding.
  (b) Two concerns merged into one REVIEWER SAID block: split into separate exchanges,
      each with its own REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME.

**Check 2a -- Outcome resolution completeness**:
Every MANUSCRIPT OUTCOME must be "[Section N]: [specific change]" or "No change -- [rationale]".
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL:
  (a) Change made but MANUSCRIPT OUTCOME is a placeholder: write section + change description.
  (b) Outcome genuinely unresolved: use Phase 2 pre-commitments as baseline and record.

**Check 2b -- P1 no-change evidence form category presence**:
For every P1 MANUSCRIPT OUTCOME that is "No change," verify the rationale names at least
one valid RULE-1 evidence form by category.
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL:
  (a) Valid form in AUTHOR RESPONDS but absent from MANUSCRIPT OUTCOME: move it.
  (b) No valid form anywhere: revise to introduce prior literature, methodological argument,
      or statistical result before proceeding.

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
